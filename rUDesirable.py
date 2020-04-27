import os
import sys
import time
import random

def sign_in():
     global logged_in
     global message
     if logged_in is False:
          username = input("Username: ")
          password = input("Password: ")
          username.strip()
          password.strip()
          with open(accounts_file_path, 'r') as f:
               if ("{"+username+":"+password+"}") not in f.read():
                    message = "Wrong username or password"
               else:
                    logged_in = True
                    message = "---You're signed in---"

     else:
          message = "You're already logged in"

def sign_out():
     global logged_in
     global message
     if logged_in is True:
          logged_in = False
          message = "---You've logged out---"
     else:
          message = "---You're already signed out---"

def create_account():
     global message
     confirm = input("Are you sure you want to create an account? (type 'no' to get out): ").strip().lower()
     if (confirm != 'no') and (confirm != 'n'):
          while True:
                print("")
                username = input("Enter username: ")
                username.strip()
                if '{' in username or ':' in username or '}' in username:
                     print("Username should not contain '{', '}' or ':' character!")
                else:
                    with open(accounts_file_path, 'r+') as f:
                         if '{'+username+':' not in f.read():
                              break
                         else:
                              print("username exists")

          while True:
               password = input("Enter password: ").strip()
               if '{' in password or ':' in password or '}' in password:
                    print("---Password can not contain '{', '}' or ':' character!---")
               else:
                    password2 = input("---Re-enter password: ").strip()
                    if password == password2:
                         break
                    else:
                         print("---Password reentered incorrectly---")

          with open(accounts_file_path, 'a+') as f:
               f.write('{{{}:{}}}'.format(username, password))

          message = "---you just created an account---"

     else:
          message = "---you need an account and sign in to play the game---"
          return

def default():
     global message
     message = "---invalid input---"
def end_program():
     sys.exit(0)
def play_game():
     global logged_in
     global message
     unvalid_num = 0
     points = 0
     in_game_message = 'How old are you (please enter a number): '
     if logged_in is True:
          while True:
               class TooOld(Exception):
                    pass
               question1 = input(in_game_message)
               try:
                    answer1 = float(question1)
                    if answer1 <= 0:
                         raise ValueError
                    elif answer1 >= 120:
                         raise TooOld
                    elif 0 < answer1 < 18:
                         print("You're too young, didn't you know this game is 18+ ?")
                         break
                    elif 18 <= answer1 <= 30:
                         print("Good! You are young, must feel great!")
                         points += 2
                         break
                    elif 30 < answer1 < 50:
                         print("Your skin is having wrinkles.")
                         points += 1
                         break
                    elif answer1 >= 50:
                         print("I'm sorry...")
                         points -= 1
                         break
               except ValueError:
                     in_game_message = "Please enter a valid number: "
                     unvalid_num += 1
                     if unvalid_num >= 3:
                          points -= 1
               except TooOld:
                    in_game_message = "What are you? A vampire? Enter your real age please: "
                    points -= 1

          in_game_message = "Next question, how much money do you really make a year in US Dollars: "
          while True:
               class TooMuchMoney(Exception):
                    pass
               question2 = input(in_game_message)
               try:
                    answer2 = float(question2)
                    if answer2 < 0:
                         raise ValueError
                    elif answer2 >= 100000000:
                         raise TooMuchMoney
                    elif 0 <= answer2 < 3000:
                         print("\nI know, I know, I cry sometimes too...")
                         points -= 3
                         break
                    elif 3000 <= answer2 <= 10000:
                         print("\nWell at least you make more than the homeless...")
                         points -= 2
                         break
                    elif 10000 < answer2 < 35000:
                         print("\nYou are categorized within the LOWER CLASS")
                         points -= 1
                         break
                    elif 35000 <= answer2 < 100000:
                         print("\nYou are categorized within the MIDDLE CLASS")
                         break
                    elif 100000 <= answer2 < 300000:
                         print("\nYou are categorized within the UPPER CLASS")
                         points += 1
                         break
                    elif 300000 <= answer2 < 500000:
                         print("\nYou're doing real well, care to give me some money?")
                         points += 2
                         break
                    elif 500000 <= answer2 < 1000000:
                         print("\nYou rich bastard!")
                         points += 3
                         break
                    elif answer2 >= 1000000:
                         print("\nI can see money coming out of your a**hole from here.")
                         points += 4
                         break
               except ValueError:
                    in_game_message = "Please enter a valid number: "
                    if unvalid_num >= 4:
                         points -= 1
               except TooMuchMoney:
                    in_game_message = "Please, Enter the amount you make not the amount you want to make:"
          in_game_message = "Last question, how do you rate yourself from 1 to 10 in terms of perfection: "
          while True:
               class NarcissismException(Exception):
                    pass
               question3 = input(in_game_message)
               try:
                    answer3 = float(question3)
                    if answer3 < 1:
                         raise ValueError
                    elif answer3 > 10:
                         raise NarcissismException
                    elif 1 <= answer3 < 4:
                         print("\nThat's okay, a lot people don't think they are attractive")
                         points += 2
                         break
                    elif 4 <= answer3 < 7:
                         print("\nYou are pretty much average")
                         points += 1
                         break
                    elif 7 <= answer3 <= 9:
                         print("\nIf you think so...")
                         points -= 1
                         break
                    elif answer3 == 10:
                         print("\nIf you're so perfect then I'm sure you won't mind never winning this game---")
                         points = 0
                         break
               except ValueError:
                    in_game_message = "Please enter a valid number: "
               except NarcissismException:
                    in_game_message = "Narcissist Detected! One Point Forfeited...\nNow just rate yourself between 1 and 10 please: "
                    points -= 1
          time.sleep(3)
          calculate_message = "Calculate"
          timeout = time.time() + random.randrange(3, 5)
          while True:
               clear_screen = lambda: os.system('cls' if os.name == 'nt' else 'clear')
               clear_screen()
               print(calculate_message)
               time.sleep(0.5)
               calculate_message += "."
               if calculate_message.endswith("...."):
                    calculate_message = "Calculate"
               if time.time() > timeout:
                    break

          if points >= 5:
               message = "---Your points are: "+str(points)+"\nYou are desirable!---"
          else:
               message = "---Your points are: "+str(points)+"\nYou are not at all desirable. Perhaps play again?---"
     elif logged_in is False:
          message = "---Please sign in to play---"

def switch(x):
     return choices.get(x, default)()

def program(instruction, message):
     clear_screen = lambda: os.system('cls' if os.name == 'nt' else 'clear')
     clear_screen()
     print(accounts_file_path)
     print(instruction)
     print(message)
     choice = input("Type your option: ")
     switch(choice)

choices = {
    '0': end_program,
    '1': sign_in,
     '2': create_account,
     '3': sign_out,
     '4': play_game
}

print("\nWelcome to 'Are You Desirable?'".upper())
logged_in = False
message = "---You're not signed in---"
instruction = "Type:\n0 to end program\n1 to sign in\n2 to create an account\n3 to sign out\n4 to play game"
dir_path = os.path.dirname(os.path.realpath(__file__))
accounts_file_path = dir_path+'/accounts.txt'
if not os.path.exists(accounts_file_path):
     accounts = open(accounts_file_path, 'x')
     accounts.close()

while True:
     program(instruction, message)



