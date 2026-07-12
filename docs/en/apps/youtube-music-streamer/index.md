---
title: YouTube Music Streamer
description: Connect YTMDesktop with Twitch and your streaming software to provide song requests, chat commands, widgets, and automated Channel Point handling.
---

# YouTube Music Streamer

![YouTube Music Streamer](/assets/images/youtube-music-streamer/YouTubeMusicStreamer.png)

[![Discord][badge-discord]][Discord Server]
[![Conventional Commits][badge-conventional-commits]][Conventional Commits]
[![License][ytms-badge-license]][ytms-license]
[![Release][ytms-badge-release]][ytms-download]

<!-- [![Downloads][ytms-badge-downloads]][ytms-download] -->

## About

YouTube Music Streamer is a Windows companion application that connects [YTMDesktop][YouTube Music Desktop App] with Twitch and your streaming software.

It allows viewers to interact with your music through chat commands, song requests, Bits, and Channel Point rewards. You can also expose information about the currently playing song through browser-source widgets for tools such as OBS Studio.

The application is built with C#, .NET MAUI, and Blazor. It is available for x64, x86, and ARM64 Windows systems.

Most settings include an explanation and their default value directly inside the application. The built-in Health Center and persistent diagnostic logs can help identify connection, authentication, startup, and configuration problems.

## Features

- **Twitch integration**: Connect your broadcaster account and optionally use a separate bot account for chat messages.
- **Chat commands**: Control playback, request songs, display information, and customize command triggers and responses.
- **Channel Point rewards**: Bind commands to rewards and automatically approve or refund redemptions based on their result.
- **Song request queue**: Review, reorder, remove, and automatically play songs requested by viewers.
- **Blacklist**: Prevent selected songs from being requested or started through Twitch commands.
- **Bits support**: Require Twitch Bits before selected commands can be used.
- **Browser-source widgets**: Display information about the currently playing song in OBS Studio or other streaming software.
- **Independent widget server**: Keep widgets available independently from the current YTMDesktop connection.
- **Health Center and diagnostics**: Inspect the state of important services and access persistent logs for troubleshooting.
- **Automatic settings migration**: Existing settings from older versions are imported automatically when upgrading.
- **Automatic updates**: Installed versions can check for and install application updates.
- **Installer and portable builds**: Choose the distribution format that fits your setup.
- **Free and open source**: Review the source code, report issues, and contribute through GitHub.

## Guides

{% for page in list_pages_in('guides') %}
- [{{ page.title }}]({{ page.url }}){% if page.description %} - {{ page.description }}{% endif %}
{% endfor %}

## Setup

To get started:

1. Download the appropriate build from the [releases page][ytms-download].
2. Install or extract YouTube Music Streamer.
3. Install and configure [YTMDesktop][YouTube Music Desktop App].
4. Connect the application to YTMDesktop and Twitch.
5. Add any desired widgets as browser sources in your streaming software.

You need a Twitch account to use Twitch commands, Bits, Channel Point rewards, or song requests. A separate Twitch account can optionally be connected as a dedicated chat bot.

Existing settings from previous versions are migrated automatically during the first startup after upgrading.

!!! warning "Release assets"
    GitHub may initially hide some files on the release page. Select **Show all assets** to display every available installer and portable build.

## Contributing

Contributions are welcome. You can open an issue or pull request on GitHub, or join the [Discord Server][] to discuss features, report problems, or ask questions.

See the [Contributing Guide][ytms-contributing-guide] for development and contribution instructions.

## Code of Conduct

This project follows an adapted version of the Contributor Covenant. See [CODE_OF_CONDUCT.md][ytms-code-of-conduct] for the complete policy.

Contributors and community members are expected to follow it to maintain a welcoming and constructive environment.

## License

YouTube Music Streamer is licensed under the GNU Affero General Public License v3.0. See [LICENSE][ytms-license].

Additional permissions and exceptions are documented in [ADDITIONAL-PERMISSIONS][ytms-additional-license].
