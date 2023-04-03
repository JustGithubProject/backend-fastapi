from typing import List
from fastapi import APIRouter, Depends, HTTPException, status

from models.user import User, UserIn
from repositories.users import UserRepository
from endpoints.depends import get_user_repository, get_current_user

router = APIRouter()


@router.get("/", response_model=List[User])
async def read_users(
        users: UserRepository = Depends(get_user_repository),
        limit: int = 100,
        skip: int = 100
):
    return await users.get_all(limit=limit, skip=skip)


@router.post("/", response_model=User)
async def create_user(user: UserIn, users: UserRepository = Depends(get_user_repository)):
    return await users.create(u=user)


@router.put("/", response_model=User)
async def update_user(
        id: int,
        user: UserIn,
        users: UserRepository = Depends(get_user_repository),
        current_user: User = Depends(get_current_user)
):
    old_user = await users.get_by_email(id=id)
    if not old_user or old_user.email != current_user.email:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found user")
    return await users.update(id_=id, u=user)
