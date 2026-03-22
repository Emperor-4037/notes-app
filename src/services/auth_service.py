from src.repositories.auth_repo import AuthenticationRepository
from src.schemas.auth_schema import UserCreate, UserLogin, TokenResponse
from src.models.user import User
from src.utils.security import hash_password, verify_password, generate_access_token 

class AuthService():
    def __init__(self, auth_repository : AuthenticationRepository):
        self.auth_repository = auth_repository

    async def register_user(self, payload : UserCreate) -> TokenResponse:
        existing = await self.auth_repository.get_user_by_email(payload.email)

        if existing:
            raise ValueError("User already exists")
        
        hashed_password = hash_password(payload.password)

        user = User(
            email = payload.email,
            hashed_password = hashed_password
        ) 

        user = await self.auth_repository.create(user)

        token = generate_access_token(subject=str(user.id))

        return TokenResponse(access_token=token)
    
    async def login_user(self, payload : UserLogin) -> TokenResponse:
       user = await self.auth_repository.get_user_by_email(payload.email)

       if not user or not verify_password(payload.password, user.hashed_password): #type: ignore
           raise ValueError("Invalid Credentials")
       
       token = generate_access_token(subject=str(user.id))
       return TokenResponse(access_token=token)
       