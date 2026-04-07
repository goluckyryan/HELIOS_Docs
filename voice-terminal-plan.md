# Voice Terminal Plan — Talk to HELIOS

## Goal
Connect a mic + speaker to the Pi so you can have voice conversations with HELIOS.

## Hardware Options

### Option A: AirPods 2 (Recommended)
- **Mic + Speaker** in one device over Bluetooth
- BT profile: HFP (hands-free) — lower audio quality but has mic
- Hands-free, walk around
- Caveat: pairing on Linux can be finicky; may need to "forget" from iPhone first
- PipeWire (Pi OS Bookworm default) handles AirPods better than PulseAudio

### Option B: Sony XE300 + USB Mic
- Sony XE300 = speaker only (A2DP, no mic)
- Need separate USB mic (conference mic, lavalier, or ReSpeaker array)
- Better/louder audio output than AirPods
- More reliable BT pairing

## Software Pipeline

```
🎤 Mic → [STT] → text → [OpenClaw API] → response text → [TTS] → 🔊 Speaker
```

### 1. Speech-to-Text (STT) — Listening
- **Whisper.cpp** — runs locally on Pi 5 (ARM64), small/base model
- **Vosk** — offline, lightweight, good for Pi
- **OpenAI Whisper API** via Argo (if endpoint available)

### 2. OpenClaw Integration — Thinking
- HTTP POST to gateway API (`localhost:18789`)
- Send transcribed text, get response

### 3. Text-to-Speech (TTS) — Speaking
- **OpenClaw `tts` tool** — built-in
- **Piper TTS** — local on Pi, fast, good voices
- **ElevenLabs** — premium cloud voices

### 4. Wake Word (Optional)
- **Porcupine** or **OpenWakeWord**
- Listens for "Hey HELIOS" before activating STT
- Saves resources — mic only processes after wake word

## Bluetooth Setup (Pi 5)

```bash
# Pair device
bluetoothctl
  scan on
  pair <MAC_ADDRESS>
  trust <MAC_ADDRESS>
  connect <MAC_ADDRESS>

# For AirPods: set as both input and output
pactl set-default-sink bluez_sink.<MAC>
pactl set-default-source bluez_source.<MAC>

# For Sony XE300: output only
pactl set-default-sink bluez_sink.<MAC>
# Then set USB mic as input
pactl set-default-source alsa_input.usb-*
```

## Implementation Steps

- [ ] Pick hardware: AirPods 2 or Sony XE300 + USB mic
- [ ] Pair Bluetooth device to Pi
- [ ] Verify audio input/output works (`arecord`/`aplay`)
- [ ] Install STT engine (whisper.cpp or Vosk)
- [ ] Install TTS engine (Piper or use OpenClaw tts)
- [ ] Write Python voice loop script
- [ ] Add wake word detection (optional)
- [ ] Test end-to-end conversation
- [ ] Set up as systemd service for auto-start

## Python Voice Loop (Skeleton)

```python
import sounddevice as sd
import numpy as np
# + whisper, requests, piper/tts

GATEWAY = "http://localhost:18789"

while True:
    # 1. Listen for wake word (optional)
    # 2. Record audio from mic
    audio = record_until_silence()
    
    # 3. Transcribe
    text = stt_transcribe(audio)
    
    # 4. Send to OpenClaw
    response = openclaw_chat(text)
    
    # 5. Speak response
    tts_speak(response)
```

## Notes
- AirPods HFP mode = 8kHz mono (phone quality) — fine for voice chat
- AirPods A2DP mode = high quality stereo but NO mic
- PipeWire can auto-switch profiles but may need config
- Consider adding a physical button (GPIO) as push-to-talk alternative to wake word

---

## See Also

- `voice-bridge-plan.md` — Discord voice channel bridge (complementary approach)
- `IDENTITY.md` — HELIOS identity
- `HELIOS_DAQ_Workflow.md` — DAQ context for voice commands during runs
- MEMORY.md — Voice terminal TODO item
