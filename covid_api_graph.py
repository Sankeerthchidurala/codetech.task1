import requests  # Used to make API calls
import matplotlib.pyplot as plt  # Used for data visualization

def fetch_covid_data():
    """
    Fetch COVID-19 data from the disease.sh public API.
    Returns a list of dictionaries containing country data.
    """
    url = "https://disease.sh/v3/covid-19/countries"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise error for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return []

def process_data(data):
    """
    Process the data to extract top 10 countries by total COVID cases.
    Returns lists of country names and their corresponding case counts.
    """
    # Sort data by total cases in descending order
    sorted_data = sorted(data, key=lambda x: x['cases'], reverse=True)[:10]
    
    countries = [country['country'] for country in sorted_data]
    cases = [country['cases'] for country in sorted_data]
    
    return countries, cases

def visualize_data(countries, cases):
    """
    Create a bar chart to visualize COVID cases by country.
    """
    plt.figure(figsize=(12, 6))
    plt.bar(countries, cases, color='skyblue')
    plt.title("Top 10 Countries by COVID-19 Cases")
    plt.xlabel("Country")
    plt.ylabel("Total Cases")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

def main():
    """
    Main function to integrate API fetching, processing, and visualization.
    """
    print("Fetching COVID-19 data...")
    data = fetch_covid_data()
    
    if data:
        print("Processing data...")
        countries, cases = process_data(data)
        
        print("Visualizing data...")
        visualize_data(countries, cases)
    else:
        print("No data to display.")

# Run the program
if __name__ == "__main__":
    main()
