import pandas as pd

def main():
  total_rows = error_rows = 0

  data = pd.read_csv('data.csv')
  total_rows = len(data.index)

  # TODO: should it only check rows nearby for duplicates?
  # where is the data field
  data_dupes = data[data.duplicated()]
  error_rows += len(data_dupes.index)
  data_dupes.to_csv('duped.csv', index=False)
  # print(data_dupes)

  data_nan = data[data.isna().any(axis=1)]
  error_rows += len(data_nan.index)
  data_nan.to_csv('nan.csv', index=False)
  # print(data_nan)

  # TODO: Check wrong data
  # What is the constraints?

  # print(error_rows / total_rows)
  if error_rows / total_rows > .2:
    print("The file will not be loaded as 20 percent of its contents contains errors")

  # TODO: How do you answer the last question?


if __name__ == "__main__":
  main()