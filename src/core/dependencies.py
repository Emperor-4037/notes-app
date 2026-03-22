from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.database.session import get_db
from src.repositories.notes_repo import NoteRepository
from src.services.note_service import NoteService
from src.repositories.auth_repo import AuthenticationRepository
from src.services.auth_service import AuthService


def get_note_repository(db : AsyncSession = Depends(get_db)) -> NoteRepository:
    return NoteRepository(db)

def get_note_service(note_repository : NoteRepository = Depends(get_note_repository)) -> NoteService:
    return NoteService(note_repository)

def get_auth_repository(db : AsyncSession = Depends(get_db)) -> AuthenticationRepository:
    return AuthenticationRepository(db)

def get_auth_service(auth_repository : AuthenticationRepository = Depends(get_auth_repository)) -> AuthService:
    return AuthService(auth_repository)
