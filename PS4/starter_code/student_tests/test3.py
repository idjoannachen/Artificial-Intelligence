from step import Step
from condition import Condition
from link import Link
steps = []
steps.append(Step(0, "Start", [],[Condition(True,"on b table0"),Condition(True,"on a b"),Condition(True,"clear table1"),Condition(True,"clear a")]))
steps.append(Step(1,"Finish",[Condition(True,"on b a"),Condition(True,"clear b")],[]))
steps.append(Step(2, "move a b table1",[Condition(True,"clear table1"),Condition(True,"clear a"),Condition(True,"on a b")],[Condition(True,"on a table1"),Condition(True,"on b table0"),Condition(True,"clear a"),Condition(True,"clear b")]))
steps.append(Step(3, "move b table0 a",[Condition(True,"clear b"),Condition(True,"clear a"),Condition(True,"on b table0")],[Condition(True,"on b a"),Condition(True,"clear b"),Condition(True,"on a table1")]))
ordering_constraints = []
ordering_constraints.append([ 0, 2, 3, 1])
ordering_constraints.append([ 2, 1 ])
ordering_constraints.append([ 3, 1 ])
causal_links = []

