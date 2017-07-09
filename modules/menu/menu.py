#-*-coding:utf-8-*-

# 菜单主页
def banner(modules):
    version = 'v1.0'
    exploits_count = modules['exploits_count']
    payloads_count = modules['payloads_count']

    logo = '''
    ============================================================
    =                                                          =
    =              _                           _               =
    = __      _____| |__    ___  ___  ___    __| | ___   __ _  =
    = \ \ /\ / / _ \ '_ \  / __|/ _ \/ __|  / _` |/ _ \ / _` | =
    =  \ V  V /  __/ |_) | \__ \  __/ (__  | (_| | (_) | (_| | =
    =   \_/\_/ \___|_.__/  |___/\___|\___|  \__,_|\___/ \__, | =
    =                                                    |___/ = 
    =            Author: E4sy++ soeasyd@gmail.com              =
    ============================================================
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\\
                ||----w |
                ||     ||
    + --=[ Web Exploit Framework - %s ]=-- +
    + --=[ EXPLOITS: %s ]=-- +
    + --=[ PAYLOADS: %s ]=-- +
    '''
    return (logo % (version, exploits_count, payloads_count))

# 帮助
def help():
    commands = {
        "help": "Help menu",
        "search exploits|payloads <keyword>": "Search exploit/payloads name",
        "show option": "show exploit option",
        "use <exploit name>": "use exploit module",
        "set <option> <value>": "Set exploit's variable",
        "exploit": "run exploit ",
        "update": "Update the framework",
        "quit": "Exit the program"
    }
    print("====== ")
    print("%-40s%s" % ("COMMAND", "DESCRIPTION"))
    print("%-40s%s" % ("-------", "------------"))
    for command in commands:
        print("%-40s%s" % (command, commands[command]))
    print("\n")

def showOption(options):
    print("======")
    print("%-30s%-30s%-30s" % ("OPTION", "VALUE", "EXAMPLE"))
    print("%-30s%-30s%-30s" % ("------", "------", "------"))

    for option in options:
        if isinstance(options[option], dict):
            example_value = options[option]["example"]
            current_value = options[option]["current_value"]
        else:
            example_value = options[option]
            current_value = None

        print("%-30s%-30s%-30s" % (option, current_value, example_value))
    print("\n")

def showExploit(exploit):
    print("======")
    print("[TITLE] [AUTHOR: %s]" % exploit.author)
    print(" %s" % exploit.title)
    print("\n[DESCRIPTION]")
    print(" %s" % exploit.description)
    print("\n[REDERENCE]")
    print(" %s" % exploit.reference)
    print("\n")

def showSearch(lists):
    print("============")
    print("MODULE LIST:")
    print("============")
    print("%-30s%-30s" % ("ID", "MODULE"))
    print("%-30s%-30s" % ("------", "------"))
    for i,name in enumerate(lists):
        print("%-30s%-30s" % ((i+1), name))
    print("\n")