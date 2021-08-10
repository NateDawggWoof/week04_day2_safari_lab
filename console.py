import pdb
from models.staff import Staff
from models.animal import Animal
from models.manager import Manager
import repos.staff_repo as staff_repo
import repos.animal_repo as animal_repo


staff_1 = Staff('Jeremy', 'Yoo')
staff_repo.save(staff_1)
staff_2 = Staff('Nathan', 'Pianu')
staff_repo.save(staff_2)

animal_1 = Animal('Joy', 'Tiger', staff_1)
animal_repo.save(animal_1)
animal_2 = Animal('Coy', 'Lion', staff_2)
animal_repo.save(animal_2)
animal_3 = Animal('Poy', 'Dog', staff_2)
animal_repo.save(animal_3)

pdb.set_trace()