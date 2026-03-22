from typing import Sequence
from src.repositories.notes_repo import NoteRepository
from src.models.notes import Note

class NoteService:

    def __init__(self, note_repository : NoteRepository):
        self.note_repository = note_repository


    async def create_note(self, user_id : int, title : str, content : str) -> Note:
        if not title:
            raise ValueError("Title can't be empty")
        
        if not content:
            raise ValueError("Content can't be empty")
        
        note = Note(
            user_id = user_id,
            title = title,
            content = content
        )
        return await self.note_repository.create(note)
    
    
    async def get_all_notes(self, user_id : int) -> Sequence[Note]:
        if user_id <= 0:
            raise ValueError("User should exist")
        
        return await self.note_repository.get_notes_by_user(user_id)
    
    
    async def get_note_by_id(self, note_id : int, user_id : int) -> Note | None:
        if user_id <= 0:
            raise ValueError("User should exist")
        
        if note_id <= 0:
            raise ValueError("Note_id should be present")
        
        return await self.note_repository.get_note_by_id_and_user(note_id, user_id)
    
    
    async def update_note(self, note_id : int, user_id : int, title : str | None = None, content : str | None = None):
        
        if user_id <= 0:
            raise ValueError("User should exist")
        
        if note_id <= 0:
            raise ValueError("Note_id should be present")

        note = await self.note_repository.get_note_by_id_and_user(note_id, user_id)

        if not note:
            raise ValueError("Note not found")
        
        updated_note = {}

        if title is not None:
            if not title:
                raise ValueError("Title can't be empty")

            updated_note["title"] = title

        if content is not None:
            if not content:
                raise ValueError("Content can't be empty")

            updated_note["content"] = content
        
        if not updated_note:
            raise ValueError("No data provided to update")

        return await self.note_repository.update(note, updated_note)
    
    
    async def delete_note(self, note_id : int, user_id : int) -> bool:

        if user_id <= 0:
            raise ValueError("User should exist")
        
        if note_id <= 0:
            raise ValueError("Note_id should be present")

        note = await self.note_repository.get_note_by_id_and_user(note_id, user_id)

        if not note:
            raise ValueError("Note not found")

        sucess = await self.note_repository.delete(note)   
        return sucess



