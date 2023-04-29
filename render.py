#!/usr/bin/python3
import sys
import os
import jinja2


def main(args):
    print("Loading options ...")
    kv = {}
    for a in args[1:]:
        key, value = a.split("=")
        kv[key] = value
        print(f"  {key}={value}")

    print("Rendering configuration from template ...")
    env = jinja2.Environment(loader=jinja2.FileSystemLoader("."))
    templ = env.get_template("config.tmpl")
    config = templ.render(kv)

    print("Writing to config file ...")
    try:
        os.unlink("config")
    except FileNotFoundError:
        pass
    with open("config", "w") as f:
        f.write(config)
    return 0


if __name__ == "__main__":
    exit(main(sys.argv))
