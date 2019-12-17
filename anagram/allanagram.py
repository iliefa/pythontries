test_list = [10,4,5,8,11]

print("original list"+ str(test_list))
flag = 0
if (all(test_list[i]<=test_list[i+1] for i in range(len(test_list)-1))):
    flag = 1

if (flag):
    print("list is sorted")
else :
    print("list is not sorted")

#The all() method returns:
# True - If all elements in an iterable are true
#any() -> Returns true if any of the items is True.