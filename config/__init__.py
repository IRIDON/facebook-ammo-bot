# -*- coding: utf-8 -*-

import os, sys
from key import default_api_key as apiKey

path = os.path.abspath(os.path.split(sys.argv[0])[0])

default_settings = {
    "PORT": 1025,
    "ACCESS_TOKEN": apiKey["ACCESS_TOKEN"],
    "VERIFY_TOKEN": apiKey["VERIFY_TOKEN"],
    "BOT_DATA_FILE": path + "/config/messages.json",
    "RESULT_ITEMS_COUNT": 5,
    "DISCONT": [0, 3, 5, 10, 15, 20, 25],
    "CURRENCY": "UAH",
    "DEFAULT_LOCAL": "ru",
    "AVAILABLE_LANGUAGES": ["en", "ru", "ua"],
    "CALIBERS": [
        "223_Rem",
        "308_Win",
        "338_Lapua_Mag",
        "7.62x39",
        "22_LR",
        "30-06",
        "300_Win_Mag",
        "22_WMR",
        "6.5_Creedmoor",
        "300_Win",
        "5.45x39",
        "222_Rem",
        "9PA",
        "7mm_Rem_Mag",
        "338_Win_Mag",
        "12/70_bulet",
        "12/70_buckshot",
        "12/70_fraction",
        "12/70",
        "12/76",
        "16/70",
        "20/70"
    ],
    "SHOPS": {
        "ibis": {
            "shop_name": "ibis",
            "url": "https://ibis.net.ua/",
            "url_tmp": "https://ibis.net.ua/products/%s/search/offset/?param_51[]=%s&isort=cheap&show_all=yes",
            "data_file": path + "/data/ibis.json",
            "ammo_type": {
                "rifle": "patrony-nareznye86",
                "traumatic": "patrony-travmaticheskie",
                "bore_bulet": "puli-gladkostvolnie",
                "bore_buckshot": "kartechy",
                "bore_fraction": "droby"
            },
            "category": {
                "223_Rem": ["198", "rifle", 0],
                "308_Win": ["196", "rifle", 1],
                "338_Lapua_Mag": ["275", "rifle", 2],
                "7.62x39": ["6476", "rifle", 3],
                "22_LR": ["348", "rifle", 4],
                "30-06": ["177", "rifle", 5],
                "300_Win_Mag": ["189", "rifle", 6],
                "6.5_Creedmoor": ["259908", "rifle", 7],
                "22_WMR": ["358", "rifle", 11],
                "222_Rem": ["533", "rifle", 12],
                "243_Win": ["188", "rifle", 13],
                "5.45x39": ["46441", "rifle", 14],
                "6.5x55": ["6281", "rifle", 15],
                "7mm_Rem_Mag": ["197", "rifle", 16],
                "8x57_JS": ["6324", "rifle", 17],
                "9.3x62": ["944", "rifle", 18],
                "9PA": ["8959", "traumatic", 19],
                "12/70_bulet": ["364", "bore_bulet", 20],
                "12/70_buckshot": ["364", "bore_buckshot", 21],
                "12/70_fraction": ["364", "bore_fraction", 22],
            }
        },
        "stvol": {
            "shop_name": "stvol",
            "url": "https://stvol.ua",
            "url_tmp": "https://stvol.ua/catalog/%s/filter/%s/apply/?page_sort=price_asc",
            "data_file": path + "/data/stvol.json",
            "ammo_type": {
                "rifle": "patrony_nareznye",
                "bore": "patrony_gladkostvolnye",
                "traumatic": "patrony_travmaticheskogo_deystviya"
            },
            "category": {
                "223_Rem": ["kalibr-is-91bb3ef4-f38b-11e2-bd5e-1cc1de282c58", "rifle", 0],
                "308_Win": ["kalibr-is-99957513-f397-11e2-bd5e-1cc1de282c58", "rifle", 1],
                "338_Lapua_Mag": ["kalibr-is-ca7b6293-be7d-11e4-bddc-1cc1de282c58", "rifle", 2],
                "22_LR": ["kalibr-is-ada64ea2-f397-11e2-bd5e-1cc1de282c58", "rifle", 3],
                "30-06": ["kalibr-is-c20cd9bc-f397-11e2-bd5e-1cc1de282c58", "rifle", 4],
                "300_Win_Mag": ["kalibr-is-cf2df0be-f397-11e2-bd5e-1cc1de282c58", "rifle", 5],
                "338_Win_Mag": ["kalibr-is-f37388bc-bb65-11e4-8f94-1cc1de282c58", "rifle", 6],
                "6.5_Creedmoor": ["kalibr-is-7c63096b-6b9c-11e7-ab40-00155dfa860b", "rifle", 6],
                "222_Rem": ["kalibr-is-619213a1-f397-11e2-bd5e-1cc1de282c58", "rifle", 7],
                "7.62x54R": ["kalibr-is-9a7138f2-b03a-11e4-bc08-1cc1de282c58", "rifle", 8],
                "5.45x39": ["kalibr-is-4f22644d-be84-11e4-bddc-1cc1de282c58", "rifle", 9],
                "300 AAC": ["kalibr-is-b79860b6-1837-11e6-9b00-1cc1de282c58", "rifle", 10],
                "6.5x55": ["kalibr-is-68682503-f398-11e2-bd5e-1cc1de282c58", "rifle", 11],
                "7mm_Rem_Mag": ["kalibr-is-05d3a7d3-d94a-11e4-8e15-1cc1de282c58", "rifle", 12],
                "9.3x62": ["kalibr-is-247b80d0-f398-11e2-bd5e-1cc1de282c58", "rifle", 13],
                "9RA": ["kalibr-is-f5f0d571-640b-11e4-9e41-1cc1de282c58", "traumatic", 14],
                "12/70": ["kalibr-is-a45bde61-d219-11e4-8e15-1cc1de282c58", "bore", 15],
                "12/76": ["kalibr-is-5998ccc0-d90e-11e4-8e15-1cc1de282c58", "bore", 16],
                "16/70": ["kalibr-is-114c2f3e-d210-11e4-8e15-1cc1de282c58", "bore", 17],
                "20/70": ["kalibr-is-d44ea6b4-d204-11e4-8e15-1cc1de282c58", "bore", 18]
            }
        },
        "safari": {
            "shop_name": "safari",
            "url": "http://safari-ukraina.com",
            "url_tmp": "http://safari-ukraina.com/%s=%s;sort=cheap/",
            "data_file": path + "/data/safari.json",
            "ammo_type": {
                "rifle": "nareznye-patrony/c269/kalibr-nareznoy",
                "bore": "gladkie-patrony/c281/kalibr-gladk1",
                "traumatic": "travmaticheskie-patrony/c176999/detail_11301"
            },
            "category": {
                "223_Rem": ["5456", "rifle", 0],
                "308_Win": ["5475", "rifle", 1],
                "22_LR": ["5451", "rifle", 2],
                "30-06": ["5466", "rifle", 3],
                "300_Win_Mag": ["5473", "rifle", 4],
                "6.5_Creedmoor": ["6535", "rifle", 4],
                "270_Win": ["5462", "rifle", 5],
                "280_Rem": ["5464", "rifle", 6],
                "30_R_Blaser": ["5465", "rifle", 7],
                "300_Wby_Mag": ["5471", "rifle", 8],
                "375_H_&_H_Mag": ["5485", "rifle", 9],
                "470_Nitro-Express": ["5506", "rifle", 10],
                "5.45x39": ["5525", "rifle", 10],
                "300 AAC": ["5472", "rifle", 11],
                "7mm_Rem_Mag": ["5536", "rifle", 12],
                "7x64": ["5541", "rifle", 13],
                "7x65_R": ["5542", "rifle", 14],
                "8x57_JRS": ["5543", "rifle", 15],
                "8x57_JS": ["5544", "rifle", 16],
                "9.3x74_R": ["5552", "rifle", 17],
                "9RA": ["5384", "traumatic", 18],
                "12/70": ["5371", "bore", 19],
                "12/76": ["5372", "bore", 20],
                "16/70": ["5375", "bore", 21],
                "20/70": ["5377", "bore", 22],
            }
        },
        "kulya": {
            "shop_name": "kulya",
            "url": "http://kulya.com.ua",
            "url_tmp": "http://kulya.com.ua/sortirovka/%s/%s&limit=72",
            "data_file": path + "/data/kulya.json",
            "ammo_type": {
                "rifle": "nareznye-patroni",
                "traumatic": "patrony-travmaticheskie",
                "bore_bulet": "pulya",
                "bore_buckshot": "kartech",
                "bore_fraction": "drob-dlya-ohoti"
            },
            "category": {
                "223_Rem": ["?custom_f_88[0]=2e3232332052656d", "rifle", 0],
                "308_Win": ["?custom_f_88[0]=2e3330382057696e", "rifle", 1],
                "7.62x39": ["?custom_f_88[0]=372e3632783339", "rifle", 2],
                "22_LR": ["?custom_f_88[0]=2e32324c52", "rifle", 3],
                "30-06": ["?custom_f_88[0]=2e33302d3036", "rifle", 4],
                "7.62x54_R": ["?custom_f_88[0]=372e36327835342052", "rifle", 5],
                "22_WMR": ["?custom_f_88[0]=2e323220574d52", "rifle", 6],
                "300_Win": ["?custom_f_88[0]=2e3330302057696e", "rifle", 7],
                "243_Win": ["?custom_f_88[0]=2e3234332057696e", "rifle", 8],
                "5.45x39": ["?custom_f_88[0]=352c3435783339", "rifle", 9],
                "12/70_buckshot": ["?custom_f_71[0]=31322f3730", "bore_buckshot", 10],
                "12/70_fraction": ["?custom_f_71[0]=31322f3730", "bore_fraction", 11],
                "12/70_bulet": ["?custom_f_71[0]=31322f3730", "bore_bulet", 12],
                "9RA": ["", "traumatic", 13]
            }
        }
    },
    "WEB": {
        "PAGES": {
            "home": {
                "name": "Home",
                "slug": "/",
                "template": "index.html",
                "visible": True
            },
            "privacy-policy": {
                "name": "Privacy Policy",
                "slug": "privacy-policy.html",
                "template": "privacy-policy.html",
                "visible": True
            },
            "error": {
                "name": "Error page",
                "slug": "page_not_found.html",
                "template": "page_not_found.html",
                "visible": False
            }
        },
        "BOT_NAME": "AmmoBot",
        "FACEBOOK_URL": "https://www.facebook.com/ammoPriceBot/"
    }
}

class Settings:
    def __init__(self):
        for key, value in default_settings.items():
            setattr(self, key, value)

settings = Settings()
