import typing

from common.ctype import ctype
from common.session import Session
from login.config import DEBUG
from login.keys.blowfish import BlowfishKey
from login.keys.rsa import L2RsaKey
from login.keys.session import SessionKey
from login.keys.xor import LoginXorKey
from login.protocol import Lineage2LoginProtocol
from login.state import State


class LoginSession(Session):
    def __init__(self, protocol):
        super().__init__()

        self.protocol: Lineage2LoginProtocol = protocol
        self.state: typing.Type[State, None] = None

        if DEBUG:
            self.id: ctype.int = 1
            self.state: typing.Type[State, None] = None
            self.rsa_key: L2RsaKey = L2RsaKey(
                n=114864864492067965740896094499845788661704547603461946041788430244130842942327562108037881765257637001470002088493469466590330012894850351298499234054400902909094648545037681203002379437662692263023086237588859126444600832405209700229179654815477929362986913374184282884226518004040399737373993652540837590413,
                e=65537,
                d=24101430761959650485901054663640453504650268706716909310880009023827826327275918770132229452439066188816460415023510719173143042705957106570234945027855716930584593038616254904391656876797375966251389087225009936033550634664544981501673315139777365280685902473060207377829297089665705686626339175100783535953,
                p=9916011190118260834420732077691009653459567295520159291150209477378355320775407287143204582642394937713625198095479788156570194891697637999460965480152817,
                q=11583777215432736777867145057369984035716447897863364266554340327857721534451397646420941640550969480924837472920543549449999218012096863136050055128324189,
                u=8749384252980206798590996271998110590139167440335051391024304811619350675706554671938061284513578306506720862764773635685258662045283301164468169301716502,
            )
            self.blowfish_key: BlowfishKey = BlowfishKey(
                b']\xc7\x9c\xf33\x82PN\xe9]\x1f\x05"y\xdf\xad'
            )
            self.session_key: SessionKey = SessionKey(
                **{
                    "login_ok1": 1777271179,
                    "login_ok2": 250194844,
                    "play_ok1": 1632717010,
                    "play_ok2": 930316699,
                }
            )
            self.xor_key: LoginXorKey = LoginXorKey(1882434664)
        else:
            self.id: ctype.int32 = ctype.int32.random()
            self.rsa_key: L2RsaKey = L2RsaKey.generate()
            self.blowfish_key: BlowfishKey = BlowfishKey()
            self.session_key: SessionKey = SessionKey()
            self.xor_key: LoginXorKey = LoginXorKey()

        self.protocol_version: ctype.int = 50721
        self.blowfish_enabled: ctype.bool = False
        self.account = None

    @classmethod
    def by_username(cls, username):
        for session_id, session in cls.data().items():
            if session["account"].username == username:
                return {session_id: session}
