import re
from randomtimestamp import randomtimestamp
import time


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
for i in data:
    list_string = re.split(r'\s', i.rstrip('\n'))
    if 'From:' in list_string:
        list_string = ['From:', ]
        new_name = input('Enter your name: ')
        new_email = input('Enter your email address: ')
        list_string.append(new_name)
        while chek_mail(new_email) == False:
            new_email = input('Wrong email, pls enter correct email.(Example: "abs123@gmail.com")\n')
        else:
            list_string.append(f'<{new_email}>')
    if 'Date:' in list_string:
        list_string = ['Date:', ]
        random_date = randomtimestamp(text=False).strftime(f"%a, %d %b %Y %H:%M:%S {time.strftime('%z')}")
        list_string.append(random_date)
    if 'Subject:' in list_string:
        list_string = ['Subject:', ]
        new_subject = input('Enter your subject: ')
        list_string.append(new_subject)
    new_data.append(' '.join(list_string))

with open('patch.txt', 'w') as file:
    file.write('\n'.join(new_data))