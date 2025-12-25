from turtle import *

k = 3
screensize(2000, 2000)
tracer(0)

lt(45)
for i in range(10):
    rt(45)
    fd(203 * k)
    rt(45)
up()
bk(40 * k)
rt(45)
down()
for i in range(5):
    fd(20 * k)
    lt(90)
up()

for x in range(-500, 500):
    for y in range(-500, 500):
        goto(x*k, y*k)
        dot(2, 'red')
update()
done()