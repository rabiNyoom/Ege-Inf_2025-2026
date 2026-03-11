from turtle import *
screensize(3000, 3000)
tracer(0)
k = 10

lt(90)
up()

rt(90)
rt(30)
down()
for _ in range(10):
    fd(25*k)
    rt(90)
up()

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*k, y*k)
        dot(2, 'red')

update()
done()

# ???
