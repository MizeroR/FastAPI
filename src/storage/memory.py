from dataclasses import dataclass
from datetime import date
from src.models.note import NoteCreate, NoteUpdate, NoteResponse

@dataclass
class Note:
    """Internal Note data model"""
    id: int
    title: str
    content: str
    created_at: date

class NoteStorage:
    """Stores all notes in memory using a list"""
    
    def __init__(self):
        self.notes: list[Note] = []
        self.next_id = 1
    
    def create(self, note: NoteCreate):
        """Create and store a new note"""
        new_note = Note(
            id=self.next_id,
            title=note.title,
            content=note.content,
            created_at=date.today()
        )
        self.notes.append(new_note)
        self.next_id += 1
        return NoteResponse(**vars(new_note))
    
    def get_all(self, skip=0, limit=10, title_filter=None):
        """Get all notes with optional filtering and pagination"""
        all_notes = self.notes
        
        if title_filter:
            all_notes = [
                note for note in all_notes 
                if title_filter.lower() in note.title.lower()
            ]
        
        paginated_notes = all_notes[skip : skip + limit]
        return [NoteResponse(**vars(note)) for note in paginated_notes]
    
    def get_by_id(self, note_id):
        """Get a single note by ID"""
        for note in self.notes:
            if note.id == note_id:
                return NoteResponse(**vars(note))
        return None
    
    def update(self, note_id, note: NoteUpdate):
        """Update a note (only fields provided)"""
        for existing_note in self.notes:
            if existing_note.id == note_id:
                if note.title is not None:
                    existing_note.title = note.title
                if note.content is not None:
                    existing_note.content = note.content
                return NoteResponse(**vars(existing_note))
        return None
    
    def delete(self, note_id):
        """Delete a note by ID"""
        for i, note in enumerate(self.notes):
            if note.id == note_id:
                self.notes.pop(i)
                return True
        return False


# Global instance for import
storage = NoteStorage()