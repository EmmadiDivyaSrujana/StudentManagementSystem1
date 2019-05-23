class FileWriteUtils:
    def WriteFile(self,student):
        with open('StudentRecord.csv','a+') as file:
            file.write("{},{},{},{},{}\n".format(
                student.stuId,
                student.name,
                student.age,
                student.emailAddress,
                student.marks
            )
            )
            file.close()
