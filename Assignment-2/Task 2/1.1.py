class Polygon:
    def __init__(self, n):
        self.number_of_sides = n
    def print_num_sides(self):
        print('There are ' + str(self.number_of_sides) + ' sides.')
class Triangle(Polygon):
    def __init__(self, lengths_of_sides):
        Polygon.__init__(self, 3)
        self.lengths_of_sides = lengths_of_sides  # list of three numbers
    def get_area(self):
        a, b, c = self.lengths_of_sides
        s = (a + b + c) / 2
        return (s*(s-a)*(s-b)*(s-c)) ** 0.5
x = int(input("Input a side :"))
y = int(input("Input a side :"))
z = int(input("Input a side :"))
tri = Triangle([x, y, z])
print(tri.get_area())
tri.print_num_sides()
'''OUTPUT
Input a side :5
Input a side :4
Input a side :3
6.0
There are 3 sides.
'''