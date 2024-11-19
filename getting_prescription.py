import csv

with open("eye_patient_info.csv", "r") as file:
    patients_data = csv.DictReader(file)
    diagnosis = {}
    # Diagnosis will contain drug, dosage, frequency
    for datarow in patients_data:
        diagnosis["diagnosis"] = {"diagnosis": datarow["diagnosis"], "icd_code": datarow["icd_code"],"Drug": datarow["drugname"], "Frequency": datarow["Frequency"]}
        diagnosis["dosage"] = datarow["dosage"]
file.close()

with open("drugfile.csv","r") as drugfile:
    drugfile = csv.DictReader(drugfile)
    for druginfo in drugfile:
        if diagnosis["drug"] in druginfo:
            if druginfo["controlled"] == "Y":
                #replace with a non-controlled drug
                #add the price to the pharmacy data
        else:
            #replace with an available drug
            #add the price of the drug to the pharmacy data
drugfile.close()