numList = [1,2,4,2,5,3,5,3,7]

def CountingSort(List):
  countList = [0] * (max(List)+1)
  while len(List) > 0:
    countList[List[0]] += 1
    numList.pop(0)
  for nums in countList:
    for num in range(0,nums):
      numList.append(countList.index(nums))
    countList[countList.index(nums)] = 0
  return numList

print(CountingSort(numList))
