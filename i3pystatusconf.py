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
    format="sys {free}G",)

status.register("disk",
    path="/home",
    format="home {free}G",)

status.register("disk",
    path="/tmp",
    format="tmp {free}G",)

status.register("text",
    text="Sleep Screen",
    cmd_leftclick="sleep 1; xset dpms force off",
    color="#44bbff")

status.run()
# vim: tabstop=4 expandtab shiftwidth=4
