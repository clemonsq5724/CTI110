"""
CTI 110
P3T2 - Choices and Menus
Clemons
9/26/23
"""
# The most simple program, with main()
def main():
 # Print the menu
  print('_'*10, 'Main Menu', '_'*10)
  print('1. Pizza')
  print('2. Shrimp')
  print('3. Tacos')

  # Let the user choose
  print('Your choise? ', end='')
  choice = int(input())
  print('You chose:', choice)

  # branch (if) pn choice 
  if choice == 1:
    option_1()
  elif choice == 2:
    option_2()
  elif choice == 3:
    option_3()
  else:
    print('Sorry, that is not an option.')


def option_1():
  print ('One large pizza coming up.')
  print('Would you like pepporoni or cheese?')
  topping = input()
  if topping == 'pepporoni':
    print('One pepporoni pizza coming up.')
  elif topping == 'cheese':
    print('One cheese pizza coming up.')
  else:
    print('Sorry we do not have', topping)




def option_2():
  print ('Basket of shrimp coming up')
  print('Would you like buffalo or garlic?')
  sauce = input()
  if sauce == 'buffalo':
    print('Basket of buffalo shrimp coming your way.')
  elif sauce == 'garlic':
    print('One basket of garlic shrimp coming your way.')
  else:
   print('Sorry, we do not have', sauce)

def option_3():
  print ('Order of tacos coming your way')
  print('Would you like rice or beans for your sides?')
  sides = input()
  if sides == "rice":
    print('Side of rice coming up.')
  if sides == 'beans':
    print('Side of beans coming up.')
  else:
    print("....are you serious smh")

def my_function():
  print ('This is my function')

# start program
main()