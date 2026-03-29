from turtle import *
k = 100
screensize(5000, 5000)
tracer(0)

fd(9*k)
rt(90)
for _ in range(2):
    fd(3*k)
    rt(90)
    fd(3*k)
    rt(270)
for _ in range(2):
    fd(3*k)
    rt(90)
fd(9*k)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*k, y*k)
        dot(7, 'red')
update()
done()
