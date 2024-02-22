import sqlite3
from dataclasses import dataclass


class Database:
    def __init__(self, dados):
        self.dados = dados 
        self.conn = sqlite3.connect(dados+".db")
        self.constroiTabela()

    def constroiTabela(self):
        self.conn.execute('''CREATE TABLE IF NOT EXISTS note ( id INTEGER PRIMARY KEY,
                                                               title TEXT,
                                                               content TEXT NOT NULL);''')
    def add(self, note):
        title_ = note.title
        content_ = note.content
        self.conn.execute('''INSERT INTO note (title, content) VALUES (?, ?)''', (title_, content_))
        self.conn.commit()

    def get_all(self):
        cursor = self.conn.execute("SELECT id, title, content FROM note")
        lista_note = []
        for linha in cursor:
            id_ = linha[0]
            title_ = linha[1]
            content_ = linha[2]
            note_ = Note(id=id_, title=title_, content=content_)
            lista_note.append(note_)
        return lista_note
    
    def update(self, entry):
        id_ = entry.id
        title_ = entry.title
        content_ = entry.content
        self.conn.execute('''UPDATE note SET title = ?, content = ? WHERE id = ?''', (title_, content_, id_))
        self.conn.commit()

    def delete(self, note_id):
        self.conn.execute('''DELETE FROM note WHERE id = ?''', (note_id,))
        self.conn.commit()
        


@dataclass
class Note:
    id: int = None
    title: str = None
    content: str = ''