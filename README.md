# i3-wm-config by yuuki0xff

This is my configuration for the i3 window manager and sway compositor. This is based on [benkaiser/i3-wm-config](https://github.com/benkaiser/i3-wm-config).  

Uses xterm as the terminal.  

I would recommend just copying parts of my config (as certain parts, such as the start up config, may be irrelevant to you). However helper scripts is universal.  


# Keybindings
Keys to use with $mod:  
http://www.keyboard-layout-editor.com/#/gists/69ee62f173f68a53777ec2ceace85091

Keys to use with $mod+Shift:  
http://www.keyboard-layout-editor.com/#/gists/d103877c434b5f074111a17d837a22d8


# Dependencies

Common dependencies:
- dmenu - for menu operations
- amixer - command-line mixer for ALSA soundcard driver
- pulseaudio-ctl - for volume control (https://github.com/graysky2/pulseaudio-ctl)

For i3:
- i3 - the i3 window manager
- py3status - for changing the status bar
- python3 - for my workspace controller script
- scrot - screen capture tool for X11
- xbacklight - adjust backlight brightness using RandR extension
- xinput - for mouse control
- xautolock - for screen locking
- i3lock - for screen locking


For sway:
- sway - tiling Wayland compositor
- grimshot - screenshot tool for sway


# Installation

```bash
git clone github.com/yuuki0xff/i3-wm-config ~/.i3
pipx install ~/.i3/helper/

# Use Mod4 (super key) as prefix key by default.
make -C ~/.i3 build
# Use Mod1 (alt key) as prefix key.
# make -C ~/.i3 PREFIX_KEY=Mod1 build
```
