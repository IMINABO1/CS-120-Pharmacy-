import csv

with open("eye_patient_info.csv", "r") as file:
    patients_data = csv.DictReader(file)
    diagnosis = {}
    # Diagnosis will contain drug, dosage, frequency
    for datarow in patients_data:
        diagnosis["diagnosis"] = {"diagnosis": datarow["diagnosis"], "icd_code": datarow["icd_code"], \
                                  "Drug": datarow["drugname"], "Frequency": datarow["Frequency"]}
        diagnosis["dosage"] = datarow["dosage"]
file.close()

with open("c_cs_alpha (1).csv","r") as drugs_data_file:
    drugs_data_file = csv.DictReader(drugs_data_file)
    for drug in drugs_data_file:
        if diagnosis["drugname"] == drug["Substance"] or diagnosis["drugname"] == drug["Other_Name"]:
            if drug["Controlled"] == "Y":
                continue
            else:
                diagnosis["drugname"] = drug["Substance"]
                
                
                
                