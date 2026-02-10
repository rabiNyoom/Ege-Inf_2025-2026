from turtle import *;

tracer(0);
screensize(3000, 3000);
k = 5;

lt(90);
for _ in range(9):
    fd(27*k); rt(90); fd(30*k); rt(90);
pu();

fd(3*k); rt(90); fd(6*k); lt(90);
pd();
for _ in range(9):
    fd(77*k); rt(90); fd(66*k); rt(90);
pu()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*k, y*k);
        dot(3, 'red');

update(); done();

# 96