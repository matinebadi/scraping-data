import psycopg2

connected = psycopg2.connect(user='postgres', password=3413, host="localhost", port=5432, database="etlphone")
cun = connected.cursor()

def Add(name, link, price, catagory):
    cun.execute(f"INSERT INTO users(name, link, price, catagory)\nVALUES('{name}', '{link}', '{price}', '{catagory}');")
    connected.commit()

def Update(name, obj, newobj):
    cun.execute(f"UPDATE users SET {obj}='{newobj}' WHERE name='{name}' ")
    connected.commit()

def Delete(name):
    cun.execute(f"DELETE FROM users WHERE name='{name}'")
    connected.commit()

def Show():
    cun.execute(f"SELECT * FROM users ")
    res = cun.fetchall()
    Total = []
    for i in res:
        Total.append({
            'name': i[0],
            'link': i[1],
            'price': i[2],
            'category': i[3]
        })
    return Total