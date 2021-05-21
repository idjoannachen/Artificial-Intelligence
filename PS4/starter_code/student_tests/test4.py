from step import Step
from condition import Condition
from link import Link
steps = []
steps.append(Step(0, "Start", [],[Condition(True,"on b a"),Condition(True,"on c b"),Condition(True,"on a table0"),Condition(True,"clear c"),Condition(True,"clear table1")]))
steps.append(Step(1,"Finish",[Condition(True,"clear a"),Condition(True,"clear b"),Condition(True,"on b c")],[]))
steps.append(Step(2, "mov c b table1",[Condition(True,"on c b"),Condition(True,"clear c"),Condition(True,"clear table1")],[Condition(True,"on a table0"),Condition(True,"on b a"),Condition(True,"clear b"),Condition(True,"clear c"),Condition(True,"on c table1")]))
steps.append(Step(3, "mov b a c",[Condition(True,"on b a"),Condition(True,"clear b"),Condition(True,"clear c")],[Condition(True,"clear a"),Condition(True,"clear b"),Condition(True,"on b c"),Condition(True,"on a table0"),Condition(True,"on c table1")]))
ordering_constraints = []
ordering_constraints.append([ 0, 2, 3, 1])
ordering_constraints.append([ 2, 1 ])
ordering_constraints.append([ 3, 1 ])
causal_links = []
causal_links.append(Link(0, 3, Condition(True, "on b a")))
causal_links.append(Link(0, 3, Condition(True, "clear c")))
causal_links.append(Link(0, 2, Condition(True, "clear table1")))
causal_links.append(Link(0, 2, Condition(True, "clear c")))
causal_links.append(Link(0, 2, Condition(True, "on c b")))
causal_links.append(Link(2, 3, Condition(True, "on b a")))
causal_links.append(Link(2, 3, Condition(True, "clear b")))
causal_links.append(Link(2, 3, Condition(True, "clear c")))
causal_links.append(Link(2, 1, Condition(True, "clear b")))

