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
