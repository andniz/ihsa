from num_str_parser import NumericStringParser
import math, random, sys
import numpy as np
import matplotlib.pyplot as plt
nsp=NumericStringParser()

class Problem:
    """
    Contains methods for IHS algorithm for function optimization.
    """
    harmony_memory_size = 7
    harmony_memory_considering_rate = 0.95
    pitch_adjusting_rate_min = 0.35
    pitch_adjusting_rate_max = 0.99
    bandwidth_min = 0.000001
    bandwidth_max = 4

    def __init__(self, func, dim, ranges):
        self.function = func
        self.dimensions = dim
        self.harmony_memory = []
        self.values = []
        self.iteration_number = 0
        self.max_iterations = 3000
        #starting_points_params: [x1_mean, x1_range, etc]
        self.ranges = ranges
        self.starting_points_params = []
        self.starting_points_params.append((ranges[1] + ranges[0]) / 2)
        self.starting_points_params.append(ranges[1] - ranges[0])
        self.starting_points_params.append((ranges[3] + ranges[2]) / 2)
        self.starting_points_params.append(ranges[3] - ranges[2])
        if dim > 2:
            self.starting_points_params.append((ranges[5] + ranges[4]) / 2)
            self.starting_points_params.append(ranges[5] - ranges[4])

    def get_function_value(self, x):
        """
        Expects a 2- or 3-dimensional vector. Returns the value of the function at the point.
        """
        x1 = x[0]
        x2 = x[1]
        function_string = self.function.replace('x1',str(x1)).replace('x2',str(x2))
        if self.dimensions > 2:
            x3 = x[2]
            function_string = function_string.replace('x3',str(x3))
        return nsp.eval(function_string)

    def get_starting_points(self):
        """
        Fills harmony memory and value memory with randomly generated points and their function values.
        """
        self.x1_values = []
        self.x2_values = []
        if self.dimensions == 3:
            self.x3_values = []
        self.y_values = []
        self.index_values = []
        for i in range(self.harmony_memory_size):
            x = []
            for dim in range(self.dimensions):
                x.append((random.random()- 0.5) * self.starting_points_params[2*dim+1] + self.starting_points_params[2*dim])
            self.harmony_memory.append(0)
            self.harmony_memory[-1] = x
            self.values.append(self.get_function_value(x))

    def optimize(self):
        """
        Iterates the algorithm for a given number of times.
        """
        while self.iteration_number < self.max_iterations:
            self.iterate()
        print(min(self.values))


    def iterate(self):
        """
        Generates a new vector, if its function value is better than the worst in harmony memory, it replaces the worst one.
        """
        #Generowanie nowego wektora
        x = []
        self.iteration_number += 1
        pitch_adjusting_rate=self.pitch_adjusting_rate_min+(self.pitch_adjusting_rate_max-self.pitch_adjusting_rate_min)*self.iteration_number/self.max_iterations
        bandwidth = self.bandwidth_max*math.exp(math.log(self.bandwidth_min/self.bandwidth_max)*self.iteration_number/self.max_iterations)
        for dim in range(self.dimensions):
            if random.random() < self.harmony_memory_considering_rate:
                x.append(self.harmony_memory[random.randint(0,self.harmony_memory_size-1)][dim])
                if random.random() < pitch_adjusting_rate:
                    while not (x[dim] >= self.ranges[2*dim] and x[dim] <= self.ranges[2*dim+1]):
                        x[dim] = x[dim] + (random.random()-0.5)*2*bandwidth
            else:
                x.append((random.random()- 0.5) * self.starting_points_params[2*dim+1] + self.starting_points_params[2*dim])

        if self.get_function_value(x) < max(self.values):
            worst_index = self.values.index(max(self.values))
            del(self.values[worst_index])
            del(self.harmony_memory[worst_index])
            self.harmony_memory.append(0)
            self.harmony_memory[-1] = x
            self.values.append(self.get_function_value(x))

    def solve(self):
        self.get_starting_points()
        self.optimize()

    def draw_contour(self, ranges):
        """
        Draws a contour plot of the function in the given range.
        """
        resolution = 25
        x = np.linspace(ranges[0], ranges[1], resolution)
        y = np.linspace(ranges[2], ranges[3], resolution)
        x1, x2 = np.meshgrid(x,y)
        z = np.zeros((resolution,resolution))
        for i in range(resolution):
            for j in range(resolution):
                z[j][i]=self.get_function_value([x1[j][i], x2[j][i]])
        cs = plt.contourf(x1, x2, z, 15)
        cbar = plt.colorbar(cs)
        plt.show()
