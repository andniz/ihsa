from ihsa_oop import Problem

camel_function = input("Użyć funkcji 6-hump camelback? (Y - tak)")
if camel_function.lower() == 'y':
    function = '(4-2.1*x1^2+(x1^4)/3)*x1^2+x1*x2+(-4+4*x2^2)*x2^2'
else:
    function = input("Podaj funkcję: ")

x1_lower = input("Podaj dolną granicę dla x1: ")
x1_upper = input("Podaj górną granicę dla x1: ")
x2_lower = input("Podaj dolną granicę dla x2: ")
x2_upper = input("Podaj górną granicę dla x2: ")

if 'x3' in function:
    dimensions = 3
    x3_lower = input("Podaj dolną granicę dla x3: ")
    x3_upper = input("Podaj górną granicę dla x3: ")
    prob = Problem(function, dimensions, float(x1_lower), float(x1_upper),
        float(x2_lower), float(x2_upper), float(x3_lower), float(x3_upper))
else:
    dimensions = 2
    prob = Problem(function, dimensions, float(x1_lower), float(x1_upper),
        float(x2_lower), float(x2_upper))

prob.solve()
