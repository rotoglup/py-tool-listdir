"""
Copyright 2020 Nicolas Lelong
SPDX-License-Identifier: Apache-2.0
"""

import json
import os
import sys

def main():
  
  path = sys.argv[1]
  storage = dict()

  for curdir, subdirs, filenames in os.walk(path):

    relroot = os.path.relpath(curdir, path)
    if len(subdirs) > 0:
      print(relroot, file=sys.stderr)

    subdirs.sort()
    filenames.sort()

    files = []
    for filename in filenames:
      filepath = os.path.join(curdir, filename)
      stat = os.stat(filepath)
      file = {
        'file': filename,
        'mtime': stat.st_mtime,
        'size': stat.st_size
      }
      files.append(file)

    storage[relroot] = {
      "path": relroot,
      "files": files
    }

  result = json.dumps(storage, indent=2, sort_keys=True)
  print(result)

if __name__ == "__main__":
  main()
