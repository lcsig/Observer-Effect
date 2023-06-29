#!/usr/bin/env python3
import readline 
import enum
#import seaborn as sns
#import matplotlib.pyplot as plt
from numpy import random


# Enum class to specify the distributions
class Dist(enum.Enum):  
    UNIFORM = 0
    BETA = 1


def gen_random_numbers(from_num: float, to_num: float, n: int, distribution: Dist, a, b) -> list:
    """
    A function to generate n random number with certain distribution
    """
    L = []

    if distribution == Dist.BETA:
        n += 2  # This to iliminate the first and the last items in the list since we normalize the values
        L = random.beta(a, b, n)
                
        mini = min(L)
        maxi = max(L)
        L = [(from_num + ((i - mini) * (to_num - from_num)  / (maxi - mini))) for i in L]
        L.sort()
        L.pop(0)
        L.pop()
    elif distribution == Dist.UNIFORM:
        L = random.uniform(from_num, to_num, size=n)
        
    L.sort()
    return list(L)
    

def get_arc_length(point_drop_location: float, arcs_cuts: list):
    """
    A function to get the length of the arc that is located at point_drop_location in the arcs cut
    """
    for i in range(len(arcs_cuts)):
        if point_drop_location < arcs_cuts[i]:
            return arcs_cuts[i] - (0 if i == 0 else arcs_cuts[i - 1])


if __name__ == '__main__':
    circle_diameter = float(input("[-] Enter Circle Diameter (e.g. 50): ") or "50")
    n_arcs = int(input("[-] Enter The Num of Arcs (e.g. 500): ") or "500")
    n_points = int(input("[-] Enter The Number of Points that Will be Dropped (e.g. 100000): ") or "100000")
    distribution_type = Dist[input("[-] Enter the distribution of random numbers (Beta/Uniform): ").upper() or "UNIFORM"]
    

    a, b = 0, 0
    if distribution_type == Dist.BETA:
        a = float(input("[-] Alpha Parameter: "))
        b = float(input("[-] Beta Parameter: "))
        
    
    arcs_cut_loc = gen_random_numbers(0, circle_diameter, n_arcs, distribution_type, a, b)
    arcs_cut_loc.append(circle_diameter)
    arcs_cut_loc.sort()
    #sns.displot(arcs_cut_loc)
    #plt.show()
    
    arcs_len = 0
    for i in range(n_points):
        point_loc = 0
        while(point_loc == 0 or point_loc == circle_diameter or point_loc in arcs_cut_loc):
            point_loc = random.uniform(0, circle_diameter)
            
        arcs_len += get_arc_length(point_loc, arcs_cut_loc)
        
        
    print("[+] Actual Value: " + str(circle_diameter / n_arcs))
    print("[+] Simulation Result: " + str(arcs_len / n_points))
    print("[+] Therotical Simulation Result: " + str(2 * circle_diameter / (n_arcs + 1)))
        
    
    
    
