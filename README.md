# Article Sorter

Article Sorter is a Python-based application designed to process a set of links, store their content in a vector database, and categorize them by relevance to each other.

## Features
- Scrapes content from provided links.
- Processes and stores the content in a vector database.
- Categorizes the content based on relevance.

## Prerequisites
- Docker and Docker Compose installed on your system.
- Python 3.9 or higher.

## Setup and Run Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/cedricdcc/article_sorter.git
   cd article_sorter
   ```

2. Build and start the Docker containers:
   ```bash
   docker-compose up --build
   ```

3. Access the application:
   - The application dashboard will be available at `http://localhost:5000`.

## Testing the Project
1. Install the required Python dependencies:
   ```bash
   pip install -r docker-stack/app/requirements.txt
   ```

2. Run the test suite:
   ```bash
   pytest docker-stack/app/tests/
   ```

## File Structure
- `docker-stack/app/`: Contains the main application code.
- `docker-stack/data/`: Stores input data files.
- `docker-stack/`: Docker configuration files.

## Notes
- Ensure the `input.csv` file in `docker-stack/data/` contains the links to be processed.
- Use the `setup_ollama.sh` script for additional setup if required.
