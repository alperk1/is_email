import re

if __name__ == '__main__':

    regex = r"[a-z1-9_-]+@[a-z]+\.[a-z]+\.*[a-z]+"
    email_str = input("Please enter your e-mail: ")

    if re.match(regex, email_str):
        print(email_str + " is valid")
    else:
        print(email_str + " is invalid")
