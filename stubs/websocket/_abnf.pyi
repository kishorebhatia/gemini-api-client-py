# Stubs for websocket._abnf (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from ._exceptions import *
from typing import Any

STATUS_NORMAL: int
STATUS_GOING_AWAY: int
STATUS_PROTOCOL_ERROR: int
STATUS_UNSUPPORTED_DATA_TYPE: int
STATUS_STATUS_NOT_AVAILABLE: int
STATUS_ABNORMAL_CLOSED: int
STATUS_INVALID_PAYLOAD: int
STATUS_POLICY_VIOLATION: int
STATUS_MESSAGE_TOO_BIG: int
STATUS_INVALID_EXTENSION: int
STATUS_UNEXPECTED_CONDITION: int
STATUS_BAD_GATEWAY: int
STATUS_TLS_HANDSHAKE_ERROR: int

class ABNF:
    OPCODE_CONT: int = ...
    OPCODE_TEXT: int = ...
    OPCODE_BINARY: int = ...
    OPCODE_CLOSE: int = ...
    OPCODE_PING: int = ...
    OPCODE_PONG: int = ...
    OPCODES: Any = ...
    OPCODE_MAP: Any = ...
    LENGTH_7: int = ...
    LENGTH_16: Any = ...
    LENGTH_63: Any = ...
    fin: Any = ...
    rsv1: Any = ...
    rsv2: Any = ...
    rsv3: Any = ...
    opcode: Any = ...
    mask: Any = ...
    data: Any = ...
    get_mask_key: Any = ...
    def __init__(self, fin: int = ..., rsv1: int = ..., rsv2: int = ..., rsv3: int = ..., opcode: Any = ..., mask: int = ..., data: str = ...) -> None: ...
    def validate(self, skip_utf8_validation: bool = ...): ...
    @staticmethod
    def create_frame(data, opcode, fin: int = ...): ...
    def format(self): ...
    @staticmethod
    def mask(mask_key, data): ...

class frame_buffer:
    recv: Any = ...
    skip_utf8_validation: Any = ...
    recv_buffer: Any = ...
    lock: Any = ...
    def __init__(self, recv_fn, skip_utf8_validation) -> None: ...
    header: Any = ...
    length: Any = ...
    mask: Any = ...
    def clear(self): ...
    def has_received_header(self): ...
    def recv_header(self): ...
    def has_mask(self): ...
    def has_received_length(self): ...
    def recv_length(self): ...
    def has_received_mask(self): ...
    def recv_mask(self): ...
    def recv_frame(self): ...
    def recv_strict(self, bufsize): ...

class continuous_frame:
    fire_cont_frame: Any = ...
    skip_utf8_validation: Any = ...
    cont_data: Any = ...
    recving_frames: Any = ...
    def __init__(self, fire_cont_frame, skip_utf8_validation) -> None: ...
    def validate(self, frame): ...
    def add(self, frame): ...
    def is_fire(self, frame): ...
    def extract(self, frame): ...