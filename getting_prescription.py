import csv
import json
from control_drugs import control_drugs, narcotics

def load_csv_data(file_path):
    """Load data from a CSV file and return it as a dictionary."""
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        return {row["Patient ID"]: {
            "Diagnosis": row["diagnosis"],
            "ICD_code": row["icd_code"],
            "Drug": row["drugname"],
            "Frequency": row["Frequency"],
            "Dosage": row["dosage"]
        } for row in reader}


def load_json_data(file_path):
    """Load data from a JSON file."""
    with open(file_path, "r") as file:
        return json.load(file)

def check_control(diagnosis):
    if diagnosis in control_drugs:
        return True
    return False

def check_narcotics(diagnosis):
    if diagnosis in narcotics:
        return True
    return False


def find_alternative_drug(drugs, diagnosis, current_drug):
    """
    Find an alternative drug for the given diagnosis.
    Returns the drug name and dosage, or None if no alternative is found.
    """
    for alternative_drug, details in drugs[diagnosis].items():
        if details["quantity_left"] > 0 and alternative_drug != current_drug:
            return alternative_drug, details["dosage"]
    return None, None


def update_patient_info(patient, drugs_data):
    """
    Update the drug and dosage for a patient based on availability.
    Returns updated patient information.
    """
    diagnosis = patient["Diagnosis"]
    current_drug = patient["Drug"]
    frequency = patient["Frequency"]

    updated_info = {
        "Diagnosis": diagnosis,
        "ICD_code": patient["ICD_code"],
        "Drug": None,
        "Dosage": None,
        "Frequency": frequency
    }

    if diagnosis in drugs_data:
        for drug, details in drugs_data[diagnosis].items():
            if drug == current_drug and not check_control(drug) and not check_narcotics(drug):
                if details["quantity_left"] > 0:
                    updated_info["Drug"] = drug
                    updated_info["Dosage"] = details["dosage"]
                    print(f"{current_drug} is available.")
                    return updated_info
                else:
                    print(f"{current_drug} is out of stock.")
                break

        # Find alternative drug if the current drug is unavailable
        alternative_drug, alternative_dosage = find_alternative_drug(drugs_data, diagnosis, current_drug)
        if alternative_drug:
            updated_info["Drug"] = alternative_drug
            updated_info["Dosage"] = alternative_dosage
            print(f"Alternative drug for {current_drug} is {alternative_drug}.")
        else:
            print(f"No drugs available for {diagnosis}.")
    else:
        print(f"No information available for diagnosis {diagnosis}.")

    return updated_info


def update_all_patients(patients, drugs_data):
    """Update drug and dosage information for all patients."""
    updated_patients = {}
    for patient_id, patient_info in patients.items():
        updated_patients[patient_id] = update_patient_info(patient_info, drugs_data)
    return updated_patients


def save_json_data(data, file_path):
    """Save data to a JSON file."""
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)


def main():
    # Load data
    patients = load_csv_data("eye_patient_info.csv")
    drugs_data = load_json_data("pharmacy_drugs.json")

    # Update patient data
    updated_patients = update_all_patients(patients, drugs_data)

    # Save updated data
    save_json_data(updated_patients, "updated_patients.json")
    print("Updated patient information saved to updated_patients.json.")


if __name__ == "__main__":
    main()


'''
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
'''