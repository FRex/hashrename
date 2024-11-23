# hashrename

A standalone script to rename a file to include a part (20 chars) of its SHA1 digest.

It **won't** rename a file that already contains entire SHA1 hash or the 20
char part, so it's idempotent, and can be used on images download online,
which often are already named by SHA1 or MD5 hash.

SHA1 is also decently fast as available in Python by default, as seen in
[https://github.com/FRex/pyhashbench](https://github.com/FRex/pyhashbench)
and every other algorithm that is faster is not a builtin, so SHA1 has a
good balance of prior use for files online, availability and speed.

# Example Usage

```
$ hashrename 96c3ff99217574aef8a24d5c50e5c45cba59b64f.txt LICENSE.txt
96c3ff99217574aef8a24d5c50e5c45cba59b64f.txt already is named 96c3ff99217574aef8a24d5c50e5c45cba59b64f - skipping.
LICENSE.txt renamed to LICENSE-96c3ff99217574aef8a2.txt

$ hashrename 96c3ff99217574aef8a24d5c50e5c45cba59b64f.txt LICENSE-96c3ff99217574aef8a2.txt
LICENSE-96c3ff99217574aef8a2.txt already contains -96c3ff99217574aef8a2 - skipping.
```
