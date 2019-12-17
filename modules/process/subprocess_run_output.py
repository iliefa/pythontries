import subprocess

#pass pipe for the stdout and stderr to capture the output for later processing

completed= subprocess.run(
    ['ls','-l'],
    stdout=subprocess.PIPE,
)


print ('return code',completed.returncode)

print('Have {} bytes in stdout:\n{}'.format(
    len(completed.stdout),
    completed.stdout.decode('utf-8'))
)