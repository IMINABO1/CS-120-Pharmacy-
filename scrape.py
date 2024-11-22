from bs4 import BeautifulSoup

# Load the HTML content from the file
with open("d.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

# Create a set to store the extracted substances and other names
extracted_data = set()

# Find all table rows
rows = soup.find_all("tr")

# Loop through rows to extract "substance" and "other names"
for row in rows:
    cells = row.find_all("td")
    if len(cells) >= 5:  # Ensure there are enough cells in the row
        if  cells[3].get_text(strip=True)=="Y":
            substance = cells[0].get_text(strip=True)  # First column: Substance
            other_names = cells[4].get_text(strip=True)  # Fifth column: Other Names
            
            # Add the extracted text to the set
            if substance:
                extracted_data.add(substance)
            if other_names:
                extracted_data.add(other_names)

# Print the extracted data
print("Extracted Data:", extracted_data)
