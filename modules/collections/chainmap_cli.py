import os, argparse,collections

defaults ={'color':'red','user':'guest'}
parser=argparse.ArgumentParser()
parser.add_argument('-u','--user')
parser.add_argument('-c','--color')

#a simple Namespace object will be built up from attributes parsed out of the command lin

namespace= parser.parse_args()
command_line_args= {k: v for k , v in vars(namespace).items()if v is not None}

combined= collections.ChainMap(command_line_args,os.environ,defaults)

print(combined['color'])
print(combined['user'])