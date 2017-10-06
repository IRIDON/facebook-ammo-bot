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
    
    def readDataFile(self, dataFile):
        with open(dataFile, "r") as dataFile:
            data = json.loads(dataFile.read())

            self.message = data["message"]
            self.commands = data["commands"]

    """ find and structure offer results for choise shop and caliber """
    def topPrices(self, num=3, category='', discount=0):
        result = []
        allData = self.getData()

        if not allData:
            return self.message["base_error"]

        data = allData[category]
        dataLen = len(data)

        if dataLen < num:
            num = dataLen

        for index in range(0,num):
            title = data[index]["title"]
            price = data[index]["price"]

            if discount == 0:
                result.append("%s %s - %s" % (price, self.currency, title))
            else:
                result.append("%s %s \"%s\" - %s" % (
                    self.getDiscount(price, discount),
                    self.currency,
                    price,
                    title
                ))
        
        result.append(allData["url"][category])
        
        return result

    def chunks(self, l, n):
        """Yield successive n-sized chunks from l."""
        for i in range(0, len(l), n):
            yield l[i:i + n]

    def separateText(self, text):
        return "\n\n".join(text)

    def separateMesageToTwo(self, textArray):
        lenArr = len(textArray) / 2
        first = self.separateText(textArray[:lenArr])
        second = self.separateText(textArray[lenArr:])

        return first, second

    def getAllShopsNames(self, shopData):
        result = []

        for shopName in shopData:
            shop = shopData[shopName]
            
            result.append(shop["shop_name"])

        return ", ".join(result)
