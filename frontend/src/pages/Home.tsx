import { useState, useEffect, useCallback } from "react";
import { notesApi, type Note, type NoteCreate } from "../api/notes";
import { useAuth } from "../context/AuthContext";
import NoteCard from "../components/NoteCard";
import NoteModal from "../components/NoteModal";
import Navbar from "../components/Navbar";
import "./Home.css";

export default function Home() {
  const { user } = useAuth();
  const [notes, setNotes] = useState<Note[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const [modalOpen, setModalOpen] = useState(false);
  const [editingNote, setEditingNote] = useState<Note | null>(null);

  const fetchNotes = useCallback(async () => {
    try {
      setError("");
      const data = await notesApi.getAll();
      setNotes(data);
    } catch {
      setError("Failed to load notes. Please try again.");
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    fetchNotes();
  }, [fetchNotes]);

  const handleCreate = async (payload: NoteCreate) => {
    const newNote = await notesApi.create(payload);
    setNotes((prev) => [newNote, ...prev]);
    setModalOpen(false);
  };

  const handleUpdate = async (payload: NoteCreate) => {
    if (!editingNote) return;
    const updated = await notesApi.update(editingNote.id, payload);
    setNotes((prev) =>
      prev.map((n) => (n.id === updated.id ? updated : n))
    );
    setEditingNote(null);
    setModalOpen(false);
  };

  const handleDelete = async (id: number) => {
    await notesApi.delete(id);
    setNotes((prev) => prev.filter((n) => n.id !== id));
  };

  const openEdit = (note: Note) => {
    setEditingNote(note);
    setModalOpen(true);
  };

  const openCreate = () => {
    setEditingNote(null);
    setModalOpen(true);
  };

  const closeModal = () => {
    setModalOpen(false);
    setEditingNote(null);
  };

  return (
    <div className="home-layout">
      <Navbar />
      <main className="home-main">
        <div className="home-header">
          <div>
            <h1>Your Notes</h1>
            <p className="home-subtitle">
              {user?.email ? `Logged in as ${user.email}` : "Manage your notes"}
            </p>
          </div>
          <button className="btn-primary btn-create" onClick={openCreate}>
            <span>＋</span> New Note
          </button>
        </div>

        {error && <div className="home-error">{error}</div>}

        {loading ? (
          <div className="home-loader">
            <span className="spinner spinner-lg" />
          </div>
        ) : notes.length === 0 ? (
          <div className="home-empty">
            <div className="empty-icon">📄</div>
            <h2>No notes yet</h2>
            <p>Click "New Note" to create your first one!</p>
          </div>
        ) : (
          <div className="notes-grid">
            {notes.map((note) => (
              <NoteCard
                key={note.id}
                note={note}
                onEdit={() => openEdit(note)}
                onDelete={() => handleDelete(note.id)}
              />
            ))}
          </div>
        )}
      </main>

      {modalOpen && (
        <NoteModal
          note={editingNote}
          onSubmit={editingNote ? handleUpdate : handleCreate}
          onClose={closeModal}
        />
      )}
    </div>
  );
}
