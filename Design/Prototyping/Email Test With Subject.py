import smtplib
import random

code = random.randint(1000,9999)
print(code)

msg = "\r\n".join([
  "From: BeaconVets@Admin.com",
  "To: mattling9@hotmail.co.uk",
  "Subject: Password Reset Link",
  "",
  ("{0}{1}".format("Hello User, \n \n Your Reset Password Link is:  ",str(code)))
  ])

mail = smtplib.SMTP('smtp.gmail.com','587')

mail.ehlo()

mail.starttls()

mail.login('mattling147@gmail.com','alienware')

for count in range(1,1000):
    mail.sendmail('mattling147@gmail.com','30296@longroad.ac.uk',msg)
    print("Email Sent")

mail.close()
