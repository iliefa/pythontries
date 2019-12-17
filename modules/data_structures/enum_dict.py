import enum

BugStatus= enum.Enum(
    value='BugStatus',
    names=[
        ('new',7),
        ('incomplete',6),
        ('invalid',5),
        ('in_progress',3),
    ],
)


print('all members')
for status in BugStatus:
    print('{:15} = {}'.format(status.name, status.value))