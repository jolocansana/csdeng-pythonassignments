def getAverage(sag):
  sum = 0
  for key in sag.keys():
    sum += sag[key]
  average = sum/len(sag.keys())
  print(f'{"Pass" if average >= 75 else "Failed"} - Average is {average}')

def getHighest(sag):
  highestSubj = []
  highestScore = 0
  for key in sag.keys():
    if sag[key] > highestScore:
      highestSubj = [key]
      highestScore = sag[key]
    elif sag[key] == highestScore:
      highestSubj.append(key)
  print(f'Subject/s with highest score of {highestScore}:', end = " ")
  print(*highestSubj, sep = ', ')

def main():
  subject_and_grades = {
    'communication_skills': 89,
    'programming': 95,
    'foreign_language': 79,
    'thesis': 89,
    'math': 95, # add this to the 4 to see how it handles two or more subj with same grade
    'science': 0 # add this to the 5 to see the fail condition
  }

  getAverage(subject_and_grades)
  getHighest(subject_and_grades)

if __name__=="__main__":
  main()