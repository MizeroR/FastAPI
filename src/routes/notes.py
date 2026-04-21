import asyncio
from fastapi import APIRouter, HTTPException, Query, BackgroundTasks
from typing import Optional
from src.models.note import NoteCreate, NoteUpdate, NoteResponse
from src.storage.memory import storage
from src.services.note_service import NoteService

# Initialize service with shared storage
note_service = NoteService(storage)

router = APIRouter(prefix="/notes", tags=["notes"])

@router.post("", status_code=201, response_model=NoteResponse)
def create_note(note: NoteCreate, background_tasks: BackgroundTasks):
    """Create a new note (sync)"""
    created = note_service.create_note(note)
    background_tasks.add_task(log_note_creation, created.id)
    return created

@router.get("", response_model=list[NoteResponse])
async def get_all_notes(
    skip: int = Query(0, ge=0, description="Number of notes to skip"),
    limit: int = Query(10, ge=1, le=100, description="Max notes to return"),
    title: Optional[str] = Query(None, description="Filter by title")
):
    """Get all notes with optional pagination and title filter (ASYNC)"""
    await asyncio.sleep(0.1)
    return note_service.get_all_notes(skip=skip, limit=limit, title=title)

@router.get("/{note_id}", response_model=NoteResponse)
def get_note(note_id: int):
    """Get a single note by ID"""
    note = note_service.get_note_by_id(note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note

@router.put("/{note_id}", response_model=NoteResponse)
async def update_note(note_id: int, note: NoteUpdate, background_tasks: BackgroundTasks):
    """Update a note (ASYNC)"""
    await asyncio.sleep(0.1)
    updated = note_service.update_note(note_id, note)
    if not updated:
        raise HTTPException(status_code=404, detail="Note not found")
    
    background_tasks.add_task(log_note_update, note_id)

    return updated

@router.delete("/{note_id}", status_code=204)
def delete_note(note_id: int, background_tasks: BackgroundTasks):
    """Delete a note"""
    deleted = note_service.delete_note(note_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Note not found")
    
    background_tasks.add_task(log_note_deletion, note_id)

async def log_note_creation(note_id: int):
    """Log note creation"""
    await asyncio.sleep(0.1)
    print(f"[Background] Note {note_id} created logged")

async def log_note_update(note_id: int):
    """Log note update"""
    await asyncio.sleep(0.1)
    print(f"[Background] Note {note_id} update logged")

async def log_note_deletion(note_id: int):
    """Log note deletion"""
    await asyncio.sleep(0.1)
    print(f"[Background] Note {note_id} deletion logged")