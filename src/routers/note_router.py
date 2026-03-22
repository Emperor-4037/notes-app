from fastapi import APIRouter, HTTPException, Depends
from typing import List

from src.services.note_service import NoteService
from src.schemas.note_schema import NoteCreate, NoteUpdate, NoteResponse
from src.core.dependencies import get_note_service
from src.core.auth_dependencies import get_current_user
from src.models.user import User

router = APIRouter(prefix="/notes", tags=["Notes"])

@router.post("/", response_model=NoteResponse)    
async def create_note(request : NoteCreate, note_service : NoteService = Depends(get_note_service), current_user : User = Depends(get_current_user)):

    note = await note_service.create_note(
        user_id = current_user.id, #type: ignore
        title = request.title,
        content = request.content
    )

    if not note:
        raise HTTPException(status_code=500, detail = "Failed to create note")
    
    return note


@router.get("/", response_model=List[NoteResponse])
async def get_all_notes(note_service : NoteService = Depends(get_note_service), current_user : User = Depends(get_current_user)):

    notes = await note_service.get_all_notes(current_user.id) #type: ignore
    
    return notes


@router.get("/{note_id}", response_model=NoteResponse)
async def get_note_by_id(note_id : int, note_service : NoteService = Depends(get_note_service), current_user : User = Depends(get_current_user)):

    note = await note_service.get_note_by_id(note_id, current_user.id) #type: ignore

    if not note:
        raise HTTPException(status_code=404, detail = "Note not found")
    
    return note


@router.patch("/{note_id}", response_model=NoteResponse)
async def update_note(note_id : int, request : NoteUpdate, current_user : User = Depends(get_current_user), note_service : NoteService = Depends(get_note_service)):

    updated_note = await note_service.update_note(
        note_id = note_id,
        user_id=current_user.id, #type: ignore
        title=request.title,
        content=request.content
    )

    if not updated_note:
        raise HTTPException(status_code=404, detail="Note not updated")
    
    return updated_note


@router.delete("/{note_id}")
async def delete_note(note_id : int, note_service : NoteService = Depends(get_note_service), current_user : User = Depends(get_current_user)):

    sucess = await note_service.delete_note(
        note_id = note_id,
        user_id=current_user.id #type: ignore
    )

    if not sucess:
        raise HTTPException(status_code=404, detail = "Note not deleted")
    
    return {"Message" : "Note deleted successfully"}
    

