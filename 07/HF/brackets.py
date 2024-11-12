#!/usr/bin/env python3


def isValid(s: str) -> bool:
    hashmap = {")": "(", "}": "{", "]": "["}
    verem = []

    # brackets = [c for c in s if c in hashmap.values() or c in hashmap]
    brackets = []
    for c in s:
        for k, v in hashmap.items():
            if c == v or c == k:
                brackets.append(c)
    # print(brackets)

    for c in brackets:
        if c not in hashmap:  # A value-t fogja belerakni a verembe
            verem.append(c)
            # print(verem)
        else:
            if not verem:  # Ha üres a verem pl.: csak nyitó van de záró nincs
                return False
            else:
                # print(verem)
                popped = verem.pop()
                # print(popped, "k ->", hashmap[c], "c ->", c)
                if popped != hashmap[c]:
                    return False

    return not verem  # verem isEmpty


def main():
    # print(isValid(("((5+3)*2+1)")))
    # print(isValid(("{[(3+1)+2]+}")))
    # print(isValid(("(3+{1-1)}")))
    # print(isValid(("[1+1]+(2*2)-{3/3}")))
    print(isValid(("(({[(((1)-2)+3)-3]/3}-3)")))


if __name__ == "__main__":
    main()
