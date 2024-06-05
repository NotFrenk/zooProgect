class Animal:
    def __init__ (self, name:str, species:str, age:int, height:float, width:float, preferred_habitat:str):
        self.name:str = name
        self.species:str = species
        self.age:int = age
        self.height:float = height
        self.width:float = width
        self.preferred_habitat :str =preferred_habitat
        self.health:float=round(100 * (1 / age), 3)

        if self.age <= 0:  
            self.age= 1
        elif self.height <=0: 
            self.height=2
        elif self.width <=0: 
            self.width=1


class Fence:
    def __init__(self, area:float, temperature:float, habitat:str):
        self.area = area
        self.temperature = temperature
        self.habitat = habitat
        self.animals :list[Animal]= []

        if self.area <= 0:  
            self.area= 10




class ZooKeeper:
    def __init__(self, name:str, surname:str, id:str):
        self.name:str=name
        self.surname:str = surname
        self.id:str = id



    def add_animal(self, animal: Animal, fence: Fence,):
        if fence.area >= animal.height * animal.width and fence.habitat in animal.preferred_habitat.split(','):
            fence.area -= animal.height * animal.width
            fence.animals.append(animal)
        
    def remove_animal(self, animal:Animal, fence:Fence, ):
        if animal in fence.animals:
            fence.animals.remove(animal)
            fence.area += animal.height * animal.width

    def feed(self, animal: Animal):
        if animal.health < 100 and fence.area >= animal.height * animal.width * 1.02:
            animal.health += 1
            animal.height *= 1.02
            animal.width *= 1.02
            fence.area -= animal.height * animal.width

                    

    def clean(self,fence: Fence):
        if fence.area == 0:
            return 0.0
        else:
            occupied_area = sum(animal.height * animal.width for animal in fence.animals)
            return occupied_area / fence.area if fence.area != 0 else occupied_area
        


class Zoo:
    def __init__(self, fences:list[Fence], zoo_kepers:list[ZooKeeper]):
        self.fences:list[Fence] = fences
        self.zoo_keepers:list[ZooKeeper] = zoo_kepers
    
        




    def describe_zoo(self):
        description ="Guardians:\n"
        for keeper in self.zoo_keepers:
            description += f"ZooKeeper(name={keeper.name}, surname={keeper.surname}, id={keeper.id})\n"

        description += "Fences:\n"
        for fence in self.fences:
            description += f"Fence(area={fence.area}, temperature={fence.temperature}, habitat={fence.habitat})\nwith animals:\n"
            if fence.animals:
                for animal in fence.animals:
                    description += f"    Animal(name={animal.name}, species={animal.species}, age={animal.age}, height={animal.height}, width={animal.width}, preferred_habitats={animal.preferred_habitat})\n"
            else:
                description += "    No animals in this fence.\n"
            description += "#" * 30 + "\n"
        print(description)




