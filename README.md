#Web_Sec_Dog

Web Exploit Framework
```logo

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
            (__)\       )\/\
                ||----w |
                ||     ||
    + --=[ Web Exploit Framework - v1.0 ]=-- +
    + --=[ EXPLOITS: 14 ]=-- +
    + --=[ PAYLOADS: 0 ]=-- +

```

This is another web exploit framework focus on web exploit. Framework write by Python3 to make `EXPLOIT` simple, and has some base moudle like `Http module`,
There has many feature need wirte, like `whatcms`、`scanner`、`payload geneator`　etc.

##Base Arch
```shell

|- api
|    |__todo
|- app
|    |__exploits
|    |    |_some exploits
|    |__payloads
|        |_some payloads
|- core
|   |_framwork.py (framework core)
|
|- modules
|    |- database
|    |    |_drivers
|    |    |    |_TODO(some drivers)
|    |    |_db.py
|    |- exploit
|    |    |_core.py (exploit core implement)
|    |- http
|    |    |_http.py (requests lib implement)
|    |- menu
|    |    |_menu.py (print、logo etc)
|    |- plugins
|    |    |_logger.py (logger)
|    |    |_termcolor.py (terminator color print)
|    |- scanner
|    |  |_todo
|    |- whatcms
|         |_todo
|
|_run.py
```
## INSTALL
A good framework use less code to make more feature, the framework just use `requests` lib, `cmd` lib

Python: 3.4 or more (2.7 also support)

##USAGE

* basic use
```shell
#python run.py
#use wordpress/all_in_one_seo_pack_xss
#set target http://www.demo.com
#exploit
```

* search exploit
```shell
#python run.py
#search exploits keyword
#use demo_exploits
```
* show option
```shell
#python run.py
#use demo_exploits
#show option
#set target xxx
````
* help (show some information)

* update
```shell
when you write some exploits, just run `update` command reload exploits lists.
```

* quit (quit framework)

## Issues
The web sec dog just a simple exploit framework, if you like it or find some bugs, please contact me or push PR :)

## Refs
* MST
* CMS-Exploits-Framework