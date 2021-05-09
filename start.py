#
# -*- coding: utf-8 -*-
#
# Catware-Foundation. 2016-2021
#
# ABMSv2 Loader
#

file = open("catenv.py", encoding="utf-8")
catenv = file.read()
file.close()
exec(catenv)
catenv = ""

try:
    print(readff("usr/distro.txt"))
except:
    warn("usr/distro.txt отсутсвует. Придётся довольствоваться этой надписью :(")

#
# Modules
#

import os
from math import ceil, pi
import textwrap
import tempfile
import datetime
import json
import qrcode
from gtts import gTTS
from pyaspeller import Word, YandexSpeller
speller = YandexSpeller()
import speech_recognition as speech_recog
rec = speech_recog.Recognizer()
from pydub import AudioSegment
import html2text
from lyricsgenius import Genius
genius = Genius("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[") # Вставьте ваш токен здесь
genius.response_format = 'plain'
import shutil
import markovify
import subprocess
import wikipedia
import runpy
import numpy as np
import wget
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random as randd
from random import random
import requests
from requests import get, post, Session
import vk_api
import vk_api as api2
from vk_api import VkApi
from vk_api import VkUpload
import time
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
session = requests.Session()
wikipedia.set_lang("ru")
import urllib.request
import urllib.parse
import sys
import traceback
from threading import Thread
from googletrans import Translator
translator = Translator()

for x in os.listdir("configs"):
    procmsg("Загрузка конфигурации - " + x[:-3])
    exec(readff("configs/" + x))
    succ()

outproc("Обнаружение операционной системы...")
if os.name == 'nt':
    osname = 'Windows NT'
if os.name == 'posix':
    osname = 'Unix-подобная ОС'
if os.name == 'mac':
    osname = 'MacOS'
if os.name == 'os2':
    osname = 'OS/2 Warp'
if os.name == 'ce':
    osname = 'Windows CE'
if os.name == 'java':
    osname = 'Java'
infomsg('Обнаружена операционная система: ' + osname)
#try:
#    os.mkdir('exf')
#    os.mkdir('users')
#    os.mkdir('chats')
#except Exception:
#    pass

#procmsg("Подготовка к запуску ядра...")
#authors = []
#commands = []
#ids = []
#descs = []
#modes = []
#depends = []
#codes = []
#restr = []
#succ()

procmsg("Авторизация")
vk_session = VkApi(token=token)
longpoll = VkBotLongPoll(vk_session, gid)
vk = vk_session.get_api()
keyboard = VkKeyboard(one_time=False)
uptime = str(time.ctime())
uptime_time = time.time()
succ()

#procmsg('Финальная подготовка.')
#writeto(admins, "admins.txt")
#succ()

while True:
    try:
        mta('Запускаю ядро...')
        exec(readff("kernel.py"))
        mta('Ядро упало :(')
    except Exception as e:
        print('Паника ядра: ' + str(e))
    #authors = []
    #commands = []
    #ids = []
    #descs = []
    #modes = []
    #depends = []
    #codes = []
    #restricted = []
