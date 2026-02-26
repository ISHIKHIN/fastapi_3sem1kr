from fastapi import FastAPI
from fastapi.responses import FileResponse

# задание 1.2
app = FastAPI()

@app.get("/")
async def get_html():
    return FileResponse("index.html")
