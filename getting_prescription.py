import csv
import json
from typing import Dict, Optional
from random import randint

def load_patient_data(csv_filepath: str) -> Dict:
    patients = {}
    try:
        with open(csv_filepath, "r") as file:
            patients_data = csv.DictReader(file)
            for datarow in patients_data:
                pfile = {
                    "Diagnosis": datarow["Diagnosis"],
                    "ICD_code": datarow["ICD_code"],
                    "Drug": datarow["Drugname"],
                    "Frequency": datarow["Frequency"],
                    "Dosage": datarow["Dosage"]
                }
                patients[datarow["Patient ID"]] = pfile

        return patients
    except FileNotFoundError:
        print(f"Error: Could not find file {csv_filepath}")
        return {}
    except Exception as e:
        print(f"Error loading patient data: {str(e)}")
        return {}

def load_drug_data(json_filepath: str) -> Dict:
    try:
        with open(json_filepath, "r") as drugs_data_file:
            return json.load(drugs_data_file)
    except FileNotFoundError:
        print(f"Error: Could not find file {json_filepath}")
        return {}
    except Exception as e:
        print(f"Error loading drug data: {str(e)}")
        return {}

def find_drug_alternative(patient_id: str, diagnosis: str, current_drug: str, drug_data: Dict) -> Optional[tuple]:
    if diagnosis not in drug_data:
        print(f"Patient {patient_id}: No information available for diagnosis {diagnosis}.")
        return None

    # Check if current drug is available
    if current_drug in drug_data[diagnosis]:
        details = drug_data[diagnosis][current_drug]
        if details["quantity_left"] > 0:
            # Reduce the quantity of the current drug
            drug_data[diagnosis][current_drug]["quantity_left"] -= 1
            print(f"Patient {patient_id}: {current_drug} is available. Prescribing.")
            return (current_drug, details["dosage"])
        print(f"Patient {patient_id}: {current_drug} is out of stock.")

    # Look for alternatives
    for alternative_drug, alternative_details in drug_data[diagnosis].items():
        if alternative_details["quantity_left"] > 0:
            # Reduce the quantity of the alternative drug
            drug_data[diagnosis][alternative_drug]["quantity_left"] -= 1
            print(f"Patient {patient_id}: Alternative drug for {current_drug} is {alternative_drug}. Prescribing.")
            return (alternative_drug, alternative_details["dosage"])

    print(f"Patient {patient_id}: No drugs available for {diagnosis}.")
    return None


def update_patient_prescriptions(patients: Dict, drug_data: Dict) -> Dict:
    updated_patients = {}
    for patient_id, patient_info in patients.items():
        diagnosis = patient_info["Diagnosis"]
        current_drug = patient_info["Drug"]
        frequency = patient_info["Frequency"]
        cost = None

        # Attempt to find a drug or alternative
        drug_result = find_drug_alternative(
            patient_id,
            diagnosis,
            current_drug,
            drug_data
        )
        
        # Prepare updated patient info
        updated_info = {
            "Diagnosis": diagnosis,
            "ICD_code": patient_info["ICD_code"],
            "Drug": None,
            "Dosage": None,
            "Frequency": frequency,
            "Cost": None
        }
        
        # If a drug is found (original or alternative)
        if drug_result:
            prescribed_drug, dosage = drug_result
            updated_info["Drug"] = prescribed_drug
            updated_info["Dosage"] = dosage
            
            # Get the cost of the prescribed drug
            if diagnosis in drug_data and prescribed_drug in drug_data[diagnosis]:
                updated_info["Cost"] = drug_data[diagnosis][prescribed_drug].get("price_per_unit", None)
        
        updated_patients[patient_id] = updated_info
    
    return updated_patients
def save_updated_data(updated_patients: Dict, output_filepath: str) -> bool:
    try:
        with open(output_filepath, "w") as output_file:
            json.dump(updated_patients, output_file, indent=4)
        print(f"Updated patient information saved to {output_filepath}")
        return True
    except Exception as e:
        print(f"Error saving updated patient data: {str(e)}")
        return False

def main():
    # Load data
    patients = load_patient_data("eye_patient_info.csv")
    drugs_data = load_drug_data("pharmacy_drugs.json")
    
    if not patients or not drugs_data:
        print("Error: Could not proceed due to data loading errors")
        return
    
    # Process and update prescriptions
    updated_patients = update_patient_prescriptions(patients, drugs_data)
    
    # Save updated patient data
    save_updated_data(updated_patients, "updated_patients.json")
    
    # Save updated drug inventory
    try:
        with open("pharmacy_drugs.json", "w") as drugs_file:
            json.dump(drugs_data, drugs_file, indent=2)
        print("Updated drug inventory saved to pharmacy_drugs.json")
    except Exception as e:
        print(f"Error saving updated drug inventory: {str(e)}")

if __name__ == "__main__":
    main()