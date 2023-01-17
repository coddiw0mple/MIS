from pgmpy.models import BayesianNetwork
from pgmpy.inference import VariableElimination, CausalInference
from pgmpy.factors.discrete import TabularCPD
import tkinter as tk
import json

main = tk.Tk()
main.geometry("700x350")

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
    
    #print(cons_1, cons_2)

    nodes = data["con_vals"].keys()

    for node in nodes:
        node_val = data["con_vals"][node]
        node_val = [i.split(" ") for i in node_val.split("\n")]
        #print(node_val)
        if node in cons_2:
            cpd = TabularCPD(node, len(node_val), node_val, evidence=cons_2[node], evidence_card=[2 for i in cons_2[node]])
        else:
            cpd = TabularCPD(node, len(node_val), node_val)
        model.add_cpds(cpd)
    
    print(model.check_model())
    print(model.edges())
    print(model.get_independencies())
    
    indeps = tk.Toplevel(main)
    a = tk.Label(indeps, text=model.get_independencies())
    a.pack()
    
    edges = tk.Toplevel(main)
    b = tk.Label(edges, text=str(model.edges()))
    b.pack()
    
    c = tk.Label(main, text=model.edges())
    c.pack()

    infer_non_adjust = VariableElimination(model)
    print(infer_non_adjust.query(variables=["Alarm"], evidence={"Burglary": 1, "Earthquake": 1}))
    print(infer_non_adjust.query(variables=["Alarm"], evidence={"Burglary": 0, "Earthquake": 0}))

    main.mainloop()

compute()