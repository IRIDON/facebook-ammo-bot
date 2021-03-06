import json, requests

from lib.Constructor.facebookConstructor import FacebookConstructor

DEFAULT_API_VERSION = 2.6

class BotSetSettings(FacebookConstructor):
    __slots__ = {
        "url",
        "accessToken",
        "shopData",
        "message",
        "commands",
        "availableLanguages",
        "defaultLocal"
    }
    def __init__(self, **kwargs):
        self.url = "https://graph.facebook.com/v%s/me/messenger_profile?access_token=%s"
        self.accessToken = kwargs["token"]
        self.shopData = kwargs["shopData"]
        self.availableLanguages = kwargs["availableLanguages"]
        self.defaultLocal = kwargs["defaultLocal"]
        self.readDataFile(kwargs["dataFile"])
        
    def getStart(self):
        textResult = []
        textData = self.message["greeting_text"]
        command = "COMMANDS__COMMANDS"

        for local, value in textData.iteritems():
            textResult.append({
                "locale": self.getFbLocaleName(local),
                "text": value % (self.getAllShopsNames(self.shopData))
            })

        payload = {
            "setting_type": "greeting",
            "greeting": textResult,
            "get_started": {
                "payload": command
            }
        }

        return self.botSendProfile(payload)

    def setMenu(self):
        menuItems = []

        # for language in self.availableLanguages:
        #     data = self.commands[language]

        #     if data:
        #         menuItems.append(self.getMenuItem(data, language))
        menuItems.append(self.getMenuItem(self.commands[self.defaultLocal], self.defaultLocal))

        payload = {
            "persistent_menu": menuItems
        }

        return self.botSendProfile(payload)

    def getMenuItem(self, data, local):
        dict = {}

        dict["locale"] = self.getFbLocaleName(local)
        dict["composer_input_disabled"] = True
        dict["call_to_actions"] = self.getFormateCommands(data, local)

        return dict

    def botSendProfile(self, payload):
        request_endpoint = self.url % (DEFAULT_API_VERSION, self.accessToken)
        response = requests.post(
            request_endpoint,
            json=payload
        )

        return response.json()

    def getFbLocaleName(self, local):
        fbLocaleName = {
            "en": "en_US",
            "ru": "ru_RU",
            "ua": "uk_UA"
        }

        if fbLocaleName[local]:
            return 'default' if local == self.defaultLocal else fbLocaleName[local]
        else:
            return None
