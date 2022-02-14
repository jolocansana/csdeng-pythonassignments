import pandas as pd

def main():
  total_rows = error_rows = 0

  # Load CSV
  data = pd.read_csv('data.csv')
  total_rows = len(data.index)

  # Find duplicates and save to duped.csv
  data_dupes = data[data.duplicated()]
  error_rows += len(data_dupes.index)
  data_dupes.to_csv('duped.csv', index=False)
  # print(data_dupes)

  # Find null/empty cells and save rows to nan.csv
  data_nan = data[data.isna().any(axis=1)]
  error_rows += len(data_nan.index)
  data_nan.to_csv('nan.csv', index=False)
  # print(data_nan)

  # Check wrong data
  for x in data.index:
    # Check set duration limit to 120
    if data.loc[x, "Duration"] > 120:
      data.loc[x, "Duration"] = 120

  # print(error_rows / total_rows)
  if error_rows / total_rows > .2:
    print("The file will not be loaded as 20 percent of its contents contains errors")
    
  # Q: If in the future, the CSV File can be 100GB to 500GB in size, how would you read it using pandas?
  # A: By adding the chunksize parameter to pandas read_csv method, you can read the file and process the information per block as to not consume too much memory.

if __name__ == "__main__":
  main()
