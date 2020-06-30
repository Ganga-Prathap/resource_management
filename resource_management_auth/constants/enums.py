import enum

from ib_common.constants import BaseEnumClass


class AccessLevelEnum(BaseEnumClass, enum.Enum):
    READ = 'READ'
    WRITE = 'WRITE'
    ADMIN = 'ADMIN'
    COMMENTONLY = 'COMMENT-ONLY'


class GenderEnum(BaseEnumClass, enum.Enum):
    MALE = 'MALE'
    FEMALE = 'FEMALE'

class StatusLevelEnum(BaseEnumClass, enum.Enum):
    PENDING = 'PENDING'
    ACCEPT = 'ACCEPT'
    REJECT = 'REJECT'
