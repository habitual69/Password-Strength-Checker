print("""
Please Enter any string that has
1: Upper Case letter(s)
2: Lower Case letter(s)
3: Special Characters from the list 
   given below: |@, #, !, %|
""")

str=input("")
if len(str)>=16:
  for x in str:
      if (x==x.upper()):
        if x==x.lower():
          if(x=='@' or x=='#' or x=='%' or x=='!'):
            print("Strong Password")
            break
  else:
    print ("Weak Password")
else:
  print("Please Enter 16 Digit Password")
