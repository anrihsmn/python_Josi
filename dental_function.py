
class Appointment:
  def __init__(self, apo_name, apo_date, apo_reason):
    self.apo_name = apo_name
    self.apo_date = apo_date
    self.apo_reason = apo_reason
  
  def get_apo_name(self):
    return self.apo_name
  
  def get_apo_date(self):
    return self.apo_date
  
  def get_apo_reason(self):
    return self.apo_reason



class Patient:
  def __init__(self,pt_name, pt_age, pt_diagnosis, pt_treatment):
    self.pt_name = pt_name
    self.pt_age = pt_age
    self.pt_diagnosis = pt_diagnosis
    self.pt_treatment = pt_treatment
  
  def get_pt_name(self):
    return self.pt_name
  
  def get_pt_age(self):
    return self.pt_age
  
  def get_pt_diagnosis(self):
    return self.pt_diagnosis
  
  def get_pt_treatment(self):
    return self.pt_treatment
