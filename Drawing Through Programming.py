import turtle

def polygon (t, length):
    t.fd(length)
    t.lt(60)
    t.fd(length)
    t.lt(60)
    t.fd(length)
    t.lt(60)
    t.fd(length)
    t.lt(60)
    t.fd(length)
    t.lt(60)
    t.fd(length)
    t.lt(60)

def Random(t, length):
    t.fd(length)
    t.rt(90)
    t.fd(length)
    t.lt(90)
    t.bk(length)
    t.lt(90)
    t.fd(length)
    t.lt(90)

def door (t, length):
    t.fd(length)
    t.lt(90)
    t.fd(length)
    t.lt(90)
    t.fd(length)
    t.lt(90)
    t.fd(length)
    t.lt(90)

def new(t, length):
    t.bk(length)
    t.lt(120)
    t.bk(length)
    t.rt(120)
    t.bk(length)
    t.rt(120)
    t.fd(length)
    t.rt(120)
    t.fd(length)
    t.rt(120)
    t.fd(length)
    t.rt(120)
    t.bk(length)
    t.rt(120)
    t.fd(length)
    t.rt(120)
    t.bk(length)
    t.rt(120)
    t.fd(length)
    t.rt(120)
    t.bk(length)
    t.rt(120)


def King(t, length):
    t.bk(length)
    t.lt(120)
    t.fd(length)
    t.rt(120)
    t.fd(length)
    t.lt(120)


Cynthia = turtle.Turtle()
Severa = turtle.Turtle()
Marth = turtle.Turtle()
Roy = turtle.Turtle()
Ike = turtle.Turtle()
Ichigo = turtle.Turtle()

polygon(Cynthia, 100)
Random(Severa, 200)
polygon(Marth, 200)
door(Roy, 50)
new(Ike,100)
King(Ichigo, 100)



turtle.done()
