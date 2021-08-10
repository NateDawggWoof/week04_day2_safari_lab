from db.run_sql import run_sql
from models.staff import Staff

# def save(user): O
def save(staff):
    sql = "INSERT INTO staffs (first_name, last_name) VALUES (%s, %s) RETURNING *"
    values = [staff.first_name, staff.last_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    staff.id = id
    return staff

# def select_all(): O
def select_all():
    staffs = []
    sql = "SELECT * FROM staffs"
    results = run_sql(sql)
    for row in results:
        staff = Staff(row['first_name'], row['last_name'], row['id'])
        staffs.append(staff)
    return staffs

# def select(id): O
def select(id):
    staff = None
    sql = "SELECT * FROM staffs WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        staff = Staff(result['first_name'], result['last_name'], result['id'])
    return staff

# def delete_all():
def delete_all():
    sql = "DELETE FROM staffs"
    run_sql(sql)

# def delete(id): O
def delete(id):
    sql = "DELETE FROM staffs WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# def update(user): O
def update(staff):
    sql = "UPDATE staffs SET (first_name, last_name) = (%s, %s) WHERE id = %s"
    values = [staff.first_name, staff.last_name, staff.id]
    run_sql(sql, values)
