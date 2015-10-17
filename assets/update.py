#!/usr/bin/python
#-*- coding: utf-8 -*-

import os
import sys
from urllib import urlretrieve

url = "https://raw.githubusercontent.com/tomghuang/tomghuang.github.io/master/assets/update.py"

def report_hook(block_num, block_size, total_size):
    readsofar = block_num * block_size
    if total_size > 0:
        percent = readsofar * 1e2 / total_size
        s = "\r%5.1f%% %*d / %d" % (
                percent, len(str(total_size)), readsofar, total_size)
        sys.stderr.write(s)
        if readsofar >= total_size:
            sys.stderr.write("\n")
    else:
        sys.stderr.write("read %d\n" % (readsofar,))


if __name__ == "__main__":
    local_file_path = os.path.realpath(__file__)
    urlretrieve(url, local_file_path, report_hook)
