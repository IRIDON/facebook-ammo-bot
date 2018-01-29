# -*- coding: utf-8 -*-
import json, os
from config import settings
from flask import Flask, request, send_from_directory
from lib.Constructor.facebookConstructor import FacebookConstructor
from lib.Constructor.botSetSettings import BotSetSettings
from lib.Web.page import Page
from lib.Logger.logger import Log

app = Flask(__name__)
viewPage = Page(settings.WEB)
fb = FacebookConstructor(
    token=settings.ACCESS_TOKEN,
    dataFile=settings.BOT_DATA_FILE,
    currency=settings.CURRENCY,
    discount=settings.DISCONT,
    shopData=settings.SHOPS,
    allCalibers=settings.CALIBERS,
    resultItemCount=settings.RESULT_ITEMS_COUNT,
    local=settings.DEFAULT_LOCAL
)
botSettings = BotSetSettings(
    token=settings.ACCESS_TOKEN,
    dataFile=settings.BOT_DATA_FILE,
    shopData=settings.SHOPS,
    availableLanguages=settings.AVAILABLE_LANGUAGES,
    defaultLocal=settings.DEFAULT_LOCAL
)

botSettings.getStart()
botSettings.setMenu()

log = Log()
print 'run'
@app.route("/", methods=['GET'])
def index():
    print 'index'
    if request.method == 'GET':
        print 'Get is ok'

        if request.args.get("hub.verify_token") == settings.VERIFY_TOKEN:
            print 'verify token is ok'
            return request.args.get("hub.challenge")
        else:
            return viewPage.page("home")

@app.route("/", methods=['POST'])
def webhook():
    """
    1) select command - all message or post COMMAND
    2) select store - SHOP
        2.1) Select simple top list - TOP
        2.2) Select list with discount - DISCOUNT
            2.2.1) User select discout
    3) select caliber from current shop
    4) Print top list
    """
    data = request.get_json()
    recipient_id, message = fb.getMessage(data)
    print 'Post'
    print 'Id ' + recipient_id
    print 'Id ' + message
    if recipient_id and message:
        dataCategory = ''

        """ Test if it post data """
        if message.find("__") != -1:
            messageArray = message.split("__")
            dataCategory = messageArray[0]
            dataId = messageArray[1]

            if len(messageArray) > 2:
                fb.setLocal(messageArray[2])

        if dataCategory == "SHOP": # (2)
            if dataId == "DISCOUNT": # (2.2.1)
                fb.printListDiscount(recipient_id)
            elif dataId == "ALL":
                fb.setDiscount("0%")
                fb.botAllCaliberChoice(recipient_id)
            else: # (2.1)
                fb.setDiscount("0%")
                fb.botSelectStore(recipient_id)
        elif dataCategory == "DISCOUNT": # (2.2)
            fb.setDiscount(dataId)
            fb.botSelectStore(recipient_id)
        elif dataCategory == "CHOICE": # (3)
            fb.botCaliberChoice(dataId, recipient_id)
        elif dataCategory == "TOP": # (4)
            fb.botPrintTop(dataId , recipient_id)
        elif dataCategory == "ALL": # (2.2)
            fb.botPrintAll(dataId, recipient_id)
        elif dataCategory == "COMMANDS": # (4)
            fb.botCommands(recipient_id)
        else: # (1)
            fb.botCommands(recipient_id)
    
    return "ok", 200

@app.route("/<page>")
def page(page):
    page = page.replace(".html", "")

    return viewPage.page(page)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, 'static'),
        'favicon.ico',
        mimetype='image/vnd.microsoft.icon'
    )

@app.errorhandler(404)
def page_not_found(error):
    return viewPage.page("error")

if __name__ == "__main__":
    app.run(port=settings.PORT)
