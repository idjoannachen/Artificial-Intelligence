#!/usr/bin/env python3

from condition import Condition

class Link(object):
    def __init__(self, id1, id2, effect):
        if isinstance(id1, int) and isinstance(id2, int) and isinstance(effect, Condition):
            self.id1 = id1 # int
            self.id2 = id2 # int
            self.effect = Condition(effect.getState(), effect.getPredicate())
        else:
            raise Exception("[Link]: invalid parameters types")

    def getFirstId(self):
        return self.id1

    def getSecondId(self):
        return self.id2

    def getEffect(self):
        return self.effect

