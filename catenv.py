
#
# catENV V2.
#
# Catware-Foundation, 2020. Вы можете использовать определения из этого 
# набора определений, но с вас требуется указать наше авторство с обязательной
# ссылкой на данный репозиторий.
#
# Справку по данному проекту можно найти на https://catware.space/
#
#
# CatENV Memory (нахуя?)
#
# Собственное пространство имён
#
catenv_memory = []
def gname(name):
    try:
        global catenv_memory
        return catenv_memory[str(name)]
    except:
        return None
def setvar(name, value):
    try:
        global catenv_memory
        catenv_memory[str(value)] = value
    except:
        return None
#
# Конец зоны catENV Memory
#
#
# Сокращение для randd.choice
#
def choice(lst):
    return randd.choice(lst)
            dst_quad = [dst_grid[i    , j    , 0], dst_grid[i    , j    , 1],
#
# Сокращение для os.listdir().
#

def getfiles(path):
    return os.listdir(path)

#
# (исключительно для ВКонтакте) Зачёркивание текста.
#

def strike(text):
    text = list(str(text))
    txt = ""
    for a in text:
        txt += "&#0822;" + a
    log("Issued strike() with parameter: {}. Output: {}".format(str(text), str(txt + "&#0822;")))
    return txt + "&#0822;"

#
# Скрипт отправки сообщения по указанию идентификатора получателя
#

def messagecust(message, peer_id):
        vk.messages.send(random_id=randd.randint(-2147483647, 2147483647),peer_id=peer_id, message=message, dont_parse_links=1)

#
# Парсинг RSS-ленты сконвертированной в JSON. Должно быть в отдельном catLIB
#

def rssparse(txt):
    news = []
    for q in parse(txt)["entries"]:
        news.append({"title": q["title"], "link": q["link"], "description": q["title_detail"]["value"]})
    return news

#
# Скрипт логирования. Желательно отредактируйте его под свои нужды
#

def log(text):
    #txt = "[ " + str("-".join(deunix(time.time()))) + " UTC ] [" + str(__name__) + "] [" + str(__file__) + "] " + text + "\n"
    #PlusWrite(txt, "tmp/syslog.txt")
    pass

#
# Конвертировать имя хоста в IP адрес.
#

def hosttoip(host):
    log("Issued HostToIp() with " + str(host) + "parameter. Output: " + str(gethostbyname(host)))
    return gethostbyname(host)

#
# Вычисление процента. 
#

def percent(frst, scnd):
    coef = 100 / frst
    gets = scnd * coef
    log("Issued percent() with parameters: {} {}. Output: {}".format(str(frst), str(scnd), str(gets)))
    return gets

#
# Получить ID пользователя по короткому имени ВКонтакте
#

def getid(sname):
    unamea = vk.users.get(user_ids=sname)
    log("Issued getid() with parameter {}. Output: {}".format(sname, str(unamea[0]['id'])))
    return unamea[0]['id']

#
# Получить упоминание пользователя
#

def getmention(uid):
    unamee = vk.users.get(user_id=uid)[0]
    log("Issued getmention() with parameter {}. Output: {}".format(str(uid), "[id" + str(unamee["id"]) + "|" + unamee["first_name"] + " " + unamee["last_name"] + "]"))
    return "[id" + str(unamee["id"]) + "|" + unamee["first_name"] + " " + unamee["last_name"] + "]"

#
# Получить имя пользователя
#

def getname(uid):
    unamee = vk.users.get(user_id=uid)[0]
    return unamee["first_name"] + " " + unamee["last_name"]

#
# Деюниксировать время
#

def deunix(integer):
    return datetime.datetime.utcfromtimestamp(integer).strftime('%Y %m %d %H %M %S').split(" ")

def geocode(address):
    address = address.replace(" ", "+")
    json1 = convertjson(Get("https://nominatim.openstreetmap.org/search?q="+ address + "&format=geojson"))
    json2 = json1["features"][0]["geometry"]["coordinates"]
    f1 = json2[0]
    f2 = json2[1]
    json2 = [f2, f1]
    json3 = json1["features"][0]["properties"]["display_name"]
    json2.append(json3)
    return json2

def convertjson(jsond):
    return json.loads(jsond)

def translate(text, lang):
    result = translator.translate(text, dest = str(lang))
    return result.text

def voice(path):
    upload_url = vk.docs.getMessagesUploadServer(type="audio_message", peer_id=event.object["peer_id"])['upload_url']
    request = requests.post(upload_url, files={'file': open(path, 'rb')}).json()
    save = vk.docs.save(file=request['file'])['audio_message']
    d = 'doc' + str(save['owner_id']) + '_' + str(save['id'])
    vk.messages.send(peer_id=event.object["peer_id"], attachment=d, random_id=randd.randint(-2147483647, 2147483647), dont_parse_links=1)

def randomint(first, second):
    return randd.randint(first, second)

def succ():
    print("[ \033[92mok\033[0m ]")

def failcomplete():
    print("[\033[31mfail\033[0m]")

def warn(text):
    print("\\e[91m * \033[0m " + text + "...", end='\n')

def outproc(text):
    print("\033[94 * \033[0m " + text + "...", end="\n")

def procmsg(text):
    rows, columns = os.popen('stty size', 'r').read().split()
    intm = int(columns) - 13 - len(text)
    txt = " " * intm
    print("\033[94m>>>\033[0m " + text + "..." + txt, end="")

def pluswrite(text, target):
    file = open(str(target), 'a', encoding='utf-8')
    file.write(str(text))
    file.close()

def output(text): # Alternative to print()
    sys.stdout.write(str(text) + '\n')

def get(url): # A get requests
    try:
        return get(url).text
        log("Issued Get() with URL {}".format(url))
    except Exception as e:
        log("Error in Get(). " + str(e))
        return None

def shorturl(url):
    return Get("https://clck.ru/--?url=" + url)

def installpackage(text): # Install Python Package (PIP)
    a = CallSystem("pip install " + str(text) + ' --user')
    if 'error' not in str(a).lower():
        return 'success'
    else:
        return 'error'

def readff(file): # Read From File
    try:
        Ff = open(file, 'r', encoding='UTF-8')
        Contents = Ff.read()
        Ff.close()
        return Contents
    except:
        return None

def callsystem2(command):
    os.system(str(command))

def callsystem(command): # Call system shell
    return str(check_output(str(command), shell=False))

def run(file): # Run a Python script in isolator suqa
    exec(ReadFF(str(file)))

def runthread(id, method, args): # Run a any method in thread
    exec(str(id) + ' = Thread(' + str(method) + ', args=' + str(args))
    exec(str(id) + '.start()')

def convertint(uptime): # Converting seconds to verbal notation, by Catware & Catinka
    seconds = int(uptime);
    minutes = int(uptime / 60);
    hours = int(minutes / 60);
    days = int(hours / 24);
    hours = int(hours - days * 24);
    minutes = int(minutes - (hours * 60 + days * 24 * 60));
    return str(days) + ' дней ' + str(hours) + ' часов ' + str(minutes) + ' минут '

def download(url, fn): # Download a file from any URL
    f = open(fn, 'wb')
    f.write(get(url).content)
    f.close()
    log("Used Download().")

def infomsg(text): # INFO message
    print("[ info ] " + text)

def failmsg(text): # FAIL message
    print("[ fail ] " + text)

def okmsg(text): # OK message
    print("[ ok ] " + text)

def eventmsg(text): # EVENT message
    print("[ event ] " + text)

def similar(first, second): # Similar strings
    if not len(first) == len(second):
        return False
    if len(first) - sum(l1==l2 for l1, l2 in zip(first, second)) > 3:
        return False
    return True

def texttobits(text, encoding='utf-8', errors='surrogatepass'): # Text to 101010010100101
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def textfrombits(bits, encoding='utf-8', errors='surrogatepass'): # Text from 10101001010101
    try:
        n = int(bits, 2)
        return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'
    except Exception:
        return 'error'

def createfile(name): # Create a file
    k = name
    f = open(str(k), 'w')
    f.close()

#def Save(): # Save handle data
#    try:
#        config_file = open('config.txt', 'w')
#        config_file.write(str(tiki) + '\n')
#        config_file.write(str(zarplata) + '\n')
#        config_file.write(str(surrogate) + '\n')
#        config_file.write(str(pmsg) + '\n')
#        config_file.write(str(symbols) + '\n')
#        config_file.write(str(sendm))
#        config_file.close()
#    except Exception as e:
#        mta('Ошибка записи! ' + str(e) + '\n Аварийный выход!')
#        exit()

def reverse(s): # Reverse text (Text -> txeT)
    return s[::-1]

def vinpad(text): # Convert russian name to accusative
    if text.endswith('а'):
        text = text[:-1]
        text = text + 'у'
    if text.endswith('я'):
        text = text[:-1]
        text = text + 'ю'
    if text.endswith('й'):
        text = text[:-1]
        text = text + 'я'
    if text.endswith('к'):
        text = text + 'а'
    if text.endswith('ц'):
        text = text + 'а'
    if text.endswith('к'):
        text = text + 'а'
    if text.endswith('н'):
        text = text + 'а'
    if text.endswith('г'):
        text = text + 'а'
    if text.endswith('ш'):
        text = text + 'а'
    if text.endswith('щ'):
        text = text + 'а'
    if text.endswith('з'):
        text = text + 'а'
    if text.endswith('х'):
        text = text + 'а'
    if text.endswith('ф'):
        text = text + 'а'
    if text.endswith('ы'):
        text = text + 'ов'
    if text.endswith('в'):
        text = text + 'а'
    if text.endswith('п'):
        text = text + 'а'
    if text.endswith('р'):
        text = text + 'а'
    if text.endswith('о'):
        text = text[:-1]
        text = text + 'а'
    if text.endswith('л'):
        text = text + 'а'
    if text.endswith('д'):
        text = text + 'а'
    if text.endswith('ж'):
        text = text + 'а'
    if text.endswith('ч'):
        text = text + 'а'
    if text.endswith('с'):
        text = text + 'а'
    if text.endswith('м'):
        text = text + 'а'
    if text.endswith('т'):
        text = text + 'а'
    if text.endswith('ь'):
        text = text[:-1]
        text = text + 'я'
    if text.endswith('б'):
        text = text + 'а'
    return str(text)

def randomletter():
    letters = ['q', 'Q', 'w', 'W', 'e', 'E', 'r', 'R', 't', 'T', 'y', 'Y', 'u', 'U', 'i', 'I', 'o', 'O', 'p', 'P', 'a', 'A', 's', 'S', 'd', 'D', 'f', 'F', 'g', 'G', 'h', 'H', 'j', 'J', 'k', 'K', 'l', 'L', 'z', 'Z', 'x', 'X', 'c', 'C', 'v', 'V', 'b', 'B', 'n', 'N', 'm', 'M', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    return letters[randd.randint(0, len(letters)-1)]

def mta(text,noLinks=0):
    random_id = randd.randint(-2147483647, 2147483647)
    try:
        vk.messages.send(
            random_id=random_id,
            user_ids=admins,
            message=str(text)[:4000],
            dont_parse_links=1
            )
    except Exception as e:
        FailMsg('Не удалось вызвать MTA: ' + str(e))

def writeto(text, target):
    file = open(str(target), 'w', encoding='utf-8')
    file.write(str(text))
    file.close()

def message(text):
    text = str(text)
    random_id = randd.randint(-2147483647, 2147483647)
    global peer_id
    try:
        #if len(text) > 2000 and ReadFF("from.txt") == "chat":
        #    if "#testing" not in ReadFF('commands/' + ids[commands.index(x)] + '.py'):
        #        messagecust("Во избежание спама отправил результат работы в лс, for great justice!", ReadFF("peer_id.txt"))
        #if outputd == False:
        messagecust(str(text).replace("vto.pe", '').replace("vkbot.ru", '')[:4096], peer_id)
        #else:
        #    PlusWrite(str(text).replace("vto.pe", '').replace("vkbot.ru", '')[:4096], "usr/lastoutput.txt")
        #    else:
        #        if outputd == False:
        #            messagecust("Во избежание спама отправил результат работы в лс, for great justice!", ReadFF("peer_id.txt"))
        #            messagecust("Внимание: команда может нестабильно работать.\n\n" + str(text).replace("vto.pe", '').replace("vkbot.ru", '')[:4096], user_id)
        #        PlusWrite("Внимание: команда может нестабильно работать.\n\n" + str(text).replace("vto.pe", '').replace("vkbot.ru", '')[:4096], "usr/lastoutput.txt")
        #else:
        #    if "#testing" not in ReadFF('commands/' + ids[commands.index(x)] + '.py'):
        #        if outputd == False:
        #            messagecust(str(text).replace("vto.pe", '').replace("vkbot.ru", '')[:4096], peer_id)
        #        PlusWrite(str(text).replace("vto.pe", '').replace("vkbot.ru", '')[:4096], "usr/lastoutput.txt")
        #    else:
        #        if outputd == False:
        #            messagecust("Внимание: команда может нестабильно работать.\n\n" + str(text).replace("vto.pe", '').replace("vkbot.ru", '')[:4096], peer_id)
        #        PlusWrite("Внимание: команда может нестабильно работать.\n\n" + str(text).replace("vto.pe", '').replace("vkbot.ru", '')[:4096], "usr/lastoutput.txt")

    except Exception as e:
        #mta(e)
        pass

def picture(text, text2):
    random_id = randd.randint(-2147483647, 2147483647)
    pic = str(text)
    message("Loading...")
    try:
        try:
            attachments = []
            upload = VkUpload(vk_session)
            image_url = pic
            image = session.get(image_url, stream=True)
            photo = upload.photo_messages(photos=image.raw)[0]
            attachments.append(
                'photo{}_{}'.format(photo['owner_id'], photo['id'])
            )
            vk.messages.send(
            random_id=random_id,
            peer_id=ReadFF('peer_id.txt'),
            message=str(text2).replace("vto.pe", '').replace("vkbot.ru", '')[:4000],
            attachment=','.join(attachments),
                        dont_parse_links=1
            )
        except Exception:
            message(str(text2))
    except Exception as e:
        #mta(e)
        pass

def picturedata(text, text2):
    random_id = randd.randint(-2147483647, 2147483647)
    pic = str(text)
    message("Loading...")
    try:
        try:
            attachments = []
            upload = VkUpload(vk_session)
            photo = upload.photo_messages(photos=text)[0]
            attachments.append(
                'photo{}_{}'.format(photo['owner_id'], photo['id'])
            )
            vk.messages.send(
            random_id=random_id,
            peer_id=ReadFF('peer_id.txt'),
            message=str(text2).replace("vto.pe", '').replace("vkbot.ru", '')[:4000],
            attachment=','.join(attachments),
                        dont_parse_links=1
            )
        except Exception as e:
            message(str(text2 + '\n///' + str(e) + '///'))
    except Exception as e:
        message('picture error: ' + str(e))

def resize_image(input_image_path, output_image_path, size):
    try:
        original_image = Image.open(input_image_path)
        width, height = original_image.size
        resized_image = original_image.resize(size)
        width, height = resized_image.size
        resized_image.save(output_image_path)
        return "ok"
    except Exception as e:
        return str(e)

def quad_as_rect(quad):
    if quad[0] != quad[2]: return False
    if quad[1] != quad[7]: return False
    if quad[4] != quad[6]: return False
    if quad[3] != quad[5]: return False
    return True

def quad_to_rect(quad):
    assert(len(quad) == 8)
    assert(quad_as_rect(quad))
    return (quad[0], quad[1], quad[4], quad[3])

def rect_to_quad(rect):
    assert(len(rect) == 4)
    return (rect[0], rect[1], rect[0], rect[3], rect[2], rect[3], rect[2], rect[1])

def shape_to_rect(shape):
    assert(len(shape) == 2)
    return (0, 0, shape[0], shape[1])

def griddify(rect, w_div, h_div):
    w = rect[2] - rect[0]
    h = rect[3] - rect[1]
    x_step = w / float(w_div)
    y_step = h / float(h_div)
    y = rect[1]
    grid_vertex_matrix = []
    for _ in range(h_div + 1):
        grid_vertex_matrix.append([])
        x = rect[0]
        for _ in range(w_div + 1):
            grid_vertex_matrix[-1].append([int(x), int(y)])
            x += x_step
        y += y_step
    grid = np.array(grid_vertex_matrix)
    return grid

def distort_grid(org_grid, max_shift):
    new_grid = np.copy(org_grid)
    x_min = np.min(new_grid[:, :, 0])
    y_min = np.min(new_grid[:, :, 1])
    x_max = np.max(new_grid[:, :, 0])
    y_max = np.max(new_grid[:, :, 1])
    new_grid += np.random.randint(- max_shift, max_shift + 1, new_grid.shape)
    new_grid[:, :, 0] = np.maximum(x_min, new_grid[:, :, 0])
    new_grid[:, :, 1] = np.maximum(y_min, new_grid[:, :, 1])
    new_grid[:, :, 0] = np.minimum(x_max, new_grid[:, :, 0])
    new_grid[:, :, 1] = np.minimum(y_max, new_grid[:, :, 1])
    return new_grid

def grid_to_mesh(src_grid, dst_grid):
    assert(src_grid.shape == dst_grid.shape)
    mesh = []
    for i in range(src_grid.shape[0] - 1):
        for j in range(src_grid.shape[1] - 1):
            src_quad = [src_grid[i    , j    , 0], src_grid[i    , j    , 1],
                        src_grid[i + 1, j    , 0], src_grid[i + 1, j    , 1],
                        src_grid[i + 1, j + 1, 0], src_grid[i + 1, j + 1, 1],
                        src_grid[i    , j + 1, 0], src_grid[i    , j + 1, 1]]
            dst_quad = [dst_grid[i    , j    , 0], dst_grid[i    , j    , 1],
                        dst_grid[i + 1, j    , 0], dst_grid[i + 1, j    , 1],
                        dst_grid[i + 1, j + 1, 0], dst_grid[i + 1, j + 1, 1],
                        dst_grid[i    , j + 1, 0], dst_grid[i    , j + 1, 1]]
            dst_rect = quad_to_rect(dst_quad)
            mesh.append([dst_rect, src_quad])
    return mesh

import time
import datetime
#log("Initialized CatENV")
