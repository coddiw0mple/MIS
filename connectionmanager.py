from pgmpy.models import BayesianNetwork
from pgmpy.inference import VariableElimination
from pgmpy.factors.discrete import TabularCPD
import tkinter as tk
import json

def compute():
    with open("cachedem.json", "r") as outfile:
        data = json.load(outfile)
    print(data["closed_cons"])

compute()