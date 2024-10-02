---
title: YouTube Music Desktop
description: 
published: true
date: 2024-10-02T20:41:48.228Z
tags: loupedeck, plugin, extension, ytmd
editor: markdown
dateCreated: 2022-01-10T11:54:12.635Z
---

# 1. Badges
[![Forks](https://img.shields.io/github/forks/XeroxDev/Loupedeck-plugin-YTMDesktop?color=blue&style=for-the-badge)](https://github.com/XeroxDev/Loupedeck-plugin-YTMDesktop/network/members)  [![Stars](https://img.shields.io/github/stars/XeroxDev/Loupedeck-plugin-YTMDesktop?color=yellow&style=for-the-badge)](https://github.com/XeroxDev/Loupedeck-plugin-YTMDesktop/stargazers) [![Watchers](https://img.shields.io/github/watchers/XeroxDev/Loupedeck-plugin-YTMDesktop?color=lightgray&style=for-the-badge)](https://github.com/XeroxDev/Loupedeck-plugin-YTMDesktop/watchers) [![Contributors](https://img.shields.io/github/contributors/XeroxDev/Loupedeck-plugin-YTMDesktop?color=green&style=for-the-badge)](https://github.com/XeroxDev/Loupedeck-plugin-YTMDesktop/graphs/contributors)

[![Issues](https://img.shields.io/github/issues/XeroxDev/Loupedeck-plugin-YTMDesktop?color=yellow&style=for-the-badge)](https://github.com/XeroxDev/Loupedeck-plugin-YTMDesktop/issues) [![Issues closed](https://img.shields.io/github/issues-closed/XeroxDev/Loupedeck-plugin-YTMDesktop?color=yellow&style=for-the-badge)](https://github.com/XeroxDev/Loupedeck-plugin-YTMDesktop/issues?q=is%3Aissue+is%3Aclosed)

[![Issues-pr](https://img.shields.io/github/issues-pr/XeroxDev/Loupedeck-plugin-YTMDesktop?color=yellow&style=for-the-badge)](https://github.com/XeroxDev/Loupedeck-plugin-YTMDesktop/pulls) [![Issues-pr closed](https://img.shields.io/github/issues-pr-closed/XeroxDev/Loupedeck-plugin-YTMDesktop?color=yellow&style=for-the-badge)](https://github.com/XeroxDev/Loupedeck-plugin-YTMDesktop/pulls?q=is%3Apr+is%3Aclosed) [![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=for-the-badge)](https://github.com/XeroxDev/Loupedeck-plugin-YTMDesktop/compare)

<!-- [![Build](https://img.shields.io/github/workflow/status/XeroxDev/Loupedeck-plugin-YTMDesktop/CI-CD?style=for-the-badge)](https://github.com/XeroxDev/Loupedeck-plugin-YTMDesktop/actions?query=workflow%3A%22CI-CD%22) -->
[![Release](https://img.shields.io/github/release/XeroxDev/Loupedeck-plugin-YTMDesktop?color=black&style=for-the-badge)](https://github.com/XeroxDev/Loupedeck-plugin-YTMDesktop/releases) [![Downloads](https://img.shields.io/github/downloads/XeroxDev/Loupedeck-plugin-YTMDesktop/total.svg?color=cyan&style=for-the-badge&logo=github)]()

[![Awesome Badges](https://img.shields.io/badge/badges-awesome-green?style=for-the-badge)](https://shields.io)

# 2. What is this Plugin?
This Loupedeck Plugin allows you to control the [YouTube Music Desktop App](https://github.com/ytmdesktop/ytmdesktop)

> **Note**
> We don't support v1.13.0 or lower. We also don't support V2 **yet**. We recommend updating to the [latest Nightly pre-release](https://github.com/ytmdesktop/ytmdesktop/releases/tag/1.14.2)
{.is-warning}

# 3. Supported operating systems
- [X] Windows
- [ ] Mac

# 4. Support / Feedback
You found a bug? You have a feature request? I would love to hear about it [here](https://github.com/XeroxDev/Loupedeck-plugin-YTMDesktop/issues/new/choose) or click on the "Issues" tab here on the GitHub repositorie!

You can also join my discord [here](https://s.tswi.me/discord)

# 5. Actions

- Play / Pause Track
- Next Track
- Previous Track
- Like Track
- Dislike Track
- Volume Mute
- Volume Down
- Volume Up
- Track Info
  - Shows a scrolling text for album, title and author
  - Shows the thumbnail of the track
- Shuffle
- Repeat
  - NONE
  - ALL
  - ONE

# 6. How to use it?
<ol>
  <li>Install the <a href="https://github.com/ytmdesktop/ytmdesktop">YouTube Music Desktop App</a>.</li>
    <li>Install the Plugin from <a href="https://github.com/XeroxDev/Loupedeck-plugin-YTMDesktop/releases">Releases</a> or from the official Loupedeck Store.</li>
    <li>
    Add a settings profile action, fill out everything and click save.
    <details class="example">
      <summary>Show me!</summary>
      <img src="/assets/guides/loupedeck/ytmdesktop/step3.1.png" alt="step3.1.png"/>
    </details>
  </li>
  <li>
    Make sure the YouTube Music Desktop App and the Companion Server is running
    <ul>
        <li>To start the companion server, click at the top right of YTMDesktop on the settings gear</li>
      <li>Go on the left side on the "Integrations" tab</li>
      <li>Enable the "Companion Server"</li>
    </ul>
    <details class="example">
      <summary>Show me!</summary>
      <img src="/assets/guides/ytmdesktop/step1.png" alt="step1.png"/><br/>
      <img src="/assets/guides/ytmdesktop/step2.png" alt="step2.png"/><br/>
      <img src="/assets/guides/ytmdesktop/step3.png" alt="step3.png"/>
    </details>
  </li>
  <li>
    Turn on "enable companion authorization" under the Companion Server
    <details class="example">
      <summary>Show me!</summary>
      <img src="/assets/guides/ytmdesktop/step4.png" alt="step6.png"/>
    </details>
  </li>
  <li>Press the Profile button on your device</li>
  <li>
    Compare the authorization code displaying by the plugin with the one displaying in the YouTube Music Desktop App and if they match, confirm the authorization in the YouTube Music Desktop App
    <details class="example">
      <summary>Show me!</summary>
      <img src="/assets/guides/loupedeck/ytmdesktop/step7.png" alt="step8.png"/>
    </details>
  </li>
  <li>If you've gotten no error and the plugin is now displayed in the "Authorized companions" list of YouTube Music Desktop, you can now use the plugin</li>
</ol>

# 7. Links
[Download](https://github.com/XeroxDev/Loupedeck-plugin-YTMDesktop/releases/latest/download/YTMDesktop.lplug4){: .v-btn .v-btn--flat .v-btn--text .theme--dark .v-size--default .v-btn--depressed .theme--dark .white--text .primary} [Source Code](https://github.com/XeroxDev/Loupedeck-plugin-YTMDesktop/){: .v-btn .v-btn--flat .v-btn--text .theme--dark .v-size--default .v-btn--depressed .theme--dark .white--text .secondary} [Changelog](https://github.com/XeroxDev/Loupedeck-plugin-YTMDesktop/blob/main/CHANGELOG.md){: .v-btn .v-btn--flat .v-btn--text .theme--dark .v-size--default .v-btn--depressed .theme--dark .white--text .success}

# 8. How to contribute?

Just fork the repository and create PR's, but we use [standard-version](https://github.com/conventional-changelog/standard-version) to optimal release the plugin.

standard-version is following the [conventionalcommits](https://www.conventionalcommits.org) specification which follows the [angular commit guidelines](https://github.com/angular/angular/blob/22b96b9/CONTRIBUTING.md#-commit-message-guidelines)

[Here](https://kapeli.com/cheat_sheets/Conventional_Commits.docset/Contents/Resources/Documents/index) is a neat little cheatsheet for Conventional Commits
