#!/usr/bin/env python3

TEXT = "4D69 61 6E657665 616E6E616B 61 68656C7969 6B617063736F6C6F6B6F7A706F6E746E616B2C 61686F6C 6D616A646E656D 656C6B617074616B"


def main():
    result = ""
    for s in TEXT.split(" "):
        # print(s + "->" + bytes.fromhex(s).decode("utf-8"))
        result += bytes.fromhex(s).decode("utf-8") + " "

    print(result)


if __name__ == "__main__":
    main()
