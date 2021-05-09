# *~* CatABMS Command *~* #
#start-of-config
trigger = "exec"
description = "Консоль бота [только для администраторов]"
triggermode = "parameter"
timeout = "60"
category = "Администрирование"
author_pseudo = "Cat Weird"
author_contacts = "t.me/catweir1"
#end-of-config

if str(user_id) in admins:
    try:
        exec(parameter)
        message('ok')
    except Exception as err:
        exc_type, exc_value, exc_tb = sys.exc_info()
        message('Error: \n' + "\n".join(traceback.format_exception(exc_type, exc_value, exc_tb)))
else:
    message("Вас нет в списке администраторов бота " + botname)
