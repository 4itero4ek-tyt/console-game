import time


inventory = []
safe_zone_coords = (10, 5)

items_description = {
    "нож": "Старый ржавый нож — пригодится для самообороны.",
    "ключ": "Металлический ключ. Возможно, откроет дверь в подвал.",
    "аптечка": "Аптечка первой помощи. Восстанавливает силы.",
    "камень": "Простой камень. Можно отвлечь внимание зомби шумом.",
    "батарейка": "Старая батарейка. Может питать фонарь или радиоприёмник.",
    "карта": "Карта города с отмеченным убежищем.",
}


def pause(text):
    """Красивый вывод текста с задержкой"""
    print(text)
    time.sleep(1.3)

def show_inventory():
    """Показывает какие предметы в рюкзаке"""
    
    if inventory:
        print("\n🎒 В твоём рюкзаке:", ", ".join(inventory))
    else:
        print("\n🎒 Рюкзак пуст.")

def describe_item(item):
    """Вывод описание предмета"""

    if item in items_description:
        print(f"📘 {items_description[item]}")


def level_one():
    """Уровень 1 — побег из города"""

    pause("\n*** УРОВЕНЬ 1: ПОБЕГ ИЗ ГОРОДА ***")
    pause("Ты просыпаешься в заброшенной квартире. Снаружи слышны стоны зомби...")
    pause("Перед тобой лежат предметы: нож, аптечка, камень, карта.")
    
    objects = ["нож", "аптечка", "камень", "карта"]
    
    while True:
        action = input("\nЧто сделать? (взять [предмет] / выйти): ").lower()
        if action.startswith("взять"):
            item = action.replace("взять ", "").strip()
            if item in objects:
                inventory.append(item)
                pause(f"Ты взял предмет: {item}.")
                describe_item(item)
                objects.remove(item)
            else:
                print("Такого предмета здесь нет.")
        elif action == "выйти":
            pause("Ты осторожно выглядываешь в окно...")
            break
        else:
            print("Неизвестная команда.")
    
    if "нож" in inventory:
        pause("Ты отбиваешься ножом и убегаешь в сторону выживших!")
        pause("Ты добрался до безопасного дома.")
    else:
        pause("Ты безоружен... зомби тебя догоняет!")
        pause("Конец игры — попробуй снова.")
        exit()
    if "карта" not in inventory:
        pause("Ты выбегаешь из дома, но не знаешь дороги. Улицы переполнены зомби.")
        pause("Ты бежишь куда попало... теряешь силы и падаешь без сознания.")
        pause("Без карты ты заблудился. Конец игры.")
        exit()
    else:
        pause("Благодаря карте ты находишь безопасный маршрут к подвалу выживших!")
        pause(f"На карте указано убежище по координатам: {safe_zone_coords}.")
        pause("Ты осторожно направляешься туда...")


def level_two():
    """Уровень 2 — подвал выживших"""
    pause("\n*** УРОВЕНЬ 2: ПОДВАЛ ВЫЖИВШИХ ***")
    pause("Ты находишь вход в подвал, но внутри темнота.")
    pause("Ты видишь у входа несколько предметов: батарейка, фонарь.")
    
    items = ["батарейка", "фонарь"]
    key_found = False
    light_on = False
    
    while True:
        show_inventory()
        action = input("\nЧто сделать? (взять [предмет] / использовать [предмет]): ").lower()
        
        # Взятие предметов
        if action.startswith("взять"):
            item = action.replace("взять ", "").strip()
            if item in items:
                inventory.append(item)
                pause(f"Ты подобрал {item}.")
                describe_item(item)
                items.remove(item)
            else:
                print("Такого предмета здесь нет.")
        
        # Использование предметов
        elif action.startswith("использовать"):
            item = action.replace("использовать ", "").strip()
            
            if item == "фонарь" in inventory:
                if "батарейка" in inventory:
                    pause("Ты вставляешь батарейку в фонарь... свет вспыхивает! Теперь видно в подвале.")
                    light_on = True
                    pause("На полу ты замечаешь металлический блеск — это ключ!")
                    if not key_found:
                        inventory.append("ключ")
                        describe_item("ключ")
                        key_found = True
                else:
                    pause("Фонарь не работает — нужна батарейка.")
            
            elif item == "ключ" and "ключ" in inventory:
                if light_on:
                    pause("Ты вставляешь ключ в замок... щелчок! Дверь открыта.")
                    break
                else:
                    pause("Слишком темно, ты не можешь найти замок.")
            
            else:
                print("Этот предмет нельзя использовать здесь.")
        
        else:
            print("Команда не распознана.")
    
    pause("Ты входишь в комнату... внутри запас еды и оружие!")
    pause("Ты выжил! Поздравляем, ты прошёл два уровня игры!")
    show_inventory()
    pause("\nКонец игры.")



def start_game():
    pause("🧟 Добро пожаловать в игру 'Выжить после Зомби-Апокалипсиса'!")
    pause("Твоя цель — выбраться из заражённого города и выжить любой ценой.")
    name = input("\nКак тебя зовут, выживший? ").title()
    pause(f"Удачи тебе, {name}... Пусть удача будет на твоей стороне.")
    
    level_one()
    level_two()

if __name__ == "__main__":
    start_game()
