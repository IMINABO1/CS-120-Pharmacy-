import csv
import json

# Load patient data from CSV
with open("eye_patient_info.csv", "r") as file:
    patients_data = csv.DictReader(file)
    patients = {}

    # Diagnosis will contain drug, dosage, frequency, and patient name
    for datarow in patients_data:
        pfile = {
            "Name": datarow["Name"],  # Include the patient name here
            "Diagnosis": datarow["Diagnosis"],
            "ICD_code": datarow["ICD_code"],
            "Drug": datarow["Drugname"],
            "Frequency": datarow["Frequency"],
            "Dosage": datarow["Dosage"]
        }
        patients[datarow["Patient ID"]] = pfile

# Load drug data from JSON
with open("pharmacy_drugs.json", "r") as drugs_data_file:
    drugs_data = json.load(drugs_data_file)

# Dictionary to store updated drug information for each patient
updated_patients = {}

# Check drug availability and find alternatives
def availability():
    for patient_id, patient_info in patients.items():
        diagnosis = patient_info["Diagnosis"]
        current_drug = patient_info["Drug"]
        frequency = patient_info["Frequency"]
        dosage = patient_info["Dosage"]
        drug_found = False
        updated_info = {
            "Patient ID": patient_id,
            "Name": patient_info["Name"],
            "Diagnosis": diagnosis,
            "ICD_code": patient_info["ICD_code"],
            "Drug": None,
            "Dosage": None,
            "Frequency": frequency,
            "Price": None,
        }

        # Look for the diagnosis in the drug database
        if diagnosis in drugs_data:
            for drug, details in drugs_data[diagnosis].items():
                if drug == current_drug:
                    # Check if the current drug is available
                    if details["quantity_left"] > 0:
                        updated_info["Drug"] = drug
                        updated_info["Dosage"] = dosage
                        updated_info["Price"] = "$"+str(details["price_per_unit"])
                        print(f"Patient {patient_id}: {current_drug} is available.")
                        drug_found = True
                    else:
                        print(f"Patient {patient_id}: {current_drug} is out of stock.")
                    break  # Stop checking further drugs for the current drug

            # If the current drug is unavailable, suggest the next available drug
            if not drug_found:
                for alternative_drug, alternative_details in drugs_data[diagnosis].items():
                    if alternative_details["quantity_left"] > 0:
                        updated_info["Drug"] = alternative_drug
                        updated_info["Dosage"] = alternative_details["dosage"]
                        updated_info["Price"] = "$"+str(alternative_details["price_per_unit"])
                        print(f"Patient {patient_id}: Alternative drug for {current_drug} is {alternative_drug}.")
                        break
                else:
                    print(f"Patient {patient_id}: No drugs available for {diagnosis}.")
        else:
            print(f"Patient {patient_id}: No information available for diagnosis {diagnosis}.")

        # Add the updated info to the new dictionary
        updated_patients[patient_id] = updated_info

    return updated_patients

# Write the updated patient information to a CSV file
with open("updated_patients.csv", "w", newline="") as output_file:
    fieldnames = ["Patient ID", "Name", "Diagnosis", "ICD_code", "Drug", "Dosage", "Frequency", "Price"]
    writer = csv.DictWriter(output_file, fieldnames=fieldnames)

    # Write the header
    writer.writeheader()

    # Write the rows
    writer.writerows(availability().values())

print("Updated patient information saved to updated_patients.csv.")
