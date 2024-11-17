import json
#Retrieve the doctor info from json file
with open("Patient_data.json") as file:
    patientinfo = json.load(file)

file.close()

pharmacy_drugs = ["Paracetamol", "etc"]

#Gets the patient informatin from the doctor file
patientid = patientinfo["patient"]
patientid = patientid["id"]

#Get the medical information regarding the eye disease
medical_info= patientinfo["medicalRecord"]
diagnosis = diagnosis["diagnosis"]

#Get the prescription from the doctor file
prescription = patientinfo["prescription"]

#Get a different drug if current drug from initial prescription in not at the pharmacy
for drug in prescription:
    if  drug["name"] not in pharmacy_drugs:
        for redrug in pharmacy_drugs:
            if redrug["symptoms"] == medical_info["symptoms"]:
                #Take that drug and its precription



