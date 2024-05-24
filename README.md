# Medical Data Scraper & Meilisearch Uploader

## Features
- Web Scraping: Extracts JSON medical data from a specified website
- Data Processing: Cleans and transforms data for efficient indexing
- Meilisearch Integration: Updates medical data on Meilisearch for fast and accurate search capabilities
- FastAPI: Built with FastAPI for high-performance and scalability

## Usage
Clone the repository and install dependencies with ```pip install -r requirements.txt```
Configure the web scraper by setting the WEBSITE_URL environment variable
Run the application with ```uvicorn main:app --host 0.0.0.0 --port 8000```
Send a POST request to ```/doctor/{doctor_name}``` to trigger the data scraping and Meilisearch update process

## Configuration
- WEBSITE_URL: URL of the website to scrape JSON medical data from.
- MEILISEARCH_URL: Set the URL of the Meilisearch instance (default: http://localhost:7700)

Contributing
Contributions are welcome! Open a pull request to add new features, improve performance, or enhance documentation.

License
This project is licensed under the MIT License.
