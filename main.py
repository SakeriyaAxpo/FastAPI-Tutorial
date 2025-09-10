from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl
import json

app = FastAPI()

class jokesClass(BaseModel):
    joke: str | None = None
    setup: str | None = None
    delivery: str | None = None


dog_facts = {
  "dog_facts": [
    {
      "fact": "Dogs have an extraordinary sense of smell, up to 100,000 times more sensitive than humans."
    },
    {
      "fact": "The Basenji is known as the 'barkless dog' because it makes a unique yodel-like sound instead of barking."
    },
    {
      "fact": "A dog’s nose print is unique, much like a human fingerprint."
    },
    {
      "fact": "The Greyhound is the fastest dog breed, capable of reaching speeds up to 45 miles per hour (72 km/h)."
    },
    {
      "fact": "Dogs can understand up to 250 words and gestures."
    },
    {
      "fact": "Puppies are born blind, deaf, and toothless."
    },
    {
      "fact": "The Labrador Retriever has been the most popular dog breed in the United States for decades."
    },
    {
      "fact": "Dogs curl up in a ball when sleeping to protect their organs, a habit from their wild ancestors."
    },
    {
      "fact": "A dog’s sense of hearing is more than four times better than that of humans."
    },
    {
      "fact": "Some dogs can detect medical conditions such as low blood sugar, seizures, or even certain types of cancer."
    }
  ]
}

jokes_object =    {
        "jokes" : 
        [
            {   
                "id" : 1,
                "joke" : "ASCII silly question, get a silly ANSI."
            },
            {   
                "id": 2,
                "joke":  """"Two SQL tables sit at the bar. A query approaches and asks \"Can I join you?\""""
            },
            {   
                "id": 3,
                "joke" : "Java is like Alzheimer's, it starts off slow, but eventually, your memory is gone."
            },
            {
                "id": 4,
                "setup" : "Why did the programmer jump on the table?",
                "delivery" : "Because debug was on his screen."
            },
        ]
    }

# jokes = {
#     1: "ASCII silly question, get a silly ANSI.",
#     2: """ "Two SQL tables sit at the bar. A query approaches and asks \"Can I join you?\"""",
#     3: "Java is like Alzheimer's, it starts off slow, but eventually, your memory is gone.",
#     4: ["Why did the programmer jump on the table?", "Because debug was on his screen."]
# }

# jokes
# print({jokes_object["jokes"][0]["joke"]})
# return all jokes
@app.get("/jokes/")
async def get_all_jokes():
    return jokes_object
#Muss noch gefixt werden
#Return specifif joke
@app.get("/jokes/{id}")
async def get_joke(id: int):
    jokes_list = jokes_object["jokes"]
    for joke in jokes_list:
        if joke["id"] == id:
            if joke["setup"]:
                return{"Setup" : joke["setup"], "Delivery": joke["delivery"]}
            if joke["joke"] :
                return{"Joke": joke["joke"]}      
# post joke 
@app.post("/joke/")
async def post_joke(id:int, jokes: jokesClass):
    jokes_dict = jokes.dict()
    jokes_dict.update({"id": id})
    return jokes_dict

#update code
@app.put("/jokes/{id}")
async def update_joke(id: int, jokes: jokesClass):
    return jokes

#delete code
@app.delete("/jokes/{id}")
async def delete_joke(id: int):
    jokes_list = jokes_object["jokes"]
    for joke in jokes_list: 
        if joke["id"] == id:
            joke.pop()
        return{"Deletion successful": jokes_object}