# from turtle import Turtle, Screen

# damian = Turtle()
# damian.shape('turtle')
# damian.color('DarkSlateGray4')
# damian.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column('Pokemon Name', ['Pikachu', 'Squirtle', 'Charmander'])
table.add_column('Type', ['Electricity', 'Water', 'Fire'])

table.align = "l"

print(table)