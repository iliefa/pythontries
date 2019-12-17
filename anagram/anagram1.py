test_list = [10,4,5,8,11]

print("original list"+ str(test_list))
flag = 0
test_list1 = test_list[:]
test_list1.sort()
if (test_list1 == test_list):
    flag = 1
if (flag):
    print("list is sorted")
else :
    print("list is not sorted")