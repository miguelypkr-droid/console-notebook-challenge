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