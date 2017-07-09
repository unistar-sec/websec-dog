#!/usr/bin/env python
# -*- coding:utf-8-*-

from modules.plugins import termcolor

def error(string):
    print(termcolor.colored("[!] "+string, "red"))

def success(string):
    print(termcolor.colored("[+] "+string, "green"))

def process(string):
    print(termcolor.colored("[*] "+string, "cyan"))

def prompt(string):
    print(termcolor.colored(string, "yellow"))