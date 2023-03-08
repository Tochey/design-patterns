from abc import abstractmethod, ABC
from dataclasses import dataclass
from typing import Optional

#often leads to tight coupling and code duplication
@dataclass
class Monster(ABC):
    name : str
    
    def talk(self):
        return f'My name is {self.name}'
    
    def attack(self):
        print(f'{self.name} attacked')
        
    def walk(self):
        print(f'{self.name} walked')

class FlyingMonster(Monster):
    def fly(self):
        print(f'{super().talk()} and i flew')
        

class SwimmingMonster(Monster):
    def swim(self):
        print(f'{super().talk()} and i swam')

class FlyingSwimmingMonster(Monster):
    pass
    
#class heirachy 
@dataclass    
class SwimmingMonster:
    name : str
    def swim(self):
        print(f'{self.name} swam' )

@dataclass
class FlyingMonster:
    name : str
    def fly(self):
        print(f'{self.name} flew' )

@dataclass
class SwimmingAndFlyingMonster:
    name : str
    def canFlyAndSwim(self):
        print(f'{self.name} flew and swam' )
        
@dataclass
class Monster:
    canSwim : Optional[SwimmingMonster] = None
    canFly : Optional[FlyingMonster] = None
    canFlyAndSwim : Optional[SwimmingAndFlyingMonster] = None
    name : str = ""
        
    def performAction(self):
        if self.canFly is not None:
            return self.canFly.fly()
        if self.canSwim is not None:
            return self.canSwim.swim()
        if self.canFlyAndSwim is not None:
            return self.canFlyAndSwim.canFlyAndSwim()
    
    def attack(self):
        print(f'{self.name} attacked')
        
    def walk(self):
        print(f'{self.name} walked')
        
        
if __name__ == "__main__":
    # eagle = FlyingMonster("eagle")
    # eagle.walk()
    # eagle.fly()
    # fish = SwimmingMonster('fish')
    # fish.walk()
    # fish.swim()
    fish = SwimmingAndFlyingMonster("dragon")
    swimmingMonster = Monster( canFlyAndSwim=fish, name="fish",)
    swimmingMonster.performAction()
    
    
   