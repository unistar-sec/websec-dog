#-*-coding:utf-8-*-
import sys
import os
import cmd

#导入模块
sys.path.append("../modules")
sys.path.append("../app")

#基础目录
basedir = os.path.dirname(os.path.dirname(__file__))
appdir = basedir + '/app'

#核心模块
from modules.menu import menu
from modules.plugins import logger, termcolor, manager
from modules.exploit.core import Core as ExploitCore

'''
Framework Core Class
'''
class Framework(cmd.Cmd, ExploitCore):
    def __init__(self):
        cmd.Cmd.__init__(self)
        ExploitCore.__init__(self)
        self.set_prompt()
        self.modules = manager.main(appdir)

    def do_list(self):
        return

    def do_search(self, keyword):
        if len(keyword.split()) !=2:
            return logger.error(" use `search exploits module_name`(eg: search exploits wordpress)")

        module = keyword.split()[0]
        module_name = keyword.split()[1]

        if not keyword or not module or not module_name:
            return logger.error(" use `search exploits module_name`(eg: search exploits wordpress)")

        result = []
        if 'exploits' == module.lower():
            result = manager.search_module(self.modules['exploits'], module_name)
        elif 'payloads' == module.lower():
            result = manager.search_module(self.modules['payloads'], module_name)
        else:
            return

        return menu.showSearch(result)

    # 显示Exploit参数
    def do_show(self, line):
        option = self.show_option()
        if not option:
            return logger.error("please use module first :(")
        if line == "option":
            return menu.showOption(option)
        else:
            return menu.showExploit(self.show_exploit())

    def do_use(self, exploit_name):
        if not exploit_name:
            return

        # 加载Exploit
        load_status = self.load_exploit(exploit_name)
        if load_status == False:
            return logger.error(" `%s` exploit module not exists !" % exploit_name)

        exploit_name = termcolor.colored(exploit_name, "red", None, ["bold"])

        # 更改提示符
        self.set_prompt(exploit_name)

    # 设置参数
    def do_set(self, arg):
        if not self.current_exploit:
            return
        else:
            result = self.set_option(arg.split())
            if result == True:
                pass
            else:
                logger.error(result)

    def do_exploit(self, line):
        if not self.current_exploit:
            return
        else:
            logger.process("Exloit init...")
            return self.run_exploit()

    def do_update(self, arg):
        if not arg:
            return
        # 更新本地新增文件
        if arg == 'local':
            self.modules = manager.main(appdir)
            return logger.success("update local file success :)")

    def do_back(self, arg):
        self.set_prompt()

    def do_quit(self, arg):
        exit()

    def do_clear(self, arg):
        os.system("clear")

    # 默认输出
    def default(self, line):
        logger.error("Unkown command: `%s`, use `help` command" % line)

    def emptyline(self):
        return

    def load_banner(self):
        print(menu.banner(self.modules))

    def do_help(self, arg):
        menu.help()

    # 加载数据库
    def load_db(self):
        return

    # 加载配置
    def load_config(self):
        return
    # 设置提示符
    def set_prompt(self, arg = None):
        if not arg:
            self.prompt = "Root>> "
        else:
            self.prompt = "Root>>(%s)>> " % arg