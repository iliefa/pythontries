import subprocess

print('write')
proc = subprocess.Popen(
    ['cat','-'],
    stdin=subprocess.PIPE,
)

proc.communicate('stdin: to sdtin'.encode('utf-8'))

