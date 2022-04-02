import re

validator = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

def check_mail(email):
    if re.fullmatch(validator, email):
      print("The mail is valid.")
    else:
      print("The mail is not valid.")
  
check_mail('example@email.com')
