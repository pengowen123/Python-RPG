from random import randint
import time

class Char(object):
    def __init__(self, lvl):
        self.lvl = lvl
        self.hp = 60 + self.lvl * 5 + int(self.lvl ** 1.2) * int(self.lvl / 10.0)
        self.xp = 0
        self.gold = 0
        
        self.dmg_bonus = 1 + self.lvl**.4/12
    def calc_xp(self):
        xp_needed = 250
        xp_needed *= self.lvl / 10.0
        xp_needed += self.lvl ** 2.5
        xp_needed *= self.lvl / 45.0
        xp_needed += 250 + self.lvl * 50
        return int(xp_needed)
    def calc_hp(self):
        return 60 + self.lvl * 3 + int(self.lvl ** 1.6)
    def calc_dmg(self):
        return 1 + (self.lvl**.4/12)

char_read = open("character.txt", "r")
char_read_string = char_read.read()
stat_list = [int(s) for s in char_read_string.split(",")]

shop = []
char = Char(stat_list[0])
char.xp = stat_list[1]
char.xp_needed = char.calc_xp()
dungeon_level = stat_list[2]
char.gold = stat_list[3]
hp = char.hp
current_hp = char.hp
inventory = []
inventory_appender = []
inventory2 = []
inv_read = open("inventory.txt", "r")
inv_list = inv_read.read()

for item in inv_list:
    if (item != "," and item !=" " and item !="[" and item != "]"):
        item = int(item)
        inventory_appender.append(item)
    if len(inventory_appender) == 9:
        inventory.append(inventory_appender)
        inventory_appender = []
inv_read.close()

orc_img = ["|-----------|","|  _______  |","| / ^   ^ \ |","| |(o) (o)| |","| | -v-v- | |","| \_______/ |","|           |", "|-----------|"]
goblin_img = ["|-----------|","|  _______  |","| / () () \ |","| \   I   / |","|  \ ___ /  |","|   \___/   |","|           |","|-----------|"]
troll_img = ["|-----------|","|   _____   |","|  | 1 1 |  |","|  |  o  |  |","|  |  ^  |  |","|   \___/   |","|           |","|-----------|"]
ogre_img = ["|-----------|","|   _____   |","|  /     \  |","| / O   O \ |","| |   +   | |","| \ +---+ / |","|  \_____/  |","|           |","|-----------|"]
shop_img = ["|-----------|","|    ___    |","|   /   \   |","|  | | | |  |","|  [  ^  ]  |","|  |  v  |  |","|   \___/   |","|    | |    |","|-----------|"]
wyvern_img = ["|-----------|","|   \___/   |","|   |- -|   |","|   \ = /   |","| /\ \#/ /\ |","| \_\| |/_/ |","|   \   /   |","|-----------|"]
mage_img = ["|-----------|","|   _____   |","|  < o o >  |","|   \ * /   |","| *  \=/    |","| |__| |_   |","| | \   /\  |","|-----------|"]
dragon_small_img = ["|-----------|","| \>-----</ |","|  |0   0|  |","|_ \ (O) / _|","| \ \---/ / |","|\ \/\_/\/ /|","| \/\___/\/ |","|-----------|"]
dragon_img = ["|------------------------------|","|        |\          /|        |","|        | \________/ |        |","|        \            /        |","| __      \ (|)  (|) /      __ |","| \ \_     \   %%   /     _/ / |","|  \  \_    \  __  /    _/  /  |","|   \   \__/  ({})  \__/   /   |","|    |                    |    |","|     \___/--\    /--\___/     |","|            |    |            |","|------------------------------|"]

def print_img(name):
    for line in name:
        print line

print "Python RPG"
print "--------------------------------"
print_img(dragon_img)
time.sleep(1) 

class Item(object):
    def __init__(self, lvl):
        self.lvl = lvl
        self.random_dmg = randint(self.lvl / 7, self.lvl/3)
        if self.random_dmg > 99:
            self.random_dmg = 99
        self.dmg_ten = 0
        self.dmg_one = 0
        while self.dmg_ten < 9 and self.random_dmg >= 10:
            if self.random_dmg >= 10:
                self.dmg_ten += 1
                self.random_dmg -= 10
        while self.dmg_one < 9 and self.random_dmg >= 1:
            if self.random_dmg >= 1:
                self.dmg_one += 1
                self.random_dmg -= 1
        if self.lvl > 9999:
            self.lvl = 9999
        self.lvl_kilo = 0
        self.lvl_hun = 0
        self.lvl_ten = 0
        self.lvl_one = 0
        while self.lvl_kilo < 9 and self.lvl >= 1000:
            if self.lvl >= 1000:
                self.lvl_kilo += 1
                self.lvl -= 1000
        while self.lvl_hun < 9 and self.lvl >= 100:
            if self.lvl >= 100:
                self.lvl_hun += 1
                self.lvl -= 100
        while self.lvl_ten < 9 and self.lvl >= 10:
            if self.lvl >= 10:
                self.lvl_ten += 1
                self.lvl -= 10
        while self.lvl_one < 9 and self.lvl >= 1:
            if self.lvl >= 1:
                self.lvl_one += 1
                self.lvl -= 1
        self.quality = randint(1,7)
        self.type = randint(0,9)
        self.dmg_seed2 = randint(1,9)

    def __repr__(self):
        return [self.lvl_hun,self.lvl_ten, self.lvl_one, self.type, self.quality, self.dmg_ten, self.dmg_one, self.dmg_seed2, self.lvl_kilo]

class SeedItem(object):
    def __init__(self, lvl_hun, lvl_ten, lvl_one, type, quality, dmg_ten, dmg_one, dmg_seed2, lvl_kilo):
        self.dmg = 1
        self.lvl = (1000*lvl_kilo) + (100*lvl_hun)+(10*lvl_ten)+lvl_one
        self.type = type
        self.random_damage = dmg_ten * 10 + dmg_one
        self.quality = quality
        self.name = ""
        if self.type == 1:
            self.name = "stick"
            self.dmg = 1
        elif self.type == 2 or self.type == 3:
            self.name = "rock"
            self.dmg = 2
        elif self.type == 4:
            self.name = "club"
            self.dmg = 3
        elif self.type == 5 or self.type == 6:
            self.name = "knife"
            self.dmg = 4
        elif self.type == 7:
            self.name = "mace"
            self.dmg = 5
        elif self.type == 8:
            self.name = "sword"
            self.dmg = 7
        elif self.type == 9:
            self.name = "axe"
            self.dmg = 8
        elif self.type == 0:
            self.name = "morning star"
            self.dmg = 11
        self.dmg *= int(self.random_damage ** .3)
        self.dmg *= self.lvl ** .5
        self.dmg = int(self.dmg)
        self.dmg += dmg_seed2
        if self.quality == 1:
            self.name = "broken " + self.name
            self.dmg /= 2
        elif self.quality == 2:
            self.name = "blunt " + self.name
            self.dmg = int(self.dmg*.8)
        elif self.quality == 5:
            self.name = "sturdy " + self.name
            self.dmg += int(self.dmg*.15)
        elif self.quality == 6 and (self.type > 5 or self.type == 0):
            self.name = "sharpened " + self.name
            self.dmg = int(self.dmg * 1.4)
        elif self.quality == 7 and (self.type > 6 or self.type == 0):
            self.name = "razor-edged " + self.name
            self.dmg *= 2
    def __repr__(self):
        return "A level %s %s with %s to %s damage" % (self.lvl, self.name, int(self.dmg*.9), int(self.dmg*1.1))

def shop_item(dungeon_level):
    rand_lvl = randint(int(dungeon_level*.65), int(dungeon_level*.9))
    seed = Item(rand_lvl)
    a = seed.lvl_hun
    b = seed.lvl_ten
    c = seed.lvl_one
    d = seed.type
    e = seed.quality
    f = seed.dmg_ten
    g = seed.dmg_one
    h = seed.dmg_seed2
    t = seed.lvl_kilo
    item_seed = [a,b,c,d,e,f,g,h,t]
    random_gold = (75 + rand_lvl * 10 + randint(1,12)) * int(1 + rand_lvl ** .55) * (1 + seed.quality/2) + (seed.dmg_ten*10+seed.dmg_one) * 35
    shop_append = [item_seed, SeedItem(a,b,c,d,e,f,g,h,t), random_gold]
    shop.append(shop_append)

def create_shop(dungeon_level):
    global shop
    shop = []
    for x in range(5):
        shop_item(dungeon_level)

create_shop(dungeon_level)

inventory2 = []
def update_inventory(inventory):
    for item_ in inventory:
        seed_list = []
        for number in item_:
            seed_list.append(number)
        description_appender = SeedItem(seed_list[0],seed_list[1],seed_list[2],seed_list[3],seed_list[4],seed_list[5],seed_list[6],seed_list[7], seed_list[8])
        inventory2.append(description_appender)

update_inventory(inventory)

def create_item(lvl):
    seed = Item(lvl)
    a = seed.lvl_hun
    b = seed.lvl_ten
    c = seed.lvl_one
    d = seed.type
    e = seed.quality
    f = seed.dmg_ten
    g = seed.dmg_one
    h = seed.dmg_seed2
    t = seed.lvl_kilo
    inv_seed = [a,b,c,d,e,f,g,h,t]
    inventory.append(inv_seed)
    return SeedItem(a,b,c,d,e,f,g,h,t)

def print_inventory(inventory_desc):
    for x in range(0,len(inventory_desc)):
        print str(str(str(x) + ": " + str(inventory2[x])))
    select_item = raw_input("Type the number next to the item to use:")
    if int(select_item) <= len(inventory_desc):
        a = inventory[int(select_item)][0]
        b = inventory[int(select_item)][1]
        c = inventory[int(select_item)][2]
        d = inventory[int(select_item)][3]
        e = inventory[int(select_item)][4]
        f = inventory[int(select_item)][5]
        g = inventory[int(select_item)][6]
        h = inventory[int(select_item)][7]
        t = inventory[int(select_item)][8]
        print "Successfully switched to item in slot %s" % (select_item)
        global item_in_use
        item_in_use = SeedItem(a,b,c,d,e,f,g,h,t)
        print "------------------------------------------------------"
    else:
        print "That's not in your inventory"
        print_inventory(inventory2)

def print_inventory2(inventory_desc):
    for x in range(0,len(inventory_desc)):
        print str(str(str(x) + ": " + str(inventory2[x])))
    

class Monster(object):
    global dungeon_level
    
    def __init__(self, lvl):
        
        self.lvl = lvl
        if self.lvl < 1:
            self.lvl = 1
        monster_type = randint(1, 9)

        if monster_type == 1 or monster_type == 2:
            self.type = "goblin"
            self.hp = 10
            self.dmg = 4
        elif monster_type == 3 or monster_type == 4:
            self.type = "orc"
            self.hp = 14
            self.dmg = 6
        elif monster_type == 5:
            self.type = "wyvern"
            self.hp = 10
            self.dmg = 12
        elif monster_type == 6:
            self.type = "goblin mage"
            self.hp = 14
            self.dmg = 16
        elif monster_type == 7:
            self.type = "troll"
            self.hp = 20
            self.dmg = 10
        elif monster_type == 8:
            self.type = "ogre"
            self.hp = 30
            self.dmg = 18
        elif monster_type == 9:
            self.type = "dragon"
            self.hp = 45
            self.dmg = 25
            if self.lvl > 49 and randint(1,25) == 1:
                self.type = "elder dragon"
                self.hp = 80
                self.dmg = 50

        if dungeon_level < 8:
            new_type = randint(1,2)
            if new_type == 1:
                self.type = "goblin"
                self.hp = 10
                self.dmg = 4
            else:
                self.type = "orc"
                self.hp = 14
                self.dmg = 6

        elif dungeon_level < 16:
            new_type = randint(1,4)
            if new_type == 1:
                self.type = "goblin"
                self.hp = 10
                self.dmg = 4
            elif new_type == 2:
                self.type = "orc"
                self.hp = 14
                self.dmg = 6
            elif new_type == 3:
                self.type = "wyvern"
                self.hp = 10
                self.dmg = 12
            elif new_type == 2:
                self.type = "goblin mage"
                self.hp = 14
                self.dmg = 16

        if dungeon_level < 25:
            if self.type == "dragon":
                self.type == "wyvern"

        self.hp *= int(self.lvl ** .65) + 1
        self.hp += self.lvl * randint(6, 12)
        self.hp += randint(1, 9)
        self.hp += self.lvl ** 2 / 3
        monster_name = randint(1, 9)
        range_min = self.lvl / 10
        range_max = self.lvl/7
        if range_min > range_max:
            range_max += 2
        self.dmg += self.lvl / 4 * (randint(range_min, range_max))
        if monster_name == 1:
            self.name = "weak " + self.type
            self.hp = self.hp - self.lvl / 2
            self.dmg = self.dmg - int(self.lvl ** .5)
        elif monster_name == 2 or monster_name == 3:
            self.name = "" + self.type
        elif monster_name == 4 or monster_name == 5:
            self.name = "durable " + self.type
            self.hp = self.hp + self.lvl
            self.dmg += 4
        elif monster_name == 6:
            self.name = "tough " + self.type
            self.hp = self.hp + self.lvl/2
            self.dmg += self.lvl
        elif monster_name == 7:
            self.name = "powerful " + self.type
            self.hp = self.hp + self.lvl
            self.dmg += self.lvl
        elif monster_name == 8:
            self.name = "vicious " + self.type
            self.hp = self.hp + int(self.lvl*1.5)
            self.dmg *= 1+int((self.lvl/5)**.5)
        elif monster_name == 9:
            self.name = "legendary " + self.type
            self.hp *= int(self.lvl**.5)/2
            self.dmg *= int((self.lvl/3)**.5)
        self.monster_name = monster_name
        self.max_hp = self.hp
        
    def __repr__(self):
            return "Level %s %s with %s hp and %s to %s damage" % (self.lvl, self.name, self.hp, int(self.dmg*.9), int(self.dmg*1.1))

population = randint(1+int(dungeon_level**.25),2+int(dungeon_level**.5))

def attack_monster():
    global population
    global current_hp
    global item_in_use
    fight_action = raw_input("What to do? (auto, attack or run)")
    print "------------------------------------------------------"
    if fight_action == "auto":
        while new_monster.hp > item_in_use.dmg * 1.1 * char.dmg_bonus and current_hp > new_monster.dmg * 1.1:
            auto_attack()
        else:
            attack_monster()
    elif fight_action == "attack":
        random_hit2 = randint(int(new_monster.dmg*.9), int(new_monster.dmg * 1.1))
        current_hp -= random_hit2
        if current_hp < 1:
            print "You were killed by %s" % (new_monster.name)
            current_hp = char.hp
            char.gold = int(char.gold * .66)
            char.xp = int(char.xp * .66)
            town()
        else:
            print "The %s hit you for %s damage (%s to %s)" % (new_monster.name, random_hit2, current_hp + random_hit2, current_hp)
            print "------------------------------------------------------"
            random_hit = randint(int(item_in_use.dmg*.9),int(item_in_use.dmg*1.1))
            random_hit = int(random_hit * char.dmg_bonus)
            print "Attacked %s for %s damage (%s to %s)" % (new_monster.name, random_hit, new_monster.hp, new_monster.hp - random_hit)
            print "------------------------------------------------------"
            if new_monster.type == "goblin":
                print_img(goblin_img)
            elif new_monster.type == "orc":
                print_img(orc_img)
            elif new_monster.type == "troll":
                print_img(troll_img)
            elif new_monster.type == "ogre":
                print_img(ogre_img)
            elif new_monster.type == "wyvern":
                print_img(wyvern_img)
            elif new_monster.type == "goblin mage":
                print_img(mage_img)
            else:
                print_img(dragon_img)
            new_monster.hp -= random_hit
            if new_monster.hp < 1:
                print "You defeated the %s" % (new_monster.name)
                population -= 1
                item_drop_chance = randint(1, 3)
                global gold
                xp_given = randint(18,28) * new_monster.lvl + int((randint(3,5)/4) ** 2)
                char.xp += xp_given
                gold_given = randint(2,5) * new_monster.lvl + int(new_monster.lvl ** 1.2)
                char.gold += gold_given
                if "legendary" in new_monster.name:
                    char.xp += new_monster.lvl * 20
                    print "+ %s xp for killing a legendary monster" % (20*new_monster.lvl)
                if new_monster.type == "dragon":
                    char.xp += 15*new_monster.lvl + 5*new_monster.lvl
                    print "+ %s xp for killing a dragon" % (15*new_monster.lvl + 5*new_monster.lvl)
                char.xp += 2 * new_monster.dmg
                char.xp += new_monster.max_hp / 5
                while char.xp >= char.xp_needed:
                    char.xp_needed = char.calc_xp()
                    xp_carry_over = char.xp - char.xp_needed
                    char.xp = 0
                    char.xp += xp_carry_over
                    char.lvl += 1
                    char.xp_needed = char.calc_xp()
                    char.hp = char.calc_hp()
                    hp = char.hp
                    char.dmg_bonus = char.calc_dmg()
                    print "You leveled up to level %s" % (char.lvl)
                if item_drop_chance == 1:
                    random_lvl = randint(1+new_monster.lvl/2,1+new_monster.lvl)
                    if new_monster.lvl < 2 and random_lvl > 1:
                        random_lvl = -1
                    new_item = create_item(random_lvl)
                    inventory2.append(new_item)
                    print "You found: " + str(new_item)
                print "You gained %s xp (%s needed to level up)" % (xp_given, char.xp_needed - char.xp)
                print "You found %s gold" % (gold_given)
                print "------------------------------------------------------"
                print "Monsters remaining: " + str(population)
                fight()
            else:
                attack_monster()
    elif fight_action == "run":
        if new_monster.type == "goblin":
            print_img(goblin_img)
        elif new_monster.type == "orc":
            print_img(orc_img)
        elif new_monster.type == "troll":
            print_img(troll_img)
        elif new_monster.type == "ogre":
            print_img(ogre_img)
        elif new_monster.type == "wyvern":
            print_img(wyvern_img)
        elif new_monster.type == "goblin mage":
            print_img(mage_img)
        else:
            print_img(dragon_img)
        chance_to_escape = randint(1,3)
        time.sleep(1)
        if chance_to_escape == 1:
            print "You have escaped the %s" % (new_monster.name)
            town()
        else:
            print "You failed to escape!"
            current_hp = current_hp - new_monster.dmg
            print "The %s hit you for %s damage (%s to %s)" % (new_monster.name, new_monster.dmg, current_hp + new_monster.dmg, current_hp)
            if current_hp > 0:
                attack_monster()
            else:
                print "You were killed by %s" % (new_monster.name)
                current_hp = char.hp
                char.gold = int(char.gold * .66)
                char.xp = int(char.xp * .66)
                town()
                
    else:
        print "Invalid input"
        attack_monster()

def auto_attack():
    time.sleep(.25)
    global current_hp, item_in_use
    random_hit2 = randint(int(new_monster.dmg*.9), int(new_monster.dmg * 1.1))
    current_hp -= random_hit2
    try:
        item_in_use = item_in_use
    except Exception:
        print_inventory(inventory2)
    if True:
        print "The %s hit you for %s damage (%s to %s)" % (new_monster.name, random_hit2, current_hp + random_hit2, current_hp)
        print "------------------------------------------------------"
        random_hit = randint(int(item_in_use.dmg*.9),int(item_in_use.dmg*1.1))
        random_hit = int(random_hit * char.dmg_bonus)
        print "Attacked %s for %s damage (%s to %s)" % (new_monster.name, random_hit, new_monster.hp, new_monster.hp - random_hit)
        print "------------------------------------------------------"
        new_monster.hp -= random_hit
        if new_monster.hp < 1:
            print "You defeated the %s" % (new_monster.name)
            population -= 1
            item_drop_chance = randint(1, 3)
            global gold
            xp_given = randint(20,30) * new_monster.lvl + int((randint(3,7)/4) ** 2)
            char.xp += xp_given
            gold_given = randint(7,15) * new_monster.lvl + int(new_monster.lvl ** 1.2)
            char.gold += gold_given
            if "legendary" in new_monster.name:
                char.xp += new_monster.lvl * 20
                print "+ %s xp for killing a legendary monster" % (20*new_monster.lvl)
            if new_monster.type == "dragon":
                char.xp += 15*new_monster.lvl + 5*new_monster.lvl
                print "+ %s xp for killing a dragon" % (15*new_monster.lvl + 5*new_monster.lvl)
            char.xp += 2 * new_monster.dmg
            char.xp += new_monster.max_hp / 5
            while char.xp >= char.xp_needed:
                char.xp_needed = char.calc_xp()
                xp_carry_over = char.xp - char.xp_needed
                char.xp = 0
                char.xp += xp_carry_over
                char.lvl += 1
                char.xp_needed = char.calc_xp()
                char.hp = char.calc_hp()
                hp = char.hp
                char.dmg_bonus = char.calc_dmg()
                print "You leveled up to level %s" % (char.lvl)
            if item_drop_chance == 1:
                random_lvl = randint(1+new_monster.lvl/2,1+new_monster.lvl)
                if new_monster.lvl < 2 and random_lvl > 1:
                    random_lvl = -1
                new_item = create_item(random_lvl)
                inventory2.append(new_item)
                print "You found: " + str(new_item)
            print "You gained %s xp (%s needed to level up)" % (xp_given, char.xp_needed - char.xp)
            print "You found %s gold" % (gold_given)
            print "------------------------------------------------------"
            print "Monsters remaining: " + str(population)
            fight()

def next_level():
    next_level_cancel = raw_input("Do you wish to continue to the next level? (yes or no)")
    if next_level_cancel == "yes":
        global dungeon_level
        global population
        dungeon_level += 1
        population = randint(1+int(dungeon_level**.25),2+int(dungeon_level**.4))
        create_shop(dungeon_level)
        fight()
    else:
        town()

def fight():
    global item_in_use
    global dungeon_level
    if len(inventory) < 1:
        free_item = create_item(1)
        inventory2.append(free_item)
    try:
        item_in_use = item_in_use
    except Exception:
        print " "
        print "Select an item to use"
        print " "
        print_inventory(inventory2)
    
    global new_monster
    if population == 0:
        print "------------------------------------------------------"
        print "You have made it to dungeon level %s" % (dungeon_level+1)
        next_level()
    if population > 0:
        variance = randint(-2,2)
        if dungeon_level < 2:
            variance = 0
        new_monster = Monster(int(dungeon_level + variance))
        if new_monster.type == "goblin":
            print_img(goblin_img)
        elif new_monster.type == "orc":
            print_img(orc_img)
        elif new_monster.type == "troll":
            print_img(troll_img)
        elif new_monster.type == "ogre":
            print_img(ogre_img)
        elif new_monster.type == "wyvern":
            print_img(wyvern_img)
        elif new_monster.type == "goblin mage":
            print_img(mage_img)
        else:
            print_img(dragon_img)
        print "You ran into a: " + str(new_monster) + "!"
        attack_monster()

population = randint(1+int(dungeon_level**.25),2+int(dungeon_level**.35))

def save():
    inv_write = open("inventory.txt", "w")
    inv_write.write(str(inventory))
    inv_write.close()

    char_save = open("character.txt", "w")
    char_save.write(str(char.lvl) + "," + str(char.xp) + "," + str(dungeon_level) + "," + str(char.gold))
    char_save.close()

def print_shop(shop_list):
    global inventory
    global dungeon_level
    print "------------------------------------------------------"
    print "Welcome to the shop!"
    print_img(shop_img)
    print "------------------------------------------------------"
    shop_action = raw_input("What will you do at the shop? (buy, sell, enchant, or leave)")
    print "------------------------------------------------------"
    if shop_action == "buy":
        print "Here are today's items:"
        for x in range(len(shop_list)):
            print str(x) + ": " + str(shop_list[x][1]) + " for " + str([shop_list[x][2]]) + " gold"
        shop_buy = raw_input("Type the number next to the item you want to buy, or type cancel")
        if shop_buy == "cancel":
            print_shop(shop)
        else:
            if char.gold >= shop_list[int(shop_buy)][2]:
                char.gold -= shop_list[int(shop_buy)][2]
                print "Item added to inventory"
                inventory.append(shop_list[int(shop_buy)][0])
                global inventory2
                inventory2 = []
                update_inventory(inventory)
                del shop_list[int(shop_buy)]
                shop_item(dungeon_level)
                print_shop(shop)
            else:
                print "Not enough gold (need %s more)" % (shop_list[int(shop_buy)][2] - char.gold)
                print_shop(shop)
    elif shop_action == "sell":
        if len(inventory) > 0:
            for x in range(0,len(inventory)):
                print str(x) + " " + str(inventory2[x]) + " for " + str(int(inventory2[x].lvl*7 * int(1 + inventory2[x].dmg ** .2))) + " gold"
            del_item = raw_input("Type the number next to the item to sell, or type cancel")
            if del_item == "cancel":
                print_shop(shop)
            else:
                char.gold += inventory2[int(del_item)].lvl * 7 * int(1 + inventory2[int(x)].dmg ** .2)
                print "------------------------------------------------------"
                print "Item sold for %s gold" % (inventory2[int(del_item)].lvl * 7 * int(1 + inventory2[int(del_item)].dmg ** .2))
                del inventory[int(del_item)]
                del inventory2[int(del_item)]
                print_shop(shop)
        else:
            print "There are no items to sell"
            print_shop(shop)
    elif shop_action == "enchant":
        if len(inventory) > 0:
            print "Enchanting rerolls all properties of an item except for item level"
            print "------------------------------------------------------"
            for x in range(0,len(inventory)):
                print str(x) + " " + str(inventory2[x]) + " for " + str(int(inventory2[x].lvl*15 + (1.1 ** inventory2[x].lvl))/2) + " gold"
            ench_item = raw_input("Type the number next to the item to enchant, or type cancel")
            if ench_item == "cancel":
                print_shop(shop)
            else:
                enchant_cost = int(inventory2[x].lvl*15 + (1.1 ** inventory2[x].lvl)/2)
                if char.gold >= enchant_cost:
                    char.gold -= enchant_cost
                    enchant_lvl = inventory2[int(ench_item)].lvl
                    print enchant_lvl
                    del inventory2[int(ench_item)]
                    del inventory[int(ench_item)]
                    enchanted_item = create_item(enchant_lvl)
                    inventory2.append(enchanted_item)
                    print "Enchanted item: " + str(enchanted_item)
                    print_shop(shop)
                else:
                    print "Not enough gold (need %s more)" % (enchant_cost - char.gold)
                    print_shop(shop)
        else:
            print "There are no items to enchant"
            print_shop(shop)
    else:
        town()

def train(dungeon_level):
    if len(inventory) == 0:
        free_item = create_item(2)
        inventory2.append(free_item)
    print_inventory(inventory2)
    global current_hp
    train_level = 1+int(dungeon_level**.7)+randint(1,1+dungeon_level/4)
    train_monster = Monster(train_level)
    if train_monster.type == "goblin":
        print_img(goblin_img)
    elif train_monster.type == "orc":
        print_img(orc_img)
    elif train_monster.type == "troll":
        print_img(troll_img)
    elif train_monster.type == "ogre":
        print_img(ogre_img)
    elif train_monster.type == "goblin mage":
        print_img(mage_img)
    elif train_monster.type == "wyvern":
        print_img(wyvern_img)
    elif train_monster.type == "dragon":
        print_img(dragon_img)
    
    print "------------------------------------------------------"
    print "You will be matched against a %s for training" % (train_monster)
    while 1 > 0:
        if current_hp < 1:
            print "You were defeated by your opponent!"
            print "------------------------------------------------------"
            current_hp = char.hp
            char.xp += 15
            town()
            break
        elif train_monster.hp < 1:
            char.xp += train_monster.lvl * 15
            char.gold += 5 + train_monster.lvl * 3
            print "You defeated your opponent and gained %s xp and %s gold!" % (train_monster.lvl * 15, 5 + train_monster.lvl * 3)
            print "------------------------------------------------------"
            while char.xp >= char.xp_needed:
                    char.xp_needed = char.calc_xp()
                    xp_carry_over = char.xp - char.xp_needed
                    char.xp = 0
                    char.xp += xp_carry_over
                    char.lvl += 1
                    char.xp_needed = char.calc_xp()
                    char.hp = char.calc_hp()
                    hp = char.hp
                    print "You leveled up to level %s" % (char.lvl)
            town()
            break
        else:
            current_hp -= train_monster.dmg
            train_monster.hp -= int(item_in_use.dmg * char.dmg_bonus)
            time.sleep(.5)

def town():
    print "------------------------------------------------------"
    print "Welcome to town!"
    print "------------------------------------------------------"
    global current_hp
    current_hp = char.hp
    if char.dmg_bonus < 1.1:
        dmg_bonus = str(char.dmg_bonus)[3:4]
    else:
        dmg_bonus = str(char.dmg_bonus)[2:4]
    print "Stats:"
    print "HP: " + str(current_hp) + " / " + str(char.hp)
    print "LVL: " + str(char.lvl)
    print "DMG BONUS: " + dmg_bonus + "%"
    print "XP: " + str(char.xp) + " / " + str(char.xp_needed)
    print "GOLD: " + str(char.gold)
    print "DUNGEON: "+  str(dungeon_level)
    print "------------------------------------------------------"
    area = raw_input("Where do you go? (dungeon, train, shop, inventory, save)")
    if area == "dungeon":
        fight()
    elif area == "shop":
        print_shop(shop)
    elif area == "train":
        train(dungeon_level)
    elif area == "save":
        print "Character lvl, dungeon, inventory, gold, and xp are saved. Type \"town()\" to continue playing."
        save()
    elif area == "inventory":
        print_inventory(inventory2)
        town()
    else:
        print "Invalid input"
        town()

town()

save()
