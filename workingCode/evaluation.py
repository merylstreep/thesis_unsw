import random

from deap import base
from deap import creator
from deap import tools

IND_SIZE = 5

creator.create("FitnessMin", base.Fitness, weights=(-1.0, -1.0))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("attr_float", random.random)
toolbox.register("individual", tools.initRepeat, creator.Individual,
                 toolbox.attr_float, n=IND_SIZE)

ind1 = toolbox.individual()

print (ind1.fitness)               # [0.86..., 0.27..., 0.70..., 0.03..., 0.87...]
print (ind1.fitness.valid) # False

def evaluate(individual):
    # Do some hard computing on the individual
    a = sum(individual)
    b = len(individual)
    return a, 1. / b

ind1.fitness.values = evaluate(ind1)

print (ind1.fitness)             
print (ind1.fitness.valid)