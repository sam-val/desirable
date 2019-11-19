import os
import sys


def sign_in():
     global logged_in
     global message
     if logged_in is False:
          username = input("Username: ")
          password = input("Password: ")
          username.strip()
          password.strip()
          with open('accounts.txt', 'r') as f:
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
                    with open('accounts.txt', 'r+') as f:
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

          with open('accounts.txt', 'a+') as f:
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
     global points
     global message
     if logged_in is True:
          point = input("how desirable you are: ")
          points = float(point)
          if points > 10:
               message = "---you are desirable!---"
          else:
               message = "---You are not at all desirable. Perhaps play again?---"
     elif logged_in is False:
          message = "---Please sign in to play---"

def switch(x):
     return choices.get(x, default)()

def program(instruction, message):
     clear_screen = lambda: os.system('cls' if os.name == 'nt' else 'clear')
     clear_screen()
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
points = 0
instruction = "Type:\n0 to end program\n1 to sign in\n2 to create an account\n3 to sign out\n4 to play game"
dir_path = os.path.dirname(os.path.realpath(__file__))
accounts_file_path = dir_path+'/accounts.txt'

if not os.path.exists(accounts_file_path):
     accounts = open('accounts.txt', 'x')
     accounts.close()

while True:
     program(instruction, message)



