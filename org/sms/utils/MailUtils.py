import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class GmailMailer():
    def getPassword(self):
        """This is basically used to get the password from a file"""
        file=open(r'C:\Users\dheer\PycharmProjects\StudentManagementSystem\org\sms\utils\password','r')
        return file.readline()
    def add(self,a,b):
        return a+b

    def sendMail(self, emailAddress, subject='Testing', body="Whe just checked"):
        fromaddr = "loggerdemon@gmail.com"  # Your Email Address
        toaddr = emailAddress  # whom you want to send to
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = subject
        # body = "Hi all this was an automation done by me + Python with core SMTP libraries"
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, self.getPassword())
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()
        print("an email with subject was sent successfully ")


if __name__ == '__main__':
   #print( GmailMailer().getPassword())

   print(help(GmailMailer.getPassword))
