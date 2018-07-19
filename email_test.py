import smtplib



sender = 'forerunnerfarms@gmail.com'
psw = 'Greenl0ngneck'
send_to = 'm.delphii@gmail.com'
content = 'This email is a test'


mail = smtplib.SMTP('smtp.gmail.com:587')
mail.ehlo()
mail.starttls()
mail.login(sender, psw)
mail.sendmail(sender, send_to, content)
mail.close()

