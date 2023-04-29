#!/usr/bin/env python3
import glob
import os.path
from i3pystatus import Status


def list_battery():
    return [os.path.basename(d) for d in glob.glob("/sys/class/power_supply/BAT*")]


def is_laptop():
    return "laptop" in os.uname().nodename


def main():
    status = Status(standalone=True)
    status.register("clock", format="%Y-%m-%d %H:%M %A")

    if list_battery():
        status.register("battery", format="BAT {status} {percentage:.0f}%")

    if is_laptop():
        status.register(
            "network",
            interface="wlp2s0",
            format_up="WiFi {v4cidr} {kbs}",
            format_down="WiFi ❌",
        )

    status.register("load", format="Load {avg1}")
    status.register("mem", format="MEM {avail_mem} MiB")
    status.register("shell", command="hostname")
    status.register("xkblayout")
    status.run()


if __name__ == "__main__":
    main()
