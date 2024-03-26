numList = [43, 34, 24, 3, 4, 3, 5, 2]


def SelectionSort(List):
  for x in range(len(List) - 1):
    minValIndex = x
    for y in range(x, len(List)):
      if List[minValIndex] > List[y]:
        minValIndex = y
    List[x], List[minValIndex] = List[minValIndex], List[x]
  print(List)


SelectionSort(numList)
