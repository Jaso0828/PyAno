from commons import KeysBaseModel
from .keys_type import KeysType


class Synth(KeysBaseModel):
    def __init__(self, name, synth_type: KeysType):
        super().__init__(name)
        self.synth_type = synth_type
        