#!/usr/bin/env python3
#*-* coding:utf-8 *-*

from core.framework import Framework

def run():
    app = Framework()
    try:
        app.load_banner()
        app.cmdloop()
    except KeyboardInterrupt:
        print("Exception occur, use 'quit' command to quit")
if __name__ == "__main__":
   run()