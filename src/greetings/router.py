from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def root():
    return {"message": "Hello from 'greetings' module!"}


@router.get("/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}!"}
