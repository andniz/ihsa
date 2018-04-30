from num_str_parser import NumericStringParser
import math, random, sys
nsp=NumericStringParser()




class Problem:

#Przerobić argumenty dla x3 na kwargs
    def __init__(self, func, dim, x1_lower, x1_upper, x2_lower, x2_upper, x3_lower=0, x3_upper=0):
        self.function = func
        self.dimensions = dim
        self.harmony_memory = []
        self.values = []
        self.iteration_number = 0
        self.harmony_memory_size = 7
        self.harmony_memory_considering_rate = 0.95
        self.pitch_adjusting_rate_min = 0.35
        self.pitch_adjusting_rate_max = 0.99
        self.bandwidth_min = 0.000001
        self.bandwidth_max = 4
        self.max_iterations = 3000
        #starting_points_params: [x1_mean, x1_range, etc]
        self.starting_points_params = []
        self.starting_points_params.append((x1_upper + x1_lower) / 2)
        self.starting_points_params.append(x1_upper - x1_lower)
        self.starting_points_params.append((x2_upper + x2_lower) / 2)
        self.starting_points_params.append(x2_upper - x2_lower)
        if dim > 2:
            self.starting_points_params.append((x3_upper + x3_lower) / 2)
            self.starting_points_params.append(x3_upper - x3_lower)


    def get_function_value(self,x):
        x1 = x[0]
        x2 = x[1]
        function_string = self.function.replace('x1',str(x1)).replace('x2',str(x2))
        if self.dimensions > 2:
            x3 = x[2]
            function_string = function_string.replace('x3',str(x3))
        return nsp.eval(function_string)

    def get_starting_points(self):
        for i in range(self.harmony_memory_size):
            x = []
            for dim in range(self.dimensions):
                x.append((random.random()- 0.5) * self.starting_points_params[2*dim] + self.starting_points_params[2*dim+1])
            self.harmony_memory.append(0)
            self.harmony_memory[-1] = x
            self.values.append(self.get_function_value(x))

    def optimize(self):
        while self.iteration_number < self.max_iterations:
            self.iterate()


    def iterate(self):
        #Generowanie nowego wektora
        x = []
        self.iteration_number += 1
        pitch_adjusting_rate=self.pitch_adjusting_rate_min+(self.pitch_adjusting_rate_max-self.pitch_adjusting_rate_min)*self.iteration_number/self.max_iterations
        bandwidth = self.bandwidth_max*math.exp(math.log(self.bandwidth_min/self.bandwidth_max)*self.iteration_number/self.max_iterations)
        for dim in range(self.dimensions):
            if random.random() < self.harmony_memory_considering_rate:
                x.append(self.harmony_memory[random.randint(0,self.harmony_memory_size-1)][dim])
                if random.random() < pitch_adjusting_rate:
                    x[dim] = x[dim] + (random.random()-0.5)*2*bandwidth
            else:
                x.append((random.random()- 0.5) * self.starting_points_params[2*dim] + self.starting_points_params[2*dim+1])

        if self.get_function_value(x) < max(self.values):
            worst_index = self.values.index(max(self.values))
            del(self.values[worst_index])
            del(self.harmony_memory[worst_index])
            self.harmony_memory.append(0)
            self.harmony_memory[-1] = x
            self.values.append(self.get_function_value(x))

# function = '(4-2.1*x1^2+(x1^4)/3)*x1^2+x1*x2+(-4+4*x2^2)*x2^2'
function = 'x1^2+x2^2+x3^2'
# function=input("Wprowadź funkcję: ")
if 'x3' in function:
    dimensions=3
else:
    dimensions=2

ambaras=Problem(function, dimensions, -2, 2, -1, 7, -4, 2)

ambaras.get_starting_points()
ambaras.optimize()

print(min(ambaras.values))
# Dorobić obsługę źle wprowadzonej funkcji (żeby dało komunikat o błędzie) - pyparsing.ParseException
# dorobić ograniczenia żeby wyszukiwało minima lokalne - ale nie w jednym przebiegu
# funkcje takie żeby było kilka minimów
# 3 garbny wielbłąd też jest
