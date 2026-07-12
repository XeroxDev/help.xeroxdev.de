---
title: About / Updates
description: View build information, check for updates, access project links, and review application and third-party licenses.
---

# About / Updates

The **About** page displays information about the installed YouTube Music Streamer build, its update status, project links, and licensing information.

It is also useful when reporting a problem because it shows the exact version and commit currently running.

![YouTube Music Streamer About page](/assets/images/youtube-music-streamer/YouTubeMusicStreamer.png)

## Application information

The top section identifies the current application build.

### Build Time

**Build Time** shows when the application package was created.

This can help distinguish between different builds of the same development version.

### Version

**Version** shows the installed YouTube Music Streamer version.

Portable builds are identified with a **Portable** label beside the version.

Include this value when reporting a bug or asking for support.

### Commit

**Commit** shows the Git commit used to build the application.

This uniquely identifies the source revision and is particularly useful for development, preview, or troubleshooting builds.

## Updates

The **Updates** field shows the current state of the application updater.

Depending on the current state, it may indicate that:

- the application is up to date;
- an update is available;
- an update check failed;
- an update has been downloaded and is waiting for a restart.

Installed builds display an action button below the update status. The button changes according to the next available update action.

Portable builds are identified in the version field and do not display the installed-build update action.

### Release notes

When an update is available or waiting for a restart, a collapsible **Release notes** section appears below the application information.

It describes the features, improvements, and fixes included in the newer version.

## Project links

The About page provides direct links to:

- the project Discord server;
- the source code and issue tracker on GitHub;
- the developer's website.

These links open in your default browser.

## License

The **License** section contains the full license text for YouTube Music Streamer.

Expand the section to review the terms under which the application may be used, modified, and redistributed.

## Additional Permissions

The **Additional Permissions** section contains permissions that supplement the application's main software license.

These are legal licensing terms. They are not Twitch permissions, Windows permissions, or permissions that the application requests from your account.

## Third-Party Licenses

The **Third-Party Licenses** section lists libraries and components included with YouTube Music Streamer.

Entries may include:

- package name;
- package version;
- authors;
- copyright information;
- the detected license;
- a local or online copy of the license text.

Select a package name to open its project or package page.

When a license document is available, select its license label to open it.

!!! note
    Third-party components remain subject to their own licenses, even though they are distributed as part of YouTube Music Streamer.

## Information to include in support requests

When reporting a problem, include:

- the application version;
- whether the build is portable;
- the commit;
- the relevant update status;
- a diagnostics summary or log file when applicable.

Diagnostics and logs can be accessed from the [Logging](logging.md) page.
