#!/usr/bin/env python3


def sort(user: str):
    return int(user.split(":")[0])


def main():
    users = ["10:User1", "80:User2", "100:User3", "00:User4", "75:User4", "45:User5"]

    print(users)

    print(sorted(users, key=sort, reverse=True))


if __name__ == "__main__":
    main()
