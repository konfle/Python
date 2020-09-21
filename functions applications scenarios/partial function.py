# Lesson 3 - Sending emails from Gmail
import smtplib
import functools
import requests
import os


def send_info_email(user, password, mailForm, mailTo, mailSubject, mailBody):
    message = '''From: {}
Subject: {}

{}'''.format(mailForm, mailSubject, mailBody)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(user, password)
        server.sendmail(user, mailTo, message)
        server.close()
        print('mail sent')
        return True
    except:
        print('error sending mail')
        return False


mailForm = "konfle automation system"
mailTo = ['your@email.here0', 'your_another@email.here']
mailSubject = 'Processing finished successfully'
mailBody = '''Hello!

This mail confirms that processing has finished without problems,

Have a nice day!'''

user = 'your_username@gmail.com'
password = 'your_password_here'

send_info_email_from_gmail = functools.partial(send_info_email, user, password, mailSubject='Execution alert')

# send_info_email_from_gmail(mailForm=mailForm, mailTo=mailTo, mailBody=mailBody)
# send_info_email(user, password, mailForm, mailTo, mailSubject, mailBody)

# LAB


def save_url_file(url, dir, file, msg):
    print(msg.format(file))

    r = requests.get(url, stream=True)
    file_path = os.path.join(dir, file)

    with open(file_path, "wb") as f:
        f.write(r.content)


msg = "Please wait - the file {} will be downloaded"

url = 'http://mobilo24.eu/spis'
# dir = 'c:/temp/'
file = 'spis.html'
# save_url_file(url, dir, file, msg)
# url = 'https://www.mobilo24.eu/wp-content/uploads/2015/11/Mobilo_logo_kolko_512-565b1626v1_site_icon.png'
# dir = 'c:/temp/'
# file = 'logo.png'
# save_url_file(url, dir, file, msg)

save_url_to_dir = functools.partial(save_url_file, dir='c:/temp/', msg="Please wait:{}")
save_url_to_dir(url=url, file=file)

url = 'https://www.mobilo24.eu/wp-content/uploads/2015/11/Mobilo_logo_kolko_512-565b1626v1_site_icon.png'
file = 'logo.png'
save_url_to_dir(url=url, file=file)

