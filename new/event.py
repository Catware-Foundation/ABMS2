# *~* CatABMS Command *~* #
#start-of-config
trigger = "событие"
description = "Событие, которое случится когда нибудь"
triggermode = "is"
timeout = "5"
author_pseudo = "Cat Weird"
author_contacts = "t.me/catweir1"
#end-of-config

list1 = "террорист,носок,котопай,гей,натурал,дибил,султан,разработчик котопая,линукс,кот".split(",")
list2 = "умер,воскрес,ахуел,летает,ездит,ебётся,кушает,срёт,горит,устроил поджог,обосрался".split(",")
list3 = "за спиной у,на,в гостях у,в кармане у,под,в".split(",")
list4 = "бомжа,бота,россию,путина,себя,тебя".split(",")

message("Событие: " + randd.choice(list1) + " " + randd.choice(list2) + " " + randd.choice(list3) + " " + randd.choice(list4))
