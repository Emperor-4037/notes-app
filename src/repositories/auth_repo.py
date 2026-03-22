from src.repositories.base_repo import BaseRepository
from sqlalchemy import select

from sqlalchemy.ext.asyncio import AsyncSession
from src.models.user import User

class AuthenticationRepository(BaseRepository[User]):

    def __init__(self, session : AsyncSession):
        super().__init__(User, session)
    
    async def get_user_by_email(self, email : str) -> User | None:
        result = await self.session.execute(
            select(self.model).where(self.model.email == email)
        )
        return result.scalar_one_or_none()
    
    async def get_user_by_id(self, user_id : int) -> User | None:

        result = await self.session.execute(
            select(self.model).where(self.model.id == user_id)        
            )
        
        return result.scalar_one_or_none()
