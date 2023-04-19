from turtle import*

speed('fastest')
pencolor ('red')
fillcolor('yellow')
for i in range(8):
    fd(100)
    for i in range(8):
        fd(50)
        begin_fill()
        for i in range(8):
            fd(25)
            lt(35)
        end_fill()
        lt(35)
    rt(60)


hideturtle()
mainloop()