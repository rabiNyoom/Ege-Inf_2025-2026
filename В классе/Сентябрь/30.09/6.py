from turtle import *
lt(90)

screensize(3000,3000)
tracer(0)
k = 10

for _ in range(12):
    fd(4*k); rt(144); fd(4*k); lt(72)
pu()

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*k,y*k)
        dot(2, 'red')
update()
done()
# 30