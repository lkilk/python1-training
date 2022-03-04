from functools import reduce 

class Widget:
    def __init__(self, name, size, colour):
        self.name = name
        self.size = size
        self.colour = colour

# List of widgets
widgets = [
Widget('Widgey', 3, 'Red'),
Widget('Widgealot', 5, 'Blue'),
Widget('Widgeroo', 6, 'Red'),
Widget('Widgeyoh', 9, 'Red'),
Widget('Widgeorama', 11, 'Yellow'),
Widget('Widgeydidge', 7, 'Blue'),
Widget('Widgeydoodle', 3, 'Yellow'),
Widget('Widgeywobbly', 8, 'Red'),
Widget('Widgeyboy', 4, 'Blue'),
Widget('Widgeywort', 7, 'Red'),
Widget('Widgeyanna', 1, 'Yellow'),
Widget('Widgeyloo', 6, 'Blue'),
Widget('Widgeywidgey', 5, 'Red')
]
red_widgets = filter(lambda widge: widge.colour == 'Red', widgets)
largest_red = reduce(lambda w1, w2: w1 if w1.size > w2.size else w2, red_widgets)
print(largest_red.colour, largest_red.size)

