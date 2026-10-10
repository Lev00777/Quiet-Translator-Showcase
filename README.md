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
  <img src="screen-002.png" width="180" alt="AWS Setup Logs">
  <img src="screen-006.png" width="180" alt="Home Screen">
  <img src="screen-007.png" width="180" alt="Recording Mode">
  <img src="screen-008.png" width="180" alt="Translated Text View">
  <img src="screen-009.png" width="180" alt="Translated Text View">
  <img src="screen-011.png" width="180" alt="Translated Text View">
  <img src="screen-013.png" width="180" alt="Translated Text View">
  <img src="screen-015.png" width="180" alt="Translated Text View">
  <img src="screen-016.png" width="180" alt="Translated Text View">
</p>

## 🛠 Architecture & Tech Stack

* **Frontend:** Flutter, Dart
* **Backend / Proxy:** AWS Serverless (API Gateway, AWS Lambda), Node.js
* **Speech-to-Text (STT):** Deepgram / AssemblyAI via WebSockets
* **Translation:** DeepL API
* **Security:** JWT Token generation, Custom Headers, Obfuscated compiled binaries

## 🌐 Website languages

The landing page is published in 17 languages: English at the root, the rest in folders (`/es/`, `/fr/`, `/de/`, `/pt/`, `/pl/`, `/tr/`, `/id/`, `/el/`, `/ru/`, `/uk/`, `/vi/`, `/th/`, `/zh/`, `/ko/`, `/ar/`, `/he/`).

* Layout lives in `i18n/template.html`, texts in `i18n/strings/<code>.json`.
* After editing either, run `python3 i18n/build.py` and commit the regenerated `index.html`, `<code>/index.html` and `sitemap.xml`.
* Do not edit the generated `index.html` files by hand: the next build overwrites them.
* To add a text, add the key to every JSON file (the build stops and lists missing keys) and use `{{key}}` in the template.
