'''
Chalenge: Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
'''

# Random List generator:
import random

x = random.randrange(0,25)
y = random.randrange(0,25)

nums1 =  [random.randrange(1, 50, 1) for i in range(y)]
nums2 = [random.randrange(1, 50, 1) for i in range(x)]

'''  
Solution ( in leetcode there's a class based solution system but you can consider everything inside the function as a valid answer in their model.
The variables (nums1, nums2) are compatible with they're random list system
'''

def findMedianSortedArrays(nums1, nums2) -> float:
    for i in nums2:
        nums1.append(i)
    
    nums1.sort()

    if len(nums1) % 2 == 0:
        metade = int(len(nums1) / 2)
        numero1 = nums1[metade - 1]
        numero2 = nums1[metade]
        resultado = (numero1 + numero2) / 2
    else:
        meio = len(nums1) / 2
        mediana = meio - 0.5
        conversao = int(mediana)
        resultado = nums1[conversao]
    return resultado

