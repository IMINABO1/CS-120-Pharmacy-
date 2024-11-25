import json

class PatientDataHandler:
    def __init__(self, data):
        self.data = data

    def get_patient_data(self):
        raise NotImplementedError("Subclasses must implement this method")


class ClientTeamHandler(PatientDataHandler):
    def get_patient_data(self):
        result = {}
        for patient_id, details in self.data.items():
            result[patient_id] = {
                "Diagnosis": details["Diagnosis"],
                "Drug": details["Drug"],
                "Dosage Frequency": f"{details['Dosage']} | {details['Frequency']}",
                "Cost": details["Cost"]
            }
        return result

class BillingTeamHandler(PatientDataHandler):
    def get_patient_data(self):
        result = {}
        for patient_id, details in self.data.items():
            result[patient_id] = {
                "Diagnosis": details["Diagnosis"],
                "Cost": details["Cost"]
            }
        return result

# Load the JSON data from an external source
with open("updated_patients.json", "r") as file:
    data = json.load(file)

# Instantiate and use the classes
client_handler = ClientTeamHandler(data)
billing_handler = BillingTeamHandler(data)

# Get data for client team
client_data = client_handler.get_patient_data()
with open("client_team_data.json", "w") as client_file:
    json.dump(client_data, client_file, indent=4)
print("Client Team Data saved to 'client_team_data.json'.")

# Get data for billing team
billing_data = billing_handler.get_patient_data()
with open("billing_team_data.json", "w") as billing_file:
    json.dump(billing_data, billing_file, indent=4)
print("Billing Team Data saved to 'billing_team_data.json'.")
