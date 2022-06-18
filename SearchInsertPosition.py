'''
Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.
'''


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
      if target in nums:
        return(nums.index(target))
      else:
        lista = []
        lista2 = []
        for i in nums:
          if i > target:
            lista.append(i)

            indice = lista[0]
            troca = nums.index(indice)

            return troca

          elif i < target:
            lista2.append(i)

        return len(lista2)  
