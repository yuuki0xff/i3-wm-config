from i3pystatus import Status

status = Status(standalone=True)

status.register("clock",
    format="%Y-%m-%d %H:%M %A")

status.register("load",
        format="Load {avg1}")

status.register("mem",
        format="MEM {avail_mem} MiB")

status.register("shell",
    command="hostname")

status.register("xkblayout")

status.run()
# vim: tabstop=4 expandtab shiftwidth=4
