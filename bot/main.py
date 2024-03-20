import telebot
from telebot import types
BOT_TOKEN = "6910054215:AAHEUpxHVOcVInq-EUoqo231cnrc9cpC9_s"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def handle_start(message):
    # Приветственное сообщение
    text = "<b>Привет!</b>\nВас приветствует команда <b>Международной группы компаний Адам Адал Жол и МБК Дуние</b>\n\nЗдесь вы сможете ознакомиться с продуктами, идеями и ценностями, которые транслирует и предоставляет наша группа компаний!"
    photo_path = "images/hello_photo.jpg"
    with open(photo_path, 'rb') as photo:
        bot.send_photo(message.chat.id, photo, caption=text, parse_mode='HTML')

    # Создаем блок навигации с кнопками
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('О Позитивном Планетарном Движении "Дуние"')
    itembtn2 = types.KeyboardButton('Ключевые принципы и ценности')
    itembtn3 = types.KeyboardButton('Наши инструменты')
    itembtn4 = types.KeyboardButton('Перспективы')
    itembtn5 = types.KeyboardButton('Будущее позитивного планетарного движения')
    itembtn6 = types.KeyboardButton('Контактные данные')
    itembtn7 = types.KeyboardButton('Юридический Каркас')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6)
    markup.add(itembtn7)  # последняя кнопка в отдельной строке
    # Отправляем блок навигации
    bot.send_message(message.chat.id, "Выберите интересующий вас раздел:", reply_markup=markup)



# Обработчик для кнопки "О Позитивном Планетарном Движении "Дуние""
@bot.message_handler(commands=['about'])

@bot.message_handler(func=lambda message: message.text == 'О Позитивном Планетарном Движении "Дуние"')
def handle_dunie(message):
    text = "<b>Первое позитивное планетарное движение</b>\n\nМБК «ДУНИЕ» является международной некоммерческой, членской, благотворительной организацией, созданной на добровольном объединении граждан, физических и/или юридических лиц на ОСНОВЕ чистоты, равенства, сохранности и защиты все вся всех всего, живых и не живых, всего человечества, животного мира, экологического оздоровления жизни и планеты, Благо-творения, Благо-человечности, Благо-человеческой семьи, Благо-живым и не живым, Благо-справедливости и всеобщего мира, Благо-созидательности, содействия и осуществления взаимодействия человечества, граждан, народов, населения, нации, всех государств и не государств, республик и не республик, монархии и не монархии, религиозных и не религиозных, конфессий и не конфессий, государственных и не государственных, сообществ, членств, организаций."
    photo_path = "images/about_dunie.jpg"
    with open(photo_path, 'rb') as photo:
        bot.send_photo(message.chat.id, photo, caption=text, parse_mode='HTML')


    file_path = "files/dunie.pdf"
    with open(file_path, 'rb') as photo:
        bot.send_document(message.chat.id, photo, caption="Презентация Дуние")


# Обработчик для кнопки "Ключевые принципы и ценности"
@bot.message_handler(commands=['principles'])
@bot.message_handler(func=lambda message: message.text == 'Ключевые принципы и ценности')
def handle_principles(message):
    
    text = '''<b>Солидарность</b>\n\nМы верим в солидарность и взаимопомощь, в общую ответственность перед будущим поколением и нашей планетой.\n\n<b>Справедливость</b>\n\nМы стремимся к созданию справедливого общества, где люди не будут ограничены неравенством, дискриминацией и эксплуатацией.\n\n<b>Инновации</b>\n\nМы ищем новые идеи и решения, чтобы преобразовать системы и процессы в более прорывные ноосферные, природоподобные, экологически устойчивые.\n\n<b>Исключим из жизни</b> \n\nБоль, страх, искажения. Имеем решения как прекратить войны, болезни, снять все долговое бремя кредитов по планете, как с государств, так и с человека.'''
    photo_path = 'images/principles.jpg'
    
    with open(photo_path, 'rb') as photo:
        bot.send_photo(message.chat.id, photo, caption=text, parse_mode='HTML')


# Обработчик для кнопки "Наши инструменты"
@bot.message_handler(commands=['cvb'])
@bot.message_handler(func=lambda message: message.text == 'Наши инструменты')
def handle_tools(message):
    text = "<b>CVB</b>\n\n<b>«Converted Virtual Balance» или «Конвертируемый Виртуальный Баланс»</b>\n\nЧто такое CVB и что он дает для всех всё вся всего, народа, человечества, государства, бизнеса и Вас самих?\n\nВо-первых, это программное обеспечение, которое дает возможность конвертировать любую валюту мира без привязки к любой бирже, без привязки к любому кросс курсу, без финансовых потерь.\n\nВо-вторых, это решение для всех секторов экономики и в жизни человека, в том числе по любым транзакциям.\n\n<b>Что даст CVB:</b>\n\nЭто снижение финансовой зависимости от внешних регуляторов, постепенный уход от внешних финансовых влияний, выход из разных долговых ям и обязательств, как и у самого государства, так и у человечества.\n\nИ еще - возможность иметь низкие устойчивые цены на все товары и услуги посредством оплаты через систему CVB.\n\n<b>Девиз продукта: Нет больше финансовых границ!</b>"
    bot.send_message(message.chat.id, text, parse_mode="HTML")
    
    
# Обработчик для кнопки "Перспективы"
@bot.message_handler(commands=['perspectives'])
@bot.message_handler(func=lambda message: message.text == 'Перспективы')
def perspectives(message):
    text = "<b>Перспективы</b>\n\nВсе доходы от работы платформы идут в строительство уникальных инновационных городов, где мир , спокойствие , справедливость , любовь , труд по предназначению и оплата благами по труду, доступ всем ко всем знаниям, теглубокое образование с малых лет без нагрузки, требований, искажений и тп.\n\nТакже доходы от работы платформы идут в создание в промышленных масштабах для всего населения мира самых современных, экологичных, прорывных и футуристических вещей бытового назначения,  медицины и питания - вот абсолютно все иное,  работающее во благо человека и его организма. Что приведет к включению механизмов регенерации и самовосстановления; омоложения и баланса внутри<b></b>"
    photo_path = 'images/perspectives.jpg'
    
    with open(photo_path, 'rb') as photo:
        bot.send_photo(message.chat.id, photo, caption=text, parse_mode='HTML')


# Обработчик для кнопки "Будущее позитивного планетарного движения"
@bot.message_handler(commands=['future'])
@bot.message_handler(func=lambda message: message.text == 'Будущее позитивного планетарного движения')
def handle_tools(message):
    bot.send_message(message.chat.id, "Вы выбрали раздел: Будущее позитивного планетарного движения")


# Обработчик для кнопки "Контактные данные"
@bot.message_handler(commands=['contacts'])
@bot.message_handler(func=lambda message: message.text == 'Контактные данные')
def handle_tools(message):
    text = "<b>Контактные данные</b>\n\n+7 963 722 22 60 WA, TG\n<a href='https://t.me/conso27'>Telegram</a>\n<a href='https://vk.com/dunie'>ВК</a>\n<a href='https://dzen.ru/id/65d73d810feeaa2ff60f0260'>Яндекс дзен</a>\n<a href='https://vc.ru/u/2959417-press-sluzhba-mbk-dunie'>VC ru</a>\n<a href='https://ibcdunie.livejournal.com/profile/?rfrom=mbkdunie'>LiveJournal</a>\n\n<a href='https://dunie.press'>Сайт Дуние</a>\n<a href='https://www.youtube.com/@Dunie-2024'>Youtube</a>\nEmail adamadalzhol@gmail.com\nEmail: 7928117@mail.ru"
    bot.send_message(message.chat.id, text, parse_mode="HTML")


# Обработчик для кнопки "Юридический Каркас"
@bot.message_handler(func=lambda message: message.text == 'Юридический Каркас')
def handle_tools(message):
    text = "<b>Юридический каркас</b>\n\nДвижение и дорожная карта проявлены юридическими лицами с единым уставом в рамках которого ведется вся деятельность по всей планете.\n\nНаши компании: МБК Дуние и ООО Адам Адал Жол представлены в Российской Федерации, Кыргызстане, Казахстане, Канаде, Индии, Турции. На данный момент идет процесс регистрации и выстраивания отношений в более чем 90 стран мира и в течении полугода наша группа компаний проявится во всех 251 странах.\n\nНаша группа компаний трудится во благо человечества, в том числе мы занимаемся образовательной, воспитательной и медицинской деятельностью F 0, социальными и строительными программами.\n\nГруппа компаний является заказчиком разнообразных программных продуктов. В том числе СѴВ выходит на рынок; платформа платформ на очереди. Затем будут и другие програмные продукты"
    bot.send_message(message.chat.id, text, parse_mode="HTML")





# @bot.message_handler(func=lambda message: True)
# def echo_message(message):
#     bot.reply_to(message, message.text)
    
bot.infinity_polling()