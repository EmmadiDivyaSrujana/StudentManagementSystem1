class ReadUtils:

    def ReadUserInputStr(self,userMsg,errMsg):
        stringData=''
        stringData=input(userMsg)
        f= stringData.strip()
        if f!='':
            return stringData
            #pass
        else:
            print(errMsg)
            self.ReadUserInputStr(userMsg,errMsg)
        return  stringData

if __name__ == '__main__':
    r=ReadUtils()
    d=r.ReadUserInputStr('Please Enter The nbame ',"Error : Please ceck the Input")
    print(d)
