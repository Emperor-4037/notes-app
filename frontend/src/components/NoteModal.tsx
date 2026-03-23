import { useState, useEffect, type FormEvent } from "react";
import { type Note, type NoteCreate } from "../api/notes";
import "./NoteModal.css";

interface NoteModalProps {
  note: Note | null; // null means create mode
  onSubmit: (payload: NoteCreate) => Promise<void>;
  onClose: () => void;
}

export default function NoteModal({ note, onSubmit, onClose }: NoteModalProps) {
  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    if (note) {
      setTitle(note.title);
      setContent(note.content);
    }
  }, [note]);

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();
    setLoading(true);
    try {
      await onSubmit({ title, content });
    } catch {
      // Errors handled by parent or could add local error state
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="modal-overlay" onClick={onClose} role="dialog" aria-modal="true">
      <div 
        className="modal-content" 
        onClick={(e) => e.stopPropagation()}
        role="document"
      >
        <div className="modal-header">
          <h2>{note ? "Edit Note" : "New Note"}</h2>
          <button className="btn-close" onClick={onClose} aria-label="Close modal">×</button>
        </div>

        <form onSubmit={handleSubmit} className="modal-form">
          <div className="form-group">
            <input
              type="text"
              placeholder="Note Title"
              value={title}
              onChange={(e) => setTitle(e.target.value)}
              required
              autoFocus
              className="modal-input-title"
            />
          </div>
          <div className="form-group flex-grow">
            <textarea
              placeholder="Write your note here..."
              value={content}
              onChange={(e) => setContent(e.target.value)}
              required
              className="modal-textarea"
            />
          </div>
          <div className="modal-actions">
            <button type="button" className="btn-secondary" onClick={onClose} disabled={loading}>
              Cancel
            </button>
            <button type="submit" className="btn-primary" disabled={loading}>
              {loading ? <span className="spinner" /> : (note ? "Save Changes" : "Create Note")}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}
