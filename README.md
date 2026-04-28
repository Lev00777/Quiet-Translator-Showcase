# 🦁 AI Quiet Translator

*Real-time AI voice translation pipeline designed specifically for high-noise industrial and assembly environments.*

Leonardo_Lightning_A_digital_illustration_of_a_stylized_lion_h_3.jpg

## 🎯 The Problem
In industrial environments, heavy machinery and ambient noise make communication between team members difficult. Traditional translation apps fail because their standard Bluetooth and microphone configurations cannot isolate voice from industrial noise, and waiting for full-sentence translation causes unacceptable delays on the floor.

## 💡 The Solution
**Quiet Translator** uses a custom two-phase audio pipeline and forced microphone routing to ensure seamless communication. Users can speak directly into the device's main microphone (bypassing low-quality Bluetooth headset mics) while receiving instant, translated audio feedback directly into their earpieces.

### ✨ Key Features
* **Continuous Streaming:** Real-time audio streaming without waiting for the speaker to finish.
* **Smart Audio Routing:** Forces device microphone usage while outputting to Bluetooth headphones to bypass hardware limitations of HFP (Hands-Free Profile).
* **Background Execution:** Maintains translation streams even when the device screen is off.
* **Secure Architecture:** No hardcoded API keys. All third-party AI requests are securely proxied through a custom Serverless backend.

## 🛠 Architecture & Tech Stack

* **Frontend:** Flutter, Dart
* **Backend / Proxy:** AWS Serverless (API Gateway, AWS Lambda), Node.js
* **Speech-to-Text (STT):** Deepgram / AssemblyAI via WebSockets
* **Translation:** DeepL API
* **Security:** JWT Token generation, Custom Headers, Obfuscated compiled binaries
