import pdb
from models.staff import Staff
import repos.staff_repo as staff_repo

staff_1 = Staff('Jeremy', 'Yoo')
staff_repo.save(staff_1)
staff_2 = Staff('Nathan', 'Pianu')
staff_repo.save(staff_2)

pdb.set_trace()