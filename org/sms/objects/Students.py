class Student:
    temp=0
    def __init__(self, name, age, contact, marks, emailAddress):
        """This is the Student initiliazer will askk sonme arguments"""
        self.name=name
        self.age=age
        self.conact= contact
        self.marks=marks
        self.emailAddress=emailAddress
        Student.temp=Student.temp+1
        self.stuId = Student.temp

    def __str__(self):
        return "ID is : {}\n" \
               "Name is : {}\n" \
               "Age is : {}  \n" \
               "Contact No Is : {}\n" \
               "Address is : {}\n" \
               "Marks are : {}".format(
            self.stuId,
            self.name,
            self.age,
            self.conact,
            self.address,
            self.marks)
