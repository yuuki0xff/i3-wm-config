#!/usr/bin/python3
import hashlib
import io
import os
import pathlib
import subprocess
import sys
import tempfile
import typing


def get_cache_file_path() -> pathlib.Path:
    cache_dir = pathlib.Path(
        os.environ.get("XDG_CACHE_HOME", os.path.expanduser("~/.cache"))
    )
    cache_dir.mkdir(parents=True, exist_ok=True)
    path_digest = hashlib.sha1(os.environ.get("PATH", "").encode("utf-8")).hexdigest()
    return cache_dir / f"dmenu_run-{path_digest}"


class AppListCache:
    __slots__ = ("cache_file", "paths")

    def __init__(self, cache_file: pathlib.Path, path: str):
        self.cache_file = cache_file
        self.paths = path.split(os.pathsep)

    def update_if_needed(self):
        if self.is_need_update():
            self.update()

    def is_need_update(self) -> bool:
        if not self.cache_file.exists():
            return True

        cmd = ["stest", "-dqr", "-n", str(self.cache_file.absolute())] + self.paths
        result = subprocess.run(cmd)
        if result.returncode not in (0, 1):
            # the stest command failed.
            result.check_returncode()

        if result.returncode == 0:
            # bin directories are newer than cache file.
            return True

        # bin directories are older than cache file.
        # It means that the cache is up-to-date.
        assert result.returncode == 1
        return False

    def update(self):
        with tempfile.TemporaryFile() as tmp, tempfile.NamedTemporaryFile(
            dir=self.cache_file.parent, prefix=self.cache_file.name
        ) as f:
            # List all available command names.
            subprocess.run(["stest", "-flx"] + self.paths, stdout=tmp, check=True)
            tmp.seek(0, io.SEEK_SET)
            tmp.flush()
            # Sort and dedup command names.
            subprocess.run(["sort", "-u"], stdin=tmp, stdout=f, check=True)
            f.flush()
            # Replace the cache file.
            self.cache_file.unlink(missing_ok=True)
            self.cache_file.hardlink_to(f.name)

    def print_list(self, out: typing.TextIO):
        with self.cache_file.open() as f:
            out.writelines(f.readlines())


def main():
    cache_file = get_cache_file_path()
    cache = AppListCache(cache_file, os.environ.get("PATH", ""))
    cache.update_if_needed()
    cache.print_list(sys.stdout)


if __name__ == "__main__":
    main()
