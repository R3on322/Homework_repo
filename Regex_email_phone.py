import re
from randomtimestamp import randomtimestamp
import time

# def chek_phone(number):
#     num_ok = re.match(r'([0-9]{3})([\d-]{7})', number)
#     print(num_ok.group())
# num = 9162256413
# chek_phone(str(num))

def chek_mail(email):
    try:
        email_ok = re.match(r'^[\w.+_]+@[\w.]+$', email)
        email_ok.group()
        return True
    except AttributeError:
        return False

with open('patch.txt', 'r') as file:
    data = file.readlines()
new_data = []
new_name = input('Enter your name: ')
new_email = input('Enter your email address: ')
while chek_mail(new_email) == False:
    new_email = input('Wrong email, pls enter correct email.(Example: "abs123@gmail.com")\n')
new_subject = input("Enter your subject: ")
random_date = randomtimestamp(text=False).strftime(f"%a, %d %b %Y %H:%M:%S {time.strftime('%z')}")
for string in data:
    string = re.sub(r'(From:)(.+)(.+)$', fr'\1 {new_name} <{new_email}>', string)
    string = re.sub(r'(Date:) (.+)$', fr'\1 {random_date}', string)
    string = re.sub(r'(Subject:) (.+)$', fr'\1 {new_subject}', string)
    new_data.append(string)
for i in new_data:
    print(i.strip('\n'))
with open('patch.txt', 'w') as file:
    file.write(''.join(new_data))