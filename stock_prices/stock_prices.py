#!/usr/bin/python

import argparse

def find_max_profit(prices):
      # declare value for max profit as negative infinity 
      max_profit_so_far = float('-inf')
      # declare value for min price as positive infinity
      
      # Traverse through all prices in list starting from first price
      for i in range(0, len(prices)):
            # Traverse through list beginning with second price
            for j in range(i + 1, len(prices)):
                  #  if max profit so far is less than the current price - the current minimum price so far
                  # max profit so far = current price - current minimum price 
                  if prices[j] - prices[i] > max_profit_so_far:
                        max_profit_so_far = prices[j] - prices[i]

      return max_profit_so_far
      

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))