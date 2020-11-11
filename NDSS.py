import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender = 'NerdDinnerSecretSantaBot@gmail.com'
password = 'H*!R%5jE6vw3'
subject = 'Nerd Diner Secret Santa 2019'

info = [('Zach', 'zach.s.laskin@gmail.com'),
        ('Katie', 'katiejhseifert@gmail.com'),
        ('Steph', 'cocomcphail@gmail.com'),
        ('Sacha', 'sachagoldman@icloud.com'),
        ('Derek', 'derek_strangway@telus.net'),
        ('Keelan', 'keelan.brydon@gmail.com')]
random.shuffle(info)

seed = random.randint(1, len(info) - 1)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender, password)

for i in range(len(info)):
    person_info = info[i]
    email = person_info[1]
    message = f'Dear {person_info[0]} \n \t You are receiving this email because you are apart of the Nerd Dinner Secret Santa for 2019. Your recipient is {info[(i + seed) % 6][0]}. You are to buy them a gift at the 30$ price point and bring it to the Nerd Christmas Dinner on 21/12/2019. \n -The Nerd Dinner Secret Santa Bot (REAL DEAL)'

    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    text = msg.as_string()
    server.sendmail(sender, email, text)

server.quit()
