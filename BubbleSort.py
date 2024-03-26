numList = [3, 5, 2, 1, 7, 3, 6]


def BubbleSort(List):
  for x in range(len(List) - 1):
    for y in range(len(List) - 1):
      if List[y] > List[y + 1]:
        List[y], List[y + 1] = List[y + 1], List[y]
        print(List)


BubbleSort(numList)
