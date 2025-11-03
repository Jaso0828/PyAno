from .piano_categories import PianoCategories
from .piano_types import PianoType


class Piano:
    def __init__(self, category: PianoCategories, type: PianoType, name, description = ''):
        self.category = category
        self.type = type
        self.name = name
        self.description = description
        self.id = 1


    def __repr__(self):
        return(f'Piano {self.category}, {self.type}, {self.name}, {self.description}')
