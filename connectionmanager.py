from pgmpy.models import BayesianNetwork
from pgmpy.inference import VariableElimination
from pgmpy.factors.discrete import TabularCPD
import tkinter as tk
import json

def compute():
    with open("cachedem.json", "r") as outfile:
        data = json.load(outfile)
    closed_cons = [tuple(i) for i in data["closed_cons"]]

    model = BayesianNetwork(closed_cons)

    # TODO: remove cons_1
    cons_1 = {}
    cons_2 = {}
    for con in closed_cons:
        if con[0] not in cons_1:
            cons_1[con[0]] = []
            cons_1[con[0]].append(con[1])
        else:
            cons_1[con[0]].append(con[1])
        
        if con[1] not in cons_2:
            cons_2[con[1]] = []
            cons_2[con[1]].append(con[0])
        else:
            cons_2[con[1]].append(con[0])
    
    print(cons_1, cons_2)

    #model.check_model()

compute()