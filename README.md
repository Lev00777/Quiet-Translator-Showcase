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
  <img src="screen-main.png" width="180" alt="Home screen">
  <img src="screen-languages.png" width="180" alt="Language picker">
  <img src="screen-006.png" width="180" alt="Lock screen">
  <img src="screen-settings.png" width="180" alt="Settings">
  <img src="screen-category.png" width="180" alt="Translation category">
  <img src="screen-help.png" width="180" alt="Help & Guide">
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
