import datetime

class call(object):
    def __init__(self,unique_id,name,phone,time,reason):
        self.unique_id = unique_id
        self.name = name
        self.phone = phone
        self.reason = reason
        self.time = time
    def displayCall(self):
        print self.unique_id
        print self.name
        print self.phone
        print self.time
        print self.reason
    
class callCenter(call):
    def __init__(self,list_calls,call_list_len):
        self.list_calls = list_calls
        self.call_list_len = call_list_len
        return self

newcall = callCenter(1,"Joe","443-932-5443","5:30","questions")

newcall.displayCall()
