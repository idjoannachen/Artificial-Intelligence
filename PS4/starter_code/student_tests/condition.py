#!/usr/bin/env python3

# 
#  * Predicate list must be of the format:
#  * 		Clear command: { "clear", "c" }, meaning (c is clear)
#  * 		On command: { "on", "a", "b" }, meaning (a is on b)
#  * or of the format:
#  * 		Clear command: { "clear c" }, meaning (c is clear)
#  * 		On command: { "on a b" }, meaning (a is on b)
#  *
#

class Condition(object):
    def __init__(self, state, predicate):
        if isinstance(state, bool):
            self.state = state # True/False
        else:
            raise Exception("[Condition]: state in the wrong format")
        
        self.predicate = []
        if isinstance(predicate, str):
            predicate = predicate.strip().split()
        elif isinstance(predicate, list):
            pass
        else:
            raise Exception("[Condition]: predicate in the wrong format")
        
        for element in predicate:
            self.predicate.append(element)

    def getState(self):
        return self.state

    def getPredicate(self):
        return self.predicate

