# -*- coding: utf-8 -*-
import json

class BotConstructor(object):
    __slots__ = [
        "currency",
        "message",
        "shopData"
    ]
    def __init__(self, **kwargs):
        self.currency = kwargs["currency"]
        self.message = kwargs["message"]
        self.shopData = kwargs["shopData"]

    def initShopData(self, shopName):
        shopName = shopName.lower()
        
        if self.shopData[shopName]:
            shopData = self.shopData[shopName]

            self.categories = shopData["category"]
            self.categoriesKeys = self.categories.keys()
            self.availableAmmo = shopData["ammo_type"]
            self.dataFileUrl = shopData["data_file"]
            self.currentShop = shopName
        else:
            return False

    def getData(self):
        with open(self.dataFileUrl, "r") as file:
            return json.load(file)

    def getDiscount(self, price, discount):
        factor = (100 - float(discount)) / 100

        return format(price * factor, '.2f')

    def getKeyName(self, name):
        return name.replace("_", " ")

    def toSeconds(self, day):
        return day * 24 * 60 * 60

    def capitalize(self, text):
        return text[:1].upper() + text[1:]
    