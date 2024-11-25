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

```plaintext
├── data/
│   └── controlled_substances_list.txt      # List of controlled substances
│   └── medications_info.json               # Dictionary of approved medications with dosages and prices
│   └── sample_patient_data.csv             # Sample CSV file with patient data
├── scripts/
│   └── pharmacy_module.py                  # Main script for processing prescriptions
├── README.md                               # Project documentation


```
## Usage Instructions
Prepare Input Data: Ensure the diagnosis team’s CSV file contains patient details, prescriptions, and dosages. Store the CSV file in the data/ folder.
Run the Pharmacy Module: Execute pharmacy_module.py to process the CSV file.
 Output:
If any prescription requires substitution or dosage validation, a notification will be generated.
A billing dictionary with itemized drug costs and balance amounts will be prepared for the insurance team.
## Dependencies
Python 3.x
Pandas (for CSV file handling)
JSON (for loading medication and dosage information)
Future Enhancements
Expand Ailment and Medication Range: Include additional ailments and medications.
Enhanced Billing Integration: Provide a dynamic billing system with detailed insurance handling.
Pharmacy Locator API: Integrate with external APIs to locate pharmacies more accurately.
## Contributors
This project was developed as part of a school assignment. We are a team of beginner developers working to understand basic principles of virtual health systems, CSV processing, and Python programming.

## License

This Markdown structure gives a clear and organized overview for your GitHub repository. Let me know if there are any other details you'd like to add!
