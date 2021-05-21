from step import Step
from condition import Condition
from link import Link
steps = []
steps.append(Step(0, "start", [], [Condition(True, "on a b"), Condition(True, "on b table0"), Condition(True, "on c d"), Condition(True, "on d table1"), Condition(True, "clear a"), Condition(True, "clear c"), Condition(True, "clear table2")]))
steps.append(Step(1, "finish", [Condition(True, "on a b"), Condition(True, "on b c"), Condition(True, "on c d"), Condition(True, "on d table1"), Condition(True, "clear a"), Condition(True, "clear table0"), Condition(True, "clear table2")], []))
steps.append(Step(3, "move a b table2", [Condition(True, "on a b"), Condition(True, "clear a"), Condition(True, "clear table2")], [Condition(True, "on a table2"), Condition(True, "clear b"), Condition(False, "clear table2"), Condition(False, "on a b")]))
steps.append(Step(4, "move b table0 c", [Condition(True, "on b table0"), Condition(True, "clear c")], [Condition(True, "on b c"), Condition(True, "clear table0"), Condition(False, "clear c")]))
ordering_constraints = []
ordering_constraints.append([0, 3, 4, 1])
ordering_constraints.append([3, 4, 1])
ordering_constraints.append([4, 1])
causal_links = []
causal_links.append(Link(0, 3, Condition(True, "on a b")))
causal_links.append(Link(0, 3, Condition(True, "clear a")))
causal_links.append(Link(0, 3, Condition(True, "clear table2")))
causal_links.append(Link(0, 4, Condition(True, "on b table0")))
causal_links.append(Link(0, 4, Condition(True, "clear c")))
causal_links.append(Link(3, 4, Condition(True, "clear b")))
causal_links.append(Link(4, 1, Condition(True, "on b c")))
causal_links.append(Link(0, 1, Condition(True, "on c d")))
causal_links.append(Link(0, 1, Condition(True, "on d table1")))
causal_links.append(Link(0, 1, Condition(True, "clear a")))
causal_links.append(Link(4, 1, Condition(True, "clear table0")))

