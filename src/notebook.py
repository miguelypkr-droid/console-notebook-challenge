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
        if tag not in self.tags: # Si tag no esta en tags
            self.tags.append(tag) # Entonces esto permite para no agregar duplicados con el append

    def __str__(self):
        return f"Date: {self.creation_date}, {self.tittle} {self.text}"


