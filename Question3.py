""" Implement a class Airplane that keeps track of the following features of an airplane:
 consumption: an integer representing number of litres consumed per km of distance
 position: a tuple (pair) of integers representing a position of the plane on a map with 1 km precision
 (assume that the airplane can only be in one of the positions of the grid)
 fuel_level: a float number representing the current fuel level in litres.

Implement the following methods:
 constructor __init__: takes four integer parameters (in the specified sequence)
initX, initY, cons and init_fuel, where (initX, initY) represents initial location of the plane,
cons represents the consumption (litre/km) and init_fuel represents the initial fuel level
 goto: takes two integer parameters X and Y representing the location where the plane needs to go to.
 If the airplane has enough fuel to travel there from its current location, the method moves it there,
 updates remaining fuel level, and returns True. Otherwise, the plain does not move and False is returned.
 refuel: takes one integer parameter indicating how many litres of fuel are added. No value returned.

Assume that the airplane travels in a direct line between two positions (X1; Y1) and
(X2; Y2). The distance between two locations is computed as sqrt((X2 - X1)2 + (Y 2 - Y 1)2)

Indicative test cases:
ap789 = Airplane(0, 0, 10, 3000)
assert ap789.goto(95,70) == True
assert ap789.position[0] == 95 and ap789.position[1]==70
assert abs(ap789.fuel_level - 1819.96) < 0.01 """