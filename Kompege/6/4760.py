from turtle import *
k = 100
screensize(5000, 5000)
tracer(0)

for _ in range(14):
    for _2 in range(3):
        fd(3*k)
        rt(90)
    lt(180)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*k, y*k)
        dot(7, 'red')
update()
done()
