#!/usr/bin/env python3
"""
pdf_extract.py -- PDF → Markdown + Page Images for HELIOS paper notes.

For each PDF:
  1. Extracts full-page PNG images (for visual figure reference)
  2. Extracts text layer → clean Markdown file
  3. Writes a summary.md linking pages + text

Uses pypdfium2 (PDFium engine) only -- no ML, no cloud, no OCR models needed.
Text extraction works for digitally-created PDFs (APS, AIP journals etc.)

Requirements: pypdfium2, Pillow  (both in ~/venv)

Usage:
    python3 pdf_extract.py <pdf_file> [options]

Examples:
    python3 pdf_extract.py ~/publications/2010_Wuosmaa_15Cdp16C.pdf
    python3 pdf_extract.py paper.pdf --pages 2,3 --dpi 200
    python3 pdf_extract.py paper.pdf --text-only       # only extract text
    python3 pdf_extract.py paper.pdf --images-only     # only extract images

Output structure:
    ~/HELIOS_MD/pictures/<stem>/
        page-001.png
        page-002.png
        ...
        text.md          <- extracted text as markdown
        summary.md       <- page list + text previews + figure links

Markdown link syntax:
    ![Fig 1](../pictures/<stem>/page-002.png)
"""

import argparse
import re
import sys
from pathlib import Path

import pypdfium2 as pdfium
from PIL import Image


# ---------------------------------------------------------------------------
# Text cleaning helpers
# ---------------------------------------------------------------------------

# APS/PRC/PRL often encodes special characters oddly in the text layer.
# Map common encoding artifacts -> correct Unicode.
CHAR_MAP = {
    'ðd; pÞ': '(d,p)',
    'ðp; dÞ': '(p,d)',
    'ðd; tÞ': '(d,t)',
    'ðt; dÞ': '(t,d)',
    'ðd; 3HeÞ': '(d,³He)',
    'ð3He; dÞ': '(³He,d)',
    'ðd; Þ':   '(d,α)',
    'ð; dÞ':   '(α,d)',
    'ðp; Þ':   '(p,α)',
    'ð; pÞ':   '(α,p)',
    'ðd; pÞ':  '(d,p)',
    '\r\n': '\n',
    '\r': '\n',
}

def clean_text(raw: str) -> str:
    """Clean raw text extracted from PDF text layer."""
    text = raw
    for bad, good in CHAR_MAP.items():
        text = text.replace(bad, good)

    # Collapse 3+ newlines to 2
    text = re.sub(r'\n{3,}', '\n\n', text)

    # Remove lone hyphen line-breaks (PDF line wrap artifacts)
    text = re.sub(r'(\w)-\n(\w)', r'\1\2', text)

    return text.strip()


def text_to_markdown(page_texts: list, title: str = "") -> str:
    """Convert list of per-page text strings to a markdown document."""
    lines = []
    if title:
        lines.append(f"# {title}\n")
        lines.append("*Text extracted from PDF by pdf_extract.py*\n")
        lines.append("---\n")

    for i, text in enumerate(page_texts, 1):
        lines.append(f"## Page {i}\n")
        lines.append(text)
        lines.append("\n---\n")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Page rendering
# ---------------------------------------------------------------------------

def render_page(page, dpi: int = 150, max_dim: int = 3500) -> Image.Image:
    """Render a PDF page to PIL Image using PDFium."""
    scale = dpi / 72.0
    w, h = page.get_size()
    if max(w, h) * scale > max_dim:
        scale = max_dim / max(w, h)
    bitmap = page.render(scale=scale)
    img = bitmap.to_pil()
    bitmap.close()
    return img


# ---------------------------------------------------------------------------
# Main extraction function
# ---------------------------------------------------------------------------

def extract_pdf(
    pdf_path: str,
    outdir: str = None,
    pages: list = None,
    dpi: int = 150,
    max_dim: int = 3500,
    do_images: bool = True,
    do_text: bool = True,
    verbose: bool = True,
) -> dict:
    """
    Extract a PDF to PNG images + Markdown text.

    Args:
        pdf_path:   Path to PDF file
        outdir:     Output directory (default: ~/HELIOS_MD/pictures/<stem>/)
        pages:      1-indexed page list (default: all)
        dpi:        Image rendering DPI
        max_dim:    Max pixel dimension
        do_images:  Render page images
        do_text:    Extract text layer
        verbose:    Print progress

    Returns:
        dict with keys: 'images', 'text_md', 'summary_md', 'outdir'
    """
    pdf_path = Path(pdf_path).expanduser().resolve()
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF not found: {pdf_path}")

    if outdir is None:
        outdir = Path.home() / "HELIOS_MD" / "pictures" / pdf_path.stem
    else:
        outdir = Path(outdir).expanduser()
    outdir.mkdir(parents=True, exist_ok=True)

    doc = pdfium.PdfDocument(str(pdf_path))
    n_pages = len(doc)

    if verbose:
        print(f"\nPDF: {pdf_path.name}  ({n_pages} pages)")
        print(f"Output: {outdir}/")

    # Page selection
    if pages is None:
        page_indices = list(range(n_pages))
    else:
        page_indices = [p - 1 for p in pages if 1 <= p <= n_pages]

    image_files = []
    page_texts = [''] * n_pages  # full text, all pages

    for idx in page_indices:
        page = doc[idx]

        # --- Text extraction ---
        if do_text:
            try:
                tp = page.get_textpage()
                raw = tp.get_text_range()
                page_texts[idx] = clean_text(raw)
            except Exception as e:
                page_texts[idx] = f"[text extraction failed: {e}]"

        # --- Image rendering ---
        if do_images:
            img = render_page(page, dpi=dpi, max_dim=max_dim)
            out_path = outdir / f"page-{idx+1:03d}.png"
            img.save(out_path, optimize=True)
            image_files.append(out_path)
            if verbose:
                w, h = img.size
                kb = out_path.stat().st_size // 1024
                txt_preview = page_texts[idx][:60].replace('\n', ' ')
                print(f"  p{idx+1:02d}: {w}x{h}px {kb}KB | {txt_preview}...")

        page.close()

    doc.close()

    # --- Write text.md ---
    text_md_path = None
    if do_text:
        active_texts = [page_texts[i] for i in page_indices]
        md_content = text_to_markdown(active_texts, title=pdf_path.stem.replace('_', ' '))
        text_md_path = outdir / "text.md"
        text_md_path.write_text(md_content, encoding='utf-8')
        if verbose:
            total_chars = sum(len(t) for t in active_texts)
            print(f"\n  Text: {text_md_path.name}  ({total_chars} chars)")

    # --- Write summary.md ---
    summary_lines = [
        f"# {pdf_path.stem.replace('_', ' ')}",
        f"",
        f"**Source:** `{pdf_path}`  ",
        f"**Pages:** {n_pages}  ",
        f"**Extracted:** pages {[i+1 for i in page_indices]}  ",
        f"**DPI:** {dpi}  ",
        f"",
        f"---",
        f"",
        f"## Pages",
        f"",
    ]
    for idx in page_indices:
        page_num = idx + 1
        img_link = f"![page {page_num}](page-{page_num:03d}.png)"
        text_preview = page_texts[idx][:200].replace('\n', ' ').strip()
        summary_lines += [
            f"### Page {page_num}",
            f"",
            img_link,
            f"",
            f"*{text_preview}...*",
            f"",
        ]

    if do_text:
        summary_lines += [
            f"---",
            f"",
            f"## Full Text",
            f"",
            f"See [text.md](text.md) for the complete extracted text.",
        ]

    summary_md_path = outdir / "summary.md"
    summary_md_path.write_text('\n'.join(summary_lines), encoding='utf-8')

    if verbose:
        print(f"  Summary: {summary_md_path.name}")
        print(f"\nDone. {len(image_files)} images, text extracted.")
        print(f"\nLink in paper notes:")
        stem = pdf_path.stem
        print(f"  ![Fig 1](../pictures/{stem}/page-002.png)")
        print(f"  *Fig 1: Caption here.*")

    return {
        'images': [str(f) for f in image_files],
        'text_md': str(text_md_path) if text_md_path else None,
        'summary_md': str(summary_md_path),
        'outdir': str(outdir),
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Extract PDF → PNG images + Markdown text for HELIOS paper notes."
    )
    parser.add_argument("pdf", help="Path to PDF file")
    parser.add_argument("--outdir", "-o", default=None,
        help="Output directory (default: ~/HELIOS_MD/pictures/<stem>/)")
    parser.add_argument("--pages", "-p", default=None,
        help="Comma-separated 1-indexed page numbers (default: all). E.g. --pages 1,2,4")
    parser.add_argument("--dpi", "-d", type=int, default=150,
        help="Image DPI (default: 150; use 200 for sharper)")
    parser.add_argument("--max-dim", type=int, default=3500,
        help="Max pixel dimension (default: 3500)")
    parser.add_argument("--text-only", action="store_true",
        help="Only extract text, skip image rendering")
    parser.add_argument("--images-only", action="store_true",
        help="Only render images, skip text extraction")
    parser.add_argument("--quiet", "-q", action="store_true",
        help="Suppress output")

    args = parser.parse_args()

    if args.text_only and args.images_only:
        print("Error: --text-only and --images-only are mutually exclusive.")
        sys.exit(1)

    pages = None
    if args.pages:
        try:
            pages = [int(p.strip()) for p in args.pages.split(",")]
        except ValueError:
            print(f"Error: --pages must be comma-separated integers. Got: {args.pages}")
            sys.exit(1)

    extract_pdf(
        pdf_path=args.pdf,
        outdir=args.outdir,
        pages=pages,
        dpi=args.dpi,
        max_dim=args.max_dim,
        do_images=not args.text_only,
        do_text=not args.images_only,
        verbose=not args.quiet,
    )


if __name__ == "__main__":
    main()
