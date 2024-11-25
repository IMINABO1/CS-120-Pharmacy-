# Mini Virtual Hospital System - Pharmacy Module

This project is a mini virtual hospital system developed for educational purposes, focusing on providing basic pharmacy services for specific ailments. The system handles ailments such as myopia, pink eye, dry eyes, and general conditions like headaches, stress, and anxiety. As beginners, our scope is limited to these cases to provide a manageable approach to learning and implementing basic health system functionalities.

## Project Overview

The pharmacy module of this virtual hospital system is designed to:

- **Process Patient Data**: Receive patient information from the diagnosis team in CSV format.
- **Check for Controlled Substances**: Verify if prescribed drugs are controlled substances and substitute them with approved alternatives if necessary.
- **Validate Dosages**: Ensure dosage information is provided; if missing, request it from the diagnosis team.
- **Provide Billing Information**: Include the price of each medication in the billing output and accommodate partial insurance payments.

## Data Flow

1. **CSV Input**: A CSV file containing patient bio-details, insurance information, ICD codes, prescriptions, and dosages is uploaded by the diagnosis team.
2. **Controlled Substance Check**: The system cross-checks prescribed drugs with a predefined list of controlled substances.
3. **Substitution and Dosage Verification**: 
   - If a controlled drug is detected, it is substituted with a safe alternative from a dictionary containing approved medications for each ailment and age range.
   - If a prescribed medication lacks a dosage, the system flags it and returns the file to the diagnosis team for correction.
4. **Billing and Insurance**: The cost of each medication is calculated. If the insurance only covers part of the cost, the system will output the balance for the patient.
5. **Pharmacy Location Output**: Using the doctor’s provided ZIP code, the system suggests the nearest pharmacy for patient convenience.

## File Structure

## File Structure

```plaintext
CS-120-PHARMACY/
├── control_drugs.py              # Script to handle controlled drugs
├── d.html                        # HTML file for controlled drugs
├── d.pdf                         # PDF file for controlled drugs
├── doctor_data.csv               # CSV file containing doctor-related data
├── drug.json                     # JSON file for drug data
├── eye_patient_info.csv          # CSV file with patient details for eye-related ailments
├── getting_prescription.py       # Script for processing prescription data
├── loc.py                        # Script for finding nearest pharmacies
├── pharmacy_drugs.json           # JSON file containing pharmacy drug details
├── README.md                     # Project documentation
├── requirements.txt              # File listing project dependencies
├── scrape.py                     # Script for scraping data (e.g., from HTML)
├── updated_patients.json         # JSON file containing updated patient details
├── output.py                     # Generates the JSON for the different Billing and Client team respectively
├── billing_team_data.json        # The billing team output
├── client_team_data.json         # The client team output
```
## Usage Instructions
Prepare Input Data: Ensure the diagnosis team’s CSV file contains patient details, prescriptions, and dosages. Store the CSV file in the data/ folder.
Run the Pharmacy Module: Execute pharmacy_module.py to process the CSV file.
 Output:
If any prescription requires substitution or dosage validation, a notification will be generated.
A billing dictionary with itemized drug costs and balance amounts will be prepared for the insurance team.
## Dependencies
Python 3.x
CSV (for CSV file handling)
JSON (for loading medication and dosage information)
Google Places API (to locate pharmacies more accurately)
Future Enhancements
Expand Ailment and Medication Range: Include additional ailments and medications.
Enhanced Billing Integration: Provide a dynamic billing system with detailed insurance handling.
## Contributors
This project was developed as part of a school assignment. We are a team of beginner developers working to understand basic principles of virtual health systems, CSV processing, and Python programming.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.


