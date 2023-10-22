def coffee_bot():
  print("Welcome to the cafe!")
  size = get_size()
  drink_type = get_drink_type()
  print("Alright that\'s a {} {}!"
  .format(size, drink_type))
  name = input("Can i get your name please?")
  print("Thanks, {}! Your drink will be ready shortly.".format(name))
  

def get_size():
  res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')
  if res == 'a':
    return 'Small'
  elif res == 'b':
    return 'Medium'
  elif res == 'c':
    return 'Large'
  else:
    print_message()
    return get_size()

def print_message():
  print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")

def get_drink_type():
  res = input("What type of drink would you like? \n[a] Brewed Cofee \n[b] Mocha \n[c] Latte \n>")
  if res == 'a':
    return 'brewed coffee'
  elif res == 'b':
    return 'mocha'
  elif res == 'c':
    return order_latte()
  else:
    print_message()
    return get_drink_type()

def order_latte():
  res = input("And what kind of milk for your latte?\n[a] 2% Milk \n[b] Non-fat milk \n[c] Soy milk \n>")
  if res == 'a':
    return '2% Milk'
  elif res == 'b':
    return 'Non-fat milk'
  elif res == 'c':
    return 'soy milk'
  else:
    print_message()
    return order_latte()



coffee_bot()
