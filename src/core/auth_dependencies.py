from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from src.utils.security import decode_access_token
from src.repositories.auth_repo import AuthenticationRepository
from src.core.dependencies import get_auth_repository
from src.models.user import User

oauth_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

async def get_current_user(
    token : str = Depends(oauth_scheme),
    auth_repo : AuthenticationRepository = Depends(get_auth_repository)
    )-> User:
    
    payload = decode_access_token(token)

    user_id = payload.get("sub")

    if not user_id:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = "Invalid token"
        )

    user = await auth_repo.get_user_by_id(int(user_id))

    if not user:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = "User not found"
        )
    
    return user
    
