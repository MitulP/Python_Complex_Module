import math
class com(object):
    def __init__(self,real,imaginary):
        self.real=real
        self.imaginary=imaginary
    def getreal(self):
        return self.real
    def getimaginary(self):
        return self.imaginary
    def __add__(self,no):
        self.real = self.real+no.real
        self.imaginary = self.imaginary + no.imaginary
        result = "%.2f+%.2fi" % (self.real, self.imaginary)
        return result   
    def __sub__(self,no):
        self.real = self.real- no.real
        self.imaginary = self.imaginary-no.imaginary
        result = "%.2f-%.2fi" % (self.real-no.real, abs(self.imaginary-no.imaginary))
        return result
    def __mul__(self,no):
        temp1 = self.real*no.real-self.imaginary*no.imaginary
        temp2 = self.imaginary*no.real-self.real*no.imaginary
        result = "%.2f+%.2fi" % (temp1,temp2)
        return result
    def __div__(self,no):
        temp1 = (self.real*no.real+self.imaginary*no.imaginary)/(no.real**2+no.imaginary**2)
        temp2 = (self.imaginary*no.real-self.real*no.imaginary) /(no.real**2+no.imaginary**2) 
        result = "%.2f+%.2fi" % (temp1,temp2)
        return result   
    def mod(self):
        return "%.2f+0.00i" % (abs(math.sqrt(self.real**2 +self.imaginary**2)))                 
    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
                result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result       
    def arg(self):
        return math.atan2(self.imaginary,self.real)        
    def conjugate(self):    
        if '-'  in str(self.imaginary):             
            return "%.2f+%.2fi" % (self.real, abs(self.imaginary)) 
        else :
            return "%.2f-%.2fi" % (self.real, self.imaginary) 

c = map(float, raw_input().split(' '))
d = map(float, raw_input().split(' '))
try:
    x=com(c[0],c[1])
    y=com(d[0],d[1])
    #print 
   # print '\n'.join(map(str,[x+y, x-y,x*y,x/y,x.mod(),y.mod(),x.getreal(),x.getimaginary(),y.getreal(),y.getimaginary(),x.arg(),y.arg(),x.conjugate(),y.conjugate()]))
except ValueError as e:
    print("Incorrect Input:{0}".format(e))
    raise

