from datetime import date
from src.models.note import NoteCreate, NoteUpdate, NoteResponse

class NoteStorage:
    """Stores all notes in memory (simple dictionary)"""
    
    def __init__(self):
        self.notes = {}
        self.next_id = 1
    
    def create(self, note: NoteCreate):
        """Create and store a new note"""
        note_id = self.next_id
        self.next_id += 1
        
        self.notes[note_id] = {
            "id": note_id,
            "title": note.title,
            "content": note.content,
            "created_at": date.today()
        }
        
        return NoteResponse(**self.notes[note_id])
    
    def get_all(self, skip=0, limit=10, title_filter=None):
        """Get all notes with optional filtering and pagination"""
        all_notes = list(self.notes.values())
        
        if title_filter:
            all_notes = [
                note for note in all_notes 
                if title_filter.lower() in note["title"].lower()
            ]
        
        paginated_notes = all_notes[skip : skip + limit]
        
        return [NoteResponse(**note) for note in paginated_notes]
    
    def get_by_id(self, note_id):
        """Get a single note by ID"""
        if note_id in self.notes:
            return NoteResponse(**self.notes[note_id])
        return None
    
    def update(self, note_id, note: NoteUpdate):
        """Update a note (only fields provided)"""
        if note_id not in self.notes:
            return None
        
        if note.title is not None:
            self.notes[note_id]["title"] = note.title
        if note.content is not None:
            self.notes[note_id]["content"] = note.content
        
        return NoteResponse(**self.notes[note_id])
    
    def delete(self, note_id):
        """Delete a note by ID"""
        if note_id in self.notes:
            del self.notes[note_id]
            return True
        return False

storage = NoteStorage()