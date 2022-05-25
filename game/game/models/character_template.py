from dataclasses import dataclass, field

import common
from common.dataclass import BaseDataclass
from common.document import Document


@dataclass(kw_only=True)
class CharacterTemplate(Document):
    @classmethod
    def from_static_template(cls, template, sex):
        pass
