import csv
import json

# Load patient data from CSV
with open("eye_patient_info.csv", "r") as file:
    patients_data = csv.DictReader(file)
    patients = {}

    for datarow in patients_data:
        pfile = {
            "Diagnosis": datarow["diagnosis"],
            "ICD_code": datarow["icd_code"],
            "Drug": datarow["drugname"],
            "Frequency": datarow["Frequency"],
            "Dosage": datarow["dosage"]
        }
        patients[datarow["Patient ID"]] = pfile

with open("pharmacy_drugs.json", "r") as drugs_data_file:
    drugs_data = json.load(drugs_data_file)

updated_patients = {}

# Check drug availability and find alternatives
for patient_id, patient_info in patients.items():
    diagnosis = patient_info["Diagnosis"]
    current_drug = patient_info["Drug"]
    frequency = patient_info["Frequency"]
    dosage = patient_info["Dosage"]
    drug_found = False
    updated_info = {
        "Diagnosis": diagnosis,
        "ICD_code": patient_info["ICD_code"],
        "Drug": None,
        "Dosage": None,
        "Frequency": frequency,
    }

    # Look for the diagnosis in the drug database
    if diagnosis in drugs_data:
        for drug, details in drugs_data[diagnosis].items():
            if drug == current_drug:
                if details["quantity_left"] > 0:
                    updated_info["Drug"] = drug
                    updated_info["Dosage"] = details["dosage"]
                    print(f"Patient {patient_id}: {current_drug} is available.")
                    drug_found = True
                else:
                    print(f"Patient {patient_id}: {current_drug} is out of stock.")
                break

        if not drug_found:
            for alternative_drug, alternative_details in drugs_data[diagnosis].items():
                if alternative_details["quantity_left"] > 0:
                    updated_info["Drug"] = alternative_drug
                    updated_info["Dosage"] = alternative_details["dosage"]
                    print(
                        f"Patient {patient_id}: Alternative drug for {current_drug} is {alternative_drug}."
                    )
                    break
            else:
                print(f"Patient {patient_id}: No drugs available for {diagnosis}.")
    else:
        print(f"Patient {patient_id}: No information available for diagnosis {diagnosis}.")

    updated_patients[patient_id] = updated_info

# Save the updated patient information to a new JSON file
with open("updated_patients.json", "w") as output_file:
    json.dump(updated_patients, output_file, indent=4)

print("Updated patient information saved to updated_patients.json.")
