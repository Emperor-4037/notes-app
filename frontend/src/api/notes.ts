import apiClient from "./client";

export interface Note {
  id: number;
  title: string;
  content: string;
  collection_id?: number | null;
  created_at: string;
  updated_at: string;
  [key: string]: unknown; // Allow extra fields for forward-compatibility
}

export interface NoteCreate {
  title: string;
  content: string;
  collection_id?: number | null;
}

export interface NoteUpdate {
  title?: string;
  content?: string;
  collection_id?: number | null;
}

export const notesApi = {
  getAll: async (): Promise<Note[]> => {
    const { data } = await apiClient.get<Note[]>("/notes");
    return data;
  },

  getById: async (id: number): Promise<Note> => {
    const { data } = await apiClient.get<Note>(`/notes/${id}`);
    return data;
  },

  create: async (payload: NoteCreate): Promise<Note> => {
    const { data } = await apiClient.post<Note>("/notes", payload);
    return data;
  },

  update: async (id: number, payload: NoteUpdate): Promise<Note> => {
    const { data } = await apiClient.patch<Note>(`/notes/${id}`, payload);
    return data;
  },

  delete: async (id: number): Promise<void> => {
    await apiClient.delete(`/notes/${id}`);
  },
};
