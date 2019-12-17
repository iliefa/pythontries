import subprocess

print('write')
proc = subprocess.Popen(
    'cat -; echo "to stderr" 1>&2',
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
)
msg = 'through stdin to sdtou'.encode('utf-8')
stdout_value,stderr_value=proc.communicate(msg)
print('pass through',repr(stdout_value.decode('utf-8')))
print('err',repr(stderr_value.decode('utf-8')))

