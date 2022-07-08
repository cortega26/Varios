import re

validator = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

def check_mail(email):
    if re.fullmatch(validator, email):
      return "The mail is valid."
    return "The mail is not valid."

if __name__ == "__main__":
    check_mail('example@email.com')
