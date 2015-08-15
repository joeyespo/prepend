"""
Prepends a list of files with text.
"""

import os
import sys


def prepend(prefix, ext):
    cwd = os.getcwd()
    for filename in os.listdir(cwd):
        if os.path.splitext(filename)[1] != ext:
            continue
        newname = prefix + filename
        try:
            os.rename(filename, newname)
        except Exception as ex:
            print ' *** ', ex
            continue
        print filename, '->', newname


def main():
    if len(sys.argv) <= 2:
        print 'usage: pre <filename-prefix> <extension>'
        return 1

    prepend(sys.argv[1], sys.argv[2])
    return 0


if __name__ == '__main__':
    main()
