import rhinoscriptsyntax as rs
from math import*


MyList=[]

rs.EnableRedraw(False)

for t in rs.frange (0, 6*pi, pi/45):
    a = [0]*3
    a[0] = 0.5*exp(0.15*t)*cos(2*t)
    a[1] = 0.5*exp(0.15*t)*sin(2*t)
    a[2] = 0
    MyList.append(a)
    
print MyList
for i in MyList:
    rs.AddSphere(i, 0.2)    

rs.EnableRedraw(True)