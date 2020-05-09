#!/usr/bin/env python
"""
Simple coffee chatbot, using loops.
"""
__author__ = "Max Huang"
__version__ = "1.0"

from utils import get_size, get_drink_type

def coffee_bot():
  order_correct = False
  more_orders = True
  drinks = []

  while not order_correct:
    while more_orders:
      size = get_size()  
      drink_type = get_drink_type()

      drink = '{} {}'.format(size, drink_type)
      print('\nAlright, that\'s a {}!'.format(drink))

      drinks.append([size, drink_type])

      another_drink = input("\nWould you like to order another drink? [y/N]\n> ")
      if another_drink.casefold() == 'y':
        print()
        continue
      more_orders = False
    
    if len(drinks) == 1:
      print("\nOkay, so I have a {} {}".format(drinks[0][0], drinks[0][1]))
    else: 
      print("\nOkay, so I have:")
      for drink in drinks:
        print("- A {} {}".format(drink[0], drink[1]))
      
    check_order = input("\nIs this order correct? [y/N]\n> ")
    if check_order.casefold() == 'y':
      order_correct = True
      break
    print("\nSorry about that, let's start again.")
    more_orders = True
    drinks = []

  name = input('\nCan I get your name please? \n> ')
  print('\nThanks, {}! Your order will be ready shortly.'.format(name.capitalize()))

  
if __name__ == "__main__":
  print('Welcome to the cafe!')
  coffee_bot()
