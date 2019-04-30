#!/usr/bin/python3
# -*- coding:utf-8 -*-

from pymongo import MongoClient

from util.readConfig import ReadConfig

db = ReadConfig()


class MongoDb:
    def __init__(self):
        self.client = MongoClient(db.mongodb("host"), db.mongodb("port"))
        self.db = self.client[db.mongodb("database")]

    def get_collection(self, collection):
        return self.db[collection]

    def find(self, collection, data, data_field={}):
        collection = self.get_collection(collection)
        if len(data_field):
            res = collection.find(data, data_field)
        else:
            res = collection.find(data)
        return res

if __name__ == '__main__':

    test = MongoDb()
    test.find("te")