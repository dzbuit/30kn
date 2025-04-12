
# 30KN (Three-ten-thousand numeral system) Encoder/Decoder by blueradiance

BASE_30KN = 30000
HANGUL_OFFSET = 0xAC00  # '가'
HANJA_OFFSET = 0x4E00   # '一'
HANGUL_MAX = 9999
HANJA_MAX = 29999

def encode_30kn(n: int) -> str:
    if n == 0:
        return chr(HANGUL_OFFSET)
    result = []
    while n > 0:
        digit = n % BASE_30KN
        if digit <= HANGUL_MAX:
            ch = chr(HANGUL_OFFSET + digit)
        else:
            ch = chr(HANJA_OFFSET + (digit - (HANGUL_MAX + 1)))
        result.insert(0, ch)
        n //= BASE_30KN
    return ''.join(result)

def decode_30kn(s: str) -> int:
    n = 0
    for ch in s:
        code = ord(ch)
        if HANGUL_OFFSET <= code <= HANGUL_OFFSET + HANGUL_MAX:
            val = code - HANGUL_OFFSET
        elif HANJA_OFFSET <= code <= HANJA_OFFSET + (HANJA_MAX - HANGUL_MAX - 1):
            val = HANGUL_MAX + 1 + (code - HANJA_OFFSET)
        else:
            raise ValueError(f"Invalid character in 30KN string: '{ch}'")
        n = n * BASE_30KN + val
    return n
