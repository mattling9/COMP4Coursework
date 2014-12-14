import smtplib
import random

code = random.randint(1000,9999)
print(code)

content = '{0}'.format(code)

mail = smtplib.SMTP('smtp.gmail.com','587')

mail.ehlo()

mail.starttls()

mail.login('mattling147@gmail.com','alienware')

mail.sendmail('mattling147@gmail.com','mattling9@hotmail.co.uk',content)

mail.close()
