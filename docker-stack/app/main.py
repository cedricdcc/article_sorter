# Main application logic for the Docker stack


import os
from scraper import extract_abstract_from_website
from pdf_processor import extract_text_from_pdf, generate_abstract_from_text
from vector_db import connect_to_vector_db, store_data_in_vector_db
from dashboard import start_dashboard
from utils import validate_url, categorize_article
import csv


def main():
    print("Starting the application...")

    # Connect to the vector database
    db_connection = connect_to_vector_db()
    if not db_connection:
        print("Failed to connect to the vector database.")
        return

    # cgeck what directory the script is running in and print all files in the directory
    current_directory = os.getcwd()
    print(f"Current directory: {current_directory}")
    print("Files in the current directory:")
    for file in os.listdir(current_directory):
        print(file)

    # go one level higher then the cwd and print all files in the directory
    parent_directory = os.path.dirname(current_directory)
    print(f"Parent directory: {parent_directory}")

    # Read the input CSV file
    input_file = os.path.join("..", "data", "input.csv")
    with open(input_file, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            url = row["URL"]
            collection = row["Collection"]

            if not validate_url(url):
                print(f"Invalid URL: {url}")
                continue

            # Categorize as PDF or website
            if url.endswith(".pdf"):
                print(f"Processing PDF: {url}")
                text = extract_text_from_pdf(url)
                abstract = generate_abstract_from_text(text) if text else None
            else:
                print(f"Processing website: {url}")
                abstract = extract_abstract_from_website(url)

            # Categorize the article if no collection is provided
            if not collection:
                collection = categorize_article(None, abstract or "")

            # Store the data in the vector database
            data = {
                "url": url,
                "collection": collection,
                "abstract": abstract,
            }
            store_data_in_vector_db(data)

    # Start the dashboard
    start_dashboard()


if __name__ == "__main__":
    main()
