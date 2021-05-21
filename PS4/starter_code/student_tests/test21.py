from step import Step
from condition import Condition
from link import Link
steps = []
steps.append(Step(0, "start", [], [Condition(True, "on a b"), Condition(True, "on b table0"), Condition(True, "on c d"), Condition(True, "on d table1"), Condition(True, "clear a"), Condition(True, "clear c"), Condition(True, "clear table2")]))
steps.append(Step(1, "finish", [Condition(True, "on a b"), Condition(True, "on b c"), Condition(True, "on c d"), Condition(True, "on d table1"), Condition(True, "clear a"), Condition(True, "clear table0"), Condition(True, "clear table2")], []))
steps.append(Step(3, "move a b table2", [Condition(True, "on a b"), Condition(True, "clear a"), Condition(True, "clear table2")], [Condition(True, "on a table2"), Condition(True, "clear b"), Condition(False, "clear table2"), Condition(False, "on a b")]))
steps.append(Step(4, "move b table0 c", [Condition(True, "clear b"), Condition(True, "on b table0"), Condition(True, "clear c")], [Condition(True, "on b c"), Condition(True, "clear table0"), Condition(False, "clear c")]))
steps.append(Step(5, "move a table2 b", [Condition(True, "clear b"), Condition(True, "on a table2")], [Condition(True, "on a b"), Condition(False, "clear b"), Condition(True, "clear table2")]))
ordering_constraints = []
ordering_constraints.append([0, 3, 4, 5, 1])
ordering_constraints.append([3, 4, 5, 1])
ordering_constraints.append([4, 5, 1])
ordering_constraints.append([5, 0, 1])
causal_links = []
causal_links.append(Link(0, 3, Condition(True, "on a b")))
causal_links.append(Link(0, 3, Condition(True, "clear a")))
causal_links.append(Link(0, 3, Condition(True, "clear table2")))
causal_links.append(Link(0, 4, Condition(True, "on b table0")))
causal_links.append(Link(0, 4, Condition(True, "clear c")))
causal_links.append(Link(3, 4, Condition(True, "clear b")))
causal_links.append(Link(3, 5, Condition(True, "clear b")))
causal_links.append(Link(3, 5, Condition(True, "on a table2")))
causal_links.append(Link(5, 1, Condition(True, "on a b")))
causal_links.append(Link(4, 1, Condition(True, "on b c")))
causal_links.append(Link(0, 1, Condition(True, "on c d")))
causal_links.append(Link(0, 1, Condition(True, "on d table1")))
causal_links.append(Link(0, 1, Condition(True, "clear a")))
causal_links.append(Link(4, 1, Condition(True, "clear table0")))
causal_links.append(Link(5, 1, Condition(True, "clear table2")))

