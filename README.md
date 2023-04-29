# i3-wm-config by yuuki0xff

This is my configuration for the i3 window manager. This is based on [benkaiser/i3-wm-config](https://github.com/benkaiser/i3-wm-config).  

Uses xterm as the terminal.  

I would recommend just copying parts of my config (as certain parts, such as the start up config, may be irrelevent to you). However my workspace_controller.py script is universal.  


# Keybindings
Keys to use with $mod:  
http://www.keyboard-layout-editor.com/#/gists/69ee62f173f68a53777ec2ceace85091

Keys to use with $mod+Shift:  
http://www.keyboard-layout-editor.com/#/gists/d103877c434b5f074111a17d837a22d8


# Dependencies

- i3 - the i3 window manager
- py3status - for changing the status bar
- dmenu - for menu operations
- python3 - for my workspace controller script
- amixer - command-line mixer for ALSA soundcard driver
- xbacklight - adjust backlight brightness using RandR extension

# Installation

```bash
git clone github.com/yuuki0xff/i3-wm-config ~/.i3
pipx install ~/.i3/helper/
```
