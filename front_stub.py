from ihsa_oop import Problem

camel_function = input("Użyć funkcji 6-hump camelback? (Y - tak) ")
if camel_function.lower() == 'y':
    function = '(4-2.1*x1^2+(x1^4)/3)*x1^2+x1*x2+(-4+4*x2^2)*x2^2'
else:
    function = input("Podaj funkcję: ")

ranges = []
ranges.append(float(input("Podaj dolną granicę dla x1: ")))
ranges.append(float(input("Podaj górną granicę dla x1: ")))
ranges.append(float(input("Podaj dolną granicę dla x2: ")))
ranges.append(float(input("Podaj górną granicę dla x2: ")))

if 'x3' in function:
    dimensions = 3
    ranges.append(float(input("Podaj dolną granicę dla x3: ")))
    ranges.append(float(input("Podaj górną granicę dla x3: ")))
else:
    dimensions = 2

prob = Problem(function, dimensions, ranges)
prob.draw_contour(ranges)
prob.solve()
