# -*- coding: utf-8 -*-
import logging, json, requests
from lib.Constructor.botConstructor import BotConstructor
from pymessenger.bot import Bot
from lib.Logger.logger import Log

log = Log()

class FacebookConstructor(BotConstructor):
    __slots__ = [
        "accessToken",
        "bot",
        "currency",
        "availableDiscount",
        "message",
        "commands",
        "shopData",
        "visibleTopItems",
        "availableShops",
        "categories",
        "categoriesKeys",
        "availableAmmo",
        "dataFileUrl",
        "discount"
    ]
    def __init__(self, **kwargs):
        self.accessToken = kwargs["token"]
        self.bot = Bot(self.accessToken)
        self.currency = kwargs["currency"]
        self.availableDiscount = kwargs["discount"]
        self.shopData = kwargs["shopData"]
        self.visibleTopItems = kwargs["resultItemCount"]
        self.availableShops = self.shopData.keys()
        self.discount = 0
        self.readDataFile(kwargs["dataFile"])
        self.initShopData(self.availableShops[0])

    """ Parse facebook data and return message """
    def getMessage(self, data):
        try:
            for event in data['entry']:
                for item in event['messaging']:
                    recipient_id = item['sender']['id']

                    if item.get('message'):
                        message = item['message']

                        if message.get('quick_reply'):
                            message_text = message['quick_reply']['payload']
                        elif message.get('text') and not message.get('app_id'):
                            message_text = message['text']
                        else:
                            return False, False

                    elif item.get('postback'):
                        message_text = item['postback']['payload']
                    else:
                        return False, False

                    return recipient_id, message_text
        except Exception as error:
            log.error("Facebook " + error)

    def setDiscount(self, discount):
        try:
            discount = discount.replace("%", "")
            discount = int(discount)

            self.discount = discount
        except Exception as error:
            log.error("Facebook " + error)
        
    """ Create slide button group """
    def createButtonGroup(self, arr, dataId):
        result = []

        for name in arr:
            dic = {}
            dic["type"] = "postback"
            dic["title"] = self.getKeyName(name)
            dic["payload"] = "%s__%s" % (dataId.upper(), name)

            result.append(dic)
        
        return list(self.chunks(result, 3))

    """ Create button pack for button group """
    def botCreateButtons(self, title, arr, dataId):
        result = []
        buttons = self.createButtonGroup(arr, dataId)

        for item in buttons:
            dic = {}
            dic["title"] = title
            dic["buttons"] = item

            result.append(dic)

        return result

    def botCreadeQuickReplies(self, text, arr, dataId):
        result = []

        for name in arr:
            dic = {}
            dic["content_type"] = "text"
            dic["title"] = self.getKeyName(name)
            dic["payload"] = "%s__%s" % (dataId.upper(), name)

            result.append(dic)

        return {
            "text": text,
            "quick_replies": result
        }

    """ Create button link """
    def createButtonLink(self, title, link):
        result = []

        dic = {}
        dic["type"] = "web_url"
        dic["title"] = title
        dic["url"] = link

        result.append(dic)
        
        return result

    """ Create structure for list main commans """
    def getFormateCommands(self, data):
        result = []
  
        for key in data:
            dic = {}
            dic["type"] = "postback"
            dic["title"] = data[key][1]
            dic["payload"] = "%s__%s" % (data[key][0], key.upper())

            result.append(dic)

        return result

    def botCommands(self, recipient_id):
        try:
            self.bot.send_button_message(
                recipient_id,
                self.message["select_commad"],
                self.getFormateCommands(self.commands)
            )
        except Exception as error:
            log.error("Facebook " + error)

    def botNone(self, recipient_id):
        try:
            self.bot.send_text_message(
                recipient_id,
                self.message["no_commad"][0],
            )
        except Exception as error:
            log.error("Facebook " + error)

    """ Print aviable discounts """
    def printListDiscount(self, recipient_id):
        try:
            doscounts = []

            for item in self.availableDiscount:
                doscounts.append(
                    str(item) + "%"
                )
                
            keyboard = self.botCreadeQuickReplies(
                self.message["select_discount"],
                doscounts,
                "discount"
            )

            self.bot.send_message(
                recipient_id,
                keyboard
            )
        except Exception as error:
            log.error("Facebook " + error)

    """ Print aviable shops list """
    def botSelectStore(self, recipient_id):
        try:
            shopName = []

            for shop in self.availableShops:
                shopName.append(shop.upper())
                
            keyboard = self.botCreadeQuickReplies(
                self.message["select_store"],
                shopName,
                "choice"
            )

            self.bot.send_message(
                recipient_id,
                keyboard
            )
        except Exception as error:
            log.error("Facebook " + error)

    """ Print aviable caliber list for current shop """
    def botCaliberChoice(self, currentShop, recipient_id):
        try:
            self.initShopData(currentShop);

            keyboard = self.botCreateButtons(
                self.message["select_caliber"],
                self.categoriesKeys,
                "top"
            )
            self.bot.send_generic_message(
                recipient_id,
                keyboard
            )
        except Exception as error:
            log.error("Facebook " + error)

    """ Print offers """
    def botPrintTop(self, currentCaliber, recipient_id):
        try:
            text = self.topPrices(
                self.visibleTopItems,
                str(currentCaliber),
                self.discount
            )
            textArray = text[:-1]
            link = text[-1]
            textFormated = self.separateText(textArray)

            if len(textFormated) >= 640: # test message for chars limit - for facebook it's 640 chars
                textPartFirst, textPartSecond = self.separateMesageToTwo(textArray)

                self.bot.send_text_message(
                    recipient_id,
                    textPartFirst
                )
                textFormated = textPartSecond
            elif len(textArray) == 0:
                self.bot.send_button_message(
                    recipient_id,
                    self.message["no_results"],
                    self.createButtonLink(
                        self.message["link_text"],
                        link
                    )
                )
                    
            self.bot.send_button_message(
                recipient_id,
                textFormated,
                self.createButtonLink(
                    self.message["link_text"],
                    link
                )
            )
        except Exception as error:
            log.error("Facebook " + error)
