# TODO: Agrega el código de las clases del modelo aquí. Borra este comentario al terminar.
import datetime

class Note:

    HIGH = 'High'
    MEDIUM = 'Medium'
    LOW = 'Low'

    def __init__(self, code: str, tittle: str, text: str, importance: int):
        self.code = code
        self.tittle = tittle
        self.text = text
        self.importance = importance
        creation_date = datetime.datetime.now()
        self.tags: list[str] = []

    def add_tag(self, tag: str):
        if tag not in self.tags: # Si el tag creado no esta en la lista tags
            self.tags.append(tag) # Entonces esto permite para no agregar duplicados con el append

    def __str__(self): # Este es Str para devolver un texto que va aparecer.
        return f"Date: {self.creation_date}, {self.tittle} {self.text}"

class Notebook:

    def __init__(self):
        self.notes: list[Note] = []

    # Use chatgpt para comprender como hacer _generate_code

    def _generate_code(self) -> int: # Esto significa que el codigo devuelve un numero entero con el -> int
        existing_codes = {note.code for note in self.notes} # verificar el codigo de cada nota que esta en notas, los cuales se guardan en existing_codes
        code = 1 # Inicia con el codigo 1
        while code in existing_codes: # esto prueba los code que hay, si no existe para poder usarlo
            code += 1 # Crear 1 code que no este en esa lista
        return code

    # El script anterior crea un identificador unico para cada note.

    def add_note(self, title: str, text: str, importance: str):
        code = self._generate_code() # llama el metodo anterior para conseguir un codigo unico
        note = Note(code, title, text, importance) # note crea un Note con la informacion dentro del ()
        self.notes.append(note) # Agrega la nueva nota en la lista notes
        return code

    def delete_note(self, code: int): #################
        self.notes = [note for note in self.notes if note.code != code]  ############

    def important_notes(self) -> list[Note]: #######
        return [note for note in self.notes if note.importance > 0]  ########






