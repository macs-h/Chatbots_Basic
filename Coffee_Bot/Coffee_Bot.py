#!/usr/bin/env python
"""Simple coffee ordering chatbot.

Prompts user for input to find out what coffee the user wants to order.
"""
__author__ = "Max Huang"
__version__ = "1.0"


# Initial greeting function, then gets the order.
def coffee_bot():
  print("Welcome to the cafe!")
  get_order()
    

# Gets the full order, asks for name, and also prompts user for another order.
def get_order():
  size = get_size()
  drink_type = get_drink_type()
  print("\nAlright, that's a "+size+" "+drink_type)

  name = input("Can I get your name please?\n> ")
  print("\nThanks, "+name.capitalize()+"! Your drink will be ready shortly.")

  another_order = input("Can I get you anything else today?\n[a] Yes\n[b] No\n> ")
  if another_order.casefold() == 'a' or another_order.casefold() == 'yes':
    get_order()


# Gets the size of the coffee
def get_size():
  res = input("What size drink can I get for you?\n[a] Small\n[b] Medium\n[c] Large\n> ")
  if res.casefold() == 'a' or res.casefold() == "small":
    return "Small"
  elif res.casefold() == 'b' or res.casefold() == 'medium':
    return "Medium"
  elif res.casefold() == 'c' or res.casefold() == 'large':
    return "Large"
  else:
    print_message()
    return get_size()


# Message to prompt user when invalid input is received.
def print_message():
  print("\nI'm sorry, I did not understand your selection.")
  print("Please enter the corresponding letter or value for your response")


# Gets the type of drink
def get_drink_type():
  res = input("\nWhat type of drink would you like?\n[a] Black Coffee\n[b] Mocha\n[c] Latte\n> ")
  if res.casefold() == 'a' or res.casefold() == "black coffee":
    return "Black coffee"
  elif res.casefold() == 'b' or res.casefold() == 'mocha':
    return "Mocha"
  elif res.casefold() == 'c' or res.casefold() == 'latte':
    return "Latte with " + order_latte()
  else:
    print_message()
    return get_drink_type()


# If user orders a latter, ask what kind of milk they would like.
def order_latte():
  res = input("\nAnd what kind of milk for your latte?\n[a] 2% milk\n[b] Non-fat milk\n[c] Soy milk\n> ")
  if res.casefold() == 'a' or res.casefold() == "2% milk":
    return "2% milk"
  elif res.casefold() == 'b' or res.casefold() == 'non-fat milk':
    return "Non-fat milk"
  elif res.casefold() == 'c' or res.casefold() == 'soy milk':
    return "Soy milk"
  else:
    print_message()
    return order_latte()


# Main function.
if __name__ == "__main__":
  coffee_bot()
