#!/usr/bin/env python3

class Set():
    def __init__(self, content=[]):
        self.content = list(set(content))
        self.content.sort()
    
    def add(self, element):
        if element not in self.content:
            self.content.append(element)
            self.content.sort()
    
    def __len__(self):
        return len(self.content)
    
    def __sub__(self, other):
        self.content = list(set(self.content) - set(other.content))
        self.content.sort()
        return self
    
    def __iter__(self):
        return iter(self.content)    