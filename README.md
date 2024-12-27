

ETL Phone Product Scraper & Database API

This project is a Python-based web scraper and API service designed to extract product details from an e-commerce website and store them in a PostgreSQL database. Built using FastAPI for the web server, BeautifulSoup for scraping, and psycopg2 for interacting with the PostgreSQL database, this tool simplifies the process of extracting, updating, and managing product data.

Features

Add Product: Insert new products into the database.

Refresh Data: Automatically refresh the product data by scraping the latest information from the target website.

Update Product: Update the details of an existing product.

Delete Product: Remove a product from the database.

Show All Products: Retrieve and display a list of all products in the database.


Requirements

Python 3.7+

PostgreSQL Database

FastAPI

Uvicorn (for running the server)

psycopg2 (for PostgreSQL integration)

BeautifulSoup (for scraping)


Installation

1. Clone this repository:

git clone https://github.com/your-username/etl-phone-scraper.git
cd etl-phone-scraper


2. Install dependencies:

pip install -r requirements.txt


3. Set up the PostgreSQL database:

Create a database named etlphone.

Make sure the table users exists with columns: name, link, price, category.



4. Configure database connection in the script (adjust username, password, and host as needed):

connected = psycopg2.connect(user='postgres', password='yourpassword', host="localhost", port=5432, database="etlphone")



Running the API

To start the FastAPI server, run the following command:

uvicorn main:app --reload

The server will start on http://127.0.0.1:8000. You can now use the following endpoints.

API Endpoints

1. Add Product

POST /add/
Adds a new product to the database.

{
    "name": "Product Name",
    "link": "http://product-link.com",
    "price": "299.99",
    "category": "Electronics"
}

2. Refresh Data

POST /refresh/
Scrapes the latest product data and inserts it into the database.

3. Update Product

PUT /update/{item_name}
Updates a product's name or price in the database.

{
    "name": "Updated Product Name",
    "price": "249.99"
}

4. Delete Product

DELETE /delete/
Deletes a product from the database based on the product's name.

{
    "item_name": "Product Name"
}

5. Show All Products

GET /show/
Returns a list of all products stored in the database.

[
    {
        "name": "Product Name",
        "link": "http://product-link.com",
        "price": "299.99",
        "category": "Electronics"
    },
    ...
]

How It Works

1. Scraping: The GetDatas function scrapes product data from a predefined e-commerce website using BeautifulSoup. It collects information such as the product name, price, category, and description.


2. Database Interaction: The psycopg2 library is used to interact with a PostgreSQL database, allowing you to insert, update, delete, and display product data.


3. FastAPI: The API is built with FastAPI, providing a modern and efficient way to expose the product data to clients. Uvicorn serves the FastAPI app.



Contributing

Contributions are welcome! If you'd like to improve or extend the project, feel free to submit a pull request.

