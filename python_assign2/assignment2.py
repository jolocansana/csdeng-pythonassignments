def getAddends(list, sum):
  addends = []
  for index, x in enumerate(list):
    for y in list[index+1:]:
      if x + y == sum:
        addends.append(f'{x} and {y}')
  print(addends)

def main():
  mylist = [1,2,3,4,5] # example given
  sum = 7
  getAddends(mylist, sum)

  mylist = [1,2,3,4,5,6,7,8,9,1,2,3,4,5] # example with repeating numbers
  sum = 10
  getAddends(mylist, sum)

  
if __name__=="__main__":
  main()