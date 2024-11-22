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
            "Dosage": datarow["Dosage"],
            "Doctor_name": datarow["Doctor Name"],
            "Doctor_NPI": datarow["NPI"],
            "Specialization": datarow["Specialization"],
            "Doctor_ID": datarow["Doctor_ID"]
        }
        patients[datarow["Patient ID"]] = pfile


# Load doctor data from a CSV file
def doctor_verification(doctors_file):
    verified_doctors = {}
    with open(doctors_file, "r") as file:
        doctor_data = csv.DictReader(file)
        for row in doctor_data:
            verified_doctors[row["Doctor_ID"]] = {
                "Name": row["Name"],
                "Specialization": row["Specialization"],
                "License_Number": row["License_Number"],
                "Active_Status": row["Active_Status"],
            }
    return verified_doctors


# Load drug data from JSON
with open("pharmacy_drugs.json", "r") as drugs_data_file:
    drugs_data = json.load(drugs_data_file)

# Dictionary to store updated drug information for each patient
updated_patients = {}

# Check drug availability and verify doctor information
def availability(doctors_file):
    verified_doctors = doctor_verification(doctors_file)

    for patient_id, patient_info in patients.items():
        diagnosis = patient_info["Diagnosis"]
        current_drug = patient_info["Drug"]
        frequency = patient_info["Frequency"]
        dosage = patient_info["Dosage"]
        doctor_id = patient_info["Doctor_ID"]
        doctor_npi = patient_info["Doctor_NPI"]
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

        # Verify the doctor
        if doctor_id not in verified_doctors:
            print(f"Patient {patient_id}: Doctor not registered.")
            continue

        doctor_details = verified_doctors[doctor_id]
        if (
            doctor_details["Name"] != patient_info["Doctor_name"]
            or doctor_details["Specialization"] != patient_info["Specialization"]
            or doctor_details["License_Number"] != patient_info["Doctor_NPI"]
            or doctor_details["Active_Status"] != "Active"
        ):
            print(f"Patient {patient_id}: Doctor is not active or details mismatch.")
            continue

        # Look for the diagnosis in the drug database
        drug_found = False
        if diagnosis in drugs_data:
            for drug, details in drugs_data[diagnosis].items():
                if drug == current_drug:
                    # Check if the current drug is available
                    if details["quantity_left"] > 0:
                        updated_info["Drug"] = drug
                        updated_info["Dosage"] = dosage
                        updated_info["Price"] = details["price_per_unit"]
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
                        updated_info["Price"] = alternative_details["price_per_unit"]
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
    writer.writerows(availability("doctor_data.csv").values())

print("Updated patient information saved to updated_patients.csv.")
