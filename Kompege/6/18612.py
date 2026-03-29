from turtle import *
k = 40
screensize(5000, 5000)
tracer(0)


for _ in range(2):
    fd(24*k)
    rt(90)
    fd(10*k)
    rt(90)
fd(3*k)
lt(90)
fd(13*k)
rt(90)
for _ in range(2):
    fd(9*k)
    rt(90)
    fd(32*k)
    rt(90)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*k, y*k)
        dot(4, 'red')
update()
done()
