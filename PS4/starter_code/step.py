#!/usr/bin/env python3

# 
#  * Operator should follow the format:
#  *	"start", designate the start state
#  * 	"finish", designate the end state
#  * 	"move a b", designate that you intend to move a onto b
#  *
#

class Step(object):
    def __init__(self, identity, operator, preconditions, effects):
        if isinstance(identity, int) and isinstance(operator, str) and isinstance(preconditions, list) and isinstance(effects, list):
            self.identity = identity
            self.operator = operator
            self.preconditions = []
            self.effects = []
            
            for precondition in preconditions:
                self.preconditions.append(precondition)
            for effect in effects:
                self.effects.append(effect)
                
        else:
            raise Exception("[Step]: invalid parameter types")

    def getId(self):
        return self.identity

    def getOperator(self):
        return self.operator

    def getPrecondition(self):
        return self.preconditions

    def getEffect(self):
        return self.effects
    
    def __lt__(self, other):
        return self.getId() < other.getId()

