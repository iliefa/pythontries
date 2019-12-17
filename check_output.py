#!/usr/bin/env python

import subprocess

s=subprocess.check_output(["echo","hello world"])
print(s)

#shell=treats this as command completely
print(subprocess.call("ls -l",shell=True))