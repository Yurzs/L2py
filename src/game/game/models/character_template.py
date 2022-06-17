from dataclasses import dataclass, field

import src.common
from src.common.common.dataclass import BaseDataclass
from src.common.common.document import Document


@dataclass(kw_only=True)
class CharacterTemplate(Document):
    @classmethod
    def from_static_template(cls, template, sex):
        pass
