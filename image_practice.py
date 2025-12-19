# Section 1 - Your code
from utils import *
set_background("kitchen")

s1 = create_sprite("person", 50, 200)
s2 = create_sprite("fish", -100, 100)
s2 = create_sprite("fish", -100, -100)
s2 = create_sprite("fish", 100, -100)

message1 = create_sprite("alien",-200,200)
message1.color("white")
message1.write("do you want a fish i have 3",font = ("Arial",30, "normal"))
message1.hideturtle()


######################################################################


# Section 2 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()