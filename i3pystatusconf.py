from i3pystatus import Status

status = Status(standalone=True)

# Displays clock like this:
# Tue 30 Jul 11:59:46 PM KW31
status.register("clock",
    format="%a %-d %b %Y %X",)

status.register("load",
        format="Load {avg1} {avg5} {avg15}")

status.register("mem",
        format="MEM {avail_mem} MiB")

status.register("xkblayout")

status.run()
# vim: tabstop=4 expandtab shiftwidth=4
