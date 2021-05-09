# *~* CatABMS Command *~* #
#start-of-config
trigger = "инфо"
description = "Информация о боте и его разработчиках"
triggermode = "is"
timeout = "10"
author_pseudo = "Cat Weird"
author_contacts = "t.me/catweir1"
#end-of-config

message("""Бот {} {}
Веб-сайт: {}
Багрепорты отправлять сюда -> {}
Работает под управлением: {} ({}, {}-like)
Разработчик: {}
Исходный код можно найти здесь: {}
""".format(botname, bot_codename, botsite, bugreport_url, systemname, systemname_acronym, distribution_like, developer, source_link))
