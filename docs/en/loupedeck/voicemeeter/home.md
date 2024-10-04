---
title: VoiceMeeter
tags:

- plugin
- extension
- VoiceMeeter
- loupedeck

---

# VoiceMeeter

## 1. Badges

{{badges(repo='Loupedeck-plugin-VoiceMeeter', loupedeck='VoiceMeeter')}}

## 2. What is this Plugin?

With this plugin, you can easily control nearly everything about [VoiceMeeter](https://voicemeeter.com/). This turns your Loupedeck into a mixer controller for VoiceMeeter.

## 3. Supported operating systems
- [x] Windows
- [ ] MacOS
- [ ] Linux

## 4. Support / Feedback

{{feedback_section('Loupedeck-plugin-VoiceMeeter')}}

## 5. Available Actions

??? tip "Busses"
    - EQ
    - Gain
    - Mono
    - Mute
    - Sel

??? tip "Strips"
    - A1-A5
    - B1-B3
    - Comp
    - Delay
    - Fx 1 and 2
    - Gain
    - Gate
    - Mono
    - Mute
    - Pan x and y
    - PostDelay
    - PostFx 1 and 2
    - PostReverb
    - Reverb
    - Solo
??? tip annotate "Special"
    - Eject
    - Reset
    - Restart
    - Show
    - Shutdown
    - Load
    - Raw Adjustment (1) 
    - Raw Command (2) 
1. This action allows you to send a raw adjustment to VoiceMeeter. This can be useful if you want to adjust a parameter that isn't supported by the plugin yet. These are the current available settings: ![Raw Adjustment](/assets/images/guides/Loupedeck/VoiceMeeter/raw_adjustment.png)
2. This action allows you to send a raw (toggle) commands to VoiceMeeter. This can be useful if you want to execute a command that isn't supported by the plugin yet. These are the current available settings: ![Raw Adjustment](/assets/images/guides/Loupedeck/VoiceMeeter/raw_command.png)

## 6. How to use it?

1. Install [VoiceMeeter](https://voicemeeter.com/)
2. Install the Plugin from <a href="https://github.com/XeroxDev/Loupedeck-plugin-VoiceMeeter/releases">Releases</a> or from the official Loupedeck Store.
3. Add your desired actions to your Loupedeck Profile.
4. Enjoy controlling VoiceMeeter with your Loupedeck!

## 7. Links

{{links_section('Loupedeck-plugin-VoiceMeeter', 'VoiceMeeterPlugin.lplug4', 'VoiceMeeter')}}

## 8. How to contribute?

Just fork the repository and create PR's.

!!! info
    We're using [release-please](https://github.com/googleapis/release-please) to optimal release the plugin.
    release-please is following the [conventionalcommits](https://www.conventionalcommits.org) specification.
