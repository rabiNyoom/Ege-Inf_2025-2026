from turtle import *

screensize(2000, 2000)
tracer(0)
lt(90)

k = 10

for i in range(4):
    fd(10 * k)
    rt(90)

up()

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * k, y * k)
        dot(2, 'red')

update()
done()

# 81