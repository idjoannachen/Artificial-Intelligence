from step import Step
from condition import Condition
from link import Link
steps=[]
steps.append(Step(0,"start",[],[Condition(True,"on a table0"),Condition(True,"on d table6"),Condition(True,"on b a"),Condition(True,"on c d"),Condition(True,"clear b"),Condition(True,"clear c"),Condition(True,"clear table2"),Condition(True,"clear table3"),Condition(True,"clear table4")]))
steps.append(Step(1,"finish",[Condition(True,"on d table0"),Condition(True,"on a table3"),Condition(True,"on b table2"),Condition(True,"on c b"),Condition(True,"clear table6")],[]))

causal_links=[]
causal_links.append(Link(0,6,Condition(True,"clear b")))
causal_links.append(Link(0,6,Condition(True,"on b a")))
causal_links.append(Link(0,6,Condition(True,"clear table2")))
causal_links.append(Link(0,2,Condition(True,"clear c")))
causal_links.append(Link(0,2,Condition(True,"on d c")))
causal_links.append(Link(0,2,Condition(True,"clear table3")))
causal_links.append(Link(2,3,Condition(True,"on c table3")))
causal_links.append(Link(0,3,Condition(True,"clear c")))
causal_links.append(Link(0,3,Condition(True,"clear b")))
causal_links.append(Link(3,4,Condition(True,"clear table3")))
causal_links.append(Link(3,4,Condition(True,"on a table0")))
causal_links.append(Link(6,4,Condition(True,"clear a")))
causal_links.append(Link(4,5,Condition(True,"clear table0")))
causal_links.append(Link(0,5,Condition(True,"on d table6")))
causal_links.append(Link(2,5,Condition(True,"clear d")))
causal_links.append(Link(5,1,Condition(True,"on d table0")))
causal_links.append(Link(5,1,Condition(True,"on d table0")))
causal_links.append(Link(6,1,Condition(True,"on b table2")))
causal_links.append(Link(3,1,Condition(True,"on c b")))
causal_links.append(Link(5,1,Condition(True,"clear table6")))
causal_links.append(Link(4,1,Condition(True,"on a table3")))
ordering_constraints=[]
ordering_constraints.append([0,5,4,3,2,6,1])
ordering_constraints.append([6,2,4,3,5,1])
ordering_constraints.append([2,3,4,5,1])
ordering_constraints.append([3,4,1])
ordering_constraints.append([4,5,1])
ordering_constraints.append([5,1])



