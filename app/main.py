from fastapi import FastAPI
from app import services
from app.schema import UserIn, BaseResponse, UserListOut

app = FastAPI()


@app.get("/")
async def index():
    """
    Index route for our application
    """
    return {"message": "Hello from FastAPI ;)"}


@app.post("/users", response_model=BaseResponse)
async def user_create(user: UserIn):
    """
    Add user data to users.json file
    """
    try:
        services.add_userdata(user.dict())
    except Exception:
        return {"success": False}
    return {"success": True}


@app.get("/users", response_model=UserListOut)
async def get_users():
    """
    Read user data from users.json file
    """
    return services.read_usersdata()
