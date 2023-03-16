import functions
import os


options = ['Create a person', 'Create a course record', 'Create a cohort','Assign student to cohort', 'Remove student from cohort','Deactive Course/Person/Cohort', 'Complete a course', 'Reactivate Course/Person/Cohort/Student_Cohort_registration', 'View active registrations for a cohort', 'View all active cohorts for a course', 'View all active people', 'Quit']

while True:
    # os.system('clear')

    print("\nCustomer Database\n---------------------------\n")
    for i, val in enumerate(options, start=1):
      print(f"{i}. {val}")
    print('\n---------------------------\n')
    
    user_input = input('What would you like to do? ')
    print()

    if user_input == '1':
       functions.add_a_person()
    elif user_input == '2':
      functions.add_a_course()
    elif user_input == '3':
       functions.add_a_cohort()
    elif user_input == '4':
       functions.add_student()
    elif user_input == '5':
       functions.update_student_reg()
    elif user_input == '6':
       deactive_list = ['Deactive Course', "Deactive Person", "Deactive Cohort"]
       for i, val in enumerate(deactive_list, start=1):
          print(f"{i}: {val}")
       deactive_input = input("\nwhat would you like to do?(SELECT BY NUMBER): ")
       if deactive_input == '1':
          functions.deactivate_course()
       elif deactive_input == '2':
          functions.deactivate_person()
       elif deactive_input == '3':
          functions.deactivate_cohort() 
    elif user_input == '7':
       functions.complete_course()
    elif user_input == '8':
       reactive_list = ['Reactive Course', "Reactive Person", "Reactive Cohort"]
       for i, val in enumerate(reactive_list, start=1):
          print(f"{i}: {val}")
       reactive_input = input("\nwhat would you like to do?(SELECT BY NUMBER): ")
       if reactive_input == '1':
          functions.reactivate_course()
       elif reactive_input == '2':
          functions.reactivate_person()
       elif reactive_input == '3':
          functions.reactivate_cohort()
    elif user_input == '9':
       functions.view_students_regs()
    elif user_input == '10':
       functions.view_cohort()
    elif user_input == '11':
       functions.view_people()
    else:
      break