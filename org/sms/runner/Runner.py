from Cython.Includes.libcpp.queue import priority_queue

from org.sms.objects.Students import Student
from  org.sms.utils.MailUtils import GmailMailer
from  org.sms.utils.FileUtils import FileWriteUtils
def menu():
    print('---MAIN MENU---')
    print('1. To add a student')
    print('2. To show All Students')
    print('3. Exit ')

if __name__ == '__main__':
    GmailMailer.getPassword()
    studentList=list()
    menu()
    fileutls= FileWriteUtils()
    userInp=int(input('Please enter the choice from above menu'))
    runagain=True
    if userInp ==1:
        while runagain:
            s = Student(
                input('Enter the name'),
                contact=input('Enter the contact number'),
                age=int(input("Enter the age")),
                emailAddress=input('Enter the Email address'),
                marks=input('Enter the marks')
            )
            fileutls.WriteFile(s)
            #send the mail to the student
            mailer=GmailMailer()
            mailer.sendMail(s.emailAddress,
                            'Student Addition Information ',
                            'Hello {} You have added to the CRM and your Student is {}'.format(s.name,s.stuId))
            studentList.append(s)
            a= input('Do you want add more  press ! to continue and any key to exit...')
            if a[0] !='!':
                runagain=False
                menu()
                userInp= userInp=int(input('Please enter the choice from above menu'))
            else:
                runagain=True
    if userInp==2:
        for d in studentList:
            print(d)
