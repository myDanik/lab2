from fastapi import FastAPI
import wikipedia
from pydantic import BaseModel
app = FastAPI(title='wikipedia')
@app.get('/{argument}')
def path(argument: str):
    return wikipedia.search(argument)
@app.get('/')
def query(argument, res: int):
    return path(argument)[res-1]
class Sen(BaseModel):
    estimation: int

@app.post('/{argument}/')
def body(estimation: Sen, argument: str, res: int):
    return wikipedia.search(argument)[res-1]+' '+str(estimation)
