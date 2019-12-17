import heapq
#used to represent a priority queue
#each time the smallest of heap element is popped(min heap)
#whenever elements are pushed or popped, heap structure is mantained
# heap[0] is the smallest element each time

li= [5,7,100,4,1,2,10]

heapq.heapify(li)
print(list(li))
heapq.heappush(li,6)
print(list(li))
print(heapq.heappop(li))
print(list(li))