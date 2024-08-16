import re

def is_valid_email(email):
    
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
   
    if re.match(email_regex, email):
        return True
    else:
        return False


email = input("Enter an email address: ")


if is_valid_email(email):
    print(f"{email} is a valid email address.")
else:
    print(f"{email} is not a valid email address.")
