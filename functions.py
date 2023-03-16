import database
from datetime import datetime, date, time

# ----------View all people function----------
def view_people():
    rows = database.find_all()
    
    print()
    print(f"{'ID':<9}{'First name':<20}{'Last name':<20}")
    print(f"{'--':<9}{'----------':<20}{'---------':<20}")

    for val in rows:
        print(f"{val[0]:<9}{val[1]:<20}{val[2]:<20}")
        print(f"{'--':<9}{'----------':<20}{'---------':<20}")

# View inactive people
def view_inactive_people():
    rows = database.find_all_inactive()
    
    print()
    print(f"{'ID':<9}{'First name':<20}{'Last name':<20}")
    print(f"{'--':<9}{'----------':<20}{'---------':<20}")

    for val in rows:
        print(f"{val[0]:<9}{val[1]:<20}{val[2]:<20}")
        print(f"{'--':<9}{'----------':<20}{'---------':<20}")



# ----------View all courses-----------
def view_courses():
    rows = database.find_course()
    
    print()
    print(f"{'ID':<9}{'Name':<30}{'Description':<40}")
    print(f"{'--':<9}{'----':<30}{'-----------':<40}")

    for val in rows:
        print(f"{val[0]:<9}{val[1]:<30}{val[2]:<40}")
        print(f"{'--':<9}{'----':<30}{'-----------':<40}")

# VIew all inactive courese
def view__inactive_courses():
    rows = database.find_not_active_course()
    
    print()
    print(f"{'ID':<9}{'Name':<30}{'Description':<40}")
    print(f"{'--':<9}{'----':<30}{'-----------':<40}")

    for val in rows:
        print(f"{val[0]:<9}{val[1]:<30}{val[2]:<40}")
        print(f"{'--':<9}{'----':<30}{'-----------':<40}")


# VIEW STUDENT REGISTRATIONS
def view_students_regs():
    rows = database.view_student_reg()

    print()
    print(f"{'ID':<9}{'First Name':<20}{'Last Name':<20}{'Cohort ID':<20}{'Registration Date':<20}")
    print(f"{'--':<9}{'----------':<20}{'---------':<20}{'---------':<20}{'-----------------':<20}")

    for val in rows:
        print(f"{val[0]:<9}{val[3]:<20}{val[4]:<20}{val[1]:<20}{val[2]:<20}")
        print(f"{'--':<9}{'----------':<20}{'---------':<20}{'---------':<20}{'-----------------':<20}")

# VIEW COHORT
def view_cohort():
    rows = database.view_cohort()
    
    print()
    print(f"{'ID':<9}{'Instructor ID':<20}{'Course ID':<20}{'start date':<20}{'active(1 is active 0 is NOT active)'}")
    print(f"{'--':<9}{'-------------':<20}{'---------':<20}{'----------':<20}{'-----------------------------------'}")

    for val in rows:
        print(f"{val[0]:<9}{val[1]:<20}{val[2]:<20}{val[3]:<20}{val[5]}")
        print(f"{'--':<9}{'-------------':<20}{'---------':<20}{'----------':<20}{'-----------------------------------'}")
    

# VIEW INACTIVE COHORTS
def view_inactive_cohort():
    rows = database.view_not_active_cohort()
    
    print()
    print(f"{'ID':<9}{'Instructor ID':<20}{'Course ID':<20}{'start date':<20}{'active(1 is active 0 is NOT active)'}")
    print(f"{'--':<9}{'-------------':<20}{'---------':<20}{'----------':<20}{'-----------------------------------'}")

    for val in rows:
        print(f"{val[0]:<9}{val[1]:<20}{val[2]:<20}{val[3]:<20}{val[5]}")
        print(f"{'--':<9}{'-------------':<20}{'---------':<20}{'----------':<20}{'-----------------------------------'}")

# ----------view  single person----------
def search_by_id(id):
    
    result = database.find_one_from_id(id)

    final_result = [result[0][0],result[0][1]]

    print()

    return final_result

# ----------remove student from cohort----------
def update_student_reg():

    view_people()

    user_input = input("\nWhat student would you like to remove from their cohort(SELECT BY ID): ")
    id_data = database.search_student_reg(user_input)
    
    values = [id_data[0][0],id_data[0][1],id_data[0][2]]
    
    for i, value in enumerate(values):
        if i == 0:
            print(f'Student ID: {value}')
        if i == 1:
            print(f"Cohort ID: {value}")
        elif i == 2:
            print(f"Registration date: {value}")
    
    value_to_update = input('\nAre you sure you would like to remove this student from this cohort?(Y or N): ')
    print()

    date = get_date()
    active = 0

    if value_to_update == 'y':
        values.append(date)
        values.append(active)
        database.update(values)
        return

# ----------To add a person----------
def add_a_person():
    while True:
        add_first_name = input('What is the persons first name: ')
        add_last_name = input('What is the persons last name: ')
        add_email = input('What is the new persons email: ')
        add_phone = input('What is the new persons phone number: ')
        add_street_address = input('What is the new persons street address: ')
        add_city = input('What is the new customers city: ')
        add_state = input('What is the new customers state: ')
        add_zip = input('What is the new customers zip code: ')
        add_password = input('What is the new persons password: ')

        new_customer = [add_first_name, add_last_name, add_email, add_phone, add_street_address, add_city, add_state, add_zip, add_password]

        add_new_user = input(f'{new_customer}\nAre you sure you would like to add this person?(Y or N or [Q]uit): ').lower()
                
        if add_new_user == 'y':
            database.add(new_customer)
            return 'Action Complete'
        elif add_new_user == 'q':
            break
        else:
            print('Ok try again')


# ----------To add a course----------
def add_a_course():
    while True:
        add_course_name = input('What is the name of this course: ')
        add_course_description = input('What is the course description: ')

        new_course = [add_course_name, add_course_description]

        add_new_course = input(f'{new_course}\nAre you sure you would like to add this course?(Y or N or [Q]uit): ').lower()
                
        if add_new_course == 'y':
            database.add_course(new_course)
            return 'Action Complete'
        elif add_new_course == 'q':
            break
        else:
            print('Ok try again')

# ----------To add a cohort----------
def add_a_cohort():
    while True:
        view_people()
        course_instructor = input('Choose the instructor for this cohort(SELECT BY ID): ')
        view_courses()
        course = input('What course are they teaching?(SELECT BY ID): ')

        start_date = get_date()
        new_cohort = [course_instructor, course, start_date]

        add_new_cohort = input(f'{new_cohort}\nAre you sure you would like to add this cohort?(Y or N or [Q]uit): ').lower()
                
        if add_new_cohort == 'y':
            database.add_cohort(new_cohort)
            return 'Action Complete'
        elif add_new_cohort == 'q':
            break
        else:
            print('Ok try again')

# ----------ADD STUDENT TO COHORT---------
def add_student():
    while True:
            view_people()
            cohort_student = input('Choose the student to add to this cohort(SELECT BY ID): ')
            view_courses()
            cohort = input('What cohort are they joining?(SELECT BY ID): ')

            reg_date = get_date()
            join_student = [cohort_student, cohort, reg_date]

            add_new_student = input(f'{join_student}\nAre you sure you would like to add this student?(Y or N or [Q]uit): ').lower()
                    
            if add_new_student == 'y':
                database.add_student_reg(join_student)
                return 'Action Complete'
            elif add_new_student == 'q':
                break
            else:
                print('Ok try again')


# ----------to remove a person----------
def remove_a_customer():
    rows = database.find_all()

    for val in rows:
        print(f"{val[0]:<13}{val[1]:<30}")
        print(f"{'-----------':<13}{'----':<30}")

    removed_customer = input('What customer would you like to remove?(SELECT BY ID): ')

    
    saved = database.find_one_from_id(removed_customer)
    print(f"\n{saved}\n")

    remove = input(f'Are you sure you would like to remove "{saved[0][1]}" from the data base? THIS IS PERMANENT(Y or N): ').lower()

    if remove == 'y':
       return database.delete(removed_customer)
    

# DEACTIVATE COURSE
def deactivate_course():
    while True:
        view_courses()
        user_input = input('which course would you like to deactivate?(SELECT BY ID [Q]uit): ').lower()

        blank_check = check_if_blank(user_input)
        if blank_check == False:
            continue

        checking = input(f'are you sure you want to deactivate this id -- {user_input}?(Y or N or [Q]uit): ').lower()

        if checking == 'y':
            database.deactivate_course(user_input)
            return
        elif checking == 'n':
            continue
        else:
            break

# DEACTIVATE PERSON
def deactivate_person():
    while True:
        view_people()
        user_input = input('which person would you like to deactivate?(SELECT BY ID [Q]uit): ').lower()
        blank_check = check_if_blank(user_input)
        if blank_check == False:
            continue
        checking = input(f'are you sure you want to deactivate this id -- {user_input}?(Y or N or [Q]uit): ').lower()

        if checking == 'y':
            database.deactivate_person(user_input)
            return
        elif checking == 'n':
            continue
        else:
            break

# DEACTIVATE cohort
def deactivate_cohort():
    while True:
        view_cohort()
        user_input = input('which cohort would you like to deactivate?(SELECT BY ID [Q]uit): ').lower()
        blank_check = check_if_blank(user_input)
        if blank_check == False:
            continue
        checking = input(f'are you sure you want to deactivate this id -- {user_input}? (Y or N or [Q]uit): ').lower()

        if checking == 'y':
            database.deactivate_cohort(user_input)
            return
        elif checking == 'n':
            continue
        else:
            break


# SET COMPLETion  DATE 
def complete_course():
    while True:
        view_people()
        completion_date = get_date()
        results = []
        user_input = input("what person has completed their course?(Choose by ID [Q]uit): ").lower()
        blank_check = check_if_blank(user_input)
        if blank_check == False:
            continue

        results.append(completion_date)
        results.append(user_input)

        print(results)

        check = input('is this the correct date and person id?(Y or N or [Q]uit): ').lower()

        if check == 'y':
            database.complete_course(results)
            return
        elif check == 'n':
            continue
        else:
            break

# ReACTIVATE COURSE
def reactivate_course():
    while True:
        view__inactive_courses()
        user_input = input('which course would you like to reactivate?(SELECT BY ID [Q]uit): ').lower()
        blank_check = check_if_blank(user_input)
        if blank_check == False:
            continue
        checking = input(f'are you sure you want to reactivate this id -- {user_input}?(Y or N or [Q]uit): ').lower()

        if checking == 'y':
            database.reactivate_course(user_input)
            return
        elif checking == 'n':
            continue
        else:
            break

# DEACTIVATE PERSON
def reactivate_person():
    while True:
        view_inactive_people()
        user_input = input('which person would you like to reactivate?(SELECT BY ID [Q]uit): ').lower()
        blank_check = check_if_blank(user_input)
        if blank_check == False:
            continue
        checking = input(f'are you sure you want to reactivate this id -- {user_input}?(Y or N or [Q]uit): ').lower()

        if checking == 'y':
            database.reactivate_person(user_input)
            return
        elif checking == 'n':
            continue
        else:
            break

# reACTIVATE cohort
def reactivate_cohort():
    while True:
        view_inactive_cohort()
        user_input = input('which cohort would you like to reactivate?(SELECT BY ID [Q]uit): ').lower()
        blank_check = check_if_blank(user_input)
        if blank_check == False:
            continue
        checking = input(f'are you sure you want to reactivate this id -- {user_input}? (Y or N or [Q]uit): ').lower()

        if checking == 'y':
            database.reactivate_cohort(user_input)
            return
        elif checking == 'n':
            continue
        else:
            break


# GET CURRENT TIME

def get_date():
    today = date.today()
    day_is = date.isoformat(today)

    return day_is

# CHeck for blank input


def check_if_blank(value):
    if value == 'q':
        return
    elif value == '':
        print(f'\n----------\nINVALID INPUT, PLEASE TRY AGAIN\n----------\n')
        return False
    else:
        True
    
     
