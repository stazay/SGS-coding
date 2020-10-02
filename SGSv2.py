"""
    __________   ___     ____    ___  __________  ___    ___  __________  __________   ___   ___  ___      ___
   / _______//  / ||    /   ||  / // / _______// / //   / // / _____  // / _______//  / //  / // / ||     / //
  / //_______  /  ||   / /| || / // / // ____   / //   / // / //   / // / //_______  / //__/ // /  ||    / //
 /_______  // / ` ||  / //| ||/ // / // /_  // / //   / // / //   / // /_______  // / ____  // / ` ||   /_//
 _______/ // / /| || / // | |/ // / //___/ // / //___/ // / //___/ //  _______/ // / //  / // / /| ||  ___
/________// /_//|_||/_//  |___// /________// /________// /________//  /________// /_//  /_// /_//| || /_//
                                SanGuoSha Coding by Saba Tazayoni               /||______________| ||
                    Started: 21/07/2020                                        /___________________||
Current Version: 01/10/2020
"""

from __future__ import print_function, unicode_literals
import random
from PyInquirer import prompt, Separator
from examples import custom_style_2


# Determine the number of players and roles
def number_of_players():
    question = [
        {
            'type': 'list',
            'name': 'Number of Players',
            'message': 'Please decide how many players will be playing:',
            'choices': ['3', '4', '5', '6', '7', '8', '9', '10'],
        },
    ]

    answer = prompt(question, style=custom_style_2)
    return int(answer.get('Number of Players'))


def format_six_players():
    question = [
        {
            'type': 'list',
            'name': 'Format with Six Players',
            'message': 'Please decide how you would like the roles to be distributed:',
            'choices': [
                '{"Emperor": 1, "Advisor": 1, "Rebel": 3, "Spy": 1}',
                '{"Emperor": 1, "Advisor": 1, "Rebel": 2, "Spy": 2}',
                '{Random & hidden choice of above options}',
            ],
        },
    ]

    answer = prompt(question, style=custom_style_2)
    return (answer.get('Format with Six Players'))


def format_eight_players():
    question = [
        {
            'type': 'list',
            'name': 'Format with Eight Players',
            'message': 'Please decide how you would like the roles to be distributed:',
            'choices': [
                '{"Emperor": 1, "Advisor": 2, "Rebel": 4, "Spy": 1}',
                '{"Emperor": 1, "Advisor": 2, "Rebel": 3, "Spy": 2}',
                '{Random & hidden choice of above options}',
            ],
        },
    ]

    answer = prompt(question, style=custom_style_2)
    return (answer.get('Format with Eight Players'))


def generate_roles_dictionary():
    number_of_players_output = number_of_players()
    if number_of_players_output == 3:
        roles_dictionary = {"Emperor": 1, "Advisor": 0, "Rebel": 1, "Spy": 1}
    if number_of_players_output == 4:
        roles_dictionary = {"Emperor": 1, "Advisor": 1, "Rebel": 1, "Spy": 1}
    if number_of_players_output == 5:
        roles_dictionary = {"Emperor": 1, "Advisor": 1, "Rebel": 2, "Spy": 1}
    if number_of_players_output == 6:
        answer = format_six_players()
        if answer == '{"Emperor": 1, "Advisor": 1, "Rebel": 3, "Spy": 1}':
            roles_dictionary = {"Emperor": 1,
                                "Advisor": 1, "Rebel": 3, "Spy": 1}
        if answer == '{"Emperor": 1, "Advisor": 1, "Rebel": 2, "Spy": 2}':
            roles_dictionary = {"Emperor": 1,
                                "Advisor": 1, "Rebel": 2, "Spy": 2}
        if answer == '{Random & hidden choice of above options}':
            list_for_random = [{"Emperor": 1, "Advisor": 1, "Rebel": 3, "Spy": 1}, {
                "Emperor": 1, "Advisor": 1, "Rebel": 2, "Spy": 2}]
            random.shuffle(list_for_random)
            roles_dictionary = list_for_random.pop()
    if number_of_players_output == 7:
        roles_dictionary = {"Emperor": 1, "Advisor": 2, "Rebel": 3, "Spy": 1}
    if number_of_players_output == 8:
        answer = format_eight_players()
        if answer == '{"Emperor": 1, "Advisor": 2, "Rebel": 4, "Spy": 1}':
            roles_dictionary = {"Emperor": 1,
                                "Advisor": 2, "Rebel": 4, "Spy": 1}
        if answer == '{"Emperor": 1, "Advisor": 2, "Rebel": 3, "Spy": 2}':
            roles_dictionary = {"Emperor": 1,
                                "Advisor": 2, "Rebel": 3, "Spy": 2}
        if answer == '{Random & hidden choice of above options}':
            list_for_random = [{"Emperor": 1, "Advisor": 2, "Rebel": 4, "Spy": 1}, {
                "Emperor": 1, "Advisor": 2, "Rebel": 3, "Spy": 2}]
            random.shuffle(list_for_random)
            roles_dictionary = list_for_random.pop()
    if number_of_players_output == 9:
        roles_dictionary = {"Emperor": 1, "Advisor": 3, "Rebel": 4, "Spy": 1}
    if number_of_players_output == 10:
        roles_dictionary = {"Emperor": 1, "Advisor": 3, "Rebel": 4, "Spy": 2}
    return (number_of_players_output, roles_dictionary)


def roles_to_list(roles_dictionary):
    roles_list = []
    for key in roles_dictionary.keys():
        for item in range(0, roles_dictionary[key]):
            roles_list.append(key)
    return roles_list


def roles_from_list(roles_list):
    role = roles_list.pop()
    return role


# Select Character-Picking Mode
def picking_format():
    question = [
        {
            'type': 'list',
            'name': 'Picking Format',
            'message': 'Please decide how characters will be selected:',
            'choices': [
                'All-Pick',
                'Banning-Pick',
                'Draft-Pick',
                'All-Random',
            ],
        },
    ]

    answer = prompt(question, style=custom_style_2)
    return (answer.get('Picking Format'))


# Game Setup Loop
def setup_confirmation():
    question = [
        {
            'type': 'list',
            'name': 'Setup confirmation',
            'message': 'Please confirm if the above settings are correct?',
            'choices': [
                'Yes',
                'No',
            ],
        },
    ]

    answer = prompt(question, style=custom_style_2)
    return (answer.get('Setup confirmation'))


def setup_loop():
    print(' ')
    (number_of_players_output, roles_dictionary) = generate_roles_dictionary()
    roles_list = roles_to_list(roles_dictionary)
    picking_format_output = picking_format()
    setup_confirmation_output = setup_confirmation()
    if setup_confirmation_output == 'Yes':
        return [number_of_players_output, roles_dictionary, roles_list, picking_format_output]
    else:
        return setup_loop()


# Players and win-conditions
def generate_players():
    players = [Player(roles_from_list(roles_list))
               for player_number in range(number_of_players_output)]
    return players


def player_assignment():
    if picking_format_output == "All-Pick":
        print("---------------")
        print("!Picking Phase!")
        print("---------------")
        for player in players:
            player.assign_character_all_pick()
        for card in all_character_cards.contents:
            character_card_discard_pile.add_to_top(card)
        character_card_discard_pile.shuffle()
    if picking_format_output == "Banning-Pick":
        print("---------------")
        print("Banning Phase 1")
        print("---------------")
        for player in players[::-1]:
            player.banning_pick_characters()
        print("---------------")
        print("Banning Phase 2")
        print("---------------")
        for player in players[::-1]:
            player.banning_pick_characters()
        print("---------------")
        print("!Picking Phase!")
        print("---------------")
        for player in players:
            player.assign_character_all_pick()
        for card in all_character_cards.contents:
            character_card_discard_pile.add_to_top(card)
        character_card_discard_pile.shuffle()
    if picking_format_output == "Draft-Pick":
        shu_emperor_cards.shuffle()
        wei_emperor_cards.shuffle()
        wu_emperor_cards.shuffle()
        hero_emperor_cards.shuffle()
        shu_character_cards.shuffle()
        wei_character_cards.shuffle()
        wu_character_cards.shuffle()
        hero_character_cards.shuffle()
        for player in players:
            player.assign_character_single_draft()
        for card in shu_emperor_cards.contents:
            character_card_discard_pile.add_to_top(card)
        for card in wei_emperor_cards.contents:
            character_card_discard_pile.add_to_top(card)
        for card in wu_emperor_cards.contents:
            character_card_discard_pile.add_to_top(card)
        for card in hero_emperor_cards.contents:
            character_card_discard_pile.add_to_top(card)
        for card in shu_character_cards.contents:
            character_card_discard_pile.add_to_top(card)
        for card in wei_character_cards.contents:
            character_card_discard_pile.add_to_top(card)
        for card in wu_character_cards.contents:
            character_card_discard_pile.add_to_top(card)
        for card in hero_character_cards.contents:
            character_card_discard_pile.add_to_top(card)
        character_card_discard_pile.shuffle()
    if picking_format_output == "All-Random":
        all_character_cards.shuffle()
        for player in players:
            player.assign_character_all_random()
        for card in all_character_cards.contents:
            character_card_discard_pile.add_to_top(card)
        character_card_discard_pile.shuffle()


def check_win_conditions():
    global game_started
    if roles_dictionary["Emperor"] == 1 and roles_dictionary["Rebel"] == 0 and roles_dictionary["Spy"] == 0:
        print("Emperor and Advisor(s) win:")
        for player in players_at_start:
            if player.role == "Emperor" or player.role == "Advisor":
                print(player)
        game_started = False
    elif roles_dictionary["Spy"] == 1 and roles_dictionary["Emperor"] == 0 and roles_dictionary["Advisor"] == 0 and roles_dictionary["Rebel"] == 0:
        print("Spy wins:")
        for player in players:
            if player.role == "Spy":
                print(player)
        game_started = False
    elif roles_dictionary["Emperor"] == 0:
        print("Rebel(s) win:")
        for player in players_at_start:
            if player.role == "Rebel":
                print(player)
        game_started = False


# Loose functions
def question_yes_no(message):
    question = [
        {
            'type': 'list',
            'name': 'Selected',
            'message': message,
            'choices': ['Yes', 'No'],
        },
    ]
    answer = prompt(question, style=custom_style_2)
    if answer.get('Selected') == 'Yes':
        return True


def get_emperors_for_single_draft(self):
    options = [shu_emperor_cards.contents.pop(), wei_emperor_cards.contents.pop(
    ), wu_emperor_cards.contents.pop(), hero_emperor_cards.contents.pop()]
    return options


def get_options_for_single_draft(self):
    options = [shu_character_cards.contents.pop(), wei_character_cards.contents.pop(
    ), wu_character_cards.contents.pop(), hero_character_cards.contents.pop()]
    return options


def list_character_options(options):
    return [str(option) for option in options]


def ability_formatting(self):
    if (self.character_ability5 == "None") and (self.character_ability4 == "None") and (self.character_ability3 == "None") and (self.character_ability2 == "None"):
        return f"   - {self.character_ability1}"
    elif (self.character_ability5 == "None") and (self.character_ability4 == "None") and (self.character_ability3 == "None"):
        return f"   - {self.character_ability1} \n   - {self.character_ability2}"
    elif (self.character_ability5 == "None") and (self.character_ability4 == "None"):
        return f"   - {self.character_ability1} \n   - {self.character_ability2} \n   - {self.character_ability3}"
    elif (self.character_ability5 == "None"):
        return f"   - {self.character_ability1} \n   - {self.character_ability2} \n   - {self.character_ability3} \n   - {self.character_ability4}"
    else:
        return f"   - {self.character_ability1} \n   - {self.character_ability2} \n   - {self.character_ability3} \n   - {self.character_ability4} \n   - {self.character_ability5}"


def check_allegiances_in_play():
    allegiances = []
    for player in players:
        allegiances.append(player.allegiance)
    allegiances = set(allegiances)
    return len(allegiances)


def check_judgement_tinkering(judgement_card, targeted_index):
    for player in players[targeted_index:]:
        judgement_tinker = player.check_dark_sorcery(
            judgement_card)
        if judgement_tinker[0]:
            judgement_card = judgement_tinker[1]
        judgement_tinker = player.check_devil(
            judgement_card)
        if judgement_tinker[0]:
            judgement_card = judgement_tinker[1]
    for player in players[:targeted_index]:
        judgement_tinker = player.check_dark_sorcery(
            judgement_card)
        if judgement_tinker[0]:
            judgement_card = judgement_tinker[1]
        judgement_tinker = player.check_devil(
            judgement_card)
        if judgement_tinker[0]:
            judgement_card = judgement_tinker[1]
    return judgement_card


# A class for handling individual characters
class Character:
    def __init__(self, character, allegiance, health, gender, character_ability1, character_ability2="None", character_ability3="None", character_ability4="None", character_ability5="None"):
        self.character = character
        self.allegiance = allegiance
        self.health = health
        self.gender = gender
        self.character_ability1 = character_ability1
        self.character_ability2 = character_ability2
        self.character_ability3 = character_ability3
        self.character_ability4 = character_ability4
        self.character_ability5 = character_ability5

    def __repr__(self):
        character_details = f"[{self.character} of {self.allegiance.upper()}, {self.gender} // {self.health} max-health.]"
        return character_details

    def __str__(self):
        character_details = f"[{self.character} of {self.allegiance.upper()}, {self.gender} // {self.health} max-health.]"
        return character_details

    def character_ability_formatting(self):
        if (self.character_ability5 == "None") and (self.character_ability4 == "None") and (self.character_ability3 == "None") and (self.character_ability2 == "None"):
            return f"   - {self.character_ability1}"
        elif (self.character_ability5 == "None") and (self.character_ability4 == "None") and (self.character_ability3 == "None"):
            return f"   - {self.character_ability1} \n   - {self.character_ability2}"
        elif (self.character_ability5 == "None") and (self.character_ability4 == "None"):
            return f"   - {self.character_ability1} \n   - {self.character_ability2} \n   - {self.character_ability3}"
        elif (self.character_ability5 == "None"):
            return f"   - {self.character_ability1} \n   - {self.character_ability2} \n   - {self.character_ability3} \n   - {self.character_ability4}"
        else:
            return f"   - {self.character_ability1} \n   - {self.character_ability2} \n   - {self.character_ability3} \n   - {self.character_ability4} \n   - {self.character_ability5}"

    def list_ability_options(self):
        if (self.character_ability5 == "None") and (self.character_ability4 == "None") and (self.character_ability3 == "None") and (self.character_ability2 == "None"):
            return [f"   - {self.character_ability1}"]
        elif (self.character_ability5 == "None") and (self.character_ability4 == "None") and (self.character_ability3 == "None"):
            return [f"   - {self.character_ability1}", f"   - {self.character_ability2}"]
        elif (self.character_ability5 == "None") and (self.character_ability4 == "None"):
            return [f"   - {self.character_ability1}", f"   - {self.character_ability2}", f"   - {self.character_ability3}"]
        elif (self.character_ability5 == "None"):
            return [f"   - {self.character_ability1}", f"   - {self.character_ability2}", f"   - {self.character_ability3}", f"   - {self.character_ability4}"]
        else:
            return [f"   - {self.character_ability1}", f"   - {self.character_ability2}", f"   - {self.character_ability3}", f"   - {self.character_ability4}", f"   - {self.character_ability5}"]


# A class for handling the character-deck (mostly for selection purposes and Zuo Ci)
class CharacterDeck:
    def __init__(self, character_deck):
        self.contents = []
        self.contents = character_deck

    def add_to_top(self, card):
        self.contents.insert(0, card)

    def remove_from_top(self):
        card = self.contents[0]
        self.contents.pop(0)
        return card

    def shuffle(self):
        random.shuffle(self.contents)


# Emperor Characters
shu_emperors = [
    Character("Liu Bei", "Shu", 4, "Male",
              "Benevolence: You can give any number of your hand-cards to any players. If you give away more than one card, you recovers one unit of health.",
              "Rouse (Ruler Ability): If you need to use an ATTACK, you can ask Sun Shang Xiang or any member of Shu to play it on your behalf."),
    Character("Liu Shan", "Shu", 3, "Male",
              "Relish: Whenever another player targets an ATTACK against you, they must discard a basic card, or else that ATTACK has no net effect on you.",
              "Decentralization: You can skip your action phase. If you do so, you can discard an on-hand card at the end of your turn, in order to allow another player to take a turn directly after yours.",
              "Eiron (Awakening/Ruler Ability): At the start of your turn, if your health is the least or among the least, you must raise your maximum health by one unit, regain one unit of health, and permanently gain the ability 'Rouse'.",
              "Rouse (INACTIVE Ability): If you need to use an ATTACK, you can ask any member of Shu to play it on your behalf.")
]

wei_emperors = [
    Character("Cao Cao", "Wei", 4, "Male",
              "Evil Hero: Whenever you are damaged by a card, you can immediately add it to your hand.",
              "Escort (Ruler Ability): If you need to use a DEFEND, you can ask any member of Wei to play it on your behalf."),
    Character("Cao Pi", "Wei", 3, "Male",
              "Unnatural Death: You can immediately take possession of all cards (both on-hand and equipped) of any player that dies.",
              "Exile: Every instance that you suffer damage, you can force any other player to draw X number of cards (X being the units of health you have missing from your maximum after damage). By doing so the targeted player will have to flip their character card. Flipped character cards must miss their next turn.",
              "Exalt (Ruler Ability): Whenever any Wei character (other than yourself) makes a judgement, if the judgement card that takes effect is either \u2663 or \u2660, that character can choose to let you draw one card from the deck.")
]

wu_emperors = [
    Character("Sun Ce", "Wu", 4, "Male",
              "Ardour: Whenever you use or become the target of any DUEL or red-suited ATTACK cards, you can draw a card.",
              "Divinity (Awakening Ability): If, at the start of your turn, your health is one unit, you must reduce your maximum health by one. After which you permanently gain the abilities 'Dashing Hero' and 'Lingering Spirit'.",
              "Dashing Hero (INACTIVE Ability): Draw an extra card at the start of your turn.",
              "Lingering Spirit (INACTIVE Ability): If your health is not at maximum in your drawing phase, you can force any player to draw X cards, and then discard 1 card, or draw 1 card, and discard X cards. X is the amount of health you have missing from your maximum.",
              "Hegemony (Ruler Ability): During the action phase of any other Wu characters, they can choose to COMPETE against you; you both show a card simultaneously, and whoever has the higher value wins. If they do not win, you can take both cards used. After your awakening ability activates, you are able to refuse COMPETE effects."),
    Character("Sun Quan", "Wu", 4, "Male",
              "Reconsider: You can discard any number of cards to then draw the same number. Limited to one use per turn.",
              "Rescued (Ruler Ability): Whenever another member of Wu uses a PEACH to save you from the brink of death, it provides you with two units of health.")
]

hero_emperors = [
    Character("Dong Zhuo", "Heroes", 8, "Male",
              "Drown in Wine: You can use any of your on-hand cards with suit of \u2660 as WINE. WINE can be used on yourself the brink of death to restore one unit of health, or to increase the damage of their next ATTACK by one damage.",
              "Garden of Lust: Whenever you use an ATTACK on a female character or vice-versa, the targeted character needs to use two DEFEND cards to successfully evade the attack.",
              "Disintegrate: At the end of every turn, if your health is not the least or among the least, you must either lose one unit of health, or reduce your maximum health by one unit.",
              "Tyrant (Ruler Ability): Whenever another Hero character causes damage to any other player, you can flip a judgement card. If the judgement card is of the suit \u2660, you can regain one unit of health."),
    Character("Yuan Shao", "Heroes", 4, "Male",
              "Random Strike: You can use any two hand-cards which have the same suit as RAIN OF ARROWS.",
              "Bloodline (Ruler Ability): Your maximum hand-limit is increased by two for each other Hero character still alive."),
    Character("Zhang Jiao", "Heroes", 3, "Male",
              "Lightning Strike: Whenever you use a DEFEND card, you can target any other player to make a judgement. If the judgement card is of the suit \u2660, the target player suffers two points of lightning damage.",
              "Dark Sorcery: You can exchange the judgement card of any player before it takes effect, with any of your \u2663 or \u2660, either on-hand or equipped.",
              "Amber Sky (Ruler Ability): All Hero characters can give you a DEFEND or LIGHTNING card during their individual turns.")
]

# Shu Characters
shu_characters = [
    Character("Fa Zheng", "Shu", 3, "Male",
              "Grudge: Whenever someone damages you, they must give you a card of suit \u2665 from their hand. If they do not, they lose one unit of health. Whenever another player heals you, they draw a card from the deck.",
              "Dazzle: During your action phase, you can give a card with suit of \u2665 to another player. Then, you can take any of their cards (on-hand or equipped), and give it to any character. Limited to one use per turn."),
    Character("Guan Yu", "Shu", 4, "Male",
              "Horsemanship: You will always be -1 distance in any range calculations.",
              "Warrior Saint: You can use any red-suited cards (on-hand or equipped) as an ATTACK."),
    Character("Huang Yue Ying", "Shu", 3, "Female",
              "Wisdom: Whenever you use a non-delay tool card, you immediately draw a card from the deck.",
              "Talent: You can use tool cards without range restrictions."),
    Character("Huang Zhong", "Shu", 4, "Male",
              "Fearsome Archer: During your action phase, your ATTACK cards cannot be evaded by a DEFEND under the following two conditions: the number of on-hand cards of the target player is less than or equal to your attacking range; or the number of on-hand cards of the target player is more than or equal to the units of health you have remaining."),
    Character("Jian Yong", "Shu", 3, "Male",
              "Persuasion: At the beginning of your action phase, you can COMPETE with any other player; you both show a card simultaneously, and whoever has the higher value wins. If you win, you can either increase or decrease the number of targets to your next basic or non-delay tool card by one for this turn. There are no range restrictions to the extra target. If you lose, you cannot use any tool cards for this turn.",
              "Ignore Formalities: Whenever you COMPETE, you can keep the card played by the loser."),
    Character("Jiang Wei", "Shu", 4, "Male",
              "Taunt: During your action phase, you can pick any player that is able to reach you using an ATTACK. That player must use an ATTACK on you, or else you can discard one of their cards. Limited to one use per turn.",
              "Recommence the Legacy (Awakening Ability): If at the start of your turn, you have no on-hand cards, you must either regain one unit of health or draw two cards, and then reduce your maximum health limit by one. You then permanently gain the ability 'Astrology'.",
              "Astrology (INACTIVE Ability): Before your judgement phase, you can view the top X cards of the deck (X being the number of players still in play, with a maximum of five). Of these X cards, you can rearrange the order of the cards, and choose any number to place at the top or bottom of the draw-deck."),
    Character("Ma Chao", "Shu", 4, "Male",
              "Horsemanship: You will always be -1 distance in any range calculations.",
              "Iron Cavalry: Whenever you ATTACK a player, you can flip a judgement card. If it is red, the ATTACK cannot be dodged."),
    Character("Ma Dai", "Shu", 4, "Male",
              "Horsemanship: You will always be -1 distance in any range calculations.",
              "Backstab: Whenever you use an ATTACK to cause damage to a player within your physical range, you can flip a judgement card. If the judgement is not \u2665, no damage is caused, and instead you cause the target to reduce their maximum health by 1."),
    Character("Wei Yan", "Shu", 4, "Male",
              "Insanity: Whenever you cause damage to any player within your physical range, you regain one unit of health for every unit of damage caused."),
    Character("Zhang Fei", "Shu", 4, "Male",
              "Berserk: There is no limit on how many times you can ATTACK during your turn.",
              "Second Wind (Single-Use Ability): Once per game, at the beginning of your turn, you can return to the same amount of health that you had at the end of your previous turn. You draw a card for each unit of health that changes."),
    Character("Zhao Yun", "Shu", 4, "Male",
              "Dragon Heart: Your ATTACK and DEFEND cards can be used interchangeably.",
              "Cornering Maneuver: Whenever you use a hand-card outside of your turn, you can flip the top card from the deck. If the card is the same type (basic, tool or equipment) as the card used, you can give the card to any player. If not, Zhao Yun can discard or return the card to the top of the deck."),
    Character("Zhu Rong", "Shu", 4, "Female",
              "Giant Elephant: The tool card BARBARIANS has no net effect on you. When any other player uses BARBARIANS and its effects and subsequent card effects are concluded, you will acquire the BARBARIANS card used.",
              "Fearsome Blade: Whenever you successfully damage a target player with an ATTACK, you can choose to COMPETE against them; you both show a card simultaneously, and whoever has the higher value wins. If you win, you can take one card from the target, on-hand or equipped. This takes effect before any retaliatory abilities."),
    Character("Zhuge Liang", "Shu", 3, "Male",
              "Astrology: Before your judgement phase, you can view the top X cards of the deck (X being the number of players still in play, with a maximum of five). Of these X cards, you can rearrange the order of the cards, and choose any number to place at the top or bottom of the draw-deck.",
              "Empty City: When you have no hand-cards, you cannot become the target of an ATTACK or a DUEL.")
]

# Wei Characters
wei_characters = [
    Character("Deng Ai", "Wei", 4, "Male",
              "Amassing Terrain: Every instance that you use or lose cards outside of your turn, you can flip a judgement card. If the judgement is not \u2665, you can place the judgement card (referred to as a TERRAIN) atop your character card. For every TERRAIN that you gain, your physical distance to other players is considered -1.",
              "Conduit (Awakening Ability): At the beginning of your turn, if you have three or more TERRAINS, you must reduce your maximum health by one unit. You then permanently gain the ability 'Blitz'.",
              "Blitz (INACTIVE Ability): In your action phase, you can use any of your TERRAINS as STEAL."),
    Character("Dian Wei", "Wei", 4, "Male",
              "Ferocious Assault: During your action phase, you can inflict one unit of damage to any player within your attacking range by either; reducing one unit of your own health, or discarding one weapon card (on-hand or equipped). Limited to one use per turn."),
    Character("Guo Jia", "Wei", 3, "Male",
              "Envy of Heaven: You can obtain any judgement card that you flip over.",
              "Bequeathed Strategy: For every one unit of damage you recieve, you can draw two cards from the deck. You can then choose to give away one, two or none of these cards to any player."),
    Character("Sima Yi", "Wei", 3, "Male",
              "Retaliation: For every one unit of damage you recieve, you can take one card (whether on-hand or equipped) from the player who was the source of that damage.",
              "Devil: After any judgement has been flipped over, you can immediately discard one of your on-hand or equipped cards to replace the judgement card."),
    Character("Xiahou Dun", "Wei", 4, "Male",
              "Eye for an Eye: For every instance that you suffer damage, you can flip a judgement card. If the judgement is not \u2665, the character that damaged you must choose between the following options; lose one unit of health, or discard any two on-hand cards."),
    Character("Xiahou Yuan", "Wei", 4, "Male",
              "Godspeed: You can do either or both of the following options; skip your judgement and drawing phases, or skip your action phase and discard one equipment card. If you do either, it is the equivalent of using an ATTACK with no distance limitations."),
    Character("Xu Chu", "Wei", 4, "Male",
              "Bare-chested: You can choose to draw one less card in your drawing phase. If you do so, any ATTACK or DUEL cards that you you play in your action phase will deal an additional unit of damage."),
    Character("Xu Huang", "Wei", 4, "Male",
              "Blockade: During your action phase, you can choose to use any of your basic or equipment cards with suit \u2663 or \u2660 as RATIONS DEPLETED with a physical range of -1 in distance calculations. RATIONS DEPLETED acts as a time-delay tool card, in which a player will have to flip a judgement at the start of their turn. If the judgement is any suit other than \u2663, the target fails the judgement and must skip their drawing phase."),
    Character("Xun Yu", "Wei", 3, "Male",
              "Rouse the Tiger: During your action phase, you can choose to COMPETE with any character with more health than you; you both show a card simultaneously, and whoever has the higher value wins. If you win, that player will cause one unit of damage to another player within their attacking range of your choosing. If you lose, the target causes one unit of damage to you. Limited to one use per turn.",
              "Eternal Loyalty: For every one unit of damage you suffer, you can allow any player of your choice (including yourself) to replenish that player’s on-hand cards to their maximum health level."),
    Character("Zhang He", "Wei", 4, "Male",
              "Flexibility: You can discard one on-hand card to skip any of your phases (excluding the beginning and end phases). If you skip your drawing phase using this method, you can draw one on-hand card from a maximum of two other players. If you skip your action phase using this method, you can relocate a card (in the equipment area or pending time-delay tool card area) from its original location to an identical location."),
    Character("Zhang Liao", "Wei", 4, "Male",
              "Raid: In your drawing phase, you can choose to forgo drawing cards from the deck and, instead, draw one on-hand card from a maximum of two other players."),
    Character("Zhen Ji", "Wei", 3, "Female",
              "Impetus: Every one of your black-suited on-hand cards may be used as DEFEND.",
              "Goddess Luo: At the beginning of your turn, you flip a judgement card. If the judgement is a black-suited, you may choose to flip another. This process continues until you flip a red-suited card. The red card is discarded and all black-suited cards are added to your hand."),
    Character("Zhong Hui", "Wei", 4, "Male",
              "Plotting for Power: For every unit of damage you recieve, you can choose to draw one card and then set one hand-card face down as a RITE. Your hand limit is increased by one for each RITE.",
              "Insurrection (Awakening Ability): Whenever you begin your turn with three or more RITES, you must either recover one unit of health or draw two cards. You must then decrease your maximum health by one and permanently gain the ability 'Rejection'.",
              "Rejection (INACTIVE Ability): Once per turn, you can discard one RITE and force any character to draw two cards. If after, that character has more hand-cards than you, you then deal one damage to them.")
]

# Wu Characters
wu_characters = [
    Character("Da Qiao", "Wu", 3, "Female",
              "National Colours: During your action phase, you can use any of your cards (on-hand or equipped) with a \u2666 suit as ACEDIA.",
              "Displacement: Whenever you become the target of an ATTACK, you can discard any card to divert the ATTACK to any player within your attacking range. This effect cannot be used against the player that played the ATTACK card."),
    Character("Gan Ning", "Wu", 4, "Male",
              "Surprise: During your action phase, you can use any of your black-suited cards (on-hand or equipped) as DISMANTLE."),
    Character("Han Dang", "Wu", 4, "Male",
              "Horsebow: You can use any equipment cards as an ATTACK. Whenever you do so, that ATTACK has unlimited range.",
              "Relief: When anyone is on the brink of death, you are able to play an ATTACK on the player taking their turn. If you hit, no damage is dealt, and instead a PEACH is automatically used on the character on the brink of death. This can only be activated outside of your turn."),
    Character("Huang Gai", "Wu", 4, "Male",
              "Trojan Flesh: During your action phase, you can choose to lose one unit of health to draw two more cards from the deck. This ability can be used repeatedly in a turn."),
    Character("Lu Meng", "Wu", 4, "Male",
              "Restraint: If you did not use any ATTACK cards during your action phase, you can skip your discard phase."),
    Character("Lu Su", "Wu", 3, "Male",
              "Altruism: In the drawing phase, you can choose to draw two more cards (total of four cards). If you have more than five on-hand cards as a result, you must give half of your on-hand cards (rounded down to a whole number) to the player with the least on-hand cards (excluding yourself).",
              "Alliance: During your action phase, you can choose to force any two players (other than yourself) to exchange their entire set of on-hand cards by discarding X number of cards, X being the difference between the number of on-hand cards between these two players. Limited to one use per turn."),
    Character("Lu Xun", "Wu", 3, "Male",
              "Humility: You cannot become the target of STEAL or ACEDIA.",
              "One After Another: Whenever you use or lose your last on-hand card, you can immediately draw one card from the deck."),
    Character("Sun Jian", "Wu", 4, "Male",
              "Lingering Spirit: If your health is not at maximum in your drawing phase, you can force any player to draw X cards, and then discard 1 card, or draw 1 card, and discard X cards. X is the amount of health you have missing from your maximum."),
    Character("Sun Shang Xiang", "Wu", 3, "Female",
              "Marriage: During your action phase, you can choose to discard two on-hand cards and pick any male character that is not at full-health. By doing so, both the male character and yourself will recover one unit of health. Limited to one use per turn.",
              "Warrior Woman: Whenever any equipped card is removed from your equipment, you can immediately draw two cards from the deck."),
    Character("Xiao Qiao", "Wu", 3, "Female",
              "Fantasy: Whenever you recieve damage, you can choose to pass the damage onto any other player by discarding an on-hand card that has the suit \u2665. The victim that recieves the damage gets to draw X number of cards from the deck, X being the amount of health missing from the maximum level after damage.",
              "Beauty: All of your \u2660 will be regarded as \u2665."),
    Character("Zhang Zhao and Zhang Hong", "Wu", 3, "Male",
              "Blunt Advice: During your action phase, you can put an on-hand equipment card in the equipment area of another character (you cannot replace something already equipped). If you do so, you draw a card.",
              "Stabilization: At the end of other players' discard phase, you can return one discarded card to that player. If you do so, you can take all of the other cards discarded in this phase as your own on-hand cards."),
    Character("Zhou Tai", "Wu", 4, "Male",
              "Refusing Death: Whenever you are brought to the brink of death, you take a card from the deck and place it atop your character card. If the number on the card is different to all of the others, you return with one health. If the number matches another card, you discard this card and continue to be on the brink of death. When you have cards atop your character card, your hand limit becomes the number of cards atop your character card.",
              "Exertion: Whenever another player has cards taken or discarded by another player, you can lose one health to let that player draw two cards."),
    Character("Zhou Yu", "Wu", 3, "Male",
              "Dashing Hero: Draw an extra card at the start of your turn.",
              "Sow Dissension: During your action phase, you can show an on-hand card and give it to any other player. They must either choose to lose one unit of health or show their entire hand and discard all cards of the same suit as the card you showed them. Limited to one use per turn.")
]

# Hero Characters
hero_characters = [
    Character("Cai Wen Ji", "Heroes", 3, "Female",
              "Lament: Whenever any player is damaged by an ATTACK, you can discard any card, on-hand or equipped. The victim must then flip a judgement. If \u2660, the attacker flips their character card. If \u2665, the victim regains one health. If \u2663, the attacker discards two cards. If \u2666, the victim draws two cards.",
              "Heartbreak: Whenever a player kills you, they lose all of their character abilities for the rest of the game."),
    Character("Chen Gong", "Heroes", 3, "Male",
              "Brilliant Scheme: Once per turn, you can give another player an ATTACK or equipment card. The player can then choose to draw one card or allow you to choose one character within their attacking range. This character is ATTACKed by the player that recieved the card. Limited to one use per turn.",
              "Delayed Wisdom: Whenever you are damaged outside of your turn, you become immune to all ATTACKs and non-delay tool cards for the rest of that turn."),
    Character("Diao Chan", "Heroes", 3, "Female",
              "Seed of Animosity: During your action phase, you can discard one card (on-hand or equipped) and select two male characters to undergo a DUEL with eachother. This ability cannot be prevented using NEGATE, and is limited to one use per turn.",
              "Eclipse the Moon: At the end of your turn, you may draw an additional card from the deck."),
    Character("Hua Tuo", "Heroes", 3, "Male",
              "First Aid: Outside of your turn, you can use any red-suited cards (on-hand or equipped) as a PEACH.",
              "Green Salve: During your action phase, you can discard any card and allow any player to regain one unit of health. Limited to one use per turn."),
    Character("Hua Xiong", "Heroes", 6, "Male",
              "Reckless: Every instance that you suffer damage from a red-suited ATTACK, or a WINE ATTACK, your maximum health limit is reduced by one instead."),
    Character("Jia Xu", "Heroes", 3, "Male",
              "Unmitigated Murder: During your turn, with the exception of yourself, only characters on the brink of death can use a PEACH.",
              "Upheaval (Single-Use Ability): During your action phase, you can force every player, other than yourself, to use an ATTACK on another player with the least distance away. If a player is unable to do so, the player will lose one unit of health. Recipients of the ATTACK need to DEFEND to evade. This ability will proceed in succession starting from the player on your right.",
              "Behind the Curtain: You cannot become the target of any black-suited tool cards."),
    Character("Ling Ju", "Heroes", 3, "Female",
              "Deplete Karma: Whenever you are damaged by another player whose health level is greater or equal to your own, you can discard a red-suited hand-card to reduce the damage by one. If you damage another player whose health is greater than or equal to your own, you can discard black-suited hand-card to increase the damage by one.",
              "Burning Heart (Single-Use Ability): When you kill another character, you can exchange role cards with the player you just killed. You cannot activate this ability if you are the emperor, or just killed the emperor."),
    Character("Lu Bu", "Heroes", 4, "Male",
              "Without Equal: Whenever you use ATTACK, your target has to use two DEFEND cards to successfully evade the attack. During a DUEL, your opponent has to use two ATTACK cards for every one ATTACK card that you use."),
    Character("Pang De", "Heroes", 4, "Male",
              "Horsemanship: You will always be -1 distance in any range calculations.",
              "Fearsome Advance: Whenever your ATTACK is evaded by a DEFEND, you can discard one of your opponents cards (on-hand or equipped)."),
    Character("Yan Liang and Wen Chou", "Heroes", 4, "Male",
              "Dual Heroes: At the beginning of your turn, you can choose to forgo your drawing phase and instead flip a judgement. Unlike usual judgement cards, this card will be added to your hand. Note the colour of the suit of this judgement card. For the rest of your action phase, you can choose to use any on-hand card with a different colour suit from this judgement card as a DUEL."),
    Character("Yuan Shu", "Heroes", 4, "Male",
              "Mediocrity: During your drawing phase, you draw an extra X cards, X being the total number of allegiances still in play. During your discard phase, you must discard at least as many card as there are allegiances still in play. If you have less cards than there are allegiances, you must discard all of them.",
              "False Ruler: You possess the same ruler ability as the current emperor."),
    Character("Zuo Ci", "Heroes", 3, "Male",
              "Shapeshift: After everyone has selected their character cards, you select two unused character cards at random from the deck. Select one of these two characters and place it before you, then state one of that character's abilities (excluding Single-Use, Awakening, INACTIVE and Ruler abilities). You will obtain the stated ability, the allegiance, and the gender of this character until you have replaced it. At the beginning and end of each turn, you can replace the character with another character and/or re-state another ability.",
              "Geminate: For every one unit of damage you recieve, you can acquire a new character card for 'Shapeshift'.")
]


# Generation of character_decks
def generate_character_decks():
    shu_emperor_cards = CharacterDeck(shu_emperors)
    wei_emperor_cards = CharacterDeck(wei_emperors)
    wu_emperor_cards = CharacterDeck(wu_emperors)
    hero_emperor_cards = CharacterDeck(hero_emperors)
    shu_character_cards = CharacterDeck(shu_characters)
    wei_character_cards = CharacterDeck(wei_characters)
    wu_character_cards = CharacterDeck(wu_characters)
    hero_character_cards = CharacterDeck(hero_characters)
    all_emperor_cards = CharacterDeck(
        shu_emperors + wei_emperors + wu_emperors + hero_emperors)
    all_character_cards = CharacterDeck(
        shu_emperors + shu_characters + wei_emperors + wei_characters + wu_emperors + wu_characters + hero_emperors + hero_characters)
    character_card_discard_pile = CharacterDeck([])
    all_decks = [shu_emperor_cards, wei_emperor_cards, wu_emperor_cards, hero_emperor_cards, shu_character_cards, wei_character_cards,
                 wu_character_cards, hero_character_cards, all_emperor_cards, all_character_cards, character_card_discard_pile]
    return all_decks


# A class for handling the individual cards in the deck
class Card:
    def __init__(self, rank, val, suit, type, effect, flavour_text, weapon_range=None, effect2=None):
        self.rank = rank
        self.val = val
        self.suit = suit
        self.type = type
        self.effect = effect
        self.flavour_text = flavour_text
        self.weapon_range = weapon_range
        self.effect2 = effect2

    def __str__(self):
        if self.type == "Weapon":
            return f"[{self.effect} <:{self.weapon_range}:> - {self.val}{self.suit}]"
        else:
            return f"[{self.effect} - {self.val}{self.suit}]"

    def __repr__(self):
        if self.type == "Weapon":
            return f"{self.effect} <:{self.weapon_range}:> - {self.val}{self.suit}"
        else:
            return f"[{self.effect} - {self.val}{self.suit}]"

    def __gt__(self, other):
        return self.rank > other.rank


# A class for handling the deck of cards in play
class Deck:
    def __init__(self, main_deck):
        self.contents = []
        self.contents = main_deck

    def list_cards(self):
        return [str(card) for card in self.contents]

    def shuffle(self):
        random.shuffle(self.contents)

    def check_if_empty(self):
        if len(main_deck.contents) <= 0:
            print(
                f"{len(discard_deck.contents)} discarded cards have been shuffled back into the main deck!")
            main_deck.contents, discard_deck.contents = discard_deck.contents, main_deck.contents
            main_deck.shuffle()

    def add_to_top(self, card):
        self.contents.insert(0, card)

    def add_to_bottom(self, card):
        self.contents.append(card)

    def remove_from_top(self):
        card = self.contents[0]
        self.contents.pop(0)
        return card

    def discard_from_deck(self, num=1):
        while num > 0:
            main_deck.check_if_empty()
            card = self.remove_from_top()
            discard_deck.contents.insert(0, card)
            print(
                f"The following card has been discarded from the deck: {card}")
            num -= 1

    def view(self, num=1):
        print(f"{num} card(s) being viewed from the deck.")
        viewed = self.contents[:num]
        for card in viewed:
            return card


# A class for handling the cards in a player's hand
class Hand(Deck):
    def __init__(self, hand_cards):
        self.contents = []
        self.contents = hand_cards

    def prompt_for_discard_from_hand(self):
        options_str = []
        for card in self.list_cards():
            options_str.append(card)
        question = [
            {
                'type': 'list',
                'name': 'Selected',
                'message': 'Please select a card to discard:',
                'choices': options_str,
                'filter': lambda card: options_str.index(card)
            },
        ]

        answer = prompt(question, style=custom_style_2)
        return answer

    def discard_from_hand(self, num=1):
        print(f'{num} card(s) to be discarded:')
        while num > 0:
            card_index = self.prompt_for_discard_from_hand().get('Selected')
            card = self.contents[card_index]
            self.contents.pop(card_index)
            discard_deck.add_to_top(card)
            num -= 1

    def view_hand(self):
        if self.contents == []:
            print("There are no cards remaining in your hand.")
        else:
            print("The following card(s) are in your hand:")
            for card in self.list_cards():
                print(card)

    def draw(self, deck_drawn, num=1, message=True):
        if message == True:
            if num == 1:
                print(
                    f"{num} card has been added to {players[0].character}'s hand.")
            else:
                print(
                    f"{num} cards have been added to {players[0].character}'s hand.")
        while num > 0:
            if deck_drawn == main_deck:
                main_deck.check_if_empty()
            card = deck_drawn.remove_from_top()
            self.add_to_top(card)
            num -= 1


# 108 Cards in the Deck;
all_cards = [
    Card(1, 'A', '\u2660', 'Tool', 'Duel', 'You can target any player for a duel with this card. If the target does not play an ATTACK, they are damaged. If they do ATTACK, then you must play one in response or take damage. Whoever does not attack, takes damage.'),
    Card(1, 'A', '\u2660', 'Delay-Tool', 'Lightning', 'You can place this Delay-Tool on yourself. In your next turn, you will perform a judgement for this card; if it is between two and nine of \u2660 (inclusively), you recieve three units of lightning damage. If not, LIGHTNING passes to the next player.'),
    Card(2, '2', '\u2660', 'Weapon', 'Frost Blade',
         'When equipped, and an ATTACK hits a target, the wielder has a choice; they can either damage the target or force them to discard two cards.', 2),
    Card(2, '2', '\u2660', 'Weapon', 'Gender-Swords',
         'When equipped, and playing an ATTACK on the target, the wielder can force the target to make a choice; to either discard a hand-card or allow the wielder to draw one from the deck.', 2),
    Card(2, '2', '\u2660', 'Armor', 'Eight-Trigrams',
         'When equipped: whenever a DEFEND is needed, the wearer can perform a judgement. If it is red, the DEFEND is considered to be played.'),
    Card(3, '3', '\u2660', 'Tool', 'Dismantle',
         'You can target any player and discard one of their cards, on-hand or equipped.'),
    Card(3, '3', '\u2660', 'Tool', 'Steal',
         'You can use this card on a player within physical range to take a card from them (on-hand or equipped) and add it to your hand.'),
    Card(4, '4', '\u2660', 'Tool', 'Dismantle',
         'You can target any player and discard one of their cards, on-hand or equipped.'),
    Card(4, '4', '\u2660', 'Tool', 'Steal',
         'You can use this card on a player within physical range to take a card from them (on-hand or equipped) and add it to your hand.'),
    Card(5, '5', '\u2660', '+1 Horse', 'Shadow; +1 Horse',
         'When equipped, this horse places you further away from players in distance calculations by +1.'),
    Card(5, '5', '\u2660', 'Weapon', 'Green Dragon Halberd',
         "When equipped, and the target of the wielder's ATTACK is DEFENDED against, the wielder may ATTACK again.", 3),
    Card(6, '6', '\u2660', 'Delay-Tool', 'Acedia',
         'You can place Delay-Tool on any other player. The target must perform a judgement for this card. If it is not \u2665, they forfeit their action-phase.'),
    Card(6, '6', '\u2660', 'Weapon', 'Black Pommel',
         'When equipped, the wielder ignores any armor of their targets.', 2),
    Card(7, '7', '\u2660', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(7, '7', '\u2660', 'Tool', 'Barbarians',
         'All other players must play an ATTACK or else suffer one damage.'),
    Card(8, '8', '\u2660', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(8, '8', '\u2660', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(9, '9', '\u2660', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(9, '9', '\u2660', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(10, '10', '\u2660', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(10, '10', '\u2660', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(11, 'J', '\u2660', 'Tool', 'Negate',
         'Any player may play this card in response to a tool card being played. This prevents that tool card from working.'),
    Card(11, 'J', '\u2660', 'Tool', 'Steal',
         'You can use this card on a player within physical range to take a card from them (on-hand or equipped) and add it to your hand.'),
    Card(12, 'Q', '\u2660', 'Tool', 'Dismantle',
         'You can target any player and discard one of their cards, on-hand or equipped.'),
    Card(12, 'Q', '\u2660', 'Weapon', 'Serpent Spear',
         'When equipped, the wielder can discard any two cards to behave as an ATTACK.', 3),
    Card(13, 'K', '\u2660', 'Tool', 'Barbarians',
         'All other players must play an ATTACK or else suffer one damage.'),
    Card(13, 'K', '\u2660', '-1 Horse', 'Da Yuan; -1 Horse',
         'When equipped, this horse places other players closer to you in distance calculations by -1.'),
    Card(1, 'A', '\u2665', 'Tool', 'Peach Gardens',
         'All damaged players will be healed by one health.'),
    Card(1, 'A', '\u2665', 'Tool', 'Rain of Arrows',
         'All other players must play a DEFEND or else suffer one damage.'),
    Card(2, '2', '\u2665', 'Basic', 'Defend',
         'When targeted by an ATTACK, you can play this card to avoid taking damage.'),
    Card(2, '2', '\u2665', 'Basic', 'Defend',
         'When targeted by an ATTACK, you can play this card to avoid taking damage.'),
    Card(3, '3', '\u2665', 'Basic', 'Peach',
         'During your turn, you can use this card to recover one unit of missing health. Additionally, whenever a player is on the brink of death, any player can use a PEACH to make them recover one unit of health.'),
    Card(3, '3', '\u2665', 'Tool', 'Granary',
         'You can use this card to flip over one card for every living player. Then, starting with the user of this card, each player will select a card and add it to their hand.'),
    Card(4, '4', '\u2665', 'Basic', 'Peach', 'During your turn, you can use this card to recover one unit of missing health. Additionally, whenever a player is on the brink of death, any player can use a PEACH to make them recover one unit of health.'),
    Card(4, '4', '\u2665', 'Tool', 'Granary',
         'You can use this card to flip over one card for every living player. Then, starting with the user of this card, each player will select a card and add it to their hand.'),
    Card(5, '5', '\u2665', '-1 Horse', 'Red Hare; -1 Horse',
         'When equipped, this horse places other players closer to you in distance calculations by -1.'),
    Card(5, '5', '\u2665', 'Weapon', "Huang's Longbow",
         'When equipped, if the wielder successfully damages another player with an ATTACK, they can discard any horse of the target player.', 5),
    Card(6, '6', '\u2665', 'Basic', 'Peach', 'During your turn, you can use this card to recover one unit of missing health. Additionally, whenever a player is on the brink of death, any player can use a PEACH to make them recover one unit of health.'),
    Card(6, '6', '\u2665', 'Delay-Tool', 'Acedia',
         'You can place Delay-Tool on any other player. The target must perform a judgement for this card. If it is not \u2665, they forfeit their action-phase.'),
    Card(7, '7', '\u2665', 'Basic', 'Peach',
         'During your turn, you can use this card to recover one unit of missing health. Additionally, whenever a player is on the brink of death, any player can use a PEACH to make them recover one unit of health.'),
    Card(7, '7', '\u2665', 'Tool', 'Greed',
         'Use this card to draw two cards from the deck.'),
    Card(8, '8', '\u2665', 'Basic', 'Peach',
         'During your turn, you can use this card to recover one unit of missing health. Additionally, whenever a player is on the brink of death, any player can use a PEACH to make them recover one unit of health.'),
    Card(8, '8', '\u2665', 'Tool', 'Greed',
         'Use this card to draw two cards from the deck.'),
    Card(9, '9', '\u2665', 'Basic', 'Peach', 'During your turn, you can use this card to recover one unit of missing health. Additionally, whenever a player is on the brink of death, any player can use a PEACH to make them recover one unit of health.'),
    Card(9, '9', '\u2665', 'Tool', 'Greed',
         'Use this card to draw two cards from the deck.'),
    Card(10, '10', '\u2665', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(10, '10', '\u2665', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(11, 'J', '\u2665', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(11, 'J', '\u2665', 'Tool', 'Greed',
         'Use this card to draw two cards from the deck.'),
    Card(12, 'Q', '\u2665', 'Basic', 'Peach',
         'During your turn, you can use this card to recover one unit of missing health. Additionally, whenever a player is on the brink of death, any player can use a PEACH to make them recover one unit of health.'),
    Card(12, 'Q', '\u2665', 'Tool', 'Dismantle',
         'You can target any player and discard one of their cards, on-hand or equipped.'),
    Card(12, 'Q', '\u2665', 'Delay-Tool', 'Lightning',
         'You can place this Delay-Tool on yourself. In your next turn, you will perform a judgement for this card; if it is between two and nine of \u2660 (inclusively), you recieve three units of lightning damage. If not, the Lightning passes to the next player.'),
    Card(13, 'K', '\u2665', 'Basic', 'Defend',
         'When targeted by an ATTACK, you can play this card to avoid taking damage.'),
    Card(13, 'K', '\u2665', '+1 Horse', 'Storm Runner; +1 Horse',
         'When equipped, this horse places you further away from players in distance calculations by +1.'),
    Card(1, 'A', '\u2663', 'Tool', 'Duel', 'You can target any player for a duel with this card. If the target does not play an ATTACK, they are damaged. If they do ATTACK, then you must play one in response or take damage. Whoever does not attack, takes damage.'),
    Card(1, 'A', '\u2663', 'Weapon', 'Zhuge Crossbow',
         'When equipped, the wielder has no limit to the number of ATTACKs they can play in their turn.', 1),
    Card(2, '2', '\u2663', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(2, '2', '\u2663', 'Armor', 'Black Shield',
         'When equipped, black ATTACK cards cannot affect the wearer.'),
    Card(2, '2', '\u2663', 'Armor', 'Eight-Trigrams',
         'When equipped: whenever a DEFEND is needed, the wearer can perform a judgement. If it is red, the DEFEND is considered to be played.'),
    Card(3, '3', '\u2663', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(3, '3', '\u2663', 'Tool', 'Dismantle',
         'You can target any player and discard one of their cards, on-hand or equipped.'),
    Card(4, '4', '\u2663', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(4, '4', '\u2663', 'Tool', 'Dismantle',
         'You can target any player and discard one of their cards, on-hand or equipped.'),
    Card(5, '5', '\u2663', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(5, '5', '\u2663', '+1 Horse', 'Di Lu; +1 Horse',
         'When equipped, this horse places you further away from players in distance calculations by +1.'),
    Card(6, '6', '\u2663', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(6, '6', '\u2663', 'Delay-Tool', 'Acedia',
         'You can place Delay-Tool on any other player. The target must perform a judgement for this card. If it is not \u2665, they forfeit their action-phase.'),
    Card(7, '7', '\u2663', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(7, '7', '\u2663', 'Tool', 'Barbarians',
         'All other players must play an ATTACK or else suffer one damage.'),
    Card(8, '8', '\u2663', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(8, '8', '\u2663', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(9, '9', '\u2663', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(9, '9', '\u2663', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(10, '10', '\u2663', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(10, '10', '\u2663', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(11, 'J', '\u2663', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(11, 'J', '\u2663', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(12, 'Q', '\u2663', 'Tool', 'Coerce', 'Use this card to target any other player that possesses a weapon. Afterwards, you can then select any target within their attacking range. Your target can then ATTACK the victim. If they do not, you will take their weapon and add it to your hand.'),
    Card(12, 'Q', '\u2663', 'Tool', 'Negate',
         'Any player may play this card in response to a tool card being played. This prevents that tool card from working.'),
    Card(13, 'K', '\u2663', 'Tool', 'Coerce', 'Use this card to target any other player that possesses a weapon. Afterwards, you can then select any target within their attacking range. Your target can then ATTACK the victim. If they do not, you will take their weapon and add it to your hand.'),
    Card(13, 'K', '\u2663', 'Tool', 'Negate',
         'Any player may play this card in response to a tool card being played. This prevents that tool card from working.'),
    Card(1, 'A', '\u2666', 'Tool', 'Duel', 'You can target any player for a duel with this card. If the target does not play an ATTACK, they are damaged. If they do ATTACK, then you must play one in response or take damage. Whoever does not attack, takes damage.'),
    Card(1, 'A', '\u2666', 'Weapon', 'Zhuge Crossbow',
         'When equipped, the wielder has no limit to the number of ATTACKs they can play in their turn.', 1),
    Card(2, '2', '\u2666', 'Basic', 'Defend',
         'When targeted by an ATTACK, you can play this card to avoid taking damage.'),
    Card(2, '2', '\u2666', 'Basic', 'Defend',
         'When targeted by an ATTACK, you can play this card to avoid taking damage.'),
    Card(3, '3', '\u2666', 'Basic', 'Defend',
         'When targeted by an ATTACK, you can play this card to avoid taking damage.'),
    Card(3, '3', '\u2666', 'Tool', 'Steal',
         'You can use this card on a player within physical range to take a card from them (on-hand or equipped) and add it to your hand.'),
    Card(4, '4', '\u2666', 'Basic', 'Defend',
         'When targeted by an ATTACK, you can play this card to avoid taking damage.'),
    Card(4, '4', '\u2666', 'Tool', 'Steal',
         'You can use this card on a player within physical range to take a card from them (on-hand or equipped) and add it to your hand.'),
    Card(5, '5', '\u2666', 'Basic', 'Defend',
         'When targeted by an ATTACK, you can play this card to avoid taking damage.'),
    Card(5, '5', '\u2666', 'Weapon', 'Axe',
         'When equipped, and the target of the wielder DEFENDs against the ATTACK of the wielder, they can discard two cards to force the damage.', 3),
    Card(6, '6', '\u2666', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(6, '6', '\u2666', 'Basic', 'Defend',
         'When targeted by an ATTACK, you can play this card to avoid taking damage.'),
    Card(7, '7', '\u2666', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(7, '7', '\u2666', 'Basic', 'Defend',
         'When targeted by an ATTACK, you can play this card to avoid taking damage.'),
    Card(8, '8', '\u2666', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(8, '8', '\u2666', 'Basic', 'Defend',
         'When targeted by an ATTACK, you can play this card to avoid taking damage.'),
    Card(9, '9', '\u2666', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(9, '9', '\u2666', 'Basic', 'Defend',
         'When targeted by an ATTACK, you can play this card to avoid taking damage.'),
    Card(10, '10', '\u2666', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(10, '10', '\u2666', 'Basic', 'Defend',
         'When targeted by an ATTACK, you can play this card to avoid taking damage.'),
    Card(11, 'J', '\u2666', 'Basic', 'Defend',
         'When targeted by an ATTACK, you can play this card to avoid taking damage.'),
    Card(11, 'J', '\u2666', 'Basic', 'Defend',
         'When targeted by an ATTACK, you can play this card to avoid taking damage.'),
    Card(12, 'Q', '\u2666', 'Basic', 'Peach',
         'During your turn, you can use this card to recover one unit of missing health. Additionally, whenever a player is on the brink of death, any player can use a PEACH to make them recover one unit of health.'),
    Card(12, 'Q', '\u2666', 'Tool', 'Negate',
         'Any player may play this card in response to a tool card being played. This prevents that tool card from working.'),
    Card(12, 'Q', '\u2666', 'Weapon', 'Sky Scorcher Halberd',
         'When equipped and using the last on-hand card to ATTACK, the ATTACK can target an additional two players.', 4),
    Card(13, 'K', '\u2666', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(13, 'K', '\u2666', '-1 Horse', 'Hua Liu; -1 Horse',
         'When equipped, this horse places other players closer to you in distance calculations by -1.')
]


# A class for individual players and their stats in the game
class Player(Character):
    def __init__(self, role):
        self.role = role
        self.weapon_range = 1
        self.attacks_this_turn = 0
        self.current_health = 0
        self.max_health = 0
        self.hand_cards = Hand([])
        self.equipment_weapon = []
        self.equipment_armor = []
        self.equipment_defensive_horse = []
        self.equipment_offensive_horse = []
        self.pending_judgements = []
        self.acedia_active = False
        self.rations_depleted_active = False
        self.awakened = False
        self.forms = CharacterDeck([])
        self.refusing_death = []
        self.rites = []
        self.terrains = []
        self.previous_turn_health = None
        self.used_trigrams = False
        self.amassed_terrain = False
        self.used_cornering_maneuver = False
        self.used_bare_chested = False
        self.wine_active = False
        self.flipped_char_card = False
        self.weapon_popped = False
        self.armor_popped = False
        self.off_horse_popped = False
        self.def_horse_popped = False
        self.tools_disabled = False
        self.tools_immunity = False

    def __repr__(self):
        character_details = f"{self.character} of {self.allegiance.upper()}, {self.gender} // {self.current_health}/{self.max_health} HP remaining"
        if self.role == 'Emperor':
            return ("[Emperor] " + character_details)
        else:
            return (character_details)

    def __str__(self):
        if game_started:
            character_details = f"{self.character} of {self.allegiance.upper()}, {self.gender} // {self.current_health}/{self.max_health} HP remaining"
            if self.role == 'Emperor':
                return ("[Emperor] " + character_details)
            else:
                return (character_details)
        else:
            character_details, abilities_list = f"{self.character} of {self.allegiance.upper()}, {self.gender} // {self.current_health}/{self.max_health} HP remaining \n", ability_formatting(self)
            if self.role == 'Emperor':
                return ("[Emperor] " + character_details + abilities_list)
            else:
                return (character_details + abilities_list)

# Character assignment and game-setup
    def all_pick_characters(self):
        print(f'Your role is the {self.role}.')
        card_index = self.prompt_all_pick_characters(
            all_character_cards.contents)
        print(' ')
        return (card_index)

    def banning_pick_characters(self):
        print(f'Your role is the {self.role}.')
        card_index = self.prompt_banning_pick_characters(
            all_character_cards.contents)
        if card_index == None:
            card_index = 0
        all_character_cards.contents.pop(card_index)
        print(' ')

    def prompt_all_pick_characters(self, char_cards):
        char_cards_str = list_character_options(char_cards)
        question = [
            {
                'type': 'list',
                'name': 'Selected',
                'message': 'Please select a card that you would like to play as:',
                'choices': char_cards_str,
                'filter': lambda card: char_cards_str.index(card)
            },
        ]

        answer = prompt(question, style=custom_style_2)
        card_index = answer.get('Selected')
        print(char_cards_str[card_index])
        print(char_cards[card_index].character_ability_formatting())
        message = "Please confirm you want to play with the above character."
        if question_yes_no(message):
            return (card_index)
        else:
            self.prompt_all_pick_characters(char_cards)

    def prompt_banning_pick_characters(self, char_cards):
        char_cards_str = list_character_options(char_cards)
        question = [
            {
                'type': 'list',
                'name': 'Selected',
                'message': 'Please select a card that you would like to BAN:',
                'choices': char_cards_str,
                'filter': lambda card: char_cards_str.index(card)
            },
        ]

        answer = prompt(question, style=custom_style_2)
        card_index = answer.get('Selected')
        print(char_cards_str[card_index])
        print(char_cards[card_index].character_ability_formatting())
        message = "Please confirm you want to BAN the above character."
        if question_yes_no(message):
            return (card_index)
        else:
            self.prompt_banning_pick_characters(char_cards)

    def single_draft_emperors(self):
        print(f'Your role is the {self.role}.')
        char_cards = get_emperors_for_single_draft(self)
        card_index = self.prompt_single_draft_emperors(char_cards)
        print(' ')
        return (card_index, char_cards)

    def single_draft_characters(self):
        print(f'Your role is the {self.role}.')
        char_cards = get_options_for_single_draft(self)
        card_index = self.prompt_single_draft_characters(char_cards)
        print(' ')
        return (card_index, char_cards)

    def prompt_single_draft_emperors(self, char_cards):
        char_cards_str = list_character_options(char_cards)
        question = [
            {
                'type': 'list',
                'name': 'Selected',
                'message': 'Please select a card:',
                'choices': char_cards_str,
                'filter': lambda card: char_cards_str.index(card)
            },
        ]

        answer = prompt(question, style=custom_style_2)
        card_index = answer.get('Selected')
        print(char_cards_str[card_index])
        print(char_cards[card_index].character_ability_formatting())
        message = "Please confirm you want to play with the above character."
        if question_yes_no(message):
            return (card_index)
        else:
            self.prompt_single_draft_emperors(char_cards)

    def prompt_single_draft_characters(self, char_cards):
        char_cards_str = list_character_options(char_cards)
        question = [
            {
                'type': 'list',
                'name': 'Selected',
                'message': 'Please select a card:',
                'choices': char_cards_str,
                'filter': lambda card: char_cards_str.index(card)
            },
        ]

        answer = prompt(question, style=custom_style_2)
        card_index = answer.get('Selected')
        print(char_cards_str[card_index])
        print(char_cards[card_index].character_ability_formatting())
        message = "Please confirm you want to play with the above character."
        if question_yes_no(message):
            return (card_index)
        else:
            self.prompt_single_draft_characters(char_cards)

    def assign_character_all_pick(self):
        card_index = self.all_pick_characters()
        if card_index == None:
            card_index = 0
        selected_char = all_character_cards.contents[card_index]
        all_character_cards.contents.pop(card_index)
        self.character = selected_char.character
        self.allegiance = selected_char.allegiance
        if (self.role == "Emperor") and (number_of_players_output > 4):
            self.current_health = (selected_char.health + 1)
            self.max_health = (selected_char.health + 1)
        else:
            self.current_health = selected_char.health
            self.max_health = selected_char.health
        self.gender = selected_char.gender
        self.character_ability1 = selected_char.character_ability1
        self.character_ability2 = selected_char.character_ability2
        self.character_ability3 = selected_char.character_ability3
        self.character_ability4 = selected_char.character_ability4
        self.character_ability5 = selected_char.character_ability5

    def assign_character_single_draft(self):
        if self.role == 'Emperor':
            card_index, char_cards = self.single_draft_emperors()
            if card_index == None:
                card_index = 0
        else:
            card_index, char_cards = self.single_draft_characters()
            if card_index == None:
                card_index = 0
        selected_char = char_cards[card_index]
        char_cards.pop(card_index)
        for card in char_cards:
            character_card_discard_pile.add_to_top(card)
        self.character = selected_char.character
        self.allegiance = selected_char.allegiance
        if (self.role == "Emperor") and (number_of_players_output > 4):
            self.current_health = (selected_char.health + 1)
            self.max_health = (selected_char.health + 1)
        else:
            self.current_health = selected_char.health
            self.max_health = selected_char.health
        self.gender = selected_char.gender
        self.character_ability1 = selected_char.character_ability1
        self.character_ability2 = selected_char.character_ability2
        self.character_ability3 = selected_char.character_ability3
        self.character_ability4 = selected_char.character_ability4
        self.character_ability5 = selected_char.character_ability5

    def assign_character_all_random(self):
        selected_char = all_character_cards.contents[0]
        all_character_cards.contents.pop(0)
        self.character = selected_char.character
        self.allegiance = selected_char.allegiance
        if (self.role == "Emperor") and (number_of_players_output > 4):
            self.current_health = (selected_char.health + 1)
            self.max_health = (selected_char.health + 1)
        else:
            self.current_health = selected_char.health
            self.max_health = selected_char.health
        self.gender = selected_char.gender
        self.character_ability1 = selected_char.character_ability1
        self.character_ability2 = selected_char.character_ability2
        self.character_ability3 = selected_char.character_ability3
        self.character_ability4 = selected_char.character_ability4
        self.character_ability5 = selected_char.character_ability5
        print(self)
        print(' ')

# Menu Creation for targeting players
    def calculate_targets_in_physical_range(self, source_player_index, modifier=0):
        output = []
        for (target_index, target) in enumerate(players):
            if target_index != source_player_index:
                distance = abs(target_index - source_player_index)
                if distance > len(players) / 2:
                    distance = len(players) - distance
                if distance - (players[source_player_index].check_horsemanship() + modifier + (len(players[source_player_index].equipment_offensive_horse) + 1)) + (len(target.equipment_defensive_horse)) <= 0:
                    output.append(target_index)
        return output

    def calculate_targets_in_weapon_range(self, source_player_index, modifier=0, omit=None):
        output = []
        for (target_index, target) in enumerate(players):
            if target_index != source_player_index:
                distance = abs(target_index - source_player_index)
                if distance > len(players) / 2:
                    distance = len(players) - distance
                if distance - (players[source_player_index].check_horsemanship() + modifier + (len(players[source_player_index].equipment_offensive_horse)) + (players[source_player_index].weapon_range)) + (len(target.equipment_defensive_horse)) <= 0:
                    output.append(target_index)
        if omit != None:
            output.remove(omit)
        return output

    def create_targeting_menu(self, range_type="Weapon", source_player_index=0, modifier=0, omit=None):
        if range_type == "Physical":
            if self.check_talent():
                output_str = [
                    Separator("------<Cannot target yourself>------")]
                for player in players[1:]:
                    output_str.append(str(player))
                return (output_str)

            reachable_indexes = self.calculate_targets_in_physical_range(
                source_player_index, modifier)
            if len(reachable_indexes) == 0:
                print(
                    f"{self.character} - You have insufficient range to reach anyone with this card.")
                return "Break"
            output_str = []
            for player in players:
                output_str.append(Separator("------" + str(player) + "------"))
            for reachable_index in reachable_indexes:
                output_str.pop(reachable_index)
                output_str.insert(reachable_index, str(
                    players[reachable_index]))
            return (output_str)

        if range_type == "Weapon":
            reachable_indexes = self.calculate_targets_in_weapon_range(
                source_player_index, modifier, omit)
            if len(reachable_indexes) == 0:
                print(
                    f"{self.character} - You have insufficient range to reach anyone with an ATTACK.")
                return "Break"
            output_str = []
            for player in players:
                output_str.append(Separator("------" + str(player) + "------"))
            for reachable_index in reachable_indexes:
                output_str.pop(reachable_index)
                output_str.insert(reachable_index, str(
                    players[reachable_index]))
            return (output_str)

# Menu Creation for cards!
    def create_actual_menu(self):
        options = []
        options.append("HAND")
        for card in self.hand_cards.contents:
            options.append(card)
        options.append("EQUIP")
        if len(self.equipment_weapon) > 0:
            options.append(self.equipment_weapon[0])
        else:
            options.append("Empty Weapon Slot")
        if len(self.equipment_armor) > 0:
            options.append(self.equipment_armor[0])
        else:
            options.append("Empty Armor Slot")
        if len(self.equipment_offensive_horse) > 0:
            options.append(self.equipment_offensive_horse[0])
        else:
            options.append("Empty Horse Slot")
        if len(self.equipment_defensive_horse) > 0:
            options.append(self.equipment_defensive_horse[0])
        else:
            options.append("Empty Horse Slot")
        return(options)

    def create_blind_menu(self):
        cards_discardable = (len(self.hand_cards.contents))
        if cards_discardable > 0:
            options_str = []
            i = 1
            for item in self.hand_cards.contents:
                options_str.append(f"Hand-Card {i}")
                i += 1

            return(options_str)

    def create_semiblind_menu(self, append_judgements=False):
        cards_discardable = (len(self.hand_cards.contents) + len(self.equipment_weapon) + len(
            self.equipment_armor) + len(self.equipment_offensive_horse) + len(self.equipment_defensive_horse))
        if append_judgements == 1:
            cards_discardable += len(self.pending_judgements)
        if cards_discardable > 0:
            options_str = []
            i = 1
            for item in self.hand_cards.contents:
                options_str.append(f"Hand-Card {i}")
                i += 1
            options_str.append(
                Separator("---------------EQUIPPED--CARDS---------------"))
            if len(self.equipment_weapon) > 0:
                options_str.append(
                    str(self.equipment_weapon[0]))
            else:
                options_str.append(
                    Separator("  -----------<Empty Weapon Slot>-----------  "))
            if len(self.equipment_armor) > 0:
                options_str.append(
                    str(self.equipment_armor[0]))
            else:
                options_str.append(
                    Separator("  -----------<Empty Armor Slot>------------  "))
            if len(self.equipment_offensive_horse) > 0:
                options_str.append(
                    str(self.equipment_offensive_horse[0]))
            else:
                options_str.append(
                    Separator("  -----------<Empty Horse Slot>------------  "))
            if len(self.equipment_defensive_horse) > 0:
                options_str.append(
                    str(self.equipment_defensive_horse[0]))
            else:
                options_str.append(
                    Separator("  -----------<Empty Horse Slot>------------  "))
            if append_judgements:
                options_str.append(
                    Separator("-----------PENDING-JUDGEMENT-CARDS-----------"))
                if len(self.pending_judgements) > 0:
                    for pending_judgement_card in self.pending_judgements:
                        options_str.append(str(pending_judgement_card))

            return(options_str)

    def create_nonblind_menu(self, only_hand_cards=False, append_judgements=False, omit_item=None):
        cards_discardable = (len(self.hand_cards.contents) + len(self.equipment_weapon) + len(
            self.equipment_armor) + len(self.equipment_offensive_horse) + len(self.equipment_defensive_horse))
        if append_judgements == 1:
            cards_discardable += len(self.pending_judgements)
        if cards_discardable > 0:
            options_str = []
            for card in self.hand_cards.contents:
                options_str.append(str(card))
            if only_hand_cards:
                return (options_str)
            else:
                options_str.append(
                    Separator("---------------EQUIPPED--CARDS---------------"))
            if omit_item == "Weapon":
                options_str.append(
                    Separator("    ---------<Cannot use weapon>---------    "))
            else:
                if len(self.equipment_weapon) > 0:
                    options_str.append(str(self.equipment_weapon[0]))
                else:
                    options_str.append(
                        Separator("  -----------<Empty Weapon Slot>-----------  "))
            if not omit_item == "Non-weapon":
                if len(self.equipment_armor) > 0:
                    options_str.append(str(self.equipment_armor[0]))
                else:
                    options_str.append(
                        Separator("  -----------<Empty Armor Slot>------------  "))
                if len(self.equipment_offensive_horse) > 0:
                    options_str.append(
                        str(self.equipment_offensive_horse[0]))
                else:
                    options_str.append(
                        Separator("  -----------<Empty Horse Slot>------------  "))
                if len(self.equipment_defensive_horse) > 0:
                    options_str.append(
                        str(self.equipment_defensive_horse[0]))
                else:
                    options_str.append(
                        Separator("  -----------<Empty Horse Slot>------------  "))
                if append_judgements:
                    options_str.append(
                        Separator("-----------PENDING-JUDGEMENT-CARDS-----------"))
                    if len(self.pending_judgements) > 0:
                        for pending_judgement_card in self.pending_judgements:
                            options_str.append(str(pending_judgement_card))

            return(options_str)

    def create_nohands_menu(self, append_judgements=False):
        cards_discardable = (len(self.equipment_weapon) + len(self.equipment_armor) + len(
            self.equipment_offensive_horse) + len(self.equipment_defensive_horse))
        if append_judgements == 1:
            cards_discardable += len(self.pending_judgements)
        if cards_discardable > 0:
            options_str = []
            options_str.append(
                Separator("---------------EQUIPPED--CARDS---------------"))
            if len(self.equipment_weapon) > 0:
                options_str.append(str(self.equipment_weapon[0]))
            else:
                options_str.append(
                    Separator("  -----------<Empty Weapon Slot>-----------  "))
            if len(self.equipment_armor) > 0:
                options_str.append(str(self.equipment_armor[0]))
            else:
                options_str.append(
                    Separator("  -----------<Empty Armor Slot>------------  "))
            if len(self.equipment_offensive_horse) > 0:
                options_str.append(
                    str(self.equipment_offensive_horse[0]))
            else:
                options_str.append(
                    Separator("  -----------<Empty Horse Slot>------------  "))
            if len(self.equipment_defensive_horse) > 0:
                options_str.append(
                    str(self.equipment_defensive_horse[0]))
            else:
                options_str.append(
                    Separator("  -----------<Empty Horse Slot>------------  "))
            if append_judgements:
                options_str.append(
                    Separator("-----------PENDING-JUDGEMENT-CARDS-----------"))
                if len(self.pending_judgements) > 0:
                    for pending_judgement_card in self.pending_judgements:
                        options_str.append(str(pending_judgement_card))

            return(options_str)

# In-game Checks
    def check_break_brink_loop(self, amount_healed):
        if self.current_health + amount_healed > 0:
            return True
        else:
            return False

    def check_brink_of_death_loop(self, dying_player_index=0, source_player_index=0):
        # Backstab Kill Loop
        if self.max_health == 0:
            print(
                f"{self.character} - Your maximum health has reached 0 and therefore you are dead! - {self.character}'s role was {self.role}!")
            self.discard_all_cards(death=True)
            roles_dictionary[self.role] -= 1
            players.pop(dying_player_index)
            check_win_conditions()
            return "Break"
        elif (self.max_health != 0) and (self.current_health < 1):
            print(f"{self.character} - You are on the brink of death ({self.current_health}/{self.max_health} health), and you must be brought back to life with a PEACH or WINE.")
            reacting_player_index = dying_player_index

            # Unmitigated Murder Loop
            if players[0].check_unmitigated_murder():
                self.check_refusing_death("Brink of Death")
                self.current_health += players[0].use_reaction_effect(
                    "Brink Of Death", None, dying_player_index, reacting_player_index)
                if (players[dying_player_index].current_health < 1) and (players[0] != players[dying_player_index]):
                    self.current_health += players[dying_player_index].use_reaction_effect(
                        "Brink Of Death", 1, None, dying_player_index, reacting_player_index)

            # Regular Brink of Death Loop
            else:
                self.check_refusing_death("Brink of Death")
                for player in players[dying_player_index:]:
                    if players[dying_player_index].current_health > 0:
                        break
                    self.current_health += player.use_reaction_effect(
                        "Brink Of Death", 1, None, dying_player_index, reacting_player_index)
                    reacting_player_index += 1
                    if reacting_player_index >= len(players):
                        reacting_player_index -= len(players)
                for player in players[:dying_player_index]:
                    if players[dying_player_index].current_health > 0:
                        break
                    self.current_health += player.use_reaction_effect(
                        "Brink Of Death", 1, None, dying_player_index, reacting_player_index)
                    reacting_player_index += 1
                    if reacting_player_index >= len(players):
                        reacting_player_index -= len(players)

            # If player died
            if self.current_health < 1:
                if source_player_index != "Self":
                    players[source_player_index].check_burning_heart(
                        dying_player_index)
                print(
                    f"{self.character} wasn't saved from the brink of death! - {self.character}'s role was {self.role}!")
                self.discard_all_cards(death=True)
                if source_player_index != "Self":
                    if self.role == 'Rebel':
                        players[source_player_index].hand_cards.draw(
                            main_deck, 3, False)
                        print(
                            f"{players[source_player_index].character} draws 3 cards for killing a rebel!")
                    if self.role == 'Advisor' and players[source_player_index].role == 'Emperor':
                        print(
                            f"{players[source_player_index].character} loses all their cards for killing their Advisor.")
                        players[source_player_index].discard_all_cards()
                    self.check_heartbreak(source_player_index)
                roles_dictionary[self.role] -= 1
                players.pop(dying_player_index)
                check_win_conditions()
                return "Break"

            # If player survived
            else:
                print(
                    f"{players[dying_player_index].character} has been successfully healed back to {players[dying_player_index].current_health}/{players[dying_player_index].max_health} HP.")

    def check_pending_judgements(self):
        while len(self.pending_judgements) > 0:
            print(" ")
            main_deck.check_if_empty()
            pending_judgement = self.pending_judgements.pop(0)
            if pending_judgement.effect2 == 'Acedia':
                print(
                    f"{self.character} must face judgement for ACEDIA; (needs \u2665 to pass, or else misses action-phase of turn).")
                main_deck.discard_from_deck()
                judgement_card = discard_deck.contents[0]
                print(f"{self.character} flipped a {judgement_card}.")
                judgement_card = check_judgement_tinkering(judgement_card, 0)
                self.check_envy_of_heaven()
                self.check_exalt()
                if self.check_beauty(judgement_card):
                    if judgement_card.suit == "\u2660" or judgement_card.suit == "\u2665":
                        print(
                            f"{self.character}'s judgement card is a {judgement_card} and therefore {pending_judgement} has no effect.")
                elif judgement_card.suit == "\u2665":
                    print(
                        f"{self.character}'s judgement card is a {judgement_card} and therefore {pending_judgement} has no effect.")
                else:
                    print(
                        f"{self.character}'s judgement card is a {judgement_card} and thus they miss their action-phase of this turn.")
                    self.acedia_active = True
                discard_deck.add_to_top(pending_judgement)

            if pending_judgement.effect2 == 'Lightning':
                print(
                    f"{self.character} must face judgement for LIGHTNING; (needs anything but TWO to NINE of \u2660 or else they suffer THREE points of lightning damage)! If no hit, LIGHTNING will pass onto {players[1].character}.")
                main_deck.discard_from_deck()
                judgement_card = discard_deck.contents[0]
                print(f"{self.character} flipped a {judgement_card}.")
                judgement_card = check_judgement_tinkering(judgement_card, 0)
                self.check_envy_of_heaven()
                self.check_exalt()
                if self.check_beauty(judgement_card):
                    print(
                        f"{self.character}'s judgement card is a {judgement_card} and therefore {pending_judgement} passes on to {players[1].character}.")
                    players[1].pending_judgements.insert(0, pending_judgement)

                elif judgement_card.suit == "\u2660" and (10 > judgement_card.rank > 1):
                    print(
                        f"{self.character}'s judgement card is a {judgement_card} and therefore {pending_judgement} deals THREE DAMAGE!")
                    damage_dealt = 3
                    fantasy = self.check_fantasy(damage_dealt)
                    if not fantasy[0]:
                        self.current_health -= damage_dealt
                        if self.current_health < 1:
                            if self.check_brink_of_death_loop(0, "Self") == "Break":
                                return "Break"
                        discard_deck.add_to_top(pending_judgement)
                        self.check_bequeathed_strategy(damage_dealt)
                        self.check_eternal_loyalty(damage_dealt)
                        self.check_evil_hero(pending_judgement)
                        self.check_exile()
                        self.check_geminate(damage_dealt)
                    else:
                        redirected = fantasy[1]
                        players[redirected].current_health -= damage_dealt

                        if players[redirected].current_health < 1:
                            if players[redirected].check_brink_of_death_loop(redirected, "Self") == "Break":
                                return "Break"

                        discard_deck.add_to_top(pending_judgement)
                        players[redirected].check_bequeathed_strategy(
                            damage_dealt)
                        players[redirected].check_delayed_wisdom()
                        players[redirected].check_eternal_loyalty(damage_dealt)
                        players[redirected].check_evil_hero(pending_judgement)
                        players[redirected].check_exile()
                        players[redirected].check_geminate(damage_dealt)

                elif len(players[1].pending_judgements) > 0:
                    for possible_lightning in players[1].pending_judgements:
                        if possible_lightning.effect2 == 'Lightning':
                            if (len(players) < 3) and (players[1].check_behind_the_curtain(pending_judgement)):
                                print(
                                    f"{self.character}'s judgement card is a {judgement_card}, but there are no other players to pass to, so it stays put.")
                            else:
                                if players[1].check_behind_the_curtain(pending_judgement):
                                    print(
                                        f"{self.character} is immune to {pending_judgement} so it passes on to {players[2]}.")
                                    players[2].pending_judgements.insert(
                                        0, pending_judgement)
                                else:
                                    print(
                                        f"{self.character}'s judgement card is a {judgement_card} and therefore {pending_judgement} passes on to {players[2].character}.")
                                    players[2].pending_judgements.insert(
                                        0, pending_judgement)
                else:
                    print(
                        f"{self.character}'s judgement card is a {judgement_card} and therefore {pending_judgement} passes on to {players[1].character}.")
                    players[1].pending_judgements.insert(
                        0, pending_judgement)

            if pending_judgement.effect2 == 'Rations Depleted':
                print(
                    f"{self.character} must face judgement for RATIONS DEPLETED; (needs \u2663 to pass, or else misses drawing-phase of turn).")
                main_deck.discard_from_deck()
                judgement_card = discard_deck.contents[0]
                print(f"{self.character} flipped a {judgement_card}.")
                judgement_card = check_judgement_tinkering(judgement_card, 0)
                self.check_envy_of_heaven()
                self.check_exalt()
                self.check_beauty(judgement_card)
                if judgement_card.suit == "\u2663":
                    print(
                        f"{self.character}'s judgement card is a {judgement_card} and therefore {pending_judgement} has no effect.")
                else:
                    print(
                        f"{self.character}'s judgement card is a {judgement_card} and thus they miss their drawing-phase of this turn.")
                    self.rations_depleted_active = True
                discard_deck.add_to_top(pending_judgement)

    def check_activatable_abilities(self, types=None):
        char_abils = []
        if types == None:
            emperor_index = None
            false_ruler_index = None
            for player_index, player in enumerate(players):
                if (player.character_ability3.startswith("Amber Sky (Ruler Ability):")):
                    if player.role == "Emperor":
                        emperor_index = player_index
                    else:
                        false_ruler_index = player_index
            if self.allegiance == "Heroes":
                if (emperor_index != None) and (false_ruler_index != None):
                    char_abils.append(" Ruler Ability >> Amber Sky")
                elif emperor_index != None:
                    if self.role != "Emperor":
                        char_abils.append(" Ruler Ability >> Amber Sky")

        if types == None:
            emperor_index = None
            false_ruler_index = None
            for player_index, player in enumerate(players):
                if (player.character_ability3.startswith("Hegemony (Ruler Ability):") or player.character_ability4.startswith("Hegemony (Ruler Ability):")) or player.character_ability5.startswith("Hegemony (Ruler Ability):"):
                    if player.role == "Emperor":
                        emperor_index = player_index
                    else:
                        false_ruler_index = player_index
            if self.allegiance == "Wu":
                if (emperor_index != None) and (false_ruler_index != None):
                    char_abils.append(" Ruler Ability >> Hegemony")
                elif emperor_index != None:
                    if self.role != "Emperor":
                        char_abils.append(" Ruler Ability >> Hegemony")

            if (self.character_ability2.startswith("Alliance:") or self.character_ability3.startswith("Alliance:")):
                char_abils.append(" Character Ability >> Alliance")
            if (self.character_ability1.startswith("Benevolence:") or self.character_ability3.startswith("Benevolence:")):
                char_abils.append(" Character Ability >> Benevolence")
            if self.character_ability3.startswith("Blitz:"):
                char_abils.append(" Character Ability >> Blitz")
            if (self.character_ability1.startswith("Blockade:") or self.character_ability3.startswith("Blockade:")):
                char_abils.append(" Character Ability >> Blockade")
            if (self.character_ability1.startswith("Blunt Advice:") or self.character_ability3.startswith("Blunt Advice:")):
                char_abils.append(" Character Ability >> Blunt Advice")
            if (self.character_ability1.startswith("Brilliant Scheme:") or self.character_ability3.startswith("Brilliant Scheme")):
                char_abils.append(" Character Ability >> Brilliant Scheme")
            if (self.character_ability2.startswith("Dazzle:") or self.character_ability3.startswith("Dazzle:")):
                char_abils.append(" Character Ability >> Dazzle")
            if (self.character_ability1.startswith("Dragon Heart:") or self.character_ability3.startswith("Dragon Heart:")):
                char_abils.append(" Character Ability >> Dragon Heart")
            if (self.character_ability1.startswith("Drown in Wine:") or self.character_ability3.startswith("Drown in Wine:")):
                char_abils.append(" Character Ability >> Drown in Wine")
            if (self.character_ability1.startswith("Dual Heroes:") or self.character_ability3.startswith("Dual Heroes:")):
                if self.used_dual_heroes != False:
                    char_abils.append(" Character Ability >> Dual Heroes")
            if (self.character_ability1.startswith("Ferocious Assault:") or self.character_ability3.startswith("Ferocious Assault:")):
                char_abils.append(" Character Ability >> Ferocious Assault")
            if (self.character_ability2.startswith("Green Salve:") or self.character_ability3.startswith("Green Salve:")):
                char_abils.append(" Character Ability >> Green Salve")
            if (self.character_ability1.startswith("Heaven's Justice:") or self.character_ability3.startswith("Heaven's Justice:")):
                char_abils.append(" Character Ability >> Heaven's Justice")
            if (self.character_ability1.startswith("Horsebow:") or self.character_ability3.startswith("Horsebow:")):
                char_abils.append(" Character Ability >> Horsebow")
            if (self.character_ability1.startswith("Marriage:") or self.character_ability3.startswith("Marriage:")):
                char_abils.append(" Character Ability >> Marriage")
            if (self.character_ability1.startswith("National Colours:") or self.character_ability3.startswith("National Colours:")):
                char_abils.append(" Character Ability >> National Colours")
            if (self.character_ability1.startswith("Random Strike:") or self.character_ability3.startswith("Random Strike")):
                char_abils.append(" Character Ability >> Random Strike")
            if (self.character_ability1.startswith("Reconsider:") or self.character_ability3.startswith("Reconsider:")):
                char_abils.append(" Character Ability >> Reconsider")
            if self.character_ability3.startswith("Rejection:"):
                char_abils.append(" Character Ability >> Rejection")
            if (self.role == "Emperor" or self.character_ability2.startswith("False Ruler:") or self.character_ability3.startswith("False Ruler:")) and (self.character_ability2.startswith("Rouse (Ruler Ability):") or self.character_ability3.startswith("Rouse (Ruler Ability):") or self.character_ability4.startswith("Rouse (Ruler Ability):")):
                char_abils.append(" Ruler Ability >> Rouse")
            if (self.character_ability1.startswith("Rouse the Tiger:") or self.character_ability3.startswith("Rouse the Tiger:")):
                char_abils.append(" Character Ability >> Rouse the Tiger")
            if (self.character_ability1.startswith("Seed of Animosity:") or self.character_ability3.startswith("Seed of Animosity:")):
                char_abils.append(" Character Ability >> Seed of Animosity")
            if (self.character_ability2.startswith("Sow Dissension:") or self.character_ability3.startswith("Sow Dissension:")):
                char_abils.append(" Character Ability >> Sow Dissension")
            if (self.character_ability1.startswith("Surprise:") or self.character_ability3.startswith("Surprise:")):
                char_abils.append(" Character Ability >> Surprise")
            if (self.character_ability1.startswith("Taunt:") or self.character_ability3.startswith("Taunt:")):
                char_abils.append(" Character Ability >> Taunt")
            if (self.character_ability1.startswith("Trojan Flesh:") or self.character_ability3.startswith("Trojan Flesh:")):
                char_abils.append(" Character Ability >> Trojan Flesh")
            if self.character_ability2.startswith("Upheaval (Single-Use Ability):"):
                char_abils.append(
                    " Character Ability >> Upheaval (Single-Use Ability)")
            if (self.character_ability2.startswith("Warrior Saint:") or self.character_ability3.startswith("Warrior Saint:")):
                char_abils.append(" Character Ability >> Warrior Saint")
            return char_abils

        if types == "Attack":
            if (self.character_ability1.startswith("Dragon Heart:") or self.character_ability3.startswith("Dragon Heart:")):
                char_abils.append(" Character Ability >> Dragon Heart")
            if (self.character_ability1.startswith("Horsebow:") or self.character_ability3.startswith("Horsebow:")):
                char_abils.append(" Character Ability >> Horsebow")
            if (self.character_ability2.startswith("Warrior Saint:") or self.character_ability3.startswith("Warrior Saint:")):
                char_abils.append(" Character Ability >> Warrior Saint")
            if (self.role == "Emperor" or self.character_ability2.startswith("False Ruler:") or self.character_ability3.startswith("False Ruler:")) and (self.character_ability2.startswith("Rouse (Ruler Ability):") or self.character_ability3.startswith("Rouse (Ruler Ability):") or self.character_ability4.startswith("Rouse (Ruler Ability):")):
                char_abils.append(" Ruler Ability >> Rouse")
            return char_abils

    def reset_once_per_turn(self):
        self.attacks_this_turn = 0
        self.wine_active = False
        self.acedia_active = False
        self.rations_depleted_active = False
        self.card_double = False
        self.tools_disabled = False
        self.tools_immunity = False
        self.weapon_popped = False
        self.armor_popped = False
        self.off_horse_popped = False
        self.def_horse_popped = False

        self.used_alliance = False
        self.used_amber_sky = False
        self.used_bare_chested = False
        self.used_benevolence = False
        self.used_brilliant_scheme = False
        self.used_dazzle = False
        self.used_dual_heroes = False
        self.used_ferocious_assault = False
        self.used_green_salve = False
        self.used_heavens_justice = False
        self.used_hegemony = False
        self.used_marriage = False
        self.used_reconsider = False
        self.used_rouse_the_tiger = False
        self.used_seed_of_animosity = False
        self.used_sow_dissension = False
        self.used_taunt = False

        for player in players:
            player.used_delayed_wisdom = False

# Equipment-card checks
    def armor_black_shield(self, attack_card, source_player_index=0):
        if len(self.equipment_armor) > 0:
            if self.equipment_armor[0].effect == "Black Shield":
                if players[source_player_index].check_beauty():
                    if attack_card.suit == "\u2663":
                        print(
                            f"  >> {self.character} has {self.equipment_armor[0]} equipped, and therefore CANNOT be affected by black attack cards. ({attack_card} discarded as normal)")
                        return True

                if attack_card.suit == "\u2660" or attack_card.suit == "\u2663":
                    print(
                        f"  >> {self.character} has {self.equipment_armor[0]} equipped, and therefore CANNOT be affected by black attack cards. ({attack_card} discarded as normal)")
                    return True
            else:
                return False

    def armor_eight_trigrams(self):
        if len(self.equipment_armor) > 0:
            if self.equipment_armor[0].effect == "Eight-Trigrams":

                if self.equipment_armor[0].suit == "\u2660":
                    for player_index, player in enumerate(players):
                        if len(player.equipment_armor) > 0:
                            if player.equipment_armor[0].effect == "Eight-Trigrams" and player.equipment_armor[0].suit == "\u2660":
                                user_index = player_index
                                break

                if self.equipment_armor[0].suit == "\u2663":
                    for player_index, player in enumerate(players):
                        if len(player.equipment_armor) > 0:
                            if player.equipment_armor[0].effect == "Eight-Trigrams" and player.equipment_armor[0].suit == "\u2663":
                                user_index = player_index
                                break

                message = f"{self.character}: Choose to activate Eight-Trigrams (armor), and flip a judgement card (if red, automatically DEFEND is played)?"
                if question_yes_no(message):
                    main_deck.check_if_empty()
                    print(
                        f"  >> {self.character} chose to activate their equipped {self.equipment_armor[0]} (armor); needs \u2665 or \u2666 to automatically dodge.")
                    main_deck.discard_from_deck()
                    judgement_card = discard_deck.contents[0]
                    print(f"{self.character} flipped a {judgement_card}.")
                    judgement_card = check_judgement_tinkering(
                        judgement_card, user_index)
                    self.check_envy_of_heaven()
                    self.check_exalt()
                    if self.check_beauty(judgement_card):
                        if judgement_card.suit == "\u2660" or judgement_card.suit == "\u2665" or judgement_card.suit == "\u2666":
                            return (True, judgement_card)
                    if judgement_card.suit == "\u2665" or judgement_card.suit == "\u2666":
                        return (True, judgement_card)
                    else:
                        return (False, None)
        else:
            return (False, None)

    def check_weapon_axe(self, card, target_index=0):
        if len(self.equipment_weapon) > 0:
            if self.equipment_weapon[0].effect == "Axe":

                for player_index, player in enumerate(players):
                    if len(player.equipment_weapon) > 0:
                        if player.equipment_weapon[0].effect == "Axe":
                            user_index = player_index

                cards_discardable = (len(self.hand_cards.contents) + len(self.equipment_armor) + len(
                    self.equipment_offensive_horse) + len(self.equipment_defensive_horse))
                if cards_discardable > 1:
                    message = f"{self.character}: Would you like to discard two cards to force the damage against {players[target_index].character} ({players[target_index].current_health}/{players[target_index].max_health} HP remaining)?"
                    if question_yes_no(message):
                        num = 2
                        options_str = self.create_nonblind_menu(
                            False, False, omit_item="Weapon")
                        options = self.create_actual_menu()
                        while num > 0:
                            question = [
                                {
                                    'type': 'list',
                                    'name': 'Selected',
                                    'message': f'{self.character}: Please select card(s) to discard ({num} remaining):',
                                    'choices': options_str,
                                    'filter': lambda card: options_str.index(card)
                                },
                            ]
                            answer = prompt(question, style=custom_style_2)
                            card_index = answer.get('Selected')
                            if card_index > len(self.hand_cards.contents):
                                self.check_warrior_woman()
                            options_str.pop(card_index)
                            discarded = options.pop(card_index)
                            discard_deck.add_to_top(discarded)
                            print(
                                f"{self.character} has discarded {discarded} using {self.equipment_weapon[0]}.")
                            num -= 1
                        damage_dealt = 1
                        if self.wine_active:
                            damage_dealt = 2
                            self.wine_active = False

                        fantasy = players[target_index].check_fantasy(
                            damage_dealt, user_index)
                        if fantasy[0]:
                            target_index = fantasy[1]

                        deplete_karma = self.check_deplete_karma(
                            damage_dealt, None, target_index)
                        if deplete_karma[0]:
                            damage_dealt = deplete_karma[1]
                        deplete_karma = players[target_index].check_deplete_karma(
                            damage_dealt, user_index, None)
                        if deplete_karma[0]:
                            damage_dealt = deplete_karma[1]

                        players[target_index].current_health -= damage_dealt
                        print(
                            f"  >> {self.character} has forced the damage to {players[target_index].character}, by using {self.equipment_weapon[0]}, and discarding two cards ({players[target_index].current_health}/{players[target_index].max_health} HP remaining).")
                        self.check_insanity(target_index, damage_dealt)
                        self.check_tyrant()
                        for player_index, player in enumerate(players):
                            player.check_relief()
                            if player.current_health < 1:
                                if players[player_index].check_brink_of_death_loop(player_index, 0) == "Break":
                                    return "Break"
                        if fantasy[0]:
                            cards_to_draw = (
                                players[target_index].max_health - players[target_index].current_health)
                            print(
                                f"  >> Character Ability: Fantasy; {self.character} draws {cards_to_draw} from the deck.")
                            players[target_index].hand_cards.draw(
                                main_deck, cards_to_draw, False)
                        for player in players:
                            player.check_lament(user_index, target_index)
                        self.check_grudge(target_index, "Damage")
                        players[target_index].check_bequeathed_strategy(
                            damage_dealt)
                        players[target_index].check_delayed_wisdom()
                        players[target_index].check_eternal_loyalty(
                            damage_dealt)
                        players[target_index].check_evil_ruler(discarded)
                        players[target_index].check_exile()
                        if players[target_index].check_eye_for_an_eye(
                                source_player_index=0, mode="Activate") == "Break":
                            return "Break"
                        players[target_index].check_geminate(damage_dealt)
                        players[target_index].check_plotting_for_power(
                            damage_dealt, mode="Reaction")
                        players[target_index].check_retaliation(
                            0, damage_dealt)
                return ("Axe")

    def check_weapon_black_pommel(self):
        if len(self.equipment_weapon) > 0:
            if self.equipment_weapon[0].effect == "Black Pommel":
                return True

    def check_weapon_frost_blade(self, target_index=0, mode="Check"):
        if target_index == None:
            target_index = 0
        if mode == "Check":
            if len(self.equipment_weapon) > 0:
                if self.equipment_weapon[0].effect == "Frost Blade":
                    cards_discardable = (len(players[target_index].hand_cards.contents) + len(players[target_index].equipment_weapon) + len(
                        players[target_index].equipment_armor) + len(players[target_index].equipment_offensive_horse) + len(players[target_index].equipment_defensive_horse))
                    if cards_discardable > 1:
                        message = f"{self.character}: Would you like to force {players[target_index].character} to discard two cards instead of taking damage ({players[target_index].current_health}/{players[target_index].max_health} HP remaining)?"
                        if question_yes_no(message):
                            print(
                                f"  >> {self.character} has {self.equipment_weapon[0]} equipped, and chose to make {players[target_index].character} discard two cards instead of taking damage.")
                            players[target_index].check_weapon_frost_blade(
                                0, "Activate")
                            return True

        if mode == "Activate":
            self.discard_from_equip_or_hand(2)
            self.check_amassing_terrain()
            self.check_exertion(None, "Check")
            self.check_one_after_another()

    def check_weapon_gender_swords(self, target_index=0, mode="Check"):
        if target_index == None:
            target_index = 0
        if mode == "Check":
            if len(self.equipment_weapon) > 0:
                if self.equipment_weapon[0].effect == "Gender-Swords":
                    if self.gender != players[target_index].gender:
                        print(
                            f"  >> {self.character} has attacked {players[target_index].character} with Gender-Swords, and forced a choice!")
                        if players[target_index].check_weapon_gender_swords(self, 0, mode="Activate"):
                            self.hand_cards.draw(main_deck, 1, False)
                            print(
                                f"  >> {players[target_index].character} has decided to let {self.character} draw a card after attacking with Gender-Swords.")
                        else:
                            players[target_index].hand_cards.discard_from_hand()
                            print(
                                f"  >> {players[target_index].character} has decided to discard a hand-card after being hit by Gender-Swords.")
                            players[target_index].check_one_after_another()

        if mode == "Activate":
            options = ["Allow attacker to draw one card."]
            if len(self.hand_cards.contents) > 0:
                options.append("Discard one hand-card.")
            else:
                options.append(Separator("------No cards  to discard------"))
            question = [
                {
                    'type': 'list',
                    'name': 'Selected',
                    'message': f'{self.character}: Would you like to allow the attacker to draw a card, or yourself to discard a card?',
                    'choices': options
                },
            ]
            answer = prompt(question, style=custom_style_2)
            if answer.get('Selected') == "Allow attacker to draw one card.":
                return True
            if answer.get('Selected') == "Discard one hand-card.":
                return False

    def check_weapon_green_dragon_halberd(self, target_index=0):
        if target_index == None:
            target_index = 0
        if len(self.equipment_weapon) > 0:
            if self.equipment_weapon[0].effect == "Green Dragon Halberd":
                possible_attacks = []
                for card in self.hand_cards.contents:
                    if card.effect == "Attack":
                        possible_attacks.append(card)
                if len(possible_attacks) > 0:
                    message = f"{self.character}: Your ATTACK was defended by {players[target_index].character}. ATTACK again with Green Dragon Halberd?"
                    if question_yes_no(message):
                        options_str = self.hand_cards.list_cards()
                        options_str.append(
                            Separator("--------------------Other--------------------"))
                        options_str.append("Do nothing.")
                        question = [
                            {
                                'type': 'list',
                                'name': 'Selected',
                                'message': f'{self.character}: Select another card to ATTACK {players[target_index].character} again with Green Dragon Halberd?',
                                'choices': options_str,
                                'filter': lambda player: options_str.index(player)
                            },
                        ]
                        answer = prompt(question, style=custom_style_2)
                    card_index = answer.get('Selected')
                    if options_str[card_index] == "Do nothing.":
                        return (' ')
                    elif self.hand_cards.contents[card_index].effect == "Attack":
                        discarded = self.hand_cards.contents.pop(card_index)
                        discard_deck.add_to_top(discarded)
                        self.check_one_after_another()
                        print(
                            f"  >> {self.character} used Green Dragon Halberd to ATTACK again with {discarded}!")
                        discarded.effect2 = "Attack"
                        self.activate_attack(discarded, target_index)

    def check_weapon_huangs_longbow(self, target_index=0):
        if target_index == None:
            target_index = 0
        if len(self.equipment_weapon) > 0:
            if self.equipment_weapon[0].effect == "Huang's Longbow":
                if (len(players[target_index].equipment_offensive_horse) + len(players[target_index].equipment_defensive_horse)) > 0:
                    options_str = []
                    if len(players[target_index].equipment_offensive_horse) > 0:
                        options_str.append(
                            str(players[target_index].equipment_offensive_horse))
                    else:
                        options_str.append(
                            Separator("  -----------<Empty Horse Slot>------------  "))
                    if len(players[target_index].equipment_defensive_horse) > 0:
                        options_str.append(
                            str(players[target_index].equipment_defensive_horse))
                    else:
                        options_str.append(
                            Separator("  -----------<Empty Horse Slot>------------  "))
                    question = [
                        {
                            'type': 'list',
                            'name': 'Selected',
                            'message': f'{self.character}: Please select which horse of {players[target_index]} to slay?',
                            'choices': options_str,
                            'filter': lambda card: options_str.index(card)
                        },
                    ]
                    answer = prompt(question, style=custom_style_2)
                    slain_horse_index = answer.get('Selected')
                    if slain_horse_index == 0:
                        discarded = players[target_index].equipment_offensive_horse.pop(
                        )
                        discard_deck.add_to_top(discarded)
                        players[target_index].check_warrior_woman()
                    if slain_horse_index == 1:
                        discarded = players[target_index].equipment_defensive_horse.pop(
                        )
                        discard_deck.add_to_top(discarded)
                        players[target_index].check_warrior_woman()
                    print(
                        f"  >> {self.character} has {self.equipment_weapon[0]} equipped, and slays {discarded} of {players[target_index]} upon hit.")
                return True

    def check_weapon_serpent_spear(self, mode="Check"):
        if len(self.equipment_weapon) > 0:
            if self.equipment_weapon[0].effect == "Serpent Spear":
                if mode == "Check":
                    return True

                if mode == "Activate":
                    if self.equipment_weapon[0].effect == "Serpent Spear":
                        if len(self.hand_cards.contents) < 2:
                            print(
                                f"{self.character}: You cannot use this weapon effect as you need at least two hand-cards to do so.")
                            return [None, None, None, None, None]

                        options_str = self.create_nonblind_menu(True)
                        options_str.append(
                            Separator("--------------------Other--------------------"))
                        options_str.append("Cancel ability.")

                        question = [
                            {
                                'type': 'list',
                                'name': 'Selected',
                                'message': f'{self.character}: Please select two cards to discard and play as an ATTACK:',
                                'choices': options_str,
                                'filter': lambda card: options_str.index(card)
                            },
                        ]
                        answer = prompt(question, style=custom_style_2)
                        card1_index = answer.get('Selected')
                        if options_str[card1_index] == "Cancel ability.":
                            return [None, None, None, None, None]

                        card1 = self.hand_cards.contents[card1_index]
                        options_str.pop(card1_index)
                        options_str.insert(card1_index, Separator(
                            "------" + str(card1) + "------"))

                        question = [
                            {
                                'type': 'list',
                                'name': 'Selected',
                                'message': f'{self.character}: Please select one more card to discard and play as an ATTACK:',
                                'choices': options_str,
                                'filter': lambda card: options_str.index(card)
                            },
                        ]
                        answer = prompt(question, style=custom_style_2)
                        card2_index = answer.get('Selected')
                        if options_str[card2_index] == "Cancel ability.":
                            return [None, None, None, None, None]

                        card2 = self.hand_cards.contents[card2_index]

                        if card1.suit == "\u2660" or card1.suit == "\u2663":
                            if card2.suit == "\u2660" or card2.suit == "\u2663":
                                return ["Black Attack", card1_index, card1, card2_index, card2]

                        if card1.suit == "\u2665" or card2.suit == "\u2666":
                            if card2.suit == "\u2665" or card2.suit == "\u2666":
                                return ["Red Attack", card1_index, card1, card2_index, card2]

                        else:
                            return ["Colourless Attack", card1_index, card1, card2_index, card2]

    def check_weapon_sky_scorcher_halberd(self, target_index=0):
        if target_index == None:
            target_index = 0
        if len(self.hand_cards.contents) == 0:
            if len(self.equipment_weapon) > 0:
                if self.equipment_weapon[0].effect == "Sky Scorcher Halberd":
                    message = f"{self.character}: You used your last hand-card to ATTACK {players[target_index].character} with Sky Scorcher Halberd. Target extra players?"
                    if question_yes_no(message):
                        options = self.create_targeting_menu("Weapon")
                        options.pop(target_index)
                        options.insert(target_index, Separator(
                            "------" + str(player) + "------"))
                        options.append(
                            Separator("--------------------Other--------------------"))
                        options.append("Target noone else.")

                        question = [
                            {
                                'type': 'list',
                                'name': 'Selected',
                                'message': f'{self.character}: Select up to two extra players to ATTACK:',
                                'choices': options,
                                'filter': lambda player: options.index(player)
                            },
                        ]
                        answer = prompt(question, style=custom_style_2)
                        if options[answer.get('Selected')] == "Target noone else.":
                            return [0]
                        selected1 = answer.get('Selected')
                        options.pop(selected1)
                        options.insert(selected1, Separator(
                            "------" + str(player) + "------"))

                        question = [
                            {
                                'type': 'list',
                                'name': 'Selected',
                                'message': f'{self.character}: Select up to one more extra player to ATTACK:',
                                'choices': options,
                                'filter': lambda player: options.index(player)
                            },
                        ]
                        answer = prompt(question, style=custom_style_2)
                        if options[answer.get('Selected')] == "Target noone else.":
                            print(
                                f"  >> {self.character} used the Sky Scorcher Halberd to hit an extra player, {players[selected1].character}!!!")
                            return [1, selected1]
                        selected2 = answer.get('Selected')
                        print(
                            f"  >> {self.character} used the Sky Scorcher Halberd to hit two extra players, {players[selected1].character} and {players[selected2].character}!!!")
                        return [2, selected1, selected2]

    def check_weapon_zhuge_crossbow(self):
        if len(self.equipment_weapon) > 0:
            if self.equipment_weapon[0].effect == "Zhuge Crossbow":
                print(
                    f"  >> {self.character} has {self.equipment_weapon[0]} equipped, and therefore has no limit to the amount of attacks per turn.")
                return True

# Using cards from a players' hand
    def use_card_effect(self, card_index, card, secondary_index=None, secondary_card=None):
        if card_index == None:
            card_index = 0
        if secondary_index == None:
            secondary_index = 0
        print(" ")
        popping = False
        # Special attacks via Serpent Spear
        if card.effect2 == "Black Attack":
            if (self.attacks_this_turn == 0) or (self.check_berserk()) or (self.check_weapon_zhuge_crossbow()):
                choices_index = self.calculate_targets_in_weapon_range(
                    0)
                if len(choices_index) > 0:
                    options_str = self.create_targeting_menu("Weapon")
                    question = [
                        {
                            'type': 'list',
                            'name': 'Selected',
                            'message': f'{self.character}: Please select a character to ATTACK.',
                            'choices': options_str,
                            'filter': lambda player: options_str.index(player)
                        },
                    ]
                    answer = prompt(question, style=custom_style_2)
                    selected = answer.get('Selected')

                    if players[selected].check_empty_city():
                        return False
                    if players[selected].used_delayed_wisdom:
                        return False

                    print(f"ATTACK - Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.")
                    message = f"{self.character}: Please confirm you would like to use a BLACK ATTACK against {players[selected]}."
                    if not question_yes_no(message):
                        return False
                    else:
                        self.attacks_this_turn += 1
                        card1 = self.hand_cards.contents.pop(card_index)
                        self.hand_cards.contents.insert(
                            card_index, "Placeholder")
                        discard_deck.add_to_top(card1)
                        card2 = self.hand_cards.contents.pop(secondary_index)
                        discard_deck.add_to_top(card2)
                        self.hand_cards.contents.remove("Placeholder")
                        self.check_one_after_another()
                        self.activate_attack(card1, selected, card2)
                        if not self.card_double:
                            return True
                else:
                    print(
                        f"{self.character}: You have insufficient range to reach anyone with {card}.")
            elif (self.attacks_this_turn > 0):
                print(
                    f"{self.character}: You can only play one ATTACK card per turn.")

            if self.card_double:
                options_str = [
                    (Separator("------<Cannot target yourself>------"))]
                for player in players[1:]:
                    options_str.append(str(player))
                options_str.pop(selected)
                options_str.insert(selected, (Separator(
                    "------<Already targetted>------")))
                options_str.append(
                    Separator("--------------------Other--------------------"))
                options_str.append("Cancel Ability.")
                question = [
                    {
                        'type': 'list',
                        'name': 'Selected',
                        'message': f'{self.character}: Please select a character to ATTACK.',
                        'choices': options_str,
                        'filter': lambda player: options_str.index(player)
                    },
                ]
                answer = prompt(question, style=custom_style_2)
                selected = answer.get('Selected')
                if options_str[selected] == "Cancel Ability.":
                    return False
                if players[selected].check_empty_city():
                    return False
                if players[selected].used_delayed_wisdom:
                    return False

                print(f"ATTACK - Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.")
                message = f"{self.character}: Please confirm you would like to use a BLACK ATTACK against {players[selected]}."
                if question_yes_no(message):
                    self.activate_attack(card1, selected, card2)

        if card.effect2 == "Red Attack":
            if (self.attacks_this_turn == 0) or (self.check_berserk()) or (self.check_weapon_zhuge_crossbow()):
                choices_index = self.calculate_targets_in_weapon_range(
                    0)
                if len(choices_index) > 0:
                    options_str = self.create_targeting_menu("Weapon")
                    question = [
                        {
                            'type': 'list',
                            'name': 'Selected',
                            'message': f'{self.character}: Please select a character to ATTACK.',
                            'choices': options_str,
                            'filter': lambda player: options_str.index(player)
                        },
                    ]
                    answer = prompt(question, style=custom_style_2)
                    selected = answer.get('Selected')

                    if players[selected].check_empty_city():
                        return False
                    if players[selected].used_delayed_wisdom:
                        return False

                    print(f"ATTACK - Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.")
                    message = f"{self.character}: Please confirm you would like to use a RED ATTACK against {players[selected]}."
                    if not question_yes_no(message):
                        return False
                    else:
                        self.attacks_this_turn += 1
                        card1 = self.hand_cards.contents.pop(card_index)
                        self.hand_cards.contents.insert(
                            card_index, "Placeholder")
                        discard_deck.add_to_top(card1)
                        card2 = self.hand_cards.contents.pop(secondary_index)
                        discard_deck.add_to_top(card2)
                        self.hand_cards.contents.remove("Placeholder")
                        self.check_one_after_another()
                        self.activate_attack(card1, selected, card2)
                        if not self.card_double:
                            return True
                else:
                    print(
                        f"{self.character}: You have insufficient range to reach anyone with {card}.")
            elif (self.attacks_this_turn > 0):
                print(
                    f"{self.character}: You can only play one ATTACK card per turn.")

            if self.card_double:
                options_str = [
                    (Separator("------<Cannot target yourself>------"))]
                for player in players[1:]:
                    options_str.append(str(player))
                options_str.pop(selected)
                options_str.insert(selected, (Separator(
                    "------<Already targetted>------")))
                options_str.append(
                    Separator("--------------------Other--------------------"))
                options_str.append("Cancel Ability.")
                question = [
                    {
                        'type': 'list',
                        'name': 'Selected',
                        'message': f'{self.character}: Please select a character to ATTACK.',
                        'choices': options_str,
                        'filter': lambda player: options_str.index(player)
                    },
                ]
                answer = prompt(question, style=custom_style_2)
                selected = answer.get('Selected')
                if options_str[selected] == "Cancel Ability.":
                    return False
                if players[selected].check_empty_city():
                    return False
                if players[selected].used_delayed_wisdom:
                    return False

                print(f"ATTACK - Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.")
                message = f"{self.character}: Please confirm you would like to use a RED ATTACK against {players[selected]}."
                if question_yes_no(message):
                    self.activate_attack(card1, selected, card2)

        if card.effect2 == "Colourless Attack":
            if (self.attacks_this_turn == 0) or (self.check_berserk()) or (self.check_weapon_zhuge_crossbow()):
                choices_index = self.calculate_targets_in_weapon_range(
                    0)
                if len(choices_index) > 0:
                    options_str = self.create_targeting_menu("Weapon")
                    question = [
                        {
                            'type': 'list',
                            'name': 'Selected',
                            'message': f'{self.character}: Please select a character to ATTACK.',
                            'choices': options_str,
                            'filter': lambda player: options_str.index(player)
                        },
                    ]
                    answer = prompt(question, style=custom_style_2)
                    selected = answer.get('Selected')

                    if players[selected].check_empty_city():
                        return False
                    if players[selected].used_delayed_wisdom:
                        return False

                    print(f"ATTACK - Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.")
                    message = f"{self.character}: Please confirm you would like to use a COLOURLESS ATTACK against {players[selected]}."
                    if not question_yes_no(message):
                        return False
                    else:
                        self.attacks_this_turn += 1
                        card1 = self.hand_cards.contents.pop(card_index)
                        self.hand_cards.contents.insert(
                            card_index, "Placeholder")
                        discard_deck.add_to_top(card1)
                        card2 = self.hand_cards.contents.pop(secondary_index)
                        discard_deck.add_to_top(card2)
                        self.hand_cards.contents.remove("Placeholder")
                        self.check_one_after_another()
                        self.activate_attack(card1, selected, card2)
                        if not self.card_double:
                            return True
                else:
                    print(
                        f"{self.character}: You have insufficient range to reach anyone with {card}.")
            elif (self.attacks_this_turn > 0):
                print(
                    f"{self.character}: You can only play one ATTACK card per turn.")

            if self.card_double:
                options_str = [
                    (Separator("------<Cannot target yourself>------"))]
                for player in players[1:]:
                    options_str.append(str(player))
                options_str.pop(selected)
                options_str.insert(selected, (Separator(
                    "------<Already targetted>------")))
                options_str.append(
                    Separator("--------------------Other--------------------"))
                options_str.append("Cancel Ability.")
                question = [
                    {
                        'type': 'list',
                        'name': 'Selected',
                        'message': f'{self.character}: Please select a character to ATTACK.',
                        'choices': options_str,
                        'filter': lambda player: options_str.index(player)
                    },
                ]
                answer = prompt(question, style=custom_style_2)
                selected = answer.get('Selected')
                if options_str[selected] == "Cancel Ability.":
                    return False
                if players[selected].check_empty_city():
                    return False
                if players[selected].used_delayed_wisdom:
                    return False

                print(f"ATTACK - Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.")
                message = f"{self.character}: Please confirm you would like to use a COLOURLESS ATTACK against {players[selected]}."
                if question_yes_no(message):
                    self.activate_attack(card1, selected, card2)

        # card.type == 'Basic':
        elif card.effect2 == 'Attack':
            if (self.attacks_this_turn == 0) or (self.check_berserk()) or (self.check_weapon_zhuge_crossbow()):
                choices_index = self.calculate_targets_in_weapon_range(
                    0)
                if len(choices_index) > 0:
                    options_str = self.create_targeting_menu("Weapon")
                    question = [
                        {
                            'type': 'list',
                            'name': 'Selected',
                            'message': f'{self.character}: Please select a character to ATTACK.',
                            'choices': options_str,
                            'filter': lambda player: options_str.index(player)
                        },
                    ]
                    answer = prompt(question, style=custom_style_2)
                    selected = answer.get('Selected')

                    if players[selected].check_empty_city():
                        return False
                    if players[selected].used_delayed_wisdom:
                        return False

                    print(f"{card} - ATTACK - Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.")
                    message = f"{self.character}: Please confirm you would like to use {card} against {players[selected]}."
                    if not question_yes_no(message):
                        return False
                    else:
                        self.attacks_this_turn += 1
                        if card_index == "Special":
                            pass
                        else:
                            discard_deck.add_to_top(
                                self.hand_cards.contents.pop(card_index))
                        self.check_ardour(card)
                        self.check_one_after_another()
                        extra_targets = self.check_weapon_sky_scorcher_halberd(
                            selected)
                        if (extra_targets == None) or (extra_targets[0] == 0):
                            self.activate_attack(card, selected)
                        elif (extra_targets[0] == 1):
                            self.activate_attack(card, selected)
                            self.activate_attack(card, extra_targets[1])
                        elif (extra_targets[0] == 2):
                            self.activate_attack(card, selected)
                            self.activate_attack(card, extra_targets[1])
                            self.activate_attack(card, extra_targets[2])
                        if not self.card_double:
                            return True
                else:
                    print(
                        f"{self.character}: You have insufficient range to reach anyone with {card}.")
            elif (self.attacks_this_turn > 0):
                print(
                    f"{self.character}: You can only play one ATTACK card per turn.")

            if self.card_double:
                options_str = [
                    (Separator("------<Cannot target yourself>------"))]
                for player in players[1:]:
                    options_str.append(str(player))
                options_str.pop(selected)
                options_str.insert(selected, (Separator(
                    "------<Already targetted>------")))
                options_str.append(
                    Separator("--------------------Other--------------------"))
                options_str.append("Cancel Ability.")
                question = [
                    {
                        'type': 'list',
                        'name': 'Selected',
                        'message': f'{self.character}: Please select a character to ATTACK.',
                        'choices': options_str,
                        'filter': lambda player: options_str.index(player)
                    },
                ]
                answer = prompt(question, style=custom_style_2)
                selected = answer.get('Selected')
                if options_str[selected] == "Cancel Ability.":
                    return False
                if players[selected].check_empty_city():
                    return False
                if players[selected].used_delayed_wisdom:
                    return False

                print(f"ATTACK - Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.")
                message = f"{self.character}: Please confirm you would like to use {card} against {players[selected]}."
                if question_yes_no(message):
                    extra_targets = self.check_weapon_sky_scorcher_halberd(
                        selected)
                    if (extra_targets == None) or (extra_targets[0] == 0):
                        self.activate_attack(card, selected)
                    elif (extra_targets[0] == 1):
                        self.activate_attack(card, selected)
                        self.activate_attack(card, extra_targets[1])
                    elif (extra_targets[0] == 2):
                        self.activate_attack(card, selected)
                        self.activate_attack(card, extra_targets[1])
                        self.activate_attack(card, extra_targets[2])

        elif card.effect2 == 'Defend':
            print(
                f"{self.character}: {card} can only be played as a reaction.")

        elif card.effect2 == 'Peach':
            if self.max_health > self.current_health:
                print(f"{card} - PEACH - During your turn, you can use this card to recover one unit of missing health. Additionally, whenever a player is on the brink of death, any player can use a PEACH to make them recover one unit of health.")
                message = f"{self.character}: Please confirm you would like to use the basic card: {card.effect}."
                if question_yes_no(message):
                    if card_index == "Special":
                        discarded = card
                    else:
                        discarded = self.hand_cards.contents.pop(
                            card_index)
                    self.check_one_after_another()
                    discard_deck.add_to_top(discarded)
                    self.current_health += 1
                    print(
                        f"{self.character} has used a PEACH to heal by one from {self.current_health -1} to {self.current_health}.")
            else:
                print(
                    f"{self.character}: {card} cannot currently be used on yourself as you are at full-health.")

            if self.card_double:
                options_str = [
                    (Separator("------<Cannot target yourself>------"))]
                for player in players[1:]:
                    if player.max_health > player.current_health:
                        options_str.append(str(player))
                options_str.append(
                    Separator("--------------------Other--------------------"))
                options_str.append("Cancel Ability.")
                question = [
                    {
                        'type': 'list',
                        'name': 'Selected',
                        'message': f'{self.character}: Please select a secondary character to PEACH.',
                        'choices': options_str,
                        'filter': lambda player: options_str.index(player)
                    },
                ]
                answer = prompt(question, style=custom_style_2)
                selected = answer.get('Selected')
                if options_str[selected] == "Cancel Ability.":
                    return False
                else:
                    players[selected].current_health += 1
                    print(
                        f"{self.character} has used a PEACH to heal {players[selected]} by one from {self.current_health -1} to {self.current_health}.")
                    self.check_grudge(selected, "Heal")

        # card.type == 'Tool':
        elif card.effect2 == 'Barbarians':
            print(f"{card} - BARBARIANS - {card.flavour_text}")
            message = f"{self.character}: Please confirm you would like to use the tool card: {card.effect.upper()}."
            if question_yes_no(message):
                print(
                    f"{self.character} has activated {card}. All damaged players will take one damage (unless playing ATTACK or tool-card negated).")
                discard_deck.add_to_top(
                    self.hand_cards.contents.pop(card_index))
                self.check_one_after_another()
                self.check_wisdom()

                if self.card_double:
                    options_str = [
                        (Separator("------<Cannot target yourself>------"))]
                    for player in players[1:]:
                        options_str.append(str(player))
                    options_str.append(
                        Separator("--------------------Other--------------------"))
                    options_str.append("Cancel Ability.")
                    question = [
                        {
                            'type': 'list',
                            'name': 'Selected',
                            'message': f'{self.character}: Please select a character to prevent being affected by BARBARIANS:',
                            'choices': options_str,
                            'filter': lambda player: options_str.index(player)
                        },
                    ]
                    answer = prompt(question, style=custom_style_2)
                    selected = answer.get('Selected')
                    if options_str[selected] == "Cancel Ability.":
                        pass
                    else:
                        players[selected].tools_immunity = True

                # NEED SOME SORT OF NEGATE LOOP HERE !?!?!?
                for player_index, player in enumerate(players):
                    if (player != players[0]) and (player.current_health > 0) and (not player.tools_immunity):
                        beauty = self.check_beauty(card)
                        if (not player.check_behind_the_curtain(card, beauty)) and (not player.check_giant_elephant(card, "Reaction")) and (not player.used_delayed_wisdom):
                            barb_response = player.use_reaction_effect(
                                "Attack", 1, card, 0, player)
                            if type(barb_response) == Card:
                                if (barb_response.effect == "Attack") or (barb_response.effect2 == "Attack"):
                                    print(
                                        f"{player.character} successfully defended against BARBARIANS with {barb_response}.")
                            else:
                                print(
                                    f"{player.character} failed to defend from BARBARIANS!")
                                fantasy = players[player_index].check_fantasy(
                                    1, 0)
                                if fantasy[0]:
                                    player_index = fantasy[1]
                                    player = players[player_index]

                                damage_dealt = 1
                                deplete_karma = self.check_deplete_karma(
                                    damage_dealt, None, player_index)
                                if deplete_karma[0]:
                                    damage_dealt = deplete_karma[1]
                                deplete_karma = players[player_index].check_deplete_karma(
                                    damage_dealt, 0, None)
                                if deplete_karma[0]:
                                    damage_dealt = deplete_karma[1]

                                player.current_health -= damage_dealt
                                print(
                                    f"{player.character} takes {damage_dealt} damage ({player.current_health}/{player.max_health} HP remaining).")
                                self.check_insanity(player, damage_dealt)
                                self.check_tyrant()

                                for item in players:
                                    item.check_relief()
                                    if item.current_health < 1:
                                        item.check_brink_of_death_loop(
                                            player_index, 0)

                                if player.current_health > 0:
                                    if fantasy[0]:
                                        cards_to_draw = (
                                            player.max_health - player.current_health)
                                        print(
                                            f"  >> Character Ability: Fantasy; {player.character} draws {cards_to_draw} from the deck.")
                                        player.hand_cards.draw(
                                            main_deck, cards_to_draw, False)

                                    self.check_grudge(player_index, "Damage")
                                    player.check_bequeathed_strategy(
                                        damage_dealt)
                                    player.check_delayed_wisdom()
                                    player.check_eternal_loyalty(damage_dealt)
                                    player.check_evil_hero(card)
                                    player.check_exile()
                                    player.check_eye_for_an_eye(
                                        source_player_index=0, mode="Activate")
                                    player.check_geminate(damage_dealt)
                                    player.check_plotting_for_power(
                                        damage_dealt, mode="Reaction")
                                    player.check_retaliation(0, damage_dealt)
                for player in players:
                    player.check_giant_elephant(card, "Check")

        elif card.effect2 == 'Granary':
            print(f"{card} - GRANARY - {card.flavour_text}")
            message = f"{self.character}: Please confirm you would like to use the tool card: {card.effect}."
            if question_yes_no(message):
                print(
                    f"{self.character} has activated {card}. {len(players)} cards have been flipped from the deck. Everyone takes a card; {self.character} goes first!")
                discard_deck.add_to_top(
                    self.hand_cards.contents.pop(card_index))
                self.check_one_after_another()
                self.check_wisdom()

                if self.card_double:
                    options_str = [
                        (Separator("------<Cannot target yourself>------"))]
                    for player in players[1:]:
                        options_str.append(str(player))
                    options_str.append(
                        Separator("--------------------Other--------------------"))
                    options_str.append("Cancel Ability.")
                    question = [
                        {
                            'type': 'list',
                            'name': 'Selected',
                            'message': f'{self.character}: Please select a character to prevent being affected by GRANARY:',
                            'choices': options_str,
                            'filter': lambda player: options_str.index(player)
                        },
                    ]
                    answer = prompt(question, style=custom_style_2)
                    selected = answer.get('Selected')
                    if options_str[selected] == "Cancel Ability.":
                        pass
                    else:
                        players[selected].tools_immunity = True

                # NEED SOME SORT OF NEGATE LOOP HERE !?!?!?
                granary = Player("Temporary")
                granary.hand_cards.draw(main_deck, len(players), False)
                options_str = granary.create_nonblind_menu(
                    only_hand_cards=True)
                for player in players:
                    if not player.tools_immunity:
                        beauty = self.check_beauty(card)
                        if (not player.check_behind_the_curtain(card, beauty)) and (not player.used_delayed_wisdom):
                            question = [
                                {
                                    'type': 'list',
                                    'name': 'Selected',
                                    'message': f'{player.character}: Please select which card you would like to take:',
                                    'choices': options_str,
                                    'filter': lambda card: options_str.index(card)
                                },
                            ]
                            answer = prompt(question, style=custom_style_2)
                            card_index = answer.get('Selected')
                            drawn = granary.hand_cards.contents.pop(card_index)
                            player.hand_cards.add_to_top(drawn)
                            options_str.pop(card_index)
                            print(
                                f"{player.character} has taken {drawn} via GRANARY!")

                for item in granary.hand_cards.contents:
                    discard_deck.add_to_top(granary.hand_cards.remove_from_top)

        elif card.effect2 == 'Peach Gardens':
            print(f"{card} - PEACH GARDENS - {card.flavour_text}")
            message = f"{self.character}: Please confirm you would like to use the tool card: {card.effect}."
            if question_yes_no(message):
                print(
                    f"{self.character} has activated {card}. All damaged players will be healed by one health (unless negated).")
                discard_deck.add_to_top(
                    self.hand_cards.contents.pop(card_index))
                self.check_one_after_another()
                self.check_wisdom()

                if self.card_double:
                    options_str = [
                        (Separator("------<Cannot target yourself>------"))]
                    for player in players[1:]:
                        options_str.append(str(player))
                    options_str.append(
                        Separator("--------------------Other--------------------"))
                    options_str.append("Cancel Ability.")
                    question = [
                        {
                            'type': 'list',
                            'name': 'Selected',
                            'message': f'{self.character}: Please select a character to prevent being affected by PEACH GARDENS:',
                            'choices': options_str,
                            'filter': lambda player: options_str.index(player)
                        },
                    ]
                    answer = prompt(question, style=custom_style_2)
                    selected = answer.get('Selected')
                    if options_str[selected] == "Cancel Ability.":
                        pass
                    else:
                        players[selected].tools_immunity = True

                # NEED SOME SORT OF NEGATE LOOP HERE !?!?!?
                for player in players:
                    beauty = self.check_beauty(card)
                    if (not player.check_behind_the_curtain(card, beauty)) and (not player.used_delayed_wisdom):
                        if not player.tools_immunity:
                            if player.max_health > player.current_health:
                                player.current_health += 1
                                print(
                                    f"{player.character} has been healed by one. ({player.current_health}/{player.max_health} HP remaining)")

        elif card.effect2 == 'Rain of Arrows':
            print(
                f"{card} - RAIN OF ARROWS - All other players must play a DEFEND or else suffer one damage.")
            message = f"{self.character}: Please confirm you would like to use the tool card: RAIN OF ARROWS."
            if not question_yes_no(message):
                return False

            print(
                f"{self.character} has activated RAIN OF ARROWS. All damaged players will take one damage (unless playing DEFEND or tool-card negated).")
            if card_index == "Special":
                pass
            else:
                discard_deck.add_to_top(
                    self.hand_cards.contents.pop(card_index))
            self.check_one_after_another()
            self.check_wisdom()

            if self.card_double:
                options_str = [
                    (Separator("------<Cannot target yourself>------"))]
                for player in players[1:]:
                    options_str.append(str(player))
                options_str.append(
                    Separator("--------------------Other--------------------"))
                options_str.append("Cancel Ability.")
                question = [
                    {
                        'type': 'list',
                        'name': 'Selected',
                        'message': f'{self.character}: Please select a character to prevent being affected by RAIN OF ARROWS:',
                        'choices': options_str,
                        'filter': lambda player: options_str.index(player)
                    },
                ]
                answer = prompt(question, style=custom_style_2)
                selected = answer.get('Selected')
                if options_str[selected] == "Cancel Ability.":
                    pass
                else:
                    players[selected].tools_immunity = True

            # NEED SOME SORT OF NEGATE LOOP HERE !?!?!?
            for player_index, player in enumerate(players):
                if (player != players[0]) and (player.current_health > 0) and (not player.tools_immunity):
                    beauty = self.check_beauty(card)
                    if (not player.check_behind_the_curtain(card, beauty)) and (not player.used_delayed_wisdom):
                        roa_response = player.use_reaction_effect(
                            "Defend", 1, card, 0, player)
                        if type(roa_response) == Card:
                            if (roa_response.effect == "Defend") or (roa_response.effect2 == "Defend"):
                                print(
                                    f"{player.character} successfully defended against RAIN OF ARROWS with {roa_response}.")
                        else:
                            print(
                                f"{player.character} failed to defend from RAIN OF ARROWS.")
                            fantasy = players[player_index].check_fantasy(
                                1, 0)
                            if fantasy[0]:
                                player_index = fantasy[1]
                                player = players[player_index]

                            damage_dealt = 1
                            deplete_karma = self.check_deplete_karma(
                                damage_dealt, None, player_index)
                            if deplete_karma[0]:
                                damage_dealt = deplete_karma[1]
                            deplete_karma = players[player_index].check_deplete_karma(
                                damage_dealt, 0, None)
                            if deplete_karma[0]:
                                damage_dealt = deplete_karma[1]

                            player.current_health -= damage_dealt
                            print(
                                f"{player.character} takes {damage_dealt} damage ({player.current_health}/{player.max_health} HP remaining).")
                            self.check_insanity(player, damage_dealt)
                            self.check_tyrant()

                            for item in players:
                                item.check_relief()
                                if item.current_health < 1:
                                    item.check_brink_of_death_loop(
                                        player_index, 0)

                            if player.current_health > 0:
                                if fantasy[0]:
                                    cards_to_draw = (
                                        player.max_health - player.current_health)
                                    print(
                                        f"  >> Character Ability: Fantasy; {player.character} draws {cards_to_draw} from the deck.")
                                    player.hand_cards.draw(
                                        main_deck, cards_to_draw, False)

                                self.check_grudge(player_index, "Damage")
                                player.check_bequeathed_strategy(damage_dealt)
                                player.check_delayed_wisdom()
                                player.check_eternal_loyalty(damage_dealt)
                                player.check_evil_hero(card)
                                player.check_exile()
                                player.check_eye_for_an_eye(
                                    source_player_index=0, mode="Activate")
                                player.check_geminate(damage_dealt)
                                player.check_plotting_for_power(
                                    damage_dealt, mode="Reaction")
                                player.check_retaliation(0, damage_dealt)
            return True

        elif card.effect2 == 'Coerce':
            possible_targets = 0
            for player in players[1:]:
                if len(player.equipment_weapon) > 0:
                    possible_targets += 1

            if possible_targets == 0:
                print(
                    f"{self.character}: There are no possible targets with weapons.")
                return False

            elif possible_targets > 0:
                options_str = []
                options_str.append(
                    Separator("------<Cannot target yourself>------"))
                for player in players[1:]:
                    if len(player.equipment_weapon) > 0:
                        options_str.append(str(player))
                    else:
                        options_str.append(
                            Separator("------" + str(player) + "------"))

                question = [
                    {
                        'type': 'list',
                        'name': 'Selected',
                        'message': f'{self.character}: Please select a character to target with {card}.',
                        'choices': options_str,
                        'filter': lambda player: options_str.index(player)
                    },
                ]
                answer = prompt(question, style=custom_style_2)
                selected = answer.get('Selected')

                if players[selected].used_delayed_wisdom:
                    return False

                print(
                    f"{card} - COERCE - Use this card to target any other player that possesses a weapon. Afterwards, you can then select any target within their attacking range. Your target can then ATTACK the victim. If they do not, you will take their weapon and add it to your hand.")
                message = f"{self.character}: Please confirm you would like to use the tool card: {card} against {players[selected]}."
                if not question_yes_no(message):
                    return False

                beauty = self.check_beauty(card)
                if players[selected].check_behind_the_curtain(card, beauty):
                    return False
                if len(players[selected].calculate_targets_in_weapon_range(selected)) > 0:
                    options_str = players[selected].create_targeting_menu(
                        "Weapon", selected)
                    options_str.append(
                        Separator("--------------------Other--------------------"))
                    options_str.append("Cancel")

                    question = [
                        {
                            'type': 'list',
                            'name': 'Selected',
                            'message': f'{self.character}: Please select a target for {players[selected].character} to ATTACK!',
                            'choices': options_str,
                            'filter': lambda player: options_str.index(player)
                        },
                    ]
                    answer = prompt(question, style=custom_style_2)
                    attacked = answer.get('Selected')
                    if options_str[attacked] == "Cancel":
                        return False
                    if players[attacked].used_delayed_wisdom:
                        return False

                    else:
                        print(
                            f"{self.character} has coerced {players[selected].character} into attacking {players[attacked].character}. If they refuse, {self.character} gets their weapon.")
                        discard_deck.add_to_top(self.hand_cards.contents.pop(
                            card_index))
                        self.check_one_after_another()
                        self.check_wisdom()
                        players[selected].activate_coerce(
                            card, selected, attacked)
                        if not self.card_double:
                            return True

                        if self.card_double:
                            possible_targets -= 1
                            options_str = [
                                (Separator("------<Cannot target yourself>------"))]
                            for player in players[1:]:
                                options_str.append(str(player))
                            options_str.pop(selected)
                            options_str.insert(selected, (Separator(
                                "------<Already targetted>------")))
                            options_str.append(
                                Separator("--------------------Other--------------------"))
                            options_str.append("Cancel Ability.")
                            question = [
                                {
                                    'type': 'list',
                                    'name': 'Selected',
                                    'message': f'{self.character}: Please select a secondary character to target with {card}:',
                                    'choices': options_str,
                                    'filter': lambda player: options_str.index(player)
                                },
                            ]
                            answer = prompt(question, style=custom_style_2)
                            selected = answer.get('Selected')
                            if options_str[selected] == "Cancel Ability.":
                                return False
                            beauty = self.check_beauty(card)
                            if players[selected].check_behind_the_curtain(card, beauty):
                                return False

                            if len(players[selected].calculate_targets_in_weapon_range(selected)) > 0:
                                options_str = players[selected].create_targeting_menu(
                                    "Weapon", selected)
                                options_str.append(
                                    Separator("--------------------Other--------------------"))
                                options_str.append("Cancel")

                                question = [
                                    {
                                        'type': 'list',
                                        'name': 'Selected',
                                        'message': f'{self.character}: Please select a target for {players[selected].character} to ATTACK!',
                                        'choices': options_str,
                                        'filter': lambda player: options_str.index(player)
                                    },
                                ]
                                answer = prompt(question, style=custom_style_2)
                                attacked = answer.get('Selected')
                                if options_str[attacked] == "Cancel":
                                    return False
                                if players[attacked].used_delayed_wisdom:
                                    return False
                                else:
                                    print(
                                        f"{self.character} has coerced {players[selected].character} into attacking {players[attacked].character}. If they refuse, {self.character} gets their weapon.")
                                    discard_deck.add_to_top(self.hand_cards.contents.pop(
                                        card_index))
                                    players[selected].activate_coerce(
                                        card, selected, attacked)
                            return True

        elif card.effect2 == 'Dismantle':
            options_str = list_character_options(players)
            options_str.pop(0)
            options_str.insert(
                0, (Separator("------<Cannot target yourself>------")))
            question = [
                {
                    'type': 'list',
                    'name': 'Selected',
                    'message': f'{self.character}: Please select a character to target with {card}.',
                    'choices': options_str,
                    'filter': lambda player: options_str.index(player)
                },
            ]
            answer = prompt(question, style=custom_style_2)
            selected = answer.get('Selected')

            if players[selected].used_delayed_wisdom:
                return False

            print(
                f"{card} - DISMANTLE - You can target any player and discard one of their cards, on-hand or equipped.")
            message = f"{self.character}: Please confirm you would like to use the tool card: {card} against {players[selected]}."
            if not question_yes_no(message):
                return False
            beauty = self.check_beauty(card)
            if players[selected].check_behind_the_curtain(card, beauty):
                return False

            cards_discardable = (len(players[selected].hand_cards.contents) + len(players[selected].equipment_weapon) + len(
                players[selected].equipment_armor) + len(players[selected].equipment_offensive_horse) + len(players[selected].equipment_defensive_horse) + len(players[selected].pending_judgements))

            if cards_discardable == 0:
                print(
                    f"{players[selected].character} has no cards that can be dismantled.")
                return False

            if cards_discardable > 0:
                if card_index == "Special":
                    pass
                else:
                    discard_deck.add_to_top(
                        self.hand_cards.contents.pop(card_index))
                self.check_one_after_another()
                self.check_wisdom()
                self.activate_dismantle(card, selected)
                if not self.card_double:
                    return True

            if self.card_double:
                options_str = [
                    (Separator("------<Cannot target yourself>------"))]
                for player in players[1:]:
                    options_str.append(str(player))
                options_str.pop(selected)
                options_str.insert(selected, (Separator(
                    "------<Already targetted>------")))
                options_str.append(
                    Separator("--------------------Other--------------------"))
                options_str.append("Cancel Ability.")
                question = [
                    {
                        'type': 'list',
                        'name': 'Selected',
                        'message': f'{self.character}: Please select a secondary character to target with {card}:',
                        'choices': options_str,
                        'filter': lambda player: options_str.index(player)
                    },
                ]
                answer = prompt(question, style=custom_style_2)
                selected = answer.get('Selected')
                if options_str[selected] == "Cancel Ability.":
                    return False
                elif players[selected].used_delayed_wisdom:
                    return False
                beauty = self.check_beauty(card)
                if players[selected].check_behind_the_curtain(card, beauty):
                    return False

                cards_discardable = (len(players[selected].hand_cards.contents) + len(players[selected].equipment_weapon) + len(
                    players[selected].equipment_armor) + len(players[selected].equipment_offensive_horse) + len(players[selected].equipment_defensive_horse) + len(players[selected].pending_judgements))
                if cards_discardable == 0:
                    print(
                        f"{players[selected].character} has no cards that can be dismantled.")
                    return False
                if cards_discardable > 0:
                    self.activate_dismantle(card, selected)
                    return True

        elif card.effect2 == 'Duel':
            options_str = []
            options_str.append(
                Separator("------<Cannot target yourself>------"))
            for player in players[1:]:
                options_str.append(str(player))
            question = [
                {
                    'type': 'list',
                    'name': 'Selected',
                    'message': f'{self}: Please select a player to target with {card}.',
                    'choices': options_str,
                    'filter': lambda player: options_str.index(player)
                },
            ]
            answer = prompt(question, style=custom_style_2)
            selected = answer.get('Selected')

            if players[selected].check_empty_city():
                return False
            if players[selected].used_delayed_wisdom:
                return False

            print(f"{card} - DUEL - You can target any player for a duel with this card. If the target does not play an ATTACK, they are damaged. If they do ATTACK, then you must play one in response or take damage. Whoever does not attack, takes damage.")
            message = f"{self.character}: Please confirm you would like to use the tool card: {card} against {players[selected]}."
            if not question_yes_no(message):
                return False

            beauty = self.check_beauty(card)
            if players[selected].check_behind_the_curtain(card, beauty):
                return False

            if card_index == "Special":
                pass
            else:
                discard_deck.add_to_top(
                    self.hand_cards.contents.pop(card_index))
            print(
                f"{self.character} has challenged {players[selected].character} to a DUEL! Players must play ATTACK cards in turn, until one doesn't. The loser of the DUEL, takes one damage!")
            self.check_ardour(card)
            players[selected].check_ardour(card)
            self.check_one_after_another()
            self.activate_duel(card, selected)
            if not self.card_double:
                return True

            if self.card_double:
                options_str = [
                    (Separator("------<Cannot target yourself>------"))]
                for player in players[1:]:
                    options_str.append(str(player))
                options_str.pop(selected)
                options_str.insert(selected, (Separator(
                    "------<Already targetted>------")))
                options_str.append(
                    Separator("--------------------Other--------------------"))
                options_str.append("Cancel Ability.")
                question = [
                    {
                        'type': 'list',
                        'name': 'Selected',
                        'message': f'{self.character}: Please select a secondary character to target with {card}:',
                        'choices': options_str,
                        'filter': lambda player: options_str.index(player)
                    },
                ]
                answer = prompt(question, style=custom_style_2)
                selected = answer.get('Selected')
                if options_str[selected] == "Cancel Ability.":
                    return False
                elif players[selected].check_empty_city():
                    return False
                elif players[selected].used_delayed_wisdom:
                    return False
                beauty = self.check_beauty(card)
                if players[selected].check_behind_the_curtain(card, beauty):
                    return False

                players[selected].check_ardour(card)
                self.activate_duel(card, selected)
                return True

        elif card.effect2 == 'Negate':
            print(
                f"{self.character}: {card} can only be played as a reaction.")

        elif card.effect2 == 'Greed':
            print(f"{card} - GREED - {card.flavour_text}")
            message = f"{self.character}: Please confirm you would like to use the tool card: {card}."
            if question_yes_no(message):
                if card_index == "Special":
                    pass
                else:
                    discard_deck.add_to_top(
                        self.hand_cards.contents.pop(card_index))
                self.check_one_after_another()
                self.check_wisdom()
                print(f"{self.character} has played {card}.")
                self.hand_cards.draw(main_deck, 2)

            if self.card_double:
                options_str = [
                    (Separator("------<Cannot target yourself>------"))]
                for player in players[1:]:
                    options_str.append(str(player))
                options_str.append(
                    Separator("--------------------Other--------------------"))
                options_str.append("Cancel Ability.")
                question = [
                    {
                        'type': 'list',
                        'name': 'Selected',
                        'message': f'{self.character}: Please select a secondary character to target with {card}:',
                        'choices': options_str,
                        'filter': lambda player: options_str.index(player)
                    },
                ]
                answer = prompt(question, style=custom_style_2)
                selected = answer.get('Selected')
                if options_str[selected] == "Cancel Ability.":
                    return False
                else:
                    players[selected].hand_cards.draw(main_deck, 2, False)

        elif card.effect2 == 'Steal':
            choices_index = self.calculate_targets_in_physical_range(
                0)

            if len(choices_index) > 0:
                options_str = self.create_targeting_menu("Physical")
                stealing_possible = True

            if stealing_possible:
                question = [
                    {
                        'type': 'list',
                        'name': 'Selected',
                        'message': f'{self.character}: Please select a character to use {card} against.',
                        'choices': options_str,
                        'filter': lambda player: options_str.index(player)
                    },
                ]
                answer = prompt(question, style=custom_style_2)
                selected = answer.get('Selected')

                if players[selected].check_humility():
                    return False
                if players[selected].used_delayed_wisdom:
                    return False

                print(f"{card} - STEAL - You can use this card on a player within physical range to take a card from them (on-hand or equipped) and add it to your hand.")
                message = f"{self.character}: Please confirm you would like to use the tool card: {card} against {players[selected]}."
                if not question_yes_no(message):
                    return False
                beauty = self.check_beauty(card)
                if players[selected].check_behind_the_curtain(card, beauty):
                    return False

                cards_discardable = (len(players[selected].hand_cards.contents) + len(players[selected].equipment_weapon) + len(
                    players[selected].equipment_armor) + len(players[selected].equipment_offensive_horse) + len(players[selected].equipment_defensive_horse) + len(players[selected].pending_judgements))

                if cards_discardable == 0:
                    print(
                        f"{players[selected].character} has no cards that can be stolen.")
                    return False

                if cards_discardable > 0:
                    if card_index == "Special":
                        pass
                    else:
                        discard_deck.add_to_top(
                            self.hand_cards.contents.pop(card_index))
                    self.check_one_after_another()
                    self.check_wisdom()
                    self.activate_steal(card, selected)
                    if not self.card_double:
                        return True
            else:
                print(
                    f"{self.character}: You have insufficient range to reach anyone with {card}.")
                return False

            if self.card_double:
                options_str = [
                    (Separator("------<Cannot target yourself>------"))]
                for player in players[1:]:
                    options_str.append(str(player))
                options_str.pop(selected)
                options_str.insert(selected, (Separator(
                    "------<Already targetted>------")))
                options_str.append(
                    Separator("--------------------Other--------------------"))
                options_str.append("Cancel Ability.")
                question = [
                    {
                        'type': 'list',
                        'name': 'Selected',
                        'message': f'{self.character}: Please select a secondary character to target with {card}:',
                        'choices': options_str,
                        'filter': lambda player: options_str.index(player)
                    },
                ]
                answer = prompt(question, style=custom_style_2)
                selected = answer.get('Selected')
                if options_str[selected] == "Cancel Ability.":
                    return False
                elif players[selected].check_humility():
                    return False
                elif players[selected].used_delayed_wisdom:
                    return False
                beauty = self.check_beauty(card)
                if players[selected].check_behind_the_curtain(card, beauty):
                    return False

                cards_discardable = (len(players[selected].hand_cards.contents) + len(players[selected].equipment_weapon) + len(players[selected].equipment_armor) + len(
                    players[selected].equipment_offensive_horse) + len(players[selected].equipment_defensive_horse) + len(players[selected].pending_judgements))
                if cards_discardable == 0:
                    print(
                        f"{players[selected].character} has no cards that can be stolen.")
                    return False
                else:
                    self.activate_steal(card, selected)
                    return True

        # card.type == 'Delay-Tool':
        elif card.effect2 == 'Acedia':
            options_str = []
            options_str.append(
                Separator("------<Cannot target yourself>------"))
            for player in players[1:]:
                options_str.append(str(player))
            question = [
                {
                    'type': 'list',
                    'name': 'Selected',
                    'message': f'{self.character}: Please select a player to target with {card}.',
                    'choices': options_str,
                    'filter': lambda player: options_str.index(player)
                },
            ]
            answer = prompt(question, style=custom_style_2)
            selected = (answer.get('Selected'))
            if players[selected].check_humility():
                return False

            print(f"{card} - ACEDIA - You can place Delay-Tool on any other player. The target must perform a judgement for this card. If it is not \u2665, they forfeit their action-phase.")
            message = f"{self.character}: Please confirm you would like to use the delay-tool card {card} against {players[selected].character}."
            if not question_yes_no(message):
                return False
            beauty = self.check_beauty(card)
            if players[selected].check_behind_the_curtain(card, beauty):
                return False

            for possible_acedia in players[selected].pending_judgements:
                if possible_acedia.effect2 == 'Acedia':
                    print(
                        f"{self.character}: {players[selected].character} cannot be targeted by ACEDIA as they already have one pending.")
                    if card_index == "Special":
                        return False
                    else:
                        card = discard_deck.remove_from_top()
                        self.hand_cards.contents.append(card)

            if card_index == "Special":
                card_used = card
            else:
                card_used = self.hand_cards.contents.pop(
                    card_index)
            self.check_one_after_another()
            players[selected].pending_judgements.append(
                card_used)
            print(
                f"{self.character}: {players[selected].character} will face judgement for ACEDIA on their next turn.")
            return True

        elif card.effect2 == 'Lightning':
            for possible_lightning in self.pending_judgements:
                if possible_lightning.effect2 == 'Lightning':
                    print(
                        f"{self.character}: You cannot play a LIGHTNING when you already have one active on yourself.")
            else:
                print(f"{card} - LIGHTNING - {card.flavour_text}")
                message = f"{self.character}: Please confirm you would like to use the delay-tool card: {card.effect}."
                if question_yes_no(message):
                    beauty = self.check_beauty(card)
                    if self.check_behind_the_curtain(card, beauty):
                        return False
                    else:
                        self.pending_judgements.append(
                            self.hand_cards.contents.pop(card_index))
                    self.check_one_after_another()
                    print(f"{self.character} has called {card}.")

        elif card.effect2 == 'Rations Depleted':
            choices_index = self.calculate_targets_in_physical_range(0, +1)

            if len(choices_index) > 0:
                options_str = self.create_targeting_menu("Physical", +1)
                blockade_possible = True

            if blockade_possible:
                question = [
                    {
                        'type': 'list',
                        'name': 'Selected',
                        'message': f'{self}: Please select a player to target with {card} as RATIONS DEPLETED.',
                        'choices': options_str,
                        'filter': lambda player: options_str.index(player)
                    },
                ]
                answer = prompt(question, style=custom_style_2)
                selected = (answer.get('Selected'))

                print(f"{card} - RATIONS DEPLETED - You can place Delay-Tool on any other player in physical range. The target must perform a judgement for this card. If it is not \u2663, they forfeit their draw-phase.")
                message = f"{self.character}: Please confirm you would like to use {card} against {players[selected].character}?"
                if not question_yes_no(message):
                    return False
                beauty = self.check_beauty(card)
                if players[selected].check_behind_the_curtain(card, beauty):
                    return False

                for possible_rations_depleted in players[selected].pending_judgements:
                    if possible_rations_depleted.effect2 == 'Rations Depleted':
                        print(
                            f"{self.character}: {players[selected].character} cannot be targeted by RATIONS DEPLETED as they already have one pending.")
                    return False

                if card_index == "Special":
                    card_used = card
                self.check_one_after_another()
                players[selected].pending_judgements.append(
                    card_used)
                print(
                    f"{self.character}: {players[selected].character} will face judgement by {card_used} for RATIONS DEPLETED on their next turn.")
                return True

        # card.type == 'Equipment'
        elif card.type == 'Weapon' or card.type == 'Armor' or card.type == '+1 Horse' or card.type == '-1 Horse':
            if card.type == 'Weapon':
                if self.equipment_weapon == []:
                    message = f'{self.character}: Please confirm you would like to equip {card}.'
                    print(f"{card} - {card.flavour_text}")
                    popping = False
                else:
                    message = f'{self.character}: Please confirm you would like to equip {card} and replace {self.equipment_weapon}.'
                    print(f"{card} - {card.flavour_text}")
                    popping = True
                if question_yes_no(message):
                    if popping:
                        discarded = self.equipment_weapon.pop()
                        discard_deck.add_to_top(discarded)
                        self.check_warrior_woman()
                    self.hand_cards.contents.pop(card_index)
                    self.equipment_weapon = [card]
                    self.weapon_range = card.weapon_range
                    self.check_one_after_another()
                    print(f"{self.character} has equipped {card}.")

            if card.type == 'Armor':
                if self.equipment_armor == []:
                    message = f'{self.character}: Please confirm you would like to equip {card}.'
                    print(f"{card} - {card.flavour_text}")
                    popping = False
                else:
                    message = f'{self.character}: Please confirm you would like to equip {card} and replace {self.equipment_armor}.'
                    print(f"{card} - {card.flavour_text}")
                    popping = True
                if question_yes_no(message):
                    if popping:
                        discarded = self.equipment_armor.pop()
                        discard_deck.add_to_top(discarded)
                        self.check_warrior_woman()
                    self.hand_cards.contents.pop(card_index)
                    self.equipment_armor = [card]
                    self.check_one_after_another()
                    print(f"{self.character} has equipped {card}.")

            if card.type == '+1 Horse':
                if self.equipment_defensive_horse == []:
                    message = f'{self.character}: Please confirm you would like to equip {card}.'
                    print(f"{card} - {card.flavour_text}")
                    popping = False
                else:
                    message = f'{self.character}: Please confirm you would like to equip {card} and replace {self.equipment_defensive_horse}.'
                    print(f"{card} - {card.flavour_text}")
                    popping = True
                if question_yes_no(message):
                    if popping:
                        discarded = self.equipment_defensive_horse.pop()
                        discard_deck.add_to_top(discarded)
                        self.check_warrior_woman()
                    self.hand_cards.contents.pop(card_index)
                    self.equipment_defensive_horse = [card]
                    self.check_one_after_another()
                    print(f"{self.character} has equipped {card}.")

            if card.type == '-1 Horse':
                if self.equipment_offensive_horse == []:
                    message = f'{self.character}: Please confirm you would like to equip {card}.'
                    print(f"{card} - {card.flavour_text}")
                    popping = False
                else:
                    message = f'{self.character}: Please confirm you would like to equip {card} and replace {self.equipment_offensive_horse}.'
                    print(f"{card} - {card.flavour_text}")
                    popping = True
                if question_yes_no(message):
                    if popping:
                        discarded = self.equipment_offensive_horse.pop()
                        discard_deck.add_to_top(discarded)
                        self.check_warrior_woman()
                    self.hand_cards.contents.pop(card_index)
                    self.equipment_offensive_horse = [card]
                    self.check_one_after_another()
                    print(f"{self.character} has equipped {card}.")
        popping = False

    def use_reaction_effect(self, response_required, required=1, card_played=None, player_index=0, reacting_player_index=0, other_effect=None):
        reactions_possible = True
        output_value = 0

        while reactions_possible:
            print(" ")
            if response_required == "Brink Of Death":
                options_str = self.hand_cards.list_cards()
                options_str.append(
                    Separator("--------------------Other--------------------"))
                if (self.activate_drown_in_wine("Check")) and (self.character == players[player_index].character):
                    options_str.append(" Character Ability >> Drown in Wine")
                if self.check_first_aid(player_index, "Check"):
                    options_str.append(" Character Ability >> First Aid")
                options_str.append("Do nothing.")

                question = [
                    {
                        'type': 'list',
                        'name': 'Selected',
                        'message': f"{self.character}: {players[player_index].character} is on the brink of death; please choose a response (a PEACH card or do nothing)!",
                        'choices': options_str,
                        'filter': lambda card: options_str.index(card)
                    },
                ]
                answer = prompt(question, style=custom_style_2)
                card_index = answer.get('Selected')
                if options_str[card_index] == "Do nothing.":
                    reactions_possible = False
                    return(output_value)

                elif options_str[card_index] == " Character Ability >> Drown in Wine":
                    if self.activate_drown_in_wine("Reaction"):
                        output_value += 1
                        print(
                            f"{self.character} has healed themselves using WINE! ({players[player_index].current_health + output_value}/{players[player_index].max_health} HP remaining!)")
                        if players[player_index].check_break_brink_loop(output_value):
                            reactions_possible = False
                            return(output_value)

                elif options_str[card_index] == " Character Ability >> First Aid":
                    if (self.check_first_aid(player_index, "Reaction")):
                        output_value += 1
                        if self.character == players[player_index].character:
                            print(
                                f"{self.character} has healed themselves using a PEACH! ({players[player_index].current_health + output_value}/{players[player_index].max_health} HP remaining!)")
                        else:
                            print(
                                f"{self.character} has healed {players[player_index].character} using a PEACH. ({players[player_index].current_health + output_value}/{players[player_index].max_health} HP remaining!)")
                        self.check_grudge(player_index, "Heal")
                        if players[player_index].check_break_brink_loop(output_value):
                            reactions_possible = False
                            return(output_value)

                elif self.hand_cards.contents[card_index].effect == "Peach":
                    discarded = self.hand_cards.contents.pop(card_index)
                    if not self.amassed_terrain:
                        self.check_amassing_terrain()
                    if not self.used_cornering_maneuver:
                        self.check_cornering_maneuver(discarded)
                    self.check_one_after_another()
                    discard_deck.add_to_top(discarded)
                    output_value += 1
                    bonus_output = players[player_index].check_rescued(
                        reacting_player_index)
                    if bonus_output == 1:
                        output_value += bonus_output
                    if self.character == players[player_index].character:
                        print(
                            f"{self.character} has healed themselves using a PEACH! ({players[player_index].current_health + output_value}/{players[player_index].max_health} HP remaining!)")
                    else:
                        print(
                            f"{self.character} has healed {players[player_index].character} using a PEACH. ({players[player_index].current_health + output_value}/{players[player_index].max_health} HP remaining!)")
                    self.check_grudge(player_index, "Heal")
                    if players[player_index].check_break_brink_loop(output_value):
                        reactions_possible = False
                        return(output_value)

            elif response_required == "Defend" and ((card_played.effect2 == "Attack") or (card_played.effect2 == "Black Attack") or (card_played.effect2 == "Red Attack") or (card_played.effect2 == "Colourless Attack")):
                discarded = None
                while required > 0:
                    if card_played.effect2 == "Attack" or card_played.effect2 == "Red Attack":
                        self.check_ardour(card_played, player_index)

                    if not players[player_index].check_weapon_black_pommel():
                        armor_check = self.armor_eight_trigrams()
                        if not self.used_trigrams:
                            self.used_trigrams = True
                            if armor_check[0]:
                                self.used_trigrams = False
                                required -= 1
                                discarded = armor_check[1]

                    options_str = self.hand_cards.list_cards()
                    options_str.append(
                        Separator("--------------------Other--------------------"))
                    if self.activate_dragon_heart("Check"):
                        options_str.append(
                            " Character Ability >> Dragon Heart")
                    if self.check_impetus(player_index, "Check"):
                        options_str.append(" Character Ability >> Impetus")
                    if self.check_escort("Check"):
                        options_str.append(" Ruler Ability >> Escort")
                    options_str.append("Do nothing.")

                    if other_effect == "Escort":
                        message = f"{self.character}: You have been requested to play a DEFEND by {players[reacting_player_index].character}; please choose a response (a DEFEND card or do nothing)!"
                    elif card_played.effect2 == "Attack":
                        message = f"{self.character}: You are being attacked by {players[player_index].character} using {card_played}; please choose a response (a DEFEND card or do nothing)!"
                    else:
                        message = f"{self.character}: You are being attacked by {players[player_index].character} using a {card_played.effect2.upper()}; please choose a response (a DEFEND card or do nothing)!"

                    question = [
                        {
                            'type': 'list',
                            'name': 'Selected',
                            'message': message,
                            'choices': options_str,
                            'filter': lambda card: options_str.index(card)
                        },
                    ]
                    answer = prompt(question, style=custom_style_2)
                    card_index = answer.get('Selected')
                    if options_str[card_index] == "Do nothing.":
                        reactions_possible = False
                        return None

                    elif options_str[card_index] == " Ruler Ability >> Escort":
                        defender = self.check_escort("Reaction")
                        if defender[0]:
                            discarded = players[defender[1]].use_reaction_effect(
                                "Defend", 1, card_played, player_index, reacting_player_index, "Escort")
                            if type(discarded) == Card:
                                if (discarded.effect == "Defend") or (discarded.effect2 == "Defend"):
                                    print(
                                        f"  >> Ruler Ability: Escort; {players[defender[1]].character} has played a DEFEND on {self.character}'s behalf!")
                                    self.used_trigrams = False
                                    required -= 1

                    elif options_str[card_index] == " Character Ability >> Dragon Heart":
                        discarded = (
                            self.activate_dragon_heart("Reaction Defend"))
                        if discarded != None:
                            discarded.effect2 = "Defend"
                            if not self.used_cornering_maneuver:
                                self.check_cornering_maneuver(discarded)
                                self.used_cornering_maneuver = True
                            self.used_trigrams = False
                            required -= 1

                    elif options_str[card_index] == " Character Ability >> Impetus":
                        discarded = (self.check_impetus(
                            player_index, "Reaction"))
                        if discarded != None:
                            discarded.effect2 = "Defend"
                            self.used_trigrams = False
                            required -= 1

                    elif self.hand_cards.contents[card_index].effect == "Defend":
                        discarded = self.hand_cards.contents.pop(card_index)
                        if not self.amassed_terrain:
                            self.check_amassing_terrain()
                            self.amassed_terrain = True
                        if not self.used_cornering_maneuver:
                            self.check_cornering_maneuver(discarded)
                            self.used_cornering_maneuver = True
                        self.check_one_after_another()
                        discard_deck.add_to_top(discarded)
                        discarded.effect2 = "Defend"
                        self.used_trigrams = False
                        required -= 1

                return(discarded)

            elif response_required == "Attack" and card_played.effect2 == "Barbarians":
                options_str = self.hand_cards.list_cards()
                options_str.append(
                    Separator("--------------------Other--------------------"))
                activatable_abilities = self.check_activatable_abilities(
                    "Attack")
                for ability in activatable_abilities:
                    options_str.append(ability)
                if self.check_weapon_serpent_spear("Check"):
                    options_str.append(" Weapon Ability >> Serpent Spear")
                options_str.append("Do nothing.")

                if other_effect == "Relief":
                    message = f"{self.character}: You have opted to play an ATTACK against {players[0].character}; please choose a response (an ATTACK card or do nothing)!"
                elif other_effect == "Taunt":
                    message = f"{self.character}: You have been TAUNTED by {players[0].character}. Please choose a response (an ATTACK card or do nothing)!"
                elif other_effect == "Upheaval":
                    message = f"{self.character}: Please choose a response (an ATTACK card), or take one damage!"
                elif other_effect == "Rouse":
                    message = f"{self.character}: You have been requested to play an ATTACK by {players[reacting_player_index].character}; please choose a response (an ATTACK card or do nothing)!"
                else:
                    message = f"{self.character}: {players[player_index].character} has activated BARBARIANS; please choose a response (an ATTACK card or do nothing)!"
                question = [
                    {
                        'type': 'list',
                        'name': 'Selected',
                        'message': message,
                        'choices': options_str,
                        'filter': lambda card: options_str.index(card)
                    },
                ]
                answer = prompt(question, style=custom_style_2)
                card_index = answer.get('Selected')
                if options_str[card_index] == "Do nothing.":
                    return(0)

                elif options_str[card_index] == " Ruler Ability >> Rouse":
                    defender = self.activate_rouse("Reaction")
                    if defender[0]:
                        placeholder = Card(
                            0, 'NONE', 'NONE', 'Tool', 'Barbarians', 'NONE', None, 'Barbarians')
                        discarded = players[defender[1]].use_reaction_effect(
                            "Attack", 1, placeholder, player_index, defender[2], "Rouse")
                        if type(discarded) == Card:
                            if (discarded.effect == "Attack") or (discarded.effect2 == "Attack"):
                                print(
                                    f"  >> Ruler Ability: Rouse; {players[defender[1]].character} has played an ATTACK on {self.character}'s behalf!")
                                return(discarded)

                elif options_str[card_index] == " Character Ability >> Dragon Heart":
                    discarded = self.activate_dragon_heart("Reaction Attack")
                    if discarded != None:
                        discarded.effect2 = "Attack"
                        if not self.used_cornering_maneuver:
                            self.check_cornering_maneuver(discarded)
                            self.used_cornering_maneuver = True
                        return(discarded)

                elif options_str[card_index] == " Character Ability >> Horsebow":
                    discarded = self.activate_horsebow("Reaction")
                    if discarded != None:
                        discarded.effect2 = "Attack"
                        return(discarded)

                elif options_str[card_index] == " Character Ability >> Warrior Saint":
                    discarded = self.activate_warrior_saint("Reaction")
                    if discarded != None:
                        discarded.effect2 = "Attack"
                        return(discarded)

                elif options_str[card_index] == " Weapon Ability >> Serpent Spear":
                    attack_played = self.check_weapon_serpent_spear("Activate")
                    if attack_played[0] != None:
                        discarded1 = self.hand_cards.contents.pop(
                            attack_played[1])
                        self.hand_cards.contents.insert(
                            attack_played[1], "Placeholder")
                        discard_deck.add_to_top(discarded1)
                        discarded2 = self.hand_cards.contents.pop(
                            attack_played[3])
                        self.hand_cards.contents.remove("Placeholder")
                        if not self.amassed_terrain:
                            self.check_amassing_terrain()
                            self.amassed_terrain = True
                        if not self.used_cornering_maneuver:
                            self.check_cornering_maneuver(discarded)
                            self.used_cornering_maneuver = True
                        self.check_one_after_another()
                        discard_deck.add_to_top(discarded2)
                        discarded2.effect2 == "Attack"
                        return(discarded2)

                elif self.hand_cards.contents[card_index].effect == "Attack":
                    discarded = self.hand_cards.contents.pop(card_index)
                    if not self.amassed_terrain:
                        self.check_amassing_terrain()
                        self.amassed_terrain = True
                    if not self.used_cornering_maneuver:
                        self.check_cornering_maneuver(discarded)
                        self.used_cornering_maneuver = True
                    self.check_one_after_another()
                    discard_deck.add_to_top(discarded)
                    discarded.effect2 = "Attack"
                    return(discarded)

            elif response_required == "Defend" and card_played.effect2 == "Rain of Arrows":
                options_str = self.hand_cards.list_cards()
                options_str.append(
                    Separator("--------------------Other--------------------"))
                if self.activate_dragon_heart("Check"):
                    options_str.append(" Character Ability >> Dragon Heart")
                if self.check_impetus(player_index, "Check"):
                    options_str.append(" Character Ability >> Impetus")
                if self.check_escort("Check"):
                    options_str.append(" Ruler Ability >> Escort")
                options_str.append("Do nothing.")

                armor_check = self.armor_eight_trigrams()
                if not self.used_trigrams:
                    self.used_trigrams = True
                    if armor_check[0]:
                        self.used_trigrams = False
                        return (armor_check[1])

                if other_effect == "Escort":
                    message = f"{self.character}: You have been requested to play a DEFEND by {players[reacting_player_index].character}; please choose a response (a DEFEND card or do nothing)!"
                else:
                    message = f"{self.character}: {players[player_index].character} has activated RAIN OF ARROWS; please choose a response (a DEFEND card or do nothing)!"
                question = [
                    {
                        'type': 'list',
                        'name': 'Selected',
                        'message': message,
                        'choices': options_str,
                        'filter': lambda card: options_str.index(card)
                    },
                ]
                answer = prompt(question, style=custom_style_2)
                card_index = answer.get('Selected')
                if options_str[card_index] == "Do nothing.":
                    return(0)

                elif options_str[card_index] == " Ruler Ability >> Escort":
                    defender = self.check_escort("Reaction")
                    if defender[0]:
                        discarded = players[defender[1]].use_reaction_effect(
                            "Defend", 1, card_played, player_index, reacting_player_index, "Escort")
                        if type(discarded) == Card:
                            if (discarded.effect == "Defend") or (discarded.effect2 == "Defend"):
                                print(
                                    f"  >> Ruler Ability: Escort; {players[defender[1]].character} has played a DEFEND on {self.character}'s behalf!")
                                self.used_trigrams = False
                                return(discarded)

                elif options_str[card_index] == " Character Ability >> Dragon Heart":
                    discarded = (self.activate_dragon_heart("Reaction Defend"))
                    if discarded != None:
                        discarded.effect2 = "Defend"
                        if not self.used_cornering_maneuver:
                            self.check_cornering_maneuver(discarded)
                            self.used_cornering_maneuver = True
                        self.used_trigrams = False
                        return(discarded)

                elif options_str[card_index] == " Character Ability >> Impetus":
                    discarded = self.check_impetus(player_index, "Reaction")
                    if discarded != None:
                        discarded.effect2 = "Defend"
                        self.used_trigrams = False
                        return(discarded)

                elif self.hand_cards.contents[card_index].effect == "Defend":
                    discarded = self.hand_cards.contents.pop(card_index)
                    self.check_amassing_terrain()
                    self.check_cornering_maneuver(discarded)
                    self.check_one_after_another()
                    discard_deck.add_to_top(discarded)
                    discarded.effect2 = "Defend"
                    self.used_trigrams = False
                    return(discarded)

            elif response_required == "Attack" and card_played.effect2 == "Duel":
                enemy_attack_required = 1
                while required > 0:

                    options_str = self.hand_cards.list_cards()
                    options_str.append(
                        Separator("--------------------Other--------------------"))
                    activatable_abilities = self.check_activatable_abilities(
                        "Attack")
                    for ability in activatable_abilities:
                        options_str.append(ability)
                    if self.check_weapon_serpent_spear("Check"):
                        options_str.append(" Weapon Ability >> Serpent Spear")
                    options_str.append("Do nothing.")

                    if self.check_without_equal():
                        enemy_attack_required = 2

                    question = [
                        {
                            'type': 'list',
                            'name': 'Selected',
                            'message': f"{self.character}: You having a DUEL vs {players[player_index].character}; please choose a response (an ATTACK card or do nothing)!",
                            'choices': options_str,
                            'filter': lambda card: options_str.index(card)
                        },
                    ]
                    answer = prompt(question, style=custom_style_2)
                    card_index = answer.get('Selected')
                    if options_str[card_index] == "Do nothing.":
                        return True

                    elif options_str[card_index] == " Ruler Ability >> Rouse":
                        defender = self.activate_rouse("Reaction")
                        if defender[0]:
                            placeholder = Card(
                                0, 'NONE', 'NONE', 'Tool', 'Barbarians', 'NONE', None, 'Barbarians')
                            discarded = players[defender[1]].use_reaction_effect(
                                "Attack", 1, placeholder, player_index, reacting_player_index, "Rouse")
                            if type(discarded) == Card:
                                if (discarded.effect == "Attack") or (discarded.effect2 == "Attack"):
                                    print(
                                        f"  >> Ruler Ability: Rouse; {players[defender[1]].character} has played an ATTACK on {self.character}'s behalf!")
                                    required -= 1

                    elif options_str[card_index] == " Character Ability >> Dragon Heart":
                        discarded = self.activate_dragon_heart(
                            "Reaction Attack")
                        if not self.used_cornering_maneuver:
                            self.check_cornering_maneuver(discarded)
                            self.used_cornering_maneuver = True
                        required -= 1

                    elif options_str[card_index] == " Character Ability >> Horsebow":
                        discarded = self.activate_horsebow("Reaction")
                        required -= 1

                    elif options_str[card_index] == " Character Ability >> Warrior Saint":
                        discarded = self.activate_warrior_saint("Reaction")
                        required -= 1

                    elif options_str[card_index] == " Weapon Ability >> Serpent Spear":
                        attack_played = self.check_weapon_serpent_spear(
                            "Activate")
                        if attack_played[0] != None:
                            discarded1 = self.hand_cards.contents.pop(
                                attack_played[1])
                            self.hand_cards.contents.insert(
                                attack_played[1], "Placeholder")
                            discard_deck.add_to_top(discarded1)
                            discarded2 = self.hand_cards.contents.pop(
                                attack_played[3])
                            self.hand_cards.contents.remove("Placeholder")
                            if not self.amassed_terrain:
                                self.check_amassing_terrain()
                                self.amassed_terrain = True
                            if not self.used_cornering_maneuver:
                                self.check_cornering_maneuver(discarded)
                                self.used_cornering_maneuver = True
                            self.check_one_after_another()
                            discard_deck.add_to_top(discarded2)
                            required -= 1

                    elif self.hand_cards.contents[card_index].effect == "Attack":
                        discarded = self.hand_cards.contents.pop(card_index)
                        if not self.amassed_terrain:
                            self.check_amassing_terrain()
                            self.amassed_terrain = True
                        if not self.used_cornering_maneuver:
                            self.check_cornering_maneuver(discarded)
                            self.used_cornering_maneuver = True
                        self.check_one_after_another()
                        discard_deck.add_to_top(discarded)
                        discarded.effect2 = "Attack"
                        required -= 1

                duel_won = players[player_index].use_reaction_effect(
                    "Attack", enemy_attack_required, card_played, reacting_player_index, player_index)
                if duel_won:
                    return False
                else:
                    return True

    def activate_attack(self, discarded, selected, coerced=0, discarded2=None):
        # Early pre-reactionary effects
        redirect = players[selected].check_displacement(
            source_player_index=coerced)
        if redirect[0]:
            return self.activate_attack(discarded, redirect[1], coerced, discarded2)
        elif players[selected].check_relish(source_player_index=coerced, mode="Activate"):
            return(' ')
        elif players[selected].used_delayed_wisdom:
            return(' ')

        # Weapon and black shield checks
        self.check_weapon_gender_swords(selected)
        if (discarded2 == None) or (discarded2.effect == "Black Attack"):
            if self.check_weapon_black_pommel():
                print(
                    f"  >> {self.character} has {self.equipment_weapon[0]} equipped, and therefore ignores any armor when attacking.")
            elif players[selected].armor_black_shield(discarded, coerced):
                return(' ')

        # Undodgeable ATTACK checks
        if self.character == players[0].character:
            if self.check_fearsome_archer(discarded, discarded2, selected):
                return(' ')
        if self.check_iron_cavalry(discarded, discarded2, selected):
            return(' ')

        # Double ATTACK checks
        if self.check_without_equal("Attack") or self.check_garden_of_lust(selected):
            defend_required = 2
        else:
            defend_required = 1

        # Check for DEFEND
        attack_defended = players[selected].use_reaction_effect(
            "Defend", defend_required, discarded, coerced, selected)
        if type(attack_defended) == Card:
            if (attack_defended.effect == "Defend") or (attack_defended.effect2 == "Defend"):
                print(
                    f"{players[selected].character} successfully defended the ATTACK with {attack_defended}.")

                # DEFENDED - reactionary abilities
                players[selected].check_lightning_strike()
                self.check_weapon_axe(discarded, selected)
                self.check_fearsome_advance(
                    discarded, selected)
                self.check_weapon_green_dragon_halberd(selected)
            elif attack_defended.effect == 0:
                pass

        else:
            # DAMAGED - pre-damage abilities and damage resolution
            if self.check_weapon_frost_blade(selected, "Check"):
                return(' ')
            if self.check_backstab(discarded, discarded2, selected):
                return(' ')
            if (discarded2 == None) or (discarded2.effect2 == "Red Attack"):
                if players[selected].check_reckless(discarded, coerced):
                    return(' ')
            damage_dealt = 1
            if (self.wine_active) or (self.used_bare_chested):
                damage_dealt = 2

            fantasy = players[selected].check_fantasy(damage_dealt, coerced)
            if fantasy[0]:
                selected = fantasy[1]

            deplete_karma = self.check_deplete_karma(
                damage_dealt, None, selected)
            if deplete_karma[0]:
                damage_dealt = deplete_karma[1]
            deplete_karma = players[selected].check_deplete_karma(
                damage_dealt, 0, None)
            if deplete_karma[0]:
                damage_dealt = deplete_karma[1]

            players[selected].current_health -= damage_dealt
            print(
                f"{self.character} attacked {players[selected].character}, dealing {damage_dealt} damage. ({players[selected].current_health}/{players[selected].max_health} HP remaining)")
            self.check_weapon_huangs_longbow(selected)
            self.check_insanity(selected, damage_dealt)
            self.check_tyrant()
            self.wine_active = False

            # DAMAGED - post-damage abilities and brink of death
            for player_index, player in enumerate(players):
                player.check_relief()
                if player.current_health < 1:
                    if players[player_index].check_brink_of_death_loop(player_index, coerced) == "Break":
                        return "Break"

            if fantasy[0]:
                cards_to_draw = (
                    players[selected].max_health - players[selected].current_health)
                print(
                    f"  >> Character Ability: Fantasy; {players[selected].character} draws {cards_to_draw} from the deck.")
                players[selected].hand_cards.draw(
                    main_deck, cards_to_draw, False)

            self.check_fearsome_blade(selected)
            for player in players:
                player.check_lament(coerced, selected)
            self.check_grudge(selected, "Damage")
            players[selected].check_bequeathed_strategy(damage_dealt)
            players[selected].check_delayed_wisdom()
            players[selected].check_eternal_loyalty(
                damage_dealt)
            if (discarded.effect == "Colourless Attack") and (discarded2 == None):
                pass
            else:
                players[selected].check_evil_hero(discarded, discarded2)
            players[selected].check_exile()
            if players[selected].check_eye_for_an_eye(
                    source_player_index=coerced, mode="Activate") == "Break":
                return(' ')
            players[selected].check_geminate(damage_dealt)
            players[selected].check_plotting_for_power(
                damage_dealt, mode="Reaction")
            players[selected].check_retaliation(coerced, damage_dealt)

    def activate_coerce(self, discarded, coerced, selected=0):
        options_str = []
        options_str.append(
            Separator("--------------------Cards--------------------"))
        playing_card_options_str = self.create_nonblind_menu(True)
        for card in playing_card_options_str:
            options_str.append(card)
        options_str.append(
            Separator("--------------------Other--------------------"))
        activatable_abilities = self.check_activatable_abilities("Attack")
        for ability in activatable_abilities:
            options_str.append(ability)
        if self.check_weapon_serpent_spear("Check"):
            options_str.append(" Weapon Ability >> Serpent Spear")
        options_str.append(f"Don't attack {players[selected]}!")

        options = []
        options.append("Cards")
        for card in self.hand_cards.contents:
            options.append(card)
        options.append("Other")
        activatable_abilities = self.check_activatable_abilities("Attack")
        for ability in activatable_abilities:
            options.append(ability)
        if self.check_weapon_serpent_spear("Check"):
            options.append(" Weapon Ability >> Serpent Spear")
        options.append(f"Don't attack {players[selected]}!")

        question = [
            {
                'type': 'list',
                'name': 'Selected',
                'message': f"{self.character}: You have been targeted by {discarded} into attacking {players[selected].character}! If you don't, {players[0].character} gets your weapon. (Play an ATTACK or do nothing!)",
                'choices': options_str,
                'filter': lambda action: options_str.index(action)
            },
        ]

        answer = prompt(question, style=custom_style_2)
        action_taken_index = answer.get('Selected')

        if options[action_taken_index] == (f"Don't attack {players[selected]}!"):
            weapon = self.equipment_weapon.pop()
            self.weapon_range = 1
            players[0].hand_cards.add_to_top(weapon)
            print(
                f"{self.character}: Your weapon has been stolen by {players[0].character} for not attacking {players[selected].character}!")

        elif options[action_taken_index] == " Ruler Ability >> Rouse":
            defender = self.activate_rouse("Reaction")
            if defender[0]:
                placeholder = Card(0, 'NONE', 'NONE', 'Tool',
                                   'Barbarians', 'NONE', None, 'Barbarians')
                discarded = players[defender[1]].use_reaction_effect(
                    "Attack", 1, placeholder, coerced, defender[2], "Rouse")
                if type(discarded) == Card:
                    if (discarded.effect == "Attack") or (discarded.effect2 == "Attack"):
                        print(
                            f"  >> Ruler Ability: Rouse; {players[defender[1]].character} has played an ATTACK on {self.character}'s behalf!")
                        print(
                            f"{self.character} was coerced into attacking {players[selected]}.")
                        extra_targets = self.check_weapon_sky_scorcher_halberd(
                            selected)
                        if (extra_targets == None) or (extra_targets[0] == 0):
                            self.activate_attack(discarded, selected, coerced)
                        elif (extra_targets[0] == 1):
                            self.activate_attack(discarded, selected, coerced)
                            self.activate_attack(
                                discarded, extra_targets[1], coerced)
                        elif (extra_targets[0] == 2):
                            self.activate_attack(discarded, selected, coerced)
                            self.activate_attack(
                                discarded, extra_targets[1], coerced)
                            self.activate_attack(
                                discarded, extra_targets[2], coerced)

        elif options[action_taken_index] == " Character Ability >> Dragon Heart":
            discarded = self.activate_dragon_heart("Reaction Attack")
            if discarded != None:
                discarded.effect2 = "Attack"
                print(
                    f"{self.character} was coerced into attacking {players[selected]}.")
                extra_targets = self.check_weapon_sky_scorcher_halberd(
                    selected)
                if (extra_targets == None) or (extra_targets[0] == 0):
                    self.activate_attack(discarded, selected, coerced)
                elif (extra_targets[0] == 1):
                    self.activate_attack(discarded, selected, coerced)
                    self.activate_attack(
                        discarded, extra_targets[1], coerced)
                elif (extra_targets[0] == 2):
                    self.activate_attack(discarded, selected, coerced)
                    self.activate_attack(
                        discarded, extra_targets[1], coerced)
                    self.activate_attack(
                        discarded, extra_targets[2], coerced)

        elif options[action_taken_index] == " Character Ability >> Horsebow":
            discarded = self.activate_horsebow("Reaction")
            if discarded != None:
                print(
                    f"{self.character} was coerced into attacking {players[selected]}.")
                extra_targets = self.check_weapon_sky_scorcher_halberd(
                    selected)
                if (extra_targets == None) or (extra_targets[0] == 0):
                    self.activate_attack(discarded, selected, coerced)
                elif (extra_targets[0] == 1):
                    self.activate_attack(discarded, selected, coerced)
                    self.activate_attack(
                        discarded, extra_targets[1], coerced)
                elif (extra_targets[0] == 2):
                    self.activate_attack(discarded, selected, coerced)
                    self.activate_attack(
                        discarded, extra_targets[1], coerced)
                    self.activate_attack(
                        discarded, extra_targets[2], coerced)

        elif options[action_taken_index] == " Character Ability >> Warrior Saint":
            discarded = self.activate_warrior_saint("Reaction")
            if discarded != None:
                discarded.effect2 = "Attack"
                print(
                    f"{self.character} was coerced into attacking {players[selected]}.")
                extra_targets = self.check_weapon_sky_scorcher_halberd(
                    selected)
                if (extra_targets == None) or (extra_targets[0] == 0):
                    self.activate_attack(discarded, selected, coerced)
                elif (extra_targets[0] == 1):
                    self.activate_attack(discarded, selected, coerced)
                    self.activate_attack(
                        discarded, extra_targets[1], coerced)
                elif (extra_targets[0] == 2):
                    self.activate_attack(discarded, selected, coerced)
                    self.activate_attack(
                        discarded, extra_targets[1], coerced)
                    self.activate_attack(
                        discarded, extra_targets[2], coerced)

        elif options[action_taken_index] == " Weapon Ability >> Serpent Spear":
            attack_played = self.check_weapon_serpent_spear("Activate")
            if attack_played[0] != None:
                print(
                    f"{self.character} was coerced into attacking {players[selected]}.")
                self.check_amassing_terrain()
                discarded1 = self.hand_cards.contents.pop(
                    attack_played[1])
                self.hand_cards.contents.insert(
                    attack_played[1], "Placeholder")
                discard_deck.add_to_top(discarded1)
                discarded2 = self.hand_cards.contents.pop(
                    attack_played[3])
                self.hand_cards.contents.remove("Placeholder")
                self.check_one_after_another()
                discard_deck.add_to_top(discarded2)
                discarded1.effect1 = "Attack"
                discarded2.effect2 = "Attack"
                self.activate_attack(discarded, selected, coerced, discarded2)

        elif options[action_taken_index].effect == "Attack":
            print(
                f"{self.character} was coerced into attacking {players[selected]}.")
            discarded = options.pop(action_taken_index)
            discard_deck.add_to_top(discarded)
            discarded.effect2 = "Attack"
            self.check_ardour(discarded, coerced)
            self.check_amassing_terrain()
            self.check_one_after_another()
            extra_targets = self.check_weapon_sky_scorcher_halberd(
                selected)
            if (extra_targets == None) or (extra_targets[0] == 0):
                self.activate_attack(discarded, selected, coerced)
            elif (extra_targets[0] == 1):
                self.activate_attack(discarded, selected, coerced)
                self.activate_attack(
                    discarded, extra_targets[1], coerced)
            elif (extra_targets[0] == 2):
                self.activate_attack(discarded, selected, coerced)
                self.activate_attack(
                    discarded, extra_targets[1], coerced)
                self.activate_attack(
                    discarded, extra_targets[2], coerced)

    def activate_dismantle(self, discarded, selected=0):
        options_str = players[selected].create_semiblind_menu(True)
        question = [
            {
                'type': 'list',
                'name': 'Selected',
                'message': f'{self.character}: Please select which card you would like to destroy:',
                'choices': options_str,
                'filter': lambda card: options_str.index(card)
            },
        ]
        answer = prompt(question, style=custom_style_2)
        card_dismantled_index = answer.get('Selected')

        # Check if hand-card
        if card_dismantled_index <= len(players[selected].hand_cards.contents):
            card_dismantled = players[selected].hand_cards.contents.pop(
                card_dismantled_index)
            discard_deck.add_to_top(card_dismantled)
            print(
                f"{self.character} has destroyed {card_dismantled} from {players[selected].character}'s hand!")
            players[selected].check_amassing_terrain()
            players[selected].check_exertion(None, "Check")
            players[selected].check_one_after_another()

        # Check if equipment-card
        if card_dismantled_index > len(players[selected].hand_cards.contents):
            if card_dismantled_index == (len(players[selected].hand_cards.contents) + 1):
                card_dismantled = players[selected].equipment_weapon.pop(
                )
                discard_deck.add_to_top(card_dismantled)
                players[selected].weapon_range = 1
                print(
                    f"{self.character} has destroyed {card_dismantled} from {players[selected].character}'s weapon-slot!")
                players[selected].check_warrior_woman()

            elif card_dismantled_index == (len(players[selected].hand_cards.contents) + 2):
                card_dismantled = players[selected].equipment_armor.pop(
                )
                discard_deck.add_to_top(card_dismantled)
                print(
                    f"{self.character} has destroyed {card_dismantled} from {players[selected].character}'s armor-slot!")
                players[selected].check_warrior_woman()

            elif card_dismantled_index == (len(players[selected].hand_cards.contents) + 3):
                card_dismantled = players[selected].equipment_offensive_horse.pop(
                )
                discard_deck.add_to_top(card_dismantled)
                print(
                    f"{self.character} has destroyed {card_dismantled} from {players[selected].character}'s horse-slot!")
                players[selected].check_warrior_woman()

            elif card_dismantled_index == (len(players[selected].hand_cards.contents) + 4):
                card_dismantled = players[selected].equipment_defensive_horse.pop(
                )
                discard_deck.add_to_top(card_dismantled)
                print(
                    f"{self.character} has destroyed {card_dismantled} from {players[selected].character}'s horse-slot!")
                players[selected].check_warrior_woman()

            # Check if pending-time-delay-tool-card
            else:
                if card_dismantled_index == (len(players[selected].hand_cards.contents) + 6):
                    card_dismantled = players[selected].pending_judgements[0]
                    discard_deck.add_to_top(
                        card_dismantled)
                    print(
                        f"{self.character} has destroyed {card_dismantled} from {players[selected].character}'s pending judgements!")

                if card_dismantled_index == (len(players[selected].hand_cards.contents) + 7):
                    card_dismantled = players[selected].pending_judgements[1]
                    discard_deck.add_to_top(
                        card_dismantled)
                    print(
                        f"{self.character} has destroyed {card_dismantled} from {players[selected].character}'s pending judgements!")

                if card_dismantled_index == (len(players[selected].hand_cards.contents) + 8):
                    card_dismantled = players[selected].pending_judgements[2]
                    discard_deck.add_to_top(
                        card_dismantled)
                    print(
                        f"{self.character} has destroyed {card_dismantled} from {players[selected].character}'s pending judgements!")

    def activate_duel(self, discarded, selected, selected2=0):
        # Double ATTACK check
        attack_required = 1
        if self.check_without_equal("Duel"):
            attack_required = 2

        # Duel Effect
        duel_won = players[selected].use_reaction_effect(
            "Attack", attack_required, discarded, selected2, selected)

        # Damage/Target Alterations
        damage_dealt = 1
        if self.used_bare_chested:
            damage_dealt = 2
        if duel_won:
            fantasy = players[selected].check_fantasy(damage_dealt, 0)
            if fantasy[0]:
                selected = fantasy[1]

            deplete_karma = self.check_deplete_karma(
                damage_dealt, None, selected)
            if deplete_karma[0]:
                damage_dealt = deplete_karma[1]
            deplete_karma = players[selected].check_deplete_karma(
                damage_dealt, 0, None)
            if deplete_karma[0]:
                damage_dealt = deplete_karma[1]

            # Damage Resolution
            players[selected].current_health -= damage_dealt
            self.check_insanity(selected, damage_dealt)
            self.check_tyrant()
            print(
                f"{self.character} has won the DUEL! {players[selected].character} takes {damage_dealt} damage! ({players[selected].current_health}/{players[selected].max_health} HP remaining)")
            for player_index, player in enumerate(players):
                player.check_relief()
                if player.current_health < 1:
                    if players[player_index].check_brink_of_death_loop(player_index, 0) == "Break":
                        return (' ')

            # Retaliatory Ability Checks
            if fantasy[0]:
                cards_to_draw = (
                    players[selected].max_health - players[selected].current_health)
                print(
                    f"  >> Character Ability: Fantasy; {self.character} draws {cards_to_draw} from the deck.")
                players[selected].hand_cards.draw(
                    main_deck, cards_to_draw, False)
            self.check_grudge(selected, "Damage")
            players[selected].check_bequeathed_strategy(damage_dealt)
            players[selected].check_delayed_wisdom()
            players[selected].check_eternal_loyalty(damage_dealt)
            players[selected].check_evil_hero(discarded)
            players[selected].check_exile()
            if players[selected].check_eye_for_an_eye(
                    source_player_index=0, mode="Activate") == "Break":
                return (' ')
            players[selected].check_geminate(damage_dealt)
            players[selected].check_plotting_for_power(
                damage_dealt, mode="Reaction")
            players[selected].check_retaliation(0, damage_dealt)

        if not duel_won:
            # Damage/Target Alterations
            fantasy = self.check_fantasy(damage_dealt, selected)
            if not fantasy[0]:

                deplete_karma = self.check_deplete_karma(
                    damage_dealt, selected, None)
                if deplete_karma[0]:
                    damage_dealt = deplete_karma[1]
                deplete_karma = players[selected].check_deplete_karma(
                    damage_dealt, None, 0)
                if deplete_karma[0]:
                    damage_dealt = deplete_karma[1]

                # Damage Resolution
                self.current_health -= damage_dealt
                if selected2 == None:
                    players[selected].check_insanity(0, damage_dealt)
                else:
                    players[selected].check_insanity(selected2, damage_dealt)
                players[selected].check_tyrant()
                print(
                    f"{players[selected].character} has won the DUEL! {self.character} takes {damage_dealt} damage! ({self.current_health}/{self.max_health} HP remaining)")

                for player_index, player in enumerate(players):
                    player.check_relief()
                    if player.current_health < 1:
                        if players[player_index].check_brink_of_death_loop(player_index, 0) == "Break":
                            return (' ')

                # Retaliatory Ability Checks
                if selected2 == None:
                    players[selected].check_grudge(0, "Damage")
                else:
                    players[selected].check_grudge(selected2, "Damage")
                self.check_bequeathed_strategy(damage_dealt)
                self.check_eternal_loyalty(damage_dealt)
                self.check_evil_hero(discarded)
                self.check_exile()
                if self.check_eye_for_an_eye(
                        source_player_index=selected, mode="Activate") == "Break":
                    return (' ')
                self.check_geminate(damage_dealt)
                self.check_plotting_for_power(
                    damage_dealt, mode="Reaction")
                self.check_retaliation(0, damage_dealt)

            else:
                # Damage/Target Alterations
                redirected = fantasy[1]
                deplete_karma = self.check_deplete_karma(
                    damage_dealt, None, redirected)
                if deplete_karma[0]:
                    damage_dealt = deplete_karma[1]
                deplete_karma = players[redirected].check_deplete_karma(
                    damage_dealt, 0, None)
                if deplete_karma[0]:
                    damage_dealt = deplete_karma[1]

                # Damage Resolution
                players[redirected].current_health -= damage_dealt
                players[selected].check_insanity(
                    redirected, damage_dealt)
                players[selected].check_tyrant()
                print(
                    f"{players[selected].character} has won the DUEL! {players[redirected].character} takes {damage_dealt} damage! ({players[redirected].current_health}/{players[redirected].max_health} HP remaining)")

                for player_index, player in enumerate(players):
                    player.check_relief()
                    if player.current_health < 1:
                        if players[player_index].check_brink_of_death_loop(player_index, 0) == "Break":
                            return (' ')

                # Retaliatory Ability Checks
                cards_to_draw = (
                    players[redirected].max_health - players[redirected].current_health)
                print(
                    f"  >> Character Ability: Fantasy; {players[redirected].character} draws {cards_to_draw} from the deck.")
                players[redirected].hand_cards.draw(
                    main_deck, cards_to_draw, False)
                self.check_grudge(redirected, "Damage")
                players[redirected].check_bequeathed_strategy(damage_dealt)
                players[redirected].check_delayed_wisdom()
                players[redirected].check_eternal_loyalty(damage_dealt)
                players[redirected].check_evil_hero(discarded)
                players[redirected].check_exile()
                if players[redirected].check_eye_for_an_eye(
                        source_player_index=selected, mode="Activate") == "Break":
                    return (' ')
                players[redirected].check_geminate(damage_dealt)
                players[redirected].check_plotting_for_power(
                    damage_dealt, mode="Reaction")
                players[redirected].check_retaliation(0, damage_dealt)
        return (' ')

    def activate_steal(self, discarded, selected=0, pending_judgements=True):
        if pending_judgements:
            options_str = players[selected].create_semiblind_menu(True)
        else:
            options_str = players[selected].create_semiblind_menu(False)
        question = [
            {
                'type': 'list',
                'name': 'Selected',
                'message': f'{self.character}: Please select which card you would like to take:',
                'choices': options_str,
                'filter': lambda card: options_str.index(card)
            },
        ]
        answer = prompt(question, style=custom_style_2)
        card_stolen_index = answer.get('Selected')

        # Check if hand-card
        if card_stolen_index <= len(players[selected].hand_cards.contents):
            card_stolen = players[selected].hand_cards.contents.pop(
                card_stolen_index)
            self.hand_cards.add_to_top(card_stolen)
            print(
                f"{self.character} has taken {card_stolen} from {players[selected].character}'s hand!")
            players[selected].check_amassing_terrain()
            players[selected].check_exertion(None, "Check")
            players[selected].check_one_after_another()

        # Check if equipment-card
        if card_stolen_index > len(players[selected].hand_cards.contents):
            if card_stolen_index == (len(players[selected].hand_cards.contents) + 1):
                card_stolen = players[selected].equipment_weapon.pop(
                )
                players[selected].weapon_range = 1
                self.hand_cards.add_to_top(card_stolen)
                print(
                    f"{self.character} has taken {card_stolen} from {players[selected].character}'s weapon-slot!")
                players[selected].check_warrior_woman()

            elif card_stolen_index == (len(players[selected].hand_cards.contents) + 2):
                card_stolen = players[selected].equipment_armor.pop(
                )
                self.hand_cards.add_to_top(card_stolen)
                print(
                    f"{self.character} has taken {card_stolen} from {players[selected].character}'s armor-slot!")
                players[selected].check_warrior_woman()

            elif card_stolen_index == (len(players[selected].hand_cards.contents) + 3):
                card_stolen = players[selected].equipment_offensive_horse.pop(
                )
                self.hand_cards.add_to_top(card_stolen)
                print(
                    f"{self.character} has taken {card_stolen} from {players[selected].character}'s horse-slot!")
                players[selected].check_warrior_woman()

            elif card_stolen_index == (len(players[selected].hand_cards.contents) + 4):
                card_stolen = players[selected].equipment_defensive_horse.pop(
                )
                self.hand_cards.add_to_top(card_stolen)
                print(
                    f"{self.character} has taken {card_stolen} from {players[selected].character}'s horse-slot!")
                players[selected].check_warrior_woman()

            # Check if pending-time-delay-tool-card
            else:
                if card_stolen_index == (len(players[selected].hand_cards.contents) + 6):
                    card_stolen = players[selected].pending_judgements[0]
                    self.hand_cards.add_to_top(card_stolen)
                    print(
                        f"{self.character} has taken {card_stolen} from {players[selected].character}'s pending judgements!")

                if card_stolen_index == (len(players[selected].hand_cards.contents) + 7):
                    card_stolen = players[selected].pending_judgements[1]
                    self.hand_cards.add_to_top(card_stolen)
                    print(
                        f"{self.character} has taken {card_stolen} from {players[selected].character}'s pending judgements!")

                if card_stolen_index == (len(players[selected].hand_cards.contents) + 8):
                    card_stolen = players[selected].pending_judgements[2]
                    self.hand_cards.add_to_top(card_stolen)
                    print(
                        f"{self.character} has taken {card_stolen} from {players[selected].character}'s pending judgements!")

    def activate_compete(self):
        options = self.create_nonblind_menu(True)
        question = [
            {
                'type': 'list',
                'name': 'Selected',
                'message': f'{self.character}: Please select a card to use for your COMPETITION:',
                'choices': options,
                'filter': lambda card: options.index(card)
            },
        ]
        answer = prompt(question, style=custom_style_2)
        my_card_index = answer.get('Selected')
        card = self.hand_cards.contents.pop(my_card_index)
        discard_deck.add_to_top(card)
        if not self.amassed_terrain:
            self.check_amassing_terrain()
            self.amassed_terrain = True
        if not self.used_cornering_maneuver:
            self.check_cornering_maneuver(card)
            self.used_cornering_maneuver = True
        self.check_one_after_another()
        return card

# Discarding cards (to use primarily as player-effects)
    def discard_from_hand_boolpop(self, suit1=None, suit2=None):
        options_str = self.create_nonblind_menu(True)
        if (suit1 != None) and (suit2 != None):
            message = f"{self.character}: Please select a card of suits, {suit1} or {suit2}:"
        elif (suit1 != None):
            message = f"{self.character}: Please select a card to discard of suit: {suit1}:"
        else:
            message = f"{self.character}: Please select a card to discard; from your hand:"
        question = [
            {
                'type': 'list',
                'name': 'Selected',
                'message': message,
                'choices': options_str,
                'filter': lambda card: options_str.index(card)
            }
        ]
        answer = prompt(question, style=custom_style_2)
        discarded_index = answer.get('Selected')

        # Check if hand-card
        if discarded_index < len(self.hand_cards.contents):
            card = self.hand_cards.contents[discarded_index]
            if (card.suit == suit1) or (card.suit == suit2):
                self.hand_cards.contents.pop(discarded_index)
                discard_deck.add_to_top(card)
                self.check_one_after_another()
                return card

    def discard_from_equip_or_hand_boolpop(self, suit1=None, suit2=None):
        options_str = self.create_nonblind_menu()
        if (suit1 != None) and (suit2 != None):
            message = f"{self.character}: Please select a card of suits: {suit1} or {suit2};"
        elif (suit1 != None):
            message = f"{self.character}: Please select a card to discard of suit: {suit1};"
        else:
            message = f"{self.character}: Please select a card to discard; from your hand or your equipment area."
        question = [
            {
                'type': 'list',
                'name': 'Selected',
                'message': message,
                'choices': options_str,
                'filter': lambda card: options_str.index(card)
            }
        ]
        answer = prompt(question, style=custom_style_2)
        discarded_index = answer.get('Selected')

        # Check if hand-card
        if discarded_index < len(self.hand_cards.contents):
            card = self.hand_cards.contents[discarded_index]
            if card.suit == suit1 or card.suit == suit2:
                self.hand_cards.contents.pop(discarded_index)
                discard_deck.add_to_top(card)
                self.check_one_after_another()
                return card

        # Check if equipment-card
        else:
            if discarded_index == (len(self.hand_cards.contents) + 1):
                card = self.equipment_weapon[0]
                if card.suit == suit1 or card.suit == suit2:
                    self.equipment_weapon.pop()
                    self.weapon_popped = True
                    discard_deck.add_to_top(card)
                    self.weapon_range = 1
                    print(
                        f"{self.character} has discarded {card} from their weapon-slot.")

            if discarded_index == (len(self.hand_cards.contents) + 2):
                card = self.equipment_armor[0]
                if card.suit == suit1 or card.suit == suit2:
                    self.equipment_armor.pop()
                    self.armor_popped = True
                    discard_deck.add_to_top(card)
                    print(
                        f"{self.character} has discarded {card} from their armor-slot.")

            if discarded_index == (len(self.hand_cards.contents) + 3):
                card = self.equipment_offensive_horse[0]
                if card.suit == suit1 or card.suit == suit2:
                    self.equipment_offensive_horse.pop()
                    self.off_horse_popped = True
                    discard_deck.add_to_top(card)
                    print(
                        f"{self.character} has discarded {card} from their horse-slot.")

            if discarded_index == (len(self.hand_cards.contents) + 4):
                card = self.equipment_defensive_horse[0]
                if card.suit == suit1 or card.suit == suit2:
                    self.equipment_defensive_horse.pop()
                    self.def_horse_popped = True
                    discard_deck.add_to_top(card)
                    print(
                        f"{self.character} has discarded {card} from their horse-slot.")

            self.check_warrior_woman()
            return card

    def discard_from_equip_or_hand(self, num=1):
        while num > 0:
            options_str = self.create_nonblind_menu()
            question = [
                {
                    'type': 'list',
                    'name': 'Selected',
                    'message': f'{self.character}: Please select a card to discard; from your hand or your equipment area.',
                    'choices': options_str,
                    'filter': lambda card: options_str.index(card)
                }
            ]

            answer = prompt(question, style=custom_style_2)
            discarded_index = answer.get('Selected')

            # Check if hand-card
            if discarded_index < len(self.hand_cards.contents):
                card = self.hand_cards.contents.pop(discarded_index)
                discard_deck.add_to_top(card)
                self.check_one_after_another()

            # Check if equipment-card
            else:
                if discarded_index == (len(self.hand_cards.contents) + 1):
                    card = self.equipment_weapon.pop()
                    discard_deck.add_to_top(card)
                    self.weapon_range = 1
                    print(
                        f"{self.character} has discarded {card} from their weapon-slot.")

                if discarded_index == (len(self.hand_cards.contents) + 2):
                    card = self.equipment_armor.pop()
                    discard_deck.add_to_top(card)
                    print(
                        f"{self.character} has discarded {card} from their armor-slot.")

                if discarded_index == (len(self.hand_cards.contents) + 3):
                    card = self.equipment_offensive_horse.pop()
                    discard_deck.add_to_top(card)
                    print(
                        f"{self.character} has discarded {card} from their horse-slot.")

                if discarded_index == (len(self.hand_cards.contents) + 4):
                    card = self.equipment_defensive_horse.pop()
                    discard_deck.add_to_top(card)
                    print(
                        f"{self.character} has discarded {card} from their horse-slot.")
                self.check_warrior_woman()
            num -= 1
        return card

    def discard_all_cards(self, death=False):
        cards_discarded = (len(self.hand_cards.contents) + len(self.equipment_weapon) + len(
            self.equipment_armor) + len(self.equipment_offensive_horse) + len(self.equipment_defensive_horse))
        while len(self.hand_cards.contents) > 0:
            discard_deck.add_to_top(self.hand_cards.contents.pop())
        if len(self.equipment_weapon) == 1:
            discard_deck.add_to_top(self.equipment_weapon.pop())
        if len(self.equipment_armor) == 1:
            discard_deck.add_to_top(self.equipment_armor.pop())
        if len(self.equipment_offensive_horse) == 1:
            discard_deck.add_to_top(self.equipment_offensive_horse.pop())
        if len(self.equipment_defensive_horse) == 1:
            discard_deck.add_to_top(self.equipment_defensive_horse.pop())
        if death == False:
            self.check_amassing_terrain()
            self.check_exertion(None, "Check")
            self.check_one_after_another()
        if death:
            for card in self.refusing_death:
                discard_deck.add_to_top(card)
            for card in self.rites:
                discard_deck.add_to_top(card)
            for card in self.terrains:
                discard_deck.add_to_top(card)
            print(
                f"{self.character} discarded {cards_discarded} card(s) upon their death.")
            for player in players:
                if player != "Placeholder":
                    player.check_unnatural_death(cards_discarded)
            while len(self.pending_judgements) > 0:
                discard_deck.add_to_top(self.pending_judgements.pop())

# Ability checks
    def check_altruism(self):
        # "Altruism: In the drawing phase, you can choose to draw two more cards (total of four cards). If you have more than five on-hand cards as a result, you must give half of your on-hand cards (rounded down to a whole number) to the player with the least on-hand cards (excluding yourself)."
        if (self.character_ability1.startswith("Altruism:") or self.character_ability3.startswith("Altruism:")):
            message = f"{self.character}: Choose to activate Altruism, and draw 2 additional cards? If you have more than 5 afterwards, you must give half of your hand the player with the last cards:"
            if question_yes_no(message):
                print(
                    f"  >> Character Ability: Altruism; {self.character} draws two extra cards from the deck (total of four) in their drawing phase.")
                self.hand_cards.draw(main_deck, 4, False)

                my_hand_size = len(self.hand_cards.contents)
                if my_hand_size > 5:
                    if my_hand_size % 2 == 0:
                        cards_to_give = int(my_hand_size / 2)
                    else:
                        my_hand_size -= 1
                        cards_to_give = int(my_hand_size / 2)

                    hand_sizes = []
                    for player in players:
                        hand_sizes.append(len(player.hand_cards.contents))

                    min_sizes = []
                    for player_index, size in enumerate(hand_sizes):
                        if size == min(hand_sizes):
                            min_sizes.append(str(players[player_index]))
                        else:
                            min_sizes.append(
                                Separator("------" + str(players[player_index]) + "------"))

                    question = [
                        {
                            'type': 'list',
                            'name': 'Selected',
                            'message': f'{self.character}: Please select a player to give half of your hand-cards to:',
                            'choices': min_sizes,
                            'filter': lambda player: min_sizes.index(player)
                        },
                    ]
                    answer = prompt(question, style=custom_style_2)
                    selected_index = answer.get('Selected')
                    print(
                        f"  >> Character Ability: Altruism; {self.character} has to give {players[selected_index].character} half of his hand-cards!")
                    while cards_to_give > 0:
                        options = self.create_nonblind_menu(True)
                        question = [
                            {
                                'type': 'list',
                                'name': 'Selected',
                                'message': f'{self.character}: Please select a card to give to {players[selected_index].character} ({cards_to_give} remaining):',
                                'choices': options,
                                'filter': lambda card: options.index(card)
                            },
                        ]
                        answer = prompt(question, style=custom_style_2)
                        given_index = answer.get('Selected')
                        given = self.hand_cards.contents.pop(given_index)
                        players[selected_index].hand_cards.add_to_top(given)
                        cards_to_give -= 1
                return True

    def check_amassing_terrain(self):
        # "Amassing Terrain: Every instance that you use or lose cards outside of your turn, you can flip a judgement card. If the judgement is not \u2665, you can place the judgement card (referred to as a TERRAIN) atop your character card. For every TERRAIN that you gain, your physical distance to other players is considered -1."
        if (self.character_ability1.startswith("Amassing Terrain:") or self.character_ability3.startswith("Amassing Terrain:")):

            for player_index, player in enumerate(players):
                if (player.character_ability1.startswith("Amassing Terrain:") or player.character_ability3.startswith("Amassing Terrain:")):
                    user_index = player_index
                    break

            if self.character != players[0].character:
                message = f"{self.character}: You used or lost a card outside of your turn; flip a judgement with a chance to gain a TERRAIN?"
                if question_yes_no(message):
                    print(
                        f"  >> Character Ability: Amassing Terrain; {self.character} has used or lost a card outside their turn. They can flip a judgement. If \u2665, they gain a TERRAIN!")
                    main_deck.check_if_empty()
                    main_deck.discard_from_deck()
                    judgement_card = discard_deck.contents[0]
                    self.check_exalt()
                    print(f"{self.character} flipped a {judgement_card}.")
                    judgement_card = check_judgement_tinkering(
                        judgement_card, user_index)
                    if judgement_card.suit != "\u2665":
                        terrain = discard_deck.remove_from_top()
                        self.terrains.append(terrain)
                        print(
                            f"  >> Character Ability: Amassing Terrain; {self.character} has gained a TERRAIN: {terrain}!")
                    else:
                        print(
                            f"  >> Character Ability: Amassing Terrain; Nothing happens...")
                return True

    def check_ardour(self, card, source_player_index=0):
        # "Ardour: Whenever you use or become the target of any DUEL or red-suited ATTACK cards, you can draw a card."
        if (self.character_ability1.startswith("Ardour:") or self.character_ability3.startswith("Ardour:")):
            if players[source_player_index].check_beauty(card):
                if (card.effect == "Duel") or (card.effect == "Attack" and (card.suit == "\u2660" or card.suit == "\u2665" or card.suit == "\u2666")):
                    print(
                        f"  >> Character Ability: Ardour; {self.character} used or was target of {card} (a DUEL or red-suited ATTACK). He draws a card.")
                    self.hand_cards.draw(main_deck, 1, False)
            if (card.effect == "Duel") or (card.effect == "Attack" and (card.suit == "\u2665" or card.suit == "\u2666")):
                print(
                    f"  >> Character Ability: Ardour; {self.character} used or was target of {card} (a DUEL or red-suited ATTACK). He draws a card.")
                self.hand_cards.draw(main_deck, 1, False)

    def check_astrology(self):
        # "Astrology: Before your judgement phase, you can view the top X cards of the deck (X being the number of players still in play, with a maximum of five). Of these X cards, you can rearrange the order of the cards, and choose any number to place at the top or bottom of the draw-deck."
        if (self.character_ability1.startswith("Astrology:") or self.character_ability3.startswith("Astrology:")):
            message = f"{self.character}: Choose to activate Astrology to view the top X cards of the deck, and rearrange them to the top or bottom of the deck?"
            if question_yes_no(message):

                cards_viewed = len(players)
                if cards_viewed > 4:
                    cards_viewed = 5
                astrology = Player("Temporary")
                astrology.hand_cards.draw(main_deck, cards_viewed, False)
                for item in range(cards_viewed):
                    options = astrology.create_nonblind_menu(True)
                    question = [
                        {
                            'type': 'list',
                            'name': 'Selected',
                            'message': f'{self.character}: Please select a card to add to the top/bottom of deck (note: first card in, last card out):',
                            'choices': options,
                            'filter': lambda card: options.index(card)
                        },
                    ]
                    answer = prompt(question, style=custom_style_2)
                    card_index = answer.get('Selected')
                    question = [
                        {
                            'type': 'list',
                            'name': 'Selected',
                            'message': f'{self.character}: Please decide whether you want to add {astrology.hand_cards.contents[card_index]} to the top or the bottom of the deck:',
                            'choices': ["Add to top.", "Add to bottom."]
                        },
                    ]
                    answer = prompt(question, style=custom_style_2)
                    if answer.get('Selected') == "Add to top.":
                        main_deck.add_to_top(
                            astrology.hand_cards.contents.pop())
                    else:
                        main_deck.add_to_bottom(
                            astrology.hand_cards.contents.pop())
                print(
                    f"  >> Character Ability: Astrology; {self.character} has rearranged the top {cards_viewed} of the deck to the top/bottom.")

    def check_backstab(self, discarded, discarded2=None, selected_index=0):
        # "Backstab: Whenever you use an ATTACK to cause damage to a player within your physical range, you can flip a judgement card. If the judgement is not \u2665, no damage is caused, and instead you cause the target to reduce their maximum health by 1."
        if (self.character_ability2.startswith("Backstab:") or self.character_ability3.startswith("Backstab:")):

            for player_index, player in enumerate(players):
                if (player.character_ability2.startswith("Backstab:") or player.character_ability3.startswith("Backstab:")):
                    user_index = player_index
                    break

            possible_indexes = self.calculate_targets_in_physical_range(0)
            possible_targets = []
            for target in possible_indexes:
                possible_targets.append(players[target])
            if (players[selected_index]) in possible_targets:
                message = f"{self.character}: Choose to activate Backstab against {players[selected_index].character}, causing you to flip a judgement; if not \u2665, the attack will instead reduce their maximum health by 1."
                if question_yes_no(message):
                    print(
                        f"  >> Character Ability: Backstab; {self.character} has activated Backstab, forcing a judgement card to be flipped. If not \u2665, {players[selected_index].character} loses a maximum health instead of a health.")
                    main_deck.check_if_empty()
                    main_deck.discard_from_deck()
                    judgement_card = discard_deck.contents[0]
                    print(f"{self.character} flipped a {judgement_card}.")
                    judgement_card = check_judgement_tinkering(
                        judgement_card, user_index)
                    if judgement_card.suit == "\u2660" or judgement_card.suit == "\u2663" or judgement_card.suit == "\u2666":
                        players[selected_index].max_health -= 1
                        if players[selected_index].current_health > players[selected_index].max_health:
                            players[selected_index].current_health -= 1
                        print(
                            f"{self.character}'s judgement card is a {judgement_card} and therefore {players[selected_index].character} loses maximum health instead. ({players[selected_index].current_health}/{players[selected_index].max_health} HP remaining)")
                        for player_index, player in enumerate(players):
                            player.check_relief()
                            if player.current_health < 1:
                                players[player_index].check_brink_of_death_loop(
                                    player_index, 0)

                    if judgement_card.suit == "\u2665":
                        damage_dealt = 1

                        fantasy = players[selected_index].check_fantasy(
                            damage_dealt, 0)
                        if fantasy[0]:
                            selected_index = fantasy[1]

                        deplete_karma = players[selected_index].check_deplete_karma(
                            damage_dealt, user_index, None)
                        if deplete_karma[0]:
                            damage_dealt = deplete_karma[1]

                        players[selected_index].current_health -= damage_dealt
                        print(
                            f"{self.character}'s judgement card is a {judgement_card} and therefore Backstab does not apply. Damage dealt as normal; {damage_dealt} damage to {players[selected_index].character}. ({players[selected_index].current_health}/{players[selected_index].max_health} HP remaining)")
                        self.check_weapon_huangs_longbow(selected_index)
                        for player_index, player in enumerate(players):
                            player.check_relief()
                            if player.current_health < 1:
                                players[player_index].check_brink_of_death_loop(
                                    player_index, 0)

                        if player.current_health > 0:
                            if fantasy[0]:
                                cards_to_draw = (
                                    players[selected_index].max_health - players[selected_index].current_health)
                                print(
                                    f"  >> Character Ability: Fantasy; {players[selected_index].character} draws {cards_to_draw} from the deck.")
                                players[selected_index].hand_cards.draw(
                                    main_deck, cards_to_draw, False)

                            self.check_grudge(selected_index, "Damage")
                            for player in players:
                                player.check_lament(user_index, selected_index)
                            players[selected_index].check_bequeathed_strategy(
                                damage_dealt)
                            players[selected_index].check_delayed_wisdom()
                            players[selected_index].check_eternal_loyalty(
                                damage_dealt)
                            if (discarded.effect == "Colourless Attack") and (discarded2 == None):
                                pass
                            else:
                                players[selected_index].check_evil_hero(
                                    discarded, discarded2)
                            players[selected_index].check_exile()
                            if players[selected_index].check_eye_for_an_eye(
                                    source_player_index=0, mode="Activate") == "Break":
                                return True
                            players[selected_index].check_geminate(
                                damage_dealt)
                            players[selected_index].check_plotting_for_power(
                                damage_dealt, mode="Reaction")
                            players[selected_index].check_retaliation(
                                0, damage_dealt)
                    return True

    def check_bare_chested(self):
        # "Bare-chested: You can choose to draw one less card in your drawing phase. If you do so, any ATTACK or DUEL cards that you you play in your action phase will deal an additional unit of damage."
        if (self.character_ability1.startswith("Bare-chested:") or self.character_ability3.startswith("Bare-chested:")):
            message = f"{self.character}: Choose to activate Bare-chested, and draw one less card; if yes, all ATTACK or DUEL cards will do increased damage?"
            if question_yes_no(message):
                print(
                    f"  >> Character Ability: Bare-chested; {self.character} has activated Bare-chested, drawing one card only, and all their ATTACK and DUEL cards will do increased damage for this turn.")
                self.used_bare_chested = True
                return True

    def check_beauty(self, card):
        # "Beauty: All of your \u2660 will be regarded as \u2665."
        if (self.character_ability2.startswith("Beauty:") or self.character_ability3.startswith("Beauty:")):
            if card.suit == "\u2660":
                print(
                    f"  >> Character Ability: Beauty; {self.character}'s \u2660 are regarded as \u2665.")
                return True
        return False

    def check_behind_the_curtain(self, card, beauty=False):
        # "Behind the Curtain: You cannot become the target of any black-suited tool cards."
        if self.character_ability3.startswith("Behind the Curtain:"):
            if card.suit == "\u2660" or card.suit == "\u2663":
                if card.effect2 == "Barbarians" or card.effect2 == "Rain of Arrows" or card.effect2 == "Coerce" or card.effect2 == "Dismantle" or card.effect2 == "Duel" or card.effect2 == "Steal" or card.effect2 == "Acedia" or card.effect2 == "Lightning" or card.effect2 == "Rations Depleted":
                    print(
                        f"  >> Character Ability: Behind the Curtain; {self.character} is immune to the effects of {card} as it is a BLACK tool card.")
                    return True
            if beauty and card.suit == "\u2663":
                if card.effect2 == "Barbarians" or card.effect2 == "Rain of Arrows" or card.effect2 == "Coerce" or card.effect2 == "Dismantle" or card.effect2 == "Duel" or card.effect2 == "Steal" or card.effect2 == "Acedia" or card.effect2 == "Lightning" or card.effect2 == "Rations Depleted":
                    print(
                        f"  >> Character Ability: Behind the Curtain; {self.character} is immune to the effects of {card} as it is a BLACK tool card.")
                    return True
        return False

    def check_bequeathed_strategy(self, damage_dealt):
        # "Bequeathed Strategy: For every one unit of damage you recieve, you can draw two cards from the deck. You can then choose to give away one, two or none of these cards to any player."
        if (self.character_ability2.startswith("Bequeathed Strategy:") or self.character_ability3.startswith("Bequeathed Strategy:")):
            message = f"{self.character}: Choose to activate Bequeathed Strategy and draw {damage_dealt}x2 cards? You can then redistribute them between players."
            if question_yes_no(message):
                print(
                    f"  >> Character Ability: Bequeathed Strategy; {self.character} has taken {damage_dealt} and therefore draws {damage_dealt*2} cards, and redestributes them.")
                for item in range(damage_dealt):
                    beq_strat = Player("Temporary")
                    beq_strat.hand_cards.draw(main_deck, 2, False)
                    cards_to_distribute = 2
                    while cards_to_distribute > 0:
                        options = beq_strat.create_nonblind_menu(True)
                        question = [
                            {
                                'type': 'list',
                                'name': 'Selected',
                                'message': f'{self.character}: Please select a card:',
                                'choices': options,
                                'filter': lambda card: options.index(card)
                            },
                        ]
                        answer = prompt(question, style=custom_style_2)
                        card_index = answer.get('Selected')
                        options = []
                        for player in players:
                            options.append(
                                str(player) + f" ({str(len(player.hand_cards.contents))} hand-cards)")
                        question = [
                            {
                                'type': 'list',
                                'name': 'Selected',
                                'message': f'{self.character}: Please decide to whom you would like to distribute this card:',
                                'choices': options,
                                'filter': lambda player: options.index(player)
                            },
                        ]
                        answer = prompt(question, style=custom_style_2)
                        player_index = answer.get('Selected')
                        if self.character != players[player_index].character:
                            print(
                                f"  >> Character Ability: Bequeathed Strategy; {self.character} gave a card to {players[player_index]}.")
                        else:
                            print(
                                f"  >> Character Ability: Bequeathed Strategy; {self.character} took a card and added it to his own hand.")
                        players[player_index].hand_cards.add_to_top(
                            beq_strat.hand_cards.contents.pop(card_index))
                        cards_to_distribute -= 1

    def check_berserk(self):
        # "Berserk: There is no limit on how many times you can ATTACK during your turn."
        if (self.character_ability1.startswith("Berserk:") or self.character_ability3.startswith("Berserk:")):
            print(
                f"  >> Character Ability: Berserk; {self.character} has no limit to the amount of attacks they can play.")
            return True

    def check_bloodline(self):
        limit_increase = 0
        # "Bloodline (Ruler Ability): Your maximum hand-limit is increased by two for each other Hero character still alive."
        if (self.role == 'Emperor') or (self.character_ability2.startswith("False Ruler:")) or (self.character_ability3.startswith("False Ruler:")):
            if (self.character_ability2.startswith("Bloodline:") or self.character_ability3.startswith("Bloodline:") or self.character_ability4.startswith("Bloodline:")):
                heroes = []
                for player in players:
                    if player.allegiance == 'Heroes':
                        heroes.append("1")
                limit_increase = ((len(heroes)-1)*2)
                if limit_increase > 0:
                    print(
                        f"  >> Character Ability: Bloodline (Ruler Ability); {self.character}'s hand limit is increased by {limit_increase} (two for every other HERO character still alive).")
        return limit_increase

    def check_burning_heart(self, dying_player_index=0):
        # "Burning Heart (Single-Use Ability): When you kill another character, you can exchange role cards with the player you just killed. You cannot activate this ability if you are the emperor, or just killed the emperor."
        if self.character_ability2.startswith("Burning Heart (Single-Use Ability):"):
            if (self.awakened != True) and (self.role != "Emperor") and (players[dying_player_index].role != "Emperor"):
                message = f"{self.character}: Choose to activate Burning Heart (Single-Use), and swap role cards with {players[dying_player_index].character}?"
                if question_yes_no(message):
                    self.awakened = True
                    self.role, players[dying_player_index].role = players[dying_player_index].role, self.role
                    self.character_ability2 = "Burning Heart (INACTIVE Ability): When you kill another character, you can exchange role cards with the player you just killed. You cannot activate this ability if you are the emperor, or just killed the emperor."
                    print(
                        f"  >> Character Ability: Burning Heart; {self.character} has swapped role cards with {players[dying_player_index]}!")

    def check_conduit(self):
        # "Conduit (Awakening Ability): At the beginning of your turn, if you have three or more TERRAINS, you must reduce your maximum health by one unit. You then permanently gain the ability 'Blitz'."
        if self.character_ability2.startswith("Conduit (Awakening Ability):"):
            if len(self.terrains) >= 3:
                self.awakened = True
                print(
                    f"  >> Character Ability: Conduit (Awakening Ability): {self.character} has awakened, losing one maximum health. They permanently gain the ability 'Blitz'.")
                self.max_health -= 1
                if self.current_health > self.max_health:
                    self.current_health -= 1
                self.character_ability2 = "Conduit (INACTIVE Ability): At the beginning of your turn, if you have three or more TERRAINS, you must reduce your maximum health by one unit. You then permanently gain the ability 'Blitz'."
                self.character_ability3 = "Blitz: In your action phase, you can use any of your TERRAINS as STEAL."
                if self.max_health == 0:
                    self.check_brink_of_death_loop()

    def check_cornering_maneuver(self, card):
        # "Cornering Maneuver: Whenever you use a hand-card outside of your turn, you can flip the top card from the deck. If the card is the same type (basic, tool or equipment) as the card used, you can give the card to any player. If not, Zhao Yun can discard or return the card to the top of the deck."
        if (self.character_ability2.startswith("Cornering Maneuver:") or self.character_ability3.startswith("Cornering Maneuver:")):
            if self.character != players[0].character:
                message = f"{self.character}: Activate Cornering Maneuver and reveal the top card of the deck?"
                if question_yes_no(message):
                    main_deck.check_if_empty()
                    flipped_card = main_deck.remove_from_top()
                    print(
                        f"  >> Character Ability: Cornering Maneuver; {self.character} flipped {flipped_card} from the deck!")
                    if (card.type == "Basic" and flipped_card.type == "Basic") or (card.type == "Tool" and flipped_card.type == "Tool") or ((card.type == "Weapon" or card.type == "Armor" or card.type == "-1 Horse" or card.type == "+1 Horse") and (flipped_card.type == "Weapon" or flipped_card.type == "Armor" or flipped_card.type == "-1 Horse" or flipped_card.type == "+1 Horse")):
                        options = []
                        for player in players:
                            options.append(
                                str(player) + f" ({str(len(player.hand_cards.contents))} hand-cards)")
                        question = [
                            {
                                'type': 'list',
                                'name': 'Selected',
                                'message': f'{self.character}: Please decide to whom you would like to distribute this card:',
                                'choices': options,
                                'filter': lambda player: options.index(player)
                            },
                        ]
                        answer = prompt(question, style=custom_style_2)
                        player_index = answer.get('Selected')
                        players[player_index].hand_cards.add_to_top(
                            flipped_card)
                        print(
                            f"  >> Character Ability: Cornering Maneuver; {self.character} gave {flipped_card} to {players[player_index].character}!")
                    else:
                        question = [
                            {
                                'type': 'list',
                                'name': 'Selected',
                                'message': f'{self.character}: Return {flipped_card} to top of deck or discard it?',
                                'choices': ["Return to top of deck.", "Discard card."]
                            },
                        ]
                        answer = prompt(question, style=custom_style_2)
                        if answer == "Return to top of deck.":
                            main_deck.add_to_top(flipped_card)
                            print(
                                f"  >> Character Ability: Cornering Maneuver; {self.character} returned {flipped_card} to the top of the deck!")
                        else:
                            discard_deck.add_to_top(flipped_card)
                            print(
                                f"  >> Character Ability: Cornering Maneuver; {self.character} placed {flipped_card} on the top of the discard deck!")

    def check_dark_sorcery(self, judgement_card):
        # "Dark Sorcery: You can exchange the judgement card of any player before it takes effect, with any of your \u2663 or \u2660, either on-hand or equipped."
        if (self.character_ability2.startswith("Dark Sorcery:") or self.character_ability3.startswith("Dark Sorcery:")):
            cards_discardable = (len(self.hand_cards.contents) + len(self.equipment_weapon) + len(
                self.equipment_armor) + len(self.equipment_offensive_horse) + len(self.equipment_defensive_horse))
            if cards_discardable > 0:
                print(' ')
                message = f"{self.character}: Choose to activate Dark Sorcery, and exchange the current judgement card: {judgement_card}, with one of your \u2660 or \u2663?"
                if not question_yes_no(message):
                    return [False]
                else:
                    new_judgement_card = self.discard_from_equip_or_hand_boolpop(
                        "\u2660", "\u2663")
                    if new_judgement_card == None:
                        print(
                            f"{self.character}: You must use a BLACK-suited card for Dark Sorcery!")
                        return self.check_dark_sorcery(judgement_card)
                    else:
                        if judgement_card in discard_deck.contents:
                            discard_deck.contents.remove(judgement_card)
                        elif judgement_card in main_deck.contents:
                            main_deck.contents.remove(judgement_card)
                        self.hand_cards.add_to_top(judgement_card)
                        print(
                            f"  >> Character Ability: Dark Sorcery; {self.character} has exchanged the judgement card: {judgement_card} with {new_judgement_card}!")
                        return [True, new_judgement_card]
        return [False]

    def check_dashing_hero(self):
        # "Dashing Hero: Draw an extra card at the start of your turn."
        if (self.character_ability1.startswith("Dashing Hero:") or self.character_ability2.startswith("Dashing Hero:") or self.character_ability3.startswith("Dashing Hero:") or self.character_ability4.startswith("Dashing Hero:") or self.character_ability1.startswith("Dashing Hero:")):
            print(
                f"  >> Character Ability: Dashing Hero; {self.character} draws an extra card from the deck (total of three) in their drawing phase.")
            return True

    def check_decentralization(self):
        # "Decentralization: You can skip your action phase. If you do so, you can discard an on-hand card at the end of your turn, in order to allow another player to take a turn directly after yours."
        if (self.character_ability2.startswith("Decentralization:") or self.character_ability3.startswith("Decentralization:")):
            if len(self.hand_cards.contents) > 0:
                message = f"{self.character}: Skip your action-phase and discard a card to let another player take a turn immediately after you?"
                if question_yes_no(message):
                    options = [
                        Separator("------<Cannot target yourself>------")]
                    for player in players[1:]:
                        options.append(
                            str(player) + f" ({str(len(player.hand_cards.contents))} hand-cards)")
                    options.append(
                        Separator("--------------------Other--------------------"))
                    options.append("Cancel ability.")
                    question = [
                        {
                            'type': 'list',
                            'name': 'Selected',
                            'message': f'{self.character}: Select a player to take a turn after you:',
                            'choices': options,
                            'filter': lambda player: options.index(player)
                        },
                    ]
                    answer = prompt(question, style=custom_style_2)
                    player_index = answer.get('Selected')
                    if options[player_index] == "Cancel ability.":
                        return False
                    else:
                        self.start_discard_phase()
                        self.hand_cards.discard_from_hand()
                        print(
                            f"  >> Character Ability: Decentralization; {self.character} is allowing {players[player_index].character} to take their turn next!")
                        temp_players = players
                        decent = players[0]
                        for player in players[:player_index]:
                            players.append(players.pop(0))
                        players[0].start_beginning_phase()
                        if decent in players:
                            for player in players:
                                players.append(players.pop(0))
                                if decent == players[0]:
                                    return True
                        elif temp_players[1] in players:
                            for player in players:
                                players.append(players.pop(0))
                                if temp_players[1] == players[0]:
                                    return False
                        elif temp_players[2] in players:
                            for player in players:
                                players.append(players.pop(0))
                                if temp_players[2] == players[0]:
                                    return False
                        elif temp_players[3] in players:
                            for player in players:
                                players.append(players.pop(0))
                                if temp_players[3] == players[0]:
                                    return False
                        elif temp_players[4] in players:
                            for player in players:
                                players.append(players.pop(0))
                                if temp_players[4] == players[0]:
                                    return False
                        elif temp_players[5] in players:
                            for player in players:
                                players.append(players.pop(0))
                                if temp_players[5] == players[0]:
                                    return False
                        elif temp_players[6] in players:
                            for player in players:
                                players.append(players.pop(0))
                                if temp_players[6] == players[0]:
                                    return False
                        elif temp_players[7] in players:
                            for player in players:
                                players.append(players.pop(0))
                                if temp_players[7] == players[0]:
                                    return False
                        elif temp_players[8] in players:
                            for player in players:
                                players.append(players.pop(0))
                                if temp_players[8] == players[0]:
                                    return False
                        elif temp_players[9] in players:
                            for player in players:
                                players.append(players.pop(0))
                                if temp_players[9] == players[0]:
                                    return False
        return False

    def check_delayed_wisdom(self):
        # "Delayed Wisdom: Whenever you are damaged outside of your turn, you become immune to all ATTACKs and non-delay tool cards for the rest of that turn."
        if (self.character_ability2.startswith("Delayed Wisdom:") or self.character_ability3.startswith("Delayed Wisdom:")):
            if self.character != players[0].character:
                print(
                    f"  >> Character Ability: Delayed Wisdom; {self.character} has been damaged outside of their turn, and is now immune to all ATTACKS and non-delay tool cards for the rest of this turn!")
                self.used_delayed_wisdom = True

    def check_deplete_karma(self, damage_dealt, source_player_index=None, target_player_index=None):
        # "Deplete Karma: Whenever you are damaged by another player whose health level is greater or equal to your own, you can discard a red-suited hand-card to reduce the damage by one. If you damage another player whose health is greater than or equal to your own, you can discard black-suited hand-card to increase the damage by one."
        if (self.character_ability1.startswith("Deplete Karma:") or self.character_ability3.startswith("Deplete Karma:")):
            if source_player_index != None:
                if players[source_player_index].current_health >= self.current_health:
                    message = f"{self.character}: Choose to activate Deplete Karma, discarding a red card, and reducing your incoming damage from {players[source_player_index].character} by one?"
                    if question_yes_no(message):
                        # Discard red to reduce by one
                        cards_discardable = []
                        for card in self.hand_cards.contents:
                            if card.suit == "\u2665" or card.suit == "\u2666":
                                cards_discardable.append(card)
                        if len(cards_discardable) < 1:
                            print(
                                f"{self.character}: You cannot activate Deplete Karma as you have no red-cards in your hand.")
                        else:
                            card = self.discard_from_hand_boolpop(
                                "\u2665", "\u2666")
                            if card != None:
                                print(
                                    f"  >> Character Ability: Deplete Karma; {self.character} has discarded {card} to reduce the incoming damage by one!")
                                damage_dealt -= 1
                                return [True, damage_dealt]
                            else:
                                print(
                                    f"{self.character}: You must use a RED-suited card for Deplete Karma!")
                                return [False]

            elif target_player_index != None:
                if players[target_player_index].current_health >= self.current_health:
                    message = f"{self.character}: Choose to activate Deplete Karma, discarding a black card, and increasing your outgoing damage to {players[target_player_index].character} by one?"
                    if question_yes_no(message):
                        # Discard black to increase by one
                        cards_discardable = []
                        for card in self.hand_cards.contents:
                            if card.suit == "\u2660" or card.suit == "\u2663":
                                cards_discardable.append(card)
                        if len(cards_discardable) < 1:
                            print(
                                f"{self.character}: You cannot activate Deplete Karma as you have no black-cards in your hand.")
                        else:
                            card = self.discard_from_hand_boolpop(
                                "\u2660", "\u2663")
                            if card != None:
                                print(
                                    f"  >> Character Ability: Deplete Karma; {self.character} has discarded {card} to increase the outgoing damage by one!")
                                damage_dealt += 1
                                return [True, damage_dealt]
                            else:
                                print(
                                    f"{self.character}: You must use a BLACK-suited card for Deplete Karma!")
                                return [False]
        return [False]

    def check_devil(self, judgement_card):
        # "Devil: After any judgement has been flipped over, you can immediately discard one of your on-hand or equipped cards to replace the judgement card."
        if (self.character_ability2.startswith("Devil:") or self.character_ability3.startswith("Devil:")):
            cards_discardable = (len(self.hand_cards.contents) + len(self.equipment_weapon) + len(
                self.equipment_armor) + len(self.equipment_offensive_horse) + len(self.equipment_defensive_horse))
            if cards_discardable > 0:
                print(' ')
                message = f"{self.character}: Choose to activate Devil, and change the current judgement card: {judgement_card}?"
                if not question_yes_no(message):
                    return [False]
                else:
                    new_judgement_card = self.discard_from_equip_or_hand()
                    print(
                        f"  >> Character Ability: Devil; {self.character} has replaced the judgement card: {judgement_card} with {new_judgement_card}!")
                    return [True, new_judgement_card]
        return [False]

    def check_disintegrate(self):
        # "Disintegrate: At the end of every turn, if your health is not the least or among the least, you must either lose one unit of health, or reduce your maximum health by one unit."
        if self.character_ability3.startswith("Disintegrate:"):
            for player in players:
                if player.current_health > self.current_health:
                    return(' ')
            else:
                question = [
                    {
                        'type': 'list',
                        'name': 'Selected',
                        'message': f'{self.character}: You must either lose one health or one max-health ({self.current_health}/{self.max_health} HP remaining):',
                        'choices': ['Lose one health', 'Lose one maximum-health'],
                    },
                ]
                answer = prompt(question, style=custom_style_2)
                if answer.get('Selected') == 'Lose one health':
                    self.current_health -= 1
                    print(
                        f"  >> Character Ability: Disintegrate; {self.character}'s health is not among the least, so they lose one health. ({self.current_health}/{self.max_health} HP remaining)")
                    for player in players:
                        player.check_relief()
                if answer.get('Selected') == 'Lose one maximum-health':
                    self.max_health -= 1
                    if self.current_health > self.max_health:
                        self.current_health -= 1
                    if self.max_health == 0:
                        self.check_brink_of_death_loop()
                    print(
                        f"  >> Character Ability: Disintegrate; {self.character}'s health is not among the least, so they lose one maximum-health. ({self.current_health}/{self.max_health} HP remaining)")

    def check_displacement(self, source_player_index=0):
        # "Displacement: Whenever you become the target of an ATTACK, you can discard any card to divert the ATTACK to any player within your attacking range. This effect cannot be used against the player that played the ATTACK card."
        if (self.character_ability2.startswith("Displacement:") or self.character_ability3.startswith("Displacement:")):

            for player_index, player in enumerate(players):
                if (player.character_ability2.startswith("Displacement:") or player.character_ability3.startswith("Displacement:")):
                    user_index = player_index
                    break

            targets = players[user_index].create_targeting_menu(
                "Weapon", user_index, 0, source_player_index)
            if len(targets) > 0:
                message = f"{self.character}: Choose to activate Displacement, and redirect the ATTACK from {players[source_player_index].character}?"
                if not question_yes_no(message):
                    return [False]

                options_str = self.create_nonblind_menu()
                options_str.append(
                    Separator("--------------------Other--------------------"))
                options_str.append("Cancel ability.")
                question = [
                    {
                        'type': 'list',
                        'name': 'Selected',
                        'message': f'{self.character}: Select any card to discard to activate DISPLACEMENT:',
                        'choices': options_str,
                        'filter': lambda card: options_str.index(card)
                    },
                ]
                answer = prompt(question, style=custom_style_2)
                discarded_index = answer.get('Selected')
                if options_str[discarded_index] == "Cancel ability.":
                    return [False]
                else:
                    if discarded_index == (len(self.hand_cards.contents) + 1):
                        self.weapon_range = 1
                    if discarded_index == (len(self.hand_cards.contents) + 3):
                        self.weapon_range -= 1
                    targets = players[user_index].create_targeting_menu(
                        "Weapon", user_index, source_player_index)
                    if len(targets) > 0:
                        targets.append(
                            Separator("--------------------Other--------------------"))
                        targets.append("Cancel ability.")
                        question = [
                            {
                                'type': 'list',
                                'name': 'Selected',
                                'message': f'{self.character}: Select a target to redirect the ATTACK towards:',
                                'choices': targets,
                                'filter': lambda player: targets.index(player)
                            },
                        ]
                        answer = prompt(question, style=custom_style_2)
                        target_index = answer.get('Selected')
                        if targets[target_index] == "Cancel ability.":
                            if discarded_index == (len(self.hand_cards.contents) + 1):
                                self.weapon_range = self.equipment_weapon[0].weapon_range
                            if discarded_index == (len(self.hand_cards.contents) + 3):
                                self.weapon_range += 1
                            return [False]
                        else:
                            # Check if hand-card
                            if discarded_index < len(self.hand_cards.contents):
                                card = self.hand_cards.contents.pop(
                                    discarded_index)
                                discard_deck.add_to_top(card)
                                print(
                                    f"  >> Character Ability: Displacement; {self.character} has discarded {card} from their hand to redirect the ATTACK to {players[target_index].character}.")
                                return [True, target_index]

                            # Check if equipment-card
                            else:
                                if discarded_index == (len(self.hand_cards.contents) + 1):
                                    card = self.equipment_weapon.pop()
                                    discard_deck.add_to_top(card)
                                    self.weapon_range = 1
                                    print(
                                        f"  >> Character Ability: Displacement; {self.character} has discarded {card} from their weapon-slot to redirect the ATTACK to {players[target_index].character}.")
                                    return [True, target_index]

                                if discarded_index == (len(self.hand_cards.contents) + 2):
                                    card = self.equipment_armor.pop()
                                    discard_deck.add_to_top(card)
                                    print(
                                        f"  >> Character Ability: Displacement; {self.character} has discarded {card} from their armor-slot to redirect the ATTACK to {players[target_index].character}.")
                                    return [True, target_index]

                                if discarded_index == (len(self.hand_cards.contents) + 3):
                                    card = self.equipment_offensive_horse.pop()
                                    discard_deck.add_to_top(card)
                                    print(
                                        f"  >> Character Ability: Displacement; {self.character} has discarded {card} from their horse-slot to redirect the ATTACK to {players[target_index].character}.")
                                    return [True, target_index]

                                if discarded_index == (len(self.hand_cards.contents) + 4):
                                    card = self.equipment_defensive_horse.pop()
                                    discard_deck.add_to_top(card)
                                    print(
                                        f"  >> Character Ability: Displacement; {self.character} has discarded {card} from their horse-slot to redirect the ATTACK to {players[target_index].character}.")
                                    return [True, target_index]
        return [False]

    def check_divinity(self):
        # "Divinity (Awakening Ability): If, at the start of your turn, your health is one unit, you must reduce your maximum health by one. After which you permanently gain the abilities 'Dashing Hero' and 'Lingering Spirit'."
        if self.character_ability2.startswith("Divinity (Awakening Ability):"):
            if self.current_health == 1:
                self.awakened = True
                print(
                    f"  >> Character Ability: Divinity (Awakening Ability): {self.character} has awakened, losing one maximum health. They permanently gain the abilities 'Dashing Hero' and 'Brave Gesture'.")
                self.max_health -= 1
                self.character_ability2 = "Divinity (INACTIVE Ability): If, at the start of your turn, your health is one unit, you must reduce your maximum health by one. After which you permanently gain the abilities 'Dashing Hero' and 'Lingering Spirit'."
                self.character_ability3 = "Dashing Hero: Draw an extra card at the start of your turn."
                self.character_ability4 = "Lingering Spirit: If your health is not at maximum in your drawing phase, you can force any player to draw X cards, and then discard 1 card, or draw 1 card, and discard X cards. X is the amount of health you have missing from your maximum."
                if self.max_health == 0:
                    self.check_brink_of_death_loop()

    def check_dual_heroes(self, phase="Draw"):
        # "Dual Heroes: At the beginning of your turn, you can choose to forgo your drawing phase and instead flip a judgement. Unlike usual judgement cards, this card will be added to your hand. Note the colour of the suit of this judgement card. For the rest of your action phase, you can choose to use any on-hand card with a different colour suit from this judgement card as a DUEL."
        if (self.character_ability1.startswith("Dual Heroes:") or self.character_ability3.startswith("Dual Heroes:")):

            user_index = 0
            for player_index, player in enumerate(players):
                if (player.character_ability1.startswith("Dual Heroes:") or player.character_ability3.startswith("Dual Heroes:")):
                    user_index = player_index
                    break

            if phase == "Draw":
                message = f"{self.character}: Choose to activate Dual Heroes, and flip (then draw) a judgement; if yes, all cards of the opposite colour can be used as DUEL?"
                if question_yes_no(message):
                    print(
                        f"  >> Character Ability: Dual Heroes; {self.character} has/have activated Dual Heroes, flipping a judgement, then adding it to their hand.")
                    main_deck.check_if_empty()
                    main_deck.discard_from_deck()
                    judgement_card = discard_deck.contents[0]
                    print(f"{self.character} flipped a {judgement_card}.")
                    judgement_card = check_judgement_tinkering(
                        judgement_card, user_index)
                    self.hand_cards.draw(discard_deck, 1, False)

                    if judgement_card.suit == "\u2660" or judgement_card.suit == "\u2663":
                        self.used_dual_heroes = "Red"
                        print(
                            f"  >> Character Ability: Dual Heroes; {self.character} drew {judgement_card} and can use any on-hand red cards as DUEL!")
                        return True

                    if judgement_card.suit == "\u2665" or judgement_card.suit == "\u2666":
                        self.used_dual_heroes = "Black"
                        print(
                            f"  >> Character Ability: Dual Heroes; {self.character} drew {judgement_card} and can use any on-hand black cards as DUEL!")
                        return True

            if phase == "Activate":
                if self.used_dual_heroes == "Black":
                    if len(self.hand_cards.contents) > 0:
                        card = self.discard_from_hand_boolpop(
                            "\u2660", "\u2663")
                        if card != None:
                            card.effect2 = "Duel"
                            if not self.use_card_effect("Special", card):
                                self.hand_cards.draw(
                                    discard_deck, 1, False)
                                print(
                                    f"{self.character} cancelled using their effect, and {card} was returned.")
                        else:
                            print(
                                f"{self.character}: That card cannot be used as DUEL as is it NOT of suit \u2660 or \u2663.")

                if self.used_dual_heroes == "Red":
                    if len(self.hand_cards.contents) > 0:
                        card = self.discard_from_hand_boolpop(
                            "\u2665", "\u2666")
                        if card != None:
                            card.effect2 = "Duel"
                            if not self.use_card_effect("Special", card):
                                self.hand_cards.draw(
                                    discard_deck, 1, False)
                                print(
                                    f"{self.character} cancelled using their effect, and {card} was returned.")
                        else:
                            print(
                                f"{self.character}: That card cannot be used as DUEL as is it NOT of suit \u2665 or \u2666.")

    def check_eclipse_the_moon(self):
        # "Eclipse the Moon: At the end of your turn, you may draw an additional card from the deck."
        if (self.character_ability2.startswith("Eclipse the Moon:") or self.character_ability3.startswith("Eclipse the Moon:")):
            print(
                f"  >> Character Ability: Eclipse the Moon; {self.character} draws an extra card from the deck in their end-phase.")
            self.hand_cards.draw(main_deck, 1, False)

    def check_eiron(self):
        # "Eiron (Awakening/Ruler Ability): At the start of your turn, if your health is the least or among the least, you must raise your maximum health by one unit, regain one unit of health, and permanently gain the ability 'Rouse'."
        if (self.role == 'Emperor') or (self.character_ability2.startswith("False Ruler:")) or (self.character_ability3.startswith("False Ruler:")):
            if (self.character_ability3.startswith("Eiron (Awakening/Ruler Ability):") or self.character_ability4.startswith("Eiron (Awakening/Ruler Ability):")):
                for player in players:
                    if self.current_health > player.current_health:
                        return(' ')
                else:
                    self.awakened = True
                    print(
                        f"  >> Character Ability: Eiron (Awakening/Ruler Ability): {self.character} has awakened, gaining one health and maximum health. They also permanently gain the ability 'Rouse'.")
                    self.current_health += 1
                    self.max_health += 1
                    if self.character_ability3 == "Eiron (Awakening/Ruler Ability): At the start of your turn, if your health is the least or among the least, you must raise your maximum health by one unit, regain one unit of health, and permanently gain the ability 'Rouse'.":
                        self.character_ability3 = "Eiron (INACTIVE Ability): At the start of your turn, if your health is the least or among the least, you must raise your maximum health by one unit, regain one unit of health, and permanently gain the ability 'Rouse'."
                        self.character_ability4 = "Rouse (Ruler Ability): If you need to use an ATTACK, you can ask Sun Shang Xiang or any member of Shu to play it on your behalf."
                    if self.character_ability2 == "False Ruler: You possess the same ruler ability as the current emperor." and self.character_ability3 == self.character_ability2 == "Eiron (Awakening/Ruler Ability): At the start of your turn, if your health is the least or among the least, you must raise your maximum health by one unit, regain one unit of health, and permanently gain the ability 'Rouse'.":
                        self.character_ability3 = "Eiron (INACTIVE Ability): At the start of your turn, if your health is the least or among the least, you must raise your maximum health by one unit, regain one unit of health, and permanently gain the ability 'Rouse'."
                        self.character_ability4 = "Rouse (Ruler Ability): If you need to use an ATTACK, you can ask Sun Shang Xiang or any member of Shu to play it on your behalf."

    def check_empty_city(self):
        # "Empty City: When you have no hand-cards, you cannot become the target of an ATTACK or a DUEL."
        if (self.character_ability2.startswith("Empty City:") or self.character_ability3.startswith("Empty City:")):
            if len(self.hand_cards.contents) == 0:
                print(
                    f"  >> Character Ability; Empty City: {self.character} has no hand-cards, and therefore cannot be targeted by ATTACK or DUEL.")
                return True

    def check_envy_of_heaven(self):
        # "Envy of Heaven: You can obtain any judgement card that you flip over."
        if (self.character_ability1.startswith("Envy of Heaven:") or self.character_ability3.startswith("Envy of Heaven:")):
            print(
                f"  >> Character Ability: Envy of Heaven; The top judgement card has been added to {self.character}'s hand before it takes effect.")
            self.hand_cards.draw(discard_deck, 1, False)

    def check_escort(self, mode="Check"):
        # "Escort (Ruler Ability): If you need to use a DEFEND, you can ask any member of Wei to play it on your behalf."
        emperor_index = None
        false_ruler_index = None
        for player_index, player in enumerate(players):
            if (player.character_ability2.startswith("Escort (Ruler Ability):") or player.character_ability3.startswith("Escort (Ruler Ability):") or player.character_ability4.startswith("Escort (Ruler Ability):")):
                if (player.role == "Emperor"):
                    emperor_index = player_index
                else:
                    false_ruler_index = player_index

        if mode == "Check":
            if (self.role == "Emperor") or (self.character_ability2.startswith("False Ruler:")) or (self.character_ability3.startswith("False Ruler:")):
                if (self.character_ability2.startswith("Escort (Ruler Ability):") or self.character_ability3.startswith("Escort (Ruler Ability):") or self.character_ability4.startswith("Escort (Ruler Ability):")):
                    return True

        if mode == "Reaction":
            if self.character == players[emperor_index].character:
                targets = []
                for player in players:
                    targets.append(
                        Separator("------" + str(player) + "------"))
                for player_index, player in enumerate(players):
                    if player.role != "Emperor" and player.allegiance == "Wei":
                        targets.pop(player_index)
                        targets.insert(player_index, str(
                            players[player_index]))
            elif self.character == players[false_ruler_index].character:
                targets = []
                for player in players:
                    targets.append(
                        Separator("------" + str(player) + "------"))
                for player_index, player in enumerate(players):
                    if player.allegiance == "Wei":
                        targets.pop(player_index)
                        targets.insert(player_index, str(
                            players[player_index]))
            targets.append(
                Separator("--------------------Other--------------------"))
            targets.append("Cancel ability.")
            question = [
                {
                    'type': 'list',
                    'name': 'Selected',
                    'message': f'{self.character}: Please select a player to DEFEND you via Escort (Ruler Ability):',
                    'choices': targets,
                    'filter': lambda player: targets.index(player)
                },
            ]
            answer = prompt(question, style=custom_style_2)
            defender_index = answer.get('Selected')
            if targets[defender_index] == "Cancel ability.":
                return [False]
            print(
                f"  >> Ruler Ability: Escort; {self.character} has asked {players[defender_index].character} to play a DEFEND on their behalf!")
            return [True, defender_index]

    def check_eternal_loyalty(self, damage_dealt):
        # "Eternal Loyalty: For every one unit of damage you suffer, you can allow any player of your choice (including yourself) to replenish that player’s on-hand cards to their maximum health level."
        if (self.character_ability2.startswith("Eternal Loyalty:") or self.character_ability3.startswith("Eternal Loyalty:")):
            while damage_dealt > 0:
                message = f"{self.character}: Choose to activate Eternal Loyalty, and refill a players' hand-limit to full? ({damage_dealt} hand(s) can be refilled)?"
                if not question_yes_no(message):
                    return (' ')

                options_str = []
                options = []
                for player in players:
                    if player.max_health > len(player.hand_cards.contents):
                        difference = player.max_health - \
                            len(player.hand_cards.contents)
                        options_str.append(
                            str(player) + " (+" + str(difference) + ")")
                        options.append(player)
                options_str.append(
                    Separator("--------------------Other--------------------"))
                options.append("Blank")
                options_str.append("Cancel ability.")
                options.append("Cancel")

                if len(options_str) > 2:
                    question = [
                        {
                            'type': 'list',
                            'name': 'Selected',
                            'message': f'{self.character}: Choose a character whose hand to refill to their maximum-health level?',
                            'choices': options_str,
                            'filter': lambda player: options_str.index(player)
                        },
                    ]

                    answer = prompt(question, style=custom_style_2)
                    if answer.get('Selected') == (len(options_str) - 1):
                        damage_dealt = 0
                    else:
                        selected_index = answer.get('Selected')
                        difference = options[selected_index].max_health - \
                            len(options[selected_index].hand_cards.contents)
                        options[selected_index].hand_cards.draw(
                            main_deck, difference, False)
                        print(
                            f"  >> Character Ability: Eternal Loyalty; {self.character} has refilled {options[selected_index].character}'s hand to their maximum health limit! (+{difference} cards)")
                        damage_dealt -= 1
                else:
                    print(
                        f"{self.character}: There are no players that you can use this ability against.")

    def check_evil_hero(self, card, card2=None):
        # "Evil Hero: Whenever you are damaged by a card, you can immediately add it to your hand."
        if (self.character_ability1.startswith("Evil Hero:") or self.character_ability3.startswith("Evil Hero:")):
            if card in discard_deck.contents:
                discard_deck.contents.remove(card)
                self.hand_cards.add_to_top(card)
                print(
                    f"  >> Character Ability: Evil Hero; {self.character} immediately draws {card} after taking damage from it.")
            elif card in main_deck.contents:
                main_deck.contents.remove(card)
                self.hand_cards.add_to_top(card)
                print(
                    f"  >> Character Ability: Evil Hero; {self.character} immediately draws {card} after taking damage from it.")

            if card2 != None:
                if card2 in discard_deck.contents:
                    discard_deck.contents.remove(card2)
                    self.hand_cards.add_to_top(card2)
                    print(
                        f"  >> Character Ability: Evil Hero; {self.character} immediately draws {card2} after taking damage from it.")
                elif card2 in main_deck.contents:
                    main_deck.contents.remove(card2)
                    self.hand_cards.add_to_top(card2)
                    print(
                        f"  >> Character Ability: Evil Hero; {self.character} immediately draws {card2} after taking damage from it.")

    def check_exalt(self):
        # "Exalt (Ruler Ability): Whenever any Wei character (other than yourself) makes a judgement, if the judgement card that takes effect is either \u2663 or \u2660, that character can choose to let you draw one card from the deck."
        if self.allegiance == "Wei":
            emperor_index = None
            false_ruler_index = None
            for player_index, player in enumerate(players):
                if (player.character_ability3.startswith("Exalt (Ruler Ability):") or player.character_ability4.startswith("Exalt (Ruler Ability):")):
                    if (player.role == "Emperor"):
                        emperor_index = player_index
                    else:
                        false_ruler_index = player_index

            if emperor_index != None:
                if false_ruler_index != None:
                    message = f'{self.character}: Choose to activate Exalt (Ruler Ability), to allow the emperor (or false-ruler) to draw a card?'
                elif self.role != "Emperor":
                    message = f'{self.character}: Choose to activate Exalt (Ruler Ability), to allow the emperor to draw a card?'
                else:
                    return(' ')

                if question_yes_no(message):
                    target_indexes = [emperor_index]

                    if self.role == "Emperor":
                        if (false_ruler_index != None):
                            target_index = false_ruler_index

                    elif self.role != "Emperor":
                        if false_ruler_index == None:
                            target_index = emperor_index

                        elif (false_ruler_index != None) and (self.character == players[false_ruler_index].character):
                            target_index = emperor_index

                        else:
                            options = [str(players[emperor_index]), str(
                                players[false_ruler_index]), "Both players!"]
                            question = [
                                {
                                    'type': 'list',
                                    'name': 'Selected',
                                    'message': f'{self.character}: Please select which target will draw a card (Exalt):',
                                    'choices': options,
                                },
                            ]
                            answer = prompt(question, style=custom_style_2)
                            selected = answer.get('Selected')
                            if selected == "Both players!":
                                target_indexes = [
                                    emperor_index, false_ruler_index]
                            elif selected == str(players[emperor_index]):
                                target_indexes = [emperor_index]
                            else:
                                target_indexes = [false_ruler_index]

                    for target_index in target_indexes:
                        players[target_index].hand_cards.draw(
                            main_deck, 1, False)
                        print(
                            f"  >> Ruler Ability: Exalt; {self.character} has allowed 1 card to be added to {players[target_index].character}'s hand.")

    def check_exertion(self, source_player_index=None, mode="Check"):
        # "Exertion: Whenever another player has cards taken or discarded by another player, you can lose one health to let that player draw two cards."
        user_index = 0
        for player_index, player in enumerate(players):
            if (player.character_ability2.startswith("Exertion:") or player.character_ability3.startswith("Exertion:")):
                user_index = player_index
                break

        if mode == "Check":
            for player_index, player in enumerate(players):
                if player.character == self.character:
                    source_player_index = player_index
                    break
            if user_index != None:
                players[user_index].check_exertion(
                    source_player_index, "Reaction")

        if mode == "Reaction":
            if (self.character_ability2.startswith("Exertion:") or self.character_ability3.startswith("Exertion:")):
                message = f"{self.character}: Choose to activate Exertion and lose 1 health ({self.current_health}/{self.max_health} HP remaining), to let {players[source_player_index].character} draw 2 cards?"
                if self.character != players[source_player_index].character:
                    if question_yes_no(message):
                        self.current_health -= 1
                        print(
                            f"  >> Character Ability: Exertion; {self.character} has lost 1 health ({self.current_health}/{self.max_health} HP remaining), and allowed {players[source_player_index].character} to draw 2 cards!")
                        self.check_brink_of_death_loop(user_index, "Self")
                        players[source_player_index].hand_cards.draw(
                            main_deck, 2, False)

    def check_exile(self):
        # "Exile: Every instance that you suffer damage, you can force any other player to draw X number of cards (X being the units of health you have missing from your maximum after damage). By doing so the targeted player will have to flip their character card. Flipped character cards must miss their next turn."
        if (self.character_ability2.startswith("Exile:") or self.character_ability3.startswith("Exile:")):

            for player_index, player in players:
                if (player.character_ability2.startswith("Exile:") or player.character_ability3.startswith("Exile:")):
                    user_index = player_index
                    break

            message = f"{self.character}: Choose to activate Exile, making someone miss their next turn, and draw {self.max_health - self.current_health} cards?"
            if question_yes_no(message):
                targets_str = []
                for player in players:
                    targets_str.append(str(player))
                targets_str.pop(user_index)
                targets_str.insert(user_index, Separator(
                    f"--{self.character} (Can't target yourself!)--"))
                targets_str.append(
                    Separator("--------------------Other--------------------"))
                targets_str.append("Cancel ability.")

                question = [
                    {
                        'type': 'list',
                        'name': 'Selected',
                        'message': f'{self.character}: Please select a character to target with Exile:',
                        'choices': targets_str,
                        'filter': lambda player: targets_str.index(player)
                    },
                ]
                answer = prompt(question, style=custom_style_2)
                selected = answer.get('Selected')
                if targets_str[selected] == "Cancel ability.":
                    return(' ')
                else:
                    cards_to_draw = self.max_health - self.current_health
                    players[selected].hand_cards.draw(
                        main_deck, cards_to_draw, True)

                    if players[selected].char_card_flipped == False:
                        players[selected].char_card_flipped = True
                        print(
                            f"  >> Character Ability: Exile; {self.character} has flipped {players[selected].character}'s character card to face-down! They miss their next turn!")
                    else:
                        players[selected].char_card_flipped = False
                        print(
                            f"  >> Character Ability: Exile; {self.character} has flipped {players[selected].character}'s character card to face-up!")

    def check_eye_for_an_eye(self, source_player_index=0, mode="Activate"):
        # "Eye for an Eye: For every instance that you suffer damage, you can flip a judgement card. If the judgement is not \u2665, the character that damaged you must choose between the following options; lose one unit of health, or discard any two on-hand cards."
        user_index = 0
        for player_index, player in enumerate(players):
            if (player.character_ability1.startswith("Eye for an Eye:") or player.character_ability3.startswith("Eye for an Eye:")):
                user_index = player_index
                break

        if mode == "Activate":
            if (self.character_ability1.startswith("Eye for an Eye:") or self.character_ability3.startswith("Eye for an Eye:")):
                print(' ')
                message = f"{self.character}: Choose to activate Eye for an Eye, and force {players[source_player_index].character} to either take one damage or discard two hand-cards?"
                if question_yes_no(message):
                    print(
                        f"  >> Character Ability: Eye for an Eye; {self.character} is forcing a judgement card to be flipped. If not \u2665, {players[source_player_index].character} must either take one damage or discard two hand-cards.")
                main_deck.check_if_empty()
                main_deck.discard_from_deck()
                judgement_card = discard_deck.contents[0]
                self.check_exalt()
                print(f"{self.character} flipped a {judgement_card}.")
                judgement_card = check_judgement_tinkering(
                    judgement_card, user_index)
                if judgement_card.suit != "\u2665":
                    print(
                        f"{self.character}'s judgement card is a {judgement_card} and therefore {players[source_player_index].character} must suffer one damage or discard two hand-cards.")
                    players[source_player_index].check_eye_for_an_eye(
                        user_index, "Reaction")
                if judgement_card.suit == "\u2665":
                    print(
                        f"{self.character}'s judgement card is a {judgement_card} and therefore has no effect.")
                    return (' ')

        if mode == "Reaction":
            print(' ')
            choices = ['Suffer one damage.']
            if len(self.hand_cards.contents) > 1:
                choices.append('Discard two cards.')
            question = [
                {
                    'type': 'list',
                    'name': 'Selected',
                    'message': f'{self.character}: Please select an option:',
                    'choices': choices,
                },
            ]
            answer = prompt(question, style=custom_style_2)
            if answer.get('Selected') == 'Suffer one damage.':
                damage_dealt = 1
                fantasy = self.check_fantasy(1, user_index)
                if not fantasy[0]:

                    deplete_karma = self.check_deplete_karma(
                        damage_dealt, user_index, None)
                    if deplete_karma[0]:
                        damage_dealt = deplete_karma[1]

                    self.current_health -= damage_dealt
                    print(
                        f"{self.character} suffered {damage_dealt} damage from {players[user_index].character}'s an Eye for an Eye ({self.current_health}/{self.max_health} HP remaining).")
                    for player_index, player in enumerate(players):
                        player.check_relief()
                        if player.current_health < 1:
                            if players[player_index].check_brink_of_death_loop(player_index, user_index) == "Break":
                                return "Break"
                    self.check_bequeathed_strategy(damage_dealt)
                    self.check_delayed_wisdom()
                    self.check_eternal_loyalty(damage_dealt)
                    self.check_exile()
                    self.check_geminate(damage_dealt)
                    self.check_retaliation(user_index, damage_dealt)
                    self.check_plotting_for_power(damage_dealt, "Reaction")
                else:
                    redirected = fantasy[1]

                    deplete_karma = players[redirected].check_deplete_karma(
                        damage_dealt, user_index, None)
                    if deplete_karma[0]:
                        damage_dealt = deplete_karma[1]

                    players[redirected].current_health -= damage_dealt
                    print(f"{players[redirected].character} suffered {damage_dealt} damage from {players[user_index].character}'s an Eye for an Eye ({players[redirected].current_health}/{players[redirected].max_health} HP remaining).")
                    for player_index, player in enumerate(players):
                        if player.current_health < 1:
                            if players[player_index].check_brink_of_death_loop(player_index, user_index) == "Break":
                                return "Break"
                    players[redirected].check_bequeathed_strategy(damage_dealt)
                    players[redirected].check_delayed_wisdom()
                    players[redirected].check_eternal_loyalty(damage_dealt)
                    players[redirected].check_exile()
                    players[redirected].check_geminate(damage_dealt)
                    players[redirected].check_retaliation(
                        user_index, damage_dealt)
                    players[redirected].check_plotting_for_power(
                        damage_dealt, "Reaction")

            if answer.get('Selected') == 'Discard two cards.':
                self.hand_cards.discard_from_hand(2)
                print(
                    f"{self.character} discarded two hand-cards due to {players[user_index].character}'s an Eye for an Eye.")
                self.check_amassing_terrain()
                self.check_exertion(None, "Check")
                self.check_one_after_another()

    def check_false_ruler(self):
        # "False Ruler: You possess the same ruler ability as the current emperor."
        if self.character_ability2.startswith("False Ruler:"):
            for player in players:
                if player.role == 'Emperor':
                    if player.character == 'Liu Bei':
                        self.character_ability3 = "Rouse (Ruler Ability): If you need to use an ATTACK, you can ask Sun Shang Xiang or any member of Shu to play it on your behalf."
                    if (player.character == 'Liu Shan') and (not self.awakened):
                        self.character_ability3 = "Eiron (Awakening/Ruler Ability): At the start of your turn, if your health is the least or among the least, you must raise your maximum health by one unit, regain one unit of health, and permanently gain the ability 'Rouse'."
                    elif (player.character == 'Liu Shan') and (self.awakened):
                        self.character_ability3 = "Eiron (INACTIVE Ability): At the start of your turn, if your health is the least or among the least, you must raise your maximum health by one unit, regain one unit of health, and permanently gain the ability 'Rouse'."
                        self.character_ability4 = "Rouse (Ruler Ability): If you need to use an ATTACK, you can ask Sun Shang Xiang or any member of Shu to play it on your behalf."
                    if player.character == 'Cao Cao':
                        self.character_ability3 = "Escort (Ruler Ability): If you need to use a DEFEND, you can ask any member of Wei to play it on your behalf."
                    if player.character == 'Cao Pi':
                        self.character_ability3 = "Exalt (Ruler Ability): Whenever any Wei character (other than yourself) makes a judgement, if the judgement card that takes effect is either \u2663 or \u2660, that character can choose to let you draw one card from the deck."
                    if player.character == 'Sun Ce':
                        self.character_ability3 = "Hegemony (Ruler Ability): During the action phase of any other Wu characters, they can choose to COMPETE against you; you both show a card simultaneously, and whoever has the higher value wins. If they do not win, you can take both cards used. After your awakening ability activates, you are able to refuse COMPETE effects."
                    if player.character == 'Sun Quan':
                        self.character_ability3 = "Rescued (Ruler Ability): Whenever another member of Wu uses a PEACH to save you from the brink of death, it provides you with two units of health."
                    if player.character == 'Dong Zhuo':
                        self.character_ability3 = "Tyrant (Ruler Ability): Whenever another Hero character causes damage to any other player, you can flip a judgement card. If the judgement card is of the suit \u2660, you can regain one unit of health."
                    if player.character == 'Yuan Shao':
                        self.character_ability3 = "Bloodline (Ruler Ability): Your maximum hand-limit is increased by two for each other Hero character still alive."
                    if player.character == 'Zhang Jiao':
                        self.character_ability3 = "Amber Sky (Ruler Ability): All Hero characters can give you a DEFEND or LIGHTNING card during their individual turns."
        elif self.character_ability3.startswith("False Ruler:"):
            for player in players:
                if player.role == 'Emperor':
                    if player.character == 'Liu Bei':
                        self.character_ability4 = "Rouse (Ruler Ability): If you need to use an ATTACK, you can ask Sun Shang Xiang or any member of Shu to play it on your behalf."
                    if (player.character == 'Liu Shan') and (not self.awakened):
                        self.character_ability4 = "Eiron (Awakening/Ruler Ability): At the start of your turn, if your health is the least or among the least, you must raise your maximum health by one unit, regain one unit of health, and permanently gain the ability 'Rouse'."
                    elif (player.character == 'Liu Shan') and (self.awakened):
                        self.character_ability4 = "Eiron (INACTIVE Ability): At the start of your turn, if your health is the least or among the least, you must raise your maximum health by one unit, regain one unit of health, and permanently gain the ability 'Rouse'."
                        self.character_ability5 = "Rouse (Ruler Ability): If you need to use an ATTACK, you can ask Sun Shang Xiang or any member of Shu to play it on your behalf."
                    if player.character == 'Cao Cao':
                        self.character_ability4 = "Escort (Ruler Ability): If you need to use a DEFEND, you can ask any member of Wei to play it on your behalf."
                    if player.character == 'Cao Pi':
                        self.character_ability4 = "Exalt (Ruler Ability): Whenever any Wei character (other than yourself) makes a judgement, if the judgement card that takes effect is either \u2663 or \u2660, that character can choose to let you draw one card from the deck."
                    if player.character == 'Sun Ce':
                        self.character_ability4 = "Hegemony (Ruler Ability): During the action phase of any other Wu characters, they can choose to COMPETE against you; you both show a card simultaneously, and whoever has the higher value wins. If they do not win, you can take both cards used. After your awakening ability activates, you are able to refuse COMPETE effects."
                    if player.character == 'Sun Quan':
                        self.character_ability4 = "Rescued (Ruler Ability): Whenever another member of Wu uses a PEACH to save you from the brink of death, it provides you with two units of health."
                    if player.character == 'Dong Zhuo':
                        self.character_ability4 = "Tyrant (Ruler Ability): Whenever another Hero character causes damage to any other player, you can flip a judgement card. If the judgement card is of the suit \u2660, you can regain one unit of health."
                    if player.character == 'Yuan Shao':
                        self.character_ability4 = "Bloodline (Ruler Ability): Your maximum hand-limit is increased by two for each other Hero character still alive."
                    if player.character == 'Zhang Jiao':
                        self.character_ability4 = "Amber Sky (Ruler Ability): All Hero characters can give you a DEFEND or LIGHTNING card during their individual turns."

    def check_fantasy(self, damage_dealt, source_player_index=0):
        # "Fantasy: Whenever you recieve damage, you can choose to pass the damage onto any other player by discarding an on-hand card that has the suit \u2665. The victim that recieves the damage gets to draw X number of cards from the deck, X being the amount of health missing from the maximum level after damage."
        if (self.character_ability1.startswith("Fantasy:") or self.character_ability3.startswith("Fantasy:")):

            user_index = 0
            for player_index, player in enumerate(players):
                if (player.character_ability1.startswith("Fantasy:") or self.character_ability3.startswith("Fantasy:")):
                    user_index = player_index

            message = f"{self.character}: Discard a \u2665 card to activate Fantasy, and redirect the incoming damage to another player? They, then draw X cards; X being the number of health points they have missing after the damage is passed."
            if question_yes_no(message):
                if (self.character_ability2.startswith("Beauty:") or self.character_ability3.startswith("Beauty:")):
                    discarded = self.discard_from_equip_or_hand_boolpop(
                        "\u2660", "\u2665")
                else:
                    discarded = self.discard_from_equip_or_hand_boolpop(
                        "\u2665")

                if discarded != None:
                    self.check_beauty(discarded)
                    targets_str = []
                    for player in players:
                        targets_str.append(
                            str(player)+f" - ({player.current_health}/{player.max_health} HP remaining)")
                    targets_str.pop(user_index)
                    targets_str.insert(user_index, Separator(
                        f"--{self.character} (Can't target yourself!)--"))
                    question = [
                        {
                            'type': 'list',
                            'name': 'Selected',
                            'message': f'{self.character}: Please select a character to target with Fantasy:',
                            'choices': targets_str,
                            'filter': lambda player: targets_str.index(player)
                        },
                    ]
                    answer = prompt(question, style=custom_style_2)
                    selected = answer.get('Selected')
                    print(
                        f"  >> Character Ability: Fantasy; {self.character} redirected {damage_dealt} damage to {players[selected].character}!")
                    return [True, selected]
                else:
                    print(
                        f"{self.character}: That card cannot be used for Fantasy as is it NOT of suit \u2665.")
        return [False]

    def check_fearsome_advance(self, discarded, selected_index=0):
        # "Fearsome Advance: Whenever your ATTACK is evaded by a DEFEND, you can discard one of your opponents cards (on-hand or equipped)."
        if (self.character_ability2.startswith("Fearsome Advance:") or self.character_ability3.startswith("Fearsome Advance:")):
            cards_discardable = (len(players[selected_index].hand_cards.contents) + len(players[selected_index].equipment_weapon) + len(
                players[selected_index].equipment_armor) + len(players[selected_index].equipment_offensive_horse) + len(players[selected_index].equipment_defensive_horse))
            if cards_discardable > 0:
                message = f"{self.character}: Choose to activate Fearsome Advance against {players[selected_index].character}, causing you to discard one of their cards?"
                if question_yes_no(message):
                    print(
                        f"  >> Character Ability: Fearsome Advance; {self.character} has activated Fearsome Advance, forcing {players[selected_index].character} to discard a card.")

                    options_str = players[selected_index].create_semiblind_menu(
                    )
                    question = [
                        {
                            'type': 'list',
                            'name': 'Selected',
                            'message': f'{self.character}: Please select which card you would like to discard from {players[selected_index]}:',
                            'choices': options_str,
                            'filter': lambda card: options_str.index(card)
                        },
                    ]
                    answer = prompt(question, style=custom_style_2)
                    card_discarded_index = answer.get('Selected')

                    # Check if hand-card
                    if card_discarded_index <= len(players[selected_index].hand_cards.contents):
                        card_discarded = players[selected_index].hand_cards.contents.pop(
                            card_discarded_index)
                        discard_deck.add_to_top(card_discarded)
                        print(
                            f"  >> Character Ability: Fearsome Advance; {self.character} has made {players[selected_index].character} discard {card_discarded} from their hand.")
                        players[selected_index].check_amassing_terrain()
                        players[selected_index].check_exertion(None, "Check")
                        players[selected_index].check_one_after_another()

                    # Check if equipment-card
                    else:
                        if card_discarded_index == (len(players[selected_index].hand_cards.contents) + 1):
                            card_discarded = players[selected_index].equipment_weapon.pop(
                            )
                            discard_deck.add_to_top(card_discarded)
                            players[selected_index].weapon_range = 1
                            print(
                                f"  >> Character Ability: Fearsome Advance; {self.character} has made {players[selected_index].character} discard {card_discarded} from their weapon-slot.")
                            players[selected_index].check_warrior_woman()

                        elif card_discarded_index == (len(players[selected_index].hand_cards.contents) + 2):
                            card_discarded = players[selected_index].equipment_armor.pop(
                            )
                            discard_deck.add_to_top(card_discarded)
                            print(
                                f"  >> Character Ability: Fearsome Advance; {self.character} has made {players[selected_index].character} discard {card_discarded} from their armor-slot.")
                            players[selected_index].check_warrior_woman()

                        elif card_discarded_index == (len(players[selected_index].hand_cards.contents) + 3):
                            card_discarded = players[selected_index].equipment_offensive_horse.pop(
                            )
                            discard_deck.add_to_top(card_discarded)
                            print(
                                f"  >> Character Ability: Fearsome Advance; {self.character} has made {players[selected_index].character} discard {card_discarded} from their horse-slot.")
                            players[selected_index].check_warrior_woman()

                        elif card_discarded_index == (len(players[selected_index].hand_cards.contents) + 4):
                            card_discarded = players[selected_index].equipment_defensive_horse.pop(
                            )
                            discard_deck.add_to_top(card_discarded)
                            print(
                                f"  >> Character Ability: Fearsome Advance; {self.character} has made {players[selected_index].character} discard {card_discarded} from their horse slot.")
                            players[selected_index].check_warrior_woman()

    def check_fearsome_archer(self, discarded, discarded2=None, selected_index=0):
        # "Fearsome Archer: During your action phase, your ATTACK cards cannot be evaded by a DEFEND under the following two conditions: the number of on-hand cards of the target player is less than or equal to your attacking range; or the number of on-hand cards of the target player is more than or equal to the units of health you have remaining."
        if (self.character_ability1.startswith("Fearsome Archer:") or self.character_ability2.startswith("Fearsome Archer:")):

            user_index = 0
            for player_index, player in enumerate(players):
                if (player.character_ability1.startswith("Fearsome Archer:") or player.character_ability3.startswith("Fearsome Archer:")):
                    user_index = player_index
                    break

            if (len(players[selected_index].hand_cards.contents) <= self.weapon_range) or (len(players[selected_index].hand_cards.contents) >= self.current_health):
                message = f"{self.character}: Choose to activate Fearsome Archer against {players[selected_index].character}, and make your attack impossible to dodge?"
                if question_yes_no(message):
                    if self.check_weapon_frost_blade(selected_index, "Check"):
                        return(' ')
                    if (discarded2 == None) or (discarded2.effect2 == "Red Attack"):
                        if players[selected_index].check_reckless(discarded, 0):
                            return(' ')
                    damage_dealt = 1

                    fantasy = players[selected_index].check_fantasy(
                        damage_dealt, 0)
                    if fantasy[0]:
                        selected_index = fantasy[1]

                    deplete_karma = players[selected_index].check_deplete_karma(
                        damage_dealt, user_index, None)
                    if deplete_karma[0]:
                        damage_dealt = deplete_karma[1]

                    players[selected_index].current_health -= damage_dealt
                    if discarded2 == None:
                        print(
                            f"  >> Character Ability: Fearsome Archer; {self.character} attacked {players[selected_index].character} with an undodgable {discarded}, dealing {damage_dealt} damage. ({players[selected_index].current_health}/{players[selected_index].max_health} HP remaining)")
                    else:
                        print(
                            f"  >> Character Ability: Fearsome Archer; {self.character} attacked {players[selected_index].character} with an undodgable ATTACK, dealing {damage_dealt} damage. ({players[selected_index].current_health}/{players[selected_index].max_health} HP remaining)")
                    self.check_weapon_huangs_longbow(selected_index)
                    for player_index, player in enumerate(players):
                        player.check_relief()
                        if player.current_health < 1:
                            players[player_index].check_brink_of_death_loop(
                                player_index, 0)

                    if players[selected_index].current_health > 0:
                        if fantasy[0]:
                            cards_to_draw = (
                                players[selected_index].max_health - players[selected_index].current_health)
                            print(
                                f"  >> Character Ability: Fantasy; {players[selected_index].character} draws {cards_to_draw} from the deck.")
                            players[selected_index].hand_cards.draw(
                                main_deck, cards_to_draw, False)
                        for player in players:
                            player.check_lament(user_index, selected_index)
                        self.check_grudge(selected_index, "Damage")
                        players[selected_index].check_bequeathed_strategy(
                            damage_dealt)
                        players[selected_index].check_delayed_wisdom()
                        players[selected_index].check_eternal_loyalty(
                            damage_dealt)
                        if (discarded.effect == "Colourless Attack") and (discarded2 == None):
                            pass
                        else:
                            players[selected_index].check_evil_hero(
                                discarded, discarded2)
                        players[selected_index].check_exile()
                        players[selected_index].check_eye_for_an_eye(
                            user_index, "Activate")
                        players[selected_index].check_geminate(damage_dealt)
                        players[selected_index].check_plotting_for_power(
                            damage_dealt, mode="Reaction")
                        players[selected_index].check_retaliation(
                            user_index, damage_dealt)
                    return True

    def check_fearsome_blade(self, selected_index=0):
        # "Fearsome Blade: Whenever you successfully damage a target player with an ATTACK, you can choose to COMPETE against them; you both show a card simultaneously, and whoever has the higher value wins. If you win, you can take one card from the target, on-hand or equipped. This takes effect before any retaliatory abilities."
        if (self.character_ability2.startswith("Fearsome Blade:") or self.character_ability3.startswith("Fearsome Blade:")):
            if (len(self.hand_cards.contents) > 0) and (len(players[selected_index].hand_cards.contents) > 0):
                message = f"{self.character}: Choose to activate Fearsome Blade against {players[selected_index].character}, causing you to COMPETE? If you win, you take 1 of their cards!"
                if question_yes_no(message):
                    my_card = self.activate_compete()
                    their_card = players[selected_index].activate_compete()
                    if my_card > their_card:
                        print(
                            f"  >> Character Ability: Fearsome Blade; {self.character} won vs {players[selected_index].character} in their COMPETITION! She can take one of their cards!")
                        cards_discardable = (len(players[selected_index].hand_cards.contents) + len(players[selected_index].equipment_weapon) + len(
                            players[selected_index].equipment_armor) + len(players[selected_index].equipment_offensive_horse) + len(players[selected_index].equipment_defensive_horse))
                        if cards_discardable > 0:
                            players[selected_index].check_ignore_formalities(
                                my_card, their_card)
                            self.activate_steal(
                                "Special", selected_index, False)
                    else:
                        print(
                            f"  >> Character Ability: Fearsome Blade; {players[selected_index].character} won vs {self.character} in their COMPETITION!")
                        players[selected_index].check_ignore_formalities(
                            my_card, their_card)

    def check_first_aid(self, dying_player_index=0, mode="Check"):
        # "First Aid: Outside of your turn, you can use any red-suited cards (on-hand or equipped) as a PEACH."
        if (self.character_ability1.startswith("First Aid:") or self.character_ability3.startswith("First Aid:")):
            if mode == "Check":
                return True

            if mode == "Reaction":
                cards_discardable = (len(self.hand_cards.contents) + len(self.equipment_weapon) + len(
                    self.equipment_armor) + len(self.equipment_offensive_horse) + len(self.equipment_defensive_horse))
                if cards_discardable > 0:
                    card = self.discard_from_equip_or_hand_boolpop(
                        "\u2665", "\u2666")
                    if card != None:
                        print(
                            f"  >> Character Ability: First Aid; {self.character} has discarded {card} to use as PEACH.")
                        return True
                    else:
                        print(
                            f"{self.character}: That card cannot be used as PEACH as is it NOT of suit \u2665 or \u2666.")

    def check_flexibility(self, phase="Judgement"):
        # "Flexibility: You can discard one on-hand card to skip any of your phases (excluding the beginning and end phases). If you skip your drawing phase using this method, you can draw one on-hand card from a maximum of two other players. If you skip your action phase using this method, you can relocate a card (in the equipment area or pending time-delay tool card area) from its original location to an identical location."
        if (self.character_ability1.startswith("Flexibility:") or self.character_ability3.startswith("Flexibility")):
            if len(self.hand_cards.contents) > 0:
                if phase == "Judgement":
                    message = f"{self.character}: Discard a card to skip your judgement phase?"
                    if question_yes_no(message):
                        self.hand_cards.discard_from_hand()
                        print(
                            f"  >> Character Ability: Flexibility; {self.character} discarded a card to skip their judgement phase!")
                        return True

                if phase == "Draw":
                    message = f"{self.character}: Discard a card to skip your draw phase? You can instead draw one card from two different players:"
                    if question_yes_no(message):
                        self.hand_cards.discard_from_hand()
                        print(
                            f"  >> Character Ability: Flexibility; {self.character} discarded a card to skip their draw phase!")
                        draw_from_players = 2
                        selected_indexes = []
                        options = [
                            Separator("------<Cannot target yourself>------")]
                        for player in players[1:]:
                            if len(player.hand_cards.contents) > 0:
                                options.append(
                                    str(player) + f" ({str(len(player.hand_cards.contents))} hand-cards)")
                            else:
                                options.append(Separator(
                                    "------" + str(player) + f" ({str(len(player.hand_cards.contents))} hand-cards)" + "------"))
                        options.append(
                            Separator("--------------------Other--------------------"))
                        options.append("Target no others.")

                        while draw_from_players > 0:
                            question = [
                                {
                                    'type': 'list',
                                    'name': 'Selected',
                                    'message': f'{self.character}: Please select a character to draw a hand-card from:',
                                    'choices': options,
                                    'filter': lambda player: options.index(player)
                                },
                            ]
                            answer = prompt(question, style=custom_style_2)
                            target_index = answer.get('Selected')
                            if options[target_index] == "Target no others.":
                                draw_from_players = 0
                            else:
                                selected_indexes.append(target_index)
                                options.pop(target_index)
                                options.insert(target_index, (Separator(
                                    "------<ALREADY SELECTED>------")))
                                draw_from_players -= 1

                        for player_index in selected_indexes:
                            options = players[player_index].create_blind_menu()
                            question = [
                                {
                                    'type': 'list',
                                    'name': 'Selected',
                                    'message': f"{self.character}: Please select which card you would like to take from {players[player_index].character}'s hand:",
                                    'choices': options,
                                    'filter': lambda card: options.index(card)
                                },
                            ]
                            answer = prompt(question, style=custom_style_2)
                            card_stolen_index = answer.get('Selected')
                            card_stolen = players[player_index].hand_cards.contents.pop(
                                card_stolen_index)
                            self.hand_cards.add_to_top(card_stolen)
                            print(
                                f"  >> Character Ability: Flexibility; {self.character} has drawn {card_stolen} from {players[player_index].character}'s hand.")
                            players[player_index].check_amassing_terrain()
                            players[player_index].check_exertion(None, "Check")
                            players[player_index].check_one_after_another()
                        return True

                if phase == "Action":
                    message = f"{self.character}: Discard a card to skip your action phase? You can then reposition any piece of equipment/pending judgement cards."
                    if question_yes_no(message):
                        print(
                            f"  >> Character Ability: Flexibility; {self.character} discarded a card to skip their action phase!")
                        possible_repositions = 0
                        for player in players:
                            if len(player.equipment_weapon) + len(player.equipment_armor) + len(player.equipment_offensive_horse) + len(player.equipment_defensive_horse) + len(player.pending_judgements) > 0:
                                possible_repositions += 1

                        if possible_repositions > 0:
                            options = []
                            for player in players:
                                if len(player.equipment_weapon) + len(player.equipment_armor) + len(player.equipment_offensive_horse) + len(player.equipment_defensive_horse) + len(player.pending_judgements) > 0:
                                    options.append(str(
                                        player) + f" W:[{len(player.equipment_weapon)}] / A:[{len(player.equipment_armor)}] / H:[{len(player.equipment_offensive_horse)}] / H:[{len(player.equipment_defensive_horse)}] / PJ:[{len(player.pending_judgements)}]")
                                else:
                                    options.append(Separator(
                                        "------" + str(player) + f" (No equipped or pending judgement cards)" + "------"))

                            question = [
                                {
                                    'type': 'list',
                                    'name': 'Selected',
                                    'message': f'{self.character}: Please select a character whose equipment or judgement you want to reposition:',
                                    'choices': options,
                                    'filter': lambda player: options.index(player)
                                },
                            ]
                            answer = prompt(question, style=custom_style_2)
                            target_index = answer.get('Selected')

                            options = players[target_index].create_nohands_menu(
                                True)
                            question = [
                                {
                                    'type': 'list',
                                    'name': 'Selected',
                                    'message': f'{self.character}: Please select which card you would like to reposition:',
                                    'choices': options,
                                    'filter': lambda card: options.index(card)
                                },
                            ]
                            answer = prompt(question, style=custom_style_2)
                            card_index = answer.get('Selected')
                            options = []

                            if card_index == 1:
                                repositioned = players[target_index].equipment_weapon.pop(
                                )
                                players[target_index].weapon_range = 1
                                players[target_index].check_warrior_woman()
                                for player in players:
                                    if len(player.equipment_weapon) == 0:
                                        options.append(str(
                                            player) + f" ///  W:[{len(player.equipment_weapon)}] / A:[{len(player.equipment_armor)}] / H:[{len(player.equipment_offensive_horse)}] / H:[{len(player.equipment_defensive_horse)}] / PJ:[{len(player.pending_judgements)}]")
                                    else:
                                        options.append(Separator(
                                            "------" + str(player) + f" (has a weapon!)" + "------"))

                            elif card_index == 2:
                                repositioned = players[target_index].equipment_armor.pop(
                                )
                                players[target_index].check_warrior_woman()
                                for player in players:
                                    if len(player.equipment_armor) == 0:
                                        options.append(str(
                                            player) + f" ///  W:[{len(player.equipment_weapon)}] / A:[{len(player.equipment_armor)}] / H:[{len(player.equipment_offensive_horse)}] / H:[{len(player.equipment_defensive_horse)}] / PJ:[{len(player.pending_judgements)}]")
                                    else:
                                        options.append(Separator(
                                            "------" + str(player) + f" (has armor!)" + "------"))

                            elif card_index == 3:
                                repositioned = players[target_index].equipment_offensive_horse.pop(
                                )
                                players[target_index].check_warrior_woman()
                                for player in players:
                                    if len(player.equipment_offensive_horse) == 0:
                                        options.append(str(
                                            player) + f" ///  W:[{len(player.equipment_weapon)}] / A:[{len(player.equipment_armor)}] / H:[{len(player.equipment_offensive_horse)}] / H:[{len(player.equipment_defensive_horse)}] / PJ:[{len(player.pending_judgements)}]")
                                    else:
                                        options.append(Separator(
                                            "------" + str(player) + f" (has a -1 horse!)" + "------"))

                            elif card_index == 4:
                                repositioned = players[target_index].equipment_defensive_horse.pop(
                                )
                                players[target_index].check_warrior_woman()
                                for player in players:
                                    if len(player.equipment_defensive_horse) == 0:
                                        options.append(str(
                                            player) + f" ///  W:[{len(player.equipment_weapon)}] / A:[{len(player.equipment_armor)}] / H:[{len(player.equipment_offensive_horse)}] / H:[{len(player.equipment_defensive_horse)}] / PJ:[{len(player.pending_judgements)}]")
                                    else:
                                        options.append(Separator(
                                            "------" + str(player) + f" (has a -1 horse!)" + "------"))

                            else:
                                repositioned = players[target_index].pending_judgements.pop(
                                    card_index - 6)
                                for player in players:
                                    for pending_judgement in player.pending_judgements:
                                        if pending_judgement.effect2 == repositioned.effect2:
                                            options.append(Separator(
                                                "------" + str(player) + f" (has pending {repositioned.effect2})" + "------"))
                                    else:
                                        options.append(str(
                                            player) + f" ///  W:[{len(player.equipment_weapon)}] / A:[{len(player.equipment_armor)}] / H:[{len(player.equipment_offensive_horse)}] / H:[{len(player.equipment_defensive_horse)}] / PJ:[{len(player.pending_judgements)}]")

                            question = [
                                {
                                    'type': 'list',
                                    'name': 'Selected',
                                    'message': f'{self.character}: Please select to where you would like to reposition {repositioned}:',
                                    'choices': options,
                                    'filter': lambda player: options.index(player)
                                },
                            ]
                            answer = prompt(question, style=custom_style_2)
                            target2_index = answer.get('Selected')

                            if card_index == 1:
                                players[target2_index].equipment_weapon.append(
                                    repositioned)
                                players[target2_index].weapon_range = repositioned.weapon_range
                                print(
                                    f"  >> Character Ability: Flexibility; {self.character} moved {repositioned} from {players[target_index].character} to the weapon-slot of {players[target2_index].character}!")

                            elif card_index == 2:
                                players[target2_index].equipment_armor.append(
                                    repositioned)
                                print(
                                    f"  >> Character Ability: Flexibility; {self.character} moved {repositioned} from {players[target_index].character} to the armor-slot of {players[target2_index].character}!")

                            elif card_index == 3:
                                players[target2_index].equipment_offensive_horse.append(
                                    repositioned)
                                print(
                                    f"  >> Character Ability: Flexibility; {self.character} moved {repositioned} from {players[target_index].character} to the horse-slot of {players[target2_index].character}!")

                            elif card_index == 4:
                                players[target2_index].equipment_defensive_horse.append(
                                    repositioned)
                                print(
                                    f"  >> Character Ability: Flexibility; {self.character} moved {repositioned} from {players[target_index].character} to the horse-slot of {players[target2_index].character}!")

                            else:
                                players[target2_index].pending_judgements.append(
                                    repositioned)
                                print(
                                    f"  >> Character Ability: Flexibility; {self.character} moved {repositioned} from {players[target_index].character} to the pending judgements of {players[target2_index].character}!")
                        return True

                if phase == "Discard":
                    message = f"{self.character}: Discard a card to skip your discard phase?"
                    if question_yes_no(message):
                        self.hand_cards.discard_from_hand()
                        print(
                            f"  >> Character Ability: Flexibility; {self.character} discarded a card to skip their discard phase!")
                        return True
        return False

    def check_garden_of_lust(self, selected_index=0):
        # "Garden of Lust: Whenever you use an ATTACK on a female character or vice-versa, the targeted character needs to use two DEFEND cards to successfully evade the attack."
        if (self.character_ability2.startswith("Garden of Lust:") or self.character_ability3.startswith("Garden of Lust:")):
            if self.gender != players[selected_index].gender:
                print(
                    f"  >> Character Ability: Garden of Lust; {self.character} and {players[selected_index].character} must use two DEFEND cards for every ATTACK card they use against one another.")
                return True

    def check_geminate(self, num=1, message=True):
        # "Geminate: For every one unit of damage you recieve, you can acquire a new character card for 'Shapeshift'."
        if self.character_ability2.startswith("Geminate:"):
            if message == True:
                if num == 1:
                    print(
                        f"  >> Character Ability: Geminate; {num} character card has been added to {self.character}'s hand.")
                else:
                    print(
                        f"  >> Character Ability: Geminate; {num} character cards have been added to {self.character}'s hand.")
            while num > 0:
                if len(character_card_discard_pile.contents) == 0:
                    print("There are no more character cards to play with!")
                card = character_card_discard_pile.remove_from_top()
                self.forms.add_to_top(card)
                num -= 1

    def check_giant_elephant(self, card, mode="Check"):
        # "Giant Elephant: The tool card BARBARIANS has no net effect on you. When any other player uses BARBARIANS and its effects and subsequent card effects are concluded, you will acquire the BARBARIANS card used."
        if (self.character_ability1.startswith("Giant Elephant:") or self.character_ability3.startswith("Giant Elephant:")):
            if mode == "Reaction":
                print(
                    f"  >> Character Ability: Giant Elephant; {self.character} is immune to the effects of {card}!")
                return True

            if mode == "Check":
                if card in discard_deck.contents:
                    discard_deck.contents.remove(card)
                    self.hand_cards.add_to_top(card)
                    print(
                        f"  >> Character Ability: Giant Elephant; {self.character} draws {card} after it resolves!")
                elif card in main_deck.contents:
                    main_deck.contents.remove(card)
                    self.hand_cards.add_to_top(card)
                    print(
                        f"  >> Character Ability: Giant Elephant; {self.character} draws {card} after it resolves!")

    def check_goddess_luo(self):
        # "Goddess Luo: At the beginning of your turn, you flip a judgement card. If the judgement is a black-suited, you may choose to flip another. This process continues until you flip a red-suited card. The red card is discarded and all black-suited cards are added to your hand."
        if (self.character_ability2.startswith("Goddess Luo:") or self.character_ability3.startswith("Goddess Luo")):
            print(
                f"  >> Character Ability: Goddess Luo; {self.character} can flip judgement cards until one is red. All black cards are added to their hand.")
            activated_goddess_luo = True
            cards_drawn = []
            print(' ')
            while activated_goddess_luo:
                message = f"{self.character}: Choose to activate Goddess Luo, and flip another judgement card (currently {len(cards_drawn)})?"
                if not question_yes_no(message):
                    activated_goddess_luo = False
                else:
                    main_deck.check_if_empty()
                    judgement_card = main_deck.remove_from_top()
                    self.check_exalt()
                    print(
                        f"{self.character}'s judgement card is a {judgement_card}.")
                    judgement_card = check_judgement_tinkering(
                        judgement_card, 0)
                    if judgement_card.suit == '\u2660' or judgement_card.suit == '\u2663':
                        cards_drawn.append(judgement_card)
                    else:
                        discard_deck.add_to_top(judgement_card)
                        activated_goddess_luo = False
            if len(cards_drawn) > 0:
                print(
                    f"  >> Character Ability: Goddess Luo; {self.character} adds {len(cards_drawn)} black card(s) to their hand.")
                for card in cards_drawn:
                    self.hand_cards.contents.append(card)

    def check_godspeed(self, phase="Judgement"):
        # "Godspeed: You can do either or both of the following options; skip your judgement and drawing phases, or skip your action phase and discard one equipment card. If you do either, it is the equivalent of using an ATTACK with no distance limitations."
        if (self.character_ability1.startswith("Godspeed:") or self.character_ability3.startswith("Godspeed:")):
            if phase == "Judgement":
                message = f"{self.character}: Choose to skip your judgement and drawing phases, activating Godspeed, and allowing you to ATTACK any player?"
                if question_yes_no(message):
                    options = self.create_targeting_menu("Weapon", 0, 6)
                    question = [
                        {
                            'type': 'list',
                            'name': 'Selected',
                            'message': f'{self.character}: Who would you like to ATTACK with Godspeed?',
                            'choices': options,
                            'filter': lambda player: options.index(player)
                        },
                    ]
                    answer = prompt(question, style=custom_style_2)
                    target_index = answer.get('Selected')
                    main_deck.check_if_empty()
                    attack_card = main_deck.contents[0]
                    attack_card.effect2 = "Colourless Attack"
                    extra_targets = self.check_weapon_sky_scorcher_halberd(
                        target_index)
                    if (extra_targets == None) or (extra_targets[0] == 0):
                        self.activate_attack(attack_card, target_index)
                    elif (extra_targets[0] == 1):
                        self.activate_attack(attack_card, target_index)
                        self.activate_attack(attack_card, extra_targets[1])
                    elif (extra_targets[0] == 2):
                        self.activate_attack(attack_card, target_index)
                        self.activate_attack(attack_card, extra_targets[1])
                        self.activate_attack(attack_card, extra_targets[2])
                    return True

            if phase == "Action":
                usable_cards = []
                for card in self.hand_cards.contents:
                    if card.type == "Weapon" or card.type == "Armor" or card.type == "-1 Horse" or card.type == "+1 Horse":
                        usable_cards.append(card)
                for card in self.equipment_weapon:
                    usable_cards.append(card)
                for card in self.equipment_armor:
                    usable_cards.append(card)
                for card in self.equipment_offensive_horse:
                    usable_cards.append(card)
                for card in self.equipment_defensive_horse:
                    usable_cards.append(card)
                if len(usable_cards) > 0:
                    message = f"{self.character}: Choose to skip your action phase, and discard a piece of equipment, activating Godspeed, and allowing you to ATTACK any player?"
                    if question_yes_no(message):
                        options = self.create_targeting_menu("Weapon", 0, 6)
                        question = [
                            {
                                'type': 'list',
                                'name': 'Selected',
                                'message': f'{self.character}: Who would you like to ATTACK with Godspeed?',
                                'choices': options,
                                'filter': lambda player: options.index(player)
                            },
                        ]
                        answer = prompt(question, style=custom_style_2)
                        target_index = answer.get('Selected')
                        main_deck.check_if_empty()
                        attack_card = main_deck.contents[0]
                        attack_card.effect2 = "Colourless Attack"
                        extra_targets = self.check_weapon_sky_scorcher_halberd(
                            target_index)
                        if (extra_targets == None) or (extra_targets[0] == 0):
                            self.activate_attack(attack_card, target_index)
                        elif (extra_targets[0] == 1):
                            self.activate_attack(attack_card, target_index)
                            self.activate_attack(attack_card, extra_targets[1])
                        elif (extra_targets[0] == 2):
                            self.activate_attack(attack_card, target_index)
                            self.activate_attack(attack_card, extra_targets[1])
                            self.activate_attack(attack_card, extra_targets[2])
                        return True

    def check_grudge(self, target_index, mode="Damage"):
        # "Grudge: Whenever someone damages you, they must give you a card of suit \u2665 from their hand. If they do not, they lose one unit of health. Whenever another player heals you, they draw a card from the deck."
        if (players[target_index].character_ability1.startswith("Grudge:") or players[target_index].character_ability3.startswith("Grudge:")):
            if self.character != players[target_index].character:
                if mode == "Damage":
                    if len(self.hand_cards.contents) > 0:
                        options = self.create_nonblind_menu(True)
                        options.append(
                            Separator("--------------------Other--------------------"))
                        options.append("Lose one unit of health.")
                        question = [
                            {
                                'type': 'list',
                                'name': 'Selected',
                                'message': f'{self.character}: Please select a \u2665 card to give to {players[target_index].character} or lose one health:',
                                'choices': options,
                                'filter': lambda card: options.index(card)
                            },
                        ]
                        answer = prompt(question, style=custom_style_2)
                        discarded_index = answer.get('Selected')
                        if options[discarded_index] == "Lose one unit of health.":
                            self.current_health -= 1
                            print(
                                f"  >> Character Ability: Grudge; {self.character} did not give a \u2665 card, and instead lost one unit of health ({self.current_health}/{self.max_health} HP remaining)!")
                            for player_index, player in enumerate(players):
                                player.check_brink_of_death_loop(
                                    player_index, "Self")
                        elif self.hand_cards.contents[discarded_index].suit == "\u2665":
                            players[target_index].hand_cards.add_to_top(
                                self.hand_cards.contents.pop(discarded_index))
                            print(
                                f"  >> Character Ability: Grudge; {players[target_index].character} was given a \u2665 card by {self.character}!")
                        else:
                            return self.check_grudge(target_index, "Damage")
                    else:
                        self.current_health -= 1
                        print(
                            f"  >> Character Ability: Grudge; {self.character} did not give a \u2665 card, and instead lost one unit of health ({self.current_health}/{self.max_health} HP remaining)!")
                        for player_index, player in enumerate(players):
                            player.check_brink_of_death_loop(
                                player_index, "Self")

                if mode == "Heal":
                    print(
                        f"  >> Character Ability: Grudge; {self.character} healed {players[target_index].character}, and therefore draws a card!")
                    self.hand_cards.draw(main_deck, 1, False)

    def check_heartbreak(self, source_player_index=0):
        # "Heartbreak: Whenever a player kills you, they lose all of their character abilities for the rest of the game."
        if (self.character_ability2.startswith("Heartbreak:") or self.character_ability3.startswith("Heartbreak:")):

            print(
                f"  >> Character Ability: Heartbreak; {players[source_player_index]} loses all their character-abilities after killing {self.character}.")
            players[source_player_index].character_ability1 = "None"
            players[source_player_index].character_ability2 = "None"
            players[source_player_index].character_ability3 = "None"
            players[source_player_index].character_ability4 = "None"
            players[source_player_index].character_ability5 = "None"

    def check_horsemanship(self):
        # "Horsemanship: You will always be -1 distance in any range calculations."
        if (self.character_ability1.startswith("Horsemanship:") or self.character_ability3.startswith("Horsemanship:")):
            return(1)
        else:
            return(0)

    def check_humility(self):
        # "Humility: You cannot become the target of STEAL or ACEDIA."
        if (self.character_ability1.startswith("Humility") or self.character_ability3.startswith("Humility")):
            print(
                f"  >> Character Ability: Humility; {self.character} cannot be targeted by STEAL or ACEDIA.")
            return True

    def check_ignore_formalities(self, card1, card2):
        # "Ignore Formalities: Whenever you COMPETE, you can keep the card played by the loser."
        if (self.character_ability2.startswith("Ignore Formalities:") or self.character_ability3.startswith("Ignore Formalities:")):
            print(
                f"  >> Character Ability: Ignore Formalities; {self.character} keeps any COMPETITION cards played by the loser!")
            if card1 > card2:
                if card2 in discard_deck.contents:
                    discard_deck.contents.remove(card2)
                    self.hand_cards.add_to_top(card2)
                elif card2 in main_deck.contents:
                    discard_deck.contents.remove(card2)
                    self.hand_cards.add_to_top(card2)
            else:
                if card1 in discard_deck.contents:
                    discard_deck.contents.remove(card1)
                    self.hand_cards.add_to_top(card1)
                elif card1 in main_deck.contents:
                    discard_deck.contents.remove(card1)
                    self.hand_cards.add_to_top(card1)

    def check_iron_cavalry(self, discarded, discarded2=None, selected_index=0):
        # "Iron Cavalry: Whenever you ATTACK a player, you can flip a judgement card. If it is red, the ATTACK cannot be dodged."
        if (self.character_ability2.startswith("Iron Cavalry:") or self.character_ability3.startswith("Iron Cavalry:")):

            user_index = 0
            for player_index, player in enumerate(players):
                if (player.character_ability2.startswith("Iron Cavalry:") or player.character_ability3.startswith("Iron Cavalry:")):
                    user_index = player_index
                    break

            message = f"{self.character}: Choose to activate Iron Cavalry against {players[selected_index].character}, causing you to flip a judgement; if red, the attack is impossible to dodge?"
            if question_yes_no(message):
                print(
                    f"  >> Character Ability: Iron Cavalry; {self.character} has activated Iron Cavalry, forcing a judgement card to be flipped. If red, {players[selected_index].character} cannot dodge the attack.")
                main_deck.check_if_empty()
                main_deck.discard_from_deck()
                judgement_card = discard_deck.contents[0]
                print(f"{self.character} flipped a {judgement_card}.")
                judgement_card = check_judgement_tinkering(
                    judgement_card, user_index)

                if judgement_card.suit == "\u2666" or judgement_card.suit == "\u2665":
                    if self.check_weapon_frost_blade(selected_index, "Check"):
                        return(' ')
                    if (discarded2 == None) or (discarded2.effect2 == "Red Attack"):
                        if players[selected_index].check_reckless(discarded, 0):
                            return(' ')
                    damage_dealt = 1

                    fantasy = players[selected_index].check_fantasy(
                        damage_dealt, user_index)
                    if fantasy[0]:
                        selected_index = fantasy[1]

                    deplete_karma = players[selected_index].check_deplete_karma(
                        damage_dealt, user_index, None)
                    if deplete_karma[0]:
                        damage_dealt = deplete_karma[1]

                    players[selected_index].current_health -= damage_dealt
                    if discarded2 == None:
                        print(
                            f"{self.character}'s judgement card is a {judgement_card} and therefore {discarded} cannot be dodged, dealing {damage_dealt} damage to {players[selected_index].character}. ({players[selected_index].current_health}/{players[selected_index].max_health} HP remaining)")
                    else:
                        print(
                            f"{self.character}'s judgement card is a {judgement_card} and therefore the ATTACK cannot be dodged, dealing {damage_dealt} damage to {players[selected_index].character}. ({players[selected_index].current_health}/{players[selected_index].max_health} HP remaining)")
                    self.check_weapon_huangs_longbow(selected_index)
                    for player_index, player in enumerate(players):
                        player.check_relief()
                        if player.current_health < 1:
                            players[player_index].check_brink_of_death_loop(
                                player_index, user_index)

                    if players[selected_index].current_health > 0:
                        if fantasy[0]:
                            cards_to_draw = (
                                players[selected_index].max_health - players[selected_index].current_health)
                            print(
                                f"  >> Character Ability: Fantasy; {players[selected_index].character} draws {cards_to_draw} from the deck.")
                            players[selected_index].hand_cards.draw(
                                main_deck, cards_to_draw, False)

                        self.check_grudge(selected_index, "Damage")
                        for player in players:
                            player.check_lament(user_index, selected_index)
                        players[selected_index].check_bequeathed_strategy(
                            damage_dealt)
                        players[selected_index].check_delayed_wisdom()
                        players[selected_index].check_eternal_loyalty(
                            damage_dealt)
                        if (discarded.effect == "Colourless Attack") and (discarded2 == None):
                            pass
                        else:
                            players[selected_index].check_evil_hero(
                                discarded, discarded2)
                        players[selected_index].check_exile()
                        players[selected_index].check_eye_for_an_eye(
                            user_index, "Activate")
                        players[selected_index].check_geminate(damage_dealt)
                        players[selected_index].check_plotting_for_power(
                            damage_dealt, mode="Reaction")
                        players[selected_index].check_retaliation(
                            user_index, damage_dealt)
                        return True
                else:
                    print(
                        f"{self.character}'s judgement card is a {judgement_card} and Iron Cavalry has no effect.")

    def check_impetus(self, source_player_index, mode="Check"):
        # "Impetus: Every one of your black-suited on-hand cards may be used as DEFEND."
        if (self.character_ability1.startswith("Impetus:") or self.character_ability3.startswith("Impetus:")):
            if mode == "Check":
                return True

            if mode == "Reaction":
                if len(self.hand_cards.contents) > 0:
                    card = self.discard_from_hand_boolpop("\u2660", "\u2663")
                    if card != None:
                        return card
                    else:
                        print(
                            f"{self.character}: You must use a BLACK-suited card for Impetus!")
                        return None

    def check_insanity(self, selected_index=0, damage_dealt=1):
        # "Insanity: Whenever you cause damage to any player within your physical range, you regain one unit of health for every unit of damage caused."
        if (self.character_ability1.startswith("Insanity:") or self.character_ability3.startswith("Insanity:")):

            for player_index, player in enumerate(players):
                if (player.character_ability1.startswith("Insanity:") or player.character_ability3.startswith("Insanity:")):
                    source_index = player_index

            possible_indexes = self.calculate_targets_in_physical_range(
                source_index)
            possible_targets = []
            for target in possible_indexes:
                possible_targets.append(players[target])
            if (players[selected_index]) in possible_targets:
                if self.max_health > self.current_health:
                    self.current_health += damage_dealt

                if self.current_health > self.max_health:
                    self.current_health = self.max_health
                print(
                    f"  >> Character Ability: Insanity; {self.character} regains one unit of health for damaging {players[selected_index]}, within their physical range. ({self.current_health}/{self.max_health} HP remaining)")

    def check_insurrection(self):
        # "Insurrection (Awakening Ability): Whenever you begin your turn with three or more RITES, you must either recover one unit of health or draw two cards. You must then decrease your maximum health by one and permanently gain the ability 'Rejection'."
        if self.character_ability2.startswith("Insurrection (Awakening Ability):"):
            if len(self.rites) >= 3:
                self.awakened = True
                if self.current_health >= self.max_health:
                    choices = ["Draw two cards"]
                else:
                    choices = ["Regain one health", "Draw two cards"]
                question = [
                    {
                        'type': 'list',
                        'name': 'Selected',
                        'message': f'{self.character}: Please select an option:',
                        'choices': choices
                    },
                ]
                answer = prompt(question, style=custom_style_2)
                if answer.get('Selected') == "Regain one health":
                    self.current_health += 1
                    print(
                        f"  >> Character Ability: Insurrection (Awakening Ability): {self.character} has awakened, regaining one health. They permanently gain the ability 'Rejection'.")
                if answer.get('Selected') == 'Draw two cards':
                    self.hand_cards.draw(main_deck, 2, False)
                    print(
                        f"  >> Character Ability: Insurrection (Awakening Ability): {self.character} has awakened, drawing two cards. They permanently gain the ability 'Rejection'.")
                self.max_health -= 1
                if self.current_health > self.max_health:
                    self.current_health -= 1
                self.character_ability2 = "Insurrection (INACTIVE Ability): Whenever you begin your turn with three or more RITES, you must either recover one unit of health or draw two cards. You must then decrease your maximum health by one and permanently gain the ability 'Rejection'."
                self.character_ability3 = "Rejection: Once per turn, you can discard one RITE and force any character to draw two cards. If after, that character has more hand-cards than you, you then deal one damage to them."
                if self.max_health == 0:
                    self.check_brink_of_death_loop()

    def check_lament(self, source_player_index=0, targeted_index=0):
        # "Lament: Whenever any player is damaged by an ATTACK, you can discard any card, on-hand or equipped. The victim must then flip a judgement. If \u2660, the attacker flips their character card. If \u2665, the victim regains one health. If \u2663, the attacker discards two cards. If \u2666, the victim draws two cards."
        if (self.character_ability1.startswith("Lament:") or self.character_ability3.startswith("Lament:")):
            cards_discardable = (len(self.hand_cards.contents) + len(self.equipment_weapon) + len(
                self.equipment_armor) + len(self.equipment_offensive_horse) + len(self.equipment_defensive_horse))
            if cards_discardable > 0:
                print(
                    f"If \u2660: {players[source_player_index].character} flips their character card.")
                print(
                    f"If \u2665: {players[targeted_index].character} recovers one health.")
                print(
                    f"If \u2663: {players[source_player_index].character} discards two cards.")
                print(
                    f"If \u2666: {players[targeted_index].character} draws two cards.")
                message = f"{self.character}: Choose to activate Lament; discard a card and flip a judgement card, triggering one of the above effects?"
                if question_yes_no(message):
                    self.discard_from_equip_or_hand()
                    print(
                        f"  >> Character Ability: Lament; {self.character} discarded a card, and will force {players[targeted_index].character} to flip a judgement...")
                    main_deck.discard_from_deck()
                    judgement_card = discard_deck.contents[0]
                    print(
                        f"{players[targeted_index].character} flipped a {judgement_card}.")
                    judgement_card = check_judgement_tinkering(
                        judgement_card, targeted_index)

                    players[targeted_index].check_envy_of_heaven()
                    if players[targeted_index].check_beauty(judgement_card):
                        if judgement_card.suit == "\u2660" or judgement_card.suit == "\u2665":
                            if players[targeted_index].current_health < players[targeted_index].max_health:
                                players[targeted_index].current_health += 1
                                print(
                                    f"  >> Character Ability: Lament; {self.character} has forced {players[targeted_index].character} to regain one health ({players[targeted_index].current_health}/{players[targeted_index].max_health} HP remaining)!")
                                self.check_grudge(targeted_index, "Heal")

                    elif judgement_card.suit == "\u2660":
                        players[source_player_index].flipped_char_card = True
                        print(
                            f"  >> Character Ability: Lament; {self.character} has forced {players[source_player_index].character} to flip their character card!")

                    elif judgement_card.suit == "\u2665":
                        if players[targeted_index].current_health < players[targeted_index].max_health:
                            players[targeted_index].current_health += 1
                        print(
                            f"  >> Character Ability: Lament; {self.character} has forced {players[targeted_index].character} to regain one health ({players[targeted_index].current_health}/{players[targeted_index].max_health} HP remaining)!")

                    elif judgement_card.suit == "\u2663":
                        cards_discardable = (len(players[source_player_index].hand_cards.contents) + len(players[source_player_index].equipment_weapon) + len(
                            players[source_player_index].equipment_armor) + len(players[source_player_index].equipment_offensive_horse) + len(players[source_player_index].equipment_defensive_horse))
                        print(
                            f"  >> Character Ability: Lament; {self.character} has forced {players[source_player_index].character} to discard two cards!")
                        if cards_discardable < 2:
                            players[source_player_index].discard_all_cards()
                        else:
                            players[source_player_index].discard_from_equip_or_hand(
                                2)

                    elif judgement_card.suit == "\u2666":
                        players[targeted_index].hand_cards.draw(
                            main_deck, 2, False)
                        print(
                            f"  >> Character Ability: Lament; {self.character} has forced {players[targeted_index].character} to draw two cards!")

    def check_lightning_strike(self):
        # "Lightning Strike: Whenever you use a DEFEND card, you can target any other player to make a judgement. If the judgement card is of the suit \u2660, the target player suffers two points of lightning damage."
        if (self.character_ability1.startswith("Lightning Strike:") or self.character_ability3.startswith("Lightning Strike:")):

            user_index = 0
            for player_index, player in enumerate(players):
                if (self.character_ability1.startswith("Lightning Strike:") or self.character_ability3.startswith("Lightning Strike:")):
                    user_index = player_index
                    break

            message = f"{self.character}: Choose to activate Lightning Strike, make someone flip a judgement card; if \u2660, you deal two points of Lightning damage?"
            if question_yes_no(message):
                options_str = list_character_options(players)
                question = [
                    {
                        'type': 'list',
                        'name': 'Selected',
                        'message': f'{self.character}: Please select a character to target with Lightning Strike.',
                        'choices': options_str,
                        'filter': lambda player: options_str.index(player)
                    },
                ]
                answer = prompt(question, style=custom_style_2)
                selected_index = answer.get('Selected')
                print(
                    f"  >> Character Ability: Lightning Strike; {self.character} will force {players[selected_index].character} to flip a judgement. If \u2660, they take two lightning damage.")

                main_deck.discard_from_deck()
                judgement_card = discard_deck.contents[0]
                print(
                    f"{players[selected_index].character} flipped a {judgement_card}.")
                judgement_card = check_judgement_tinkering(
                    judgement_card, user_index)
                players[selected_index].check_envy_of_heaven()
                players[selected_index].check_exalt()

                if players[selected_index].check_beauty(judgement_card):
                    print(
                        f"  >> Character Ability: Lightning Strike; {players[selected_index].character}'s judgement card is a {judgement_card} and thus nothing happens.")

                elif judgement_card.suit == "\u2660":
                    damage_dealt = 2

                    fantasy = players[selected_index].check_fantasy(
                        damage_dealt)
                    if fantasy[0]:
                        selected_index = fantasy[1]

                    deplete_karma = players[selected_index].check_deplete_karma(
                        damage_dealt, user_index, None)
                    if deplete_karma[0]:
                        damage_dealt = deplete_karma[1]

                    players[selected_index].current_health -= damage_dealt
                    self.check_tyrant()
                    print(
                        f"  >> Character Ability: Lightning Strike; {players[selected_index].character}'s judgement card is a {judgement_card} and therefore they take {damage_dealt} lightning damage ({players[selected_index].current_health}/{players[selected_index].max_health} HP remaining).")
                    for player_index, player in enumerate(players):
                        player.check_relief()
                        if player.current_health < 1:
                            players[player_index].check_brink_of_death_loop(
                                player_index, user_index)

                    if players[selected_index].current_health > 0:
                        if fantasy[0]:
                            cards_to_draw = (
                                players[selected_index].max_health - players[selected_index].current_health)
                            print(
                                f"  >> Character Ability: Fantasy; {players[selected_index].character} draws {cards_to_draw} from the deck.")
                            players[selected_index].hand_cards.draw(
                                main_deck, cards_to_draw, False)

                        self.check_grudge(selected_index, "Damage")
                        players[selected_index].check_bequeathed_strategy(
                            damage_dealt)
                        players[selected_index].check_delayed_wisdom()
                        players[selected_index].check_eternal_loyalty(
                            damage_dealt)
                        players[selected_index].check_eye_for_an_eye(
                            user_index, "Activate")
                        players[selected_index].check_exile()
                        players[selected_index].check_geminate(damage_dealt)
                        players[selected_index].check_plotting_for_power(
                            damage_dealt, mode="Reaction")
                        players[selected_index].check_retaliation(
                            user_index, damage_dealt)
                else:
                    print(
                        f"  >> Character Ability: Lightning Strike; {players[selected_index].character}'s judgement card is a {judgement_card} and thus nothing happens.")

    def check_lingering_spirit(self):
        # "Lingering Spirit: If your health is not at maximum in your drawing phase, you can force any player to draw X cards, and then discard 1 card, or draw 1 card, and discard X cards. X is the amount of health you have missing from your maximum."
        if (self.character_ability1.startswith("Lingering Spirit:") or self.character_ability3.startswith("Lingering Spirit:") or self.character_ability4.startswith("Lingering Spirit:")):
            if self.max_health > self.current_health:
                difference = (self.max_health - self.current_health)
                message = f"{self.character}: Activate Lingering Spirit, forcing anyone to draw 1, then discard {difference} cards; OR draw {difference} cards then discard 1?"
                if question_yes_no(message):
                    options = [
                        Separator("------<Cannot target yourself>------")]
                    for player in players[1:]:
                        options.append(
                            str(player) + f" ({str(len(player.hand_cards.contents))} hand-cards)")
                    options.append(
                        Separator("--------------------Other--------------------"))
                    options.append("Cancel ability.")
                    question = [
                        {
                            'type': 'list',
                            'name': 'Selected',
                            'message': f'{self.character}: Please select a player to target with Lingering Spirit:',
                            'choices': options,
                            'filter': lambda player: options.index(player)
                        },
                    ]
                    answer = prompt(question, style=custom_style_2)
                    selected_index = answer.get('Selected')
                    if difference != 1:
                        question = [
                            {
                                'type': 'list',
                                'name': 'Selected',
                                'message': f'{self.character}: Make {players[selected_index].character} draw 1, then discard {difference}; or draw {difference} and then discard 1?',
                                'choices': [f"Draw 1, discard {difference}", f"Draw {difference}, discard 1"]
                            },
                        ]
                        answer = prompt(question, style=custom_style_2)
                        option_chosen = answer.get('Selected')
                        if option_chosen == f"Draw 1, discard {difference}":
                            cards_discardable = (len(players[selected_index].hand_cards.contents) + len(players[selected_index].equipment_weapon) + len(players[selected_index].equipment_armor) + len(
                                players[selected_index].equipment_offensive_horse) + len(players[selected_index].equipment_defensive_horse) + len(players[selected_index].pending_judgements))
                            print(
                                f"  >> Character Ability: Lingering Spirit; {self.character} has forced {players[selected_index].character} to draw 1, discard {difference}!")
                            players[selected_index].hand_cards.draw(
                                main_deck, 1, False)
                            if difference > cards_discardable:
                                players[selected_index].discard_all_cards()
                                players[selected_index].check_amassing_terrain()
                                players[selected_index].check_exertion(
                                    None, "Check")
                                players[selected_index].check_one_after_another()
                            else:
                                players[selected_index].discard_from_hand_or_equip(
                                    difference)
                                players[selected_index].check_amassing_terrain()
                                players[selected_index].check_exertion(
                                    None, "Check")
                                players[selected_index].check_one_after_another()
                        elif option_chosen == f"Draw {difference}, discard 1":
                            print(
                                f"  >> Character Ability: Lingering Spirit; {self.character} has forced {players[selected_index].character} to draw {difference}, discard 1!")
                            players[selected_index].hand_cards.draw(
                                main_deck, difference, False)
                            players[selected_index].discard_from_hand_or_equip(
                                1)
                            players[selected_index].check_amassing_terrain()
                            players[selected_index].check_exertion(
                                None, "Check")
                            players[selected_index].check_one_after_another()
                    else:
                        print(
                            f"  >> Character Ability: Lingering Spirit; {self.character} has forced {players[selected_index].character} to draw 1, discard 1!")
                        players[selected_index].hand_cards.draw(
                            main_deck, 1, False)
                        players[selected_index].discard_from_hand_or_equip(1)
                        players[selected_index].check_amassing_terrain()
                        players[selected_index].check_exertion(None, "Check")
                        players[selected_index].check_one_after_another()

    def check_mediocrity(self, phase="Draw"):
        # "Mediocrity: During your drawing phase, you draw an extra X cards, X being the total number of allegiances still in play. During your discard phase, you must discard at least as many card as there are allegiances still in play. If you have less cards than there are allegiances, you must discard all of them."
        if (self.character_ability1.startswith("Mediocrity:") or self.character_ability3.startswith("Mediocrity:")):
            if phase == "Draw":
                print(
                    f"  >> Character Ability: Mediocrity; {self.character} draws {check_allegiances_in_play()} extra card(s) (one for every allegiance still in play)!")
                return [True]

            elif phase == "Discard":
                cards_discardable = (len(self.hand_cards.contents) + len(self.equipment_weapon) + len(
                    self.equipment_armor) + len(self.equipment_offensive_horse) + len(self.equipment_defensive_horse))
                if check_allegiances_in_play() >= cards_discardable:
                    difference = (check_allegiances_in_play() -
                                  cards_discardable)
                    print(
                        f"  >> Character Ability: Mediocrity; {self.character} discards at least {check_allegiances_in_play()} cards (one for every allegiance in play) - they have no cards remaining.")
                    self.discard_all_cards()
                    return [True, difference]
                else:
                    print(
                        f"  >> Character Ability: Mediocrity; {self.character} discards at least {check_allegiances_in_play()} cards, one for every allegiance in play, and then down to their health-level ({self.current_health}/{self.max_health} HP remaining).")
                    difference1 = check_allegiances_in_play()
                    difference2 = 0
                    self.discard_from_equip_or_hand(difference1)
                    limit_increase = 0
                    if self.character_ability3 == "Bloodline (Ruler Ability): Your maximum hand-limit is increased by two for each other Hero character still alive." or self.character_ability4 == "Bloodline (Ruler Ability): Your maximum hand-limit is increased by two for each other Hero character still alive.":
                        heroes = []
                        for player in players:
                            if player.allegiance == 'Heroes':
                                heroes.append("1")
                        limit_increase = ((len(heroes)-1)*2)
                        if limit_increase > 0:
                            print(
                                f"  >> Character Ability: Bloodline (False Ruler Ability); {self.character}'s hand limit is increased by {limit_increase} (two for every other HERO character still alive).")
                    if len(self.hand_cards.list_cards()) > (self.current_health + limit_increase):
                        difference2 = (
                            len(self.hand_cards.list_cards()) - (self.current_health + limit_increase))
                        self.discard_from_equip_or_hand(difference2)
                    difference = difference1 + difference2
                    return [True, difference]
        return [False]

    def check_one_after_another(self):
        # "One After Another: Whenever you use or lose your last on-hand card, you can immediately draw one card from the deck."
        if (self.character_ability2.startswith("One After Another:") or self.character_ability3.startswith("One After Another:")):
            if len(self.hand_cards.contents) == 0:
                print(
                    f"  >> Character Ability: One After Another; {self.character} can draw a card whenever they use or lose their last on-hand card.")
                self.hand_cards.draw(main_deck, 1, False)

    def check_persuasion(self):
        # "Persuasion: At the beginning of your action phase, you can COMPETE with any other player; you both show a card simultaneously, and whoever has the higher value wins. If you win, you can either increase or decrease the number of targets to your next basic or non-delay tool card by one for this turn. There are no range restrictions to the extra target. If you lose, you cannot use any tool cards for this turn."
        if (self.character_ability1.startswith("Persuasion:") or self.character_ability3.startswith("Persuasion:")):
            message = f"{self.character}: Activate Persuasion, and COMPETE with a player? If you win, you can increase/decrease the number of targets for your next card. If you lose, you can't use tool-cards!"
            if question_yes_no(message):
                options = [Separator("------<Cannot target yourself>------")]
                for player in players[1:]:
                    if len(player.hand_cards.contents) > 0:
                        options.append(
                            str(player) + f" ({str(len(player.hand_cards.contents))} hand-cards)")
                    else:
                        options.append(
                            Separator("------" + str(player) + "------"))
                options.append(
                    Separator("--------------------Other--------------------"))
                options.append("Cancel ability.")
                question = [
                    {
                        'type': 'list',
                        'name': 'Selected',
                        'message': f'{self.character}: Please a target to COMPETE with:',
                        'choices': options,
                        'filter': lambda player: options.index(player)
                    },
                ]
                answer = prompt(question, style=custom_style_2)
                selected_index = answer.get('Selected')
                if options[selected_index] == "Cancel ability.":
                    return(' ')
                else:
                    my_card = self.activate_compete()
                    their_card = players[selected_index].activate_compete()
                    if my_card > their_card:
                        print(
                            f"  >> Character Ability: Persuasion; {self.character} won vs {players[selected_index].character} in their COMPETITION! He can increase/decrease targets on his next tool-card!")
                        self.check_ignore_formalities(my_card, their_card)
                        self.card_double = True
                    else:
                        print(
                            f"  >> Character Ability: Persuasion; {players[selected_index].character} won vs {self.character} in their COMPETITION! {self.character} can't use any tool cards for this turn!")
                        self.check_ignore_formalities(my_card, their_card)
                        self.tools_disabled = True

    def check_plotting_for_power(self, damage_dealt, mode="Reaction"):
        # "Plotting for Power: For every unit of damage you recieve, you can choose to draw one card and then set one hand-card face down as a RITE. Your hand limit is increased by one for each RITE."
        limit_increase = 0
        if (self.character_ability1.startswith("Plotting for Power:") or self.character_ability3.startswith("Plotting for Power:")):
            if mode == "Reaction":
                while damage_dealt > 0:
                    self.hand_cards.draw(main_deck, 1, False)
                    print(
                        f"  >> Character Ability: Plotting for Power; {self.character} has drawn one card.")
                    options_str = self.create_nonblind_menu(True)
                    question = [
                        {
                            'type': 'list',
                            'name': 'Selected',
                            'message': f'{self.character}: Please select a card to place down as a RITE:',
                            'choices': options_str,
                            'filter': lambda card: options_str.index(card)
                        },
                    ]

                    answer = prompt(question, style=custom_style_2)
                    rite_index = answer.get('Selected')
                    rite = self.hand_cards.contents.pop(rite_index)
                    self.rites.append(rite)
                    print(
                        f"  >> Character Ability: Plotting for Power; {self.character} has set one hand-card down aside as a RITE ({len(self.rites)} total RITE(S)).")
                    damage_dealt -= 1

            if mode == "Discard":
                limit_increase = len(self.rites)
                if limit_increase > 0:
                    print(
                        f"  >> Character Ability: Plotting for Power; {self.character}'s hand limit is increased by {limit_increase} (one for every RITE).")
        return limit_increase

    def check_raid(self):
        # "Raid: In your drawing phase, you can choose to forgo drawing cards from the deck and, instead, draw one on-hand card from a maximum of two other players."
        if (self.character_ability1.startswith("Raid:") or self.character_ability2.startswith("Raid:")):
            print(' ')
            message = f"{self.character}: Choose to activate Raid, and draw one hand-card from other player(s) instead of drawing from the deck?"
            if not question_yes_no(message):
                return False
            else:
                draw_from_players = 2
                selected_indexes = []
                options = [
                    Separator("------<Cannot target yourself>------")]
                for player in players[1:]:
                    if len(player.hand_cards.contents) > 0:
                        options.append(
                            str(player) + f" ({str(len(player.hand_cards.contents))} hand-cards)")
                    else:
                        options.append(Separator(
                            "------" + str(player) + f" ({str(len(player.hand_cards.contents))} hand-cards)" + "------"))
                options.append(
                    Separator("--------------------Other--------------------"))
                options.append("Target no others.")

                while draw_from_players > 0:
                    question = [
                        {
                            'type': 'list',
                            'name': 'Selected',
                            'message': f'{self.character}: Please select a character to draw a hand-card from:',
                            'choices': options,
                            'filter': lambda player: options.index(player)
                        },
                    ]
                    answer = prompt(question, style=custom_style_2)
                    target_index = answer.get('Selected')
                    if options[target_index] == "Target no others.":
                        draw_from_players = 0
                    else:
                        selected_indexes.append(target_index)
                        options.pop(target_index)
                        options.insert(target_index, (Separator(
                            "------<ALREADY SELECTED>------")))
                        draw_from_players -= 1

                for player_index in selected_indexes:
                    options = players[player_index].create_blind_menu()
                    question = [
                        {
                            'type': 'list',
                            'name': 'Selected',
                            'message': f"{self.character}: Please select which card you would like to take from {players[player_index].character}'s hand:",
                            'choices': options,
                            'filter': lambda card: options.index(card)
                        },
                    ]
                    answer = prompt(question, style=custom_style_2)
                    card_stolen_index = answer.get('Selected')
                    card_stolen = players[player_index].hand_cards.contents.pop(
                        card_stolen_index)
                    self.hand_cards.add_to_top(card_stolen)
                    print(
                        f"  >> Character Ability: Raid; {self.character} has drawn {card_stolen} from {players[player_index].character}'s hand.")
                    players[player_index].check_amassing_terrain()
                    players[player_index].check_exertion(None, "Check")
                    players[player_index].check_one_after_another()
                return True

    def check_reckless(self, card, source_player_index=0):
        # "Reckless: Every instance that you suffer damage from a red-suited ATTACK, or a WINE ATTACK, your maximum health limit is reduced by one instead."
        if (self.character_ability1.startswith("Reckless:") or self.character_ability3.startswith("Reckless:")):
            if players[source_player_index].check_beauty(card):
                if (card.suit == "\u2660") or (card.suit == "\u2665") or (card.suit == "\u2666") or (players[source_player_index].wine_active):
                    players[source_player_index].wine_active = False
                    self.max_health -= 1
                    if self.current_health > self.max_health:
                        self.current_health -= 1
                    print(
                        f"  >> Character Ability: Reckless; {self.character} has taken damage from {players[source_player_index].character}'s {card}, and therefore loses a maximum health! ({self.current_health}/{self.max_health} HP remaining)")
                    for player_index, player in enumerate(players):
                        if player.current_health < 1:
                            players[player_index].check_brink_of_death_loop(
                                player_index, source_player_index)
                    return True

            if (card.suit == "\u2665") or (card.suit == "\u2666") or (players[source_player_index].wine_active):
                players[source_player_index].wine_active = False
                self.max_health -= 1
                if self.current_health > self.max_health:
                    self.current_health -= 1
                print(
                    f"  >> Character Ability: Reckless; {self.character} has taken damage from {players[source_player_index].character}'s {card}, and therefore loses a maximum health! ({self.current_health}/{self.max_health} HP remaining)")
                for player_index, player in enumerate(players):
                    if player.current_health < 1:
                        players[player_index].check_brink_of_death_loop(
                            player_index, source_player_index)
                return True

    def check_recommence_the_legacy(self):
        # "Recommence the Legacy (Awakening Ability): If at the start of your turn, you have no on-hand cards, you must either regain one unit of health or draw two cards, and then reduce your maximum health limit by one. You then permanently gain the ability 'Astrology'."
        if self.character_ability2.startswith("Recommence the Legacy (Awakening Ability):"):
            if len(self.hand_cards.contents) == 0:
                self.awakened = True
                if self.current_health >= self.max_health:
                    choices = ["Draw two cards"]
                else:
                    choices = ["Regain one health", "Draw two cards"]
                question = [
                    {
                        'type': 'list',
                        'name': 'Selected',
                        'message': f'{self.character}: Please select an option:',
                        'choices': choices
                    },
                ]
                answer = prompt(question, style=custom_style_2)
                if answer.get('Selected') == "Regain one health":
                    self.current_health += 1
                    print(
                        f"  >> Character Ability: Recommence the Legacy (Awakening Ability): {self.character} has awakened; gaining one health and losing one maximum health. They also permanently gain the ability 'Astrology'.")
                if answer.get('Selected') == 'Draw two cards':
                    self.hand_cards.draw(main_deck, 2, False)
                    print(
                        f"  >> Character Ability: Recommence the Legacy (Awakening Ability): {self.character} has awakened; drawing two cards and losing one maximum health. They also permanently gain the ability 'Astrology'.")
                self.max_health -= 1
                if self.current_health > self.max_health:
                    self.current_health -= 1
                self.character_ability2 = "Recommence the Legacy (INACTIVE Ability): If at the start of your turn, you have no on-hand cards, you must either regain one unit of health or draw two cards, and then reduce your maximum health limit by one. You then permanently gain the ability 'Astrology'."
                self.character_ability3 = "Astrology: Before your judgement phase, you can view the top X cards of the deck (X being the number of players still in play, with a maximum of five). Of these X cards, you can rearrange the order of the cards, and choose any number to place at the top or bottom of the draw-deck."
                if self.max_health == 0:
                    self.check_brink_of_death_loop()

    def check_refusing_death(self, mode="Brink of Death"):
        # "Refusing Death: Whenever you are brought to the brink of death, you take a card from the deck and place it atop your character card. If the number on the card is different to all of the others, you return with one health. If the number matches another card, you discard this card and continue to be on the brink of death. When you have cards atop your character card, your hand limit becomes the number of cards atop your character card."
        if (self.character_ability1.startswith("Refusing Death:") or self.character_ability3.startswith("Refusing Death:")):
            if mode == "Brink of Death":
                main_deck.check_if_empty()
                refusing_death_card = main_deck.remove_from_top()
                self.refusing_death.append(refusing_death_card)
                card_numbers = []
                for card in self.refusing_death:
                    card_numbers.append(card.val)
                print(f"{self.character}: Refusing Death Values: {card_numbers}")
                if len(card_numbers) == len(set(card_numbers)):
                    print(
                        f"  >> Character Ability: Refusing Death; {self.character} has flipped a {refusing_death_card}! He returns with one health.")
                    self.current_health = 1
                else:
                    discard_deck.add_to_top(self.refusing_death.pop())
                    print(
                        f"  >> Character Ability: Refusing Death; {self.character} has flipped a {refusing_death_card}, but discards it and remains on the brink of death!")
                return False

            if mode == "Discard":
                if len(self.refusing_death) > 0:
                    limit_increase = (len(self.refusing_death) - 1)
                    return limit_increase
        return False

    def check_relief(self):
        # "Relief: When anyone is on the brink of death, you are able to play an ATTACK on the player taking their turn. If you hit, no damage is dealt, and instead a PEACH is automatically used on the character on the brink of death. This can only be activated outside of your turn."
        for player_index, player in enumerate(players):
            if (player.character_ability2.startswith("Relief:") or player.character_ability3.startswith("Relief:")):
                user_index = player_index
                break

        if (self.character_ability2.startswith("Relief:") or self.character_ability3.startswith("Relief:")):
            if self.character != players[0].character:
                for player_index, player in enumerate(players):
                    if player.current_health < 1:
                        dying_player_index = player_index
                        message = f"{self.character}: {players[dying_player_index].character} is on the brink of death. Activate Relief and ATTACK {players[0].character}? If hit, {players[dying_player_index].character} is healed?"
                        if question_yes_no(message):
                            card_played = Card(0, 'NONE', 'NONE', 'Tool', 'Barbarians',
                                               'NONE', None, 'Barbarians')
                            discarded = self.use_reaction_effect(
                                "Attack", 1, card_played, dying_player_index, user_index, "Relief")
                            if type(discarded) == Card:
                                if (discarded.effect == "Attack") or (discarded.effect2 == "Attack"):
                                    discarded.effect2 = "Attack"
                                    print(
                                        f"  >> Character Ability: Relief; {self.character} has ATTACKED {players[0].character} to save {players[dying_player_index].character} from the brink of death!")
                                    attack_defended = players[0].use_reaction_effect(
                                        "Defend", 1, discarded, user_index, 0)
                                    if type(attack_defended) == Card and (attack_defended.effect == "Defend" or attack_defended.effect2 == "Defend"):
                                        print(
                                            f"{players[0].character} successfully defended the ATTACK with {attack_defended}.")
                                    else:
                                        output_value = 1
                                        bonus_output = players[dying_player_index].check_rescued(
                                            user_index)
                                        if bonus_output == 1:
                                            output_value += bonus_output
                                        players[dying_player_index].current_health += output_value
                                        print(
                                            f"  >> Character Ability: Relief; {self.character} has healed {players[dying_player_index].character} by using a PEACH ({players[dying_player_index].current_health}/{players[dying_player_index].max_health} HP remaining)!")
                                        self.check_grudge(
                                            dying_player_index, "Heal")

    def check_relish(self, source_player_index=0, mode="Activate"):
        # "Relish: Whenever another player targets an ATTACK against you, they must discard a basic card, or else that ATTACK has no net effect on you."
        if mode == "Activate":
            if (self.character_ability1.startswith("Relish:") or self.character_ability3.startswith("Relish:")):
                cards_discardable = len(
                    players[source_player_index].hand_cards.contents)
                if cards_discardable > 0:
                    if not (players[source_player_index].check_relish(source_player_index, "Reaction")):
                        return True
                else:
                    print(
                        f"  >> Character Ability: Relish; {players[source_player_index].character} didn't discard a basic card! {self.character} is unaffected.")
                    return False

        if mode == "Reaction":
            for player_index, player in enumerate(players):
                if (player.character_ability1.startswith("Relish:") or player.character_ability3.startswith("Relish:")):
                    relish_player_index = player_index

            options_str = self.hand_cards.list_cards()
            options_str.append(
                Separator("--------------------Other--------------------"))
            options_str.append("Do nothing.")

            question = [
                {
                    'type': 'list',
                    'name': 'Selected',
                    'message': f'{players[source_player_index].character} - You cannot affect {players[relish_player_index].character} with an ATTACK unless you discard another basic card.',
                    'choices': options_str,
                    'filter': lambda card: options_str.index(card)
                },
            ]
            answer = prompt(question, style=custom_style_2)
            card_index = answer.get('Selected')
            if options_str[card_index] == "Do nothing.":
                print(
                    f"  >> Character Ability: Relish; {players[source_player_index].character} didn't discard a basic card! {players[relish_player_index].character} is unaffected.")
                return False
            card = self.hand_cards.contents.pop(card_index)
            discard_deck.add_to_top(card)

            if card.type == "Basic":
                print(
                    f"  >> Character Ability: Relish; {players[source_player_index].character} has discarded a basic card! {players[relish_player_index].character} must DEFEND as normal.")
                self.check_one_after_another()
                return True
            else:
                print(
                    f"  >> Character Ability: Relish; {players[source_player_index].character} didn't discard a basic card! {players[relish_player_index].character} is unaffected.")
                self.hand_cards.draw(discard_deck, 1, False)
                return False

    def check_rescued(self, reacting_player_index):
        # "Rescued (Ruler Ability): Whenever another member of Wu uses a PEACH to save you from the brink of death, it provides you with two units of health."
        if (self.role == 'Emperor') or (self.character_ability2.startswith("False Ruler:")) or (self.character_ability3.startswith("False Ruler:")):
            if (self.character_ability2.startswith("Rescued (Ruler Ability):") or self.character_ability3.startswith("Rescued (Ruler Ability):")):
                if players[reacting_player_index].character != self.character:
                    if players[reacting_player_index].allegiance == "Wu":
                        print(
                            f"  >> Character Ability: Rescued (Ruler Ability): {self.character} was saved from the brink of death by a member of Wu, and therefore recovers two health!")
                        return (1)
        else:
            return (0)

    def check_restraint(self):
        # "Restraint: If you did not use any ATTACK cards during your action phase, you can skip your discard phase."
        if (self.character_ability1.startswith("Restraint:") or self.character_ability3.startswith("Restraint:")):
            if self.attacks_this_turn == 0:
                print(
                    f"  >> Character Ability; Restraint: {self.character} skips their discard phase.")
                return True

    def check_retaliation(self, source_player_index=0, damage_dealt=1):
        # "Retaliation: For every one unit of damage you recieve, you can take one card (whether on-hand or equipped) from the player who was the source of that damage."
        if (self.character_ability1.startswith("Retaliation:") or self.character_ability3.startswith("Retaliation:")):
            cards_discardable = (len(players[source_player_index].hand_cards.contents) + len(players[source_player_index].equipment_weapon) + len(
                players[source_player_index].equipment_armor) + len(players[source_player_index].equipment_offensive_horse) + len(players[source_player_index].equipment_defensive_horse))
            while damage_dealt > 0:
                print(' ')
                if cards_discardable > 0:
                    message = f"{self.character}: Choose to activate Retaliation, and take a card (on-hand or equipped) from {players[source_player_index].character}?"
                    if question_yes_no(message):
                        self.activate_steal(
                            "Special", source_player_index, False)
                damage_dealt -= 1

    def check_second_wind(self, phase="Beginning"):
        # "Second Wind (Single-Use Ability): Once per game, at the beginning of your turn, you can return to the same amount of health that you had at the end of your previous turn. You draw a card for each unit of health that changes."
        if self.character_ability2.startswith("Second Wind (Single-Use Ability):"):
            if phase == "Beginning" and self.previous_turn_health != None:
                if not self.awakened:
                    message = f"{self.character}: Choose to activate Second Wind (Single-Use Ability), returning your health to what what it was at the end of your previous turn, and drawing a card for each unit changed."
                    if question_yes_no(message):
                        self.awakened = True
                        difference = abs(
                            self.previous_turn_health - self.current_health)
                        self.current_health += difference
                        print(
                            f"  >> Character Ability; Second Wind (Single-Use Ability): {self.character} has gone from {self.current_health} to {self.previous_turn_health} health points, and drawn {difference} cards.")
                        print("This ability cannot be used again!")
                        self.hand_cards.draw(main_deck, difference, False)
                        if self.current_health > self.max_health:
                            self.current_health = self.max_health
                        self.character_ability2 = "Second Wind (INACTIVE Ability): Once per game, at the beginning of your turn, you can return to the same amount of health that you had at the end of your previous turn. You draw a card for each unit of health that changes."

            elif phase == "End":
                self.previous_turn_health = self.current_health

    def check_shapeshift(self, phase="Start Game"):
        # "Shapeshift: After everyone has selected their character cards, you select two unused character cards at random from the deck. Select one of these two characters and place it before you, then state one of that character's abilities (excluding Single-Use, Awakening, INACTIVE and Ruler abilities). You will obtain the stated ability, the allegiance, and the gender of this character until you have replaced it. At the beginning and end of each turn, you can replace the character with another character and/or re-state another ability."
        if self.character_ability1.startswith("Shapeshift:"):
            char_cards_str = list_character_options(self.forms.contents)
            if phase != "Start Game":
                char_cards_str.append(
                    Separator("--------------------Other--------------------"))
                char_cards_str.append("Cancel ability.")
            question = [
                {
                    'type': 'list',
                    'name': 'Selected',
                    'message': f'{self.character}: Please select a character that you would like to shapeshift into, if any:',
                    'choices': char_cards_str,
                    'filter': lambda card: char_cards_str.index(card)
                },
            ]

            answer = prompt(question, style=custom_style_2)
            card_index = answer.get('Selected')
            if char_cards_str[card_index] == "Cancel ability.":
                return(' ')

            print(char_cards_str[card_index])
            print(
                self.forms.contents[card_index].character_ability_formatting())
            message = f"{self.character}: Please confirm you want to shapeshift into the above character, gaining their allegiance, gender, and one of their abilities."
            if question_yes_no(message):
                options_str = self.forms.contents[card_index].list_ability_options(
                )
                options_str.append(
                    Separator("--------------------Other--------------------"))
                options_str.append("Cancel ability.")

                question = [
                    {
                        'type': 'list',
                        'name': 'Selected',
                        'message': f'{self.character}: Please confirm which ability you want to acquire:',
                        'choices': options_str,
                        'filter': lambda ability: options_str.index(ability)
                    },
                ]
                answer = prompt(question, style=custom_style_2)
                chosen = answer.get('Selected')
                if options_str[chosen] == "Cancel ability.":
                    if phase == "Start Game":
                        self.check_shapeshift("Start Game")
                else:
                    if chosen == 0:
                        print(' ')
                        self.allegiance = self.forms.contents[card_index].allegiance
                        self.gender = self.forms.contents[card_index].gender
                        self.character_ability5 = "None"
                        self.character_ability4 = "None"
                        self.character_ability3 = self.forms.contents[card_index].character_ability1
                        print(
                            f"  >> Character Ability: Shapeshift; {self.character} has shapeshifted into {self.forms.contents[card_index]}, with the ability:\n {self.character_ability3}!")
                    elif chosen == 1:
                        print(' ')
                        if (self.forms.contents[card_index].character_ability2 != "Rouse (Ruler Ability): If you need to use an ATTACK, you can ask Sun Shang Xiang or any member of Shu to play it on your behalf." and self.forms.contents[card_index].character_ability2 != "Escort (Ruler Ability): If you need to use a DEFEND, you can ask any member of Wei to play it on your behalf." and self.forms.contents[card_index].character_ability2 != "Divinity (Awakening Ability): If, at the start of your turn, your health is one unit, you must reduce your maximum health by one. After which you permanently gain the abilities 'Dashing Hero' and 'Lingering Spirit'." and self.forms.contents[card_index].character_ability2 != "Rescued (Ruler Ability): Whenever another member of Wu uses a PEACH to save you from the brink of death, it provides you with two units of health." and self.forms.contents[card_index].character_ability2 != "Bloodline (Ruler Ability): Your maximum hand-limit is increased by two for each other Hero character still alive." and self.forms.contents[card_index].character_ability2 != "Recommence the Legacy (Awakening Ability): If at the start of your turn, you have no on-hand cards, you must either regain one unit of health or draw two cards, and then reduce your maximum health limit by one. You then permanently gain the ability 'Astrology'." and self.forms.contents[card_index].character_ability2 != "Second Wind (Single-Use Ability): Once per game, at the beginning of your turn, you can return to the same amount of health that you had at the end of your previous turn. You draw a card for each unit of health that changes." and self.forms.contents[card_index].character_ability2 != "Conduit (Awakening Ability): At the beginning of your turn, if you have three or more TERRAINS, you must reduce your maximum health by one unit. You then permanently gain the ability 'Blitz'." and self.forms.contents[card_index].character_ability2 != "Insurrection (Awakening Ability): Whenever you begin your turn with three or more RITES, you must either recover one unit of health or draw two cards. You must then decrease your maximum health by one and permanently gain the ability 'Rejection'." and self.forms.contents[card_index].character_ability2 != "Upheaval (Single-Use Ability): During your action phase, you can force every player, other than yourself, to use an ATTACK on another player with the least distance away. If a player is unable to do so, the player will lose one unit of health. Recipients of the ATTACK need to DEFEND to evade. This ability will proceed in succession starting from the player on your right." and self.forms.contents[card_index].character_ability2 != "Burning Heart (Single-Use Ability): When you kill another character, you can exchange role cards with the player you just killed. You cannot activate this ability if you are the emperor, or just killed the emperor."):
                            self.allegiance = self.forms.contents[card_index].allegiance
                            self.gender = self.forms.contents[card_index].gender
                            self.character_ability5 = "None"
                            self.character_ability4 = "None"
                            self.character_ability3 = self.forms.contents[card_index].character_ability2
                            print(
                                f"  >> Character Ability: Shapeshift; {self.character} has shapeshifted into {self.forms.contents[card_index]}, with the ability:\n  {self.character_ability3}!")
                        else:
                            print(
                                f"{self.character}: You cannot take any Awakening, Inactive, Ruler, or Single-Use abilities via Shapeshift.")
                            if phase == "Start Game":
                                self.check_shapeshift("Start Game")
                            else:
                                self.check_shapeshift("Turn")
                    elif chosen == 2:
                        print(' ')
                        if (self.forms.contents[card_index].character_ability3 != "Eiron (Awakening/Ruler Ability): At the start of your turn, if your health is the least or among the least, you must raise your maximum health by one unit, regain one unit of health, and permanently gain the ability 'Rouse'." and self.forms.contents[card_index].character_ability3 != "Exalt (Ruler Ability): Whenever any Wei character (other than yourself) makes a judgement, if the judgement card that takes effect is either \u2663 or \u2660, that character can choose to let you draw one card from the deck." and self.forms.contents[card_index].character_ability3 != "Dashing Hero (INACTIVE Ability): Draw an extra card at the start of your turn." and self.forms.contents[card_index].character_ability3 != "Amber Sky (Ruler Ability): All Hero characters can give you a DEFEND or LIGHTNING card during their individual turns." and self.forms.contents[card_index].character_ability3 != "Astrology (INACTIVE Ability): Before your judgement phase, you can view the top X cards of the deck (X being the number of players still in play, with a maximum of five). Of these X cards, you can rearrange the order of the cards, and choose any number to place at the top or bottom of the draw-deck." and self.forms.contents[card_index].character_ability3 != "Blitz (INACTIVE Ability): In your action phase, you can use any of your TERRAINS as STEAL." and self.forms.contents[card_index].character_ability3 != "Rejection (INACTIVE Ability): Once per turn, you can discard one RITE and force any character to draw two cards. If after, that character has more hand-cards than you, you then deal one damage to them."):
                            self.allegiance = self.forms.contents[card_index].allegiance
                            self.gender = self.forms.contents[card_index].gender
                            self.character_ability5 = "None"
                            self.character_ability4 = "None"
                            self.character_ability3 = self.forms.contents[card_index].character_ability3
                            print(
                                f"  >> Character Ability: Shapeshift; {self.character} has shapeshifted into {self.forms.contents[card_index]}, with the ability:\n  {self.character_ability3}!")
                        else:
                            print(
                                f"{self.character}: You cannot take any Awakening, Inactive, Ruler, or Single-Use abilities via Shapeshift.")
                            if phase == "Start Game":
                                self.check_shapeshift("Start Game")
                            else:
                                self.check_shapeshift("Turn")
                    elif chosen == 3:
                        print(' ')
                        if (self.forms.contents[card_index].character_ability4 != "Rouse (INACTIVE Ability): If you need to use an ATTACK, you can ask any member of Shu to play it on your behalf." and self.forms.contents[card_index].character_ability4 != "Lingering Spirit (INACTIVE Ability): If your health is not at maximum in your drawing phase, you can force any player to draw X cards, and then discard 1 card, or draw 1 card, and discard X cards. X is the amount of health you have missing from your maximum." and self.forms.contents[card_index].character_ability4 != "Tyrant (Ruler Ability): Whenever another Hero character causes damage to any other player, you can flip a judgement card. If the judgement card is of the suit \u2660, you can regain one unit of health."):
                            self.allegiance = self.forms.contents[card_index].allegiance
                            self.gender = self.forms.contents[card_index].gender
                            self.character_ability5 = "None"
                            self.character_ability4 = "None"
                            self.character_ability3 = self.forms.contents[card_index].character_ability4
                            print(
                                f"  >> Character Ability: Shapeshift; {self.character} has shapeshifted into {self.forms.contents[card_index]}, with the ability:\n  {self.character_ability3}!")
                        else:
                            print(
                                f"{self.character}: You cannot take any Awakening, Inactive, Ruler, or Single-Use abilities via Shapeshift.")
                            if phase == "Start Game":
                                self.check_shapeshift("Start Game")
                            else:
                                self.check_shapeshift("Turn")
                    elif chosen == 4:
                        print(' ')
                        if self.forms.contents[card_index].character_ability5 != "Hegemony (Ruler Ability): During the action phase of any other Wu characters, they can choose to COMPETE against you; you both show a card simultaneously, and whoever has the higher value wins. If they do not win, you can take both cards used. After your awakening ability activates, you are able to refuse COMPETE effects.":
                            self.allegiance = self.forms.contents[card_index].allegiance
                            self.gender = self.forms.contents[card_index].gender
                            self.character_ability5 = "None"
                            self.character_ability4 = "None"
                            self.character_ability3 = self.forms.contents[card_index].character_ability5
                            print(
                                f"  >> Character Ability: Shapeshift; {self.character} has shapeshifted into {self.forms.contents[card_index]}, with the ability:\n  {self.character_ability3}!")
                        else:
                            print(
                                f"{self.character}: You cannot take any Awakening, Inactive, Ruler, or Single-Use abilities via Shapeshift.")
                            if phase == "Start Game":
                                self.check_shapeshift("Start Game")
                            else:
                                self.check_shapeshift("Turn")

            elif phase == "Start Game":
                self.check_shapeshift("Start Game")

    def check_stabilization(self, cards_discarded=0):
        # "Stabilization: At the end of other players' discard phase, you can return one discarded card to that player. If you do so, you can take all of the other cards discarded in this phase as your own on-hand cards."
        if (self.character_ability2.startswith("Stabilization:") or self.character_ability3.startswith("Stabilization:")):
            if cards_discarded > 0:
                message = f"{self.character}: Activate Stabilization and return 1 discarded card to {players[0].character}? You keep the rest."
                if question_yes_no(message):
                    if cards_discarded == 1:
                        players[0].hand_cards.draw(discard_deck, 1, False)
                        print(
                            f"  >> Character Ability: Stabilization; {self.character} has returned a card to {players[0].character}!")
                    else:
                        stabilization = Player("Temporary")
                        stabilization.hand_cards.draw(
                            discard_deck, cards_discarded, False)
                        options_str = stabilization.create_nonblind_menu(True)
                        question = [
                            {
                                'type': 'list',
                                'name': 'Selected',
                                'message': f'{player.character}: Please select which card you would like to take:',
                                'choices': options_str,
                                'filter': lambda card: options_str.index(card)
                            },
                        ]
                        answer = prompt(question, style=custom_style_2)
                        card_index = answer.get('Selected')
                        drawn = stabilization.hand_cards.contents.pop(
                            card_index)
                        players[0].hand_cards.add_to_top(drawn)
                        total_cards = len(stabilization.hand_cards.contents)
                        while len(stabilization.hand_cards.contents) > 0:
                            self.hand_cards.add_to_top(
                                stabilization.hand_cards.contents.pop())
                        print(
                            f"  >> Character Ability: Stabilization; {self.character} has returned a card to {players[0].character}, and takes all other ({total_cards}) discarded cards for themselves!")

    def check_talent(self):
        # "Talent: You can use tool cards without range restrictions."
        if (self.character_ability2.startswith("Talent:") or self.character_ability3.startswith("Talent:")):
            print(
                f"  >> Character Ability: Talent; {self.character} has no range restriction on their tool cards.")
            return True

    def check_tyrant(self):
        # "Tyrant (Ruler Ability): Whenever another Hero character causes damage to any other player, you can flip a judgement card. If the judgement card is of the suit \u2660, you can regain one unit of health."
        if self.allegiance == "Heroes":
            emperor_index = None
            false_ruler_index = None
            for player_index, player in enumerate(players):
                if (player.character_ability3.startswith("Tyrant (Ruler Ability):") or player.character_ability4.startswith("Tyrant (Ruler Ability):")):
                    if (player.role == "Emperor"):
                        emperor_index = player_index
                    else:
                        false_ruler_index = player_index

            if emperor_index != None:
                if false_ruler_index != None:
                    message = f'{self.character}: Choose to activate Tyrant (Ruler Ability), to allow the emperor (or false-ruler) to flip a judgement card? If \u2660, they heal one!'
                elif self.role != "Emperor":
                    message = f'{self.character}: Choose to activate Tyrant (Ruler Ability), to allow the emperor to flip a judgement card? If \u2660, they heal one!'
                else:
                    return(' ')

                if question_yes_no(message):
                    target_indexes = [emperor_index]

                    if self.role == "Emperor":
                        if (false_ruler_index != None):
                            target_index = false_ruler_index

                    elif self.role != "Emperor":
                        if false_ruler_index == None:
                            target_index = emperor_index

                        elif (false_ruler_index != None) and (self.character == players[false_ruler_index].character):
                            target_index = emperor_index

                        else:
                            options = [str(players[emperor_index]), str(
                                players[false_ruler_index]), "Both players!"]
                            question = [
                                {
                                    'type': 'list',
                                    'name': 'Selected',
                                    'message': f'{self.character}: Please select which target will flip a judgement (Tyrant):',
                                    'choices': options,
                                },
                            ]
                            answer = prompt(question, style=custom_style_2)
                            selected = answer.get('Selected')
                            if selected == "Both players!":
                                target_indexes = [
                                    emperor_index, false_ruler_index]
                            elif selected == str(players[emperor_index]):
                                target_indexes = [emperor_index]
                            else:
                                target_indexes = [false_ruler_index]

                    for target_index in target_indexes:
                        print(
                            f"  >> Ruler Ability: Tyrant; {self.character} has allowed {players[target_index].character} to flip a judgement! If \u2660, they heal by one!")
                        main_deck.discard_from_deck()
                        judgement_card = discard_deck.contents[0]
                        print(
                            f"{players[target_index].character} flipped a {judgement_card}.")
                        judgement_card = check_judgement_tinkering(
                            judgement_card, target_index)

                        if judgement_card.suit == "\u2660":
                            if players[target_index].max_health > players[target_index].current_health:
                                players[target_index].current_health += 1
                                print(
                                    f"  >> Ruler Ability: Tyrant; {players[target_index].character} flipped a \u2660 and therefore heals by one ({players[target_index].current_health}/{players[target_index].max_health} HP remaining)!")
                            else:
                                print(
                                    f"  >> Ruler Ability: Tyrant; {players[target_index].character} is already at full health, and the judgement has no effect ({players[target_index].current_health}/{players[target_index].max_health} HP remaining)!")
                        else:
                            print(
                                f"  >> Ruler Ability: Tyrant; {players[target_index].character} did not flip a \u2660, so no effect!")

    def check_unmitigated_murder(self):
        # "Unmitigated Murder: During your turn, with the exception of yourself, only characters on the brink of death can use a PEACH."
        if (self.character_ability1.startswith("Unmitigated Murder:") or self.character_ability3.startswith("Unmitigated Murder:")):
            print(
                f"  >> Character Ability: Unmitigated Murder; On his turn, with the exception of {self.character}, only characters on the brink of death can use a PEACH.")
            return True

    def check_unnatural_death(self, cards_discarded):
        # "Unnatural Death: You can immediately take possession of all cards (both on-hand and equipped) of any player that dies."
        if cards_discarded == None:
            return (' ')
        if self.current_health == 0:
            return (' ')
        if (self.character_ability1.startswith("Unnatural Death:") or self.character_ability3.startswith("Unnatural Death:")):
            print(
                f"  >> Character Ability: Unnatural Death; All discarded hands are added to the hand of {self.character}.")
            self.hand_cards.draw(discard_deck, cards_discarded, False)

    def check_warrior_woman(self):
        # "Warrior Woman: Whenever any equipped card is removed from your equipment, you can immediately draw two cards from the deck."
        if (self.character_ability2.startswith("Warrior Woman:") or self.character_ability3.startswith("Warrior Woman:")):
            print(
                f"  >> Character Ability: Warrior Woman; {self.character} immediately draws 2 cards from the deck whenever their equipment card is destroyed/removed/replaced.")
            self.hand_cards.draw(main_deck, 2, False)

    def check_wisdom(self):
        # "Wisdom: Whenever you use a non-delay tool card, you immediately draw a card from the deck."
        if (self.character_ability1.startswith("Wisdom:") or self.character_ability3.startswith("Wisdom:")):
            print(
                f"  >> Character Ability: Wisdom; {self.character} immediately draws a card from the deck after using a non-delay tool card.")
            self.hand_cards.draw(main_deck, 1, False)

    def check_without_equal(self, mode="Attack"):
        # "Without Equal: Whenever you use ATTACK, your target has to use two DEFEND cards to successfully evade the attack. During a DUEL, your opponent has to use two ATTACK cards for every one ATTACK card that you use."
        if (self.character_ability1.startswith("Without Equal:") or self.character_ability3.startswith("Without Equal:")):
            if mode == "Attack":
                print(
                    f"  >> Character Ability: Without Equal; {self.character}'s victim must play two DEFEND cards for every ATTACK that {self.character} plays!")
                return True

            if mode == "Duel":
                print(
                    f"  >> Character Ability: Without Equal; {self.character}'s victim must play two ATTACK cards for every ATTACK that {self.character} plays!")
                return True

# Activatable abilities (reusable)
    def activate_blitz(self):
        # "Blitz: In your action phase, you can use any of your TERRAINS as STEAL."
        if self.character_ability3.startswith("Blitz:"):
            if len(self.terrains) < 1:
                print(
                    f"{self.character}: You do not have enough TERRAINS to perform this ability.")

            else:
                options_str = []
                for card in self.terrains:
                    options_str.append(str(card))
                options_str.append(
                    Separator("--------------------Other--------------------"))
                options_str.append("Cancel ability.")
                question = [
                    {
                        'type': 'list',
                        'name': 'Selected',
                        'message': f'{self.character}: Please select a TERRAIN to use as STEAL:',
                        'choices': options_str,
                        'filter': lambda card: options_str.index(card)
                    },
                ]
                answer = prompt(question, style=custom_style_2)
                terrain_index = answer.get('Selected')
                if options_str[terrain_index] == "Cancel ability.":
                    return (' ')
                else:
                    card = self.terrains.pop(terrain_index)
                    card.effect2 = "Steal"
                    print(
                        f"  >> Character Ability: Blitz; {self.character} has discarded a TERRAIN: {card} to use as STEAL!")
                    if not self.use_card_effect("Special", card):
                        self.terrains.append(card)
                        print(
                            f"{self.character} cancelled using their effect, and their TERRAIN: {card} was returned.")
                    else:
                        discard_deck.add_to_top(card)

    def activate_blockade(self):
        # "Blockade: During your action phase, you can choose to use any of your basic or equipment cards with suit \u2663 or \u2660 as RATIONS DEPLETED with a physical range of -1 in distance calculations. RATIONS DEPLETED acts as a time-delay tool card, in which a player will have to flip a judgement at the start of their turn. If the judgement is any suit other than \u2663, the target fails the judgement and must skip their drawing phase."
        if (self.character_ability1.startswith("Blockade:") or self.character_ability3.startswith("Blockade:")):
            cards_discardable = (len(self.hand_cards.contents) + len(self.equipment_weapon) + len(
                self.equipment_armor) + len(self.equipment_offensive_horse) + len(self.equipment_defensive_horse))
            if cards_discardable > 0:
                options_str = self.create_nonblind_menu()
                options_str.append(
                    Separator("--------------------Other--------------------"))
                options_str.append("Cancel ability.")
                options = self.create_actual_menu()

                question = [
                    {
                        'type': 'list',
                        'name': 'Selected',
                        'message': f"{self.character}: Please select 'black-suited, basic' or 'black-suited, equipment' card to use as RATIONS DEPLETED?",
                        'choices': options_str,
                        'filter': lambda card: options_str.index(card)
                    },
                ]
                answer = prompt(question, style=custom_style_2)
                discarded_index = answer.get('Selected')

                if options_str[discarded_index] == "Cancel ability.":
                    return (' ')

                if (options[discarded_index].suit == "\u2660" or options[discarded_index].suit == "\u2663") and (options[discarded_index].type == "Basic" or options[discarded_index].type == "Weapon" or options[discarded_index].type == "Armor" or options[discarded_index].type == "-1 Horse" or options[discarded_index].type == "+1 Horse"):
                    # Check if hand-card
                    if discarded_index < len(self.hand_cards.contents):
                        card = self.hand_cards.contents.pop(
                            discarded_index)
                        print(
                            f"  >> Character Ability: Blockade; {self.character} has discarded {card} from their hand to use as RATIONS DEPLETED.")

                    # Check if equipment-card
                    else:
                        if discarded_index == (len(self.hand_cards.contents) + 1):
                            card = self.equipment_weapon.pop()
                            self.weapon_range = 1
                            self.weapon_popped = True
                            print(
                                f"  >> Character Ability: Blockade; {self.character} has discarded {card} from their weapon-slot to use as RATIONS DEPLETED.")

                        if discarded_index == (len(self.hand_cards.contents) + 2):
                            card = self.equipment_armor.pop()
                            self.armor_popped = True
                            print(
                                f"  >> Character Ability: Blockade; {self.character} has discarded {card} from their armor-slot to use as RATIONS DEPLETED.")

                        if discarded_index == (len(self.hand_cards.contents) + 3):
                            card = self.equipment_offensive_horse.pop()
                            self.off_horse_popped = True
                            print(
                                f"  >> Character Ability: Blockade; {self.character} has discarded {card} from their horse-slot to use as RATIONS DEPLETED.")

                        if discarded_index == (len(self.hand_cards.contents) + 4):
                            card = self.equipment_defensive_horse.pop()
                            self.def_horse_popped = True
                            print(
                                f"  >> Character Ability: Blockade; {self.character} has discarded {card} from their horse-slot to use as RATIONS DEPLETED.")

                    card.effect2 = "Rations Depleted"
                    if not self.use_card_effect("Special", card):
                        if self.weapon_popped:
                            discard_deck.contents.pop(0)
                            self.weapon_range = card.weapon_range
                        if self.armor_popped:
                            self.equipment_armor.append(card)
                        if self.off_horse_popped:
                            self.equipment_offensive_horse.append(card)
                        if self.def_horse_popped:
                            self.equipment_defensive_horse.append(card)
                        else:
                            self.hand_cards.draw(discard_deck, 1, False)
                        print(
                            f"{self.character} cancelled using their effect, and {card} was returned.")
                    else:
                        discard_deck.add_to_top(card)
                else:
                    print(
                        f"{options[discarded_index]} cannot be used as RATIONS DEPLETED as it is NOT a black-suited, basic/equipment card.")

    def activate_blunt_advice(self):
        # "Blunt Advice: During your action phase, you can put an on-hand equipment card in the equipment area of another character (you cannot replace something already equipped). If you do so, you draw a card."
        if (self.character_ability1.startswith("Blunt Advice:") or self.character_ability3.startswith("Blunt Advice:")):
            usable_cards = []
            for card in self.hand_cards.contents:
                if card.effect == "Weapon" or card.effect == "Armor" or card.effect == "-1 Horse" or card.effect == "+1 Horse":
                    usable_cards.append(card)

            if len(usable_cards) < 1:
                print(
                    f"{self.character}: You cannot use this ability as you do not have any equipment cards in your hand!")

            else:
                options = self.create_nonblind_menu(True)
                options.append(
                    Separator("--------------------Other--------------------"))
                options.append("Cancel ability.")
                options = self.create_actual_menu()
                question = [
                    {
                        'type': 'list',
                        'name': 'Selected',
                        'message': f"{self.character}: Please select an equipment card to pass to another player:",
                        'choices': options,
                        'filter': lambda card: options.index(card)
                    },
                ]
                answer = prompt(question, style=custom_style_2)
                card_index = answer.get('Selected')
                card = self.hand_cards.contents[card_index]
                if (card.type != "Weapon" and card.type != "Armor" and card.type != "-1 Horse" and card.type != "+1 Horse"):
                    print(
                        f"{self.character}: You can't use this card as it is not an equipment card!")
                    return None
                else:
                    self.hand_cards.contents.pop(card_index)

                if card.type == "Weapon":
                    for player in players:
                        if len(player.equipment_weapon) == 0:
                            options.append(str(
                                player) + f" ///  W:[{len(player.equipment_weapon)}] / A:[{len(player.equipment_armor)}] / H:[{len(player.equipment_offensive_horse)}] / H:[{len(player.equipment_defensive_horse)}] / PJ:[{len(player.pending_judgements)}]")
                        else:
                            options.append(Separator(
                                "------" + str(player) + f" (has a weapon!)" + "------"))
                elif card.type == "Armor":
                    for player in players:
                        if len(player.equipment_armor) == 0:
                            options.append(str(
                                player) + f" ///  W:[{len(player.equipment_weapon)}] / A:[{len(player.equipment_armor)}] / H:[{len(player.equipment_offensive_horse)}] / H:[{len(player.equipment_defensive_horse)}] / PJ:[{len(player.pending_judgements)}]")
                        else:
                            options.append(Separator(
                                "------" + str(player) + f" (has armor!)" + "------"))
                elif card.type == "-1 Horse":
                    for player in players:
                        if len(player.equipment_offensive_horse) == 0:
                            options.append(str(
                                player) + f" ///  W:[{len(player.equipment_weapon)}] / A:[{len(player.equipment_armor)}] / H:[{len(player.equipment_offensive_horse)}] / H:[{len(player.equipment_defensive_horse)}] / PJ:[{len(player.pending_judgements)}]")
                        else:
                            options.append(Separator(
                                "------" + str(player) + f" (has a -1 horse!)" + "------"))
                elif card.type == "+1 Horse":
                    for player in players:
                        if len(player.equipment_defensive_horse) == 0:
                            options.append(str(
                                player) + f" ///  W:[{len(player.equipment_weapon)}] / A:[{len(player.equipment_armor)}] / H:[{len(player.equipment_offensive_horse)}] / H:[{len(player.equipment_defensive_horse)}] / PJ:[{len(player.pending_judgements)}]")
                        else:
                            options.append(Separator(
                                "------" + str(player) + f" (has a -1 horse!)" + "------"))

                question = [
                    {
                        'type': 'list',
                        'name': 'Selected',
                        'message': f'{self.character}: Please select to whom you would like to donate {card}:',
                        'choices': options,
                        'filter': lambda player: options.index(player)
                    },
                ]
                answer = prompt(question, style=custom_style_2)
                target_index = answer.get('Selected')

                if card.type == "Weapon":
                    players[target_index].equipment_weapon.append(card)
                    players[target_index].weapon_range = card.weapon_range
                    print(
                        f"  >> Character Ability: Blunt Advice; {self.character} has placed {card} in the weapon-slot of {players[target_index].character}! {self.character} draws a card.")
                    self.hand_cards.draw(main_deck, 1, False)

                elif card.type == "Armor":
                    players[target_index].equipment_armor.append(card)
                    print(
                        f"  >> Character Ability: Blunt Advice; {self.character} has placed {card} in the armor-slot of {players[target_index].character}! {self.character} draws a card.")
                    self.hand_cards.draw(main_deck, 1, False)

                elif card.type == "-1 Horse":
                    players[target_index].equipment_offensive_horse.append(
                        card)
                    print(
                        f"  >> Character Ability: Blunt Advice; {self.character} has placed {card} in the horse-slot of {players[target_index].character}! {self.character} draws a card.")
                    self.hand_cards.draw(main_deck, 1, False)

                elif card.type == "+1 Horse":
                    players[target_index].equipment_defensive_horse.append(
                        card)
                    print(
                        f"  >> Character Ability: Blunt Advice; {self.character} has placed {card} in the horse-slot of {players[target_index].character}! {self.character} draws a card.")
                    self.hand_cards.draw(main_deck, 1, False)

    def activate_dragon_heart(self, mode="Check"):
        # "Dragon Heart: Your ATTACK and DEFEND cards can be used interchangeably."
        if (self.character_ability1.startswith("Dragon Heart:") or self.character_ability3.startswith("Dragon Heart:")):
            if mode == "Check":
                return True

            if mode == "Activate" or mode == "Reaction Attack" or mode == "Reaction Defend":
                cards_discardable = len(self.hand_cards.contents)
                if cards_discardable > 0:
                    usable_cards = []
                    for card in self.hand_cards.contents:
                        if card.effect == "Attack" or card.effect == "Defend":
                            usable_cards.append(card)

                    if len(usable_cards) < 1:
                        print(
                            f"{self.character}: You cannot use this ability as you have no ATTACK or DEFEND cards.")

                    else:
                        options_str = self.create_nonblind_menu(True)
                        options_str.append(
                            Separator("--------------------Other--------------------"))
                        options_str.append("Cancel ability.")

                        question = [
                            {
                                'type': 'list',
                                'name': 'Selected',
                                'message': f'{self.character}: Please select a card that will be used as ATTACK or DEFEND:',
                                'choices': options_str,
                                'filter': lambda card: options_str.index(card)
                            },
                        ]
                        answer = prompt(question, style=custom_style_2)
                        discarded_index = answer.get('Selected')

                        if options_str[discarded_index] == "Cancel ability.":
                            return (' ')

                        card = self.hand_cards.contents.pop(discarded_index)
                        if card.effect == "Attack" or card.effect == "Defend":

                            if mode == "Activate":
                                card.effect2 = "Attack"
                                if not self.use_card_effect("Special", card):
                                    self.hand_cards.contents.append(card)
                                    print(
                                        f"{self.character} cancelled using their effect, and {card} was returned.")
                                else:
                                    discard_deck.add_to_top(card)

                            if mode == "Reaction Attack":
                                if card.effect == "Defend":
                                    print(
                                        f"  >> Character Ability: Dragon Heart; {self.character} has discarded {card} from their hand to use as ATTACK.")
                                discard_deck.add_to_top(card)
                                card.effect2 == "Attack"
                                return (card)

                            if mode == "Reaction Defend":
                                if card.effect == "Attack":
                                    print(
                                        f"  >> Character Ability: Dragon Heart; {self.character} has discarded {card} from their hand to use as DEFEND.")
                                discard_deck.add_to_top(card)
                                card.effect2 == "Defend"
                                return (card)

                        else:
                            print(
                                f"{self.hand_cards.contents[discarded_index]} cannot be used for this effect - needs to be an ATTACK or DEFEND.")

    def activate_drown_in_wine(self, mode="Check"):
        # "Drown in Wine: You can use any of your on-hand cards with suit of \u2660 as WINE. WINE can be used on yourself the brink of death to restore one unit of health, or to increase the damage of their next ATTACK by one damage."
        if (self.character_ability1.startswith("Drown in Wine:") or self.character_ability3.startswith("Drown in Wine:")):
            usable_cards = []
            for card in self.hand_cards.contents:
                if card.suit == "\u2660":
                    usable_cards.append(card)

            if mode == "Check":
                return True

            if mode == "Activate" or mode == "Reaction":
                if len(usable_cards) < 1:
                    print(
                        f"{self.character}: You cannot use this ability as you have no hand-cards that are \u2660.")
                else:
                    discarded = self.discard_from_hand_boolpop("\u2660")
                    if discarded != None:
                        if mode == "Activate":
                            print(
                                f"  >> Character Ability: Drown in Wine; {self.character} has discarded {discarded} from their hand to use as WINE - Their next attack will do two damage.")
                            self.wine_active = True

                        if mode == "Reaction":
                            print(
                                f"  >> Character Ability: Drown in Wine; {self.character} has discarded {discarded} from their hand to use as WINE!")
                        return True
                    else:
                        print(
                            f"{self.character}: That card cannot be used as WINE as is it NOT of suit \u2660.")

    def activate_heavens_justice(self):
        # "Heaven's Justice: Once per turn, you can COMPETE with any player; you both show a card simultaneously, and whoever has the higher value wins. If you win, you can use an additional ATTACK, and each ATTACK has unlimited range and can target an additional player. If you lose, you cannot attack this turn."
        if (self.character_ability1.startswith("Heaven's Justice:") or self.character_ability3.startswith("Heaven's Justice:")):
            pass

    def activate_horsebow(self, mode="Check"):
        # "Horsebow: You can use any equipment cards as an ATTACK. Whenever you do so, that ATTACK has unlimited range."
        if (self.character_ability1.startswith("Horsebow:") or self.character_ability3.startswith("Horsebow:")):
            if mode == "Check":
                return True

            if mode == "Activate" or mode == "Reaction":
                cards_discardable = (len(self.hand_cards.contents) + len(self.equipment_weapon) + len(
                    self.equipment_armor) + len(self.equipment_offensive_horse) + len(self.equipment_defensive_horse))
                if cards_discardable > 0:
                    usable_cards = []
                    for card in self.hand_cards.contents:
                        if card.type == "Weapon" or card.type == "Armor" or card.type == "-1 Horse" or card.type == "+1 Horse":
                            usable_cards.append(card)
                    for card in self.equipment_weapon:
                        usable_cards.append(card)
                    for card in self.equipment_armor:
                        usable_cards.append(card)
                    for card in self.equipment_offensive_horse:
                        usable_cards.append(card)
                    for card in self.equipment_defensive_horse:
                        usable_cards.append(card)

                    if len(usable_cards) < 1:
                        print(
                            f"{self.character}: You cannot use this ability as you have no EQUIPMENT cards.")

                    else:
                        options_str = self.create_nonblind_menu()
                        options_str.append(
                            Separator("--------------------Other--------------------"))
                        options_str.append("Cancel ability.")
                        options = self.create_actual_menu()

                        question = [
                            {
                                'type': 'list',
                                'name': 'Selected',
                                'message': f'{self.character}: Please select an EQUIPMENT card to use as ATTACK with unlimited range?',
                                'choices': options_str,
                                'filter': lambda card: options_str.index(card)
                            },
                        ]
                        answer = prompt(question, style=custom_style_2)
                        discarded_index = answer.get('Selected')
                        weapon_popped = False
                        armor_popped = False
                        off_horse_popped = False
                        def_horse_popped = False

                        if options_str[discarded_index] == "Cancel ability.":
                            return (' ')

                        if options[discarded_index].type == "Weapon" or options[discarded_index].type == "Armor" or options[discarded_index].type == "-1 Horse" or options[discarded_index].type == "+1 Horse":
                            temp_range_variable = self.weapon_range
                            self.weapon_range = 6
                            # Check if hand-card
                            if discarded_index < len(self.hand_cards.contents):
                                card = self.hand_cards.contents.pop(
                                    discarded_index)
                                print(
                                    f"  >> Character Ability: Horsebow; {self.character} has discarded {card} from their hand to use as ATTACK with unlimited range.")

                            # Check if equipment-card
                            else:
                                if discarded_index == (len(self.hand_cards.contents) + 1):
                                    card = self.equipment_weapon.pop()
                                    self.weapon_range = 1
                                    weapon_popped = True
                                    print(
                                        f"  >> Character Ability: Horsebow; {self.character} has discarded {card} from their weapon-slot to use as ATTACK with unlimited range.")

                                if discarded_index == (len(self.hand_cards.contents) + 2):
                                    card = self.equipment_armor.pop()
                                    armor_popped = True
                                    print(
                                        f"  >> Character Ability: Horsebow; {self.character} has discarded {card} from their armor-slot to use as ATTACK with unlimited range.")

                                if discarded_index == (len(self.hand_cards.contents) + 3):
                                    card = self.equipment_offensive_horse.pop()
                                    off_horse_popped = True
                                    print(
                                        f"  >> Character Ability: Horsebow; {self.character} has discarded {card} from their horse-slot to use as ATTACK with unlimited range.")

                                if discarded_index == (len(self.hand_cards.contents) + 4):
                                    card = self.equipment_defensive_horse.pop()
                                    def_horse_popped = True
                                    print(
                                        f"  >> Character Ability: Horsebow; {self.character} has discarded {card} from their horse-slot to use as ATTACK with unlimited range.")

                            card.effect2 = "Attack"
                            if mode == "Activate":
                                if not self.use_card_effect("Special", card):
                                    if weapon_popped:
                                        self.equipment_weapon.append(card)
                                        self.weapon_range = card.weapon_range
                                    if armor_popped:
                                        self.equipment_armor.append(card)
                                        self.weapon_range = temp_range_variable
                                    if off_horse_popped:
                                        self.equipment_offensive_horse.append(
                                            card)
                                        self.weapon_range = temp_range_variable
                                    if def_horse_popped:
                                        self.equipment_defensive_horse.append(
                                            card)
                                        self.weapon_range = temp_range_variable
                                    else:
                                        self.hand_cards.add_to_top(card)
                                        self.weapon_range = temp_range_variable
                                    print(
                                        f"{self.character} cancelled using their effect, and {card} was returned.")
                                else:
                                    self.weapon_range = temp_range_variable
                                    discard_deck.add_to_top(card)

                            if mode == "Reaction":
                                if weapon_popped:
                                    self.weapon_range = 1
                                else:
                                    self.weapon_range = temp_range_variable
                                discard_deck.add_to_top(card)
                                return (card)

                        else:
                            print(
                                f"{options[discarded_index]} cannot be used as an ATTACK as is it NOT an EQUIPMENT card.")

    def activate_national_colours(self):
        # "National Colours: During your action phase, you can use any of your cards (on-hand or equipped) with a \u2666 suit as ACEDIA."
        if (self.character_ability1.startswith("National Colours:") or self.character_ability3.startswith("National Colours:")):
            cards_discardable = (len(self.hand_cards.contents) + len(self.equipment_weapon) + len(
                self.equipment_armor) + len(self.equipment_offensive_horse) + len(self.equipment_defensive_horse))
            if cards_discardable > 0:
                card = self.discard_from_equip_or_hand_boolpop("\u2666")
                if card != None:
                    print(
                        f"  >> Character Ability: National Colours; {self.character} has discarded {card} to use as ACEDIA.")
                    card.effect2 = "Acedia"
                    if not self.use_card_effect("Special", card):
                        if self.weapon_popped:
                            self.equipment_weapon.append(card)
                            self.weapon_range = card.weapon_range
                        if self.armor_popped:
                            self.equipment_armor.append(card)
                        if self.off_horse_popped:
                            self.equipment_offensive_horse.append(card)
                        if self.def_horse_popped:
                            self.equipment_defensive_horse.append(card)
                        else:
                            self.hand_cards.add_to_top(card)
                        print(
                            f"{self.character} cancelled using their effect, and {card} was returned.")
                else:
                    print(
                        f"{self.character}: That card cannot be used as ACEDIA as is it NOT of suit \u2666.")

    def activate_random_strike(self):
        # "Random Strike: You can use any two hand-cards which have the same suit as RAIN OF ARROWS."
        if (self.character_ability1.startswith("Random Strike:") or self.character_ability3.startswith("Random Strike:")):
            if len(self.hand_cards.contents) > 1:
                options = self.create_nonblind_menu(True)
                options.append(
                    Separator("--------------------Other--------------------"))
                options.append("Cancel ability.")

                question = [
                    {
                        'type': 'list',
                        'name': 'Selected',
                        'message': f'{self.character}: Please select two hand-cards to discard and play as RAIN OF ARROWS:',
                        'choices': options,
                        'filter': lambda card: options.index(card)
                    },
                ]
                answer = prompt(question, style=custom_style_2)
                card1_index = answer.get('Selected')

                if options[card1_index] == "Cancel ability.":
                    return (' ')

                card1 = self.hand_cards.contents[card1_index]
                options.pop(card1_index)
                options.insert(card1_index, Separator(
                    "------" + str(card1) + "------"))

                question = [
                    {
                        'type': 'list',
                        'name': 'Selected',
                        'message': f'{self.character}: Please select one more card to discard and play as RAIN OF ARROWS:',
                        'choices': options,
                        'filter': lambda card: options.index(card)
                    },
                ]
                answer = prompt(question, style=custom_style_2)
                card2_index = answer.get('Selected')
                if options[card2_index] == "Cancel ability.":
                    return (' ')

                if (self.hand_cards.contents[card1_index].suit) == (self.hand_cards.contents[card2_index].suit):
                    discarded1 = self.hand_cards.contents.pop(card1_index)
                    discard_deck.add_to_top(discarded1)
                    self.hand_cards.contents.insert(card1_index, "Placeholder")
                    discarded2 = self.hand_cards.contents.pop(card2_index)
                    discard_deck.add_to_top(discarded2)
                    self.hand_cards.contents.remove("Placeholder")
                    print(
                        f"  >> Character Ability: Random Strike; {self.character} has activated Random Strike!")
                    discarded1.effect2 = "Rain of Arrows"
                    discarded2.effect2 = "Rain of Arrows"
                    if not self.use_card_effect("Special", discarded1, "Special", discarded2):
                        self.hand_cards.draw(discard_deck, 2, False)
                        print(
                            f"{self.character} cancelled using their effect, and their cards were returned.")

                else:
                    print(
                        f"{self.character}: You must use two cards of the SAME suit to use Random Strike!")

    def activate_rejection(self):
        # "Rejection: Once per turn, you can discard one RITE and force any character to draw two cards. If after, that character has more hand-cards than you, you then deal one damage to them."
        if self.character_ability3.startswith("Rejection:"):
            if len(self.rites) < 1:
                print(
                    f"{self.character}: You do not have enough RITES to perform this ability.")

            else:
                options_str = []
                for player in players:
                    options_str.append(str(player))
                options_str.append(
                    Separator("--------------------Other--------------------"))
                options_str.append("Cancel ability.")

                question = [
                    {
                        'type': 'list',
                        'name': 'Selected',
                        'message': f'{self.character}: Please select a target for Rejection; discard a RITE to force anyone to draw two. If they have more hand-cards than you, then you deal one damage to them:',
                        'choices': options_str,
                        'filter': lambda player: options_str.index(player)
                    },
                ]
                answer = prompt(question, style=custom_style_2)
                selected_index = answer.get('Selected')
                if options_str[selected_index] == "Cancel ability.":
                    return(' ')
                else:
                    discard_deck.add_to_top(self.rites.pop())
                    print(
                        f"  >> Character Ability: Rejection; {self.character} has forced {players[selected_index].character} to draw two cards!")
                    players[selected_index].hand_cards.draw(
                        main_deck, 2, False)
                    if len(players[selected_index].hand_cards.contents) > len(self.hand_cards.contents):
                        damage_dealt = 1

                        fantasy = players[selected_index].check_fantasy(
                            damage_dealt, 0)
                        if fantasy[0]:
                            selected_index = fantasy[1]

                        deplete_karma = players[selected_index].check_deplete_karma(
                            damage_dealt, 0, None)
                        if deplete_karma[0]:
                            damage_dealt = deplete_karma[1]

                        players[selected_index].current_health -= damage_dealt
                        print(
                            f"  >> Character Ability: Rejection; {players[selected_index].character} has more cards than {self.character}, so they take {damage_dealt} damage! ({players[selected_index].current_health}/{players[selected_index].max_health} HP remaining)")
                        for player_index, player in enumerate(players):
                            player.check_relief()
                            if player.current_health < 1:
                                players[player_index].check_brink_of_death_loop(
                                    player_index, 0)

                        if players[selected_index].current_health > 0:
                            if fantasy[0]:
                                cards_to_draw = (
                                    players[selected_index].max_health - players[selected_index].current_health)
                                print(
                                    f"  >> Character Ability: Fantasy; {players[selected_index].character} draws {cards_to_draw} from the deck.")
                                players[selected_index].hand_cards.draw(
                                    main_deck, cards_to_draw, False)
                            self.check_grudge(selected_index, "Damage")
                            players[selected_index].check_bequeathed_strategy(
                                damage_dealt)
                            players[selected_index].check_delayed_wisdom()
                            players[selected_index].check_eternal_loyalty(
                                damage_dealt)
                            players[selected_index].check_exile()
                            players[selected_index].check_eye_for_an_eye(
                                0, "Activate")
                            players[selected_index].check_geminate(
                                damage_dealt)
                            players[selected_index].check_plotting_for_power(
                                damage_dealt, mode="Reaction")
                            players[selected_index].check_retaliation(
                                0, damage_dealt)

    def activate_rouse(self, mode="Check"):
        # "Rouse (Ruler Ability): If you need to use an ATTACK, you can ask Sun Shang Xiang or any member of Shu to play it on your behalf."
        emperor_index = None
        false_ruler_index = None
        for player_index, player in enumerate(players):
            if (player.character_ability2.startswith("Rouse (Ruler Ability):") or player.character_ability3.startswith("Rouse (Ruler Ability):")):
                if (player.role == "Emperor"):
                    emperor_index = player_index
                else:
                    false_ruler_index = player_index

        if mode == "Check":
            if (self.role == "Emperor") or (self.character_ability2.startswith("False Ruler:")) or (self.character_ability3.startswith("False Ruler:")):
                if (self.character_ability2.startswith("Rouse (Ruler Ability):") or self.character_ability3.startswith("Rouse (Ruler Ability):") or self.character_ability4.startswith("Rouse (Ruler Ability):")):
                    return True

        if mode == "Activate" or mode == "Reaction":
            if self.character == players[emperor_index].character:
                targets = []
                for player in players:
                    targets.append(
                        Separator("------" + str(player) + "------"))
                for player_index, player in enumerate(players):
                    if player.role != "Emperor" and (player.allegiance == "Shu" or player.character == "Sun Shang Xiang"):
                        targets.pop(player_index)
                        targets.insert(player_index, str(
                            players[player_index]))
            elif self.character == players[false_ruler_index].character:
                targets = []
                for player in players:
                    targets.append(
                        Separator("------" + str(player) + "------"))
                for player_index, player in enumerate(players):
                    if player.allegiance == "Shu" or player.character == "Sun Shang Xiang":
                        targets.pop(player_index)
                        targets.insert(player_index, str(
                            players[player_index]))
            targets.append(
                Separator("--------------------Other--------------------"))
            targets.append("Cancel ability.")
            question = [
                {
                    'type': 'list',
                    'name': 'Selected',
                    'message': f'{self.character}: Please select a player to ATTACK for you via Rouse (Ruler Ability):',
                    'choices': targets,
                    'filter': lambda player: targets.index(player)
                },
            ]
            answer = prompt(question, style=custom_style_2)
            attacker_index = answer.get('Selected')
            if targets[attacker_index] == "Cancel ability.":
                return [False]

            if mode == "Activate":
                if self.character == players[emperor_index].character:
                    player_index = emperor_index
                elif self.character == players[false_ruler_index].character:
                    player_index = false_ruler_index

                card_played = Card(0, 'NONE', 'NONE', 'Tool', 'Barbarians',
                                   'NONE', None, 'Barbarians')
                discarded = players[attacker_index].use_reaction_effect(
                    "Attack", 1, card_played, attacker_index, player_index, "Rouse")
                if type(discarded) == Card:
                    if (discarded.effect == "Attack") or (discarded.effect2 == "Attack"):
                        discarded.effect2 = "Attack"
                        print(
                            f"  >> Ruler Ability: Rouse; {players[attacker_index].character} has played an ATTACK on {self.character}'s behalf!")
                        if not self.use_card_effect("Special", discarded):
                            return False

            if mode == "Reaction":
                print(
                    f"  >> Ruler Ability: Rouse; {self.character} has asked {players[attacker_index].character} to play an ATTACK on their behalf!")
                return [True, attacker_index, player_index]

    def activate_surprise(self):
        # "Surprise: During your action phase, you can use any of your black-suited cards (on-hand or equipped) as DISMANTLE."
        if (self.character_ability1.startswith("Surprise:") or self.character_ability3.startswith("Surprise:")):
            cards_discardable = (len(self.hand_cards.contents) + len(self.equipment_weapon) + len(
                self.equipment_armor) + len(self.equipment_offensive_horse) + len(self.equipment_defensive_horse))
            if cards_discardable > 0:
                card = self.discard_from_equip_or_hand_boolpop(
                    "\u2660", "\u2663")
                if card != None:
                    print(
                        f"  >> Character Ability: National Colours; {self.character} has discarded {card} to use as DISMANTLE.")
                    card.effect2 = "Dismantle"
                    if not self.use_card_effect("Special", card):
                        if self.weapon_popped:
                            self.equipment_weapon.append(card)
                            self.weapon_range = card.weapon_range
                        if self.armor_popped:
                            self.equipment_armor.append(card)
                        if self.off_horse_popped:
                            self.equipment_offensive_horse.append(card)
                        if self.def_horse_popped:
                            self.equipment_defensive_horse.append(card)
                        else:
                            self.hand_cards.add_to_top(card)
                        print(
                            f"{self.character} cancelled using their effect, and {card} was returned.")
                else:
                    print(
                        f"{self.character}: That card cannot be used as DISMANTLE as is it NOT of suit \u2660 or \u2663.")

    def activate_trojan_flesh(self):
        # "Trojan Flesh: During your action phase, you can choose to lose one unit of health to draw two more cards from the deck. This ability can be used repeatedly in a turn."
        if (self.character_ability1.startswith("Trojan Flesh:") or self.character_ability3.startswith("Trojan Flesh:")):
            message = f"{self.character}: Choose to activate Trojan Flesh; losing one health to draw two cards from the deck?"
            if question_yes_no(message):
                print(
                    f"  >> Character Ability: Trojan Flesh; {self.character} lost one health to draw two cards from the deck.")
                self.current_health -= 1
                for player in players:
                    player.check_relief()
                if self.current_health < 1:
                    if self.check_brink_of_death_loop(0, "Self") == "Break":
                        return "Break"
                else:
                    self.hand_cards.draw(main_deck, 2, False)
                    self.check_geminate(1)

    def activate_warrior_saint(self, mode="Check"):
        # "Warrior Saint: You can use any red-suited cards (on-hand or equipped) as an ATTACK."
        if (self.character_ability2.startswith("Warrior Saint:") or self.character_ability3.startswith("Warrior Saint:")):
            if mode == "Check":
                return True

            if mode == "Activate" or mode == "Reaction":
                cards_discardable = (len(self.hand_cards.contents) + len(self.equipment_weapon) + len(
                    self.equipment_armor) + len(self.equipment_offensive_horse) + len(self.equipment_defensive_horse))
                if cards_discardable > 0:
                    card = self.discard_from_equip_or_hand_boolpop(
                        "\u2665", "\u2666")
                    if card != None:
                        print(
                            f"  >> Character Ability: Warrior Saint; {self.character} has discarded {card} to use as ATTACK.")
                        card.effect2 = "Attack"
                        if not self.use_card_effect("Special", card):
                            if self.weapon_popped:
                                self.equipment_weapon.append(card)
                                self.weapon_range = card.weapon_range
                            if self.armor_popped:
                                self.equipment_armor.append(card)
                            if self.off_horse_popped:
                                self.equipment_offensive_horse.append(card)
                            if self.def_horse_popped:
                                self.equipment_defensive_horse.append(card)
                            else:
                                self.hand_cards.add_to_top(card)
                            print(
                                f"{self.character} cancelled using their effect, and {card} was returned.")
                    else:
                        print(
                            f"{self.character}: That card cannot be used as ATTACK as is it NOT of suit \u2665 or \u2666.")

                    if mode == "Reaction":
                        discard_deck.add_to_top(card)
                        card.effect2 == "Attack"
                        return (card)

# Activatable abilities (once-per-turn)
    def activate_alliance(self):
        # "Alliance: During your action phase, you can choose to force any two players (other than yourself) to exchange their entire set of on-hand cards by discarding X number of cards, X being the difference between the number of on-hand cards between these two players. Limited to one use per turn."
        if (self.character_ability2.startswith("Alliance:") or self.character_ability3.startswith("Alliance:")):
            if self.used_alliance:
                print(f"{self.character}: You can only use Alliance once per turn.")

            else:
                cards_discardable = (len(self.hand_cards.contents) + len(self.equipment_weapon) + len(
                    self.equipment_armor) + len(self.equipment_offensive_horse) + len(self.equipment_defensive_horse))
                options = [
                    Separator("------<Cannot target yourself>------")]
                for player in players[1:]:
                    options.append(
                        str(player) + f" ({str(len(player.hand_cards.contents))} hand-cards)")
                options.append(
                    Separator("--------------------Other--------------------"))
                options.append("Cancel ability.")
                question = [
                    {
                        'type': 'list',
                        'name': 'Selected',
                        'message': f'{self.character}: Please select two players that you will target with Alliance, swapping both their hands (note, you discard the difference):',
                        'choices': options,
                        'filter': lambda player: options.index(player)
                    },
                ]
                answer = prompt(question, style=custom_style_2)
                selected1_index = answer.get('Selected')
                options.pop(selected1_index)
                options.insert(selected1_index, (Separator("---" +
                                                           str(player) + f" ({str(len(player.hand_cards.contents))} hand-cards)---")))
                question = [
                    {
                        'type': 'list',
                        'name': 'Selected',
                        'message': f'{self.character}: Please select a second player that you will target with Alliance, swapping both their hands (note, you discard the difference):',
                        'choices': options,
                        'filter': lambda player: options.index(player)
                    },
                ]
                answer = prompt(question, style=custom_style_2)
                selected2_index = answer.get('Selected')
                if len(players[selected1_index].hand_cards.contents) != len(players[selected2_index].hand_cards.contents):
                    difference = abs(len(players[selected1_index].hand_cards.contents) - len(
                        players[selected2_index].hand_cards.contents))
                    if difference > cards_discardable:
                        print(
                            f"{self.character}: You have insufficient cards to cause an exchange!")
                        return (' ')
                    self.discard_from_equip_or_hand(difference)

                players[selected1_index].hand_cards.contents, players[selected2_index].hand_cards.contents = players[
                    selected2_index].hand_cards.contents, players[selected1_index].hand_cards.contents
                print(
                    f"  >> Character Ability: Alliance; {self.character} has discarded {difference} cards, and forced {players[selected1_index].character} and {players[selected2_index].character} to swap hands!")
                self.used_alliance = True

    def activate_amber_sky(self):
        # "Amber Sky (Ruler Ability): All Hero characters can give you a DEFEND or LIGHTNING card during their individual turns."
        emperor_index = None
        false_ruler_index = None
        if self.used_amber_sky:
            print(f"{self.character}: You can only use Amber Sky once per turn.")

        else:
            for player_index, player in enumerate(players):
                if (player.character_ability3.startswith("Amber Sky (Ruler Ability):") or player.character_ability4.startswith("Amber Sky (Ruler Ability):")):
                    if player.role == "Emperor":
                        emperor_index = player_index
                    else:
                        false_ruler_index = player_index

            if self.allegiance == "Heroes":
                if self.role == "Emperor":
                    if (false_ruler_index != None):
                        target = players[false_ruler_index]

                elif self.role != "Emperor":
                    if false_ruler_index == None:
                        target = players[emperor_index]

                    elif (false_ruler_index != None) and (self.character == players[false_ruler_index].character):
                        target = players[emperor_index]

                    else:
                        options = [str(players[emperor_index]),
                                   str(players[false_ruler_index])]

                        question = [
                            {
                                'type': 'list',
                                'name': 'Selected',
                                'message': f'{self.character}: Please select who you will target with Amber Sky:',
                                'choices': options,
                            },
                        ]
                        answer = prompt(question, style=custom_style_2)
                        selected = answer.get('Selected')
                        if selected == str(players[emperor_index]):
                            target = players[emperor_index]
                        else:
                            target = players[false_ruler_index]

                options = self.create_nonblind_menu(True)
                options.append(
                    Separator("--------------------Other--------------------"))
                options.append("Cancel ability.")
                question = [
                    {
                        'type': 'list',
                        'name': 'Selected',
                        'message': f'{self.character}: Please select a DEFEND or LIGHTNING card to give to {target.character}?',
                        'choices': options,
                        'filter': lambda card: options.index(card)
                    },
                ]
                answer = prompt(question, style=custom_style_2)
                card_index = answer.get('Selected')

                if options[card_index] == "Cancel ability.":
                    return (' ')

                else:
                    card = self.hand_cards.contents[card_index]
                    if (card.effect == "Defend") or (card.effect == "Lightning"):
                        discarded = self.hand_cards.contents.pop(
                            card_index)
                        target.hand_cards.add_to_top(
                            discarded)
                        print(
                            f"  >> Ruler Ability: Amber Sky; {self.character} gave {discarded} to {target.character} in their turn!")
                        self.used_amber_sky = True
                    else:
                        print(
                            f"{self.character}: You can only give a DEFEND or LIGHTNING CARD with this effect.")

    def activate_benevolence(self):
        # "Benevolence: You can give any number of your hand-cards to any players. If you give away more than one card, you recovers one unit of health."
        if (self.character_ability1.startswith("Benevolence:") or self.character_ability3.startswith("Benevolence:")):
            if self.used_benevolence:
                print(
                    f"{self.character}: You can only use Benevolence once per turn!")

            else:
                cards_discardable = len(self.hand_cards.contents)
                cards_to_donate = 0
                options = self.create_nonblind_menu(True)
                options.append(
                    Separator("--------------------Other--------------------"))
                options.append("No more cards.")
                options.append("Cancel ability.")
                selected_cards = []
                while cards_discardable > 0:
                    question = [
                        {
                            'type': 'list',
                            'name': 'Selected',
                            'message': f'{self.character}: Please select cards to discard and redraw:',
                            'choices': options,
                            'filter': lambda card: options.index(card)
                        },
                    ]
                    answer = prompt(question, style=custom_style_2)
                    card_index = answer.get('Selected')
                    if options[card_index] == "Cancel ability.":
                        return (' ')
                    elif options[card_index] == "No more cards.":
                        if cards_to_donate == 0:
                            return (' ')
                        cards_discardable = 0
                    else:
                        selected_cards.append(card_index)
                        options.pop(card_index)
                        options.insert(card_index, (Separator(
                            "------<ALREADY SELECTED>------")))
                        cards_discardable -= 1
                        cards_to_donate += 1

                for card_index in selected_cards:
                    card = self.hand_cards.contents[card_index]
                    options = [
                        Separator("------<Cannot target yourself>------")]
                    for player in players[1:]:
                        options.append(
                            str(player) + f" ({str(len(player.hand_cards.contents))} hand-cards)")
                    question = [
                        {
                            'type': 'list',
                            'name': 'Selected',
                            'message': f'{self.character}: Please decide to whom you would like to give {card} to:',
                            'choices': options,
                            'filter': lambda player: options.index(player)
                        },
                    ]
                    answer = prompt(question, style=custom_style_2)
                    player_index = answer.get('Selected')
                    players[player_index].hand_cards.add_to_top(
                        self.hand_cards.contents.pop(card_index))
                    self.hand_cards.contents.insert(card_index, "Placeholder")
                    print(
                        f"  >> Character Ability: Benevolence; {self.character} has given a card to {players[player_index].character}!")

                for item in self.hand_cards.contents:
                    if "Placeholder" in self.hand_cards.contents:
                        self.hand_cards.contents.remove("Placeholder")
                print(
                    f"  >> Character Ability: Benevolence; {self.character} has donated {cards_to_donate} to other players.")
                if self.max_health > self.current_health:
                    print(
                        f"  >> Character Ability: Benevolence; {self.character} has recovered 1 unit of health ({self.current_health}/{self.max_health} HP remaining)!")
                self.used_benevolence = True
                return(' ')

    def activate_brilliant_scheme(self, mode="Activate"):
        # "Brilliant Scheme: Once per turn, you can give another player an ATTACK or equipment card. The player can then choose to draw one card or allow you to choose one character within their attacking range. This character is ATTACKed by the player that recieved the card."
        if mode == "Activate":
            if (self.character_ability1.startswith("Brilliant Scheme:") or self.character_ability3.startswith("Brilliant Scheme:")):
                if self.used_brilliant_scheme:
                    print(
                        f"{self.character}: You can only use Brilliant Scheme once per turn.")

                cards_discardable = (len(self.hand_cards.contents) + len(self.equipment_weapon) + len(
                    self.equipment_armor) + len(self.equipment_offensive_horse) + len(self.equipment_defensive_horse))
                if cards_discardable > 0:
                    options = [
                        Separator("------<Cannot target yourself>------")]
                    for player in players[1:]:
                        options.append(str(player))
                    options.append(
                        Separator("--------------------Other--------------------"))
                    options.append("Cancel ability.")

                    question = [
                        {
                            'type': 'list',
                            'name': 'Selected',
                            'message': f'{self.character}: Who would you like to target with Brilliant Scheme and give a card to?',
                            'choices': options,
                            'filter': lambda player: options.index(player)
                        },
                    ]
                    answer = prompt(question, style=custom_style_2)
                    scheme_index = answer.get('Selected')

                    if options[scheme_index] == "Cancel ability.":
                        return (' ')

                    options = self.create_nonblind_menu()
                    options.append(
                        Separator("--------------------Other--------------------"))
                    options.append("Cancel ability.")

                    question = [
                        {
                            'type': 'list',
                            'name': 'Selected',
                            'message': f'{self.character}: Please select an ATTACK or EQUIPMENT card to give to {players[scheme_index].character}:',
                            'choices': options,
                            'filter': lambda player: options.index(player)
                        },
                    ]
                    answer = prompt(question, style=custom_style_2)
                    card_index = answer.get('Selected')
                    if options[card_index] == "Cancel ability.":
                        return (' ')

                    # Check if hand-card
                    elif card_index < len(self.hand_cards.contents):
                        if (self.hand_cards.contents[card_index - 1].effect == "Attack") or (self.hand_cards.contents[card_index - 1].effect == "Weapon") or (self.hand_cards.contents[card_index - 1].effect == "Armor") or (self.hand_cards.contents[card_index - 1].effect == "-1 Horse") or (self.hand_cards.contents[card_index - 1].effect == "+1 Horse"):
                            card = self.hand_cards.contents.pop(
                                card_index)
                            players[scheme_index].hand_cards.add_to_top(
                                card)
                        else:
                            print(
                                f"{self.character}: You must give an ATTACK or EQUIPMENT card for Brilliant Scheme!")
                            return(' ')

                    # Check if equipment-card
                    else:
                        if card_index == (len(self.hand_cards.contents) + 1):
                            card = self.equipment_weapon.pop()
                            players[scheme_index].hand_cards.add_to_top(
                                card)
                            self.weapon_range = 1
                            print(
                                f"{self.character} has removed {card} from their weapon-slot.")

                        if card_index == (len(self.hand_cards.contents) + 2):
                            card = self.equipment_armor.pop()
                            players[scheme_index].hand_cards.add_to_top(
                                card)
                            print(
                                f"{self.character} has removed {card} from their armor-slot.")

                        if card_index == (len(self.hand_cards.contents) + 3):
                            card = self.equipment_offensive_horse.pop()
                            players[scheme_index].hand_cards.add_to_top(
                                card)
                            print(
                                f"{self.character} has removed {card} from their horse-slot.")

                        if card_index == (len(self.hand_cards.contents) + 4):
                            card = self.equipment_defensive_horse.pop()
                            players[scheme_index].hand_cards.add_to_top(
                                card)
                            print(
                                f"{self.character} has removed {card} from their horse-slot.")

                    self.used_brilliant_scheme = True
                    print(
                        f"  >> Character Ability: Brilliant Scheme; {self.character} gave {players[scheme_index].character} a {card}!")
                    if players[scheme_index].activate_brilliant_scheme("Reaction"):
                        options = players[scheme_index].create_targeting_menu(
                            "Weapon", scheme_index)
                        question = [
                            {
                                'type': 'list',
                                'name': 'Selected',
                                'message': f'{self.character}: Please select someone for {players[scheme_index].character} to ATTACK:',
                                'choices': options,
                                'filter': lambda player: options.index(player)
                            },
                        ]
                        answer = prompt(question, style=custom_style_2)
                        target_index = answer.get('Selected')
                        main_deck.check_if_empty()
                        attack_card = main_deck.contents[0]
                        attack_card.effect2 = "Colourless Attack"
                        players[scheme_index].activate_attack(
                            attack_card, target_index, scheme_index)

        if mode == "Reaction":
            # Draw a card or allow Chen Gong to choose a target in your attack range. You then attack them with a colourless attack!
            question = [
                {
                    'type': 'list',
                    'name': 'Selected',
                    'message': f'{self.character}: Please select an option from the following:',
                    'choices': ["Draw a card.", f"Allow {players[0].character} to choose a target to ATTACK."],
                },
            ]
            answer = prompt(question, style=custom_style_2)
            chosen = answer.get('Selected')
            if chosen == "Draw a card.":
                self.hand_cards.draw(main_deck, 1, False)
                print(
                    f"  >> Character Ability: Brilliant Scheme; {self.character} has chosen to draw a card!")
                return False
            else:
                print(
                    f"  >> Character Ability: Brilliant Scheme; {self.character} chose to attack a player!")
                return True

    def activate_dazzle(self):
        # "Dazzle: During your action phase, you can give a card with suit of \u2665 to another player. Then, you can take any of their cards (on-hand or equipped), and give it to any character. Limited to one use per turn."
        if (self.character_ability2.startswith("Dazzle:") or self.character_ability3.startswith("Dazzle:")):
            if self.used_dazzle:
                print(f"{self.character}: You can only use Dazzle once per turn.")

            elif len(self.hand_cards.contents) > 0:
                card = self.discard_from_hand_boolpop("\u2665")
                if card != None:
                    options = [
                        Separator("------<Cannot target yourself>------")]
                    for player in players[1:]:
                        options.append(
                            str(player) + f" ({str(len(player.hand_cards.contents))} hand-cards)")
                    question = [
                        {
                            'type': 'list',
                            'name': 'Selected',
                            'message': f'{self.character}: Please decide to whom you would like to give {card} to:',
                            'choices': options,
                            'filter': lambda player: options.index(player)
                        },
                    ]
                    answer = prompt(question, style=custom_style_2)
                    player_index = answer.get('Selected')
                    print(
                        f"  >> Character Ability: Dazzle; {self.character} has given {players[player_index].character} a {card}. Now, he can take one of their cards, and redistribute it!")
                    players[player_index].hand_cards.shuffle()
                    self.activate_steal("Special", player_index, False)
                    gift_card = self.hand_cards.remove_from_top()
                    options = []
                    for player in players:
                        options.append(
                            str(player) + f" ({str(len(player.hand_cards.contents))} hand-cards)")
                    options.pop(player_index)
                    options.insert(player_index, Separator(
                        "-------<Cannot target player>-------"))
                    question = [
                        {
                            'type': 'list',
                            'name': 'Selected',
                            'message': f'{self.character}: Please decide to whom you would like to give {gift_card} to:',
                            'choices': options,
                            'filter': lambda player: options.index(player)
                        },
                    ]
                    answer = prompt(question, style=custom_style_2)
                    player_index = answer.get('Selected')
                    players[player_index].hand_cards.add_to_top(gift_card)
                    print(
                        f"  >> Character Ability: Dazzle; {self.character} has given {gift_card} to {players[player_index].character}!")
                    self.used_dazzle = True
                else:
                    print(
                        f"{self.character}: That card cannot be used for DAZZLE as is it NOT of suit \u2665.")

    def activate_ferocious_assault(self):
        # "Ferocious Assault: During your action phase, you can inflict one unit of damage to any player within your attacking range by either; reducing one unit of your own health, or discarding one weapon card (on-hand or equipped). Limited to one use per turn."
        if (self.character_ability1.startswith("Ferocious Assault:") or self.character_ability3.startswith("Ferocious Assault:")):
            if self.used_ferocious_assault:
                print(
                    f"{self.character}: You can only use Ferocious Assault once per turn.")

            else:
                options_str = self.create_targeting_menu("Weapon", 0)
                options_str.append(
                    Separator("--------------------Other--------------------"))
                options_str.append("Cancel ability.")
                question = [
                    {
                        'type': 'list',
                        'name': 'Selected',
                        'message': f'{self.character}: Who would you like to damage with Ferocious Assault?',
                        'choices': options_str,
                        'filter': lambda player: options_str.index(player)
                    },
                ]
                answer = prompt(question, style=custom_style_2)
                selected_index = answer.get('Selected')
                if options_str[selected_index] == "Cancel ability.":
                    return(' ')

                options_str = ["Lose 1 unit of health."]
                usable_cards = []
                for card in self.hand_cards.contents:
                    if card.type == "Weapon":
                        usable_cards.append(card)
                for card in self.equipment_weapon:
                    usable_cards.append(card)
                if len(usable_cards) > 0:
                    options_str.append("Discard a weapon.")
                options_str.append(
                    Separator("--------------------Other--------------------"))
                options_str.append("Cancel ability.")
                question = [
                    {
                        'type': 'list',
                        'name': 'Selected',
                        'message': f'{self.character}: Select how you will use this ability:',
                        'choices': options_str,
                    },
                ]
                answer = prompt(question, style=custom_style_2)
                chosen_option = answer.get('Selected')
                if chosen_option == "Cancel ability.":
                    return(' ')

                if chosen_option == "Discard a weapon.":
                    options_str = self.create_nonblind_menu(
                        False, False, "Non-weapon")
                    question = [
                        {
                            'type': 'list',
                            'name': 'Selected',
                            'message': f'{self.character}: Please select a weapon to discard to activate Ferocious Assault:',
                            'choices': options_str,
                            'filter': lambda card: options_str.index(card)
                        },
                    ]
                    answer = prompt(question, style=custom_style_2)
                    discarded_index = answer.get('Selected')

                    # Check if hand-card
                    if discarded_index <= len(self.hand_cards.contents):
                        discarded = self.hand_cards.contents[discarded_index - 1]
                        if discarded.type == "Weapon":
                            card = self.hand_cards.contents.pop(
                                discarded_index - 1)
                            discard_deck.add_to_top(card)
                            print(
                                f"  >> Character Ability: Ferocious Assault: {self.character} has discarded {card} to damage {players[selected_index].character}!")
                        else:
                            return (' ')

                    # Check if equipment-card
                    else:
                        if discarded_index == (len(self.hand_cards.contents) + 2):
                            reachable = self.calculate_targets_in_physical_range(
                                0)
                            if selected_index in reachable:
                                card = self.equipment_weapon.pop()
                                discard_deck.add_to_top(card)
                                self.weapon_range = 1
                                print(
                                    f"  >> Character Ability: Ferocious Assault: {self.character} has discarded {card} from their weapon-slot to damage {players[selected_index].character}!")
                            else:
                                print(
                                    f"{self.character}: You can't reach that target with Ferocious Assault if you discard your weapon!")
                                return (' ')
                damage_dealt = 1

                fantasy = players[selected_index].check_fantasy(
                    damage_dealt, 0)
                if fantasy[0]:
                    selected_index = fantasy[1]

                deplete_karma = players[selected_index].check_deplete_karma(
                    damage_dealt, 0, None)
                if deplete_karma[0]:
                    damage_dealt = deplete_karma[1]

                if chosen_option == "Lose 1 unit of health.":
                    self.current_health -= 1
                    print(
                        f"  >> Character Ability: Ferocious Assault: {self.character} has lost 1 health ({self.current_health}/{self.max_health} HP remaining)!")
                    for player in players:
                        player.check_relief()
                    if self.current_health < 1:
                        if self.check_brink_of_death_loop(0, "Self") == "Break":
                            players[selected_index].current_health -= damage_dealt
                            for player in players:
                                player.check_relief()
                            if players[selected_index].current_health < 1:
                                if player.check_brink_of_death_loop(selected_index, "Self") == "Break":
                                    return(' ')

                players[selected_index].current_health -= damage_dealt
                print(
                    f"  >> Character Ability: Ferocious Assault: {self.character} has dealt 1 damage to {players[selected_index].character} ({players[selected_index].current_health}/{players[selected_index].max_health} HP remaining)!")
                for player in players:
                    player.check_relief()
                if players[selected_index].current_health < 1:
                    if player.check_brink_of_death_loop(selected_index, 0) == "Break":
                        return(' ')

                if players[selected_index].current_health > 0:
                    if fantasy[0]:
                        cards_to_draw = (
                            players[selected_index].max_health - players[selected_index].current_health)
                        print(
                            f"  >> Character Ability: Fantasy; {players[selected_index].character} draws {cards_to_draw} from the deck.")
                        players[selected_index].hand_cards.draw(
                            main_deck, cards_to_draw, False)

                    for player in players:
                        player.check_lament(0, selected_index)
                    self.check_grudge(selected_index, "Damage")
                    players[selected_index].check_bequeathed_strategy(
                        damage_dealt)
                    players[selected_index].check_delayed_wisdom()
                    players[selected_index].check_eternal_loyalty(
                        damage_dealt)
                    players[selected_index].check_exile()
                    players[selected_index].check_eye_for_an_eye(
                        0, "Activate")
                    players[selected_index].check_geminate(damage_dealt)
                    players[selected_index].check_plotting_for_power(
                        damage_dealt, mode="Reaction")
                    players[selected_index].check_retaliation(
                        0, damage_dealt)
                self.used_ferocious_assault = True

    def activate_green_salve(self):
        # "Green Salve: During your action phase, you can discard any card and allow any player to regain one unit of health. Limited to one use per turn."
        if (self.character_ability2.startswith("Green Salve:") or self.character_ability3.startswith("Green Salve:")):
            if self.used_green_salve:
                print(
                    f"{self.character}: You can only use Green Salve once per turn.")

            cards_discardable = (len(self.hand_cards.contents) + len(self.equipment_weapon) + len(
                self.equipment_armor) + len(self.equipment_offensive_horse) + len(self.equipment_defensive_horse))
            if cards_discardable > 0:
                options_str = []
                options = []
                for player_index, player in enumerate(players):
                    if player.max_health > player.current_health:
                        options_str.append(str(players[player_index]))
                        options.append(players[player_index])
                options_str.append(
                    Separator("--------------------Other--------------------"))
                options_str.append("Cancel ability.")
                if not len(options_str) > 2:
                    print(
                        f"{self.character}: You cannot use this ability as everyone is on maximum health.")
                else:
                    question = [
                        {
                            'type': 'list',
                            'name': 'Selected',
                            'message': f'{self.character}: Who would you like to heal?',
                            'choices': options_str,
                            'filter': lambda player: options_str.index(player)
                        },
                    ]
                    answer = prompt(question, style=custom_style_2)
                    player_healed_index = answer.get('Selected')
                    if options_str[player_healed_index] == "Cancel ability.":
                        return(' ')

                    card = self.discard_from_equip_or_hand()
                    discard_deck.add_to_top(card)
                    options[player_healed_index].current_health += 1
                    self.used_green_salve = True
                    print(
                        f"  >> Character Ability: Green Salve; {self.character} discarded {card} to heal {options[player_healed_index].character} by one! ({options[player_healed_index].current_health}/{options[player_healed_index].max_health} HP remaining)")
                    self.check_grudge(player_healed_index, "Heal")

    def activate_hegemony(self, mode="Activate"):
        # "Hegemony (Ruler Ability): During the action phase of any other Wu characters, they can choose to COMPETE against you; you both show a card simultaneously, and whoever has the higher value wins. If they do not win, you can take both cards used. After your awakening ability activates, you are able to refuse COMPETE effects."
        if mode == "Activate":
            emperor_index = None
            false_ruler_index = None
            if self.used_amber_sky:
                print(f"{self.character}: You can only use Hegemony once per turn.")

            else:
                for player_index, player in enumerate(players):
                    if (player.character_ability3.startswith("Hegemony (Ruler Ability):") or player.character_ability4.startswith("Hegemony (Ruler Ability):") or player.character_ability5.startswith("Hegemony (Ruler Ability):")):
                        if player.role == "Emperor":
                            emperor_index = player_index
                        else:
                            false_ruler_index = player_index

                if len(self.hand_cards.contents) < 1:
                    return (' ')

                if self.allegiance == "Wu":
                    if self.role == "Emperor":
                        if (false_ruler_index != None):
                            target = players[false_ruler_index]

                    elif self.role != "Emperor":
                        if false_ruler_index == None:
                            target = players[emperor_index]

                        elif (false_ruler_index != None) and (self.character == players[false_ruler_index].character):
                            target = players[emperor_index]

                        else:
                            options = [str(players[emperor_index]),
                                       str(players[false_ruler_index])]

                            question = [
                                {
                                    'type': 'list',
                                    'name': 'Selected',
                                    'message': f'{self.character}: Please select who you will target with Hegemony:',
                                    'choices': options,
                                },
                            ]
                            answer = prompt(question, style=custom_style_2)
                            selected = answer.get('Selected')
                            if selected == str(players[emperor_index]):
                                target = players[emperor_index]
                                if len(target.hand_cards.contents) < 1:
                                    print(
                                        f"{self.character}: you cannot COMPETE with {target.character} as they have no hand-cards!")
                                    return(' ')
                                elif target.character_ability2.startswith("Divinity (INACTIVE Ability):"):
                                    if not target.activate_hegemony("Reaction"):
                                        print(
                                            f"{target.character} has refused the COMPETITION!")
                                        return(' ')
                            else:
                                target = players[false_ruler_index]
                                if len(target.hand_cards.contents) < 1:
                                    print(
                                        f"{self.character}: you cannot COMPETE with {target.character} as they have no hand-cards!")
                                    return(' ')

                    print(
                        f"  >> Ruler Ability: Hegemony; {self.character} challenged {target.character} to COMPETE! If {target.character} wins, he keeps both cards!")
                    my_card = self.activate_compete()
                    their_card = target.activate_compete()
                    self.used_hegemony = True
                    if my_card > their_card:
                        print(
                            f"  >> Ruler Ability: Hegemony; {self.character} won the COMPETITION vs {target.character}!")
                    else:
                        print(
                            f"  >> Ruler Ability: Hegemony; {target.character} won the COMPETITION vs {self.character}, and therefore gets to keep both cards!")
                        if my_card in discard_deck.contents:
                            discard_deck.contents.remove(my_card)
                            target.hand_cards.add_to_top(my_card)
                        elif my_card in main_deck.contents:
                            discard_deck.contents.remove(my_card)
                            self.hand_cards.add_to_top(my_card)
                        if their_card in discard_deck.contents:
                            discard_deck.contents.remove(their_card)
                            target.hand_cards.add_to_top(their_card)
                        elif their_card in main_deck.contents:
                            discard_deck.contents.remove(their_card)
                            self.hand_cards.add_to_top(their_card)

        if mode == "Reaction":
            message = f"{target.character}: Accept the COMPETITION?"
            if question_yes_no(message):
                return True

    def activate_marriage(self):
        # "Marriage: During your action phase, you can choose to discard two on-hand cards and pick any male character that is not at full-health. By doing so, both the male character and yourself will recover one unit of health. Limited to one use per turn."
        if (self.character_ability1.startswith("Marriage:") or self.character_ability3.startswith("Marriage:")):
            if self.used_marriage:
                print(
                    f"{self.character}: You can only use Marriage once per turn.")

            if len(self.hand_cards.contents) > 1:
                options = [
                    Separator("------<Cannot target yourself>------")]
                for player in players[1:]:
                    if (player.gender == "Male") and (player.current_health < player.max_health):
                        options.append(str(player))
                    elif player.gender != "Male":
                        options.append(
                            Separator(str(f"--{player.character} (FEMALE - cannot be targeted)--")))
                    else:
                        options.append(
                            Separator(str(f"--{player.character} (FULL HEALTH - cannot be targeted)--")))
                options.append(
                    Separator("--------------------Other--------------------"))
                options.append("Cancel ability.")

                question = [
                    {
                        'type': 'list',
                        'name': 'Selected',
                        'message': f'{self.character}: Who would you like to marry (you both heal one)?',
                        'choices': options,
                        'filter': lambda player: options.index(player)
                    },
                ]
                answer = prompt(question, style=custom_style_2)
                player_healed_index = answer.get('Selected')

                if options[player_healed_index] == "Cancel ability.":
                    return (' ')

                options = self.create_nonblind_menu(True)
                options.append(
                    Separator("--------------------Other--------------------"))
                options.append("Cancel ability.")

                question = [
                    {
                        'type': 'list',
                        'name': 'Selected',
                        'message': f'{self.character}: Please select two hand-cards to discard?',
                        'choices': options,
                        'filter': lambda card: options.index(card)
                    },
                ]
                answer = prompt(question, style=custom_style_2)
                card1_index = answer.get('Selected')

                if options[card1_index] == "Cancel ability.":
                    return (' ')

                card1 = self.hand_cards.contents[card1_index]
                options.pop(card1_index)
                options.insert(card1_index, Separator(
                    "------" + str(card1) + "------"))

                question = [
                    {
                        'type': 'list',
                        'name': 'Selected',
                        'message': f'{self.character}: Please select one more card to discard:',
                        'choices': options,
                        'filter': lambda card: options.index(card)
                    },
                ]
                answer = prompt(question, style=custom_style_2)
                card2_index = answer.get('Selected')
                if options[card2_index] == "Cancel ability.":
                    return (' ')

                discarded1 = self.hand_cards.contents.pop(card1_index)
                discard_deck.add_to_top(discarded1)
                self.hand_cards.contents.insert(card1_index, "Placeholder")
                discarded2 = self.hand_cards.contents.pop(card2_index)
                discard_deck.add_to_top(discarded2)
                self.hand_cards.contents.remove("Placeholder")
                if self.max_health > self.current_health:
                    self.current_health += 1
                    players[player_healed_index].current_health += 1
                    print(
                        f"  >> Character Ability: Marriage; {self.character} ({self.current_health}/{self.max_health} HP remaining) has healed both themselves and {players[player_healed_index].character} ({players[player_healed_index].current_health}/{players[player_healed_index].max_health} HP remaining) by discarding two cards!")
                else:
                    players[player_healed_index].current_health += 1
                    print(
                        f"  >> Character Ability: Marriage; {self.character} has healed {players[player_healed_index].character} ({players[player_healed_index].current_health}/{players[player_healed_index].max_health} HP remaining) by discarding two cards!")
                self.check_grudge(player_healed_index, "Heal")

    def activate_reconsider(self):
        # "Reconsider: You can discard any number of cards to then draw the same number. Limited to one use per turn."
        if (self.character_ability1.startswith("Reconsider:") or self.character_ability3.startswith("Reconsider:")):
            if self.used_reconsider:
                print(
                    f"{self.character}: You can only use Reconsider once per turn!")

            else:
                cards_discardable = (len(self.hand_cards.contents) + len(self.equipment_weapon) + len(
                    self.equipment_armor) + len(self.equipment_offensive_horse) + len(self.equipment_defensive_horse))
                total_hand_cards = len(self.hand_cards.contents)
                cards_to_replace = 0
                options = self.create_nonblind_menu()
                options.append(
                    Separator("--------------------Other--------------------"))
                options.append("No more cards.")
                options.append("Cancel ability.")
                selected_cards = []
                while cards_discardable > 0:
                    question = [
                        {
                            'type': 'list',
                            'name': 'Selected',
                            'message': f'{self.character}: Please select cards to discard and redraw:',
                            'choices': options,
                            'filter': lambda card: options.index(card)
                        },
                    ]
                    answer = prompt(question, style=custom_style_2)
                    card_index = answer.get('Selected')
                    if options[card_index] == "Cancel ability.":
                        return (' ')
                    elif options[card_index] == "No more cards.":
                        if cards_to_replace == 0:
                            return (' ')
                        cards_discardable = 0
                    else:
                        selected_cards.append(card_index)
                        options.pop(card_index)
                        options.insert(card_index, (Separator(
                            "------<ALREADY SELECTED>------")))
                        cards_discardable -= 1
                        cards_to_replace += 1

                cards_to_draw = len(selected_cards)
                for card_index in selected_cards:
                    if card_index < total_hand_cards:
                        discard_deck.add_to_top(
                            self.hand_cards.contents.pop(card_index))
                        self.hand_cards.contents.insert(
                            (card_index - 1), "Placeholder")
                    if card_index == (total_hand_cards + 1):
                        discard_deck.add_to_top(
                            self.equipment_weapon.pop())
                    if card_index == (total_hand_cards + 2):
                        discard_deck.add_to_top(
                            self.equipment_armor.pop())
                    if card_index == (total_hand_cards + 3):
                        discard_deck.add_to_top(
                            self.equipment_offensive_horse.pop())
                    if card_index == (total_hand_cards + 4):
                        discard_deck.add_to_top(
                            self.equipment_defensive_horse.pop())
                self.hand_cards.draw(main_deck, cards_to_draw, False)
                for item in self.hand_cards.contents:
                    if "Placeholder" in self.hand_cards.contents:
                        self.hand_cards.contents.remove("Placeholder")
                print(
                    f"  >> Character Ability: Reconsider; {self.character} has discarded {cards_to_draw} cards and redrawn the same amount from the deck.")
                self.used_reconsider = True
                return(' ')

    def activate_rouse_the_tiger(self):
        # "Rouse the Tiger: During your action phase, you can choose to COMPETE with any character with more health than you; you both show a card simultaneously, and whoever has the higher value wins. If you win, that player will cause one unit of damage to another player within their attacking range of your choosing. If you lose, the target causes one unit of damage to you. Limited to one use per turn."
        if (self.character_ability1.startswith("Rouse the Tiger:") or self.character_ability3.startswith("Rouse the Tiger:")):
            if self.used_rouse_the_tiger:
                print(
                    f"{self.character}: You can only use Rouse the Tiger once per turn.")

            else:
                options = [Separator("------<Cannot target yourself>------")]
                for player in players[1:]:
                    if len(player.hand_cards.contents) > 0:
                        options.append(
                            str(player) + f" ({str(len(player.hand_cards.contents))} hand-cards)")
                    else:
                        options.append(
                            Separator("------" + str(player) + "------"))
                options.append(
                    Separator("--------------------Other--------------------"))
                options.append("Cancel ability.")
                question = [
                    {
                        'type': 'list',
                        'name': 'Selected',
                        'message': f'{self.character}: Please a target to COMPETE with:',
                        'choices': options,
                        'filter': lambda player: options.index(player)
                    },
                ]
                answer = prompt(question, style=custom_style_2)
                target_index = answer.get('Selected')
                if options[target_index] == "Cancel ability.":
                    return(' ')
                else:
                    my_card = self.activate_compete()
                    their_card = players[target_index].activate_compete()
                    self.used_rouse_the_tiger = True
                    if my_card > their_card:
                        print(
                            f"  >> Character Ability: Rouse the Tiger; {self.character} won vs {players[target_index].character} in their COMPETITION! {self.character} chooses who they hurt!")
                        players[target_index].check_ignore_formalities(
                            my_card, their_card)
                        options = players[target_index].create_targeting_menu(
                            "Weapon", target_index)
                        question = [
                            {
                                'type': 'list',
                                'name': 'Selected',
                                'message': f'{self.character}: Please a target for {players[target_index].character} to do 1 damage to:',
                                'choices': options,
                                'filter': lambda player: options.index(player)
                            },
                        ]
                        answer = prompt(question, style=custom_style_2)
                        selected = answer.get('Selected')

                        damage_dealt = 1
                        fantasy = players[selected].check_fantasy(
                            damage_dealt, 0)
                        if fantasy[0]:
                            selected = fantasy[1]

                        deplete_karma = self.check_deplete_karma(
                            damage_dealt, None, selected)
                        if deplete_karma[0]:
                            damage_dealt = deplete_karma[1]
                        deplete_karma = players[selected].check_deplete_karma(
                            damage_dealt, 0, None)
                        if deplete_karma[0]:
                            damage_dealt = deplete_karma[1]

                        players[selected].current_health -= damage_dealt
                        print(
                            f"  >> Character Ability: Rouse the Tiger; {players[target_index].character} did 1 damage to {players[selected].character} ({players[selected].current_health}/{players[selected].max_health} HP remaining)!")

                        for player_index, player in enumerate(players):
                            player.check_relief()
                            if player.current_health < 1:
                                if players[player_index].check_brink_of_death_loop(player_index, target_index) == "Break":
                                    return "Break"

                        if fantasy[0]:
                            cards_to_draw = (
                                players[selected].max_health - players[selected].current_health)
                            print(
                                f"  >> Character Ability: Fantasy; {players[selected].character} draws {cards_to_draw} from the deck.")
                            players[selected].hand_cards.draw(
                                main_deck, cards_to_draw, False)

                        players[target_index].check_grudge(selected, "Damage")
                        players[selected].check_bequeathed_strategy(
                            damage_dealt)
                        players[selected].check_delayed_wisdom()
                        players[selected].check_eternal_loyalty(
                            damage_dealt)
                        players[selected].check_exile()
                        if players[selected].check_eye_for_an_eye(
                                source_player_index=target_index, mode="Activate") == "Break":
                            return(' ')
                        players[selected].check_geminate(damage_dealt)
                        players[selected].check_plotting_for_power(
                            damage_dealt, mode="Reaction")
                        players[selected].check_retaliation(
                            target_index, damage_dealt)
                    else:
                        print(
                            f"  >> Character Ability: Rouse the Tiger; {players[target_index].character} won vs {self.character} in their COMPETITION! {self.character} takes 1 damage ({self.current_health}/{self.max_health} HP remaining)!")
                        players[target_index].check_ignore_formalities(
                            my_card, their_card)
                        self.current_health -= 1
                        for player in players:
                            player.check_relief()
                        if self.current_health < 1:
                            if self.check_brink_of_death_loop(0, target_index) == "Break":
                                return(' ')
                        self.check_eternal_loyalty(1)

    def activate_seed_of_animosity(self):
        # "Seed of Animosity: During your action phase, you can discard one card (on-hand or equipped) and select two male characters to undergo a DUEL with eachother. This ability cannot be prevented using NEGATE, and is limited to one use per turn."
        if (self.character_ability1.startswith("Seed of Animosity:") or self.character_ability3.startswith("Seed of Animosity:")):
            if self.used_seed_of_animosity:
                print(
                    f"{self.character}: You can only use Seed of Animosity once per turn.")

            cards_discardable = (len(self.hand_cards.contents) + len(self.equipment_weapon) + len(
                self.equipment_armor) + len(self.equipment_offensive_horse) + len(self.equipment_defensive_horse))
            targetable = []
            for player in players:
                if player.gender == "Male":
                    targetable.append(player)

            if (len(targetable) > 1) and (cards_discardable > 0):
                options_str = []
                for player in players:
                    if player.gender == "Male":
                        options_str.append(str(player))
                    else:
                        options_str.append(
                            Separator("------" + str(player) + "------"))
                options_str.append(
                    Separator("--------------------Other--------------------"))
                options_str.append("Cancel ability.")
                question = [
                    {
                        'type': 'list',
                        'name': 'Selected',
                        'message': f'{self.character}: Please select two targets to DUEL eachother:',
                        'choices': options_str,
                        'filter': lambda player: options_str.index(player)
                    },
                ]
                answer = prompt(question, style=custom_style_2)
                target1_index = answer.get('Selected')
                if options_str[target1_index] == "Cancel ability.":
                    return(' ')

                options_str.pop(target1_index)
                options_str.insert(target1_index, Separator(
                    f"--{players[target1_index].character} (Already selected)--"))

                question = [
                    {
                        'type': 'list',
                        'name': 'Selected',
                        'message': f'{self.character}: Please select a second target to DUEL {players[target1_index].character}:',
                        'choices': options_str,
                        'filter': lambda player: options_str.index(player)
                    },
                ]
                answer = prompt(question, style=custom_style_2)
                target2_index = answer.get('Selected')
                if options_str[target2_index] == "Cancel ability.":
                    return(' ')

                if players[target2_index].check_empty_city():
                    return (' ')

                card = self.discard_from_equip_or_hand()
                if card != None:
                    print(
                        f"  >> Character Ability: Seed of Animosity; {self.character} has forced {players[target1_index].character} to DUEL vs {players[target2_index].character}!")
                    self.used_seed_of_animosity = True
                    card.effect2 = "Duel"
                    players[target1_index].check_ardour(card)
                    players[target1_index].activate_duel(
                        card, target2_index, target1_index)

    def activate_sow_dissension(self, mode="Activate", given_card=None):
        # "Sow Dissension: During your action phase, you can show an on-hand card and give it to any other player. They must either choose to lose one unit of health or show their entire hand and discard all cards of the same suit as the card you showed them. Limited to one use per turn."
        if mode == "Activate":
            if (self.character_ability2.startswith("Sow Dissension:") or self.character_ability3.startswith("Sow Dissension:")):
                if self.used_sow_dissension:
                    print(
                        f"{self.character}: You can only use Sow Dissension once per turn.")

                elif len(self.hand_cards.contents) < 1:
                    print(
                        f"{self.character}: You need at least one hand-card to use Sow Dissension.")

                else:
                    options = [
                        Separator("------<Cannot target yourself>------")]
                    for player in players[1:]:
                        options.append(
                            str(player) + f" ({str(len(player.hand_cards.contents))} hand-cards)")
                    options.append(
                        Separator("--------------------Other--------------------"))
                    options.append("Cancel ability.")
                    question = [
                        {
                            'type': 'list',
                            'name': 'Selected',
                            'message': f'{self.character}: Please select a target to give a card to for Sow Dissension:',
                            'choices': options,
                            'filter': lambda player: options.index(player)
                        },
                    ]
                    answer = prompt(question, style=custom_style_2)
                    target_index = answer.get('Selected')
                    if options[target_index] == "Cancel ability.":
                        return(' ')
                    else:
                        options = self.create_nonblind_menu(True)
                        options.append(
                            Separator("--------------------Other--------------------"))
                        options.append("Cancel ability.")
                        question = [
                            {
                                'type': 'list',
                                'name': 'Selected',
                                'message': f'{self.character}: Please select a card to give to {players[target_index].character} for Sow Dissension:',
                                'choices': options,
                                'filter': lambda card: options.index(card)
                            },
                        ]
                        answer = prompt(question, style=custom_style_2)
                        discarded_index = answer.get('Selected')
                        if options[discarded_index] == "Cancel ability.":
                            return(' ')
                        else:
                            self.used_sow_dissension = True
                            given_card = self.hand_cards.contents.pop(
                                discarded_index)
                            players[target_index].hand_cards.add_to_top(
                                given_card)
                            print(
                                f"  >> Character Ability: Sow Dissension; {self.character} has given {given_card} to {players[target_index]}!")
                            players[target_index].activate_sow_dissension(
                                "Reaction", given_card)

        if mode == "Reaction":
            suit = given_card.suit
            if self.check_beauty(given_card):
                suit = "\u2665"
            question = [
                {
                    'type': 'list',
                    'name': 'Selected',
                    'message': f'{self.character}: You have been given {given_card}; lose one health; or show entire hand, and discard all cards of suit {suit}?',
                    'choices': ["Lose one health", f"Discard all {suit}"]
                },
            ]
            answer = prompt(question, style=custom_style_2)
            chosen = answer.get('Selected')
            if chosen == "Lose one health":
                self.current_health -= 1
                print(
                    f"  >> Character Ability: Sow Dissension; {self.character} kept their given card, and lost one health ({self.current_health}/{self.max_health} HP remaining)!")
                for player in players:
                    player.check_relief()
                if self.current_health < 1:
                    if self.check_brink_of_death_loop(0, "Self") == "Break":
                        return "Break"
            else:
                print(
                    f"  >> Character Ability: Sow Dissension; {self.character} has shown their entire hand, and discards all cards of suit {suit}!")
                print(f"The following cards are in {self.character}'s hand:")
                for card in self.hand_cards.contents:
                    print(card)
                same_suits = []
                if (self.character_ability2.startswith("Beauty:") or self.character_ability3.startswith("Beauty:")):
                    if self.check_beauty(given_card) or suit == "\u2665":
                        for card_index, card in enumerate(self.hand_cards.contents):
                            if (card.suit == "\u2660") or (card.suit == "\u2665"):
                                same_suits.append(card_index)
                else:
                    for card_index, card in enumerate(self.hand_cards.contents):
                        if card.suit == suit:
                            same_suits.append(card_index)

                cards_to_parse = len(self.hand_cards.contents)
                for card_index in same_suits:
                    discard_deck.add_to_top(
                        self.hand_cards.contents.pop(card_index))
                    self.hand_cards.contents.insert(card_index, "Placeholder")

                while cards_to_parse > 0:
                    if "Placeholder" in self.hand_cards.contents:
                        self.hand_cards.contents.remove("Placeholder")
                    cards_to_parse -= 1

                self.check_amassing_terrain()
                self.check_exertion(None, "Check")
                self.check_one_after_another()

    def activate_taunt(self):
        # "Taunt: During your action phase, you can pick any player that is able to reach you using an ATTACK. That player must use an ATTACK on you, or else you can discard one of their cards. Limited to one use per turn."
        if (self.character_ability1.startswith("Taunt:") or self.character_ability3.startswith("Taunt:")):
            if self.used_taunt:
                print(f"{self.character}: You can only use Taunt once per turn.")

            else:
                options = [
                    Separator("------<Cannot target yourself>------")]
                for player_index, player in enumerate(players):
                    if player_index != 0:
                        if 0 in player.calculate_targets_in_weapon_range(player_index):
                            options.append(
                                str(player) + f" ({str(len(player.hand_cards.contents))} hand-cards)")
                        else:
                            options.append(
                                Separator("------" + str(player) + "------"))
                options.append(
                    Separator("--------------------Other--------------------"))
                options.append("Cancel ability.")
                question = [
                    {
                        'type': 'list',
                        'name': 'Selected',
                        'message': f'{self.character}: Please a target to ATTACK you:',
                        'choices': options,
                        'filter': lambda player: options.index(player)
                    },
                ]
                answer = prompt(question, style=custom_style_2)
                target_index = answer.get('Selected')
                if options[target_index] == "Cancel ability.":
                    return(' ')
                print(
                    f"  >> Character Ability: Taunt; {self.character} has taunted {players[target_index].character} attack him!")
                card_played = Card(0, 'NONE', 'NONE', 'Tool',
                                   'Barbarians', 'NONE', None, 'Barbarians')
                discarded = players[target_index].use_reaction_effect(
                    "Attack", 1, card_played, target_index, 0, "Taunt")
                if type(discarded) == Card:
                    if (discarded.effect == "Attack") or (discarded.effect2 == "Attack"):
                        discarded.effect2 = "Attack"
                        players[target_index].activate_attack(
                            discarded, 0, target_index)
                else:
                    cards_discardable = (len(players[target_index].hand_cards.contents) + len(players[target_index].equipment_weapon) + len(
                        players[target_index].equipment_armor) + len(players[target_index].equipment_offensive_horse) + len(players[target_index].equipment_defensive_horse))
                    if cards_discardable > 0:
                        print(
                            f"  >> Character Ability: Taunt; {players[target_index].character} didn't ATTACK! {self.character} will discard one of their cards!")
                        options = players[target_index].create_semiblind_menu(
                        )
                        options.append(
                            Separator("--------------------Other--------------------"))
                        options.append("Cancel ability.")
                        question = [
                            {
                                'type': 'list',
                                'name': 'Selected',
                                'message': f'{self.character}: Please select a card of {players[target_index].character} discard:',
                                'choices': options,
                                'filter': lambda card: options.index(card)
                            },
                        ]
                        answer = prompt(question, style=custom_style_2)
                        discarded_index = answer.get('Selected')
                        if options[discarded_index] == "Cancel ability.":
                            self.used_taunt = True
                            return(' ')

                        # Check if hand-card
                        if discarded_index <= len(players[target_index].hand_cards.contents):
                            card_discarded = players[target_index].hand_cards.contents.pop(
                                discarded_index)
                            discard_deck.add_to_top(card_discarded)
                            print(
                                f"{self.character} has discarded {card_discarded} from {players[target_index].character}'s hand!")
                            players[target_index].check_one_after_another()

                        # Check if equipment-card
                        if discarded_index > len(players[target_index].hand_cards.contents):
                            if discarded_index == (len(players[target_index].hand_cards.contents) + 1):
                                card_discarded = players[target_index].equipment_weapon.pop(
                                )
                                discard_deck.add_to_top(card_discarded)
                                players[target_index].weapon_range = 1
                                print(
                                    f"{self.character} has discarded {card_discarded} from {players[target_index].character}'s weapon-slot!")
                                players[target_index].check_warrior_woman()

                            elif discarded_index == (len(players[target_index].hand_cards.contents) + 2):
                                card_discarded = players[target_index].equipment_armor.pop(
                                )
                                discard_deck.add_to_top(card_discarded)
                                print(
                                    f"{self.character} has discarded {card_discarded} from {players[target_index].character}'s armor-slot!")
                                players[target_index].check_warrior_woman()

                            elif discarded_index == (len(players[target_index].hand_cards.contents) + 3):
                                card_discarded = players[target_index].equipment_offensive_horse.pop(
                                )
                                discard_deck.add_to_top(card_discarded)
                                print(
                                    f"{self.character} has discarded {card_discarded} from {players[target_index].character}'s horse-slot!")
                                players[target_index].check_warrior_woman()

                            elif discarded_index == (len(players[target_index].hand_cards.contents) + 4):
                                card_discarded = players[target_index].equipment_defensive_horse.pop(
                                )
                                discard_deck.add_to_top(card_discarded)
                                print(
                                    f"{self.character} has discarded {card_discarded} from {players[target_index].character}'s horse-slot!")
                                players[target_index].check_warrior_woman()

                        if not self.amassed_terrain:
                            self.check_amassing_terrain()
                            self.amassed_terrain = True
                        if not self.used_cornering_maneuver:
                            self.check_cornering_maneuver(card_discarded)
                            self.used_cornering_maneuver = True
                self.used_taunt = True

# Activatable abilities (once-per-game)
    def activate_upheaval(self):
        # "Upheaval (Single-Use Ability): During your action phase, you can force every player, other than yourself, to use an ATTACK on another player with the least distance away. If a player is unable to do so, the player will lose one unit of health. Recipients of the ATTACK need to DEFEND to evade. This ability will proceed in succession starting from the player on your right."
        if self.character_ability2.startswith("Upheaval (Single-Use Ability):"):
            message = f"{self.character}: Confirm you want to use Upheaval? Note this can only be used ONCE PER GAME!"
            if question_yes_no(message):
                print(
                    f"  >> Character Ability: Upheaval (Single-Use Ability); {self.character} has forced every player to attack a player. If they do not, they lose 1 health!")
                for player_index, player in enumerate(players):
                    if player.character != self.character:
                        options = player.create_targeting_menu(
                            "Weapon", player_index)
                        options.append(
                            Separator("--------------------Other--------------------"))
                        options.append("Do not attack.")
                        question = [
                            {
                                'type': 'list',
                                'name': 'Selected',
                                'message': f'{player.character}: Please a select a target to ATTACK, or lose one health:',
                                'choices': options,
                                'filter': lambda player: options.index(player)
                            },
                        ]
                        answer = prompt(question, style=custom_style_2)
                        target_index = answer.get('Selected')
                        if options[target_index] == "Do not attack.":
                            player.current_health -= 1
                            print(
                                f"{player.character} chose not to ATTACK, they lose one health ({player.current_health}/{player.max_health} HP remaining)!")
                            for player in players:
                                player.check_relief()
                            if player.current_health < 1:
                                player.check_brink_of_death_loop(
                                    player_index, 0)

                        else:
                            card_played = Card(
                                0, 'NONE', 'NONE', 'Tool', 'Barbarians', 'NONE', None, 'Barbarians')
                            discarded = players[player_index].use_reaction_effect(
                                "Attack", 1, card_played, player_index, target_index, "Upheaval")
                            if type(discarded) == Card:
                                if (discarded.effect == "Attack") or (discarded.effect2 == "Attack"):
                                    discarded.effect2 = "Attack"
                                    players[player_index].activate_attack(
                                        discarded, target_index, player_index)
                            else:
                                print(
                                    f"{player.character} chose not to ATTACK, they lose one health ({player.current_health}/{player.max_health} HP remaining)!")
                                player.current_health -= 1
                                for player in players:
                                    player.check_relief()
                                if player.current_health < 1:
                                    player.check_brink_of_death_loop(
                                        player_index, 0)

                options = self.create_targeting_menu("Weapon", 0)
                options.append(
                    Separator("--------------------Other--------------------"))
                options.append("Do not attack.")
                question = [
                    {
                        'type': 'list',
                        'name': 'Selected',
                        'message': f'{self.character}: Please a select a target to ATTACK, or do nothing:',
                        'choices': options,
                        'filter': lambda player: options.index(player)
                    },
                ]
                answer = prompt(question, style=custom_style_2)
                target_index = answer.get('Selected')
                if options[target_index] == "Do not attack.":
                    pass

                else:
                    card_played = Card(
                        0, 'NONE', 'NONE', 'Tool', 'Barbarians', 'NONE', None, 'Barbarians')
                    discarded = self.use_reaction_effect(
                        "Attack", 1, card_played, 0, target_index, "Upheaval")
                    if type(discarded) == Card:
                        if (discarded.effect == "Attack") or (discarded.effect2 == "Attack"):
                            discarded.effect2 = "Attack"
                            self.activate_attack(discarded, target_index, 0)

            self.awakened = True
            self.character_ability2 == "Upheaval (INACTIVE Ability): During your action phase, you can force every player, other than yourself, to use an ATTACK on another player with the least distance away. If a player is unable to do so, the player will lose one unit of health. Recipients of the ATTACK need to DEFEND to evade. This ability will proceed in succession starting from the player on your right."
            print("Upheaval has CONCLUDED!")

# Beginning Phase
    def start_beginning_phase(self):
        print(" ")
        self.reset_once_per_turn()
        self.check_shapeshift("Turn")
        self.check_false_ruler()
        self.check_conduit()
        self.check_divinity()
        self.check_eiron()
        self.check_insurrection()
        self.check_recommence_the_legacy()
        self.check_second_wind("Beginning")
        self.check_astrology()
        self.check_goddess_luo()
        self.check_lingering_spirit()
        return self.start_judgement_phase()

# Judgement Phase
    def start_judgement_phase(self):
        print(" ")
        if self.check_flexibility("Judgement"):
            return self.start_drawing_phase()
        if self.check_godspeed("Judgement"):
            return self.start_action_phase()
        if self.check_pending_judgements() == "Break":
            return "Break"
        else:
            self.check_pending_judgements()
        if self.acedia_active and self.rations_depleted_active:
            return self.start_discard_phase()
        elif self.rations_depleted_active:
            return self.start_action_phase()
        else:
            return self.start_drawing_phase()

# Drawing Phase
    def start_drawing_phase(self):
        print(" ")
        if self.check_flexibility("Draw") or self.check_raid():
            return self.start_action_phase()
        cards_drawn = 2
        message = True
        if self.check_altruism():
            cards_drawn = 0
            message = False
        if self.check_bare_chested():
            cards_drawn -= 1
            message = False
        if self.check_dashing_hero():
            cards_drawn += 1
            message = False
        if self.check_dual_heroes():
            cards_drawn = 0
            message = False
        mediocrity = self.check_mediocrity("Draw")
        if mediocrity[0]:
            cards_drawn += check_allegiances_in_play()
            message = False
        self.hand_cards.draw(main_deck, cards_drawn, message)
        if self.acedia_active:
            return self.start_discard_phase()
        else:
            return self.start_action_phase()

# Action Phase
    def start_action_phase(self):
        self.check_persuasion()
        if self.check_decentralization():
            return self.start_end_phase()
        if self.check_flexibility("Action") or self.check_godspeed("Action"):
            return self.start_discard_phase()
        action_phase_active = True
        while action_phase_active:
            if not game_started or self.current_health < 1:
                return self.start_end_phase()
            for player in players:
                player.amassed_terrain = False
                player.used_cornering_maneuver = False
                player.used_trigrams = False
                player.weapon_popped = False
                player.armor_popped = False
                player.off_horse_popped = False
                player.def_horse_popped = False
            print(' ')
            options = []
            options.append(
                Separator("--------------------Cards--------------------"))
            playing_card_options = self.create_nonblind_menu(True)
            for card in playing_card_options:
                options.append(card)
            options.append(
                Separator("--------------------Other--------------------"))
            activatable_abilities = self.check_activatable_abilities()
            for ability in activatable_abilities:
                options.append(ability)
            if self.check_weapon_serpent_spear("Check"):
                options.append(" Weapon Ability >> Serpent Spear")
            options.append('End action-phase')

            question = [
                {
                    'type': 'list',
                    'name': 'Selected',
                    'message': f"{self.character}, it is your action-phase: Please choose an option:",
                    'choices': options,
                    'filter': lambda action: options.index(action)
                },
            ]

            answer = prompt(question, style=custom_style_2)
            action_taken_index = answer.get('Selected')

            # For ending turn
            if options[action_taken_index] == 'End action-phase':
                print(f"{self.character} has ended their action-phase.")
                action_phase_active = False

            # For using a card in-hand
            elif action_taken_index <= (len(playing_card_options) + 1):
                card_index = (action_taken_index - 1)
                card = self.hand_cards.contents[card_index]
                if (self.tools_disabled) and (card.type == "Tool"):
                    print(
                        f"  >> Character Ability: Persuasion; You cannot use tool cards this turn as you lost your COMPETITION!")
                else:
                    card.effect2 = card.effect
                    self.use_card_effect(card_index, card)
                    self.card_double = False

            # For activating an ability
            else:
                if options[action_taken_index] == " Character Ability >> Alliance":
                    self.activate_alliance()
                if options[action_taken_index] == " Character Ability >> Benevolence":
                    self.activate_benevolence()
                if options[action_taken_index] == " Character Ability >> Blitz":
                    self.activate_blitz()
                if options[action_taken_index] == " Character Ability >> Blockade":
                    self.activate_blockade()
                if options[action_taken_index] == " Character Ability >> Blunt Advice":
                    self.activate_blunt_advice()
                if options[action_taken_index] == " Character Ability >> Brilliant Scheme":
                    self.activate_brilliant_scheme("Activate")
                if options[action_taken_index] == " Character Ability >> Dazzle":
                    self.activate_dazzle()
                if options[action_taken_index] == " Character Ability >> Dragon Heart":
                    self.activate_dragon_heart("Activate")
                if options[action_taken_index] == " Character Ability >> Drown in Wine":
                    self.activate_drown_in_wine("Activate")
                if options[action_taken_index] == " Character Ability >> Dual Heroes":
                    self.check_dual_heroes("Activate")
                if options[action_taken_index] == " Character Ability >> Ferocious Assault":
                    self.activate_ferocious_assault()
                if options[action_taken_index] == " Character Ability >> Green Salve":
                    self.activate_green_salve()
                if options[action_taken_index] == " Character Ability >> Heaven's Justice":
                    self.activate_heavens_justice()
                if options[action_taken_index] == " Character Ability >> Horsebow":
                    self.activate_horsebow("Activate")
                if options[action_taken_index] == " Character Ability >> Marriage":
                    self.activate_marriage()
                if options[action_taken_index] == " Character Ability >> National Colours":
                    self.activate_national_colours()
                if options[action_taken_index] == " Character Ability >> Random Strike":
                    self.activate_random_strike()
                if options[action_taken_index] == " Character Ability >> Reconsider":
                    self.activate_reconsider()
                if options[action_taken_index] == " Character Ability >> Rejection":
                    self.activate_rejection()
                if options[action_taken_index] == " Character Ability >> Rouse the Tiger":
                    self.activate_rouse_the_tiger()
                if options[action_taken_index] == " Character Ability >> Seed of Animosity":
                    self.activate_seed_of_animosity()
                if options[action_taken_index] == " Character Ability >> Sow Dissension":
                    self.activate_sow_dissension()
                if options[action_taken_index] == " Character Ability >> Surprise":
                    self.activate_surprise()
                if options[action_taken_index] == " Character Ability >> Taunt":
                    self.activate_taunt()
                if options[action_taken_index] == " Character Ability >> Trojan Flesh":
                    self.activate_trojan_flesh()
                if options[action_taken_index] == " Character Ability >> Upheaval (Single-Use Ability)":
                    self.activate_upheaval()
                if options[action_taken_index] == " Character Ability >> Warrior Saint":
                    self.activate_warrior_saint("Activate")
                if options[action_taken_index] == " Ruler Ability >> Amber Sky":
                    self.activate_amber_sky()
                if options[action_taken_index] == " Ruler Ability >> Hegemony":
                    self.activate_hegemony()
                if options[action_taken_index] == " Ruler Ability >> Rouse":
                    self.activate_rouse("Activate")
                if options[action_taken_index] == " Weapon Ability >> Serpent Spear":
                    cards_list = self.check_weapon_serpent_spear("Activate")
                    if cards_list[0] != None:
                        if cards_list[0] == "Black Attack":
                            cards_list[2].effect2 = "Black Attack"
                            cards_list[4].effect2 = "Black Attack"
                            self.use_card_effect(
                                cards_list[1], cards_list[2], cards_list[3], cards_list[4])
                        elif cards_list[0] == "Red Attack":
                            cards_list[2].effect2 = "Red Attack"
                            cards_list[4].effect2 = "Red Attack"
                            self.use_card_effect(
                                cards_list[1], cards_list[2], cards_list[3], cards_list[4])
                        else:
                            cards_list[2].effect2 = "Colourless Attack"
                            cards_list[4].effect2 = "Colourless Attack"
                            self.use_card_effect(
                                cards_list[1], cards_list[2], cards_list[3], cards_list[4])
        if self.check_restraint():
            return self.start_end_phase()
        return self.start_discard_phase()

# Discard Phase
    def start_discard_phase(self):
        print(" ")
        if self.check_flexibility("Discard"):
            return self.start_end_phase()
        difference = 0
        mediocrity = self.check_mediocrity("Discard")
        if mediocrity[0]:
            difference = mediocrity[1]
        else:
            # Check for characters that have increased hand-card limits at end of their turn
            limit_increase1 = self.check_bloodline()
            limit_increase2 = self.check_plotting_for_power(0, "Discard")
            limit_increase3 = self.check_refusing_death("Discard")
            limit_increase = limit_increase1 + limit_increase2 + limit_increase3

            # Discard down to your current health level
            if len(self.hand_cards.list_cards()) > (self.current_health + limit_increase):
                difference = (len(self.hand_cards.list_cards()) -
                              (self.current_health + limit_increase))
                self.hand_cards.discard_from_hand(difference)
        for player in players[1:]:
            player.check_stabilization(difference)
        return self.start_end_phase()

# End Phase
    def start_end_phase(self):
        print(" ")
        self.check_disintegrate()
        self.check_eclipse_the_moon()
        self.check_second_wind("End")
        self.check_shapeshift("Turn")
        self.reset_once_per_turn()


# Game-Setup
# Game-Setup
# Game-Setup
game_started = False
[number_of_players_output, roles_dictionary,
    roles_list, picking_format_output] = setup_loop()
random.shuffle(roles_list)
roles_list.append(roles_list.pop(roles_list.index("Emperor")))
players = generate_players()
players_at_start = players
[shu_emperor_cards, wei_emperor_cards, wu_emperor_cards, hero_emperor_cards, shu_character_cards, wei_character_cards, wu_character_cards,
    hero_character_cards, all_emperor_cards, all_character_cards, character_card_discard_pile] = generate_character_decks()
player_assignment()


# Game-state
# Card handling
main_deck = Deck(all_cards)
discard_deck = Deck([])
main_deck.shuffle()
print("The deck has been shuffled!")
for player in players:
    player.hand_cards.draw(main_deck, 4, False)
    player.check_geminate(2, False)
    player.check_shapeshift()
    player.check_false_ruler()
print("All players have been dealt 4 cards!")
game_started = True

while game_started:
    check_win_conditions()
    # Check if missing next turn
    if players[0].flipped_char_card:
        print(
            f"{players[0].character} misses this turn as their character card was flipped down! It has now been flipped up.")
        players[0].flipped_char_card = False
    else:
        players[0].start_beginning_phase()
    # If alive at end of turn
    if players[0].current_health > 0:
        players.append(players.pop(0))
    else:
        # If dead at end of turn
        players.pop(0)
