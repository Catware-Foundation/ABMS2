
#
# -*- coding: utf-8 -*-
#
# ABMSv2 Kernel - developed by Catware, 2018-2021.
#
# Requires catENV (developed by Catware too)
#

exec(readff("lib/detectfull.py"))
exec(readff("lib/recognize.py"))
exec(readff("systemlibs/codeaccess.py"))

outproc("Загрузка настроек...")
for x in getfiles('systemsettings'):
    exec(readff("systemsettings/" + x))

for x in getfiles('systeminformation'):
    exec(readff("systeminformation/" + x))

service_errors = [] 
corerc_errors = []
commands_errors = []
oldcommands_errors = []
commands = []
rchooks_errors = []

systemcare = 0
careless = 0

NCOMMANDSDIR = "new/"
COMMANDSDIR = "oldcommands/"

if load_old_commands:
    for x in os.listdir(COMMANDSDIR):
        try:
            try:
                procmsg("Загрузка команды " + x[:-3])
                exf = open(COMMANDSDIR + x)
                read = exf.readlines()
                for y in range(6):
                    exec(read[y + 1])
                if "#disable" not in "\n".join(read):
                    #authors.append(author)
                    #modes.append(mode)
                    #depends.append(deps.split(','))
                    #ids.append(identificator)
                    #commands.append(command_ru)
                    #descs.append(description)
                    #exf.close()
                    if mode == "=":
                        triggermode = "is"
                    if mode == "start":
                        triggermode = "argument"
                    if mode == "pic":
                        triggermode = "picture"
                    commands.append({"triggers": [command_ru], "description": description, "triggermode": triggermode,
                                     "argexample": "текст", "timeout": 30, "category": ["Старые команды"],
                                     "author_pseudo": author, "author_contacts": "vk.com/catweird", "call": COMMANDSDIR + x, "vars": ["*"],
                                     "adminmode": False})
                    succ()
                    systemcare += 1
                    if "#testing" not in "\n".join(read):
                        careless += 1
                #else:
                #    succ()
                #    print("Внимание: команда " + command_ru + " отключена.")
                #if "#restricted" not in "\n".join(read):
                #    restr.append("false")
                #else:
                #    restr.append("true")
            except:
                warn("Не удалось загрузить команду.")

        except Exception as e:
            failcomplete()
            olcommands_errors.append(str(e))
            systemcare += 1
            careless += 1

outproc("Начинается загузка команд из папки " + NCOMMANDSDIR)
for x in os.listdir(NCOMMANDSDIR):
    contents = readff(NCOMMANDSDIR + x).split("\n")
    triggers = randd.choice(["т", "у", "е", "с", "о", "к", "о", "б", "я", "к", "о", "в"]) + randd.choice(["т", "у", "е", "с", "о", "к", "о", "б", "я", "к", "о", "в"]) + randd.choice(["т", "у", "е", "с", "о", "к", "о", "б", "я", "к", "о", "в"]) + randd.choice(["т", "у", "е", "с", "о", "к", "о", "б", "я", "к", "о", "в"]) + randd.choice(["т", "у", "е", "с", "о", "к", "о", "б", "я", "к", "о", "в"])
    linecount = 0
    description = "Описание недоступно."
    triggermode = "is"
    argexample = "текст"
    category = "Неизвестно"
    adminmode = False
    variableregistry = []
    timeout = 30
    author_pseudo = "Автор неизвестен"
    author_contacts = "vk.com/catweird (нету известного мейнтейнера, пусть этим займутся разработчики бота)"
    for y in contents:
        if y != "#end-of-config":
            exec(y)
        else:
            break
    try:
        commands.append({"triggers": trigger.split(";"), "description": description, "triggermode": triggermode, "argexample": argexample, "timeout": timeout,
                     "author_pseudo": author_pseudo.split(";"), "author_contacts": author_contacts, "category": category.split(";"), "call": NCOMMANDSDIR + x, "vars": variableregistry,
                     "adminmode": adminmode})
        outproc("Загружена команда " + NCOMMANDSDIR + x)
    except Exception as e:
        warn(str(e))

rchooks = []
for x in os.listdir("rchooks"):
    try:
        procmsg("Загрузка RunCommand-хука " + x[:-3])
        rchooks.append(readff('rchooks/' + x))
        succ()
        systemcare += 1
    except Exception as e:
        rchooks_errors.append("RunCommand-hook: " + readff('rchooks/' + x) + ", ошибка: " + str(e))
        failcomplete()
        systemcare += 1
        careless += 1

rcs = []
for x in os.listdir("corerc"):
    try:
        procmsg("Загрузка динамического процесса " + x[:-3])
        rcs.append(readff('corerc/' + x))
        succ()
        systemcare += 1
    except Exception as e:
        corerc_errors.append("Динамический процесс: " + readff('corerc/' + x) + ", ошибка: " + str(e))
        failcomplete()
        systemcare += 1
        careless += 1

outproc("Запуск Autostart...")
for x in os.listdir('services'):
    procmsg("Загрузка сервиса " + x[:-3])
    try:
        run("services/" + x)
        succ()
        systemcare += 1
    except Exception as e:
        systemcare += 1
        careless += 1
        failcomplete()
        service_errors.append("Сервис: " + x + ", ошибка: " + str(e))

outproc('Ядро загружено.')

starttime = time.time()

while True:
    outproc("Запущен главный цикл")
    try:
        for event in longpoll.listen():
            eventmsg(str(event.type))
            if event.type == VkBotEventType.MESSAGE_NEW or event.type == VkBotEventType.MESSAGE_EDIT :
                for x in rcs:
                    exec(x)
                outproc("Разбор сообщения")
                mode = "ignore"
                use_prefix = False
                msgtext = event.object["text"]
                if msgtext.startswith(userprefix):
                    msgtext = msgtext[len(userprefix):]
                    use_prefix = True
                if msgtext.startswith("/"):
                    msgtext = msgtext[1:]
                    use_prefix = True
                peer_id = event.object["peer_id"]
                user_id = event.object["from_id"]
                message_id = event.object["conversation_message_id"]
                outproc("Определение источника")
                source = "undefined"
                attachments = []
                picture_urls = []
                if event.from_chat:
                    source = "chat"
                    chat_id = event.chat_id
                    outproc("Обнаружен источник: чат")
                if event.from_user:
                    source = "user"
                    chat_id = None
                    outproc("Обнаружен источник: Л/С")
                outproc("Проверка на наличие вложений...")
                for x in event.object["attachments"]:
                    try:
                        attachments.append(x["type"] + user_id + "_" + x["id"])
                        outproc("Обнаружен " + x["type"] + user_id + "_" + x["id"])
                    except:
                        warn("Вложений найти не удалось/ошибка парсинга event object")
                for x in event.object["attachments"]:
                    try:
                        for y in x:
                            try:
                                picture_urls.append(detectfull(y))
                                outproc("Приложено " + detectfull(y))
                            except:
                                pass
                    except:
                        pass
                outproc("Парсинг сообщения завершён. Определение режима сообщения")
                try:
                    if event.object["action"]["type"] == "chat_invite_user" and event.object["action"]["member_id"] == gid:
                        message(conference_welcome_text)
                        mode = "notcommand"
                except:
                    pass
                if "audio_message" in ",".join(attachments):
                    mode = "voice"
                    outproc("Обнаружено голосовое сообщение")

                if msgtext != "":
                    mode = "ai"
                    outproc("Обнаружен факт того, что сообщение не пустое")
                    cmd = msgtext.split(" ")[0]
                    parameter = " ".join(msgtext.split(" ")[1:])

                if msgtext == "" and "photo" in ",".join(attachments):
                    mode = "picture_handle_variants"
                    outproc("Будет предложено, как обработать изображение")

                if msgtext != "" and use_prefix:
                    pattern = msgtext.split(" ")
                    cmd = pattern[0]
                    parameter = " ".join(pattern[1:])
                    mode = "trycommand"
                    outproc("Пробую найти команду")

                if get_parameter_by_trigger(cmd, "call") != "error" or mode == "trycommand":
                    outproc("Пробую запустить команду")
                    exec(readff(get_parameter_by_trigger(cmd, "call")))
                    outproc("Команда " + get_parameter_by_trigger(cmd, "call") + " успешно выполнена!")
                for x in rchooks:
                    exec(x)
    except Exception as e:
        warn("Произошла ошибка ядра: " + str(e))
