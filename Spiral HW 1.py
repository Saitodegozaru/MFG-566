import rhinoscriptsyntax as rs
from math import*


rs.EnableRedraw(False)

for t in rs.frange ( 0, 2*pi, pi/45):
    x = t*cos(6*t)
    y = t*sin(6*t)
    z = t
    rs.AddSphere((x, y, z), 0.5)


rs.EnableRedraw(True)
