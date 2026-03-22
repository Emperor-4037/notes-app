from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from src.services.auth_service import AuthService
from src.core.dependencies import get_auth_service
from src.core.auth_dependencies import get_current_user

from src.schemas.auth_schema import UserCreate, UserLogin, UserResponse, TokenResponse

router = APIRouter(prefix="/auth", tags = ["Auth"])

@router.post("/register", response_model=TokenResponse)
async def register(
    payload : UserCreate, auth_service : AuthService = Depends(get_auth_service)
):
    return await auth_service.register_user(payload)

@router.post("/login", response_model=TokenResponse)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), auth_service : AuthService = Depends(get_auth_service)):
    payload = UserLogin(email=form_data.username, password=form_data.password)
    return await auth_service.login_user(payload)

@router.get("/me", response_model=UserResponse)
async def get_user(curr_user : UserResponse = Depends(get_current_user)):
    return curr_user