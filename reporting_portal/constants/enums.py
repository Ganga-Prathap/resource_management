import enum
from ib_common.constants import BaseEnumClass

class RoleEnum(BaseEnumClass, enum.Enum):
    ADMIN = 'Admin'
    USER = 'User'
    RP = 'Rp'


