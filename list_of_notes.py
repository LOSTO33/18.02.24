import pickle
from note import Note
from view import View
import json


class ListOfNotes:
    notes = []
    view = View()
    index = 0
    index_stack = []

    def __init__(self):
        try:
            with open('notes.json', 'r') as file:
                self.notes = json.load(file)
        except (EOFError, FileNotFoundError):
            self.notes = []
            self.view = View()

    def add_note(self):
        note = Note()
        note.set_name(self.view.input_note_name())
        note.set_text(self.view.input_note_text())
        note.update_date()
        self.notes.append(note)
        self.view.info_note_msg('add')

    def delete_note(self, note):
        self.notes.remove(note)
        if len(self.notes) == 0:
            self.index_stack.clear()
        self.view.info_note_msg('del')

    def read_all_notes(self):
        self.view.show_read_all_banner(len(self.notes))
        for note in self.notes:
            self.view.show_note(note)

    def manage_note_by_id(self):
        commands = {
            1: self.view.show_note,
            2: self.view.edit_note,
            3: self.delete_note}
        flag = False
        self.view.show_manage_note_menu()
        choice = self.view.input_number(len(commands.keys()), 'menu')
        value = self.view.input_number(self.index, 'id')
        for note in self.notes:
            if note.get_id() == value:
                commands[choice](note)
                flag = True
        if not flag:
            self.view.not_found()

    def save_notes_to_file(self):
        with open('notes.pkl', 'wb') as file:
            pickle.dump(self.notes, file,
                        protocol=pickle.HIGHEST_PROTOCOL)
        self.view.saved_info()




