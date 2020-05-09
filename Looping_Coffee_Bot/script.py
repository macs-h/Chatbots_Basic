#!/usr/bin/env python
"""
Simple coffee chatbot, using loops.
"""
__author__ = "Max Huang"
__version__ = "1.0"

from utils import get_size, get_drink_type

# Main function for chatbot.
def coffee_bot():
  order_correct = False
  more_orders = True
  drinks = []

  # Starts the order process again if the order is deemed incorrect.
  while not order_correct:

    # While the customer wants to place more orders, take more orders.
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

      # If no more orders, then break out and continue to rest of program.
      more_orders = False
    
    # If only one drink, no need to list it out. Just a one line print.
    if len(drinks) == 1:
      print("\nOkay, so I have a {} {}".format(drinks[0][0], drinks[0][1]))
    
    # If multiple drink orders, then list out for easy readability.
    else: 
      print("\nOkay, so I have:")
      for drink in drinks:
        print("- A {} {}".format(drink[0], drink[1]))
      
    # Check that the order printed out is correct.
    check_order = input("\nIs this order correct? [y/N]\n> ")

    # If the order is correct, do not take another order.
    # Move onto getting customer name.
    if check_order.casefold() == 'y':
      break

    # Order was wrong, take it again. Reset variables.
    print("\nSorry about that, let's start again.")
    more_orders = True
    drinks = []

  # Get customer name - Title case the name.
  name = input('\nCan I get your name please? \n> ')
  print('\nThanks, {}! Your order will be ready shortly.'.format(name.capitalize()))

  
if __name__ == "__main__":
  print('Welcome to the cafe!')
  coffee_bot()
