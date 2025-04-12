# 30KN (Three-Ten-Thousand Numeral System / 삼만진수 / 三万进制)

**30KN** is a high-compression Unicode-based numeral system that combines Hangul (10KN) and Hanzi (20KN) to represent large integers efficiently and reversibly.

**30KN**은 한글(10KN)과 한자(20KN)를 결합하여 정수 데이터를 초고압축 형태로 표현할 수 있는 유니코드 기반 숫자 인코딩 시스템입니다.

**30KN**是结合了韩文（10KN）和汉字（20KN）的高压缩Unicode数字编码系统，可高效且可逆地表示整数。

---

## 📌 Features / 특징 / 特点

- 🔢 30,000 unique Unicode characters for encoding
- 📦 ~14.9 bits per character compression
- 🔁 Fully reversible: `encode_30kn()`, `decode_30kn()`
- 🧭 Lexicographically sortable
- 🔐 Unicode-safe, stable, language-neutral

---

## 🚀 How to Use / 사용법 / 使用方法

```python
from thirtykn import encode_30kn, decode_30kn

print(encode_30kn(123456789))  # Encoded string
print(decode_30kn('...'))      # Back to number
```

---

## 🧱 Character Set / 문자셋 구성 / 字符集结构

| Range | Type | Unicode | Description |
|-------|------|---------|-------------|
| 0–9999 | Hangul | 가~힣 | Human-friendly encoding (10KN)  
| 10000–29999 | Hanja | 一~龥 | Machine-optimized encoding (20KN)

Total: **30,000** unique characters

---

## 🧑‍💻 Author

- Creator: **blueradiance**
- First Released: 2025.04.12
- Project Type: Open Unicode Compression Framework

