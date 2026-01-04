from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()

users_db = {
    1: {
        "name": "person1",
        "user_id": 1,
        "title": "infra engineer",
        "email_address": "person1@xyz.com"
    }
}


class User(BaseModel):
    name: str
    user_id: int
    title: str
    email_address: str

# welcome endpoint
@app.get("/welcome", status_code=status.HTTP_200_OK)
def welcome():
    return {"message": "Welcome to my FastAPI app"}


# get default user
@app.get("/user", response_model=User)
def get_default_user():
    return users_db[1]

# get user by user id
@app.get("/user/{user_id}", response_model=User)
def get_user_by_id(user_id: int):
    if user_id not in users_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} not found"
        )
    return users_db[user_id]


# create user
@app.post("/user", response_model=User, status_code=status.HTTP_201_CREATED)
def create_user(user: User):
    if user.user_id in users_db:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"User with id {user.user_id} already exists"
        )

    users_db[user.user_id] = user.model_dump()
    return user


# update existing user
@app.put("/user/{user_id}", response_model=User)
def update_user(user_id: int, user: User):
    if user_id not in users_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} not found"
        )

    users_db[user_id] = user.model_dump()
    return user


# remove user
@app.delete("/user/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} not found"
        )

    del users_db[user_id]
    return None
