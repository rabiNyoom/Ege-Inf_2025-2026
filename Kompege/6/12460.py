from turtle import *
k = 40
screensize(5000, 5000)
tracer(0)
up()

for _ in range(3):
    down()
    for _2 in range(2):
        fd(7*k)
        rt(90)
        fd(7*k)
        rt(90)
    up()
    fd(6*k)
    rt(90)
    fd(6*k)
    lt(90)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*k, y*k)
        dot(3, 'red')
update()
done()
