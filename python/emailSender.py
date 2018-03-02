import smtplib
content = 'Happy Hacking'
mail    = smtplib.SMTP('smtp.gmail.com', 587)
mail.ehlo()
mail.starttls()
mail.login('emailaddress@gmail.com', 'password')
mail.sendmail('sender@gmail.com', 'receiver@gmail.com', content)
mail.close()