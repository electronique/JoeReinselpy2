class mathdojo(object):
    def __init__(self,*nums):
        self.nums = nums
        for nums in nums:
           x = self.nums

    def add(self, *x):
        sum =self.nums +self.nums
        print sum

md = mathdojo()

md.add(2,3)
#which should perform 0+2+(2+5)-(3+2) and return 4.