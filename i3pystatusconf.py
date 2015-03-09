import subprocess

from i3pystatus import Status

status = Status(standalone=True)

# Displays clock like this:
# Tue 30 Jul 11:59:46 PM KW31
status.register("clock",
    format="%a %-d %b %Y %X",)

# Shows the average load of the last minute and the last 5 minutes
# (the default value for format is used)
status.register("load")

# Shows disk usage of /
# Format:
# 42/128G [86G]
status.register("disk",
    path="/",
    format="{avail}G",)

status.register("disk",
    path="/data",
    format="{avail}G",)

status.register("disk",
    path="/tmp",
    format="{avail}G",)

# Shows pulseaudio default sink volume
#
# Note: requires libpulseaudio from PyPI
status.register("alsa",
    format="♪ {volume}",)

status.register("text",
    text="Sleep Screen",
    cmd_leftclick="sleep 1; xset dpms force off",
    color="#44bbff")

status.run()
# vim: tabstop=4 expandtab shiftwidth=4
