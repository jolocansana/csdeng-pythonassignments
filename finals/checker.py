import pandas as pd

def main():
  df = pd.read_csv("sales-data.csv")

  print(df[df.duplicated(subset=['sn'])])

if __name__ == "__main__":
  main()