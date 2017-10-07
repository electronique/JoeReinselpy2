
def varargs(arg1, *args):

    for args in args:
        print args
        
#varargs(1) # output: "Got one and "
#varargs(1, 2) # output: "Got one and two"
varargs(1, 2, 3,4,5, 6) # output: "Got one and two, three"