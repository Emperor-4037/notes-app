import { type Note } from "../api/notes";
import "./NoteCard.css";

interface NoteCardProps {
  note: Note;
  onEdit: () => void;
  onDelete: () => void;
}

export default function NoteCard({ note, onEdit, onDelete }: NoteCardProps) {
  // Format the date to something readable
  const formattedDate = new Date(note.updated_at).toLocaleDateString("en-US", {
    month: "short",
    day: "numeric",
    year: "numeric",
  });

  return (
    <div className="note-card">
      <div className="note-card-header">
        <h3 className="note-title">{note.title || "Untitled"}</h3>
      </div>
      
      <div className="note-body">
        <p className="note-content">
          {note.content || <span className="text-muted">No content</span>}
        </p>
      </div>
      
      <div className="note-footer">
        <span className="note-date">{formattedDate}</span>
        <div className="note-actions">
          <button 
            onClick={onEdit} 
            className="btn-icon" 
            title="Edit note"
            aria-label="Edit note"
          >
            ✏️
          </button>
          <button 
            onClick={onDelete} 
            className="btn-icon btn-icon-danger" 
            title="Delete note"
            aria-label="Delete note"
          >
            🗑️
          </button>
        </div>
      </div>
    </div>
  );
}
