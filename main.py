import string
import random
from colorama import Fore, Back, Style

def menu():
  print(Back.CYAN+"""
  *********** Select Your Choice ***********
  1: Password Strength Checker.             
  2: Paswword Generator.                    
  3: To Generate Bulk Passwords.            
  ******************************************\n""")
  print(Style.RESET_ALL)
  choose = input()
  if (int(choose) == 1):
    pass_checker()
  elif (int(choose) == 2):
    pass_gen()
  elif (int(choose) == 3):
    bulk_psgen()
  else:
    print(f"You Have Enter Wrong Option {choose}")


################################## Password Checker ###############################################
def pass_checker():
  print(Fore.LIGHTBLUE_EX+"""
----------------------------------------
Enter any 16 digits string consist of:
>| Uppercase
>| Lowercase
>| Special Characters like (@, #, %, &)
----------------------------------------
""")
  str = input("")
  if len(str) >= 16:
    for x in str:
      if (x == x.upper()):
        if x == x.lower():
          if (x == '@' or x == '#' or x == '%' or x == '!' or x == '$'
              or x == '*' or x == ')' or x == '('):
            print("Seems Like a Strong Password to me")
            break
    else:
      print("Weak Password")
  else:
    print("Please Enter atleast 16 Digits Password")


################################## Password Generator #############################################
def pass_gen():
  password = ""
  res = int(input(Fore.YELLOW +"""
Enter The Length of the Password>| """))
  for i in range(res):
    random_string = ''.join(
      random.choice(string.ascii_letters + string.digits + string.punctuation))
    password += random_string
  print(Fore.GREEN+f"""
Your Strong {res} Digits password is
------------------------------------------------------------
{password}                                                 
------------------------------------------------------------
""")


############################### Bulk Password Generator #########################################
def bulk_psgen():
  password = ""
  res = int(input("""
Enter The Length of the Password>| """))
  numof = int(input("""
Enter Number of Password you need >| """))
  for x in range(numof):
    for i in range(res):
      random_string = ''.join(
        random.choice(string.ascii_letters + string.digits +
                      string.punctuation))
      password += random_string
    print(f"""
Your Strong {res} Digits password is
------------------------------------------------------------
{password}\n""")
    password = ""


menu()