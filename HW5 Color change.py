import rhinoscriptsyntax as rs

def main():
    surface_id = rs.GetObject("Select a surface t", 8, True, True)
    if not surface_id: return

    rs.EnableRedraw(False)
    t= 0
    while t<=1.0:
        r1parameter(surface_id,t)
        t+=0.02
    rs.EnableRedraw(True)

def r1parameter(surface,x):
    domain1=rs.SurfaceDomain(surface,0)
    domain2=rs.SurfaceDomain(surface,1)

    r1_par=domain1[0] + x*(domain1[1])
    r2_par=domain2[0] + x*(domain2[1])
    r3point=rs.EvaluateSurface(surface,r1_par,r2_par)
    if r3point:
        point_id=rs.AddSphere(r3point, 0.5)
        rs.ObjectColor(point_id, parametercolor(x))


def parametercolor(parameter):
    red = 255 * parameter
    if red<0 : red=0
    if red>255 : red=255
    return(red,0,255-red)

if __name__=="__main__":
    main()
