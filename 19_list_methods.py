# different list methods
l1 = [1, 2, 1024, 4, 8, 64, 16, 32, 128, 256, 512]
print(l1)

# 1.    list.sorted
l1.sort()
print(l1)

# 2.    list.append
l1.append(2048)
print(l1)

# 3.    list.reverse
l1.reverse()
print(l1)
l1.reverse()
print(l1)

# 4.    list.insert
l1.insert(0,0) #this will add 0 at index 0.
print(l1)

l2 = [1,3,4,5,6,7,8,9]
print(l2)
l2.insert(1,2) #this will add 2 at index 1.
print(l2)

# 5.    list.pop
l1.pop(5) #this will delete element at index 5.
print(l1)

# 6.    list.remove
l1.remove(256) #this will delete that particular element from the list.
print(l1)

# 7.    list.clear and del, BOTH YIELDS SAME RESULT
l2.clear() #this will delete all elements from the list.
print(l2)
l2 = [100, 222, 334, 510]
print(l2)
del l2[:]
print(l2)

# 8.    list.count
l3 = [100, 200, 300, 400, 100, 200, 500]
print(l3)
print(l3.count(100))

'''OUTPUT'''

# [1, 2, 1024, 4, 8, 64, 16, 32, 128, 256, 512]
# [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
# [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]        
# [2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]           
# [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]        
# [0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]     
# [1, 3, 4, 5, 6, 7, 8, 9]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# [0, 1, 2, 4, 8, 32, 64, 128, 256, 512, 1024, 2048]
# [0, 1, 2, 4, 8, 32, 64, 128, 512, 1024, 2048]
# []
# [100, 222, 334, 510]
# []
# [100, 200, 300, 400, 100, 200, 500]                        >        
# 2
