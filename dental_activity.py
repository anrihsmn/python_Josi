
from dental_function import Appointment
from dental_function import Patient

appointment_objects = []

def check_list(appointment_info):
  for object in appointment_objects:
    name = object.get_apo_name()
    date = object.get_apo_date()
    reason = object.get_apo_reason()
    if appointment_info.get_apo_date() == date:
      return object
    else:
      return None

def show_lists():
  global appointment_objects
  for object in range(len(appointment_objects)):
    print(object, ")", appointment_objects[object].get_apo_name(), appointment_objects[object].get_apo_date())


while True:
  menu = input("Press 'a' to appoint, 'c' to cancel, 'q to quit: ")
  if menu == "a":
    apo_name = input("Enter your name: ")
    apo_date = input("Enter a date you want to appoint(mm-dd e.g. 04-15): ")
    apo_reason = input("Enter a reason: ")
    # here is fine for apo_reason place?

    info1 = Appointment(apo_name, apo_date, apo_reason)

    search_appointment = check_list(info1)
    if search_appointment is None:
      appointment_objects.append(info1)
      print("[Appointment success.]")
    else:
      dup_name = search_appointment.get_apo_name()
      dup_date = search_appointment.get_apo_date()
      dup_reason = search_appointment.get_apo_reason()
      print("[Appointment failed.]")
      print(dup_date, "is already appointed for ", dup_name)

  elif menu == "c":
    show_lists()
    selected_number = int(input("Choose the number you want to cancel: "))
    cancel_list = str(selected_number), ")", appointment_objects[selected_number].get_apo_name()
    print(cancel_list)
    # list is weired
    final_check = input("Are you sure to cancel?(y/n): ")
    if final_check == "y" or final_check == "Y":
      appointment_objects.remove(appointment_objects[selected_number])
      show_lists()
    else:
      print("Try again.")

  elif menu == "q":
    break

  else:
    print("Try again.")





patient_objects = []

def check_info(patient_info):
  for object in patient_objects:
    name = object.get_pt_name()
    age = object.get_pt_age()
    diagnosis = object.get_pt_diagnosis()
    treatment = object.get_pt_treatment()
    if patient_info.get_pt_name() == name:
      return object
    return None

def show_infos():
  global patient_objects
  for info in range(len(patient_objects)):
    print(info, ")", patient_objects[info].get_pt_name(), patient_objects[info].get_pt_age(), patient_objects[info].get_pt_diagnosis(), patient_objects[info].get_pt_treatment())


while True:
  pt_info_menu = input("Press 'r' to register, 'u' to update, 'q' to quit: ")
  if pt_info_menu == "r":
    patient_name = input("Enter the patient name: ")
    patient_age = input("Enter the patient age: ")
    patient_diagnosis = input("Enter the diagnosis: ")
    patient_treatment = input("Enter the treatment: ")

    pt1 = Patient(patient_name, patient_age, patient_diagnosis, patient_treatment)

    search_patient = check_info(pt1)
    if search_patient is None:
      patient_objects.append(pt1)
      print("[Registration success.]")
    else:
      dup_pt_name = search_patient.get_pt_name()
      dup_pt_age = search_patient.get_pt_age()
      dup_pt_diagnosis = search_patient.diagnosis()
      dup_pt_treatment = search_patient.get_pt_treatment()
      print("We already have ", dup_pt_name, "info. Try again.")

  elif pt_info_menu == "u":
    show_infos()
    selected_number = int(input("Choose number you want to update: "))
    selected_category = input("Press 'a' for age, 'd' for diagnosis, 't' for treatment: ")
    if selected_category == "a":
      update_age = input("Enter new age: ")
      patient_objects[selected_number].get_pt_age = update_age
      print(patient_objects[selected_number])
    elif selected_category == "d":
      update_diagnosis = input("Enter new diagnosis: ")
      patient_objects[selected_number].get_pt_diagnosis = update_diagnosis
      print(patient_objects[selected_number])
    elif selected_category == "t":
      update_treatment = input("Enter new treatment: ")
      patient_objects[selected_number].get_pt_diagnosis = update_treatment
      print(patient_objects[selected_number])
    else:
      print("Select category again.")

  elif pt_info_menu == "q":
    break

  else:
    print("Try again.")
