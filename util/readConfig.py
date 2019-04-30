#!/usr/bin/python3
# -*- coding:utf-8 -*-

import configparser


class ReadConfig:
    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read('../config.ini')

    def database(self, name):
        value = self.cf.get("db", name)
        return value

    def mongodb(self, name):
        value = self.cf.get("mongo", name)
        return value
