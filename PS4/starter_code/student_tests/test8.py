from step import Step
from condition import Condition
from link import Link
steps = []
steps.append(Step(0, "start", [], [ Condition(True, "clear table1"), Condition(True, "clear table2"), Condition(True, "clear table3"), Condition(True, "on a table0"), Condition(True, "on b a"), Condition(True, "on c table4"), Condition(True, "on d c"), Condition(True, "clear b"), Condition(True, "clear d")]))
steps.append(Step(1, "finish", [ Condition(True, "on d table0"), Condition(True, "on a table1"), Condition(True, "on b table2"), Condition(True, "on c table3"), Condition(True, "clear table4"), Condition(True, "clear d"), Condition(True, "clear a"), Condition(True, "clear b"), Condition(True, "clear c") ], []))
ordering_constraints = []
ordering_constraints.append([0,5,2,3,4,1])
ordering_constraints.append([2,5,1])
ordering_constraints.append([4,3,1])
ordering_constraints.append([5,4,1])
causal_links = []
causal_links.append(Link(0,5,Condition(True, "clear table1")))
causal_links.append(Link(0,2,Condition(True, "clear table2")))
causal_links.append(Link(0,3,Condition(True, "clear table3")))
causal_links.append(Link(0,5,Condition(True, "on a table0")))
causal_links.append(Link(0,2,Condition(True, "on b a")))
causal_links.append(Link(0,3,Condition(True, "on c table4")))
causal_links.append(Link(0,4,Condition(True, "on d c")))
causal_links.append(Link(0,1,Condition(True, "clear b")))
causal_links.append(Link(0,2,Condition(True, "clear b")))
causal_links.append(Link(0,1,Condition(True, "clear d")))
causal_links.append(Link(0,4,Condition(True, "clear d")))
causal_links.append(Link(2,1,Condition(True, "on b table2")))
causal_links.append(Link(2,1,Condition(True, "clear a")))
causal_links.append(Link(2,5,Condition(True, "clear a")))
causal_links.append(Link(3,1,Condition(True, "clear table4")))
causal_links.append(Link(3,1,Condition(True, "on c table3")))
causal_links.append(Link(4,1,Condition(True, "on d table0")))
causal_links.append(Link(4,3,Condition(True, "clear c")))
causal_links.append(Link(4,1,Condition(True, "clear c")))
causal_links.append(Link(5,4,Condition(True, "clear table0")))
causal_links.append(Link(5,1,Condition(True, "on a table1")))

