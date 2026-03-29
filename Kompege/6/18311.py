from turtle import *
k = 60
screensize(5000, 5000)
tracer(0)


for _ in range(5):
    fd(15*k)
    lt(90)
    fd(25*k)
    lt(90)
up()
fd(4*k)
lt(90)
fd(12*k)
lt(90)
down()
for _ in range(6):
    fd(38*k)
    rt(90)
    fd(22*k)
    rt(90)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*k, y*k)
        dot(7, 'red')
update()
done()
