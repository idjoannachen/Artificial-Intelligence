from step import Step
from condition import Condition
from link import Link
steps = []
steps.append(Step(0,"start",[],[ Condition(True, "on a b"), Condition(True, "on b table0"), Condition(True, "clear a"), Condition(True, "on d c"), Condition(True, "on c table1"), Condition(True, "clear d"), Condition(True, "clear table2"), Condition(True, "clear table3") ]))
steps.append(Step(1,"finish",[Condition(True,"on a b"), Condition(True,"on b c"), Condition(True, "on c d")],[]))
steps.append(Step(2,"move a b table2",[Condition(True,"on a b"), Condition(True,"clear table2"), Condition(True,"clear a")],[ Condition(True,"on a table2"), Condition(False, "on a b"), Condition(True,"clear b"), Condition(False, "clear table2")]))
steps.append(Step(3,"move b table0 c",[Condition(True,"on b table0"), Condition(True,"clear c"), Condition(True,"clear b")],[ Condition(True,"on b c"), Condition(False, "on b table0"), Condition(True,"clear table0"), Condition(False, "clear c")]))
steps.append(Step(4,"move a table2 b",[Condition(True,"on a table2"), Condition(True,"clear b"), Condition(True,"clear a")],[ Condition(True,"on a b"), Condition(False, "on a table2"), Condition(True,"clear table2"), Condition(False, "clear b")]))
steps.append(Step(5,"move d c table3",[Condition(True,"on d c"), Condition(True,"clear table3"), Condition(True,"clear d")],[ Condition(True,"on d table3"), Condition(False, "on d c"), Condition(True,"clear c"), Condition(False, "clear table3")]))
steps.append(Step(6,"move c table1 d",[Condition(True,"on c table1"), Condition(True,"clear d"), Condition(True,"clear c")],[ Condition(True,"on c d"), Condition(False, "on c table1"), Condition(True,"clear table1"), Condition(False, "clear d")]))
ordering_constraints = []
ordering_constraints.append([0,6,5,3,2,4,1])
ordering_constraints.append([5,6,3,4,1])
ordering_constraints.append([2,3,4,1])
ordering_constraints.append([3,4,1])
ordering_constraints.append([4,1,2])
ordering_constraints.append([6,3,4,1])
causal_links = []
causal_links.append(Link(0,5,Condition(True,"on d c")))
causal_links.append(Link(0,5,Condition(True,"clear table3")))
causal_links.append(Link(0,5,Condition(True,"clear d")))
causal_links.append(Link(0,2,Condition(True,"on a b")))
causal_links.append(Link(0,2,Condition(True,"clear table2")))
causal_links.append(Link(0,2,Condition(True,"clear a")))
causal_links.append(Link(5,6,Condition(True,"clear c")))
causal_links.append(Link(0,6,Condition(True,"on c table1")))
causal_links.append(Link(0,6,Condition(True,"clear d")))
causal_links.append(Link(5,3,Condition(True,"clear c")))
causal_links.append(Link(0,3,Condition(True,"on b table0")))
causal_links.append(Link(2,3,Condition(True,"clear b")))
causal_links.append(Link(2,4,Condition(True,"clear b")))
causal_links.append(Link(2,4,Condition(True,"on a table2")))
causal_links.append(Link(0,4,Condition(True,"clear a")))
causal_links.append(Link(4,1,Condition(True,"on a b")))
causal_links.append(Link(3,1,Condition(True,"on b c")))
causal_links.append(Link(6,1,Condition(True,"on c d")))

