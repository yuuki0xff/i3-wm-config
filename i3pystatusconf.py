import glob
import os.path
from i3pystatus import Status

def list_battery():
    return [
        os.path.basename(d)
        for d in glob.glob("/sys/class/power_supply/BAT*")
    ]


status = Status(standalone=True)

status.register("clock",
    format="%Y-%m-%d %H:%M %A")

if list_battery():
    status.register("battery",
        format='{status} {percentage:.0f}%')

status.register("load",
        format="Load {avg1}")

status.register("mem",
        format="MEM {avail_mem} MiB")

status.register("shell",
    command="hostname")

status.register("xkblayout")

status.run()
# vim: tabstop=4 expandtab shiftwidth=4
