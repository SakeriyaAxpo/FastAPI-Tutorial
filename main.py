from fastapi import FastAPI
from repository import dog_facts, jokes_object
from models.joke import Joke

app = FastAPI()


@app.get("/jokes/")
async def get_all_jokes():
    return jokes_object


@app.get("/jokes/{joke_id}")
async def get_joke(joke_id: int) -> dict[str, str]:
    #TODO: Muss noch gefixt werden
    # Return specifif joke

    jokes_list = jokes_object["jokes"]

    for joke in jokes_list:
        if joke["id"] == joke_id:
            if joke.get("setup"):
                return{"Setup" : joke["setup"], "Delivery": joke["delivery"]}
            if joke.get("joke") :
                return{"Joke": joke["joke"]}      

    return{"Error": "Joke not found"}

def get_new_id() -> int:
    all_jokes = jokes_object["jokes"]

    highest_id = 0
    for joke in all_jokes:
        if joke["id"] > highest_id:
            highest_id = joke["id"]

    return highest_id + 1



# post joke
@app.post("/joke/")
async def post_joke(new_joke: Joke):

    new_id = get_new_id()

    all_jokes = jokes_object["jokes"]

    joke_to_add = {
        "id": new_id,
        "joke": new_joke.joke,
        "setup": new_joke.setup,
        "delivery": new_joke.delivery,
    }

    all_jokes.append(joke_to_add) ## might not work because we dont have a database

    return joke_to_add

#update code
@app.put("/jokes/{id}")
async def update_joke(id: int, jokes: Joke):
    return jokes

#delete code
@app.delete("/jokes/{id}")
async def delete_joke(id: int):
    jokes_list = jokes_object["jokes"]
    for joke in jokes_list: 
        if joke["id"] == id:
            joke.pop()
        return{"Deletion successful": jokes_object}