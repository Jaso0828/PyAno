from commons import KeysBaseModel
from .keys_type import KeysType

class Piano(KeysBaseModel):
    def __init__(self, name: str, type: KeysType, number_of_keys: int):
        super().__init__(name)
        self.type = type
        self.number_of_keys = number_of_keys

    def __str__(self):
        return f"Piano {self.name}, {self.type}, {self.number_of_keys}"