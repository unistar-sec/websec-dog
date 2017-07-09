#!/usr/bin/env python3
#-*-coding:utf-8-*-

import os
import re

def scan_module(module_name, path):
    '''
    scan file
    :param path: 
    :return: 
    '''
    path = path + '/' + module_name
    if not path or not os.path.isdir(path):
        return {}

    modules = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if root == path:
                file_path = name
            else:
                file_path = root.replace(path + '/', '') + '/' + name

            extension = os.path.splitext(file_path)

            # filter init file
            if extension[1] == '.py' and name != '__init__.py':
                modules.append(file_path.replace('.py', ''))

    return modules

def scan_exploit_module(path):
    return scan_module('exploits', path)

def scan_payload_module(path):
    return scan_module('payloads', path)

def search_module(module_list, keyword):
    result = []
    for module in module_list:
        if re.search(keyword, module, re.I|re.M):
            result.append(module)

    return result

def main(path):
    payloads = scan_payload_module(path)
    payloads_count = len(payloads)
    exploits = scan_exploit_module(path)
    exploits_count = len(exploits)

    modules = {
        'exploits' : exploits,
        'exploits_count' : exploits_count,
        'payloads' : payloads,
        'payloads_count' : payloads_count
    }
    return modules