# In this game you will guess the follower count of various instagram account of celebs. If you will be able to guess the highest follower count then you get a score.

import random
from higher_data import data
from higher_art import logo, vs
import os

def clear_screen():
    os.system('cls')

# Display the art

print(logo)
def check_answer(guess, a_followers, b_followers):
  """Takes user guess and follower account and checks if user is correct."""
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"
     
score = 0  

game_should_continue = True
account_b = random.choice(data)

while game_should_continue == True:
  account_a = account_b
  account_b = random.choice(data)
  if account_a == account_b:
    account_b = random.choice(data)
    
  # Format the account into printable format
  def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account['name']
    account_descr = account['description']
    account_country = account['country']
    return (f"{account_name}, a {account_descr}, from {account_country}")

  
  print(f"Compare A: {format_data(account_a)}")
  print(vs)
  print(f"Against B: {format_data(account_b)}")
  
  # Ask a user for guess
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()
  a_follower_count = account_a['follower_count']
  b_follower_count = account_b['follower_count']
  is_correct = check_answer(guess, a_follower_count, b_follower_count)
  
  clear_screen()
  print(logo)
  if is_correct:
    score += 1
    print(f"You're right. Current Score: {score}")
  else:
    game_should_continue = False
    print(f"Sorry, That's wrong. Final Score: {score}")
  
  
  
  
