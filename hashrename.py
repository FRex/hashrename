#!/usr/bin/env python3
import hashlib
import sys
import os


def mysplitext(fpath: str) -> tuple:
    """Returns a tuple of dirpath, filename, and all extensions (not just 1)."""
    dpath, fname = os.path.split(fpath)
    try:
        idx = fname.index(".", 1)  # handle hidden files correctly
    except ValueError:
        idx = len(fname)  # if no dots found then make extension empty str
    return dpath, fname[:idx], fname[idx:]


def myhashfile(fpath: str) -> str:
    """Similar to hashlib.file_digest from 3.11 and up."""
    ret = hashlib.sha1()  # TODO: make this an option later?
    with open(fpath, "rb") as fhandle:
        while True:
            data = fhandle.read(1024 * 1024)
            if not data:
                break
            ret.update(data)
    return ret.hexdigest()


def handle_file(fpath: str) -> None:
    digest = myhashfile(fpath)[:20]
    dpath, fname, extensions = mysplitext(fpath)
    if fname.endswith(f"-{digest}"):
        print(f"{fpath} already ends with -{digest} - skipping.")
        return

    if fname == digest:
        print(f"{fpath} already is named just {digest} - skipping.")
        return

    goalpath = os.path.join(dpath, f"{fname}-{digest}{extensions}")
    try:
        os.rename(fpath, goalpath)
        print(f"{fpath} renamed to {goalpath}")
    except FileExistsError as err:
        print(err)


def main():
    for fname in sys.argv[1:]:
        try:
            handle_file(fname)
        except FileNotFoundError as err:
            print(f"{err}")


if __name__ == "__main__":
    main()
