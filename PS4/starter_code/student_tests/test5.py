from step import Step
from condition import Condition
from link import Link
steps = []
steps.append(Step(0,"start",[],[ Condition(True,"clear table4"), Condition(True, "clear table3"), Condition(True, "on c a"), Condition(True, "on b table0"), Condition(True, "on a table1"), Condition(True, "clear c"), Condition(True, "clear b")]))
steps.append(Step(1,"finish",[Condition(True,"on a b"), Condition(True,"on b c")],[]))
steps.append(Step(2,"move a table1 b",[Condition(True,"on a table1"), Condition(True,"clear b"), Condition(True,"clear a")],[ Condition(True,"on a b"), Condition(False, "on a table1"), Condition(True,"clear table1"), Condition(False, "clear b")]))
steps.append(Step(3,"move b a c",[Condition(True,"on b a"), Condition(True,"clear c"), Condition(True,"clear b")],[ Condition(True,"on b c"), Condition(False, "on b a"), Condition(True,"clear a"), Condition(False, "clear c")]))
steps.append(Step(4,"move b table0 a",[Condition(True,"on b table0"), Condition(True,"clear a"), Condition(True,"clear b")],[ Condition(True,"on b a"), Condition(False, "on b table0"), Condition(True,"clear table0"), Condition(False, "clear a")]))
steps.append(Step(5,"move c a table4",[Condition(True,"on c a"), Condition(True,"clear table4"), Condition(True,"clear c")],[ Condition(True,"on c table4"), Condition(False, "on c a"), Condition(True,"clear a"), Condition(False, "clear table4")]))
ordering_constraints = []
ordering_constraints.append([0,5,3,2,4,1])
ordering_constraints.append([2,1])
ordering_constraints.append([3,2,1,4])
ordering_constraints.append([4,2,3,1])
ordering_constraints.append([5,3,2,4,1])
causal_links = []
causal_links.append(Link(0,5,Condition(True,"clear c")))
causal_links.append(Link(0,5,Condition(True,"clear table4")))
causal_links.append(Link(0,5,Condition(True,"on c a")))
causal_links.append(Link(0,4,Condition(True,"clear b")))
causal_links.append(Link(5,4,Condition(True,"clear a")))
causal_links.append(Link(0,4,Condition(True,"on b table0")))
causal_links.append(Link(0,3,Condition(True,"clear b")))
causal_links.append(Link(0,3,Condition(True,"clear c")))
causal_links.append(Link(4,3,Condition(True,"on b a")))
causal_links.append(Link(3,2,Condition(True,"clear a")))
causal_links.append(Link(0,2,Condition(True,"clear b")))
causal_links.append(Link(0,2,Condition(True,"on a table1")))
causal_links.append(Link(3,1,Condition(True,"on b c")))
causal_links.append(Link(2,1,Condition(True,"on a b")))
