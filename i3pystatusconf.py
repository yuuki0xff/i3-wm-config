import subprocess

from i3pystatus import Status

status = Status(standalone=True)

# Displays clock like this:
# Tue 30 Jul 11:59:46 PM KW31
#                          ^-- calendar week
status.register("clock",
    format="%a %-d %b %X KW%V",)

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
    path="/home/benkaiser/HD/",
    format="{avail}G",)


status.run()
