

# 📱 **ETL Phone Product Scraper & Database API** 🚀

Welcome to the **ETL Phone Product Scraper**! This project is a **Python**-based web scraper and API service designed to extract product details from an e-commerce website and store them in a **PostgreSQL** database. Built using **FastAPI** for the web server, **BeautifulSoup** for scraping, and **psycopg2** for interacting with the PostgreSQL database, this tool simplifies the process of extracting, updating, and managing product data.

---

## 🌟 **Features**

- **Add Product**: Add new products to the database.
- **Refresh Data**: Automatically refresh product data by scraping the latest information.
- **Update Product**: Modify the details of an existing product.
- **Delete Product**: Remove a product from the database.
- **Show All Products**: Retrieve and display all products in the database.

---

## 🛠 **Requirements**

Before you get started, ensure you have the following installed:

- Python 3.7+
- PostgreSQL Database
- FastAPI
- Uvicorn (for running the server)
- psycopg2 (for PostgreSQL integration)
- BeautifulSoup (for scraping)

---

## 📥 **Installation**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/etl-phone-scraper.git
   cd etl-phone-scraper

2. Install Dependencies:

pip install -r requirements.txt


3. Set Up PostgreSQL Database:

Create a database named etlphone.

Ensure the table users exists with the following columns:

name

link

price

category




4. Configure Database Connection: Update the connection parameters in the script:

connected = psycopg2.connect(user='postgres', password='yourpassword', host="localhost", port=5432, database="etlphone")




---

🚀 Running the API

To start the FastAPI server, use the following command:

uvicorn main:app --reload

This will run the server at http://127.0.0.1:8000. You can now interact with the following endpoints.


---

📜 API Endpoints

1. Add Product

POST /add/
Add a new product to the database.
Request:

{
    "name": "Product Name",
    "link": "http://product-link.com",
    "price": "299.99",
    "category": "Electronics"
}

2. Refresh Data

POST /refresh/
Automatically scrape the latest product data and update the database.

3. Update Product

PUT /update/{item_name}
Update the details of a product (name or price).
Request:

{
    "name": "Updated Product Name",
    "price": "249.99"
}

4. Delete Product

DELETE /delete/
Delete a product from the database by its name.
Request:

{
    "item_name": "Product Name"
}

5. Show All Products

GET /show/
Retrieve and display all products in the database.
Response:

[
    {
        "name": "Product Name",
        "link": "http://product-link.com",
        "price": "299.99",
        "category": "Electronics"
    },
    ...
]


---

🧑‍💻 How It Works

1. Web Scraping:
The GetDatas function scrapes product data from a predefined e-commerce website using BeautifulSoup. It collects product information such as name, price, category, and description.


2. Database Interaction:
Using psycopg2, the application connects to a PostgreSQL database to add, update, delete, and display product data.


3. FastAPI Server:
The API is built with FastAPI and served using Uvicorn, providing a fast and modern framework for exposing the data to clients.




---

🤝 Contributing

We welcome contributions! If you'd like to contribute to the project, feel free to submit a pull request. Here’s how you can help:

1. Fork the repository.


2. Create a new branch for your feature.


3. Write tests for your feature.


4. Submit a pull request.






---

💬 Contact

If you have any questions or suggestions, feel free to open an issue on the GitHub repository or reach out to us!


