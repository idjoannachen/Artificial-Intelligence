#!/usr/bin/env python3

class Plan(object):
    def __init__(self, steps, ordering_constraints, causal_links):
        if isinstance(steps, list) and isinstance(ordering_constraints, list) and isinstance(causal_links, list):
            self.steps = []
            self.ordering_constraints = []
            self.causal_links = []
            
            for step in steps:
                self.steps.append(step)
            for ordering_constraint in ordering_constraints:
                self.ordering_constraints.append(ordering_constraint)
            for causal_link in causal_links:
                self.causal_links.append(causal_link)
            
        else:
            raise Exception("[Plan]: invalid parameter types")

    def getSteps(self):
        return self.steps

    def getOrderingConstraints(self):
        return self.ordering_constraints

    def getCausalLinks(self):
        return self.causal_links
    
    def getStep(self, stepId):
        for step in self.steps:
            if step.getId() == stepId:
                return step
        return None

