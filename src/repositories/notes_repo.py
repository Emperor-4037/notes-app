from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import Sequence
from src.repositories.base_repo import BaseRepository
from src.models.notes import Note

class NoteRepository(BaseRepository[Note]):
    def __init__(self, session: AsyncSession):
        super().__init__(Note, session)
    
    async def get_notes_by_user(self, user_id: int) -> Sequence[Note]:
        result = await self.session.execute(
            select(Note).where(Note.user_id == user_id)
            )
        return result.scalars().all()


    async def get_note_by_id_and_user(self, note_id : int, user_id : int) -> Note | None:
        result = await self.session.execute(
            select(Note).where(
                Note.id == note_id,
                Note.user_id == user_id
            )
        )
        return result.scalars().first()