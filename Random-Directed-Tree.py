import networkx as nx
import matplotlib.pyplot as plt
import numpy as np 
import math as mt
import glob
import pandas as pd
from matplotlib.pyplot import figure
import random
from networkx.algorithms.distance_measures import center
from networkx.algorithms import community
from tqdm import tqdm # !pip3 install tqdm



def write_edge_list(edge_list,v_size):
    with open(f'Tree{v_size}.txt', 'w') as f:
      # replace with path tree_{v_size}.txt'
        for edge in edge_list:
            f.write(f'{edge[0]} {edge[1]}\n')
        f.close()
        #print(g.nodes())
    print(f'../DATA/randomTree/tree_{v_size}.txt')
    

def generate_multi_rooted_directed_tree(minimum_nodes, maximum_nodes, gap_in_size):
     for v_size in range(minimum_nodes,maximum_nodes,gap_in_size):
        #g = nx.read_adjlist(file, nodetype=int)
        D = {}
        g = nx.generators.random_tree(v_size,seed=5)
        #print("initial edge _list is ", list(g.edges()))
        for u in g.nodes():
            D[u] = 0
        root_list = random.sample(list(g.nodes()),50)
        queue     = []
        edge_list = []
        for u in root_list:
            queue.append(u)
            D[u] = 1
        while len(queue)!=0:
            u = queue.pop(0)
            for v in g.neighbors(u):
                if D[v]==0:
                    edge_list.append((u,v))
                    queue.append(v)
                    D[v] = 1
        #print(edge_list)
        #print("Root list is  : ", root_list)
        for e in g.edges():
            if (e[0],e[1]) not in edge_list and (e[1],e[0]) not in edge_list:
                edge_list.append(e)
        G = nx.DiGraph()
        G.add_edges_from(edge_list)
        write_edge_list(edge_list,v_size)
        
generate_multi_rooted_directed_tree(1000,50000,2000)
