from step import Step
from condition import Condition
from link import Link
steps = []
steps.append(Step(0,"start",[], [Condition(True,"on c a"), Condition(True,"on a table0"),Condition(True,"on b table1"), Condition(True, "clear table2"), Condition(True, "clear c"), Condition(True, "clear b")]))
steps.append(Step(1,"finish",[Condition(True,"on c table1"),Condition(True,"clear a"),Condition(True,"clear table0")], []))
steps.append(Step(2,"move b table1 table2",[Condition(True, "clear b"), Condition(True, "on b table1"),Condition (True, "clear table2")], [Condition(True,"on b table2"), Condition(True,"clear table1")]))
steps.append(Step(3,"move a table0 b",[Condition(True,"on a table0"),Condition(True,"clear a"),Condition(True,"clear b")],[Condition(False,"on a table0"),Condition(True,"on a b"),Condition(True,"clear table0"),Condition(False,"clear b")]))
steps.append(Step(4,"move b table2 c",[Condition(True,"clear c"),Condition(True,"clear b"),Condition(True,"on b table2")],[Condition(False,"clear c"),Condition(True,"on b c"),Condition(True,"clear table2"),Condition(False,"on b table2")]))
steps.append(Step(5,"move c a table1",[Condition(True,"on c a"),Condition(True,"clear table1")],[Condition(True,"clear a"),Condition(False,"on c a"),Condition(True,"clear a"), Condition(True, "on c table1"),Condition(False,"clear table1")]))
ordering_constraints = []
causal_links = []
causal_links.append(Link(0,2,Condition(True,"clear b")))
causal_links.append(Link(0,2,Condition(True,"on b table1")))
causal_links.append(Link(0,2,Condition(True,"clear table2")))
causal_links.append(Link(2,4,Condition(True,"on b table2")))
causal_links.append(Link(0,3,Condition(True,"on a table0")))
causal_links.append(Link(5,3,Condition(True,"clear a")))
causal_links.append(Link(5,1,Condition(True,"on c table1")))
causal_links.append(Link(5,1,Condition(True,"clear a")))
causal_links.append(Link(3,1,Condition(True,"clear table0")))
causal_links.append(Link(0,3,Condition(True,"clear b")))
causal_links.append(Link(2,5,Condition(True,"clear table1")))
causal_links.append(Link(0,5,Condition(True,"on c a")))
causal_links.append(Link(0,4,Condition(True,"clear c")))
causal_links.append(Link(2,4,Condition(True,"clear b")))


