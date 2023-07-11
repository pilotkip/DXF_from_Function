import ezdxf
import math

def f(x):
    return -1/x

def df(x):
    return 1/(x*x)

# create a new DXF R2010 document
doc = ezdxf.new("R2010")

# add new entities to the modelspace
msp = doc.modelspace()

xs = 20
ys = 20

x_start = 0.25
x_end = 7
step =   .1

x = x_end

while x > x_start:
    y = f(x)
    dx = step / (1 + df(x))
    x1 = x - dx
    y1 = f(x1)

    msp.add_line((x, y), (x1, y1))
    print(x_start, x,y,x1,y1)
    x = x1

# save the DXF document
doc.saveas("line.dxf")