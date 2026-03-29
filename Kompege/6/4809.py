from turtle import *
k = 100
screensize(5000, 5000)
tracer(0)


for _ in range(15):
    fd(7*k)
    rt(30)
    fd(8*k)
    rt(150)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*k, y*k)
        dot(7, 'red')
update()
done()
