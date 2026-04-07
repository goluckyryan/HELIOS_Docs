# Voice Bridge Plan — HELIOS AI Discord Voice Support

**Status:** Planning / Not started  
**Created:** 2026-03-25  
**Goal:** Allow Ryan to speak to HELIOS in a Discord voice channel and hear responses back.

---

## Architecture

```
Discord Voice Channel
       ↓ (audio stream, 16kHz mono PCM)
  [Voice Bridge Bot]  ← Node.js process on Pi (~/voice-bridge/)
       ↓ (faster-whisper STT → text)
  OpenClaw Gateway (localhost:18789)
       ↓ POST /v1/chat/completions
  HELIOS AI (me)
       ↓ text response
  [Voice Bridge Bot]
       ↓ (edge-tts or espeak-ng → MP3/OGG)
Discord Voice Channel
```

---

## Components

### 1. Voice Bridge Bot (`voice-bridge.js`)
- Library: `discord.js` + `@discordjs/voice`
- Commands:
  - `!join` — bot joins your current voice channel
  - `!leave` — bot leaves
- Captures audio stream per user (Opus → PCM conversion)
- Pipes audio to Whisper STT
- POSTs transcription to OpenClaw gateway
- Plays TTS response audio back into channel

### 2. STT — faster-whisper (`whisper-stt.py`)
- Model: `tiny` or `base` (fits Pi 5 RAM, ~200MB)
- int8 quantization for speed
- Input: 16kHz mono WAV file
- Output: transcribed text to stdout
- Latency: ~1–3s on Pi 5

### 3. OpenClaw Gateway Integration
- Endpoint: `POST http://localhost:18789/v1/chat/completions`
- Auth: `Authorization: Bearer hahaha`
- Model: `"openclaw"` (routes to default agent = HELIOS)
- **Config change needed** (one line in openclaw.json):
```json
"gateway": {
  "http": {
    "endpoints": {
      "chatCompletions": { "enabled": true }
    }
  }
}
```

### 4. TTS — text to speech
- **Option A:** `espeak-ng` — free, already on Pi, robotic voice
- **Option B:** `edge-tts` (Microsoft) — free, natural voice, requires internet
  - Install: `pip3 install edge-tts`
  - Usage: `edge-tts --text "Hello" --voice en-US-GuyNeural --write-media out.mp3`
- **Option C:** ElevenLabs API — best quality, costs $, already in OpenClaw TTS skill
- Recommendation: start with `edge-tts`, upgrade to ElevenLabs if needed

---

## File Structure

```
~/voice-bridge/
  voice-bridge.js       # main Discord bot (Node.js)
  whisper-stt.py        # audio → text (faster-whisper)
  tts.sh                # text → audio file (edge-tts or espeak)
  play-response.js      # audio playback into voice channel
  package.json
  .env                  # DISCORD_TOKEN, OPENCLAW_TOKEN
```

---

## Dependencies

### Node.js
```bash
npm install discord.js @discordjs/voice @discordjs/opus libsodium-wrappers ffmpeg-static
```

### Python
```bash
pip3 install faster-whisper edge-tts
```

### System
```bash
sudo apt install ffmpeg espeak-ng
```

---

## Implementation Steps

- [ ] 1. Enable OpenClaw gateway HTTP endpoint (config patch)
- [ ] 2. Install Node.js + Python dependencies on Pi
- [ ] 3. Write `whisper-stt.py` — test standalone with a WAV file
- [ ] 4. Write `tts.sh` — test standalone with sample text
- [ ] 5. Write `voice-bridge.js` — join/leave + audio capture skeleton
- [ ] 6. Wire STT → gateway → TTS pipeline
- [ ] 7. End-to-end test in Discord voice channel
- [ ] 8. Add `!join` / `!leave` commands + auto-disconnect on empty channel
- [ ] 9. (Optional) Add wake word detection to avoid always-on STT

---

## Known Challenges

- **Audio buffering:** Need to detect end-of-speech (silence detection) before sending to Whisper
- **Latency:** STT (~2s) + inference (~3–5s) + TTS (~1s) = ~6–8s total — acceptable for lab
- **Multi-user:** Need to handle multiple speakers cleanly (queue requests)
- **Discord bot token:** Voice bridge needs its own bot token OR reuses the existing HELIOS bot token (check if one bot can handle both text + voice)

---

## Notes

- Pi 5 has enough RAM and CPU for faster-whisper tiny/base
- OpenClaw gateway runs on port 18789 (loopback only by default — fine for local bridge)
- The gateway HTTP API is OpenAI-compatible, so standard `fetch`/`axios` POST works
- Keep voice bridge as a **separate process** from OpenClaw — cleaner, independent restarts

---

_Pick this up whenever ready. All the hard design decisions are made — just needs building._

---

## See Also

- `voice-terminal-plan.md` — Pi mic+speaker direct voice terminal (complementary approach)
- `IDENTITY.md` — HELIOS identity, Discord username and bot IDs
- `HELIOS_DAQ_Workflow.md` — DAQ context for voice commands during runs
- MEMORY.md — Voice channel support TODO item
