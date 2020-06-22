import math
import operator
import matplotlib
import numpy 
import scoop 
import random
from deap import base, creator, tools, gp

class Member : 
     def __init__(self, genome, fitness):
          self.genome = genome
          self.fitness = fitness

def applyMutation():
     """Apply the mutation and crossover effects here"""
     print("muttaions")

def reproduction(): 
     """Will this method also include crossing over? Or is that separate?"""
     print("reproduction")

def calculateFitness(individual):
     print("not yet impleentned")

def geneticAlgorithm(population): 
     survivors = []
     history = []
     calculateFitness()

     return survivors, history

def main():
     """Generate a population and execute the genetic algorithm"""

     # define population parameters
     maxPopulationSize = 10
     maxMemberSize = 5

     #define auxillary pset functions
     def square (x) :
          return math.pow(x, 2)

     def cubicRoot (x):
          return math.pow(x, 1/3)
     
     def cube (x):
          return math.pow(x, 3)
    
     pset = gp.PrimitiveSet("GENE_PRIMITIVES", arity=6)
     pset.addPrimitive(operator.add, 2)
     pset.addPrimitive(operator.sub, 2)
     pset.addPrimitive(operator.mul, 2)

     pset.addPrimitive(math.exp, 1)
     pset.addPrimitive(math.log, 1)
     pset.addPrimitive(math.sqrt, 1)
     pset.addPrimitive(math.sin, 1)
     pset.addPrimitive(math.cos, 1)
     pset.addPrimitive(math.tan, 1)
     pset.addPrimitive(math.atan, 1)

     pset.addPrimitive(square, 1)
     pset.addPrimitive(cubicRoot, 1)
     pset.addPrimitive(cube, 1)


     creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
     creator.create("Individual", gp.PrimitiveTree, fitness=creator.FitnessMin,
                    pset=pset)

     toolbox = base.Toolbox()
     toolbox.register("expr", gp.genHalfAndHalf, pset=pset, min_=1, max_=2)
     toolbox.register("individual", tools.initIterate, creator.Individual,
                    toolbox.expr)
     toolbox.register("population", tools.initRepeat, list, toolbox.individual)

     #generate population
     toolbox.population(maxPopulationSize)
     ind1 = toolbox.individual()
     
     print(ind1)
     
if __name__ == "__main__":
    main()