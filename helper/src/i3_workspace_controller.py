#!/usr/bin/python3
import subprocess
import sys
import json
import math
import functools
import os
from os.path import expanduser
from tempfile import TemporaryFile

@functools.cache
def i3msg():
    if 'WAYLAND_DISPLAY' in os.environ:
        return 'swaymsg'
    if 'DISPLAY' in os.environ:
        return 'i3-msg'
    raise Exception('No display found')

def get_workspace():
    handle = subprocess.Popen(
        [i3msg(), "-t", "get_workspaces"], stdout=subprocess.PIPE
    )
    output = handle.communicate()[0]
    data = json.loads(output.decode())
    data = sorted(data, key=lambda k: k["name"])
    for i in data:
        if i["focused"]:
            return i["name"]


def get_workspaces():
    handle = subprocess.Popen(
        [i3msg(), "-t", "get_workspaces"], stdout=subprocess.PIPE
    )
    output = handle.communicate()[0]
    data = json.loads(output.decode())
    data = sorted(data, key=lambda k: k["name"])
    arr = []
    for i in data:
        arr.append(i["name"])
    return arr


def move_to(num):
    subprocess.Popen(
        [i3msg(), "move container to workspace " + str(num)], stdout=subprocess.PIPE
    )


def go_to(num):
    subprocess.Popen([i3msg(), "workspace " + str(num)], stdout=subprocess.PIPE)


def dmenu_fetch(inputstr):
    t = TemporaryFile()
    t.write(bytes(inputstr, "UTF-8"))
    t.seek(0)
    dmenu_run = subprocess.Popen(["dmenu", "-b"], stdout=subprocess.PIPE, stdin=t)
    output = (dmenu_run.communicate()[0]).decode().strip()
    return output


def open_app(workspace):
    apps = subprocess.Popen(["i3-list-apps"], stdout=subprocess.PIPE)
    dmenu_run = subprocess.Popen(
        ["dmenu", "-b"], stdout=subprocess.PIPE, stdin=apps.stdout
    )
    output = (dmenu_run.communicate()[0]).decode().strip()
    if dmenu_run.returncode or len(output) == 0:
        # dmenu failed or canceled. Stop launching an app.
        return

    subprocess.Popen(
        [
            i3msg(),
            f"workspace {workspace}; "
            # Some app writes many logs to stdout or stderr. To prevent flooding journal log with useless messages,
            # redirect all input and output to /dev/null.
            # First exec command is the i3 command. Second exec command is shell built-in command.
            f"exec exec {output} </dev/null >/dev/null 2>&1",
        ],
        stdout=subprocess.PIPE,
    )


def main():
    if len(sys.argv) < 1:
        print("Error not enough arguments")

    command = sys.argv[1]
    switch_number = 1  # default switch number
    if len(sys.argv) == 3:
        # they passed in a number to move to
        try:
            switch_number = int(sys.argv[2])
        except ValueError:
            pass
    # get the workspace number
    workspace_name = get_workspace()
    workspace_val = 1  # default value if name parseing fails
    workspace_prefix = ""
    try:
        match_set = "0123456789-"
        # only look for digits in the number
        workspace_val = int("".join(filter(lambda x: x in match_set, workspace_name)))
        # include - in the ignore list incase it is a negative number
        workspace_prefix = "".join(filter(lambda x: x not in match_set, workspace_name))
    except ValueError:
        pass
    print(workspace_prefix)
    # handle the commands
    if command == "up":
        workspace_val += 10
    elif command == "down":
        workspace_val -= 10
    elif command == "next":
        workspace_val += 1
    elif command == "prev":
        workspace_val -= 1
    elif command == "go":
        # go to workspace in block
        workspace_rounded = int(math.floor(workspace_val / 10)) * 10
        workspace_rounded += switch_number
        go_to(workspace_prefix + str(workspace_rounded))
    elif command == "move":
        # move the current container to the selected workspace
        workspace_rounded = int(math.floor(workspace_val / 10)) * 10
        workspace_rounded += switch_number
        move_to(workspace_prefix + str(workspace_rounded))
    elif command == "open":
        open_app(workspace_name)
    elif command == "dynamic":
        # dynamic tagging
        command2 = sys.argv[2]
        workspaces = get_workspaces()
        inputstr = "\n".join(workspaces)
        result = dmenu_fetch(inputstr)
        if command2 == "go":
            go_to(result)
        elif command2 == "move":
            move_to(result)

    if len(sys.argv) == 3:
        # not a go or move, command2 is argv2
        command2 = sys.argv[2]
        if (
            command == "up"
            or command == "down"
            or command == "prev"
            or command == "next"
        ):
            if command2 == "go":
                go_to(workspace_prefix + str(workspace_val))
            elif command2 == "move":
                move_to(workspace_prefix + str(workspace_val))


if __name__ == "__main__":
    main()
