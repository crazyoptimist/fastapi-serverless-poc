import uvicorn
from fastapi import FastAPI
from mangum import Mangum

from greetings.router import router as greetings_router

app = FastAPI()


@app.get("/")
async def healthcheck():
    return {"status": "OK"}


app.include_router(greetings_router, prefix="/api/hello")

# AWS Lambda wrapper
handler = Mangum(app)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
