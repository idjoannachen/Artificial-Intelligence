from step import Step
from condition import Condition
from link import Link

steps = []
steps.append(Step(0, "start", [], [Condition(True, "on b table0"),
                                   Condition(True, "clear b"),
                                   Condition(True, "on a table1"),
                                   Condition(True, "clear a"),
                                   Condition(True, "clear table2"),
                                   Condition(True, "on d table3"),
                                   Condition(True, "on c d"),
                                   Condition(True, "clear c")]))

steps.append(Step(1, "finish", [Condition(True, "on c table2"),
                                Condition(True, "on d c"),
                                Condition(True, "on a d"),
                                Condition(True, "on b a"),
                                Condition(True, "clear table0"),
                                Condition(True, "clear table1"),
                                Condition(True, "clear table3")], []))

steps.append(Step(2, "move c d table2", [Condition(True, "clear c"),
                                         Condition(True, "on c d"),
                                         Condition(True, "clear table2")],
                                        [Condition(True, "on c table2"),
                                         Condition(True, "clear d"),
                                         Condition(False, "on c d"),
                                         Condition(False, "clear table2")]))

steps.append(Step(3, "move d table3 c", [Condition(True, "clear d"),
                                         Condition(True, "on d table3"),
                                         Condition(True, "clear c")],
                                        [Condition(True, "on d c"),
                                         Condition(True, "clear table3"),
                                         Condition(False, "on d table3"),
                                         Condition(False, "clear c")]))

steps.append(Step(4, "move a table1 d", [Condition(True, "clear a"),
                                         Condition(True, "on a table1"),
                                         Condition(True, "clear d")],
                                        [Condition(True, "on a d"),
                                         Condition(True, "clear table1"),
                                         Condition(False, "on a table1"),
                                         Condition(False, "clear d")]))

steps.append(Step(5, "move b table0 a", [Condition(True, "clear b"),
                                         Condition(True, "on b table0"),
                                         Condition(True, "clear a")],
                                        [Condition(True, "on b a"),
                                         Condition(True, "clear table0"),
                                         Condition(False, "on b table0"),
                                         Condition(False, "clear a")]))

ordering_constraints = []
ordering_constraints.append([0, 1, 2, 3, 4, 5])
ordering_constraints.append([2, 1, 3, 4, 5])
ordering_constraints.append([3, 1, 4, 5])
ordering_constraints.append([4, 1, 5])
ordering_constraints.append([5, 1])

causal_links = []
causal_links.append(Link(0, 2, Condition(True, "clear c")))
causal_links.append(Link(0, 2, Condition(True, "on c d")))
causal_links.append(Link(0, 2, Condition(True, "clear table2")))
causal_links.append(Link(0, 3, Condition(True, "on d table3")))
causal_links.append(Link(0, 3, Condition(True, "clear c")))
causal_links.append(Link(0, 4, Condition(True, "clear a")))
causal_links.append(Link(0, 4, Condition(True, "on a table1")))
causal_links.append(Link(0, 5, Condition(True, "clear b")))
causal_links.append(Link(0, 5, Condition(True, "on b table0")))
causal_links.append(Link(0, 5, Condition(True, "clear a")))
causal_links.append(Link(2, 3, Condition(True, "clear d")))
causal_links.append(Link(2, 4, Condition(True, "clear d")))
causal_links.append(Link(5, 1, Condition(True, "on b a")))
causal_links.append(Link(5, 1, Condition(True, "clear table0")))
causal_links.append(Link(4, 1, Condition(True, "on a d")))
causal_links.append(Link(4, 1, Condition(True, "clear table1")))
causal_links.append(Link(3, 1, Condition(True, "on d c")))
causal_links.append(Link(3, 1, Condition(True, "clear table3")))
causal_links.append(Link(2, 1, Condition(True, "on c table2")))
