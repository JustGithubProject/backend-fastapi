from fastapi import APIRouter, Depends, HTTPException, status

from endpoints.depends import get_user_repository
from models.token import Token, Login
from repositories.users import UserRepository
from core.security import verify_password, create_access_token

router = APIRouter()


@router.post("/", response_model=Token)
async def login(login_u: Login, users: UserRepository = Depends(get_user_repository)):
    user = await users.get_by_email(login_u.email)
    if not user or not verify_password(login_u.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    return Token(
        access_token=create_access_token({"sub": user.email}),
        token_type="Bearer"
    )
