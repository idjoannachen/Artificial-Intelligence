#!/usr/bin/env python3

class Animal:
    def __init__(self, species, name, hp, pp):
        self._species = species
        self._name = name
        self._hp = hp
        self._pp = pp
        
    def __str__(self):
        return self._species + ", " + self._name + ", " + str(self._hp) + ", " + str(self._pp)    
        
    def get_species(self):
        return self._species
    
    def get_name(self):
        return self._name
    
    def get_hp(self):
        return self._hp
    
    def get_pp(self):
        return self._pp
        