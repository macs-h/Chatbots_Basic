#!/usr/bin/env python
"""
Util file for a looping coffee chatbot.
"""
__author__ = "Max Huang"
__version__ = "1.0"


# Gets the full order, asks for name, and also prompts user for another order.
# def get_order():
#   size = get_size()
#   drink_type = get_drink_type()
#   print("\nAlright, that's a "+size+" "+drink_type)

#   name = input("Can I get your name please?\n> ")
#   print("\nThanks, "+name.capitalize()+"! Your drink will be ready shortly.")

#   another_order = input("Can I get you anything else today?\n[a] Yes\n[b] No\n> ")
#   if another_order.casefold() == 'a' or another_order.casefold() == 'yes':
#     get_order()


# Message to prompt user when invalid input is received.
def print_error_message():
  print("\nI'm sorry, I did not understand your selection.")
  print("Please enter the corresponding letter for your response\n")


# Gets the size of the coffee
def get_size():
  res = input("What size drink can I get for you?\n[a] Small\n[b] Medium\n[c] Large\n> ")
  if res.casefold() == 'a':
    return "small"
  elif res.casefold() == 'b':
    return "medium"
  elif res.casefold() == 'c':
    return "large"
  else:
    print_error_message()
    return get_size()


# Gets the type of drink
def get_drink_type():
  res = input("\nWhat type of drink would you like?\n[a] Black Coffee\n[b] Mocha\n[c] Latte\n> ")
  if res.casefold() == 'a':
    return "black coffee"
  elif res.casefold() == 'b':
    return order_mocha()
  elif res.casefold() == 'c':
    return "latte with " + order_latte()
  else:
    print_error_message()
    return get_drink_type()


# If user orders a latte, ask what kind of milk they would like.
def order_latte():
  res = input("\nAnd what kind of milk for your latte?\n[a] 2% milk\n[b] Non-fat milk\n[c] Soy milk\n> ")
  if res.casefold() == 'a':
    return "2% milk"
  elif res.casefold() == 'b':
    return "non-fat milk"
  elif res.casefold() == 'c':
    return "soy milk"
  else:
    print_error_message()
    return order_latte()


# If user orders a mocha, ask if they would like to try a new special.
def order_mocha():
  while True:
    res = input("\nWould you like to try our limited-edition peppermint mocha?\n[a] Sure!\n[b] Maybe next time!\n> ")
    if res.casefold() == 'a':
      return "peppermint mocha"
    if res.casefold() == 'b':
      return "mocha"
    print_error_message()

