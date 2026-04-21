from datetime import datetime
import time
import asyncio

async def log_note_creatin(note_id: int):
    """Background task: log note creatin (simulated)"""
    await asyncio.sleep(0.1)
    print(f"[Background] Note {note_id} created at {datetime.now()}")

async def cleanup_old_notes():
    """Background task: cleanup old notes (simulated)"""
    await asyncio.sleep(0.5)
    print(f"[Background] Cleanup completed at {datetime.now()}")