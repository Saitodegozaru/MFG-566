import rhinoscriptsyntax as rs
from math import*


rs.EnableRedraw(False)

for t in rs.frange ( 0, 6*pi, pi/45):
    x = 0.5*exp(0.15*t)*cos(2*t)
    y = 0.5*exp(0.15*t)*sin(2*t)
    z = 0.5*exp(0.15*t)
    rs.AddSphere((x, y, z), 0.2)


rs.EnableRedraw(True)
