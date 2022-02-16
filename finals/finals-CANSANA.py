#########################################
#       CSDENG Final Exam               #
#       Jose Lorenzo Cansana S11        #
#########################################

import pandas as pd
import json

def main():
  df = pd.read_csv("sales-data.csv")

  # 1. Remove rows with empty/null values
  df = df.dropna()

  # 2.A Sort df by sn and date ascending
  df = df.sort_values(by=['sn','date'])

  # 2. Drop duplicates based on sn. Retain the latest date.
  df = df.drop_duplicates(subset=['sn'],keep='last')

  # 3. Add a column sales_amount = price * quantity
  # TODO: Make it better with pandas iterrows
  for index in df.index:
    df.loc[index, 'sales_amount'] = df.loc[index, 'price'] * df.loc[index, 'quantity']

  # 4. Add boolean pizza_exists where if pizza_sold is in 'sales-target.json'
  target = json.load(open('sales-target.json'))
  for index in df.index:
      df.loc[index, 'pizza_exists'] = True if df.loc[index, 'pizza_sold'] in target else False
      
  df = df[df['pizza_exists'] == True]
  df.to_csv('4output.csv', index=False)

  # 5. Get sales_amount per branch
  print("""
    ********************************************
    ********** SALES AMOUNT BY BRANCH **********
    ********************************************
  """)
  print(df.groupby(by=['branch']).sum()['sales_amount'])

  # 6. Get sales_amount per pizza sold
  print("""
    ************************************************
    ********** SALES AMOUNT BY PIZZA SOLD **********
    ************************************************
  """)
  pizza_sold = df.groupby(by=['pizza_sold']).sum()['sales_amount']
  print(pizza_sold)

  # 7. Get pizza_sold that did not achieve sales target
  print("""
    *************************************
    ********** LOW SALES PIZZA **********
    *************************************
  """)
  for index,value in pizza_sold.items():
    if value < target[index]:
      # FORMAT BBQ Chicken sales: 3600000.0 target: 4320000.0
      print(f'{index} sales: {value} target: {target[index]}')

  ###########
  # OTHERS
  ############
  # print(target)
  # print(type(pizza_sold))
  # print(df.head(10))
  # print(df[df['pizza_exists'] == False].head(10))

if __name__ == "__main__":
  main()