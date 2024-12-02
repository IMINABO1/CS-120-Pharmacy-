# Python Script Documentation for Mini Virtual Hospital System - Pharmacy Module

This document provides a detailed overview of the Python scripts used in the **Mini Virtual Hospital System - Pharmacy Module**. Each script is responsible for different tasks, including processing patient data, checking for controlled substances, finding nearby pharmacies, and more.

---

## **1. `loc.py` - Find Nearby Pharmacies**

### Description:
This script is used to find pharmacies near a given location (ZIP code or latitude and longitude) using the **Google Places API**.

### Key Functions:

- **`get_nearby_pharmacies(api_key, location, radius=5000)`**
  - **Parameters**:
    - `api_key`: The API key for accessing Google services.
    - `location`: Can be a string (ZIP code or address) or a tuple representing latitude and longitude.
    - `radius`: The radius (in meters) within which to search for pharmacies. Defaults to 5000 meters.
  - **Returns**: A list of dictionaries, each containing the pharmacy's name, address, and geographical location.
  - **Example Output**:
    ```json
    {
      "name": "Pharmacy 1",
      "address": "123 Main St, City, State",
      "location": {
        "lat": 40.7128,
        "lng": -74.0060
      }
    }
    ```

### How it Works:
- The script checks if the `location` is a tuple (latitude, longitude). If not, it sends a geocoding request to Google Maps to get the latitude and longitude for the given ZIP code or address.
- It then queries the Google Places API for nearby pharmacies and extracts details like name, address, and location from the API response.

---

## **2. `getting_prescription.py` - Process and Update Prescriptions**

### Description:
This script loads patient data, checks prescriptions, validates dosages, and handles controlled substance alternatives.

### Key Functions:

- **`load_patient_data(csv_filepath: str)`**
  - Loads patient data from a CSV file.
  - **Returns**: A dictionary where keys are patient IDs and values are dictionaries containing diagnosis, ICD code, prescribed drugs, frequency, and dosage.

- **`load_drug_data(json_filepath: str)`**
  - Loads drug inventory data from a JSON file.
  - **Returns**: A dictionary containing drug names as keys and drug details (like quantity and price) as values.

- **`find_drug_alternative(patient_id, diagnosis, current_drug, drug_data)`**
  - Checks if a prescribed drug is available. If not, it finds an alternative drug.
  - **Returns**: A tuple containing the alternative drug and its dosage, or `None` if no alternative is available.

- **`update_patient_prescriptions(patients, drug_data)`**
  - Updates prescriptions for all patients based on drug availability.
  - **Returns**: A dictionary of updated patient records with new prescriptions, dosages, and costs.

- **`save_updated_data(updated_patients, output_filepath)`**
  - Saves the updated patient data to a JSON file.
  - **Returns**: `True` if successful, `False` otherwise.

### How it Works:
- The script loads patient data from a CSV file and drug inventory data from a JSON file.
- It checks if the prescribed drug is available and substitutes it with an alternative if necessary.
- After processing the prescriptions, it saves the updated patient records and drug inventory.

---

## **3. `control_drugs.py` - Controlled Drugs List**

### Description:
This script defines a Python set containing controlled substances like morphine. It can be used to check if a prescribed drug is controlled.

### Key Data:
- **`controlled_drugs`**: A set of controlled substances that need to be monitored.
  ```python
  controlled_drugs = {"morphine", "oxycodone", "fentanyl", "methadone"}
---

## **4. `scrape.py` - Scrape Controlled Drugs Data**

### Description:
This script scrapes an HTML file (`d.html`) to extract a list of controlled substances and their alternative names. It uses **BeautifulSoup** to parse the HTML content.

### How it Works:
- The script reads the `d.html` file, which contains a table with controlled substances and their alternative names.
- It extracts relevant data from the table rows, specifically looking for the substance names and their alternative names in the HTML file.
- The extracted data is stored in a set called `extracted_data`, ensuring unique entries for each substance or alternative name.

### Key Data:
- **`extracted_data`**: A set that contains the controlled substances and their alternative names.

### Example Output:
```json
{
  "Extracted Data": [
    "morphine",
    "fentanyl",
    "oxycodone",
    "hydrocodone",
    "codeine",
    "methadone"
  ]
}
```
### Dependencies for `scrape.py`

- **BeautifulSoup**: A Python library used to parse and extract data from HTML files.
  - To install BeautifulSoup, run:
    ```bash
    pip install beautifulsoup4
    ```

- **lxml**: A dependency for BeautifulSoup to parse HTML efficiently.
  - To install lxml, run:
    ```bash
    pip install lxml
    ```

- **HTML File**: The script expects an HTML file (`d.html`) from which it scrapes controlled drug data. Ensure this file is available in the working directory.

## **5. `output.py` - Format Patient Data for Billing and Client Teams**

### Description:
This script processes patient data and formats it for both the client team and billing team. It saves the formatted data into separate JSON files, which can be used by each team for their respective tasks.

### Key Classes:

- **`PatientDataHandler`**: A base class for handling patient data. This class is not used directly but serves as a parent class for the client and billing team handlers.
  - **Method**: `get_patient_data()` — This method is abstract and must be implemented by subclasses to define how patient data should be processed for each team.

- **`ClientTeamHandler`**: A subclass of `PatientDataHandler` that formats patient data for the client team. It focuses on providing data related to the diagnosis, prescribed drugs, dosage frequency, and cost for each patient.
  - **Key Method**: `get_patient_data()` — Returns a dictionary of patient data formatted for the client team, including diagnosis, prescribed drug, dosage, frequency, and drug cost.

- **`BillingTeamHandler`**: A subclass of `PatientDataHandler` that formats patient data for the billing team. It extracts the diagnosis and associated drug costs for billing purposes.
  - **Key Method**: `get_patient_data()` — Returns a dictionary of patient data formatted for the billing team, focusing on diagnosis and cost information.

### How it Works:
- The script loads patient data from `updated_patients.json`, which contains the updated prescriptions and costs.
- It uses the `ClientTeamHandler` and `BillingTeamHandler` classes to process the data for the respective teams.
- The processed data is then saved into separate JSON files:
  - **`client_team_data.json`**: Contains the client team data with diagnosis, prescribed drugs, dosage frequency, and cost.
  - **`billing_team_data.json`**: Contains the billing team data with diagnosis and cost.

### Example Output for Client Team:
```json
{
  "12345": {
    "Diagnosis": "Myopia",
    "Drug": "Atropine",
    "Dosage Frequency": "1 drop daily | Every morning",
    "Cost": 10.5
  },
  "67890": {
    "Diagnosis": "Pink Eye",
    "Drug": "Antibiotic Drops",
    "Dosage Frequency": "2 drops every 4 hours | As needed",
    "Cost": 12.75
  }
}
```
### Dependencies for `output.py`

No additional external dependencies are required for `output.py` since it only utilizes the built-in **JSON** module to process and save patient data.




