# 🦁 AI Quiet Translator

*Real-time AI voice translation pipeline designed specifically for high-noise industrial and assembly environments.*

<p align="center">
  <img src="Leonardo_Lightning_A_digital_illustration_of_a_stylized_lion_h_3.jpg" alt="Quiet Translator Logo" width="180">
</p>

## 🎯 The Problem
In industrial environments, heavy machinery and ambient noise make communication between team members difficult. Traditional translation apps fail because their standard Bluetooth and microphone configurations cannot isolate voice from industrial noise, and waiting for full-sentence translation causes unacceptable delays on the floor.

## 💡 The Solution
**Quiet Translator** uses a custom two-phase audio pipeline and forced microphone routing to ensure seamless communication. Users can speak directly into the device's main microphone (bypassing low-quality Bluetooth headset mics) while receiving instant, translated audio feedback directly into their earpieces.

## 📱 Screenshots (UI Showcase)

<p align="center">
  <img src="Screenshot_20260504_231935.jpg" width="180" alt="AWS Setup Logs">
  <img src="Screenshot_20260504_232449.jpg" width="180" alt="Home Screen">
  <img src="Screenshot_20260427_200124.jpg" width="180" alt="Recording Mode">
  <img src="Screenshot_20260427_200203.jpg" width="180" alt="Translated Text View">
</p>

## 🛠 Architecture & Tech Stack

* **Frontend:** Flutter, Dart
* **Backend / Proxy:** AWS Serverless (API Gateway, AWS Lambda), Node.js
* **Speech-to-Text (STT):** Deepgram / AssemblyAI via WebSockets
* **Translation:** DeepL API
* **Security:** JWT Token generation, Custom Headers, Obfuscated compiled binaries
