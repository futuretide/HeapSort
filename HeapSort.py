def heapsort(MyList):
  m = len(MyList)
  for i in range(m//2, -1, -1):
    heapify(MyList, n-1, i)

  for i in range(m-1, -1, -1):
    # swapping last element with the first element
    MyList[i], MyList[0] = MyList[0], MyList[i]
   
    # exclude the last element from the heap
    heapify(MyList, i-1, 0)
