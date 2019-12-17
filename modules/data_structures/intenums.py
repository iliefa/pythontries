# for enumerations where members need to behave like numbers
#to support comparisons

import enum 
class BugStatus(enum.IntEnum):
    new= 7
    incomplete= 6
    invalid = 5
    wont_fix=4
    in_progress = 3
    fix_commited = 2
    fix_released = 1

print('ordered by value')
print('\n'.join(' '+s.name for s in sorted(BugStatus)))