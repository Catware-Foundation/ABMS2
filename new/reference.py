# *~* CatABMS Command *~* #
#start-of-config
trigger = "справка;помощь;команды;help;котопай;меню"
description = "Справка: список команд бота"
triggermode = "is"
timeout = "10"
author_pseudo = "Cat Weird"
author_contacts = "t.me/catweir1"
#end-of-config

commandslist = []
adminlist = []
for a in commands:
    if "Администрирование" not in a["category"]:
        commandslist.append(" / ".join(a["triggers"]) + " -> " + a["description"])
    else:
        adminlist.append(" / ".join(a["triggers"]) + " -> " + a["description"] + " (админ-команда)")

commandstext = "\n".join(commandslist)
admincommandstext = "\n".join(adminlist)

if str(user_id) not in admins:
    message("Бот " + botname + " к вашим услугам!\n\n" + commandstext)
else:
    message("Здравствуй, хозяин. Бот " + botname + " не будет скрывать от вас админ-команд!\n\n" + admincommandstext + "\n\n- - - - - - - - -\n\n" + commandstext)
