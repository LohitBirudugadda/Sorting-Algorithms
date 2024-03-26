numList = [3, 7, 2, 5, 2, 1, 6, 8, 1, 3, 9]


def QuickSort(List):
  if len(List) <= 1:
    return List
  pivot = List[0]
  lesser = []
  greater = []
  for nums in List[1:]:
    if nums <= pivot:
      lesser.append(nums)
    else:
      greater.append(nums)
  return QuickSort(lesser) + [pivot] + QuickSort(greater)


print(QuickSort(numList))
