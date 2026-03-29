from turtle import *
k = 100
screensize(5000, 5000)
tracer(0)

for _ in range(16):
    lt(36)
    fd(4*k)
    lt(36)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*k, y*k)
        dot(7, 'red')
update()
done()
