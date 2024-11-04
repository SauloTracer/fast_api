from fast_zero.schemas import (
    Message,
    UserDB,
    UserList,
    UserPublicSchema,
    UserSchema,
)
from fastapi import FastAPI, HTTPException
from http import HTTPStatus

app = FastAPI()
database = {"users": []}


@app.get("/", status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    """API entry point"""
    return {"message": "Hello -=FastApi"}


@app.post(
    "/users", status_code=HTTPStatus.CREATED, response_model=UserPublicSchema
)
def create_user(user: UserSchema):
    createdUser = UserDB(id=len(database["users"]) + 1, **user.model_dump())

    database["users"].append(createdUser)

    return createdUser


@app.get("/users", status_code=HTTPStatus.OK, response_model=UserList)
def get_users():
    # return [UserPublicSchema(**user.model_dump())
    # for user in database["users"]]
    return {"users": database["users"]}


@app.put("/users/{user_id}", response_model=UserPublicSchema)
def update_user(user_id: int, user: UserSchema):
    if user_id > len(database["users"]) or user_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail="User not found"
        )

    user_with_id = UserDB(id=user_id, **user.model_dump())
    database["users"][int(user_id) - 1] = user_with_id
    return database["users"][int(user_id) - 1]


@app.delete("/users/{user_id}", response_model=Message)
def delete_user(user_id: int):
    if user_id > len(database["users"]) or user_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail="User not found"
        )

    del database["users"][user_id - 1]

    return {"message": f"User with id {user_id} deleted"}
