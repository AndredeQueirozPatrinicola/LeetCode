'''
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

Exemple:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
'''
'''
There are some issues about LeetCode assumptions of declared lists(when you declare a list "l1=[1,2,3]", leetcode read as a Nodelist not a regular list)
which prevents some list methods to work property. I'm working on the conversion, mean while, thats the general logic of solving the exercise.
'''
l1 = [2,4,3]
l2 = [5,6,4]

def addTwoNumbers(l1,l2): 

  finalResultStr = []
  l1strlist = []
  l2strlist = []
  l1.reverse()
  l2.reverse()

  for i in l1:
    ola = str(i)
    l1strlist.append(ola)
    l1str = ''.join(l1strlist)
    intres1 = int(l1str)

  for i in l2:
    conver = str(i)
    l2strlist.append(conver)
    l2str = ''.join(l2strlist)
    intres2 = int(l2str)

  resultint = intres1 + intres2
  resultstr = str(resultint)

  for i in resultstr:
    finalResultStr.append(i)

  finalResultStr.reverse()

  finalResult = list(map(int, finalResultStr))
  return finalResult
