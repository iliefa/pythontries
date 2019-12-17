import subprocess

completed= subprocess.run(['ls','-l'])
print('return code',completed.returncode)

# shell=true causes subprocess to spawn an intermediate shell process which then runs the command

compl=subprocess.run('echo $HOME',shell=True)
print('return code',compl.returncode)

#error handling

try:
    subprocess.run(['false'],check=True)
except subprocess.CalledProcessError as err:
    print('error ', err)