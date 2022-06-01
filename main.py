import random
from art import vs, logo
import clear
from game_data import data

print(logo)

# def person_1():
#   account = random.choice(data)
#   #print(random_account)
#   format_data = list(account.values())
#   print(f"Compare A: {format_data[0]}, {format_data[2]}, {format_data[3]}. ")
  
# def person_2():
#   account = random.choice(data)
#   #print(random_account)
#   format_data = list(account.values())
#   print(f"Against B: {format_data[0]}, {format_data[2]}, {format_data[3]}. ")  


# person_1()

# print(vs)

# person_2()

# choice = input("Who has more followers? Type 'A' or 'B': ").lower()
def account():
  account1 = random.choice(data)
  name = account1['name']
  description = account1['description']
  country = account1['country']
  follower_count_1 = account1['follower_count']
  print (f"Compare A: {name}, a {description} from {country}. ")
  account2 = random.choice(data)
  name = account2['name']
  description = account2['description']
  country = account2['country']
  follower_count_2 = account2['follower_count']
  print(vs)
  print (f"Against B: {name}, a {description} from {country}.")

  

  choice = input("Who has more followers? Type 'A' or 'B': ")
  if choice == 'A':
    if follower_count_1 > follower_count_2:
      print(" You are right")
    else:
      print("You are wrong")
  elif choice == 'B':
    if follower_count_1 < follower_count_2:
      print(" You are right")
    else:
      print("You are wrong")
  else:
    return None
    
account()




