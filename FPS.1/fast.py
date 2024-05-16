import uvicorn
from fastapi import FastAPI
from scrap import GetDatas
from postgres import Add, Update, Delete, Show

app = FastAPI()

@app.post("/add/")
async def creat_item(name , link, price, category):
    Add(name, link, price, category)

@app.post("/refresh/")
async def creat_item():
    datas = GetDatas()
    for data in datas:
        Add(data['name'], data['link'], data['price'], data['category'])


@app.put("/update/{item_name}")
async def update_item(item_name, name: str, price):
        Update(item_name, name, price)


@app.delete("/delete/")
async def delete_item(item_name):
    Delete(item_name)
    return ("massage : deleted :( ")



@app.get("/show/")
async def show_item():
    return {f"response": Show()}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)