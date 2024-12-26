#!/usr/bin/env python3

import datetime
import os
import sys


def help():
    print("""countdown v0.1
Parameters:
-h                      this help
-p, -p2, -p3            play the sound effect (for adjusting the volume)
<time>                  where time can be given in different formats, e.g.
                        60    -> 60 seconds
                        60s   -> 60 seconds
                        1m    -> 1 minute
                        1m10s -> 1 minute and 10 seconds
                        1h5m  -> 1 hour and 5 minutes
          """)


def play_audio():
    os.system("play -q beep.mp3")


def time(time: str):
    hour = 0
    minute = 0
    second = 0
    try:
        time_l = list(time)
        if len(time_l) == 1:
            if time_l[1] == "s":
                second = int(time_l[0])
            elif time_l[1] == "m":
                minute = int(time_l[0])
            elif time_l[1] == "h":
                hour == int(time_l[0])
            minute = int(time_l[0])
        #elif len(time_l) == 1
        else:
            for i in range(0, len(time_l), 2):
                pass
        total_time = second + minute * 60 + hour * 3600

        for x in range(total_time,0,-1):

    except (KeyboardInterrupt, EOFError):
        print("abort")


def main():
    args = sys.argv

    if len(args) == 2:
        if args[1] == "-h":
            help()
            sys.exit(0)
        elif args[1] == "-p":
            play_audio()
            sys.exit(0)
        elif args[1] == "-p2":
            for _ in range(0, 2):
                play_audio()
                sys.exit(0)
        elif args[1] == "-p3":
            for _ in range(0, 3):
                play_audio()
                sys.exit(0)
        time(args[1])
    else:
        help()
        sys.exit(0)


if __name__ == "__main__":
    main()
