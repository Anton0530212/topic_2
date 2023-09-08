"""Программа, которая преобразует заданный
объем информации в килобайты, мегабайты и гигабайты"""

byte_size: int = 1234567890

kilo_size: float = byte_size / 1024
mega_size: float = byte_size / 1024 / 1024
giga_size: float = byte_size / 1024 / 1024 / 1024

# ----------------------

# kilo_size: float = byte_size / 1024
# mega_size: float = byte_size / 1024 ** 2
# giga_size: float = byte_size / 1024 ** 3

# ----------------------

# kilo_size: float = byte_size / 1024
# mega_size: float = kilo_size / 1024
# giga_size: float = mega_size / 1024

print('Размер в байтах:', 1234567890,
      '\nРазмер в килобайтах:', kilo_size,
      '\nРазмер в мегабайтах:', mega_size,
      '\nРазмер в гигабайтах:', giga_size)
