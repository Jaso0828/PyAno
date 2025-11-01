from commons import KeysBaseModel

class KeysType(KeysBaseModel):
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f"Keys type '{self.name}'"