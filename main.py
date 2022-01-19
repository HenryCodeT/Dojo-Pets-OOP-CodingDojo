# from dojo_pets import Ninja
from ninja import Ninja

ninja1=Ninja("henry","torres","firulais","dog","galletas")
print(ninja1.__dict__)
ninja1.alimentar()
ninja1.pasear()
ninja1.bañar()
print(ninja1.__dict__)