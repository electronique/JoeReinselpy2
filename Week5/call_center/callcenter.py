import datetime

class call(object):
    def __init__(self,unique_id,name,phone,reason):
        self.unique_id = unique_id
        self.name = name
        self.phone = phone
        time = datetime.time
        self.time = time
        self.reason = reason
    def displayCall(self):
        print self.unique_id
        print self.name
        print self.phone
        print self.time
        print self.reason

class callCenter(call):
    
        print call

newcall = callCenter(1,"Joe","443-932-5443","questions")

newcall.displayCall()
