# CatOS-type package <- это экземпляр команды, которую можно увидеть в проприетарной catABMS. кому увидеть? создателям проприетарной катАБМС, хуле
author = "catwared"
mode = "="
deps = 'None'
identificator = 'sova'
command_ru = 'сова'
description = 'Сова с рандомным текстом (это второй символ Котопая)'

sova = """＜￣｀ヽ、　　　　　　　／￣＞
　ゝ、　　＼　／⌒ヽ,ノ 　/´
　　　ゝ、　`（ ( ͡° ͜ʖ ͡°) ／
　　 　　>　 　 　,ノ {}
　　　　　∠_,,,/"""
glagols = "взрывать,слушать,оглушать,развешивать,сушить,дрочить,резать,ссать на,пить,есть,ломать,рисовать,нюхать,искать,разрушать,избивать,бить,строить,играть в,давить,жрать,мочить,расстреливать,есть,жрать,рожать,ебать,мастурбировать".split(",")
items = ",носки,патроны,музыку,фонк,боярышник,бутылки,члены,людей,города,кошек,деда,газ,нефть,стены,зубы,монтировку,гордона фримена,снюс,энергетики,дома,водку,алкаша,воздух,одноклассника,саморезы,себя".split(",")

message(sova.format("Лечу " + randd.choice(glagols) + " " + randd.choice(items)))

#restricted
