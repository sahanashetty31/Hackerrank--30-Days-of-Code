
# coding: utf-8

# In[2]:


import sys
n = int(input())
ar = [int(x) for x in input().split(" ")]

# Write Your Code 
swap = 0
for i in range(n):
    for j in range(n - 1):
        if ar[j] > ar[j+1]:
            temp = ar[j]
            ar[j] = ar[j+1]
            ar[j+1] = temp
            swap += 1
        
    if swap == 0:
        break
        
print("Array is sorted in " + str(swap) + " swaps.")
print("First Element: " + str(ar[0]))
print("Last Element: " + str(ar[len(ar) - 1]))

