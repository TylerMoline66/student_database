import sqlite3
connection = sqlite3.connect('cohort_info.db')
cursor = connection.cursor()

# ------------------------------FIND ONE BY ID QUERY------------------------------
def find_one_from_id(value):
  query = 'SELECT first_name, last_name From people WHERE person_id = ?'
  results =  cursor.execute(query, (value,)).fetchall()
  return results 

# ------------------------------SEARCH ALL CUSTOMERS QUERY------------------------------
def find_all():
  query = 'SELECT person_id, first_name, last_name FROM people WHERE active = 1 ORDER BY first_name'
  rows = cursor.execute(query).fetchall()
  return rows

# FIND ALL INACTIVE PEOPLE
def find_all_inactive():
  query = 'SELECT person_id, first_name, last_name FROM people WHERE active = 0 ORDER BY first_name'
  rows = cursor.execute(query).fetchall()
  return rows


# SEARCH ALL COURSES
def find_course():
  query = 'SELECT course_id, name, description FROM courses WHERE active = 1'
  rows = cursor.execute(query).fetchall()
  return rows

# SEARCH ALL INACTIVE COURSES
def find_not_active_course():
  query = 'SELECT course_id, name, description FROM courses WHERE active = 0'
  rows = cursor.execute(query).fetchall()
  return rows

# SEARCH ALL COHORTS
def find_cohort():
  query = 'SELECT cohort_id FROM cohorts'
  rows = cursor.execute(query).fetchall()
  return rows

# VIEW COHORTS
def view_cohort():
  query = 'SELECT * FROM cohorts WHERE active = 1'
  rows = cursor.execute(query).fetchall()
  return rows

# VIEW INACTIVE COHORTS
def view_not_active_cohort():
  query = 'SELECT * FROM cohorts WHERE active = 0'
  rows = cursor.execute(query).fetchall()
  return rows

# view STUDENT REGISTRATIONS
def view_student_reg():
  query = 'SELECT scr.student_id, scr.cohort_id, scr.registration_date, p.first_name, p.last_name FROM student_cohort_registrations scr, people p WHERE scr.student_id = p.person_id;'

  rows = cursor.execute(query).fetchall()

  return rows

# SEARCH ONE REGISTRATION
def search_student_reg(value):

  query = 'SELECT student_id, cohort_id, registration_date FROM student_cohort_registrations WHERE student_id = ?;'
  rows = cursor.execute(query, (value,)).fetchall()
  return rows

# add Student_registration
def add_student_reg(value):
  values = [value[0], value[1], value[2]]

  query = 'INSERT into Student_Cohort_Registrations (student_id, cohort_id, registration_date) values (?, ?, ?)'

  cursor.execute(query, values)
  connection.commit()


# Create Cohort
def add_cohort(value):
  values = [value[0], value[1], value[2]]
  query = 'INSERT into cohorts (instructor_id, course_id, start_date) values (?, ?, ?)'

  cursor.execute(query, values)
  connection.commit()

# ------------------------------ADD NEW PERSON QUERY------------------------------
def add(input):
  values = (input[0], input[1], input[2], input[3], input[8], input[4], input[5], input[6], input[7])

  query = 'INSERT into People (first_name, last_name, email, phone, password, address, city, state, postal_code) values (?, ?, ?, ?, ?, ?, ?, ?, ?)'
  cursor.execute(query, values)
  connection.commit()


# ------------------------------CREATE COURSE QUERY------------------------------

def add_course(value):
  values = [value[0], value[1]]

  query = 'INSERT into courses (name, description) values (?, ?)'
  cursor.execute(query, values)
  connection.commit()





# ------------------------------UPDATE CUSTOMER QUERY------------------------------
def update(value):

  query = 'UPDATE student_cohort_registrations SET drop_date = ?, active = ? WHERE student_id = ?'

  values = (value[3], value[4], value[0])

  cursor.execute(query, values)

  user_input = input('Are you sure??(Y or N): ' )

  if user_input == 'y':  
    connection.commit()
    return

# ------------------------------REMOVE CUSTOMER QUERY------------------------------
def delete(value):
  query = 'DELETE FROM customers WHERE customer_id = ?'

  cursor.execute(query, (value,))
  final_check = input('ARE YOU SURE!?!?!(Y or N): ').lower()

  if final_check == 'y':
    connection.commit()

# DEACTIVE COURSE
def deactivate_course(value):
  query = 'UPDATE courses SET active = 0 WHERE course_id = ?'
  cursor.execute(query, (value,))
  connection.commit()

# DEACTIVATE PERSON
def deactivate_person(value):
  query = 'UPDATE people SET active = 0 WHERE person_id = ?'
  cursor.execute(query, (value,))
  connection.commit() 

# DEACTIVATE COHORT 
def deactivate_cohort(value):
  query = 'UPDATE cohorts SET active = 0 WHERE cohort_id = ?'
  cursor.execute(query, (value,))
  connection.commit() 

# COMPLETE A COURSE
def complete_course(value):
  query = 'UPDATE student_cohort_registrations SET completion_date = ?, active = 0 WHERE student_id = ?'
  values = (value[0], value[1])

  cursor.execute(query, values)
  connection.commit() 

# Reactivate course
def reactivate_course(value):
  query = 'UPDATE courses SET active = 1 WHERE course_id = ?'
  cursor.execute(query, (value,))
  connection.commit()

# reACTIVATE PERSON
def reactivate_person(value):
  query = 'UPDATE people SET active = 1 WHERE person_id = ?'
  cursor.execute(query, (value,))
  connection.commit() 

# reACTIVATE COHORT 
def reactivate_cohort(value):
  query = 'UPDATE cohorts SET active = 1 WHERE cohort_id = ?'
  cursor.execute(query, (value,))
  connection.commit() 