import re

if __name__ == '__main__':
    print("deneme")
    regex = r"[a-z1-9_-]+@[a-z]+\.[a-z]+\.*[a-z]+"
    email_str = input("Please enter your e-mail: ")
    print(email_str)

    if re.match(regex, email_str):
        print("Valid")
    else:
        print("Invalid")


