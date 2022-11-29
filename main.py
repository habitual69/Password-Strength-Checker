import string
import random


def menu():
  choose = input("""
  *********** Select Your Choice ***********
  |\t1: Password Strength Checker          |
  |\t2: Paswword Generator.                |
  |\t3: To Generate Bulk Passwords         |
  ******************************************
  """)
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
  print("""
***************************************************************
* Enter any 16 digits string consist of Uppercase, Lowercase, *
* Special Characters like |@, #, %, &|                        *
***************************************************************
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
  res = int(input("""
Enter The Length of the Password>| """))
  for i in range(res):
    random_string = ''.join(
      random.choice(string.ascii_letters + string.digits + string.punctuation))
    password += random_string
  print(f"""
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