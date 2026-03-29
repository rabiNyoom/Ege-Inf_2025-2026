from turtle import *
k = 80
screensize(5000, 5000)
tracer(0)


for _ in range(8):
    for _2 in range(4):
        fd(5*k)
        rt(30)
        fd(6*k)
        rt(150)
    rt(60)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*k, y*k)
        dot(6, 'red')
update()
done()
