from db.run_sql import run_sql
from models.animal import Animal
from models.staff import Staff

    # def __init__(self, name, type, staff_id):

def save(animal):
    sql = "INSERT INTO animals (name, animal_type, staff_id) VALUES (%s, %s, %s) RETURNING *"
    values = [animal.name, animal.animal_type, animal.keeper.id]
    print('yoy')
    results = run_sql(sql, values)
    print('hey')
    id = results[0]['id']
    animal.id = id
    return animal


