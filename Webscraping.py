# Basic Web Scraper: Fetch News Headlines
import requests
from bs4 import BeautifulSoup

def fetch_headlines(url):
    try:
        # Send a GET request to the website
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        
        # Parse HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract headlines (adjust selector based on website structure)
        headlines = soup.find_all('h3')  # example: most news sites use <h3> for headlines
        
        if headlines:
            print(f"\nNews Headlines from {url}:\n")
            for i, headline in enumerate(headlines[:10], start=1):  # Display top 10
                print(f"{i}. {headline.get_text(strip=True)}")
        else:
            print("No headlines found. The HTML structure may be different.")
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")

# Main program
def main():
    print("Basic Web Scraper: Fetch News Headlines")
    url = input("Enter the website URL (e.g., https://www.bbc.com/news): ")
    fetch_headlines(url)

if __name__ == "__main__":
    main()
