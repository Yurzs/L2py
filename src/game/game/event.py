from dataclasses import dataclass

from common import BaseDataclass


@dataclass(kw_only=True)
class ServerEvent(BaseDataclass):
    pass
