#!/usr/bin/env python3

TEXT = """
Cbcq Dgyk!

Dmeybh kce cew yrwyg hmrylyaqmr:
rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!

Aqmimjjyi:

Ynyb
"""


# Eltolja a decimális értékét 2 vel
def decode(TEXT):
    words = ""

    for char in TEXT:
        # 64 alatt csak simán hozzáadjuk
        betu = ord(char)
        if betu > 64:
            # ord(char) - egy char- nak visszadja a decimális értékét
            # Majd hozzáad kettőt
            decimal = betu + 2

            # Ha túl csordul akkor visszafordul (pl.: { (123) -> a (97))
            # Kisbetük
            if decimal >= 123:
                kulonbseg = 123 - decimal
                decimal = 97 + kulonbseg

            # Nagybetük
            if decimal >= 91 and decimal <= 96:
                kulonbseg = 91 - decimal
                decimal = 65 + kulonbseg

            words += chr(decimal)
        else:
            words += char

    return words


def main():
    decoded_words = decode(TEXT)

    print(decoded_words)


if __name__ == "__main__":
    main()
