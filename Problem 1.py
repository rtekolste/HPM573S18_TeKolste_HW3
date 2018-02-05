#Rebecca TeKolste
#Problem 1

#cost/emergency dept = $1000
#cost/hospitalization = $2000

class Patient:
    def __init__(self, name):
        self.name=name
    def discharge(self):
        pass
    #This abstract method will have the function of printing all names
    #on each list which called

class EmergencyPatient(Patient):
    def __init__(self, name):
        Patient.__init__(self, name)
        self.ecost=1000
    def discharge(self):
        print(self.name, "Emergency")

class HospitalizedPatient(Patient):
    def __init__(self, name):
        Patient.__init__(self, name)
        self.ecost=2000
    def discharge(self):
         print(self.name, "Hospitalized")


class Hospital:
    def __init__(self):
        self.patients = []
        self.cost = 0

    def admit(self, patients):
        #This function admits a patient of any type
        self.patients.append(patients)

    def discharge_all(self):
        for patients in self.patients:
            patients.discharge()
            self.cost += patients.ecost
        #This calls all of the patients to be discharged
    def get_total_cost(self):
        return self.cost

P1=HospitalizedPatient("P1")
P2=HospitalizedPatient("P2")
P3=EmergencyPatient("P3")
P4=EmergencyPatient("P4")
P5=EmergencyPatient("P5")

##2 hospitalized and three emergency

YNHH=Hospital()

#Then run admit function to admit patients to the hospital
YNHH.admit(P1)
YNHH.admit(P2)
YNHH.admit(P3)
YNHH.admit(P4)
YNHH.admit(P5)

YNHH.discharge_all()
print(YNHH.get_total_cost())
