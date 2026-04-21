from src.models.note import NoteCreate, NoteUpdate, NoteResponse
from src.storage.memory import NoteStorage
from datetime import datetime

class NoteService:
    """Business logic for note operations"""

    def __init__(self, storage: NoteStorage):
        self.storage = storage

    def create_note(self, note:NoteCreate) -> NoteResponse:
        """Create a new note"""
        created_note = self.storage.create(note)
        print(f"[Service] Note created: {created_note.id}")
        return created_note
    
    def get_all_notes(self, skip: int = 0, limit: int = 10, title: str = None) -> list[NoteResponse]:
        """Get notes with filtering and pagination"""
        return self.storage.get_all(skip=skip, limit=limit, title_filter=title)
    
    def get_note_by_id(self, note_id: int) -> NoteResponse:
        """Get a specific note"""
        return self.storage.get_by_id(note_id)
    
    def update_note(self, note_id: int, note: NoteUpdate) -> NoteResponse:
        """Update a note with business logic"""
        updated_note = self.storage.update(note_id, note)
        if updated_note:
            print(f"[Service] Note updated: {note_id}")
        return updated_note
    
    def delete_note(self, note_id: int) -> bool:
        """Delete a note"""
        deleted = self.storage.delete(note_id)
        if deleted:
            print(f"[Service] Note deleted: {note_id}")
        return deleted