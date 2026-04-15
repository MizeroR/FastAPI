from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from src.models.note import NoteCreate, NoteUpdate, NoteResponse
from src.main import storage

router = APIRouter(prefix="/notes", tags=["notes"])

@router.post("", status_code=201, response_model=NoteResponse)
def create_note(note: NoteCreate):
    """Create a new note"""
    return storage.create(note)

@router.get("", response_model=list[NoteResponse])
def get_all_notes(
    skip: int = Query(0, ge=0, description="Number of notes to skip"),
    limit: int = Query(10, ge=1, le=100, description="Max notes to return"),
    title: Optional[str] = Query(None, description="Filter by title")
):
    """Get all notes with optional pagination and title filter"""
    return storage.get_all(skip=skip, limit=limit, title_filter=title)

@router.get("/{note_id}", response_model=NoteResponse)
def get_note(note_id: int):
    """Get a single note by ID"""
    note = storage.get_by_id(note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note

@router.put("/{note_id}", response_model=NoteResponse)
def update_note(note_id: int, note: NoteUpdate):
    """Update a note"""
    updated = storage.update(note_id, note)
    if not updated:
        raise HTTPException(status_code=404, detail="Note not found")
    return updated

@router.delete("/{note_id}", status_code=204)
def delete_note(note_id: int):
    """Delete a note"""
    deleted = storage.delete(note_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Note not found")