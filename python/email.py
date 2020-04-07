import os, smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import time
import datetime
import random

gmail_username="상대에게 보여질 닉네임입니다"
gmail_user="지메일 아이디@gmail.com"
gmail_pwd="지메일 패스워드"
attach_file="만약 첨부파일을 발송한다면 첨부파일 명"

def send_gmail(to, subject, text, html, attach):
    msg=MIMEMultipart('alternative')
    msg['From']=gmail_username
    msg['To']=to
    msg['Subject']=subject
    msg.attach(MIMEText(text, 'plain'))
    msg.attach(MIMEText(html, 'html'))
    
    #첨부파일을 넣는다면 이 아래부분에 붙어있는 #들을 제거하시면 됩니다.
    #part=MIMEBase('application','octet-stream')
    #part.set_payload(open(attach, 'rb').read())
    #Encoders.encode_base64(part)
    #part.add_header('Content-Disposition','attachment; filename="%s"' % os.path.basename(attach))
    #msg.attach(part)
    
    mailServer=smtplib.SMTP("smtp.gmail.com",587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(gmail_user,gmail_pwd)
    mailServer.sendmail(gmail_user, to, msg.as_string())
    mailServer.close()


def mainLoop():

    f = open("text.txt", "r")
    message = f.read()
    f.close()

    f = open("html.html", "r")
    html = f.read()
    f.close()
    
    title="메일 제목을 여기에 넣으시면 됩니다."
    print ("Program Ready")
    print ("----------------------")
    f = open("list.txt", "r")
    emails = f.readlines()
    for email in emails:
        rand = random.randrange(5,7)       # Set range of the waiting time.
        email = email.strip()                # Removing White spaces.
        if email == "" :
            continue
        print ("[" + str(datetime.datetime.now()) + "] Sending email to " + email + "...")
        try:
            send_gmail(email,title,message,html,attach_file)
        except:
            print ("Mail sending error. (" + email + ")")
            break
        print ("[" + str(datetime.datetime.now()) + "] Complete... Waiting for " + str(rand) +" seconds.")
        time.sleep(rand)

    print ("Sending mail program is going to be terminated. Now waiting your command to exit." )
    time.sleep(-1)

if __name__ == "__main__":
    mainLoop()
    