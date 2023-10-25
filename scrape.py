import requests
from bs4 import BeautifulSoup

def fetch_gas_prices():
    # Weekly Retail Gasoline and Diesel Prices from U.S. Energy Information Administration
    URL = 'https://www.eia.gov/dnav/pet/pet_pri_gnd_dcus_r40_w.htm'
    response = requests.get(URL)
    
    if response.status_code != 200:
        print("Failed to get data")
        return
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    gas_data = {}  # Dictionary to store gas type and their respective prices
    
    # Find all 'td' tags with class 'DataStub1'
    for gas_type_tag in soup.find_all('td', {'class': 'DataStub1'}):
        gas_type = gas_type_tag.get_text().strip()  # Get the text and remove extra spaces
        
        # Check if the gas_type is one of the types we are interested in
        if gas_type in ['Regular', 'Midgrade', 'Premium']:
            prices = []
            
            # Get the next 6 'td' tags with class 'DataB' or 'Current2' for the prices
            for price_tag in gas_type_tag.find_next_siblings('td', {'class': ['DataB', 'Current2']}, limit=6):
                price = float(price_tag.get_text().strip())
                prices.append(price)
            
            gas_data[gas_type] = prices

    print(gas_data)  # This will print the extracted gas data.

if __name__ == "__main__":
    fetch_gas_prices()
