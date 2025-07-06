---
title: YouTube Music Streamer
---

# YouTube Music Streamer
![YouTubeMusicStreamer.png](/assets/images/youtube-music-streamer/YouTubeMusicStreamer.png)

[![Discord][badge-discord]][Discord Server]
[![Conventional Commits][badge-conventional-commits]][Conventional Commits]
[![License][ytms-badge-license]][ytms-license]
[![Release][ytms-badge-release]][ytms-download]

<!-- [![Downloads][ytms-badge-downloads]][ytms-download] -->

## About
YouTube Music Streamer is a simple app, that allows you to combine [YouTube Music Desktop App][] with Twitch and your favourite Streaming Software.
From widgets to commands, everything is possible and the best part, customizable to your liking!

The application is written in C#. It uses MAUI x Blazor technology to create a cross-platform app. 

Looking at the image above, the layout and structure is pretty simple. On the left, you have the menu to navigate through the app, and on the right, you have the content of the selected page. The app is designed to be user-friendly and easy to navigate.

If you go through all the guides, you learn how to configure everything. Most settings have a small description below them and also display the default settings in case you want to reset but don't know what the default settings were.

## Features
- **Widgets**: Use some of the pre-made widgets to display information about the currently playing song, or create your own custom widgets.
- **Commands**: Use commands to control YouTube Music, like play, pause, skip, and more. Define your own prefixes, command names, responses and more. Don't like `!info`? Change it to `music info` and make it look more natural.
- **Queue**: View the current queue and control it. Add, remove, or reorder songs in the queue.
- **Blacklist**: Prevent certain songs from being played in your stream. This is useful for avoiding copyright issues or if you don't want to be rickrolled.
- **Bits and Points**: Hook the commands up to Twitch Bits or Channel Points.
- **Free & Open Source**: The app is free and open source. You can contribute to the project, report issues, or just check out the code.
- **Installer & Portable**: The app comes with an installer and a portable version. You can choose the one that suits you best.
- And much more!

## Guides

{% for page in list_pages_in('guides') %}
- [{{ page.title }}]({{ page.url }}){% if page.description %} - {{ page.description }}{% endif %}
{% endfor %}

## Setup
To get started, you need to download the app from the [releases page][ytms-download]. Also, you need to have the [YouTube Music Desktop App][] installed, as this app is just a companion app for it.
Lastly, you also need a Twitch Account and, of course, a streaming software.

!!! warning "Important"
    It's possible GitHub won't show all the files in the release, so make sure pressing the "Show all x assets" button to see all available files.

## Contributing
If you want to contribute to the project, feel free to open an issue or a pull request. You can also join the [Discord Server][] to discuss features, report bugs, or just chat with other users.

For more information on how to contribute, check out the [Contributing Guide][ytms-contributing-guide].

## Code of Conduct
This project follows an adapted version of the Contributor Covenant. You can find the full text in the [CODE_OF_CONDUCT.md][ytms-code-of-conduct] file.
We expect all contributors to follow this code of conduct to ensure a welcoming and inclusive environment for everyone.

## License

This project is covered by the GNU AGPL v3.0. See [LICENSE][ytms-license].

Additional permissions and exceptions can be found in [ADDITIONAL-PERMISSIONS][ytms-additional-license].
