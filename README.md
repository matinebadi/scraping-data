

🛠️ ETL Phone Product Scraper & Database API 📱

🚀
This project is a Python-based web scraper and API service designed to extract product details from an e-commerce website and manage them through a PostgreSQL database. The backend is powered by FastAPI, while the scraping magic is done using BeautifulSoup and requests. The database interaction is handled seamlessly with psycopg2. 🔥

🛠️ Features:

Add Product: Insert new products into the database easily.

Refresh Data: Automatically update the product data by scraping the latest information.

Update Product: Modify product details directly in the database.

Delete Product: Remove unwanted products from the database.

Show All Products: Display all products currently stored in the database.


🚀 Getting Started

1️⃣ Clone the repository:

git clone https://github.com/your-username/etl-phone-scraper.git
cd etl-phone-scraper

2️⃣ Install Dependencies:

pip install -r requirements.txt

3️⃣ Set Up PostgreSQL:

Create a PostgreSQL database named etlphone.

Ensure the users table is present with the following columns:

name

link

price

category



4️⃣ Configure Database Connection:

Make sure your connection details in the script are correct:

connected = psycopg2.connect(user='postgres', password='yourpassword', host="localhost", port=5432, database="etlphone")

🏃‍♂️ Running the API:

Start the FastAPI server with:

uvicorn main:app --reload

The API will be available at http://127.0.0.1:8000.


---

🌍 API Endpoints

1️⃣ Add Product

POST /add/
Adds a new product to the database.
Request Body:

{
    "name": "Product Name",
    "link": "http://product-link.com",
    "price": "299.99",
    "category": "Electronics"
}

2️⃣ Refresh Data

POST /refresh/
Fetches the latest product information from the web and inserts it into the database.

3️⃣ Update Product

PUT /update/{item_name}
Updates an existing product’s details.
Request Body:

{
    "name": "Updated Product Name",
    "price": "249.99"
}

4️⃣ Delete Product

DELETE /delete/
Deletes a product from the database by its name.
Request Body:

{
    "item_name": "Product Name"
}

5️⃣ Show All Products

GET /show/
Returns a list of all products stored in the database.


---

🧑‍💻 How It Works:

1. Scraping with BeautifulSoup:
The GetDatas function uses BeautifulSoup to scrape product details like name, price, category, discount, and availability from a predefined website. 📈


2. Database Interaction:
The product data is stored in a PostgreSQL database using psycopg2 for database operations such as adding, updating, deleting, and retrieving products. 🗄️


3. FastAPI:
The web server is powered by FastAPI, which makes it fast and easy to interact with the data through a set of well-defined endpoints. 🚀


4. Uvicorn:
The server runs with Uvicorn, providing a high-performance web server for FastAPI applications. ⚡




---

✨ Contributing:

We welcome contributions! If you’d like to improve this project, fork the repository, make your changes, and submit a pull request. 💡


---

📄 License:

This project is licensed under the MIT License.




