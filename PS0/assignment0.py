#!/usr/bin/env python3
  
# TODO 1: Please add an import statement to correctly import animals.
# After you correctly add this line, you will not get an error after implementing TODO 2.

from animals import Animal
  
def read_all_animals(file_name):
    """
    Given the name of the file, it should return a list of Animal objects.
    
    file_name: a string of the name of the file
    
    Return: a list a Animal objects
    Example [<Animal object 1>, <Animal object 2>, ...]
    """

    results = []
    
    all_animals = open(file_name, "r")
    for animal in all_animals:
        animal = animal.strip()
        if animal:
            animal = animal.split(",")
            # TODO 2: Please add the corresponding animal objects to the results list.
            # After you correctly implement this, you should see the following lines when you run this script:
            """
            cat, c1, 1, 95
            dog, d 1, 100, 90
            dog, d2, 90, 59
            pig, pig_1, 2, 60
            pig, pig_2, 3, 60
            chinchilla, c1, 100, 49
            chinchilla, c2, 90, 15
            chinchilla, c3, 95, 79
            capybara, c1, 79, 3
            """
            results.append(Animal(animal[0], animal[1], int(animal[2]), int(animal[3])))

    all_animals.close()
    
    for result in results:
        print(str(result))

    return results
  
def animal_with_highest_average_hp(animals):
    """
    Given the list of Animal objects, it will return a list of animal species that has the highest average hp. If there are ties, return all of them.
    
    animals: a list of Animal objects
    
    Return: a list string of species
    Example ["dog", "chinchilla"]
    """
    
    hp = {}
    
    for animal in animals:
        species = animal.get_species()
        if species not in hp.keys():
            hp[species] = []
        hp[species].append(animal.get_hp())
            
    hp_average = {}
    
    for species, hps in hp.items():
        average = sum(hps) * 1.0 / len(hps)
        if average not in hp_average.keys():
            hp_average[average] = []
        hp_average[average].append(species)
    
    results = []
    
    # TODO 3: Please add the species with the highest average hp to the results list.
    # After you correctly implement this, and correctly implement TODO 7, you should see the the following lines when you run this script (the order could be different):
    """
    dog
    chinchilla
    """

    for avg, species in hp_average.items():
        if avg == max(hp_average.keys()):
            results.extend(species)

    for result in results:
        print(result)
    
    return results

def highest_pp_of_each_species(animals):
    """
    Given the list of Animal objects, it will return a list of animal names that has the highest pp in that species. If there are ties, return all of them.
    
    animals: a list of Animal objects
    
    Return: a list string of species
    Example ["c1", "dog1"]
    """
    
    all_pp = {}
    
    for animal in animals:
        species = animal.get_species()
        name = animal.get_name()
        pp = animal.get_pp()
        if species not in all_pp.keys():
            all_pp[species] = {}
        if pp not in all_pp[species].keys():
            all_pp[species][pp] = []
        all_pp[species][pp].append(name)
    
    results = []
    
    # TODO 4: Please add the names with the highest pp in that species to the results list.
    # After you correctly implement this, you should see the the following lines when you run this script (the order could be different):
    """
    c3
    pig_1
    pig_2
    d 1
    c1
    c1
    """

    for animal, pp_species in all_pp.items():
        highest_pp = max(pp_species.keys())
        for pp, sp in pp_species.items():
            if pp == highest_pp:
                results.extend(sp)
        
    for result in results:
        print(result)
    
    return results

if __name__ == "__main__":
    # TODO 5: Please uncomment the line below before you hand in the assignment.
    all_animals = read_all_animals("animals.txt")
    
    # TODO 6: Please comment the line below before you hand in the assignment.
    # all_animals = read_all_animals("sample.txt")    
    
    highest_average_hp = []

    # TODO 7: Please call the function animal_with_highest_average_hp with correct parameters, and assign the result to highest_average_hp.
    highest_average_hp = animal_with_highest_average_hp(all_animals)
    highest_pp = highest_pp_of_each_species(all_animals)

    highest_average_hp.sort()
    highest_pp.sort()
    
    # TODO 8: Please uncomment the line below before you hand in the assignment.
    output = open("answers.txt", "w")    
    
    # TODO 9: Please comment the line below before you hand in the assignment.
    # output = open("sample_answers.txt", "w")
    
    for species in highest_average_hp:
        output.write(species)
        output.write("\n")
        
    for names in highest_pp:
        output.write(names)
        output.write("\n")
    
    output.close()
