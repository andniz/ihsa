import random

#Parametry
harmony_memory_size=10
harmony_memory_considering_rate=0.9
pitch_adjusting_rate=0.3
max_iterations=5000
dimensions=2

#Funkcja, na razie do testów - potem zastąpi się funkcją otrzymaną z parsera
def camel(x):
    x1=x[0]
    x2=x[1]
    return (4 - 2.1*x1**2 + (x1**4)/3)*x1**2 + x1*x2 + (-4 + 4*x2**2)*x2**2

#Listy na wektory i wartości funkcji
harmony_memory=[]
values=[]

#Generowanie poczatkowych wektorów
for i in range(harmony_memory_size):
    x=[]
    for dim in range(dimensions):
        x.append((random.random()-0.5)*4)
    harmony_memory.append(0)
    harmony_memory[-1]=x
    values.append(camel(x))

#Właściwa część algorytmu
for i in range(max_iterations):
    #Generowanie nowego wektora
    x=[]
    for dim in range(dimensions):
        if random.random()<harmony_memory_considering_rate:
            x.append(harmony_memory[random.randint(0,9)][dim])
            if random.random()<pitch_adjusting_rate:
                x[dim]=x[dim]+(random.random()-0.5)/10
        else:
            x.append((random.random()-0.5)*4)

    #Sprawdzenie czy (x1,x2) będzie lepsze od najgorszego wektora
    if camel(x)<max(values):
        worst_index=values.index(max(values))
        del(values[worst_index])
        del(harmony_memory[worst_index])
        harmony_memory.append(0)
        harmony_memory[-1]=x
        values.append(camel(x))

    if min(values)<-1.0316:
        print(i)
        break



print(min(values))
# print("Najgorsza wartość: ")
# print(max(values))
# print("\n Indeks najgorszej wartości: ")
# print(values.index(max(values)))
