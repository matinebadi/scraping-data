

Product Information Scraper and Database API

This project provides an API that scrapes product data from an e-commerce website and stores it in a PostgreSQL database. Users can interact with the data through a set of endpoints to add, update, delete, and view product details. The project uses FastAPI for building the API, psycopg2 for database interaction, and BeautifulSoup for web scraping.

Features

Add New Products: Allows adding new product data to the database.

Update Product Information: Updates existing product information.

Delete Products: Deletes a product from the database by its name.

Show All Products: Retrieves and displays all stored product information.

Automated Scraping: Automatically scrapes product data from an external website and populates the database.


Requirements

Python 3.7+

PostgreSQL

FastAPI

Uvicorn (ASGI server)

BeautifulSoup

psycopg2

Requests


Installation

1. Clone the repository:

git clone https://github.com/yourusername/product-scraper-api.git
cd product-scraper-api


2. Install the required dependencies:

pip install -r requirements.txt


3. Set up PostgreSQL:

Install PostgreSQL if it's not installed.

Create a database called etlphone and a table users to store product data with the following schema:


CREATE TABLE users (
    name VARCHAR(255),
    link TEXT,
    price DECIMAL,
    category VARCHAR(255)
);


4. Configure your PostgreSQL credentials:

Edit the postgres.py file and replace the user, password, host, and database values with your PostgreSQL connection details.




Usage

1. Run the API:

Start the FastAPI application using uvicorn:

uvicorn main:app --reload

This will run the API locally on http://127.0.0.1:8000.


2. API Endpoints:

POST /add/: Add a new product to the database.

Parameters: name, link, price, category

Example:

{
    "name": "Product Name",
    "link": "https://product-link.com",
    "price": "100.00",
    "category": "Electronics"
}


POST /refresh/: Automatically scrape and add product data from the website.

This will fetch product details from the specified website and store them in the database.


PUT /update/{item_name}: Update product information.

Parameters: name (existing product name), obj (field to update), newobj (new value for the field)

Example:

{
    "name": "Product Name",
    "obj": "price",
    "newobj": "120.00"
}


DELETE /delete/: Delete a product by name.

Parameters: item_name (name of the product to delete)


GET /show/: View all products in the database.




Code Breakdown

1. FastAPI Application (main.py):

The FastAPI application defines several endpoints that interact with the database and the web scraper functions.

Uses POST for adding and refreshing products, PUT for updating, and DELETE for removing products.



2. Database Interaction (postgres.py):

The file contains functions for adding, updating, deleting, and showing products in the PostgreSQL database using psycopg2.

SQL queries are executed to modify and retrieve product data.



3. Web Scraping (scrap.py):

The GetUrls function scrapes product URLs from the specified e-commerce website.

The GetDatas function scrapes detailed product information, including name, price, category, description, and availability.

All product data is collected and returned as a list of dictionaries.




Example Flow

1. The user hits the POST /refresh/ endpoint.


2. The web scraper fetches product data from the external website.


3. The data is added to the PostgreSQL database via the Add function.


4. The user can query, update, or delete products through the corresponding API endpoints.



Contributing

If you'd like to contribute to this project, feel free to fork the repository, make changes, and create a pull request.

License

This project is licensed under the MIT License - see the LICENSE file for details.



