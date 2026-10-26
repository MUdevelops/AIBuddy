<div align="center">

<img src="assets/banner.svg" alt="AIBuddy - one click to every AI tool" width="100%" />

<br/>

![Manifest V3](https://img.shields.io/badge/Chrome-Manifest%20V3-ff2bd6?style=for-the-badge&labelColor=07040f&logo=googlechrome&logoColor=white)
![No Signup](https://img.shields.io/badge/Signup-Never-00e5ff?style=for-the-badge&labelColor=07040f)
![Tracking](https://img.shields.io/badge/Tracking-None-7a3cff?style=for-the-badge&labelColor=07040f)
![JavaScript](https://img.shields.io/badge/Built%20with-Vanilla%20JS-ff2bd6?style=for-the-badge&labelColor=07040f&logo=javascript&logoColor=white)
[![Stars](https://img.shields.io/github/stars/MUdevelops/AIBuddy?style=for-the-badge&color=00e5ff&labelColor=07040f&logo=github)](https://github.com/MUdevelops/AIBuddy/stargazers)

**[Overview](#-overview)** • **[Features](#-features)** • **[Install](#-installation)** • **[Usage](#-usage)** • **[Customize](#-customize-your-links)** • **[Roadmap](#-roadmap)** • **[FAQ](#-faq)**

</div>

<img src="assets/divider.svg" alt="" width="100%" />

## ⚡ Overview

**AIBuddy** is a neon, cyberpunk-styled Chrome extension that puts every AI tool you use behind one icon. Click the icon, see your buttons, press one. Claude, ChatGPT, Gemini and more open in a new tab instantly. No typing, no bookmarks folder, no signup.

> Your AI tools, one click away.

<img src="assets/divider.svg" alt="" width="100%" />

## 🧬 Features

- 🚀 **One-click launch** - every AI tool is a single button in the popup
- ➕ **Add custom links** - type a name and a URL, and a new button appears
- ➖ **Remove anything** - press **Edit** and tap the × on any button
- 🔁 **Reset to defaults** - restore the original tool list at any time
- 🌐 **Sync across devices** - your list follows your Chrome profile
- 🎨 **Cyberpunk UI** - pink and blue neon glow, scanlines, angled tiles
- 🔒 **Private by design** - no account, no analytics, no external server
- ⌨️ **Keyboard friendly** - visible focus states and Enter-to-add

<img src="assets/divider.svg" alt="" width="100%" />

## 🖥️ Preview

```text
┌──────────────────────────────────────┐
│  ⚡ AIBuddy                  [ Edit ] │
│  Your AI tools, one click away       │
├──────────────────────────────────────┤
│  [ Claude ]  [ ChatGPT ]  [ Gemini ] │
│  [ Perplexity ] [ Copilot ] [ Grok ] │
│  [ DeepSeek ] [ Mistral ] [ Meta AI ]│
│  [ Poe ]  [ NotebookLM ] [Midjourney]│
├──────────────────────────────────────┤
│     ★  Star the repo on GitHub       │
│          MUdevelops/AIBuddy          │
└──────────────────────────────────────┘
```

<!-- Add a real screenshot: place it at assets/preview.png and replace the block above with
<img src="assets/preview.png" alt="AIBuddy popup" width="380" /> -->

<img src="assets/divider.svg" alt="" width="100%" />

## 🤖 Supported AI Tools

These buttons come built in. You can remove any of them or add your own.

| Tool | Link |
| --- | --- |
| Claude | https://claude.ai |
| ChatGPT | https://chatgpt.com |
| Gemini | https://gemini.google.com |
| Perplexity | https://www.perplexity.ai |
| Copilot | https://copilot.microsoft.com |
| Grok | https://grok.com |
| DeepSeek | https://chat.deepseek.com |
| Mistral | https://chat.mistral.ai |
| Meta AI | https://www.meta.ai |
| Poe | https://poe.com |
| NotebookLM | https://notebooklm.google.com |
| Midjourney | https://www.midjourney.com |

<img src="assets/divider.svg" alt="" width="100%" />

## 🔧 Installation

AIBuddy loads as an unpacked extension, so you can install it in under a minute.

1. **Download** the code: click **Code → Download ZIP**, or run:
   ```bash
   git clone https://github.com/MUdevelops/AIBuddy.git
   ```
2. Open `chrome://extensions` in Chrome (also works in Edge, Brave and other Chromium browsers).
3. Turn on **Developer mode** (top right).
4. Click **Load unpacked** and select the `AIBuddy` folder.
5. Pin it with the puzzle-piece menu so the icon stays in your toolbar.

<img src="assets/divider.svg" alt="" width="100%" />

## 🕹️ Usage

1. Click the **AIBuddy** icon in your toolbar.
2. Press any button. The tool opens in a new tab and the popup closes.

That is the whole workflow.

<img src="assets/divider.svg" alt="" width="100%" />

## 🛠️ Customize Your Links

**Add a button**
1. Press **Edit** in the popup.
2. Enter a name (for example `Suno`) and a link (for example `suno.com`).
3. Press **Add button** or hit Enter. Missing `https://` is added for you.

**Remove a button**
1. Press **Edit**.
2. Tap the **×** on the tile you want gone.
3. Press **Done**.

**Start over**
Press **Reset to defaults** in Edit mode to bring back the original list.

<img src="assets/divider.svg" alt="" width="100%" />

## 🔒 Privacy & Permissions

| Question | Answer |
| --- | --- |
| Do I need an account? | No |
| Does it collect data? | No |
| Does it talk to a server? | No server of its own |
| Permissions requested | `storage` only, to save your button list |
| Where is my list stored? | In your Chrome profile (`chrome.storage.sync`) |

Tool logos are loaded from Google's public favicon service. If a logo cannot load, AIBuddy shows a neon letter instead.

<img src="assets/divider.svg" alt="" width="100%" />

## 🧪 Tech Stack

- **Chrome Extension Manifest V3**
- **HTML5 + CSS3** - custom neon theme, no framework
- **Vanilla JavaScript** - no build step, no dependencies
- **Chrome Storage API** - saves your links

<img src="assets/divider.svg" alt="" width="100%" />

## 📁 Project Structure

```text
AIBuddy/
├── manifest.json     # Extension config (MV3)
├── popup.html        # Popup layout
├── popup.css         # Cyberpunk neon styling
├── popup.js          # Buttons, add/remove, storage
├── icons/            # 16, 32, 48, 128 px icons
└── assets/           # README banner and divider
```

<img src="assets/divider.svg" alt="" width="100%" />

## 🗺️ Roadmap

- [x] One-click AI tool buttons
- [x] Add, remove and reset links
- [x] Neon cyberpunk popup
- [ ] Drag-to-reorder buttons
- [ ] Search box to filter tools
- [ ] Keyboard shortcut to open the popup
- [ ] Button groups (chat, image, code, research)
- [ ] Export and import your link list
- [ ] Chrome Web Store release

<img src="assets/divider.svg" alt="" width="100%" />

## 🤝 Contributing

Ideas and pull requests are welcome.

1. Fork the repo
2. Create a branch: `git checkout -b feature/my-idea`
3. Commit your changes: `git commit -m "Add my idea"`
4. Push the branch and open a pull request

Found a bug or want a new default tool? [Open an issue](https://github.com/MUdevelops/AIBuddy/issues).

<img src="assets/divider.svg" alt="" width="100%" />

## ❓ FAQ

<details>
<summary><b>Does it work in other browsers?</b></summary>
<br/>
Yes, in Chromium-based browsers such as Edge, Brave and Opera. Load it the same way from the extensions page.
</details>

<details>
<summary><b>Why did my buttons disappear?</b></summary>
<br/>
Open the popup, press <b>Edit</b>, then <b>Reset to defaults</b>.
</details>

<details>
<summary><b>Can I add any website, not just AI tools?</b></summary>
<br/>
Yes. Any <code>http</code> or <code>https</code> link works.
</details>

<details>
<summary><b>Do I need to sign in to anything?</b></summary>
<br/>
No. AIBuddy never asks for an account.
</details>

<img src="assets/divider.svg" alt="" width="100%" />

## 📜 License

Released under the MIT License. Add a `LICENSE` file to the repo to make it official.

<img src="assets/divider.svg" alt="" width="100%" />

<div align="center">

## ⭐ Support AIBuddy

If AIBuddy saves you clicks, a star helps other people find it.

[![Star on GitHub](https://img.shields.io/badge/%E2%98%85%20Star%20the%20repo-MUdevelops%2FAIBuddy-ff2bd6?style=for-the-badge&labelColor=07040f)](https://github.com/MUdevelops/AIBuddy)

Made with neon by **[MUdevelops](https://github.com/MUdevelops)**

</div>
