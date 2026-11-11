# Privacy Policy — Quiet Translator

**Last Updated: November 11, 2026**
**Effective Date: October 5, 2026**

---

## Data Controller

NeuroOrbit AI (Montréal, Québec, Canada)
Contact: mission@neuroorbitai.com

Person in charge of the protection of personal information
(Québec Law 25): Alex Klimenko — mission@neuroorbitai.com

---

## 1. Introduction

Your privacy is our top priority. Quiet Translator is designed to keep as little
data as possible. Your speech is processed in real time to show you the translation.
We do not store your audio, transcripts or translations on our servers.

This Privacy Policy explains exactly what data we collect, why we collect it,
who processes it on our behalf, and what rights you have.

---

## 2. Microphone Access and Audio Data

Quiet Translator requires access to your device microphone solely to provide
real-time speech translation during an active session.

Your audio is streamed securely over encrypted connections (HTTPS/WSS) to the
speech-recognition providers listed in Section 7, where it is transcribed into
text in real time.

**We do NOT keep audio recordings on our servers.**
Audio is streamed in real time and discarded after processing.
In one of the listening modes, short audio segments are briefly held in a temporary
file on your device while they are sent for transcription, and that file is deleted
as soon as processing finishes.
Our server-side audio retention is **0 days**.

**App versions 1.0.5 and earlier:** in that listening mode, these versions also kept
a copy of each audio segment in the app's storage on your device, and on iPhone it
could be included in your device backup. These copies were never sent to our servers.
Deleting the app removes them, and the next app update deletes them automatically.

Please note: speech-recognition and translation providers process audio and text
to deliver the service, under their own terms. Some of them may keep limited data
for a period of time (for example, OpenAI may keep translation requests for up to
30 days to monitor for abuse), and, depending on the provider and plan, may use
data to improve their models. We do not control their internal processing and
encourage you to review their privacy policies (Section 7).

---

## 3. No Transcript Storage

Translated text is displayed on screen during your active session only.
We do not store transcripts in any database, log, or file after the session ends.

Server-side transcript retention: **0 days.**
On-device transcript retention: **0 days.**

---

## 4. Data We Collect

To operate your account, provide the service, and manage subscriptions,
we collect the following limited data:

**Account data**
- Email address (via Firebase Authentication)
- A pseudonymous user identifier (uid)
- If you sign in with Google or Apple, we receive basic account identifiers
  from those providers; we do not receive or store your password.
- Your name, if you provide it or if Apple or Google share it when you sign in.
- An optional profile photo, if you choose one: it is reduced to a small image,
  stored with your account, and deleted when you delete your account.

**Using the App Without an Account (Guest Mode)**
- If you tap “Try without an account”, we create an anonymous account through Firebase Authentication. It contains only a random user identifier; we do not collect your email, name or any contact details.
- Guest use is limited to 15 minutes of listening. To enforce this limit, we record the minutes used and the device identifier described below.
- If you later sign in with Apple, Google or email, the anonymous account is linked to that account and the minutes already used carry over.
- Guest data follows the same retention rules as other accounts (see below). You can delete it at any time in the app (Settings → Delete Account) or by contacting us.

**Usage data (for billing and fair-use limits)**
- Listening time used, in minutes
- Your current subscription plan and remaining minutes
- The target language of each translation request (used to process the request, not stored)

**Device identifier (anti-abuse)**
- To prevent abuse of the one-time free trial, we use a device-level signal:
  Apple DeviceCheck on iOS, or the Android ID on Android. It is used only to
  enforce trial and usage limits. It is not used for advertising, is not shared
  with advertisers, and is not used to track you across other apps or websites.

**Subscription data**
- Your subscription status, plan, purchase and renewal events, as provided
  by Apple (App Store), Google (Google Play) and our subscription-management
  provider (RevenueCat). We do not receive or store your full payment card
  details — payment is handled by Apple or Google.

We do **not** store the content of your conversations. It passes through our
servers and the providers listed in Section 7 only to produce the transcription
and translation you see.

**Data retention:** account and usage data are retained while your account is
active. Section 8 explains what is deleted when you delete your account. Our server
also keeps technical logs (an account identifier, request type, data sizes, timing
and error codes, but no audio, transcripts or translations) for up to 30 days.

---

## 5. Legal Basis for Processing (GDPR Art. 6)

| Processing Activity | Legal Basis |
|---|---|
| Real-time audio streaming for translation | Performance of contract — Art. 6(1)(b) |
| Account and subscription management | Performance of contract — Art. 6(1)(b) |
| Usage limits and billing | Performance of contract — Art. 6(1)(b) |
| Device identifier for trial and abuse prevention | Legitimate interests — Art. 6(1)(f) |
| Technical logs, security and troubleshooting | Legitimate interests — Art. 6(1)(f) |
| Marketing communications (if any) | Your consent — Art. 6(1)(a) |
| Legal compliance | Legal obligation — Art. 6(1)(c) |

---

## 6. Recording Others / Consent Notice

You are responsible for how you use Quiet Translator. In some regions, laws
require the consent of other people before their speech is captured or processed.
You agree to use the application in compliance with all applicable laws in your
location, including any laws regarding recording or processing the speech of others.
Because we do not store audio or transcripts on our servers, no recording of
other people is created or retained by us.

---

## 7. Third-Party Sub-Processors

We use the following third-party providers, acting as data processors on our behalf.
Audio and text sent to them are used to return a transcription or translation and
are not stored by us. In two of the listening modes the app connects directly to
Deepgram or AssemblyAI, so these providers also see your IP address. We encourage you to review each provider's privacy policy.

| Sub-Processor | Service | Privacy Policy |
|---|---|---|
| Google (Firebase) | Authentication and account database | firebase.google.com/support/privacy |
| Amazon Web Services (AWS) | Serverless backend, usage database | aws.amazon.com/privacy |
| OpenAI | Speech transcription (Whisper) and text translation | openai.com/policies/privacy-policy |
| Deepgram | Real-time speech transcription | deepgram.com/privacy |
| AssemblyAI | Real-time speech transcription | assemblyai.com/legal/privacy-policy |
| DeepL | Text translation (automatic backup) | deepl.com/en/privacy |
| RevenueCat | Subscription management | revenuecat.com/privacy |
| Apple | App Store payments and subscriptions; DeviceCheck (iOS) | apple.com/legal/privacy |
| Google (Google Play) | Google Play payments and subscriptions (Android) | policies.google.com/privacy |
| Google (Google Fonts) | Fonts used in the app, downloaded the first time they are shown (Google sees your IP address) | policies.google.com/privacy |

---

## 8. Your Rights and Account Deletion

Depending on your jurisdiction (including under GDPR, UK GDPR, Canada's PIPEDA,
and CCPA/CPRA), you have the right to:

- **Access** the personal data we hold about you
- **Correct** inaccurate data
- **Erase** your data ("right to be forgotten")
- **Port** your data to another service
- **Object** to processing based on legitimate interests
- **Withdraw consent** at any time without affecting prior lawful processing

**Account deletion:** You can delete your account directly in the app
(Settings → Delete Account). This permanently deletes your sign-in account and
profile (email, name, profile photo). Your usage record (minutes used, plan, device
identifier) and your subscription record at RevenueCat are deleted on request: email
us and we will delete them within 30 days. Technical logs are deleted automatically
within 30 days. A free-trial minute counter per device is kept to prevent abuse,
without a link to your account. Subscription cancellation is managed through
your Apple ID settings (iOS) or Google Play account settings (Android).
Deleting your account does not cancel an active subscription.

**California residents (CCPA/CPRA):** You have the right to know what personal
information we collect, the right to delete it, and the right to opt out of the
"sale" or "sharing" of personal information. We do not sell your personal information.

Submit requests to: mission@neuroorbitai.com
We respond within 30 days (45 days for CCPA requests).

You may also file a complaint with your local supervisory authority — for example,
your EU Member State DPA, the UK ICO, the CNIL (France), the Office of the Privacy
Commissioner of Canada, the Commission d'accès à l'information du Québec, or the ANPD (Brazil).

---

## 9. International Data Transfers

Data may be processed on servers located in the United States and other countries.

**EU/EEA and UK users:** transfers are carried out under Standard Contractual
Clauses (SCCs) adopted by the European Commission (Decision 2021/914).

---

## 10. Data Security

We implement industry-standard security measures including TLS encryption in transit,
encryption at rest for account data, strict access controls, and regular security reviews.

---

## 11. Children's Privacy

Quiet Translator is not directed to children under 13 (under 16 in the EU/EEA),
or under the higher minimum age required in your jurisdiction. We do not knowingly collect personal data from children.
If you believe a child has provided us data, contact us and we will delete it.

---

## 12. Changes to This Policy

We will notify you of any material changes via email and/or in-app notification
at least 14 days before changes take effect. Continued use of the application
after the effective date constitutes your acceptance of the updated policy.

---

## 13. Contact

Privacy inquiries: mission@neuroorbitai.com
