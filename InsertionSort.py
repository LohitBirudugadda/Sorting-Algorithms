numList = [22,32,423,423,432,52,5]

def InsertionSort(List):
  for x in range(len(List)-1):
    minValueIndex = x
    minValue = List[minValueIndex]
    for y in range(x,len(List)):
      if List[minValueIndex] > List[y]:
        minValueIndex = y
        minValue = List[minValueIndex]
    List.pop(minValueIndex)
    List.insert(x,minValue)
  print(List)

InsertionSort(numList)
