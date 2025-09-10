from pydantic import BaseModel

class Joke(BaseModel):
    joke: str | None = None
    setup: str | None = None
    delivery: str | None = None
