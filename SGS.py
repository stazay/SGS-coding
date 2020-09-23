"""
SanGuoSha Coding by Saba Tazayoni
Started: 21/07/2020
Current Version: 22/09/2020
"""

from __future__ import print_function, unicode_literals
import random
from pprint import pprint
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
        for role in range(0, roles_dictionary[key]):
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
def get_playing_card_options(self):
    options = []
    for card in self.list_cards():
        options.append(card)
    return options


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
              "Devolution: You can skip your action phase. If you do so, you can discard an on-hand card at the end of your turn, in order to allow another player to take a turn directly after yours.",
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
              "Exalt (Ruler Ability): Whenever any Wei character (other than yourself) makes a judgement, if the judgement card that takes effect is either CLUBS or SPADES, that character can choose to let you draw one card from the deck.")
]

wu_emperors = [
    Character("Sun Ce", "Wu", 4, "Male",
              "Ardour: Whenever you use or become the target of any DUEL or red-suited ATTACK cards, you can draw a card.",
              "Divinity (Awakening Ability): If, at the start of your turn, your health is one unit, you must reduce your maximum health by one. After which you permanently gain the abilities 'Dashing Hero' and 'Lingering Spirit'.",
              "Dashing Hero (INACTIVE Ability): Draw an extra card at the start of your turn.",
              "Lingering Spirit (INACTIVE Ability): If your health is not at maximum in your drawing phase, you can force any player to draw X cards, and then discard 1 card, or draw 1 card, and discard X cards. X is the amount of health you have missing from your maximum.",
              "Hegemony (Ruler Ability): During the action phase of any other Wu characters, they can choose to COMPETE against you; you both show a card simultaneously, and whoever has the higher value wins. If they do not win, you can take both cards used. After your awakening ability activates, you are able to refuse COMPETE effects."),
    Character("Sun Quan", "Wu", 4, "Male",
              "Reconsider: Once per turn, you can discard any number of cards to then draw the same number.",
              "Rescued (Ruler Ability): Whenever another member of Wu uses a PEACH to save you from the brink of death, it provides you with two units of health.")
]

hero_emperors = [
    Character("Dong Zhuo", "Heroes", 8, "Male",
              "Drown in Wine: You can use any of your on-hand cards with suit of SPADES as WINE. WINE can be used on yourself the brink of death to restore one unit of health, or to increase the damage of their next ATTACK by one damage.",
              "Garden of Lust: Whenever you use an ATTACK on a female character or vice-versa, the targeted character needs to use two DEFEND cards to successfully evade the attack.",
              "Disintegrate: At the end of every turn, if your health is not the least or among the least, you must either lose one unit of health, or reduce your maximum health by one unit.",
              "Tyrant (Ruler Ability): Whenever another Hero character causes damage to any other player, you can flip a judgement card. If the judgement card is of the suit SPADES, you can regain one unit of health."),
    Character("Yuan Shao", "Heroes", 4, "Male",
              "Random Strike: You can use any two hand-cards which have the same suit as RAIN OF ARROWS.",
              "Bloodline (Ruler Ability): Your maximum hand-limit is increased by two for each other Hero character still alive."),
    Character("Zhang Jiao", "Heroes", 3, "Male",
              "Lightning Strike: Whenever you use a DEFEND card, you can target any other player to make a judgement. If the judgement card is of the suit SPADES, the target player suffers two points of lightning damage.",
              "Dark Sorcery: You can exchange the judgement card of any player before it takes effect, with any of your CLUBS or SPADES, either on-hand or equipped.",
              "Amber Sky (Ruler Ability): All Hero characters can give you a DEFEND or LIGHTNING card during their individual turns.")
]

# Shu Characters
shu_characters = [
    Character("Fa Zheng", "Shu", 3, "Male",
              "Grudge: Whenever someone damages you, they must give you a card of suit HEARTS from their hand. If they do not, they lose one unit of health. Whenever another player heals you, they draw a card from the deck.",
              "Dazzle: During your action phase, you can give a card with suit of HEARTS to another player. Then, you can take any of their cards (on-hand or equipped), and give it to any character."),
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
              "Backstab: Whenever you use an ATTACK to cause damage to a player within your physical range, you can flip a judgement card. If the judgement is not HEARTS, no damage is caused, and instead you cause the target to reduce their maximum health by 1."),
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
              "Amassing Terrain: Every instance that you use or lose cards outside of your turn, you can flip a judgement card. If the judgement is not HEARTS, you can place the judgement card (referred to as a TERRAIN) atop your character card. For every TERRAIN that you gain, your physical distance to other players is considered -1.",
              "Conduit (Awakening Ability): At the beginning of your turn, if you have three or more TERRAINS, you must reduce your maximum health by one unit. You then permanently gain the ability 'Blitz'.",
              "Blitz (INACTIVE Ability): In your action phase, you can use any of your TERRAINS as STEAL."),
    Character("Dian Wei", "Wei", 4, "Male",
              "Ferocious Assault: During your action phase, you can inflict one unit of damage to any player within your attacking range by either; reducing one unit of your own health, or discarding one weapon card (on-hand or equipped)."),
    Character("Guo Jia", "Wei", 3, "Male",
              "Envy of Heaven: You can obtain any judgement card that you flip over.",
              "Bequeathed Strategy: For every one unit of damage you recieve, you can draw two cards from the deck. You can then choose to give away one, two or none of these cards to any player."),
    Character("Sima Yi", "Wei", 3, "Male",
              "Retaliation: For every one unit of damage you recieve, you can take one card (whether on-hand or equipped) from the player who was the source of that damage.",
              "Devil: After any judgement has been flipped over, you can immediately discard one of your on-hand or equipped cards to replace the judgement card."),
    Character("Xiahou Dun", "Wei", 4, "Male",
              "Eye for an Eye: For every instance that you suffer damage, you can flip a judgement card. If the judgement is not HEARTS, the character that damaged you must choose between the following options; lose one unit of health, or discard any two on-hand cards."),
    Character("Xiahou Yuan", "Wei", 4, "Male",
              "Godspeed: You can do either or both of the following options; skip your judgement and drawing phases, or skip your action phase and discard one equipment card. If you do either, it is the equivalent of using an ATTACK with no distance limitations."),
    Character("Xu Chu", "Wei", 4, "Male",
              "Bare-chested: You can choose to draw one less card in your drawing phase. If you do so, any ATTACK or DUEL cards that you you play in your action phase will deal an additional unit of damage."),
    Character("Xu Huang", "Wei", 4, "Male",
              "Blockade: During your action phase, you can choose to use any of your basic or equipment cards with suit CLUBS or SPADES as RATIONS DEPLETED with a physical range of -1 in distance calculations. RATIONS DEPLETED acts as a time-delay tool card, in which a player will have to flip a judgement at the start of their turn. If the judgement is any suit other than CLUBS, the target fails the judgement and must skip their drawing phase."),
    Character("Xun Yu", "Wei", 3, "Male",
              "Rouse The Tiger: Once per turn, during your action phase, you can choose to COMPETE with any character with more health than you; you both show a card simultaneously, and whoever has the higher value wins. If you win, that player will cause one unit of damage to another player within their attacking range of your choosing. If you lose, the target causes one unit of damage to you.",
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
              "National Colours: During your action phase, you can use any of your cards (on-hand or equipped) with a DIAMONDS suit as ACEDIA.",
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
    Character("Sun Shang Xiang", "Wu", 3, "Female",
              "Marriage: During your action phase, you can choose to discard two on-hand cards and pick any male character that is not at full-health. By doing so, both the male character and yourself will recover one unit of health. Limited to one use per turn.",
              "Warrior Woman: Whenever any equipped card is removed from your equipment, you can immediately draw two cards from the deck."),
    Character("Tai Shi Ci", "Wu", 4, "Male",
              "Heaven's Justice: Once per turn, you can COMPETE with any player; you both show a card simultaneously, and whoever has the higher value wins. If you win, you can use an additional ATTACK, and each ATTACK has unlimited range and can target an additional player. If you lose, you cannot attack this turn."),
    Character("Xiao Qiao", "Wu", 3, "Female",
              "Fantasy: Whenever you recieve damage, you can choose to pass the damage onto any other player by discarding an on-hand card that has the suit HEARTS. The victim that recieves the damage gets to draw X number of cards from the deck, X being the amount of health missing from the maximum level after damage.",
              "Beauty: All of your SPADES will be regarded as HEARTS."),
    Character("Zhang Zhao and Zhang Hong", "Wu", 3, "Male",
              "Blunt Advice: During your action phase, you can put an on-hand equipment card in the equipment area of another character (you cannot replace something already equipped). If you do so, you draw a card.",
              "Stabilization: At the end of other players' discard phase, you can return one discarded card to that player. If you do so, you can take all of the other cards discarded in this phase as your own on-hand cards."),
    Character("Zhou Tai", "Wu", 4, "Male",
              "Refusing Death: Whenever you are brought to the brink of death, you take a card from the deck and place it atop your character card. If the number on the card is different to all of the others, you return with one health. If the number matches another card, you discard this card and continue to be on the brink of death. When you have cards atop your character card, your hand limit becomes the number of cards atop your character card.",
              "Exertion: Whenever another player has cards taken or discarded by another player, you can lose one health to let that player draw two cards."),
    Character("Zhou Yu", "Wu", 3, "Male",
              "Dashing Hero: Draw an extra card at the start of your turn.",
              "Sow Dissension: During your action phase, you can show an on-hand card and give it to any other player. They must either choose to lose one unit of health or show their entire hand and discard all cards of the same suit as the card you showed them.")
]

# Hero Characters
hero_characters = [
    Character("Cai Wen Ji", "Heroes", 3, "Female",
              "Lament: Whenever any player is damaged by an ATTACK, you can discard any card, on-hand or equipped. The victim must then flip a judgement. If SPADES, the attacker flips their character card. If HEARTS, the victim regains one health. If CLUBS, the attacker discards two cards. If DIAMONDS, the victim draws two cards.",
              "Heartbreak: Whenever a player kills you, they lose all of their character abilities for the rest of the game."),
    Character("Chen Gong", "Heroes", 3, "Male",
              "Brilliant Scheme: Once per turn, you can give another player an ATTACK or equipment card. The player can then choose to draw one card or allow you to choose one character within their attacking range. This character is ATTACKed by the player that recieved the card.",
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
            return f"[{self.effect} <:{self.weapon_range}:> - {self.val} of {self.suit}]"
        else:
            return f"[{self.effect} - {self.val} of {self.suit}]"

    def __repr__(self):
        if self.type == "Weapon":
            return f"{self.effect} <:{self.weapon_range}:> - {self.val} of {self.suit}"
        else:
            return f"[{self.effect} - {self.val} of {self.suit}]"

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

    def check_if_empty(self, main_deck, discard_deck):
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
            main_deck.check_if_empty(main_deck, discard_deck)
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
        options_str = get_playing_card_options(self)
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
                main_deck.check_if_empty(main_deck, discard_deck)
            card = deck_drawn.remove_from_top()
            self.add_to_top(card)
            num -= 1


# 108 Cards in the Deck;
all_cards = [
    Card(1, 'Ace', 'Spades', 'Tool', 'Duel', 'You can target any player for a duel with this card. If the target does not play an ATTACK, they are damaged. If they do ATTACK, then you must play one in response or take damage. Whoever does not attack, takes damage.'),
    Card(1, 'Ace', 'Spades', 'Delay-Tool', 'Lightning', 'You can place this Delay-Tool on yourself. In your next turn, you will perform a judgement for this card; if it is between two and nine of spades (inclusively), you recieve three units of lightning damage. If not, LIGHTNING passes to the next player.'),
    Card(2, 'Two', 'Spades', 'Weapon', 'Frost Blade',
         'When equipped, and an ATTACK hits a target, the wielder has a choice; they can either damage the target or force them to discard two cards.', 2),
    Card(2, 'Two', 'Spades', 'Weapon', 'Gender-Swords',
         'When equipped, and playing an ATTACK on the target, the wielder can force the target to make a choice; to either discard a hand-card or allow the wielder to draw one from the deck.', 2),
    Card(2, 'Two', 'Spades', 'Armor', 'Eight-Trigrams',
         'When equipped: whenever a DEFEND is needed, the wearer can perform a judgement. If it is red, the DEFEND is considered to be played.'),
    Card(3, 'Three', 'Spades', 'Tool', 'Dismantle',
         'You can target any player and discard one of their cards, on-hand or equipped.'),
    Card(3, 'Three', 'Spades', 'Tool', 'Steal',
         'You can use this card on a player within physical range to take a card from them (on-hand or equipped) and add it to your hand.'),
    Card(4, 'Four', 'Spades', 'Tool', 'Dismantle',
         'You can target any player and discard one of their cards, on-hand or equipped.'),
    Card(4, 'Four', 'Spades', 'Tool', 'Steal',
         'You can use this card on a player within physical range to take a card from them (on-hand or equipped) and add it to your hand.'),
    Card(5, 'Five', 'Spades', '+1 Horse', 'Shadow; +1 Horse',
         'When equipped, this horse places you further away from players in distance calculations by +1.'),
    Card(5, 'Five', 'Spades', 'Weapon', 'Green Dragon Halberd',
         "When equipped, and the target of the wielder's ATTACK is DEFENDED against, the wielder may ATTACK again.", 3),
    Card(6, 'Six', 'Spades', 'Delay-Tool', 'Acedia',
         'You can place Delay-Tool on any other player. The target must perform a judgement for this card. If it is not HEARTS, they forfeit their action-phase.'),
    Card(6, 'Six', 'Spades', 'Weapon', 'Black Pommel',
         'When equipped, the wielder ignores any armor of their targets.', 2),
    Card(7, 'Seven', 'Spades', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(7, 'Seven', 'Spades', 'Tool', 'Barbarians',
         'All other players must play an ATTACK or else suffer one damage.'),
    Card(8, 'Eight', 'Spades', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(8, 'Eight', 'Spades', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(9, 'Nine', 'Spades', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(9, 'Nine', 'Spades', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(10, 'Ten', 'Spades', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(10, 'Ten', 'Spades', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(11, 'Jack', 'Spades', 'Tool', 'Negate',
         'Any player may play this card in response to a tool card being played. This prevents that tool card from working.'),
    Card(11, 'Jack', 'Spades', 'Tool', 'Steal',
         'You can use this card on a player within physical range to take a card from them (on-hand or equipped) and add it to your hand.'),
    Card(12, 'Queen', 'Spades', 'Tool', 'Dismantle',
         'You can target any player and discard one of their cards, on-hand or equipped.'),
    Card(12, 'Queen', 'Spades', 'Weapon', 'Serpent Spear',
         'When equipped, the wielder can discard any two cards to behave as an ATTACK.', 3),
    Card(13, 'King', 'Spades', 'Tool', 'Barbarians',
         'All other players must play an ATTACK or else suffer one damage.'),
    Card(13, 'King', 'Spades', '-1 Horse', 'Da Yuan; -1 Horse',
         'When equipped, this horse places other players closer to you in distance calculations by -1.'),
    Card(1, 'Ace', 'Hearts', 'Tool', 'Peach Gardens',
         'All damaged players will be healed by one health.'),
    Card(1, 'Ace', 'Hearts', 'Tool', 'Rain of Arrows',
         'All other players must play a DEFEND or else suffer one damage.'),
    Card(2, 'Two', 'Hearts', 'Basic', 'Defend',
         'When targeted by an ATTACK, you can play this card to avoid taking damage.'),
    Card(2, 'Two', 'Hearts', 'Basic', 'Defend',
         'When targeted by an ATTACK, you can play this card to avoid taking damage.'),
    Card(3, 'Three', 'Hearts', 'Basic', 'Peach',
         'During your turn, you can use this card to recover one unit of missing health. Additionally, whenever a player is on the brink of death, any player can use a PEACH to make them recover one unit of health.'),
    Card(3, 'Three', 'Hearts', 'Tool', 'Granary',
         'You can use this card to flip over one card for every living player. Then, starting with the user of this card, each player will select a card and add it to their hand.'),
    Card(4, 'Four', 'Hearts', 'Basic', 'Peach', 'During your turn, you can use this card to recover one unit of missing health. Additionally, whenever a player is on the brink of death, any player can use a PEACH to make them recover one unit of health.'),
    Card(4, 'Four', 'Hearts', 'Tool', 'Granary',
         'You can use this card to flip over one card for every living player. Then, starting with the user of this card, each player will select a card and add it to their hand.'),
    Card(5, 'Five', 'Hearts', '-1 Horse', 'Red Hare; -1 Horse',
         'When equipped, this horse places other players closer to you in distance calculations by -1.'),
    Card(5, 'Five', 'Hearts', 'Weapon', "Huang's Longbow",
         'When equipped, if the wielder successfully damages another player with an ATTACK, they can discard any horse of the target player.', 5),
    Card(6, 'Six', 'Hearts', 'Basic', 'Peach', 'During your turn, you can use this card to recover one unit of missing health. Additionally, whenever a player is on the brink of death, any player can use a PEACH to make them recover one unit of health.'),
    Card(6, 'Six', 'Hearts', 'Delay-Tool', 'Acedia',
         'You can place Delay-Tool on any other player. The target must perform a judgement for this card. If it is not HEARTS, they forfeit their action-phase.'),
    Card(7, 'Seven', 'Hearts', 'Basic', 'Peach',
         'During your turn, you can use this card to recover one unit of missing health. Additionally, whenever a player is on the brink of death, any player can use a PEACH to make them recover one unit of health.'),
    Card(7, 'Seven', 'Hearts', 'Tool', 'Greed',
         'Use this card to draw two cards from the deck.'),
    Card(8, 'Eight', 'Hearts', 'Basic', 'Peach',
         'During your turn, you can use this card to recover one unit of missing health. Additionally, whenever a player is on the brink of death, any player can use a PEACH to make them recover one unit of health.'),
    Card(8, 'Eight', 'Hearts', 'Tool', 'Greed',
         'Use this card to draw two cards from the deck.'),
    Card(9, 'Nine', 'Hearts', 'Basic', 'Peach', 'During your turn, you can use this card to recover one unit of missing health. Additionally, whenever a player is on the brink of death, any player can use a PEACH to make them recover one unit of health.'),
    Card(9, 'Nine', 'Hearts', 'Tool', 'Greed',
         'Use this card to draw two cards from the deck.'),
    Card(10, 'Ten', 'Hearts', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(10, 'Ten', 'Hearts', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(11, 'Jack', 'Hearts', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(11, 'Jack', 'Hearts', 'Tool', 'Greed',
         'Use this card to draw two cards from the deck.'),
    Card(12, 'Queen', 'Hearts', 'Basic', 'Peach',
         'During your turn, you can use this card to recover one unit of missing health. Additionally, whenever a player is on the brink of death, any player can use a PEACH to make them recover one unit of health.'),
    Card(12, 'Queen', 'Hearts', 'Tool', 'Dismantle',
         'You can target any player and discard one of their cards, on-hand or equipped.'),
    Card(12, 'Queen', 'Hearts', 'Delay-Tool', 'Lightning',
         'You can place this Delay-Tool on yourself. In your next turn, you will perform a judgement for this card; if it is between two and nine of spades (inclusively), you recieve three units of lightning damage. If not, the Lightning passes to the next player.'),
    Card(13, 'King', 'Hearts', 'Basic', 'Defend',
         'When targeted by an ATTACK, you can play this card to avoid taking damage.'),
    Card(13, 'King', 'Hearts', '+1 Horse', 'Storm Runner; +1 Horse',
         'When equipped, this horse places you further away from players in distance calculations by +1.'),
    Card(1, 'Ace', 'Clubs', 'Tool', 'Duel', 'You can target any player for a duel with this card. If the target does not play an ATTACK, they are damaged. If they do ATTACK, then you must play one in response or take damage. Whoever does not attack, takes damage.'),
    Card(1, 'Ace', 'Clubs', 'Weapon', 'Zhuge Crossbow',
         'When equipped, the wielder has no limit to the number of ATTACKs they can play in their turn.', 1),
    Card(2, 'Two', 'Clubs', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(2, 'Two', 'Clubs', 'Armor', 'Black Shield',
         'When equipped, black ATTACK cards cannot affect the wearer.'),
    Card(2, 'Two', 'Clubs', 'Armor', 'Eight-Trigrams',
         'When equipped: whenever a DEFEND is needed, the wearer can perform a judgement. If it is red, the DEFEND is considered to be played.'),
    Card(3, 'Three', 'Clubs', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(3, 'Three', 'Clubs', 'Tool', 'Dismantle',
         'You can target any player and discard one of their cards, on-hand or equipped.'),
    Card(4, 'Four', 'Clubs', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(4, 'Four', 'Clubs', 'Tool', 'Dismantle',
         'You can target any player and discard one of their cards, on-hand or equipped.'),
    Card(5, 'Five', 'Clubs', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(5, 'Five', 'Clubs', '+1 Horse', 'Di Lu; +1 Horse',
         'When equipped, this horse places you further away from players in distance calculations by +1.'),
    Card(6, 'Six', 'Clubs', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(6, 'Six', 'Clubs', 'Delay-Tool', 'Acedia',
         'You can place Delay-Tool on any other player. The target must perform a judgement for this card. If it is not HEARTS, they forfeit their action-phase.'),
    Card(7, 'Seven', 'Clubs', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(7, 'Seven', 'Clubs', 'Tool', 'Barbarians',
         'All other players must play an ATTACK or else suffer one damage.'),
    Card(8, 'Eight', 'Clubs', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(8, 'Eight', 'Clubs', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(9, 'Nine', 'Clubs', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(9, 'Nine', 'Clubs', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(10, 'Ten', 'Clubs', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(10, 'Ten', 'Clubs', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(11, 'Jack', 'Clubs', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(11, 'Jack', 'Clubs', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(12, 'Queen', 'Clubs', 'Tool', 'Coerce', 'Use this card to target any other player that possesses a weapon. Afterwards, you can then select any target within their attacking range. Your target can then ATTACK the victim. If they do not, you will take their weapon and add it to your hand.'),
    Card(12, 'Queen', 'Clubs', 'Tool', 'Negate',
         'Any player may play this card in response to a tool card being played. This prevents that tool card from working.'),
    Card(13, 'King', 'Clubs', 'Tool', 'Coerce', 'Use this card to target any other player that possesses a weapon. Afterwards, you can then select any target within their attacking range. Your target can then ATTACK the victim. If they do not, you will take their weapon and add it to your hand.'),
    Card(13, 'King', 'Clubs', 'Tool', 'Negate',
         'Any player may play this card in response to a tool card being played. This prevents that tool card from working.'),
    Card(1, 'Ace', 'Diamonds', 'Tool', 'Duel', 'You can target any player for a duel with this card. If the target does not play an ATTACK, they are damaged. If they do ATTACK, then you must play one in response or take damage. Whoever does not attack, takes damage.'),
    Card(1, 'Ace', 'Diamonds', 'Weapon', 'Zhuge Crossbow',
         'When equipped, the wielder has no limit to the number of ATTACKs they can play in their turn.', 1),
    Card(2, 'Two', 'Diamonds', 'Basic', 'Defend',
         'When targeted by an ATTACK, you can play this card to avoid taking damage.'),
    Card(2, 'Two', 'Diamonds', 'Basic', 'Defend',
         'When targeted by an ATTACK, you can play this card to avoid taking damage.'),
    Card(3, 'Three', 'Diamonds', 'Basic', 'Defend',
         'When targeted by an ATTACK, you can play this card to avoid taking damage.'),
    Card(3, 'Three', 'Diamonds', 'Tool', 'Steal',
         'You can use this card on a player within physical range to take a card from them (on-hand or equipped) and add it to your hand.'),
    Card(4, 'Four', 'Diamonds', 'Basic', 'Defend',
         'When targeted by an ATTACK, you can play this card to avoid taking damage.'),
    Card(4, 'Four', 'Diamonds', 'Tool', 'Steal',
         'You can use this card on a player within physical range to take a card from them (on-hand or equipped) and add it to your hand.'),
    Card(5, 'Five', 'Diamonds', 'Basic', 'Defend',
         'When targeted by an ATTACK, you can play this card to avoid taking damage.'),
    Card(5, 'Five', 'Diamonds', 'Weapon', 'Axe',
         'When equipped, and the target of the wielder DEFENDs against the ATTACK of the wielder, they can discard two cards to force the damage.', 3),
    Card(6, 'Six', 'Diamonds', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(6, 'Six', 'Diamonds', 'Basic', 'Defend',
         'When targeted by an ATTACK, you can play this card to avoid taking damage.'),
    Card(7, 'Seven', 'Diamonds', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(7, 'Seven', 'Diamonds', 'Basic', 'Defend',
         'When targeted by an ATTACK, you can play this card to avoid taking damage.'),
    Card(8, 'Eight', 'Diamonds', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(8, 'Eight', 'Diamonds', 'Basic', 'Defend',
         'When targeted by an ATTACK, you can play this card to avoid taking damage.'),
    Card(9, 'Nine', 'Diamonds', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(9, 'Nine', 'Diamonds', 'Basic', 'Defend',
         'When targeted by an ATTACK, you can play this card to avoid taking damage.'),
    Card(10, 'Ten', 'Diamonds', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(10, 'Ten', 'Diamonds', 'Basic', 'Defend',
         'When targeted by an ATTACK, you can play this card to avoid taking damage.'),
    Card(11, 'Jack', 'Diamonds', 'Basic', 'Defend',
         'When targeted by an ATTACK, you can play this card to avoid taking damage.'),
    Card(11, 'Jack', 'Diamonds', 'Basic', 'Defend',
         'When targeted by an ATTACK, you can play this card to avoid taking damage.'),
    Card(12, 'Queen', 'Diamonds', 'Basic', 'Peach',
         'During your turn, you can use this card to recover one unit of missing health. Additionally, whenever a player is on the brink of death, any player can use a PEACH to make them recover one unit of health.'),
    Card(12, 'Queen', 'Diamonds', 'Tool', 'Negate',
         'Any player may play this card in response to a tool card being played. This prevents that tool card from working.'),
    Card(12, 'Queen', 'Diamonds', 'Weapon', 'Sky Scorcher Halberd',
         'When equipped and using the last on-hand card to ATTACK, the ATTACK can target an additional two players.', 4),
    Card(13, 'King', 'Diamonds', 'Basic', 'Attack',
         'Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.'),
    Card(13, 'King', 'Diamonds', '-1 Horse', 'Hua Liu; -1 Horse',
         'When equipped, this horse places other players closer to you in distance calculations by -1.')
]


# A class for individual players and their stats in the game
class Player(Character):
    def __init__(self, role, weapon_range=1, attacks_this_turn=0, max_health=1, current_health=1, hand_cards=[], equipment_armor=[], equipment_weapon=[], equipment_defensive_horse=[], equipment_offensive_horse=[], pending_judgements=[]):
        self.role = role
        self.weapon_range = weapon_range
        self.attacks_this_turn = attacks_this_turn
        self.current_health = current_health
        self.max_health = max_health
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
        self.rites = []
        self.terrains = []
        self.previous_turn_health = None
        self.used_bare_chested = False
        self.wine_active = False
        self.flipped_char_card = False

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
        question = [
            {
                'type': 'list',
                'name': 'Selected',
                'message': 'Please confirm you want to play with the above character.',
                'choices': ['Yes', 'No'],
            },
        ]

        answer = prompt(question, style=custom_style_2)
        if answer.get('Selected') == 'Yes':
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
        question = [
            {
                'type': 'list',
                'name': 'Selected',
                'message': 'Please confirm you want to BAN the above character.',
                'choices':  ['Yes', 'No'],
            },
        ]

        answer = prompt(question, style=custom_style_2)
        if answer.get('Selected') == 'Yes':
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
        question = [
            {
                'type': 'list',
                'name': 'Selected',
                'message': 'Please confirm you want to play with the above character.',
                'choices':  ['Yes', 'No'],
            },
        ]

        answer = prompt(question, style=custom_style_2)
        if answer.get('Selected') == 'Yes':
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
        question = [
            {
                'type': 'list',
                'name': 'Selected',
                'message': 'Please confirm you want to play with the above character.',
                'choices': ['Yes', 'No'],
            },
        ]

        answer = prompt(question, style=custom_style_2)
        if answer.get('Selected') == 'Yes':
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
    def calculate_targets_in_physical_range(self, player_index, modifier=0):
        output = []
        for (target_index, target) in enumerate(players):
            if target_index != player_index:
                distance = abs(target_index - player_index)
                if distance > len(players) / 2:
                    distance = len(players) - distance
                if distance - (players[player_index].check_horsemanship() + modifier + (len(players[player_index].equipment_offensive_horse) + 1)) + (len(target.equipment_defensive_horse)) <= 0:
                    output.append(target_index)
        return output

    def calculate_targets_in_weapon_range(self, player_index, modifier=0, omit=None):
        output = []
        for (target_index, target) in enumerate(players):
            if target_index != player_index:
                distance = abs(target_index - player_index)
                if distance > len(players) / 2:
                    distance = len(players) - distance
                if distance - (players[player_index].check_horsemanship() + modifier + (len(players[player_index].equipment_offensive_horse)) + (players[player_index].weapon_range)) + (len(target.equipment_defensive_horse)) <= 0:
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

    def create_str_blind_menu(self):
        cards_discardable = (len(self.hand_cards.contents))
        if cards_discardable > 0:
            options_str = []
            options_str.append(
                Separator("-----------------HAND--CARDS-----------------"))
            i = 1
            for item in self.hand_cards.contents:
                options_str.append(f"Hand-Card {i}")
                i += 1

            return(options_str)

    def create_str_semiblind_menu(self, append_judgements=False):
        cards_discardable = (len(self.hand_cards.contents) + len(self.equipment_weapon) + len(
            self.equipment_armor) + len(self.equipment_offensive_horse) + len(self.equipment_defensive_horse))
        if append_judgements == 1:
            cards_discardable += len(self.pending_judgements)
        if cards_discardable > 0:
            options_str = []
            options_str.append(
                Separator("-----------------HAND--CARDS-----------------"))
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

    def create_str_nonblind_menu(self, only_hand_cards=False, append_judgements=False, omit_item=None):
        cards_discardable = (len(self.hand_cards.contents) + len(self.equipment_weapon) + len(
            self.equipment_armor) + len(self.equipment_offensive_horse) + len(self.equipment_defensive_horse))
        if append_judgements == 1:
            cards_discardable += len(self.pending_judgements)
        if cards_discardable > 0:
            options_str = []
            if not only_hand_cards:
                options_str.append(
                    Separator("-----------------HAND--CARDS-----------------"))
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
                self.current_health += players[0].use_reaction_effect(
                    "Brink Of Death", None, dying_player_index, reacting_player_index)
                if (players[dying_player_index].current_health < 1) and (players[0] != players[dying_player_index]):
                    self.current_health += players[dying_player_index].use_reaction_effect(
                        "Brink Of Death", None, dying_player_index, reacting_player_index)

            # Regular Brink of Death Loop
            else:
                for player in players[dying_player_index:]:
                    if players[dying_player_index].current_health > 0:
                        break
                    self.current_health += player.use_reaction_effect(
                        "Brink Of Death", None, dying_player_index, reacting_player_index)
                    reacting_player_index += 1
                    if reacting_player_index >= len(players):
                        reacting_player_index -= len(players)
                for player in players[:dying_player_index]:
                    if players[dying_player_index].current_health > 0:
                        break
                    self.current_health += player.use_reaction_effect(
                        "Brink Of Death", None, dying_player_index, reacting_player_index)
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
            main_deck.check_if_empty(main_deck, discard_deck)
            pending_judgement = self.pending_judgements.pop(0)
            if pending_judgement.effect2 == 'Acedia':
                print(
                    f"{self.character} must face judgement for ACEDIA; (needs HEARTS to pass, or else misses action-phase of turn).")
                main_deck.discard_from_deck()
                judgement_card = discard_deck.contents[0]
                print(f"{self.character} flipped a {judgement_card}.")
                judgement_card = check_judgement_tinkering(judgement_card, 0)
                self.check_envy_of_heaven()
                if self.check_beauty(judgement_card):
                    if judgement_card.suit == "Spades" or judgement_card.suit == "Hearts":
                        print(
                            f"{self.character}'s judgement card is a {judgement_card} and therefore {pending_judgement} has no effect.")
                elif judgement_card.suit == "Hearts":
                    print(
                        f"{self.character}'s judgement card is a {judgement_card} and therefore {pending_judgement} has no effect.")
                else:
                    print(
                        f"{self.character}'s judgement card is a {judgement_card} and thus they miss their action-phase of this turn.")
                    self.acedia_active = True
                discard_deck.add_to_top(pending_judgement)

            if pending_judgement.effect2 == 'Lightning':
                print(
                    f"{self.character} must face judgement for LIGHTNING; (needs anything but TWO to NINE of SPADES or else they suffer THREE points of lightning damage)! If no hit, LIGHTNING will pass onto {players[1].character}.")
                main_deck.discard_from_deck()
                judgement_card = discard_deck.contents[0]
                print(f"{self.character} flipped a {judgement_card}.")
                judgement_card = check_judgement_tinkering(judgement_card, 0)
                self.check_envy_of_heaven()

                if self.check_beauty(judgement_card):
                    print(
                        f"{self.character}'s judgement card is a {judgement_card} and therefore {pending_judgement} passes on to {players[1].character}.")
                    players[1].pending_judgements.insert(0, pending_judgement)

                elif judgement_card.suit == "Spades" and (10 > judgement_card.rank > 1):
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
                    f"{self.character} must face judgement for RATIONS DEPLETED; (needs CLUBS to pass, or else misses drawing-phase of turn).")
                main_deck.discard_from_deck()
                judgement_card = discard_deck.contents[0]
                print(f"{self.character} flipped a {judgement_card}.")
                judgement_card = check_judgement_tinkering(judgement_card, 0)
                self.check_envy_of_heaven()
                self.check_beauty(judgement_card)
                if judgement_card.suit == "Clubs":
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

            if (self.character_ability1.startswith("Blockade:") or self.character_ability3.startswith("Blockade:")):
                char_abils.append(" Character Ability >> Blockade")
            if (self.character_ability1.startswith("Dual Heroes:") or self.character_ability3.startswith("Dual Heroes:")):
                if self.used_dual_heroes != False:
                    char_abils.append(" Character Ability >> Dual Heroes")
            if (self.character_ability1.startswith("Drown in Wine:") or self.character_ability3.startswith("Drown in Wine:")):
                char_abils.append(" Character Ability >> Drown in Wine")
            if (self.character_ability2.startswith("Green Salve:") or self.character_ability3.startswith("Green Salve:")):
                char_abils.append(" Character Ability >> Green Salve")
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
            if (self.character_ability1.startswith("Surprise:") or self.character_ability3.startswith("Surprise:")):
                char_abils.append(" Character Ability >> Surprise")
            if (self.character_ability1.startswith("Trojan Flesh:") or self.character_ability3.startswith("Trojan Flesh:")):
                char_abils.append(" Character Ability >> Trojan Flesh")
            if (self.character_ability2.startswith("Warrior Saint:") or self.character_ability3.startswith("Warrior Saint:")):
                char_abils.append(" Character Ability >> Warrior Saint")
            return char_abils

        if types == "Attack":
            if (self.character_ability2.startswith("Warrior Saint:") or self.character_ability3.startswith("Warrior Saint:")):
                char_abils.append(" Character Ability >> Warrior Saint")
            return char_abils

    def reset_once_per_turn(self):
        self.attacks_this_turn = 0
        self.used_amber_sky = False
        self.used_bare_chested = False
        self.used_dual_heroes = False
        self.used_green_salve = False
        self.used_marriage = False
        self.used_reconsider = False

# Equipment-card checks
    def armor_black_shield(self, attack_card, source_player_index=0):
        if len(self.equipment_armor) > 0:
            if self.equipment_armor[0].effect == "Black Shield":
                if players[source_player_index].check_beauty():
                    if attack_card.suit == "Clubs":
                        print(
                            f"  >> {self.character} has {self.equipment_armor[0]} equipped, and therefore CANNOT be affected by black attack cards. ({attack_card} discarded as normal)")
                        return True

                if attack_card.suit == "Spades" or attack_card.suit == "Clubs":
                    print(
                        f"  >> {self.character} has {self.equipment_armor[0]} equipped, and therefore CANNOT be affected by black attack cards. ({attack_card} discarded as normal)")
                    return True
            else:
                return False

    def armor_eight_trigrams(self):
        if len(self.equipment_armor) > 0:
            if self.equipment_armor[0].effect == "Eight-Trigrams":

                if self.equipment_armor[0].suit == "Spades":
                    for player_index, player in enumerate(players):
                        if len(player.equipment_armor) > 0:
                            if player.equipment_armor[0].effect == "Eight-Trigrams" and player.equipment_armor[0].suit == "Spades":
                                user_index = player_index
                                break

                if self.equipment_armor[0].suit == "Clubs":
                    for player_index, player in enumerate(players):
                        if len(player.equipment_armor) > 0:
                            if player.equipment_armor[0].effect == "Eight-Trigrams" and player.equipment_armor[0].suit == "Clubs":
                                user_index = player_index
                                break

                question = [
                    {
                        'type': 'list',
                        'name': 'Selected',
                        'message': f'{self.character}: Choose to activate Eight-Trigrams (armor), and flip a judgement card (if red, automatically DEFEND is played)?',
                        'choices': ['Yes', 'No'],
                    },
                ]
                answer = prompt(question, style=custom_style_2)
                if answer.get('Selected') == 'Yes':
                    main_deck.check_if_empty(main_deck, discard_deck)
                    print(
                        f"  >> {self.character} chose to activate their equipped {self.equipment_armor[0]} (armor); needs HEARTS or DIAMONDS to automatically dodge.")
                    main_deck.discard_from_deck()
                    judgement_card = discard_deck.contents[0]
                    print(f"{self.character} flipped a {judgement_card}.")
                    judgement_card = check_judgement_tinkering(
                        judgement_card, user_index)
                    self.check_envy_of_heaven()
                    if self.check_beauty(judgement_card):
                        if judgement_card.suit == "Spades" or judgement_card.suit == "Hearts" or judgement_card.suit == "Diamonds":
                            return (True, judgement_card)
                    if judgement_card.suit == "Hearts" or judgement_card.suit == "Diamonds":
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
                    question = [
                        {
                            'type': 'list',
                            'name': 'Selected',
                            'message': f'{self.character}: Would you like to discard two cards to force the damage against {players[target_index].character} ({players[target_index].current_health}/{players[target_index].max_health} HP remaining)?',
                            'choices': ['Yes', 'No']
                        },
                    ]
                    answer = prompt(question, style=custom_style_2)
                    if answer.get('Selected') == "Yes":
                        num = 2
                        options_str = self.create_str_nonblind_menu(
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
                            if card_index > len(self.hand_cards.contents) - 1:
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
                        self.check_insanity(target_index)
                        for player_index, player in enumerate(players):
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
                        self.check_lament(user_index, target_index)
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
                        question = [
                            {
                                'type': 'list',
                                'name': 'Selected',
                                'message': f'{self.character}: Would you like to force {players[target_index].character} to discard two cards instead of taking damage ({players[target_index].current_health}/{players[target_index].max_health} HP remaining)?',
                                'choices': ['Yes', 'No']
                            },
                        ]
                        answer = prompt(question, style=custom_style_2)
                        if answer.get('Selected') == "Yes":
                            print(
                                f"  >> {self.character} has {self.equipment_weapon[0]} equipped, and chose to make {players[target_index].character} discard two cards instead of taking damage.")
                            players[target_index].check_weapon_frost_blade(
                                0, "Activate")
                            return True

        if mode == "Activate":
            self.discard_from_equip_or_hand(2)

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
                    question = [
                        {
                            'type': 'list',
                            'name': 'Selected',
                            'message': f'{self.character}: Your ATTACK was defended by {players[target_index].character}. ATTACK again with Green Dragon Halberd?',
                            'choices': ['Yes', 'No']
                        },
                    ]
                    answer = prompt(question, style=custom_style_2)
                    if answer.get('Selected') == "Yes":
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

                        options_str = get_playing_card_options(self.hand_cards)
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

                        if card1.suit == "Spades" or card1.suit == "Clubs":
                            if card2.suit == "Spades" or card2.suit == "Clubs":
                                return ["Black Attack", card1_index, card1, card2_index, card2]

                        if card1.suit == "Hearts" or card2.suit == "Diamonds":
                            if card2.suit == "Hearts" or card2.suit == "Diamonds":
                                return ["Red Attack", card1_index, card1, card2_index, card2]

                        else:
                            return ["Colourless Attack", card1_index, card1, card2_index, card2]

    def check_weapon_sky_scorcher_halberd(self, target_index=0):
        if target_index == None:
            target_index = 0
        if len(self.hand_cards.contents) == 0:
            if self.equipment_weapon[0].effect == "Sky Scorcher Halberd":
                question = [
                    {
                        'type': 'list',
                        'name': 'Selected',
                        'message': f'{self.character}: You used your last hand-card to ATTACK {players[target_index].character} with Sky Scorcher Halberd. Target extra players?',
                        'choices': ['Yes', 'No']
                    },
                ]
                answer = prompt(question, style=custom_style_2)
                if answer.get('Selected') == "Yes":
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

# Using/discarding cards from a players' hand
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
                        return (' ')

                    print(f"ATTACK - Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.")
                    question = [
                        {
                            'type': 'list',
                            'name': 'Selected',
                            'message': f'{self.character}: Please confirm you would like to use a BLACK ATTACK via {self.equipment_weapon[0]} against {players[selected]}?',
                            'choices': ['Yes', 'No'],
                        },
                    ]
                    answer = prompt(question, style=custom_style_2)
                    if answer.get('Selected') == 'Yes':
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

                else:
                    print(
                        f"{self.character}: You have insufficient range to reach anyone with {card}.")
            elif (self.attacks_this_turn > 0):
                print(
                    f"{self.character}: You can only play one ATTACK card per turn.")

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
                        return (' ')

                    print(f"ATTACK - Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.")
                    question = [
                        {
                            'type': 'list',
                            'name': 'Selected',
                            'message': f'{self.character}: Please confirm you would like to use a RED ATTACK via {self.equipment_weapon[0]} against {players[selected]}?',
                            'choices': ['Yes', 'No'],
                        },
                    ]
                    answer = prompt(question, style=custom_style_2)
                    if answer.get('Selected') == 'Yes':
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
                        return (' ')

                    print(f"ATTACK - Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.")
                    question = [
                        {
                            'type': 'list',
                            'name': 'Selected',
                            'message': f'{self.character}: Please confirm you would like to use a COLOURLESS ATTACK via {self.equipment_weapon[0]} against {players[selected]}?',
                            'choices': ['Yes', 'No'],
                        },
                    ]
                    answer = prompt(question, style=custom_style_2)
                    if answer.get('Selected') == 'Yes':
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
                        return (' ')

                    print(f"{card} - ATTACK - Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.")
                    question = [
                        {
                            'type': 'list',
                            'name': 'Selected',
                            'message': f'{self.character}: Please confirm you would like to use {card} against {players[selected]}?',
                            'choices': ['Yes', 'No'],
                        },
                    ]
                    answer = prompt(question, style=custom_style_2)
                    if answer.get('Selected') == 'Yes':
                        self.attacks_this_turn += 1
                        if card_index == "Special":
                            discarded = card
                        else:
                            discarded = self.hand_cards.contents.pop(
                                card_index)
                            discard_deck.add_to_top(discarded)
                        self.check_ardour(discarded)
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
                        return True
                else:
                    print(
                        f"{self.character}: You have insufficient range to reach anyone with {card}.")
            elif (self.attacks_this_turn > 0):
                print(
                    f"{self.character}: You can only play one ATTACK card per turn.")

        elif card.effect2 == 'Defend':
            print(
                f"{self.character}: {card} can only be played as a reaction.")

        elif card.effect2 == 'Peach':
            if self.max_health > self.current_health:
                print(f"{card} - PEACH - During your turn, you can use this card to recover one unit of missing health. Additionally, whenever a player is on the brink of death, any player can use a PEACH to make them recover one unit of health.")
                question = [
                    {
                        'type': 'list',
                        'name': 'Selected',
                        'message': f'{self.character}: Please confirm you would like to use the basic card: {card.effect}.',
                        'choices': ['Yes', 'No'],
                    },
                ]
                answer = prompt(question, style=custom_style_2)
                if answer.get('Selected') == 'Yes':
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

        # card.type == 'Tool':
        elif card.effect2 == 'Barbarians':
            print(f"{card} - BARBARIANS - {card.flavour_text}")
            question = [
                {
                    'type': 'list',
                    'name': 'Selected',
                    'message': f'{self.character}: Please confirm you would like to use the tool card: {card.effect}.',
                    'choices': ['Yes', 'No'],
                },
            ]
            answer = prompt(question, style=custom_style_2)
            if answer.get('Selected') == 'Yes':
                print(
                    f"{self.character} has activated {card}. All damaged players will take one damage (unless playing ATTACK or tool-card negated).")
                discarded = self.hand_cards.contents.pop(card_index)
                self.check_one_after_another()
                self.check_wisdom()
                discard_deck.add_to_top(discarded)
                # NEED SOME SORT OF NEGATE LOOP HERE !?!?!?
                for player_index, player in enumerate(players):
                    if (player != players[0]) and (player.current_health > 0):
                        beauty = self.check_beauty(discarded)
                        if not player.check_behind_the_curtain(discarded, beauty):
                            barb_response = player.use_reaction_effect(
                                "Attack", discarded, 0, player)
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
                                self.check_insanity(player)

                                if player.current_health < 1:
                                    player.check_brink_of_death_loop(
                                        player_index, 0)

                                if player.current_health > 0:
                                    if fantasy[0]:
                                        cards_to_draw = (
                                            player.max_health - player.current_health)
                                        print(
                                            f"  >> Character Ability: Fantasy; {player.character} draws {cards_to_draw} from the deck.")
                                        player.hand_cards.draw(
                                            main_deck, cards_to_draw, False)

                                    player.check_eternal_loyalty(damage_dealt)
                                    player.check_evil_hero(card)
                                    player.check_exile()
                                    player.check_eye_for_an_eye(
                                        source_player_index=0, mode="Activate")
                                    player.check_geminate(damage_dealt)
                                    player.check_plotting_for_power(
                                        damage_dealt, mode="Reaction")
                                    player.check_retaliation(0, damage_dealt)

        elif card.effect2 == 'Granary':
            print(f"{card} - GRANARY - {card.flavour_text}")
            question = [
                {
                    'type': 'list',
                    'name': 'Selected',
                    'message': f'{self.character}: Please confirm you would like to use the tool card: {card.effect}.',
                    'choices': ['Yes', 'No'],
                },
            ]
            answer = prompt(question, style=custom_style_2)
            if answer.get('Selected') == 'Yes':
                print(
                    f"{self.character} has activated {card}. {len(players)} cards have been flipped from the deck. Everyone takes a card; {self.character} goes first!")
                discarded = self.hand_cards.contents.pop(card_index)
                self.check_one_after_another()
                self.check_wisdom()
                discard_deck.add_to_top(discarded)
                granary = Player("Temporary")
                granary.hand_cards.draw(main_deck, len(players), False)
                options_str = granary.create_str_nonblind_menu(
                    only_hand_cards=True)
                for player in players:
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
                    print(f"{player.character} has taken {drawn} via GRANARY!")

        elif card.effect2 == 'Peach Gardens':
            print(f"{card} - PEACH GARDENS - {card.flavour_text}")
            question = [
                {
                    'type': 'list',
                    'name': 'Selected',
                    'message': f'{self.character}: Please confirm you would like to use the tool card: {card.effect}.',
                    'choices': ['Yes', 'No'],
                },
            ]
            answer = prompt(question, style=custom_style_2)
            if answer.get('Selected') == 'Yes':
                print(
                    f"{self.character} has activated {card}. All damaged players will be healed by one health (unless negated).")
                discarded = self.hand_cards.contents.pop(card_index)
                self.check_one_after_another()
                self.check_wisdom()
                discard_deck.add_to_top(discarded)
                for player in players:
                    if player.max_health > player.current_health:
                        player.current_health += 1
                        print(
                            f"{player.character} has been healed by one. ({player.current_health}/{player.max_health} HP remaining)")

        elif card.effect2 == 'Rain of Arrows':
            print(
                f"{card} - RAIN OF ARROWS - All other players must play a DEFEND or else suffer one damage.")
            question = [
                {
                    'type': 'list',
                    'name': 'Selected',
                    'message': f'{self.character}: Please confirm you would like to use the tool card: RAIN OF ARROWS.',
                    'choices': ['Yes', 'No'],
                },
            ]
            answer = prompt(question, style=custom_style_2)
            if answer.get('Selected') == 'No':
                return False

            if answer.get('Selected') == 'Yes':
                print(
                    f"{self.character} has activated RAIN OF ARROWS. All damaged players will take one damage (unless playing DEFEND or tool-card negated).")
                if card_index == "Special":
                    discarded = card
                else:
                    discarded = self.hand_cards.contents.pop(card_index)
                self.check_one_after_another()
                self.check_wisdom()
                discard_deck.add_to_top(discarded)
                # NEED SOME SORT OF NEGATE LOOP HERE !?!?!?
                for player_index, player in enumerate(players):
                    if (player != players[0]) and (player.current_health > 0):
                        beauty = self.check_beauty(discarded)
                        if not player.check_behind_the_curtain(discarded, beauty):
                            roa_response = player.use_reaction_effect(
                                "Defend", discarded, 0, player)
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
                                self.check_insanity(player)

                                if player.current_health < 1:
                                    player.check_brink_of_death_loop(
                                        player_index, 0)

                                if player.current_health > 0:
                                    if fantasy[0]:
                                        cards_to_draw = (
                                            player.max_health - player.current_health)
                                        print(
                                            f"  >> Character Ability: Fantasy; {player.character} draws {cards_to_draw} from the deck.")
                                        player.hand_cards.draw(
                                            main_deck, cards_to_draw, False)
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

            if possible_targets > 0:
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

                print(
                    f"{card} - COERCE - Use this card to target any other player that possesses a weapon. Afterwards, you can then select any target within their attacking range. Your target can then ATTACK the victim. If they do not, you will take their weapon and add it to your hand.")
                question = [
                    {
                        'type': 'list',
                        'name': 'Selected',
                        'message': f'{self.character}: Please confirm you would like to use {card} against {players[selected]}?',
                        'choices': ['Yes', 'No'],
                    },
                ]
                answer = prompt(question, style=custom_style_2)
                if answer.get('Selected') == 'No':
                    return False
                if answer.get('Selected') == 'Yes':
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
                        else:
                            print(
                                f"{self.character} has coerced {players[selected].character} into attacking {players[attacked].character}. If they refuse, {self.character} gets their weapon.")
                            discarded = self.hand_cards.contents.pop(
                                card_index)
                            discard_deck.add_to_top(discarded)
                            self.check_one_after_another()
                            self.check_wisdom()
                            players[selected].activate_coerce(
                                selected, attacked, discarded)

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

            print(
                f"{card} - DISMANTLE - You can target any player and discard one of their cards, on-hand or equipped.")
            question = [
                {
                    'type': 'list',
                    'name': 'Selected',
                    'message': f'{self.character}: Please confirm you would like to use {card} against {players[selected]}?',
                    'choices': ['Yes', 'No'],
                },
            ]
            answer = prompt(question, style=custom_style_2)
            if answer.get('Selected') == 'No':
                return False
            beauty = self.check_beauty(card)
            if players[selected].check_behind_the_curtain(card, beauty):
                return False
            if answer.get('Selected') == 'Yes':
                cards_discardable = (len(players[selected].hand_cards.contents) + len(players[selected].equipment_weapon) + len(
                    players[selected].equipment_armor) + len(players[selected].equipment_offensive_horse) + len(players[selected].equipment_defensive_horse) + len(players[selected].pending_judgements))

                if cards_discardable == 0:
                    print(
                        f"{players[selected].character} has no cards that can be dismantled.")
                    return False

                if cards_discardable > 0:
                    options_str = players[selected].create_str_semiblind_menu(
                        True)

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
                if card_index == "Special":
                    discarded = card
                else:
                    discarded = self.hand_cards.contents.pop(card_index)
                    discard_deck.add_to_top(discarded)
                self.check_one_after_another()
                self.check_wisdom()

                # Check if hand-card
                if card_dismantled_index <= len(players[selected].hand_cards.contents):
                    card_dismantled = players[selected].hand_cards.contents.pop(
                        card_dismantled_index - 1)
                    discard_deck.add_to_top(card_dismantled)
                    print(
                        f"{self.character} has destroyed {card_dismantled} from {players[selected].character}'s hand by using {card}.")
                    players[selected].check_one_after_another()

                # Check if equipment-card
                if card_dismantled_index > len(players[selected].hand_cards.contents):
                    if card_dismantled_index == (len(players[selected].hand_cards.contents) + 2):
                        card_dismantled = players[selected].equipment_weapon.pop(
                        )
                        discard_deck.add_to_top(card_dismantled)
                        players[selected].weapon_range = 1
                        print(
                            f"{self.character} has destroyed {card_dismantled} from {players[selected].character}'s weapon-slot by using {card}.")
                        players[selected].check_warrior_woman()

                    elif card_dismantled_index == (len(players[selected].hand_cards.contents) + 3):
                        card_dismantled = players[selected].equipment_armor.pop(
                        )
                        discard_deck.add_to_top(card_dismantled)
                        print(
                            f"{self.character} has destroyed {card_dismantled} from {players[selected].character}'s armor-slot by using {card}.")
                        players[selected].check_warrior_woman()

                    elif card_dismantled_index == (len(players[selected].hand_cards.contents) + 4):
                        card_dismantled = players[selected].equipment_offensive_horse.pop(
                        )
                        discard_deck.add_to_top(card_dismantled)
                        print(
                            f"{self.character} has destroyed {card_dismantled} from {players[selected].character}'s horse-slot by using {card}.")
                        players[selected].check_warrior_woman()

                    elif card_dismantled_index == (len(players[selected].hand_cards.contents) + 5):
                        card_dismantled = players[selected].equipment_defensive_horse.pop(
                        )
                        discard_deck.add_to_top(card_dismantled)
                        print(
                            f"{self.character} has destroyed {card_dismantled} from {players[selected].character}'s horse-slot by using {card}.")
                        players[selected].check_warrior_woman()

                    # Check if pending-time-delay-tool-card
                    else:
                        if card_dismantled_index == (len(players[selected].hand_cards.contents) + 7):
                            card_dismantled = players[selected].pending_judgements[0]
                            discard_deck.add_to_top(
                                card_dismantled)
                            print(
                                f"{self.character} has destroyed {card_dismantled} from {players[selected].character}'s pending judgements by using {card}.")

                        if card_dismantled_index == (len(players[selected].hand_cards.contents) + 8):
                            card_dismantled = players[selected].pending_judgements[1]
                            discard_deck.add_to_top(
                                card_dismantled)
                            print(
                                f"{self.character} has destroyed {card_dismantled} from {players[selected].character}'s pending judgements by using {card}.")

                        if card_dismantled_index == (len(players[selected].hand_cards.contents) + 9):
                            card_dismantled = players[selected].pending_judgements[2]
                            discard_deck.add_to_top(
                                card_dismantled)
                            print(
                                f"{self.character} has destroyed {card_dismantled} from {players[selected].character}'s pending judgements by using {card}.")
            players[selected].check_one_after_another()
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

            print(f"{card} - DUEL - You can target any player for a duel with this card. If the target does not play an ATTACK, they are damaged. If they do ATTACK, then you must play one in response or take damage. Whoever does not attack, takes damage.")
            question = [
                {
                    'type': 'list',
                    'name': 'Selected',
                    'message': f'{self.character}: Please confirm you would like to use {card} against {players[selected]}?',
                    'choices': ['Yes', 'No'],
                },
            ]
            answer = prompt(question, style=custom_style_2)
            if answer.get('Selected') == 'No':
                return False
            beauty = self.check_beauty(card)
            if players[selected].check_behind_the_curtain(card, beauty):
                return False
            if answer.get('Selected') == 'Yes':
                if card_index == "Special":
                    discarded = card
                else:
                    discarded = self.hand_cards.contents.pop(
                        card_index)
                    discard_deck.add_to_top(discarded)
                print(
                    f"{self.character} has challenged {players[selected].character} to a DUEL! Players must play ATTACK cards in turn, until one doesn't. The loser of the DUEL, takes one damage!")
                self.check_ardour(discarded)
                self.check_one_after_another()
                duel_won = players[selected].use_reaction_effect(
                    "Attack", discarded, 0, selected)
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

                    players[selected].current_health -= damage_dealt
                    print(
                        f"{self.character} has won the DUEL! {players[selected].character} takes {damage_dealt} damage! ({players[selected].current_health}/{players[selected].max_health} HP remaining)")
                    for player_index, player in enumerate(players):
                        if player.current_health < 1:
                            if players[player_index].check_brink_of_death_loop(player_index, 0) == "Break":
                                return "Break"

                    if fantasy[0]:
                        cards_to_draw = (
                            players[selected].max_health - players[selected].current_health)
                        print(
                            f"  >> Character Ability: Fantasy; {self.character} draws {cards_to_draw} from the deck.")
                        players[selected].hand_cards.draw(
                            main_deck, cards_to_draw, False)
                    players[selected].check_eternal_loyalty(damage_dealt)
                    players[selected].check_evil_hero(card)
                    players[selected].check_exile()
                    if players[selected].check_eye_for_an_eye(
                            source_player_index=0, mode="Activate") == "Break":
                        return(' ')
                    players[selected].check_geminate(damage_dealt)
                    players[selected].check_plotting_for_power(
                        damage_dealt, mode="Reaction")
                    players[selected].check_retaliation(0, damage_dealt)

                if not duel_won:
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

                        self.current_health -= damage_dealt
                        print(
                            f"{players[selected].character} has won the DUEL! {self.character} takes {damage_dealt} damage! ({self.current_health}/{self.max_health} HP remaining)")

                        for player_index, player in enumerate(players):
                            if player.current_health < 1:
                                if players[player_index].check_brink_of_death_loop(player_index, 0) == "Break":
                                    return "Break"

                        self.check_eternal_loyalty(damage_dealt)
                        self.check_evil_hero(card)
                        self.check_exile()
                        if self.check_eye_for_an_eye(
                                source_player_index=selected, mode="Activate") == "Break":
                            return(' ')
                        self.check_geminate(damage_dealt)
                        self.check_plotting_for_power(
                            damage_dealt, mode="Reaction")
                        self.check_retaliation(0, damage_dealt)

                    else:
                        redirected = fantasy[1]
                        deplete_karma = self.check_deplete_karma(
                            damage_dealt, None, redirected)
                        if deplete_karma[0]:
                            damage_dealt = deplete_karma[1]
                        deplete_karma = players[redirected].check_deplete_karma(
                            damage_dealt, 0, None)
                        if deplete_karma[0]:
                            damage_dealt = deplete_karma[1]

                        players[redirected].current_health -= damage_dealt
                        print(
                            f"{players[selected].character} has won the DUEL! {players[redirected].character} takes {damage_dealt} damage! ({players[redirected].current_health}/{players[redirected].max_health} HP remaining)")

                        for player_index, player in enumerate(players):
                            if player.current_health < 1:
                                if players[player_index].check_brink_of_death_loop(player_index, 0) == "Break":
                                    return "Break"

                        cards_to_draw = (
                            players[redirected].max_health - players[redirected].current_health)
                        print(
                            f"  >> Character Ability: Fantasy; {players[redirected].character} draws {cards_to_draw} from the deck.")
                        players[redirected].hand_cards.draw(
                            main_deck, cards_to_draw, False)
                        players[redirected].check_eternal_loyalty(damage_dealt)
                        players[redirected].check_evil_hero(card)
                        players[redirected].check_exile()
                        if players[redirected].check_eye_for_an_eye(
                                source_player_index=selected, mode="Activate") == "Break":
                            return(' ')
                        players[redirected].check_geminate(damage_dealt)
                        players[redirected].check_plotting_for_power(
                            damage_dealt, mode="Reaction")
                        players[redirected].check_retaliation(0, damage_dealt)
                return True

        elif card.effect2 == 'Negate':
            print(
                f"{self.character}: {card} can only be played as a reaction.")

        elif card.effect2 == 'Greed':
            print(f"{card} - GREED - {card.flavour_text}")
            question = [
                {
                    'type': 'list',
                    'name': 'Selected',
                    'message': f'{self.character}: Please confirm you would like to use the tool card: {card.effect}.',
                    'choices': ['Yes', 'No'],
                },
            ]
            answer = prompt(question, style=custom_style_2)
            if answer.get('Selected') == 'Yes':
                if card_index == "Special":
                    discarded = card
                else:
                    discarded = self.hand_cards.contents.pop(card_index)
                self.check_one_after_another()
                self.check_wisdom()
                discard_deck.add_to_top(discarded)
                print(f"{self.character} has played {card}.")
                self.hand_cards.draw(main_deck, 2)

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

                print(f"{card} - STEAL - You can use this card on a player within physical range to take a card from them (on-hand or equipped) and add it to your hand.")
                question = [
                    {
                        'type': 'list',
                        'name': 'Selected',
                        'message': f'{self.character}: Please confirm you would like to use {card} against {players[selected]}?',
                        'choices': ['Yes', 'No'],
                    },
                ]
                answer = prompt(question, style=custom_style_2)
                if answer.get('Selected') == 'No':
                    return False
                beauty = self.check_beauty(card)
                if players[selected].check_behind_the_curtain(card, beauty):
                    return False
                if answer.get('Selected') == 'Yes':
                    cards_discardable = (len(players[selected].hand_cards.contents) + len(players[selected].equipment_weapon) + len(
                        players[selected].equipment_armor) + len(players[selected].equipment_offensive_horse) + len(players[selected].equipment_defensive_horse) + len(players[selected].pending_judgements))

                    if cards_discardable == 0:
                        print(
                            f"{players[selected].character} has no cards that can be stolen.")
                        return False

                    if cards_discardable > 0:
                        options_str = players[selected].create_str_semiblind_menu(
                            True)

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
                    if card_index == "Special":
                        discarded = card
                    else:
                        discarded = self.hand_cards.contents.pop(
                            card_index)
                        discard_deck.add_to_top(discarded)
                    self.check_one_after_another()
                    self.check_wisdom()

                    # Check if hand-card
                    if card_stolen_index <= len(players[selected].hand_cards.contents):
                        card_stolen = players[selected].hand_cards.contents.pop(
                            card_stolen_index - 1)
                        self.hand_cards.add_to_top(card_stolen)
                        print(
                            f"{self.character} has taken {card_stolen} from {players[selected].character}'s hand by using {card}.")
                        players[selected].check_one_after_another()

                    # Check if equipment-card
                    if card_stolen_index > len(players[selected].hand_cards.contents):
                        if card_stolen_index == (len(players[selected].hand_cards.contents) + 2):
                            card_stolen = players[selected].equipment_weapon.pop(
                            )
                            players[selected].weapon_range = 1
                            self.hand_cards.add_to_top(card_stolen)
                            print(
                                f"{self.character} has taken {card_stolen} from {players[selected].character}'s weapon-slot by using {card}.")
                            players[selected].check_warrior_woman()

                        elif card_stolen_index == (len(players[selected].hand_cards.contents) + 3):
                            card_stolen = players[selected].equipment_armor.pop(
                            )
                            self.hand_cards.add_to_top(card_stolen)
                            print(
                                f"{self.character} has taken {card_stolen} from {players[selected].character}'s armor-slot by using {card}.")
                            players[selected].check_warrior_woman()

                        elif card_stolen_index == (len(players[selected].hand_cards.contents) + 4):
                            card_stolen = players[selected].equipment_offensive_horse.pop(
                            )
                            self.hand_cards.add_to_top(card_stolen)
                            print(
                                f"{self.character} has taken {card_stolen} from {players[selected].character}'s horse-slot by using {card}.")
                            players[selected].check_warrior_woman()

                        elif card_stolen_index == (len(players[selected].hand_cards.contents) + 5):
                            card_stolen = players[selected].equipment_defensive_horse.pop(
                            )
                            self.hand_cards.add_to_top(card_stolen)
                            print(
                                f"{self.character} has taken {card_stolen} from {players[selected].character}'s horse-slot by using {card}.")
                            players[selected].check_warrior_woman()

                        # Check if pending-time-delay-tool-card
                        else:
                            if card_stolen_index == (len(players[selected].hand_cards.contents) + 7):
                                card_stolen = players[selected].pending_judgements[0]
                                self.hand_cards.add_to_top(card_stolen)
                                print(
                                    f"{self.character} has taken {card_stolen} from {players[selected].character}'s pending judgements by using {card}.")

                            if card_stolen_index == (len(players[selected].hand_cards.contents) + 8):
                                card_stolen = players[selected].pending_judgements[1]
                                self.hand_cards.add_to_top(card_stolen)
                                print(
                                    f"{self.character} has taken {card_stolen} from {players[selected].character}'s pending judgements by using {card}.")

                            if card_stolen_index == (len(players[selected].hand_cards.contents) + 9):
                                card_stolen = players[selected].pending_judgements[2]
                                self.hand_cards.add_to_top(card_stolen)
                                print(
                                    f"{self.character} has taken {card_stolen} from {players[selected].character}'s pending judgements by using {card}.")
                players[selected].check_one_after_another()
                return True
            else:
                print(
                    f"{self.character}: You have insufficient range to reach anyone with {card}.")
                return False

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
                return (' ')

            print(f"{card} - ACEDIA - You can place Delay-Tool on any other player. The target must perform a judgement for this card. If it is not HEARTS, they forfeit their action-phase.")
            question = [
                {
                    'type': 'list',
                    'name': 'Selected',
                    'message': f'{self.character}: Please confirm you would like to use {card} against {players[selected].character}?',
                    'choices': ['Yes', 'No'],
                },
            ]
            answer = prompt(question, style=custom_style_2)
            if answer.get('Selected') == 'No':
                return False
            beauty = self.check_beauty(card)
            if players[selected].check_behind_the_curtain(card, beauty):
                return False
            if answer.get('Selected') == 'Yes':
                for possible_acedia in players[selected].pending_judgements:
                    if possible_acedia.effect2 == 'Acedia':
                        print(
                            f"{self.character}: {players[selected].character} cannot be targeted by ACEDIA as they already have one pending.")
                else:
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
                question = [
                    {
                        'type': 'list',
                        'name': 'Selected',
                        'message': f'{self.character}: Please confirm you would like to use the delay-tool card: {card.effect}.',
                        'choices': ['Yes', 'No'],
                    },
                ]
                answer = prompt(question, style=custom_style_2)
                if answer.get('Selected') == 'Yes':
                    beauty = self.check_beauty(card)
                    if players[selected].check_behind_the_curtain(card, beauty):
                        return False
                    else:
                        discarded = self.hand_cards.contents.pop(
                            card_index)
                    self.check_one_after_another()
                    self.pending_judgements.append(card)
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

                print(f"{card} - RATIONS DEPLETED - You can place Delay-Tool on any other player in physical range. The target must perform a judgement for this card. If it is not CLUBS, they forfeit their draw-phase.")
                question = [
                    {
                        'type': 'list',
                        'name': 'Selected',
                        'message': f'{self.character}: Please confirm you would like to use {card} against {players[selected].character}?',
                        'choices': ['Yes', 'No'],
                    },
                ]
                answer = prompt(question, style=custom_style_2)
                if answer.get('Selected') == 'No':
                    return False
                beauty = self.check_beauty(card)
                if players[selected].check_behind_the_curtain(card, beauty):
                    return False
                if answer.get('Selected') == 'Yes':
                    for possible_rations_depleted in players[selected].pending_judgements:
                        if possible_rations_depleted.effect2 == 'Rations Depleted':
                            print(
                                f"{self.character}: {players[selected].character} cannot be targeted by RATIONS DEPLETED as they already have one pending.")
                        return False
                    else:
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
                    if popping:
                        discarded = self.equipment_offensive_horse.pop()
                        discard_deck.add_to_top(discarded)
                        self.check_warrior_woman()
                    self.hand_cards.contents.pop(card_index)
                    self.equipment_offensive_horse = [card]
                    self.check_one_after_another()
                    print(f"{self.character} has equipped {card}.")
        popping = False

    def activate_attack(self, discarded, selected, coerced=0, discarded2=None):
        # Early pre-reactionary effects
        redirect = players[selected].check_displacement(
            source_player_index=coerced)
        if redirect[0]:
            return self.activate_attack(discarded, redirect[1], coerced, discarded2)
        elif players[selected].check_relish(source_player_index=0, mode="Activate"):
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

        # Check for DEFEND
        attack_defended = players[selected].use_reaction_effect(
            "Defend", discarded, coerced, selected)
        if type(attack_defended) == Card:
            if (attack_defended.effect == "Defend") or (attack_defended.effect2 == "Defend"):
                print(
                    f"{players[selected].character} successfully defended the ATTACK with {attack_defended}.")

                # DEFENDED - reactionary abilities
                self.check_weapon_axe(discarded, selected)
                self.check_fearsome_advance(
                    discarded, selected)
                players[selected].check_lightning_strike()
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
            self.check_insanity(selected)
            self.wine_active = False

            # DAMAGED - post-damage abilities and brink of death
            for player_index, player in enumerate(players):
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

            self.check_lament(coerced, selected)
            players[selected].check_eternal_loyalty(
                damage_dealt)
            players[selected].check_evil_hero(discarded, discarded2)
            players[selected].check_exile()
            if players[selected].check_eye_for_an_eye(
                    source_player_index=coerced, mode="Activate") == "Break":
                return(' ')
            players[selected].check_geminate(damage_dealt)
            players[selected].check_plotting_for_power(
                damage_dealt, mode="Reaction")
            players[selected].check_retaliation(coerced, damage_dealt)

    def activate_coerce(self, coerced, selected=0, discarded=None):
        options_str = []
        options_str.append(
            Separator("--------------------Cards--------------------"))
        playing_card_options_str = get_playing_card_options(self.hand_cards)
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
            players[0].hand_cards.add_to_top(weapon)
            print(
                f"{self.character}: Your weapon has been stolen by {players[0].character} for not attacking {players[selected].character}!")

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

    def use_reaction_effect(self, response_required, card_played=None, player_index=None, reacting_player_index=None):
        if player_index == None:
            player_index = 0
        if reacting_player_index == None:
            reacting_player_index = 0
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
                        if players[player_index].check_break_brink_loop(output_value):
                            reactions_possible = False
                            return(output_value)

                elif self.hand_cards.contents[card_index].effect == "Peach":
                    discarded = self.hand_cards.contents.pop(card_index)
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
                    if players[player_index].check_break_brink_loop(output_value):
                        reactions_possible = False
                        return(output_value)

            elif response_required == "Defend" and ((card_played.effect2 == "Attack") or (card_played.effect2 == "Black Attack") or (card_played.effect2 == "Red Attack") or (card_played.effect2 == "Colourless Attack")):
                if card_played.effect2 == "Attack" or card_played.effect2 == "Red Attack":
                    self.check_ardour(card_played, player_index)

                if not players[player_index].check_weapon_black_pommel():
                    armor_check = self.armor_eight_trigrams(
                    )
                    if armor_check[0]:
                        return(armor_check[1])

                options_str = self.hand_cards.list_cards()
                options_str.append(
                    Separator("--------------------Other--------------------"))
                if self.check_impetus(player_index, "Check"):
                    options_str.append(" Character Ability >> Impetus")
                options_str.append("Do nothing.")

                if card_played.effect2 == "Attack":
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
                    return(0)

                elif options_str[card_index] == " Character Ability >> Impetus":
                    discarded = (self.check_impetus(player_index, "Activate"))
                    if discarded != None:
                        discarded.effect2 = "Defend"
                        reactions_possible = False
                        return(discarded)

                elif self.hand_cards.contents[card_index].effect == "Defend":
                    discarded = self.hand_cards.contents.pop(card_index)
                    self.check_one_after_another()
                    discard_deck.add_to_top(discarded)
                    discarded.effect2 = "Defend"
                    reactions_possible = False
                    return(discarded)

            elif response_required == "Attack" and card_played.effect2 == "Barbarians":

                options_str = self.hand_cards.list_cards()
                options_str.append(
                    Separator("--------------------Other--------------------"))
                if self.activate_warrior_saint("Check"):
                    options_str.append(" Character Ability >> Warrior Saint")
                if self.check_weapon_serpent_spear("Check"):
                    options_str.append(" Weapon Ability >> Serpent Spear")
                options_str.append("Do nothing.")

                question = [
                    {
                        'type': 'list',
                        'name': 'Selected',
                        'message': f"{self.character}: {players[player_index].character} has activated BARBARIANS; please choose a response (an ATTACK card or do nothing)!",
                        'choices': options_str,
                        'filter': lambda card: options_str.index(card)
                    },
                ]
                answer = prompt(question, style=custom_style_2)
                card_index = answer.get('Selected')
                if options_str[card_index] == "Do nothing.":
                    reactions_possible = False
                    return(0)

                elif options_str[card_index] == " Character Ability >> Warrior Saint":
                    discarded = self.activate_warrior_saint("Reaction")
                    if discarded != None:
                        discarded.effect2 = "Attack"
                        reactions_possible = False
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
                        self.check_one_after_another()
                        discard_deck.add_to_top(discarded2)

                        discarded2.effect2 == "Attack"
                        reactions_possible = False
                        return(discarded2)

                elif self.hand_cards.contents[card_index].effect == "Attack":
                    discarded = self.hand_cards.contents.pop(card_index)
                    self.check_one_after_another()
                    discard_deck.add_to_top(discarded)
                    discarded.effect2 = "Attack"
                    reactions_possible = False
                    return(discarded)

            elif response_required == "Defend" and card_played.effect2 == "Rain of Arrows":

                options_str = self.hand_cards.list_cards()
                options_str.append(
                    Separator("--------------------Other--------------------"))
                if self.check_impetus(player_index, "Check"):
                    options_str.append(" Character Ability >> Impetus")
                options_str.append("Do nothing.")

                question = [
                    {
                        'type': 'list',
                        'name': 'Selected',
                        'message': f"{self.character}: {players[player_index].character} has activated RAIN OF ARROWS; please choose a response (a DEFEND card or do nothing)!",
                        'choices': options_str,
                        'filter': lambda card: options_str.index(card)
                    },
                ]
                answer = prompt(question, style=custom_style_2)
                card_index = answer.get('Selected')
                if options_str[card_index] == "Do nothing.":
                    reactions_possible = False
                    return(0)

                elif options_str[card_index] == " Character Ability >> Impetus":
                    discarded = self.check_impetus(player_index, "Activate")
                    if discarded != None:
                        discarded.effect2 = "Defend"
                        reactions_possible = False
                        return(discarded)

                elif self.hand_cards.contents[card_index].effect == "Defend":
                    discarded = self.hand_cards.contents.pop(card_index)
                    self.check_one_after_another()
                    discard_deck.add_to_top(discarded)
                    discarded.effect2 = "Defend"
                    reactions_possible = False
                    return(discarded)

            elif response_required == "Attack" and card_played.effect2 == "Duel":
                self.check_ardour(card_played)

                options_str = self.hand_cards.list_cards()
                options_str.append(
                    Separator("--------------------Other--------------------"))
                if self.activate_warrior_saint("Check"):
                    options_str.append(" Character Ability >> Warrior Saint")
                if self.check_weapon_serpent_spear("Check"):
                    options_str.append(" Weapon Ability >> Serpent Spear")
                options_str.append("Do nothing.")

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
                    reactions_possible = False
                    return True

                elif options_str[card_index] == " Character Ability >> Warrior Saint":
                    discarded = self.activate_warrior_saint("Reaction")
                    duel_won = players[player_index].use_reaction_effect(
                        "Attack", card_played, reacting_player_index, player_index)
                    if duel_won:
                        reactions_possible = False
                        return False
                    else:
                        reactions_possible = False
                        return True

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
                        self.check_one_after_another()
                        discard_deck.add_to_top(discarded2)
                        duel_won = players[player_index].use_reaction_effect(
                            "Attack", card_played, reacting_player_index, player_index)
                        if duel_won:
                            reactions_possible = False
                            return False
                        else:
                            reactions_possible = False
                            return True

                elif self.hand_cards.contents[card_index].effect == "Attack":
                    discarded = self.hand_cards.contents.pop(card_index)
                    self.check_one_after_another()
                    discard_deck.add_to_top(discarded)
                    discarded.effect2 = "Attack"
                    duel_won = players[player_index].use_reaction_effect(
                        "Attack", card_played, reacting_player_index, player_index)
                    if duel_won:
                        reactions_possible = False
                        return False
                    else:
                        reactions_possible = False
                        return True

    def discard_from_equip_or_hand(self, num=1):
        while num > 0:
            options_str = self.create_str_nonblind_menu()
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
            if discarded_index <= len(self.hand_cards.contents):
                card = self.hand_cards.contents.pop(discarded_index - 1)
                discard_deck.add_to_top(card)
                self.check_one_after_another()

            # Check if equipment-card
            else:
                if discarded_index == (len(self.hand_cards.contents) + 2):
                    card = self.equipment_weapon.pop()
                    discard_deck.add_to_top(card)
                    self.weapon_range = 1
                    print(
                        f"{self.character} has discarded {card} from their weapon-slot.")

                if discarded_index == (len(self.hand_cards.contents) + 3):
                    card = self.equipment_armor.pop()
                    discard_deck.add_to_top(card)
                    print(
                        f"{self.character} has discarded {card} from their armor-slot.")

                if discarded_index == (len(self.hand_cards.contents) + 4):
                    card = self.equipment_offensive_horse.pop()
                    discard_deck.add_to_top(card)
                    print(
                        f"{self.character} has discarded {card} from their horse-slot.")

                if discarded_index == (len(self.hand_cards.contents) + 5):
                    card = self.equipment_defensive_horse.pop()
                    discard_deck.add_to_top(card)
                    print(
                        f"{self.character} has discarded {card} from their horse-slot.")
                self.check_warrior_woman()
            num -= 1

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
            self.check_one_after_another()
        if death:
            print(
                f"{self.character} discarded {cards_discarded} card(s) upon their death.")
            for player in players:
                if player != "Placeholder":
                    player.check_unnatural_death(cards_discarded)
            while len(self.pending_judgements) > 0:
                discard_deck.add_to_top(self.pending_judgements.pop())

# Ability checks
    def check_ardour(self, card, source_player_index=0):
        # "Ardour: Whenever you use or become the target of any DUEL or red-suited ATTACK cards, you can draw a card."
        if (self.character_ability1.startswith("Ardour:") or self.character_ability3.startswith("Ardour:")):
            if players[source_player_index].check_beauty(card):
                if (card.effect == "Duel") or (card.effect == "Attack" and (card.suit == "Spades" or card.suit == "Hearts" or card.suit == "Diamonds")):
                    print(
                        f"  >> Character Ability: Ardour; {self.character} used or was target of {card} (a DUEL or red-suited ATTACK). He draws a card.")
                    self.hand_cards.draw(main_deck, 1, False)
            if (card.effect == "Duel") or (card.effect == "Attack" and (card.suit == "Hearts" or card.suit == "Diamonds")):
                print(
                    f"  >> Character Ability: Ardour; {self.character} used or was target of {card} (a DUEL or red-suited ATTACK). He draws a card.")
                self.hand_cards.draw(main_deck, 1, False)

    def check_backstab(self, discarded, discarded2=None, selected_index=0):
        # "Backstab: Whenever you use an ATTACK to cause damage to a player within your physical range, you can flip a judgement card. If the judgement is not HEARTS, no damage is caused, and instead you cause the target to reduce their maximum health by 1."
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
                question = [
                    {
                        'type': 'list',
                        'name': 'Selected',
                        'message': f'{self.character}: Choose to activate Backstab against {players[selected_index].character}, causing you to flip a judgement; if not HEARTS, the attack will instead reduce their maximum health by 1.',
                        'choices': ['Yes', 'No'],
                    },
                ]
                answer = prompt(question, style=custom_style_2)
                if answer.get('Selected') == 'Yes':
                    print(
                        f"  >> Character Ability: Backstab; {self.character} has activated Backstab, forcing a judgement card to be flipped. If not HEARTS, {players[selected_index].character} loses a maximum health instead of a health.")
                    main_deck.check_if_empty(main_deck, discard_deck)
                    main_deck.discard_from_deck()
                    judgement_card = discard_deck.contents[0]
                    print(f"{self.character} flipped a {judgement_card}.")
                    judgement_card = check_judgement_tinkering(
                        judgement_card, user_index)
                    if judgement_card.suit == "Spades" or judgement_card.suit == "Clubs" or judgement_card.suit == "Diamonds":
                        players[selected_index].max_health -= 1
                        if players[selected_index].current_health > players[selected_index].max_health:
                            players[selected_index].current_health -= 1
                        print(
                            f"{self.character}'s judgement card is a {judgement_card} and therefore {players[selected_index].character} loses maximum health instead. ({players[selected_index].current_health}/{players[selected_index].max_health} HP remaining)")
                        for player_index, player in enumerate(players):
                            if player.current_health < 1:
                                players[player_index].check_brink_of_death_loop(
                                    player_index, 0)

                    if judgement_card.suit == "Hearts":
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

                            self.check_lament(user_index, selected_index)
                            players[selected_index].check_eternal_loyalty(
                                damage_dealt)
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
            question = [
                {
                    'type': 'list',
                    'name': 'Selected',
                    'message': f'{self.character}: Choose to activate Bare-chested, and draw one less card; if yes, all ATTACK or DUEL cards will do increased damage?',
                    'choices': ['Yes', 'No'],
                },
            ]

            answer = prompt(question, style=custom_style_2)
            if answer.get('Selected') == 'Yes':
                print(
                    f"  >> Character Ability: Bare-chested; {self.character} has activated Bare-chested, drawing one card only, and all their ATTACK and DUEL cards will do increased damage for this turn.")
                self.used_bare_chested = True
                return True

    def check_beauty(self, card):
        # "Beauty: All of your SPADES will be regarded as HEARTS."
        if (self.character_ability2.startswith("Beauty:") or self.character_ability3.startswith("Beauty:")):
            if card.suit == "Spades":
                print(
                    f"  >> Character Ability: Beauty; {self.character}'s SPADES are regarded as HEARTS.")
                return True
        return False

    def check_behind_the_curtain(self, card, beauty=False):
        # "Behind the Curtain: You cannot become the target of any black-suited tool cards."
        if self.character_ability3.startswith("Behind the Curtain:"):
            if card.suit == "Spades" or card.suit == "Clubs":
                if card.effect2 == "Barbarians" or card.effect2 == "Rain of Arrows" or card.effect2 == "Coerce" or card.effect2 == "Dismantle" or card.effect2 == "Duel" or card.effect2 == "Steal" or card.effect2 == "Acedia" or card.effect2 == "Lightning" or card.effect2 == "Rations Depleted":
                    print(
                        f"  >> Character Ability: Behind the Curtain; {self.character} is immune to the effects of {card} as it is a BLACK tool card.")
                    return True
            if beauty and card.suit == "Clubs":
                if card.effect2 == "Barbarians" or card.effect2 == "Rain of Arrows" or card.effect2 == "Coerce" or card.effect2 == "Dismantle" or card.effect2 == "Duel" or card.effect2 == "Steal" or card.effect2 == "Acedia" or card.effect2 == "Lightning" or card.effect2 == "Rations Depleted":
                    print(
                        f"  >> Character Ability: Behind the Curtain; {self.character} is immune to the effects of {card} as it is a BLACK tool card.")
                    return True
        return False

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
                question = [
                    {
                        'type': 'list',
                        'name': 'Selected',
                        'message': f'{self.character}: Choose to activate Burning Heart (Single-Use), and swap role cards with {players[dying_player_index].character}?',
                        'choices': ['Yes', 'No'],
                    },
                ]
                answer = prompt(question, style=custom_style_2)
                if answer.get('Selected') == 'Yes':
                    self.awakened = True
                    self.role, players[dying_player_index].role = players[dying_player_index].role, self.role
                    self.character_ability2 = "Burning Heart (INACTIVE Ability): When you kill another character, you can exchange role cards with the player you just killed. You cannot activate this ability if you are the emperor, or just killed the emperor."
                    print(
                        f"  >> Character Ability: Burning Heart; {self.character} has swapped role cards with {players[dying_player_index]}")

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

    def check_dark_sorcery(self, judgement_card):
        # "Dark Sorcery: You can exchange the judgement card of any player before it takes effect, with any of your CLUBS or SPADES, either on-hand or equipped."
        if (self.character_ability2.startswith("Dark Sorcery:") or self.character_ability3.startswith("Dark Sorcery:")):
            cards_discardable = (len(self.hand_cards.contents) + len(self.equipment_weapon) + len(
                self.equipment_armor) + len(self.equipment_offensive_horse) + len(self.equipment_defensive_horse))
            if cards_discardable > 0:
                print(' ')
                question = [
                    {
                        'type': 'list',
                        'name': 'Selected',
                        'message': f'{self.character}: Choose to activate Dark Sorcery, and exchange the current judgement card: {judgement_card}, with one of your SPADES or CLUBS?',
                        'choices': ['Yes', 'No'],
                    },
                ]
                answer = prompt(question, style=custom_style_2)
                if answer.get('Selected') == 'No':
                    return [False]
                if answer.get('Selected') == 'Yes':

                    usable_cards = []
                    for card in self.hand_cards.contents:
                        if card.suit == "Spades" or card.suit == "Clubs":
                            usable_cards.append(card)
                    for card in self.equipment_weapon:
                        if card.suit == "Spades" or card.suit == "Clubs":
                            usable_cards.append(card)
                    for card in self.equipment_armor:
                        if card.suit == "Spades" or card.suit == "Clubs":
                            usable_cards.append(card)
                    for card in self.equipment_offensive_horse:
                        if card.suit == "Spades" or card.suit == "Clubs":
                            usable_cards.append(card)
                    for card in self.equipment_defensive_horse:
                        if card.suit == "Spades" or card.suit == "Clubs":
                            usable_cards.append(card)

                    if len(usable_cards) < 1:
                        print(
                            f"{self.character}: You cannot use this ability as you have no black-suited cards.")
                        return [False]

                    else:
                        options_str = self.create_str_nonblind_menu()
                        options_str.append(
                            Separator("--------------------Other--------------------"))
                        options_str.append("Cancel ability.")

                        question = [
                            {
                                'type': 'list',
                                'name': 'Selected',
                                'message': f'{self.character}: Please select a new judgement card to exchange with {judgement_card}:',
                                'choices': options_str,
                                'filter': lambda card: options_str.index(card)
                            },
                        ]
                        answer = prompt(question, style=custom_style_2)
                        discarded_index = answer.get('Selected')
                        if options_str[discarded_index] == "Cancel ability.":
                            return [False]

                        # Check if hand-card
                        if discarded_index <= len(self.hand_cards.contents):
                            new_judgement_card = self.hand_cards.contents[discarded_index - 1]
                            if new_judgement_card.suit == "Spades" or new_judgement_card.suit == "Clubs":
                                new_judgement_card = self.hand_cards.contents.pop(
                                    discarded_index - 1)
                                discard_deck.add_to_top(new_judgement_card)
                                print(
                                    f"  >> Character Ability: Dark Sorcery; {self.character} has exchanged the judgement card: {judgement_card} with {new_judgement_card} from their hand!")
                                return [True, new_judgement_card]
                            else:
                                print(
                                    f"{self.character}: You can only exchange SPADES or CLUBS when using Dark Sorcery.")
                                return self.check_dark_sorcery(judgement_card)

                        # Check if equipment-card
                        else:
                            if discarded_index == (len(self.hand_cards.contents) + 2):
                                if self.equipment_weapon[0].suit == "Spades" or self.equipment_weapon[0] == "Clubs":
                                    new_judgement_card = self.equipment_weapon.pop()
                                    discard_deck.add_to_top(new_judgement_card)
                                    self.weapon_range = 1
                                    print(
                                        f"  >> Character Ability: Dark Sorcery; {self.character} has exchanged the judgement card: {judgement_card} with {new_judgement_card} from their weapon-slot!")
                                    return [True, new_judgement_card]
                                else:
                                    print(
                                        f"{self.character}: You can only exchange SPADES or CLUBS when using Dark Sorcery.")
                                    return self.check_dark_sorcery(judgement_card)

                            if discarded_index == (len(self.hand_cards.contents) + 3):
                                if self.equipment_armor[0].suit == "Spades" or self.equipment_armor[0] == "Clubs":
                                    new_judgement_card = self.equipment_armor.pop()
                                    discard_deck.add_to_top(new_judgement_card)
                                    print(
                                        f"  >> Character Ability: Dark Sorcery; {self.character} has exchanged the judgement card: {judgement_card} with {new_judgement_card} from their armor-slot!")
                                    return [True, new_judgement_card]
                                else:
                                    print(
                                        f"{self.character}: You can only exchange SPADES or CLUBS when using Dark Sorcery.")
                                    return self.check_dark_sorcery(judgement_card)

                            if discarded_index == (len(self.hand_cards.contents) + 4):
                                if self.equipment_offensive_horse[0].suit == "Spades" or self.equipment_offensive_horse[0] == "Clubs":
                                    new_judgement_card = self.equipment_offensive_horse.pop()
                                    discard_deck.add_to_top(new_judgement_card)
                                    print(
                                        f"  >> Character Ability: Dark Sorcery; {self.character} has exchanged the judgement card: {judgement_card} with {new_judgement_card} from their horse-slot!")
                                    return [True, new_judgement_card]
                                else:
                                    print(
                                        f"{self.character}: You can only exchange SPADES or CLUBS when using Dark Sorcery.")
                                    return self.check_dark_sorcery(judgement_card)

                            if discarded_index == (len(self.hand_cards.contents) + 5):
                                if self.equipment_defensive_horse[0].suit == "Spades" or self.equipment_defensive_horse[0].suit == "Clubs":
                                    new_judgement_card = self.equipment_defensive_horse.pop()
                                    discard_deck.add_to_top(new_judgement_card)
                                    print(
                                        f"  >> Character Ability: Dark Sorcery; {self.character} has exchanged the judgement card: {judgement_card} with {new_judgement_card} from their horse-slot!")
                                    return [True, new_judgement_card]
                                else:
                                    print(
                                        f"{self.character}: You can only exchange SPADES or CLUBS when using Dark Sorcery.")
                                    return self.check_dark_sorcery(judgement_card)
            else:
                return [False]
        return [False]

    def check_dashing_hero(self):
        # "Dashing Hero: Draw an extra card at the start of your turn."
        if (self.character_ability1.startswith("Dashing Hero:") or self.character_ability2.startswith("Dashing Hero:") or self.character_ability3.startswith("Dashing Hero:") or self.character_ability4.startswith("Dashing Hero:") or self.character_ability1.startswith("Dashing Hero:")):
            print(
                f"  >> Character Ability: Dashing Hero; {self.character} draws an extra card from the deck (total of three) in their drawing phase.")
            return True

    def check_deplete_karma(self, damage_dealt, source_player_index=None, target_player_index=None):
        # "Deplete Karma: Whenever you are damaged by another player whose health level is greater or equal to your own, you can discard a red-suited hand-card to reduce the damage by one. If you damage another player whose health is greater than or equal to your own, you can discard black-suited hand-card to increase the damage by one."
        if (self.character_ability1.startswith("Deplete Karma:") or self.character_ability3.startswith("Deplete Karma:")):
            if source_player_index != None:
                if players[source_player_index].current_health >= self.current_health:
                    question = [
                        {
                            'type': 'list',
                            'name': 'Selected',
                            'message': f'{self.character}: Choose to activate Deplete Karma, discarding a red card, and reducing your incoming damage from {players[source_player_index].character} by one?',
                            'choices': ['Yes', 'No'],
                        },
                    ]
                    answer = prompt(question, style=custom_style_2)
                    if answer.get('Selected') == 'Yes':
                        # Discard red to reduce by one
                        cards_discardable = []
                        for card in self.hand_cards.contents:
                            if card.suit == "Hearts" or card.suit == "Diamonds":
                                cards_discardable.append(card)

                        if len(cards_discardable) < 1:
                            print(
                                f"{self.character}: You cannot activate Deplete Karma as you have no red-cards in your hand.")

                        else:
                            options = self.create_str_nonblind_menu(True)
                            options.append(
                                Separator("--------------------Other--------------------"))
                            options.append("Cancel ability.")

                            question = [
                                {
                                    'type': 'list',
                                    'name': 'Selected',
                                    'message': f'{self.character}: Please select any RED card to discard for Deplete Karma!',
                                    'choices': options,
                                    'filter': lambda card: options.index(card)
                                },
                            ]
                            answer = prompt(question, style=custom_style_2)
                            card_index = answer.get('Selected')
                            if options[card_index] == "Cancel ability.":
                                return [False]

                            else:
                                if self.hand_cards.contents[card_index].suit == "Hearts" or self.hand_cards.contents[card_index].suit == "Diamonds":
                                    card = self.hand_cards.contents.pop(
                                        card_index)
                                    discard_deck.add_to_top(card)
                                    print(
                                        f"  >> Character Ability: Deplete Karma; {self.character} has discarded {card} to reduce the incoming damage by one!")
                                    damage_dealt -= 1
                                    return [True, damage_dealt]

            elif target_player_index != None:
                if players[target_player_index].current_health >= self.current_health:
                    question = [
                        {
                            'type': 'list',
                            'name': 'Selected',
                            'message': f'{self.character}: Choose to activate Deplete Karma, discarding a black card, and increasing your outgoing damage to {players[target_player_index].character} by one?',
                            'choices': ['Yes', 'No'],
                        },
                    ]
                    answer = prompt(question, style=custom_style_2)
                    if answer.get('Selected') == 'Yes':
                        # Discard black to increase by one
                        cards_discardable = []
                        for card in self.hand_cards.contents:
                            if card.suit == "Spades" or card.suit == "Clubs":
                                cards_discardable.append(card)

                        if len(cards_discardable) < 1:
                            print(
                                f"{self.character}: You cannot activate Deplete Karma as you have no black-cards in your hand.")

                        else:
                            options = self.create_str_nonblind_menu(True)
                            options.append(
                                Separator("--------------------Other--------------------"))
                            options.append("Cancel ability.")

                            question = [
                                {
                                    'type': 'list',
                                    'name': 'Selected',
                                    'message': f'{self.character}: Please select any BLACK card to discard for Deplete Karma!',
                                    'choices': options,
                                    'filter': lambda card: options.index(card)
                                },
                            ]
                            answer = prompt(question, style=custom_style_2)
                            card_index = answer.get('Selected')
                            if options[card_index] == "Cancel ability.":
                                return [False]

                            else:
                                if self.hand_cards.contents[card_index].suit == "Spades" or self.hand_cards.contents[card_index].suit == "Clubs":
                                    card = self.hand_cards.contents.pop(
                                        card_index)
                                    discard_deck.add_to_top(card)
                                    print(
                                        f"  >> Character Ability: Deplete Karma; {self.character} has discarded {card} to increase the outgoing damage by one!")
                                    damage_dealt += 1
                                    return [True, damage_dealt]
        return [False]

    def check_devil(self, judgement_card):
        # "Devil: After any judgement has been flipped over, you can immediately discard one of your on-hand or equipped cards to replace the judgement card."
        if (self.character_ability2.startswith("Devil:") or self.character_ability3.startswith("Devil:")):
            cards_discardable = (len(self.hand_cards.contents) + len(self.equipment_weapon) + len(
                self.equipment_armor) + len(self.equipment_offensive_horse) + len(self.equipment_defensive_horse))
            if cards_discardable > 0:
                print(' ')
                question = [
                    {
                        'type': 'list',
                        'name': 'Selected',
                        'message': f'{self.character}: Choose to activate Devil, and change the current judgement card: {judgement_card}?',
                        'choices': ['Yes', 'No'],
                    },
                ]
                answer = prompt(question, style=custom_style_2)
                if answer.get('Selected') == 'No':
                    return [False]
                if answer.get('Selected') == 'Yes':
                    options_str = self.create_str_nonblind_menu()
                    options_str.append(
                        Separator("--------------------Other--------------------"))
                    options_str.append("Cancel ability.")

                    question = [
                        {
                            'type': 'list',
                            'name': 'Selected',
                            'message': f'{self.character}: Please select a new judgement card to replace {judgement_card}:',
                            'choices': options_str,
                            'filter': lambda card: options_str.index(card)
                        },
                    ]
                    answer = prompt(question, style=custom_style_2)
                    discarded_index = answer.get('Selected')
                    if options_str[discarded_index] == "Cancel ability.":
                        return [False]

                    # Check if hand-card
                    if discarded_index <= len(self.hand_cards.contents):
                        new_judgement_card = self.hand_cards.contents.pop(
                            discarded_index - 1)
                        discard_deck.add_to_top(new_judgement_card)
                        print(
                            f"  >> Character Ability: Devil; {self.character} has replaced the judgement card: {judgement_card} with {new_judgement_card}!")
                        return [True, new_judgement_card]

                    # Check if equipment-card
                    else:
                        if discarded_index == (len(self.hand_cards.contents) + 2):
                            new_judgement_card = self.equipment_weapon.pop()
                            discard_deck.add_to_top(new_judgement_card)
                            self.weapon_range = 1
                            print(
                                f"  >> Character Ability: Devil; {self.character} has replaced the judgement card: {judgement_card} with {new_judgement_card}!")
                            return [True, new_judgement_card]

                        if discarded_index == (len(self.hand_cards.contents) + 3):
                            new_judgement_card = self.equipment_armor.pop()
                            discard_deck.add_to_top(new_judgement_card)
                            print(
                                f"  >> Character Ability: Devil; {self.character} has replaced the judgement card: {judgement_card} with {new_judgement_card}!")
                            return [True, new_judgement_card]

                        if discarded_index == (len(self.hand_cards.contents) + 4):
                            new_judgement_card = self.equipment_offensive_horse.pop()
                            discard_deck.add_to_top(new_judgement_card)
                            print(
                                f"  >> Character Ability: Devil; {self.character} has replaced the judgement card: {judgement_card} with {new_judgement_card}!")
                            return [True, new_judgement_card]

                        if discarded_index == (len(self.hand_cards.contents) + 5):
                            new_judgement_card = self.equipment_defensive_horse.pop()
                            discard_deck.add_to_top(new_judgement_card)
                            print(
                                f"  >> Character Ability: Devil; {self.character} has replaced the judgement card: {judgement_card} with {new_judgement_card}!")
                            return [True, new_judgement_card]
            else:
                return [False]
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
                if answer.get('Selected') == 'Lose one maximum-health':
                    self.max_health -= 1
                    if self.current_health > self.max_health:
                        self.current_health -= 1
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

                question = [
                    {
                        'type': 'list',
                        'name': 'Selected',
                        'message': f'{self.character}: Choose to activate Displacement, and redirect the ATTACK from {players[source_player_index].character}?',
                        'choices': ['Yes', 'No'],
                    },
                ]
                answer = prompt(question, style=custom_style_2)
                if answer.get('Selected') == 'No':
                    return [False]

                options_str = self.create_str_nonblind_menu()
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
                    if discarded_index == (len(self.hand_cards.contents) + 2):
                        self.weapon_range = 1
                    if discarded_index == (len(self.hand_cards.contents) + 4):
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
                            if discarded_index == (len(self.hand_cards.contents) + 2):
                                self.weapon_range = self.equipment_weapon[0].weapon_range
                            if discarded_index == (len(self.hand_cards.contents) + 4):
                                self.weapon_range += 1
                            return [False]
                        else:
                            # Check if hand-card
                            if discarded_index <= len(self.hand_cards.contents):
                                card = self.hand_cards.contents.pop(
                                    discarded_index - 1)
                                discard_deck.add_to_top(card)
                                print(
                                    f"  >> Character Ability: Displacement; {self.character} has discarded {card} from their hand to redirect the ATTACK to {players[target_index].character}.")
                                return [True, target_index]

                            # Check if equipment-card
                            else:
                                if discarded_index == (len(self.hand_cards.contents) + 2):
                                    card = self.equipment_weapon.pop()
                                    discard_deck.add_to_top(card)
                                    self.weapon_range = 1
                                    print(
                                        f"  >> Character Ability: Displacement; {self.character} has discarded {card} from their weapon-slot to redirect the ATTACK to {players[target_index].character}.")
                                    return [True, target_index]

                                if discarded_index == (len(self.hand_cards.contents) + 3):
                                    card = self.equipment_armor.pop()
                                    discard_deck.add_to_top(card)
                                    print(
                                        f"  >> Character Ability: Displacement; {self.character} has discarded {card} from their armor-slot to redirect the ATTACK to {players[target_index].character}.")
                                    return [True, target_index]

                                if discarded_index == (len(self.hand_cards.contents) + 4):
                                    card = self.equipment_offensive_horse.pop()
                                    discard_deck.add_to_top(card)
                                    print(
                                        f"  >> Character Ability: Displacement; {self.character} has discarded {card} from their horse-slot to redirect the ATTACK to {players[target_index].character}.")
                                    return [True, target_index]

                                if discarded_index == (len(self.hand_cards.contents) + 5):
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
                question = [
                    {
                        'type': 'list',
                        'name': 'Selected',
                        'message': f'{self.character}: Choose to activate Dual Heroes, and flip (then draw) a judgement; if yes, all cards of the opposite colour can be used as DUEL?',
                        'choices': ['Yes', 'No'],
                    },
                ]
                answer = prompt(question, style=custom_style_2)
                if answer.get('Selected') == 'Yes':
                    print(
                        f"  >> Character Ability: Dual Heroes; {self.character} has/have activated Dual Heroes, flipping a judgement, then adding it to their hand.")
                    main_deck.check_if_empty(main_deck, discard_deck)
                    main_deck.discard_from_deck()
                    judgement_card = discard_deck.contents[0]
                    print(f"{self.character} flipped a {judgement_card}.")
                    judgement_card = check_judgement_tinkering(
                        judgement_card, user_index)
                    self.hand_cards.draw(discard_deck, 1, False)

                    if judgement_card.suit == "Spades" or judgement_card.suit == "Clubs":
                        self.used_dual_heroes = "Red"
                        print(
                            f"  >> Character Ability: Dual Heroes; {self.character} drew {judgement_card} and can use any on-hand red cards as DUEL!")
                        return True

                    if judgement_card.suit == "Hearts" or judgement_card.suit == "Diamonds":
                        self.used_dual_heroes = "Black"
                        print(
                            f"  >> Character Ability: Dual Heroes; {self.character} drew {judgement_card} and can use any on-hand black cards as DUEL!")
                        return True

            if phase == "Activate":
                if self.used_dual_heroes == "Black":
                    usable_cards = []
                    for card in self.hand_cards.contents:
                        if card.suit == "Spades" or card.suit == "Clubs":
                            usable_cards.append(card)
                    if len(usable_cards) > 0:
                        options = self.create_str_nonblind_menu(True)
                        options.append(
                            Separator("--------------------Other--------------------"))
                        options.append("Cancel ability.")

                        question = [
                            {
                                'type': 'list',
                                'name': 'Selected',
                                'message': f'{self.character}: Please select any BLACK card to use as DUEL!',
                                'choices': options,
                                'filter': lambda card: options.index(card)
                            },
                        ]
                        answer = prompt(question, style=custom_style_2)
                        card_index = answer.get('Selected')

                        if options[card_index] == "Cancel ability.":
                            return (' ')
                        else:
                            if self.hand_cards.contents[card_index].suit == "Spades" or self.hand_cards.contents[card_index].suit == "Clubs":
                                card = self.hand_cards.contents.pop(card_index)
                                discard_deck.add_to_top(card)
                                card.effect2 = "Duel"
                                if not self.use_card_effect("Special", card):
                                    self.hand_cards.draw(
                                        discard_deck, 1, False)
                                    print(
                                        f"{self.character} cancelled using their effect, and {card} was returned.")
                            else:
                                print(
                                    f"{self.hand_cards.contents[card_index]} cannot be used as it is RED-suited!")

                if self.used_dual_heroes == "Red":
                    usable_cards = []
                    for card in self.hand_cards.contents:
                        if card.suit == "Hearts" or card.suit == "Diamonds":
                            usable_cards.append(card)
                    if len(usable_cards) > 0:
                        options = self.create_str_nonblind_menu(True)
                        options.append(
                            Separator("--------------------Other--------------------"))
                        options.append("Cancel ability.")

                        question = [
                            {
                                'type': 'list',
                                'name': 'Selected',
                                'message': f'{self.character}: Please select any RED card to use as DUEL!',
                                'choices': options,
                                'filter': lambda card: options.index(card)
                            },
                        ]
                        answer = prompt(question, style=custom_style_2)
                        card_index = answer.get('Selected')

                        if options[card_index] == "Cancel ability.":
                            return (' ')
                        else:
                            if self.hand_cards.contents[card_index].suit == "Hearts" or self.hand_cards.contents[card_index].suit == "Diamonds":
                                card = self.hand_cards.contents.pop(card_index)
                                discard_deck.add_to_top(card)
                                card.effect2 = "Duel"
                                if not self.use_card_effect("Special", card):
                                    self.hand_cards.draw(
                                        discard_deck, 1, False)
                                    print(
                                        f"{self.character} cancelled using their effect, and {card} was returned.")
                            else:
                                print(
                                    f"{self.hand_cards.contents[card_index]} cannot be used as it is BLACK-suited!")

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

    def check_eternal_loyalty(self, damage_dealt):
        # "Eternal Loyalty: For every one unit of damage you suffer, you can allow any player of your choice (including yourself) to replenish that player’s on-hand cards to their maximum health level."
        if (self.character_ability2.startswith("Eternal Loyalty:") or self.character_ability3.startswith("Eternal Loyalty:")):
            while damage_dealt > 0:
                question = [
                    {
                        'type': 'list',
                        'name': 'Selected',
                        'message': f"{self.character}: Choose to activate Eternal Loyalty, and refill a players' hand-limit to full? ({damage_dealt} hand(s) can be refilled)?",
                        'choices': ['Yes', 'No'],
                    },
                ]
                answer = prompt(question, style=custom_style_2)
                if answer.get('Selected') == 'No':
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
                            difference, False)
                        print(
                            f"  >> Character Ability: Eternal Loyalty; {self.character} has refilled {options[selected_index]}'s hand to their maximum health limit! (+{difference} cards)")
                        damage_dealt -= 1
                else:
                    print(
                        f"{self.character}: There are no players that you can use this ability against.")

    def check_exile(self):
        # "Exile: Every instance that you suffer damage, you can force any other player to draw X number of cards (X being the units of health you have missing from your maximum after damage). By doing so the targeted player will have to flip their character card. Flipped character cards must miss their next turn."
        if (self.character_ability2.startswith("Exile:") or self.character_ability3.startswith("Exile:")):

            for player_index, player in players:
                if (player.character_ability2.startswith("Exile:") or player.character_ability3.startswith("Exile:")):
                    user_index = player_index
                    break

            question = [
                {
                    'type': 'list',
                    'name': 'Selected',
                    'message': f'{self.character}: Choose to activate Exile, making someone miss their next turn, and draw {self.max_health - self.current_health} cards?',
                    'choices': ['Yes', 'No'],
                },
            ]
            answer = prompt(question, style=custom_style_2)
            if answer.get('Selected') == 'Yes':

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
        # "Eye for an Eye: For every instance that you suffer damage, you can flip a judgement card. If the judgement is not HEARTS, the character that damaged you must choose between the following options; lose one unit of health, or discard any two on-hand cards."
        if (self.character_ability1.startswith("Eye for an Eye:") or self.character_ability3.startswith("Eye for an Eye:")):

            user_index = 0
            for player_index, player in enumerate(players):
                if (player.character_ability1.startswith("Eye for an Eye:") or player.character_ability3.startswith("Eye for an Eye:")):
                    user_index = player_index
                    break

            if mode == "Activate":
                print(' ')
                question = [
                    {
                        'type': 'list',
                        'name': 'Selected',
                        'message': f'{self.character}: Choose to activate Eye for an Eye, and force {players[source_player_index].character} to either take one damage or discard two hand-cards?',
                        'choices': ['Yes', 'No'],
                    },
                ]
                answer = prompt(question, style=custom_style_2)
                if answer.get('Selected') == 'Yes':
                    print(
                        f"  >> Character Ability: Eye for an Eye; {self.character} is forcing a judgement card to be flipped. If not HEARTS, {players[source_player_index].character} must either take one damage or discard two hand-cards.")
                main_deck.check_if_empty(main_deck, discard_deck)
                main_deck.discard_from_deck()
                judgement_card = discard_deck.contents[0]
                print(f"{self.character} flipped a {judgement_card}.")
                judgement_card = check_judgement_tinkering(
                    judgement_card, user_index)
                if judgement_card.suit != "Hearts":
                    print(
                        f"{self.character}'s judgement card is a {judgement_card} and therefore {players[source_player_index].character} must suffer one damage or discard two hand-cards.")
                    players[source_player_index].check_eye_for_an_eye(
                        user_index, "Reaction")
                if judgement_card.suit == "Hearts":
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
                        if player.current_health < 1:
                            if players[player_index].check_brink_of_death_loop(player_index, user_index) == "Break":
                                return "Break"
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
                self.check_one_after_another()

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
                        self.character_ability3 = "Exalt (Ruler Ability): Whenever any Wei character (other than yourself) makes a judgement, if the judgement card that takes effect is either CLUBS or SPADES, that character can choose to let you draw one card from the deck."
                    if player.character == 'Sun Ce':
                        self.character_ability3 = "Hegemony (Ruler Ability): During the action phase of any other Wu characters, they can choose to COMPETE against you; you both show a card simultaneously, and whoever has the higher value wins. If they do not win, you can take both cards used. After your awakening ability activates, you are able to refuse COMPETE effects."
                    if player.character == 'Sun Quan':
                        self.character_ability3 = "Rescued (Ruler Ability): Whenever another member of Wu uses a PEACH to save you from the brink of death, it provides you with two units of health."
                    if player.character == 'Dong Zhuo':
                        self.character_ability3 = "Tyrant (Ruler Ability): Whenever another Hero character causes damage to any other player, you can flip a judgement card. If the judgement card is of the suit SPADES, you can regain one unit of health."
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
                        self.character_ability4 = "Exalt (Ruler Ability): Whenever any Wei character (other than yourself) makes a judgement, if the judgement card that takes effect is either CLUBS or SPADES, that character can choose to let you draw one card from the deck."
                    if player.character == 'Sun Ce':
                        self.character_ability4 = "Hegemony (Ruler Ability): During the action phase of any other Wu characters, they can choose to COMPETE against you; you both show a card simultaneously, and whoever has the higher value wins. If they do not win, you can take both cards used. After your awakening ability activates, you are able to refuse COMPETE effects."
                    if player.character == 'Sun Quan':
                        self.character_ability4 = "Rescued (Ruler Ability): Whenever another member of Wu uses a PEACH to save you from the brink of death, it provides you with two units of health."
                    if player.character == 'Dong Zhuo':
                        self.character_ability4 = "Tyrant (Ruler Ability): Whenever another Hero character causes damage to any other player, you can flip a judgement card. If the judgement card is of the suit SPADES, you can regain one unit of health."
                    if player.character == 'Yuan Shao':
                        self.character_ability4 = "Bloodline (Ruler Ability): Your maximum hand-limit is increased by two for each other Hero character still alive."
                    if player.character == 'Zhang Jiao':
                        self.character_ability4 = "Amber Sky (Ruler Ability): All Hero characters can give you a DEFEND or LIGHTNING card during their individual turns."

    def check_fantasy(self, damage_dealt, source_player_index=0):
        # "Fantasy: Whenever you recieve damage, you can choose to pass the damage onto any other player by discarding an on-hand card that has the suit HEARTS. The victim that recieves the damage gets to draw X number of cards from the deck, X being the amount of health missing from the maximum level after damage."
        if (self.character_ability1.startswith("Fantasy:") or self.character_ability3.startswith("Fantasy:")):

            user_index = 0
            for player_index, player in enumerate(players):
                if (player.character_ability1.startswith("Fantasy:") or self.character_ability3.startswith("Fantasy:")):
                    user_index = player_index

            question = [
                {
                    'type': 'list',
                    'name': 'Selected',
                    'message': f'{self.character}: Discard a HEARTS card to activate Fantasy, and redirect the incoming damage to another player? They, then draw X cards; X being the number of health points they have missing after the damage is passed.',
                    'choices': ['Yes', 'No'],
                },
            ]
            answer = prompt(question, style=custom_style_2)
            if answer.get('Selected') == 'Yes':
                options_str = self.create_str_nonblind_menu(True)
                options_str.append(
                    Separator("--------------------Other--------------------"))
                options_str.append("Cancel ability.")

                question = [
                    {
                        'type': 'list',
                        'name': 'Selected',
                        'message': f'{self.character}: Please select a card of suit HEARTS:',
                        'choices': options_str,
                        'filter': lambda card: options_str.index(card)
                    },
                ]
                answer = prompt(question, style=custom_style_2)
                discarded_index = answer.get('Selected')
                if options_str[discarded_index] == "Cancel ability.":
                    return [False]

                discarded = self.hand_cards.contents[discarded_index]
                if (self.check_beauty(discarded) and (discarded.suit == "Spades" or discarded.suit == "Hearts")) or (discarded.suit == "Hearts"):
                    targets_str = []
                    for player in players:
                        targets_str.append(
                            str(player)+f" - ({player.current_health}/{player.max_health} HP remaining)")
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
                            'message': f'{self.character}: Please select a character to target with Fantasy:',
                            'choices': targets_str,
                            'filter': lambda player: targets_str.index(player)
                        },
                    ]
                    answer = prompt(question, style=custom_style_2)
                    selected = answer.get('Selected')
                    if targets_str[selected] == "Cancel ability.":
                        return [False]
                    else:
                        discarded = self.hand_cards.contents.pop(
                            discarded_index)
                        discard_deck.add_to_top(discarded)
                        print(
                            f"  >> Character Ability: Fantasy; {self.character} redirected {damage_dealt} damage to {players[selected].character}!")
                        return [True, selected]
        return [False]

    def check_fearsome_advance(self, discarded, selected_index=0):
        # "Fearsome Advance: Whenever your ATTACK is evaded by a DEFEND, you can discard one of your opponents cards (on-hand or equipped)."
        if (self.character_ability2.startswith("Fearsome Advance:") or self.character_ability3.startswith("Fearsome Advance:")):
            cards_discardable = (len(players[selected_index].hand_cards.contents) + len(players[selected_index].equipment_weapon) + len(
                players[selected_index].equipment_armor) + len(players[selected_index].equipment_offensive_horse) + len(players[selected_index].equipment_defensive_horse))
            if cards_discardable > 0:
                question = [
                    {
                        'type': 'list',
                        'name': 'Selected',
                        'message': f'{self.character}: Choose to activate Fearsome Advance against {players[selected_index].character}, causing you to discard one of their cards?',
                        'choices': ['Yes', 'No'],
                    },
                ]
                answer = prompt(question, style=custom_style_2)
                if answer.get('Selected') == 'Yes':
                    print(
                        f"  >> Character Ability: Fearsome Advance; {self.character} has activated Fearsome Advance, forcing {players[selected_index].character} to discard a card.")

                    options_str = players[selected_index].create_str_semiblind_menu(
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
                            card_discarded_index - 1)
                        discard_deck.add_to_top(card_discarded)
                        print(
                            f"  >> Character Ability: Fearsome Advance; {self.character} has made {players[selected_index].character} discard {card_discarded} from their hand.")
                        players[selected_index].check_one_after_another()

                    # Check if equipment-card
                    else:
                        if card_discarded_index == (len(players[selected_index].hand_cards.contents) + 2):
                            card_discarded = players[selected_index].equipment_weapon.pop(
                            )
                            discard_deck.add_to_top(card_discarded)
                            players[selected_index].weapon_range = 1
                            print(
                                f"  >> Character Ability: Fearsome Advance; {self.character} has made {players[selected_index].character} discard {card_discarded} from their weapon-slot.")
                            players[selected_index].check_warrior_woman()

                        elif card_discarded_index == (len(players[selected_index].hand_cards.contents) + 3):
                            card_discarded = players[selected_index].equipment_armor.pop(
                            )
                            discard_deck.add_to_top(card_discarded)
                            print(
                                f"  >> Character Ability: Fearsome Advance; {self.character} has made {players[selected_index].character} discard {card_discarded} from their armor-slot.")
                            players[selected_index].check_warrior_woman()

                        elif card_discarded_index == (len(players[selected_index].hand_cards.contents) + 4):
                            card_discarded = players[selected_index].equipment_offensive_horse.pop(
                            )
                            discard_deck.add_to_top(card_discarded)
                            print(
                                f"  >> Character Ability: Fearsome Advance; {self.character} has made {players[selected_index].character} discard {card_discarded} from their horse-slot.")
                            players[selected_index].check_warrior_woman()

                        elif card_discarded_index == (len(players[selected_index].hand_cards.contents) + 5):
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
                question = [
                    {
                        'type': 'list',
                        'name': 'Selected',
                        'message': f'{self.character}: Choose to activate Fearsome Archer against {players[selected_index].character}, and make your attack impossible to dodge?',
                        'choices': ['Yes', 'No'],
                    },
                ]
                answer = prompt(question, style=custom_style_2)
                if answer.get('Selected') == 'Yes':
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
                        self.check_lament(user_index, selected_index)
                        players[selected_index].check_eternal_loyalty(
                            damage_dealt)
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

    def check_first_aid(self, dying_player_index=0, mode="Check"):
        # "First Aid: Outside of your turn, you can use any red-suited cards (on-hand or equipped) as a PEACH."
        if (self.character_ability1.startswith("First Aid:") or self.character_ability3.startswith("First Aid:")):
            if mode == "Check":
                return True

            if mode == "Reaction":
                cards_discardable = (len(self.hand_cards.contents) + len(self.equipment_weapon) + len(
                    self.equipment_armor) + len(self.equipment_offensive_horse) + len(self.equipment_defensive_horse))
                if cards_discardable > 0:
                    usable_cards = []
                    for card in self.hand_cards.contents:
                        if card.suit == "Hearts" or card.suit == "Diamonds":
                            usable_cards.append(card)
                    for card in self.equipment_weapon:
                        if card.suit == "Hearts" or card.suit == "Diamonds":
                            usable_cards.append(card)
                    for card in self.equipment_armor:
                        if card.suit == "Hearts" or card.suit == "Diamonds":
                            usable_cards.append(card)
                    for card in self.equipment_offensive_horse:
                        if card.suit == "Hearts" or card.suit == "Diamonds":
                            usable_cards.append(card)
                    for card in self.equipment_defensive_horse:
                        if card.suit == "Hearts" or card.suit == "Diamonds":
                            usable_cards.append(card)

                    if len(usable_cards) < 1:
                        print(
                            f"{self.character}: You cannot use this ability as you have no red-suited cards.")

                    else:
                        options_str = self.create_str_nonblind_menu()
                        options_str.append(
                            Separator("--------------------Other--------------------"))
                        options_str.append("Cancel ability.")
                        options = self.create_actual_menu()

                        question = [
                            {
                                'type': 'list',
                                'name': 'Selected',
                                'message': f'{self.character}: Please select a card to use as PEACH for {players[dying_player_index].character}?',
                                'choices': options_str,
                                'filter': lambda card: options_str.index(card)
                            },
                        ]
                        answer = prompt(question, style=custom_style_2)
                        discarded_index = answer.get('Selected')
                        if options_str[discarded_index] == "Cancel ability.":
                            return (' ')

                        if options[discarded_index].suit == "Hearts" or options[discarded_index].suit == "Diamonds" or options[discarded_index].effect == "Peach":
                            # Check if hand-card
                            if discarded_index <= len(self.hand_cards.contents):
                                card = self.hand_cards.contents.pop(
                                    discarded_index - 1)
                                discard_deck.add_to_top(card)
                                if (card.suit == "Hearts") or (card.suit == "Diamonds"):
                                    print(
                                        f"  >> Character Ability: First Aid; {self.character} has discarded {card} from their hand to use as PEACH.")
                                return True

                            # Check if equipment-card
                            else:
                                if discarded_index == (len(self.hand_cards.contents) + 2):
                                    card = self.equipment_weapon.pop()
                                    discard_deck.add_to_top(card)
                                    self.weapon_range = 1
                                    print(
                                        f"  >> Character Ability: First Aid; {self.character} has discarded {card} from their weapon-slot to use as PEACH.")
                                    return True

                                if discarded_index == (len(self.hand_cards.contents) + 3):
                                    card = self.equipment_armor.pop()
                                    discard_deck.add_to_top(card)
                                    print(
                                        f"  >> Character Ability: First Aid; {self.character} has discarded {card} from their armor-slot to use as PEACH.")
                                    return True

                                if discarded_index == (len(self.hand_cards.contents) + 4):
                                    card = self.equipment_offensive_horse.pop()
                                    discard_deck.add_to_top(card)
                                    print(
                                        f"  >> Character Ability: First Aid; {self.character} has discarded {card} from their horse-slot to use as PEACH.")
                                    return True

                                if discarded_index == (len(self.hand_cards.contents) + 5):
                                    card = self.equipment_defensive_horse.pop()
                                    discard_deck.add_to_top(card)
                                    print(
                                        f"  >> Character Ability: First Aid; {self.character} has discarded {card} from their horse-slot to use as PEACH.")
                                    return True
                        else:
                            print(
                                f"{options[discarded_index]} cannot be used as PEACH as it is NOT red-suited.")

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

    def check_goddess_luo(self):
        # "Goddess Luo: At the beginning of your turn, you flip a judgement card. If the judgement is a black-suited, you may choose to flip another. This process continues until you flip a red-suited card. The red card is discarded and all black-suited cards are added to your hand."
        if (self.character_ability2.startswith("Goddess Luo:") or self.character_ability3.startswith("Goddess Luo")):
            print(
                f"  >> Character Ability: Goddess Luo; {self.character} can flip judgement cards until one is red. All black cards are added to their hand.")
            activated_goddess_luo = True
            cards_drawn = []
            print(' ')
            while activated_goddess_luo:
                question = [
                    {
                        'type': 'list',
                        'name': 'Selected',
                        'message': f'{self.character}: Choose to activate Goddess Luo, and flip another judgement card (currently {len(cards_drawn)})?',
                        'choices': ['Yes', 'No'],
                    },
                ]
                answer = prompt(question, style=custom_style_2)
                if answer.get('Selected') == 'No':
                    activated_goddess_luo = False
                else:
                    main_deck.check_if_empty(main_deck, discard_deck)
                    judgement_card = main_deck.remove_from_top()
                    print(
                        f"{self.character}'s judgement card is a {judgement_card}.")
                    judgement_card = check_judgement_tinkering(
                        judgement_card, 0)
                    if judgement_card.suit == 'Spades' or judgement_card.suit == 'Clubs':
                        cards_drawn.append(judgement_card)
                    else:
                        discard_deck.add_to_top(judgement_card)
                        activated_goddess_luo = False
            if len(cards_drawn) > 0:
                print(
                    f"  >> Character Ability: Goddess Luo; {self.character} adds {len(cards_drawn)} black card(s) to their hand.")
                for card in cards_drawn:
                    self.hand_cards.contents.append(card)

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

    def check_iron_cavalry(self, discarded, discarded2=None, selected_index=0):
        # "Iron Cavalry: Whenever you ATTACK a player, you can flip a judgement card. If it is red, the ATTACK cannot be dodged."
        if (self.character_ability2.startswith("Iron Cavalry:") or self.character_ability3.startswith("Iron Cavalry:")):

            user_index = 0
            for player_index, player in enumerate(players):
                if (player.character_ability2.startswith("Iron Cavalry:") or player.character_ability3.startswith("Iron Cavalry:")):
                    user_index = player_index
                    break

            question = [
                {
                    'type': 'list',
                    'name': 'Selected',
                    'message': f'{self.character}: Choose to activate Iron Cavalry against {players[selected_index].character}, causing you to flip a judgement; if red, the attack is impossible to dodge?',
                    'choices': ['Yes', 'No'],
                },
            ]
            answer = prompt(question, style=custom_style_2)
            if answer.get('Selected') == 'Yes':
                print(
                    f"  >> Character Ability: Iron Cavalry; {self.character} has activated Iron Cavalry, forcing a judgement card to be flipped. If red, {players[selected_index].character} cannot dodge the attack.")
                main_deck.check_if_empty(main_deck, discard_deck)
                main_deck.discard_from_deck()
                judgement_card = discard_deck.contents[0]
                print(f"{self.character} flipped a {judgement_card}.")
                judgement_card = check_judgement_tinkering(
                    judgement_card, user_index)

                if judgement_card.suit == "Diamonds" or judgement_card.suit == "Hearts":
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

                        self.check_lament(user_index, selected_index)
                        players[selected_index].check_eternal_loyalty(
                            damage_dealt)
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

            if mode == "Activate":
                cards_discardable = len(self.hand_cards.contents)
                if cards_discardable > 0:
                    usable_cards = []
                    for card in self.hand_cards.contents:
                        if card.suit == "Spades" or card.suit == "Clubs":
                            usable_cards.append(card)

                    if len(usable_cards) < 1:
                        print(
                            f"{self.character}: You cannot use this ability as you have no black-suited cards in your hand.")

                    else:
                        options_str = get_playing_card_options(self.hand_cards)
                        options_str.append(
                            Separator("--------------------Other--------------------"))
                        options_str.append("Cancel ability.")

                        question = [
                            {
                                'type': 'list',
                                'name': 'Selected',
                                'message': f'{self.character}: Please select a BLACK card to use as a DEFEND from {players[source_player_index].character}?',
                                'choices': options_str,
                                'filter': lambda card: options_str.index(card)
                            },
                        ]
                        answer = prompt(question, style=custom_style_2)
                        discarded_index = answer.get('Selected')
                        if options_str[discarded_index] == "Cancel ability.":
                            return (' ')

                        if self.hand_cards.contents[discarded_index].suit == "Spades" or self.hand_cards.contents[discarded_index].suit == "Clubs" or self.hand_cards.contents[discarded_index].effect == "Defend":
                            # Check if hand-card
                            if discarded_index <= len(self.hand_cards.contents):
                                card = self.hand_cards.contents.pop(
                                    discarded_index)
                                discard_deck.add_to_top(card)
                                if (card.suit == "Spades") or (card.suit == "Clubs"):
                                    print(
                                        f"  >> Character Ability: Impetus; {self.character} has used {card} from their hand as a DEFEND.")
                                return (card)

                        else:
                            print(
                                f"{self.hand_cards.contents[discarded_index]} cannot be used as DEFEND as it is NOT black-suited.")
                            return None

    def check_insanity(self, selected_index=0):
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
                    self.current_health += 1
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
        # "Lament: Whenever any player is damaged by an ATTACK, you can discard any card, on-hand or equipped. The victim must then flip a judgement. If SPADES, the attacker flips their character card. If HEARTS, the victim regains one health. If CLUBS, the attacker discards two cards. If DIAMONDS, the victim draws two cards."
        for user in players:
            if (user.character_ability1.startswith("Lament:") or user.character_ability3.startswith("Lament:")):
                cards_discardable = (len(user.hand_cards.contents) + len(user.equipment_weapon) + len(
                    user.equipment_armor) + len(user.equipment_offensive_horse) + len(user.equipment_defensive_horse))
                if cards_discardable > 0:
                    print(
                        f"If Spades: {players[source_player_index].character} flips their character card.")
                    print(
                        f"If Hearts: {players[targeted_index].character} recovers one health.")
                    print(
                        f"If Clubs: {players[source_player_index].character} discards two cards.")
                    print(
                        f"If Diamonds: {players[targeted_index].character} draws two cards.")
                    question = [
                        {
                            'type': 'list',
                            'name': 'Selected',
                            'message': f'{user.character}: Choose to activate Lament; discard a card and flip a judgement card, triggering one of the above effects?',
                            'choices': ['Yes', 'No'],
                        },
                    ]
                    answer = prompt(question, style=custom_style_2)
                    if answer.get('Selected') == 'Yes':
                        user.discard_from_equip_or_hand()
                        print(
                            f"  >> Character Ability: Lament; {user.character} discarded a card, and will force {players[targeted_index].character} to flip a judgement...")
                        main_deck.discard_from_deck()
                        judgement_card = discard_deck.contents[0]
                        print(
                            f"{players[targeted_index].character} flipped a {judgement_card}.")
                        judgement_card = check_judgement_tinkering(
                            judgement_card, targeted_index)

                        players[targeted_index].check_envy_of_heaven()
                        if players[targeted_index].check_beauty(judgement_card):
                            if judgement_card.suit == "Spades" or judgement_card.suit == "Hearts":
                                if players[targeted_index].current_health < players[targeted_index].max_health:
                                    players[targeted_index].current_health += 1
                                    print(
                                        f"  >> Character Ability: Lament; {user.character} has forced {players[targeted_index].character} to regain one health ({players[targeted_index].current_health}/{players[targeted_index].max_health} HP remaining)!")

                        elif judgement_card.suit == "Spades":
                            players[source_player_index].flipped_char_card = True
                            print(
                                f"  >> Character Ability: Lament; {user.character} has forced {players[source_player_index].character} to flip their character card!")

                        elif judgement_card.suit == "Hearts":
                            if players[targeted_index].current_health < players[targeted_index].max_health:
                                players[targeted_index].current_health += 1
                            print(
                                f"  >> Character Ability: Lament; {user.character} has forced {players[targeted_index].character} to regain one health ({players[targeted_index].current_health}/{players[targeted_index].max_health} HP remaining)!")

                        elif judgement_card.suit == "Clubs":
                            cards_discardable = (len(players[source_player_index].hand_cards.contents) + len(players[source_player_index].equipment_weapon) + len(
                                players[source_player_index].equipment_armor) + len(players[source_player_index].equipment_offensive_horse) + len(players[source_player_index].equipment_defensive_horse))
                            print(
                                f"  >> Character Ability: Lament; {user.character} has forced {players[source_player_index].character} to discard two cards!")
                            if cards_discardable < 2:
                                players[source_player_index].discard_all_cards()
                            else:
                                players[source_player_index].discard_from_equip_or_hand(
                                    2)

                        elif judgement_card.suit == "Diamonds":
                            players[targeted_index].hand_cards.draw(
                                main_deck, 2, False)
                            print(
                                f"  >> Character Ability: Lament; {user.character} has forced {players[targeted_index].character} to draw two cards!")

    def check_lightning_strike(self):
        # "Lightning Strike: Whenever you use a DEFEND card, you can target any other player to make a judgement. If the judgement card is of the suit SPADES, the target player suffers two points of lightning damage."
        if (self.character_ability1.startswith("Lightning Strike:") or self.character_ability3.startswith("Lightning Strike:")):

            user_index = 0
            for player_index, player in enumerate(players):
                if (self.character_ability1.startswith("Lightning Strike:") or self.character_ability3.startswith("Lightning Strike:")):
                    user_index = player_index
                    break

            question = [
                {
                    'type': 'list',
                    'name': 'Selected',
                    'message': f'{self.character}: Choose to activate Lightning Strike, make someone flip a judgement card; if SPADES, you deal two points of Lightning damage?',
                    'choices': ['Yes', 'No'],
                },
            ]
            answer = prompt(question, style=custom_style_2)

            if answer.get('Selected') == 'Yes':
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
                    f"  >> Character Ability: Lightning Strike; {self.character} will force {players[selected_index].character} to flip a judgement. If SPADES, they take two lightning damage.")

                main_deck.discard_from_deck()
                judgement_card = discard_deck.contents[0]
                print(
                    f"{players[selected_index].character} flipped a {judgement_card}.")
                judgement_card = check_judgement_tinkering(
                    judgement_card, user_index)
                players[selected_index].check_envy_of_heaven()

                if players[selected_index].check_beauty(judgement_card):
                    print(
                        f"  >> Character Ability: Lightning Strike; {players[selected_index].character}'s judgement card is a {judgement_card} and thus nothing happens.")

                elif judgement_card.suit == "Spades":
                    damage_dealt = 2

                    fantasy = players[selected_index].check_fantasy()
                    if fantasy[0]:
                        selected_index = fantasy[1]

                    deplete_karma = players[selected_index].check_deplete_karma(
                        damage_dealt, user_index, None)
                    if deplete_karma[0]:
                        damage_dealt = deplete_karma[1]

                    players[selected_index].current_health -= damage_dealt
                    print(
                        f"  >> Character Ability: Lightning Strike; {players[selected_index].character}'s judgement card is a {judgement_card} and therefore they take {damage_dealt} lightning damage ({players[selected_index].current_health}/{players[selected_index].max_health} HP remaining).")
                    for player_index, player in enumerate(players):
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

    def check_mediocrity(self, phase="Draw"):
        # "Mediocrity: During your drawing phase, you draw an extra X cards, X being the total number of allegiances still in play. During your discard phase, you must discard at least as many card as there are allegiances still in play. If you have less cards than there are allegiances, you must discard all of them."
        if (self.character_ability1.startswith("Mediocrity:") or self.character_ability3.startswith("Mediocrity:")):
            if phase == "Draw":
                print(
                    f"  >> Character Ability: Mediocrity; {self.character} draws {check_allegiances_in_play()} extra card(s) for every allegiance still in play.")
                return True
            if phase == "Discard":
                if check_allegiances_in_play() >= (len(self.hand_cards.contents) + len(self.equipment_weapon) + len(self.equipment_armor) + len(self.equipment_offensive_horse) + len(self.equipment_defensive_horse)):
                    print(
                        f"  >> Character Ability: Mediocrity; {self.character} discards at least {check_allegiances_in_play()} cards, one for every allegiance in play - they have no cards remaining.")
                    self.discard_all_cards()
                    return True
                else:
                    print(
                        f"  >> Character Ability: Mediocrity; {self.character} discards at least {check_allegiances_in_play()} cards, one for every allegiance in play, and then down to their health-level ({self.current_health}/{self.max_health} HP remaining).")
                    self.discard_from_equip_or_hand(
                        check_allegiances_in_play())
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
                        difference = (
                            len(self.hand_cards.list_cards()) - (self.current_health + limit_increase))
                        self.hand_cards.discard_from_hand(
                            difference)
                    return True

    def check_one_after_another(self):
        # "One After Another: Whenever you use or lose your last on-hand card, you can immediately draw one card from the deck."
        if (self.character_ability2.startswith("One After Another:") or self.character_ability3.startswith("One After Another:")):
            if len(self.hand_cards.contents) == 0:
                print(
                    f"  >> Character Ability: One After Another; {self.character} can draw a card whenever they use or lose their last on-hand card.")
                self.hand_cards.draw(main_deck, 1, False)

    def check_plotting_for_power(self, damage_dealt, mode="Reaction"):
        # "Plotting for Power: For every unit of damage you recieve, you can choose to draw one card and then set one hand-card face down as a RITE. Your hand limit is increased by one for each RITE."
        limit_increase = 0
        if (self.character_ability1.startswith("Plotting for Power:") or self.character_ability3.startswith("Plotting for Power:")):
            if mode == "Reaction":
                while damage_dealt > 0:
                    self.hand_cards.draw(main_deck, 1, False)
                    print(
                        f"  >> Character Ability: Plotting for Power; {self.character} has drawn one card.")
                    options_str = get_playing_card_options(self.hand_cards)
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
            activated_raid = True
            while activated_raid:
                print(' ')
                question = [
                    {
                        'type': 'list',
                        'name': 'Selected',
                        'message': f'{self.character}: Choose to activate Raid, and draw one hand-card from other player(s) instead of drawing from the deck?',
                        'choices': ['Yes', 'No'],
                    },
                ]

                answer = prompt(question, style=custom_style_2)
                if answer.get('Selected') == 'No':
                    activated_raid = False
                if answer.get('Selected') == 'Yes':

                    targets_str = []
                    targets = []
                    targets_str.append(Separator(
                        f"--{self.character} (Can't target yourself!)--"))
                    targets.append("Blank")
                    for player in players[1:]:
                        if len(player.hand_cards.contents) > 0:
                            targets_str.append(str(player))
                            targets.append(player)
                        else:
                            targets_str.append(
                                Separator(f"--{player.character} (0 cards - cannot be targeted)--"))
                            targets.append("Blank")
                    targets_str.append(
                        Separator("--------------------Other--------------------"))
                    targets_str.append("Cancel")
                    targets.append(Separator())
                    targets.append("Cancel")

                    question = [
                        {
                            'type': 'list',
                            'name': 'Selected',
                            'message': f'{self.character}: Please select a character to target with Raid:',
                            'choices': targets_str,
                            'filter': lambda player: targets_str.index(player)
                        },
                    ]

                    answer = prompt(question, style=custom_style_2)
                    target1_index = answer.get('Selected')

                    if target1_index == (len(players) + 1):
                        return self.check_raid()

                    targets_str.pop(target1_index)
                    targets_str.insert(target1_index, Separator(
                        f"--{players[target1_index].character} (Already selected)--"))
                    target1 = targets[target1_index]
                    targets_str.insert(-1, "Target noone else")
                    targets.insert(-1, "Target noone else")

                    question = [
                        {
                            'type': 'list',
                            'name': 'Selected',
                            'message': f'{self.character}: Please select a character to target with Raid:',
                            'choices': targets_str,
                            'filter': lambda player: targets_str.index(player)
                        },
                    ]

                    answer = prompt(question, style=custom_style_2)
                    target2_index = answer.get('Selected')
                    target2 = targets[target2_index]

                    if target2 == "Cancel":
                        return self.check_raid()
                    else:
                        print(' ')
                        options_str = target1.create_str_blind_menu()

                        question = [
                            {
                                'type': 'list',
                                'name': 'Selected',
                                'message': f"{self.character}: Please select which card you would like to take from {target1.character}'s hand:",
                                'choices': options_str,
                                'filter': lambda card: options_str.index(card)
                            },
                        ]
                        answer = prompt(question, style=custom_style_2)
                        card_stolen_index = answer.get('Selected')

                        if card_stolen_index <= len(target1.hand_cards.contents):
                            card_stolen = target1.hand_cards.contents.pop(
                                card_stolen_index - 1)
                            self.hand_cards.add_to_top(card_stolen)
                            print(
                                f"  >> Character Ability: Raid; {self.character} has drawn {card_stolen} from {target1.character}'s hand.")
                            target1.check_one_after_another()
                            activated_raid = False

                    if target2 != "Target noone else":
                        print(' ')
                        options_str = target2.create_str_blind_menu()

                        question = [
                            {
                                'type': 'list',
                                'name': 'Selected',
                                'message': f"{self.character}: Please select which card you would like to take from {target2.character}'s hand:",
                                'choices': options_str,
                                'filter': lambda card: options_str.index(card)
                            },
                        ]
                        answer = prompt(question, style=custom_style_2)
                        card_stolen_index = answer.get('Selected')

                        if card_stolen_index <= len(target2.hand_cards.contents):
                            card_stolen = target2.hand_cards.contents.pop(
                                card_stolen_index - 1)
                            self.hand_cards.add_to_top(card_stolen)
                            print(
                                f"  >> Character Ability: Raid; {self.character} has drawn {card_stolen} from {target2.character}'s hand.")
                            target2.check_one_after_another()
                            activated_raid = False
                    return True

    def check_reckless(self, card, source_player_index=0):
        # "Reckless: Every instance that you suffer damage from a red-suited ATTACK, or a WINE ATTACK, your maximum health limit is reduced by one instead."
        if (self.character_ability1.startswith("Reckless:") or self.character_ability3.startswith("Reckless:")):
            if players[source_player_index].check_beauty(card):
                if (card.suit == "Spades") or (card.suit == "Hearts") or (card.suit == "Diamonds") or (players[source_player_index].wine_active):
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

            if (card.suit == "Hearts") or (card.suit == "Diamonds") or (players[source_player_index].wine_active):
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

    def check_relish(self, source_player_index=0, mode="Activate"):
        # "Relish: Whenever another player targets an ATTACK against you, they must discard a basic card, or else that ATTACK has no net effect on you."
        if mode == "Activate":
            if (self.character_ability1.startswith("Relish:") or self.character_ability3.startswith("Relish:")):
                cards_discardable = len(
                    players[source_player_index].hand_cards.contents)
                if cards_discardable > 0:
                    if not (players[source_player_index].check_relish(0, "Reaction")):
                        return True
                else:
                    print(
                        f"  >> Character Ability: Relish; {players[source_player_index.character]} didn't discard a basic card! {self.character} is unaffected.")
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
                    'message': f'{self.character} - You cannot affect {players[relish_player_index].character} with an ATTACK unless you discard another basic card.',
                    'choices': options_str,
                    'filter': lambda card: options_str.index(card)
                },
            ]
            answer = prompt(question, style=custom_style_2)
            card_index = answer.get('Selected')
            if options_str[card_index] == "Do nothing.":
                print(
                    f"  >> Character Ability: Relish; {self.character} didn't discard a basic card! {players[relish_player_index].character} is unaffected.")
                return False
            card = self.hand_cards.contents.pop(card_index)
            discard_deck.add_to_top(card)

            if card.type == "Basic":
                print(
                    f"  >> Character Ability: Relish; {self.character} has discarded a basic card! {players[relish_player_index].character} must DEFEND as normal.")
                self.check_one_after_another()
                return True
            else:
                print(
                    f"  >> Character Ability: Relish; {self.character} didn't discard a basic card! {players[relish_player_index].character} is unaffected.")
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
                    question = [
                        {
                            'type': 'list',
                            'name': 'Selected',
                            'message': f'{self.character}: Choose to activate Retaliation, and take a card (on-hand or equipped) from {players[source_player_index].character}?',
                            'choices': ['Yes', 'No'],
                        },
                    ]
                    answer = prompt(question, style=custom_style_2)
                    if answer.get('Selected') == 'Yes':

                        options_str = players[source_player_index].create_str_semiblind_menu(
                        )
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
                        if card_stolen_index <= len(players[source_player_index].hand_cards.contents):
                            card_stolen = players[source_player_index].hand_cards.contents.pop(
                                card_stolen_index - 1)
                            self.hand_cards.add_to_top(card_stolen)
                            print(
                                f"  >> Character Ability: Retaliation; {self.character} has taken {card_stolen} from {players[source_player_index].character}'s hand.")
                            players[source_player_index].check_one_after_another()

                        # Check if equipment-card
                        else:
                            if card_stolen_index == (len(players[source_player_index].hand_cards.contents) + 2):
                                card_stolen = players[source_player_index].equipment_weapon.pop(
                                )
                                self.hand_cards.add_to_top(card_stolen)
                                players[source_player_index].weapon_range = 1
                                print(
                                    f"  >> Character Ability: Retaliation {self.character} has taken {card_stolen} from {players[source_player_index].character}'s weapon-slot.")
                                players[source_player_index].check_warrior_woman()

                            elif card_stolen_index == (len(players[source_player_index].hand_cards.contents) + 3):
                                card_stolen = players[source_player_index].equipment_armor.pop(
                                )
                                self.hand_cards.add_to_top(card_stolen)
                                print(
                                    f"  >> Character Ability: Retaliation {self.character} has taken {card_stolen} from {players[source_player_index].character}'s armor-slot.")
                                players[source_player_index].check_warrior_woman()

                            elif card_stolen_index == (len(players[source_player_index].hand_cards.contents) + 4):
                                card_stolen = players[source_player_index].equipment_offensive_horse.pop(
                                )
                                self.hand_cards.add_to_top(card_stolen)
                                print(
                                    f"  >> Character Ability: Retaliation {self.character} has taken {card_stolen} from {players[source_player_index].character}'s horse-slot.")
                                players[source_player_index].check_warrior_woman()

                            elif card_stolen_index == (len(players[source_player_index].hand_cards.contents) + 5):
                                card_stolen = players[source_player_index].equipment_defensive_horse.pop(
                                )
                                self.hand_cards.add_to_top(card_stolen)
                                print(
                                    f"  >> Character Ability: Retaliation {self.character} has taken {card_stolen} from {players[source_player_index]}'s horse-slot.")
                                players[source_player_index].check_warrior_woman()
                damage_dealt -= 1

    def check_second_wind(self, phase="Beginning"):
        # "Second Wind (Single-Use Ability): Once per game, at the beginning of your turn, you can return to the same amount of health that you had at the end of your previous turn. You draw a card for each unit of health that changes."
        if self.character_ability2.startswith("Second Wind (Single-Use Ability):"):
            if phase == "Beginning" and self.previous_turn_health != None:
                if not self.awakened:
                    question = [
                        {
                            'type': 'list',
                            'name': 'Selected',
                            'message': f'{self.character}: Choose to activate Second Wind (Single-Use Ability), returning your health to what what it was at the end of your previous turn, and drawing a card for each unit changed.',
                            'choices': ['Yes', 'No'],
                        },
                    ]
                    answer = prompt(question, style=custom_style_2)
                    if answer.get('Selected') == 'Yes':
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
            question = [
                {
                    'type': 'list',
                    'name': 'Selected',
                    'message': f'{self.character}: Please confirm you want to shapeshift into the above character, gaining their allegiance, gender, and one of their abilities.',
                    'choices': ['Yes', 'No'],
                },
            ]
            answer = prompt(question, style=custom_style_2)
            if answer.get('Selected') == 'Yes':
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
                        if (self.forms.contents[card_index].character_ability3 != "Eiron (Awakening/Ruler Ability): At the start of your turn, if your health is the least or among the least, you must raise your maximum health by one unit, regain one unit of health, and permanently gain the ability 'Rouse'." and self.forms.contents[card_index].character_ability3 != "Exalt (Ruler Ability): Whenever any Wei character (other than yourself) makes a judgement, if the judgement card that takes effect is either CLUBS or SPADES, that character can choose to let you draw one card from the deck." and self.forms.contents[card_index].character_ability3 != "Dashing Hero (INACTIVE Ability): Draw an extra card at the start of your turn." and self.forms.contents[card_index].character_ability3 != "Amber Sky (Ruler Ability): All Hero characters can give you a DEFEND or LIGHTNING card during their individual turns." and self.forms.contents[card_index].character_ability3 != "Astrology (INACTIVE Ability): Before your judgement phase, you can view the top X cards of the deck (X being the number of players still in play, with a maximum of five). Of these X cards, you can rearrange the order of the cards, and choose any number to place at the top or bottom of the draw-deck." and self.forms.contents[card_index].character_ability3 != "Blitz (INACTIVE Ability): In your action phase, you can use any of your TERRAINS as STEAL." and self.forms.contents[card_index].character_ability3 != "Rejection (INACTIVE Ability): Once per turn, you can discard one RITE and force any character to draw two cards. If after, that character has more hand-cards than you, you then deal one damage to them."):
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
                        if (self.forms.contents[card_index].character_ability4 != "Rouse (INACTIVE Ability): If you need to use an ATTACK, you can ask any member of Shu to play it on your behalf." and self.forms.contents[card_index].character_ability4 != "Lingering Spirit (INACTIVE Ability): If your health is not at maximum in your drawing phase, you can force any player to draw X cards, and then discard 1 card, or draw 1 card, and discard X cards. X is the amount of health you have missing from your maximum." and self.forms.contents[card_index].character_ability4 != "Tyrant (Ruler Ability): Whenever another Hero character causes damage to any other player, you can flip a judgement card. If the judgement card is of the suit SPADES, you can regain one unit of health."):
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

    def check_talent(self):
        # "Talent: You can use tool cards without range restrictions."
        if (self.character_ability2.startswith("Talent:") or self.character_ability3.startswith("Talent:")):
            print(
                f"  >> Character Ability: Talent; {self.character} has no range restriction on their tool cards.")
            return True

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

# Activatable abilities (reusable)
    def activate_blockade(self):
        # "Blockade: During your action phase, you can choose to use any of your basic or equipment cards with suit CLUBS or SPADES as RATIONS DEPLETED with a physical range of -1 in distance calculations. RATIONS DEPLETED acts as a time-delay tool card, in which a player will have to flip a judgement at the start of their turn. If the judgement is any suit other than CLUBS, the target fails the judgement and must skip their drawing phase."
        if (self.character_ability1.startswith("Blockade:") or self.character_ability3.startswith("Blockade:")):
            cards_discardable = (len(self.hand_cards.contents) + len(self.equipment_weapon) + len(
                self.equipment_armor) + len(self.equipment_offensive_horse) + len(self.equipment_defensive_horse))
            if cards_discardable > 0:
                usable_cards = []
                for card in self.hand_cards.contents:
                    if (card.suit == "Spades" or card.suit == "Clubs") and (card.type == "Basic" or card.type == "Weapon" or card.type == "Armor" or card.type == "-1 Horse" or card.type == "+1 Horse"):
                        usable_cards.append(card)
                for card in self.equipment_weapon:
                    if (card.suit == "Spades" or card.suit == "Clubs") and (card.type == "Basic" or card.type == "Weapon" or card.type == "Armor" or card.type == "-1 Horse" or card.type == "+1 Horse"):
                        usable_cards.append(card)
                for card in self.equipment_armor:
                    if (card.suit == "Spades" or card.suit == "Clubs") and (card.type == "Basic" or card.type == "Weapon" or card.type == "Armor" or card.type == "-1 Horse" or card.type == "+1 Horse"):
                        usable_cards.append(card)
                for card in self.equipment_offensive_horse:
                    if (card.suit == "Spades" or card.suit == "Clubs") and (card.type == "Basic" or card.type == "Weapon" or card.type == "Armor" or card.type == "-1 Horse" or card.type == "+1 Horse"):
                        usable_cards.append(card)
                for card in self.equipment_defensive_horse:
                    if (card.suit == "Spades" or card.suit == "Clubs") and (card.type == "Basic" or card.type == "Weapon" or card.type == "Armor" or card.type == "-1 Horse" or card.type == "+1 Horse"):
                        usable_cards.append(card)

                if len(usable_cards) < 1:
                    print(
                        f"{self.character}: You cannot use this ability as you have no black-suited cards.")

                else:
                    options_str = self.create_str_nonblind_menu()
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
                    weapon_popped = False
                    armor_popped = False
                    off_horse_popped = False
                    def_horse_popped = False

                    if options_str[discarded_index] == "Cancel ability.":
                        return (' ')

                    if (options[discarded_index].suit == "Spades" or options[discarded_index].suit == "Clubs") and (options[discarded_index].type == "Basic" or options[discarded_index].type == "Weapon" or options[discarded_index].type == "Armor" or options[discarded_index].type == "-1 Horse" or options[discarded_index].type == "+1 Horse"):
                        # Check if hand-card
                        if discarded_index <= len(self.hand_cards.contents):
                            card = self.hand_cards.contents.pop(
                                discarded_index - 1)
                            discard_deck.add_to_top(card)
                            print(
                                f"  >> Character Ability: Blockade; {self.character} has discarded {card} from their hand to use as RATIONS DEPLETED.")

                        # Check if equipment-card
                        else:
                            if discarded_index == (len(self.hand_cards.contents) + 2):
                                card = self.equipment_weapon.pop()
                                discard_deck.add_to_top(card)
                                self.weapon_range = 1
                                weapon_popped = True
                                print(
                                    f"  >> Character Ability: Blockade; {self.character} has discarded {card} from their weapon-slot to use as RATIONS DEPLETED.")

                            if discarded_index == (len(self.hand_cards.contents) + 3):
                                card = self.equipment_armor.pop()
                                discard_deck.add_to_top(card)
                                armor_popped = True
                                print(
                                    f"  >> Character Ability: Blockade; {self.character} has discarded {card} from their armor-slot to use as RATIONS DEPLETED.")

                            if discarded_index == (len(self.hand_cards.contents) + 4):
                                card = self.equipment_offensive_horse.pop()
                                discard_deck.add_to_top(card)
                                off_horse_popped = True
                                print(
                                    f"  >> Character Ability: Blockade; {self.character} has discarded {card} from their horse-slot to use as RATIONS DEPLETED.")

                            if discarded_index == (len(self.hand_cards.contents) + 5):
                                card = self.equipment_defensive_horse.pop()
                                discard_deck.add_to_top(card)
                                def_horse_popped = True
                                print(
                                    f"  >> Character Ability: Blockade; {self.character} has discarded {card} from their horse-slot to use as RATIONS DEPLETED.")

                        card.effect2 = "Rations Depleted"
                        if not self.use_card_effect("Special", card):
                            if weapon_popped:
                                discard_deck.contents.pop(0)
                                self.equipment_weapon.append(card)
                                self.weapon_range = card.weapon_range
                            if armor_popped:
                                discard_deck.contents.pop(0)
                                self.equipment_armor.append(card)
                            if off_horse_popped:
                                discard_deck.contents.pop(0)
                                self.equipment_offensive_horse.append(card)
                            if def_horse_popped:
                                discard_deck.contents.pop(0)
                                self.equipment_defensive_horse.append(card)
                            else:
                                self.hand_cards.draw(discard_deck, 1, False)
                            print(
                                f"{self.character} cancelled using their effect, and {card} was returned.")
                    else:
                        print(
                            f"{options[discarded_index]} cannot be used as RATIONS DEPLETED as it is NOT a black-suited, basic/equipment card.")

    def activate_drown_in_wine(self, mode="Check"):
        # "Drown in Wine: You can use any of your on-hand cards with suit of SPADES as WINE. WINE can be used on yourself the brink of death to restore one unit of health, or to increase the damage of their next ATTACK by one damage."
        if (self.character_ability1.startswith("Drown in Wine:") or self.character_ability3.startswith("Drown in Wine:")):
            usable_cards = []
            for card in self.hand_cards.contents:
                if card.suit == "Spades":
                    usable_cards.append(card)

            if mode == "Check":
                return True

            if mode == "Activate" or mode == "Reaction":
                if len(usable_cards) < 1:
                    print(
                        f"{self.character}: You cannot use this ability as you have no hand-cards that are SPADES.")

                else:
                    options_str = self.create_str_nonblind_menu(True)
                    options_str.append(
                        Separator("--------------------Other--------------------"))
                    options_str.append("Cancel ability.")
                    options = self.hand_cards.contents

                    question = [
                        {
                            'type': 'list',
                            'name': 'Selected',
                            'message': f'{self.character}: Please select a card to use as WINE?',
                            'choices': options_str,
                            'filter': lambda card: options_str.index(card)
                        },
                    ]
                    answer = prompt(question, style=custom_style_2)
                    discarded_index = answer.get('Selected')
                    if options_str[discarded_index] == "Cancel ability.":
                        return (' ')

                    if options[discarded_index].suit != "Spades":
                        print(
                            f"{options[discarded_index]} cannot be used as WINE as it is not of suit SPADES.")

                    if options[discarded_index].suit == "Spades":
                        if discarded_index <= len(self.hand_cards.contents):
                            discarded = self.hand_cards.contents.pop(
                                discarded_index)
                            discard_deck.add_to_top(discarded)

                            if mode == "Activate":
                                print(
                                    f"  >> Character Ability: Drown in Wine; {self.character} has discarded {discarded} from their hand to use as WINE - Their next attack will do two damage.")
                                self.wine_active = True

                            if mode == "Reaction":
                                print(
                                    f"  >> Character Ability: Drown in Wine; {self.character} has discarded {discarded} from their hand to use as WINE!")

                            return True

    def activate_national_colours(self):
        # "National Colours: During your action phase, you can use any of your cards (on-hand or equipped) with a DIAMONDS suit as ACEDIA."
        if (self.character_ability1.startswith("National Colours:") or self.character_ability3.startswith("National Colours:")):
            cards_discardable = (len(self.hand_cards.contents) + len(self.equipment_weapon) + len(
                self.equipment_armor) + len(self.equipment_offensive_horse) + len(self.equipment_defensive_horse))
            if cards_discardable > 0:
                usable_cards = []
                for card in self.hand_cards.contents:
                    if card.suit == "Diamonds":
                        usable_cards.append(card)
                for card in self.equipment_weapon:
                    if card.suit == "Diamonds":
                        usable_cards.append(card)
                for card in self.equipment_armor:
                    if card.suit == "Diamonds":
                        usable_cards.append(card)
                for card in self.equipment_offensive_horse:
                    if card.suit == "Diamonds":
                        usable_cards.append(card)
                for card in self.equipment_defensive_horse:
                    if card.suit == "Diamonds":
                        usable_cards.append(card)

                if len(usable_cards) < 1:
                    print(
                        f"{self.character}: You cannot use this ability as you have no DIAMOND-suited cards.")

                else:
                    options_str = self.create_str_nonblind_menu()
                    options_str.append(
                        Separator("--------------------Other--------------------"))
                    options_str.append("Cancel ability.")
                    options = self.create_actual_menu()

                    question = [
                        {
                            'type': 'list',
                            'name': 'Selected',
                            'message': f'{self.character}: Please select a DIAMOND-suited card to use as ACEDIA?',
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

                    if options[discarded_index].suit == "Diamonds":
                        # Check if hand-card
                        if discarded_index <= len(self.hand_cards.contents):
                            card = self.hand_cards.contents.pop(
                                discarded_index - 1)
                            discard_deck.add_to_top(card)
                            print(
                                f"  >> Character Ability: National Colours; {self.character} has discarded {card} from their hand to use as ACEDIA.")

                        # Check if equipment-card
                        else:
                            if discarded_index == (len(self.hand_cards.contents) + 2):
                                card = self.equipment_weapon.pop()
                                discard_deck.add_to_top(card)
                                self.weapon_range = 1
                                weapon_popped = True
                                print(
                                    f"  >> Character Ability: National Colours; {self.character} has discarded {card} from their weapon-slot to use as ACEDIA.")

                            if discarded_index == (len(self.hand_cards.contents) + 3):
                                card = self.equipment_armor.pop()
                                discard_deck.add_to_top(card)
                                armor_popped = True
                                print(
                                    f"  >> Character Ability: National Colours; {self.character} has discarded {card} from their armor-slot to use as ACEDIA.")

                            if discarded_index == (len(self.hand_cards.contents) + 4):
                                card = self.equipment_offensive_horse.pop()
                                discard_deck.add_to_top(card)
                                off_horse_popped = True
                                print(
                                    f"  >> Character Ability: National Colours; {self.character} has discarded {card} from their horse-slot to use as ACEDIA.")

                            if discarded_index == (len(self.hand_cards.contents) + 5):
                                card = self.equipment_defensive_horse.pop()
                                discard_deck.add_to_top(card)
                                def_horse_popped = True
                                print(
                                    f"  >> Character Ability: National Colours; {self.character} has discarded {card} from their horse-slot to use as ACEDIA.")

                        card.effect2 = "Acedia"
                        if not self.use_card_effect("Special", card):
                            if weapon_popped:
                                discard_deck.contents.pop(0)
                                self.equipment_weapon.append(card)
                                self.weapon_range = card.weapon_range
                            if armor_popped:
                                discard_deck.contents.pop(0)
                                self.equipment_armor.append(card)
                            if off_horse_popped:
                                discard_deck.contents.pop(0)
                                self.equipment_offensive_horse.append(card)
                            if def_horse_popped:
                                discard_deck.contents.pop(0)
                                self.equipment_defensive_horse.append(card)
                            else:
                                self.hand_cards.draw(discard_deck, 1, False)
                            print(
                                f"{self.character} cancelled using their effect, and {card} was returned.")
                    else:
                        print(
                            f"{options[discarded_index]} cannot be used as ACEDIA as is it NOT of suit DIAMONDS.")

    def activate_random_strike(self):
        # "Random Strike: You can use any two hand-cards which have the same suit as RAIN OF ARROWS."
        if (self.character_ability1.startswith("Random Strike:") or self.character_ability3.startswith("Random Strike:")):
            if len(self.hand_cards.contents) > 1:
                options = get_playing_card_options(self.hand_cards)
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

    def activate_surprise(self):
        # "Surprise: During your action phase, you can use any of your black-suited cards (on-hand or equipped) as DISMANTLE."
        if (self.character_ability1.startswith("Surprise:") or self.character_ability3.startswith("Surprise:")):
            cards_discardable = (len(self.hand_cards.contents) + len(self.equipment_weapon) + len(
                self.equipment_armor) + len(self.equipment_offensive_horse) + len(self.equipment_defensive_horse))
            if cards_discardable > 0:
                usable_cards = []
                for card in self.hand_cards.contents:
                    if card.suit == "Spades" or card.suit == "Clubs":
                        usable_cards.append(card)
                for card in self.equipment_weapon:
                    if card.suit == "Spades" or card.suit == "Clubs":
                        usable_cards.append(card)
                for card in self.equipment_armor:
                    if card.suit == "Spades" or card.suit == "Clubs":
                        usable_cards.append(card)
                for card in self.equipment_offensive_horse:
                    if card.suit == "Spades" or card.suit == "Clubs":
                        usable_cards.append(card)
                for card in self.equipment_defensive_horse:
                    if card.suit == "Spades" or card.suit == "Clubs":
                        usable_cards.append(card)

                if len(usable_cards) < 1:
                    print(
                        f"{self.character}: You cannot use this ability as you have no black-suited cards.")

                else:
                    options_str = self.create_str_nonblind_menu()
                    options_str.append(
                        Separator("--------------------Other--------------------"))
                    options_str.append("Cancel ability.")
                    options = self.create_actual_menu()

                    question = [
                        {
                            'type': 'list',
                            'name': 'Selected',
                            'message': f'{self.character}: Please select a black-suited card to use as DISMANTLE?',
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

                    if options[discarded_index].suit == "Spades" or options[discarded_index].suit == "Clubs":
                        # Check if hand-card
                        if discarded_index <= len(self.hand_cards.contents):
                            card = self.hand_cards.contents.pop(
                                discarded_index - 1)
                            discard_deck.add_to_top(card)
                            print(
                                f"  >> Character Ability: Surprise; {self.character} has discarded {card} from their hand to use as DISMANTLE.")

                        # Check if equipment-card
                        else:
                            if discarded_index == (len(self.hand_cards.contents) + 2):
                                card = self.equipment_weapon.pop()
                                discard_deck.add_to_top(card)
                                self.weapon_range = 1
                                weapon_popped = True
                                print(
                                    f"  >> Character Ability: Surprise; {self.character} has discarded {card} from their weapon-slot to use as DISMANTLE.")

                            if discarded_index == (len(self.hand_cards.contents) + 3):
                                card = self.equipment_armor.pop()
                                discard_deck.add_to_top(card)
                                armor_popped = True
                                print(
                                    f"  >> Character Ability: Surprise; {self.character} has discarded {card} from their armor-slot to use as DISMANTLE.")

                            if discarded_index == (len(self.hand_cards.contents) + 4):
                                card = self.equipment_offensive_horse.pop()
                                discard_deck.add_to_top(card)
                                off_horse_popped = True
                                print(
                                    f"  >> Character Ability: Surprise; {self.character} has discarded {card} from their horse-slot to use as DISMANTLE.")

                            if discarded_index == (len(self.hand_cards.contents) + 5):
                                card = self.equipment_defensive_horse.pop()
                                discard_deck.add_to_top(card)
                                def_horse_popped = True
                                print(
                                    f"  >> Character Ability: Surprise; {self.character} has discarded {card} from their horse-slot to use as DISMANTLE.")

                        card.effect2 = "Dismantle"
                        if not self.use_card_effect("Special", card):
                            if weapon_popped:
                                discard_deck.contents.pop(0)
                                self.equipment_weapon.append(card)
                                self.weapon_range = card.weapon_range
                            if armor_popped:
                                discard_deck.contents.pop(0)
                                self.equipment_armor.append(card)
                            if off_horse_popped:
                                discard_deck.contents.pop(0)
                                self.equipment_offensive_horse.append(card)
                            if def_horse_popped:
                                discard_deck.contents.pop(0)
                                self.equipment_defensive_horse.append(card)
                            else:
                                self.hand_cards.draw(discard_deck, 1, False)
                            print(
                                f"{self.character} cancelled using their effect, and {card} was returned.")
                    else:
                        print(
                            f"{options[discarded_index]} cannot be used as DISMANTLE as it is NOT black-suited.")

    def activate_trojan_flesh(self):
        # "Trojan Flesh: During your action phase, you can choose to lose one unit of health to draw two more cards from the deck. This ability can be used repeatedly in a turn."
        if (self.character_ability1.startswith("Trojan Flesh:") or self.character_ability3.startswith("Trojan Flesh:")):
            question = [
                {
                    'type': 'list',
                    'name': 'Selected',
                    'message': f'{self.character}: Choose to activate Trojan Flesh; losing one health to draw two cards from the deck?',
                    'choices': ['Yes', 'No'],
                },
            ]
            answer = prompt(question, style=custom_style_2)
            if answer.get('Selected') == 'Yes':
                print(
                    f"  >> Character Ability: Trojan Flesh; {self.character} lost one health to draw two cards from the deck.")
                self.current_health -= 1
                if self.current_health < 1:
                    if self.check_brink_of_death_loop(0, "Self") == "Break":
                        return "Break"
                else:
                    self.hand_cards.draw(main_deck, 2, False)
                    self.check_geminate(1)

    def activate_warrior_saint(self, mode="Check"):
        # "Warrior Saint: You can use any red-suited cards (on-hand or equipped) as an ATTACK."
        if mode == "Check":
            if (self.character_ability2.startswith("Warrior Saint:") or self.character_ability3.startswith("Warrior Saint:")):
                return True

        if mode == "Activate" or mode == "Reaction":
            if (self.character_ability2.startswith("Warrior Saint:") or self.character_ability3.startswith("Warrior Saint:")):
                cards_discardable = (len(self.hand_cards.contents) + len(self.equipment_weapon) + len(
                    self.equipment_armor) + len(self.equipment_offensive_horse) + len(self.equipment_defensive_horse))
                if cards_discardable > 0:
                    usable_cards = []
                    for card in self.hand_cards.contents:
                        if card.suit == "Hearts" or card.suit == "Diamonds":
                            usable_cards.append(card)
                    for card in self.equipment_weapon:
                        if card.suit == "Hearts" or card.suit == "Diamonds":
                            usable_cards.append(card)
                    for card in self.equipment_armor:
                        if card.suit == "Hearts" or card.suit == "Diamonds":
                            usable_cards.append(card)
                    for card in self.equipment_offensive_horse:
                        if card.suit == "Hearts" or card.suit == "Diamonds":
                            usable_cards.append(card)
                    for card in self.equipment_defensive_horse:
                        if card.suit == "Hearts" or card.suit == "Diamonds":
                            usable_cards.append(card)

                    if len(usable_cards) < 1:
                        print(
                            f"{self.character}: You cannot use this ability as you have no red-suited cards.")

                    else:
                        options_str = self.create_str_nonblind_menu()
                        options_str.append(
                            Separator("--------------------Other--------------------"))
                        options_str.append("Cancel ability.")
                        options = self.create_actual_menu()

                        question = [
                            {
                                'type': 'list',
                                'name': 'Selected',
                                'message': f'{self.character}: Please select a red-suited card to use as ATTACK?',
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

                        if options[discarded_index].suit == "Hearts" or options[discarded_index].suit == "Diamonds":
                            # Check if hand-card
                            if discarded_index <= len(self.hand_cards.contents):
                                card = self.hand_cards.contents.pop(
                                    discarded_index - 1)
                                discard_deck.add_to_top(card)
                                print(
                                    f"  >> Character Ability: Warrior Saint; {self.character} has discarded {card} from their hand to use as ATTACK.")

                            # Check if equipment-card
                            else:
                                if discarded_index == (len(self.hand_cards.contents) + 2):
                                    card = self.equipment_weapon.pop()
                                    discard_deck.add_to_top(card)
                                    self.weapon_range = 1
                                    weapon_popped = True
                                    print(
                                        f"  >> Character Ability: Warrior Saint; {self.character} has discarded {card} from their weapon-slot to use as ATTACK.")

                                if discarded_index == (len(self.hand_cards.contents) + 3):
                                    card = self.equipment_armor.pop()
                                    discard_deck.add_to_top(card)
                                    armor_popped = True
                                    print(
                                        f"  >> Character Ability: Warrior Saint; {self.character} has discarded {card} from their armor-slot to use as ATTACK.")

                                if discarded_index == (len(self.hand_cards.contents) + 4):
                                    card = self.equipment_offensive_horse.pop()
                                    discard_deck.add_to_top(card)
                                    off_horse_popped = True
                                    print(
                                        f"  >> Character Ability: Warrior Saint; {self.character} has discarded {card} from their horse-slot to use as ATTACK.")

                                if discarded_index == (len(self.hand_cards.contents) + 5):
                                    card = self.equipment_defensive_horse.pop()
                                    discard_deck.add_to_top(card)
                                    def_horse_popped = True
                                    print(
                                        f"  >> Character Ability: Warrior Saint; {self.character} has discarded {card} from their horse-slot to use as ATTACK.")

                            if mode == "Activate":
                                card.effect2 = "Attack"
                                if not self.use_card_effect("Special", card):
                                    if weapon_popped:
                                        discard_deck.contents.pop(0)
                                        self.equipment_weapon.append(card)
                                        self.weapon_range = card.weapon_range
                                    if armor_popped:
                                        discard_deck.contents.pop(0)
                                        self.equipment_armor.append(card)
                                    if off_horse_popped:
                                        discard_deck.contents.pop(0)
                                        self.equipment_offensive_horse.append(
                                            card)
                                    if def_horse_popped:
                                        discard_deck.contents.pop(0)
                                        self.equipment_defensive_horse.append(
                                            card)
                                    else:
                                        self.hand_cards.draw(
                                            discard_deck, 1, False)
                                    print(
                                        f"{self.character} cancelled using their effect, and {card} was returned.")

                            if mode == "Reaction":
                                card.effect2 == "Attack"
                                return (card)

                        else:
                            print(
                                f"{options[discarded_index]} cannot be used as ATTACK as is it NOT red-suited.")

# Activatable abilities (once-per-turn)
    def activate_amber_sky(self):
        # "Amber Sky (Ruler Ability): All Hero characters can give you a DEFEND or LIGHTNING card during their individual turns."
        emperor_index = None
        false_ruler_index = None
        if self.used_amber_sky:
            print(f"{self.character}: You can only use Amber Sky once per turn.")

        if not self.used_amber_sky:
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

                options = self.create_str_nonblind_menu(True)
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

    def activate_green_salve(self):
        # "Green Salve: During your action phase, you can discard any card and allow any player to regain one unit of health. Limited to one use per turn."
        if (self.character_ability2.startswith("Green Salve:") or self.character_ability3.startswith("Green Salve:")):
            cards_discardable = (len(self.hand_cards.contents) + len(self.equipment_weapon) + len(
                self.equipment_armor) + len(self.equipment_offensive_horse) + len(self.equipment_defensive_horse))
            if self.used_green_salve:
                print(
                    f"{self.character}: You can only use Green Salve once per turn.")

            if not self.used_green_salve:
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

                        options_str = self.create_str_nonblind_menu()
                        options_str.append(
                            Separator("--------------------Other--------------------"))
                        options_str.append("Cancel ability.")

                        question = [
                            {
                                'type': 'list',
                                'name': 'Selected',
                                'message': f'{self.character}: Please select a card to discard?',
                                'choices': options_str,
                                'filter': lambda card: options_str.index(card)
                            },
                        ]
                        answer = prompt(question, style=custom_style_2)
                        discarded_index = answer.get('Selected')

                        if options_str[discarded_index] == "Cancel ability.":
                            return (' ')

                        # Check if hand-card
                        elif discarded_index <= len(self.hand_cards.contents):
                            card = self.hand_cards.contents.pop(
                                discarded_index - 1)
                            discard_deck.add_to_top(card)

                        # Check if equipment-card
                        else:
                            if discarded_index == (len(self.hand_cards.contents) + 2):
                                card = self.equipment_weapon.pop()
                                discard_deck.add_to_top(card)
                                self.weapon_range = 1
                                print(
                                    f"{self.character} has discarded {card} from their weapon-slot.")

                            if discarded_index == (len(self.hand_cards.contents) + 3):
                                card = self.equipment_armor.pop()
                                discard_deck.add_to_top(card)
                                print(
                                    f"{self.character} has discarded {card} from their armor-slot.")

                            if discarded_index == (len(self.hand_cards.contents) + 4):
                                card = self.equipment_offensive_horse.pop()
                                discard_deck.add_to_top(card)
                                print(
                                    f"{self.character} has discarded {card} from their horse-slot.")

                            if discarded_index == (len(self.hand_cards.contents) + 5):
                                card = self.equipment_defensive_horse.pop()
                                discard_deck.add_to_top(card)
                                print(
                                    f"{self.character} has discarded {card} from their horse-slot.")

                        options[player_healed_index].current_health += 1
                        self.used_green_salve = True
                        print(
                            f"  >> Character Ability: Green Salve; {self.character} discarded {card} to heal {options[player_healed_index].character} by one! ({options[player_healed_index].current_health}/{options[player_healed_index].max_health} HP remaining)")

    def activate_marriage(self):
        # "Marriage: During your action phase, you can choose to discard two on-hand cards and pick any male character that is not at full-health. By doing so, both the male character and yourself will recover one unit of health. Limited to one use per turn."
        if (self.character_ability1.startswith("Marriage:") or self.character_ability3.startswith("Marriage:")):
            if len(self.hand_cards.contents) > 1:
                if self.used_marriage:
                    print(
                        f"{self.character}: You can only use Marriage once per turn.")

                if not self.used_marriage:
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

                    options = self.create_str_nonblind_menu(True)
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
                    self.check_one_after_another()
                    if self.max_health > self.current_health:
                        self.current_health += 1
                        players[player_healed_index].current_health += 1
                        print(
                            f"  >> Character Ability: Marriage; {self.character} ({self.current_health}/{self.max_health} HP remaining) has healed both themselves and {players[player_healed_index].character} ({players[player_healed_index].current_health}/{players[player_healed_index].max_health} HP remaining) by discarding two cards!")
                    else:
                        players[player_healed_index].current_health += 1
                        print(
                            f"  >> Character Ability: Marriage; {self.character} has healed {players[player_healed_index].character} ({players[player_healed_index].current_health}/{players[player_healed_index].max_health} HP remaining) by discarding two cards!")

    def activate_reconsider(self):
        # "Reconsider: Once per turn, you can discard any number of cards to then draw the same number."
        if (self.character_ability1.startswith("Reconsider:") or self.character_ability3.startswith("Reconsider:")):
            cards_discardable = (len(self.hand_cards.contents) + len(self.equipment_weapon) + len(
                self.equipment_armor) + len(self.equipment_offensive_horse) + len(self.equipment_defensive_horse))
            total_hand_cards = len(self.hand_cards.contents)
            if self.used_reconsider:
                print(
                    f"{self.character}: You can only use Reconsider once per turn!")

            if not self.used_reconsider:
                cards_to_replace = 0
                options = self.create_str_nonblind_menu()
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
                    if card_index <= total_hand_cards:
                        discard_deck.add_to_top(
                            self.hand_cards.contents.pop(card_index - 1))
                        self.hand_cards.contents.insert(
                            (card_index - 1), "Placeholder")
                    if card_index == (total_hand_cards + 2):
                        discard_deck.add_to_top(
                            self.equipment_weapon.pop())
                    if card_index == (total_hand_cards + 3):
                        discard_deck.add_to_top(
                            self.equipment_armor.pop())
                    if card_index == (total_hand_cards + 4):
                        discard_deck.add_to_top(
                            self.equipment_offensive_horse.pop())
                    if card_index == (total_hand_cards + 5):
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
        # Check for Jiang Wei/Zhuge Liang; Astrology
        # Check for Zhang He; Flexibility
        self.check_goddess_luo()
        return self.start_judgement_phase()

# Judgement Phase
    def start_judgement_phase(self):
        print(" ")
        # Check for Xiahou Yuan; Godspeed
        # Check for Cao Pi; Exalt - this to be incorporated within below command!
        if self.check_pending_judgements() == "Break":
            return players[0].start_beginning_phase()
        else:
            self.check_pending_judgements()
        if self.acedia_active and self.rations_depleted_active:
            return self.start_discard_phase()
        elif self.rations_depleted_active:
            return self.start_action_phase()
        elif self.acedia_active:
            if self.check_raid():
                return self.start_action_phase()
            return self.start_drawing_phase()
        else:
            # Check for Yan Liang & Wen Chou; Dual Heroes
            # Check for Zhang He; Flexibility
            if self.check_raid():
                return self.start_action_phase()
            return self.start_drawing_phase()

# Drawing Phase
    def start_drawing_phase(self):
        print(" ")
        cards_drawn = 2
        message = True
        # Checks for Lu Su; Altruism
        if self.check_bare_chested():
            cards_drawn -= 1
            message = False
        if self.check_dashing_hero():
            cards_drawn += 1
            message = False
        if self.check_dual_heroes():
            cards_drawn = 0
            message = False
        if self.check_mediocrity("Draw"):
            cards_drawn += check_allegiances_in_play()
            message = False
        # Checks for Sun Ce; Lingering Spirit
        # Check for Zhang He; Flexibility
        self.hand_cards.draw(main_deck, cards_drawn, message)
        if self.acedia_active:
            return self.start_discard_phase()
        else:
            return self.start_action_phase()

# Action Phase
    def start_action_phase(self):
        action_phase_active = True
        while action_phase_active:
            if self.current_health == 0:
                return(self.start_end_phase())
            print(' ')
            options = []
            options.append(
                Separator("--------------------Cards--------------------"))
            playing_card_options = get_playing_card_options(self.hand_cards)
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
                card.effect2 = card.effect
                self.use_card_effect(card_index, card)

            # For activating an ability
            else:
                if options[action_taken_index] == " Character Ability >> Blockade":
                    self.activate_blockade()
                if options[action_taken_index] == " Character Ability >> Drown in Wine":
                    self.activate_drown_in_wine("Activate")
                if options[action_taken_index] == " Character Ability >> Dual Heroes":
                    self.check_dual_heroes("Activate")
                if options[action_taken_index] == " Character Ability >> Green Salve":
                    self.activate_green_salve()
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
                if options[action_taken_index] == " Character Ability >> Surprise":
                    self.activate_surprise()
                if options[action_taken_index] == " Character Ability >> Trojan Flesh":
                    self.activate_trojan_flesh()
                if options[action_taken_index] == " Character Ability >> Warrior Saint":
                    self.activate_warrior_saint("Activate")
                if options[action_taken_index] == " Ruler Ability >> Amber Sky":
                    self.activate_amber_sky()
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
        if self.check_mediocrity("Discard"):
            pass
        else:
            # Check for characters that have increased hand-card limits at end of their turn
            limit_increase1 = self.check_bloodline()
            limit_increase2 = self.check_plotting_for_power(0, "Discard")
            limit_increase = limit_increase1 + limit_increase2

            # Discard down to your current health level
            if len(self.hand_cards.list_cards()) > (self.current_health + limit_increase):
                difference = (len(self.hand_cards.list_cards()) -
                              (self.current_health + limit_increase))
                self.hand_cards.discard_from_hand(difference)
        return self.start_end_phase()

# End Phase
    def start_end_phase(self):
        print(" ")
        self.acedia_active = False
        self.rations_depleted_active = False
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

# how to reference players~
# players[0].hand_cards.draw(main_deck, 4)
# players[0].hand_cards.view_hand()
# players[0].hand_cards.discard_from_hand(2)
# players[0].equipment_weapon.append(Card(6, 'Six', 'Spades', 'Weapon', 'Black Pommel', 'When equipped, the wielder ignores any armor of their targets.', 2))
# players[1].equipment_weapon.append(Card(6, 'Six', 'Spades', 'Weapon', 'Black Pommel', 'When equipped, the wielder ignores any armor of their targets.', 2))
# players[1].equipment_armor.append(Card(2, 'Two', 'Spades', 'Armor', 'Eight-Trigrams', 'When equipped: whenever a DEFEND is needed, the wearer can perform a judgement. If it is red, the DEFEND is considered to be played.'))
# players[1].pending_judgements.append(Card('6', 'Six', 'Spades', 'Delay-Tool', 'Acedia', 'You can place Delay-Tool on any other player. The target must perform a judgement for this card. If it is not HEARTS, they forfeit their action-phase.', None, 'Acedia'))
# players[1].pending_judgements.append(Card('6', 'Six', 'Spades', 'Delay-Tool', 'Lightning', 'You can place Delay-Tool on any other player. The target must perform a judgement for this card. If it is not HEARTS, they forfeit their action-phase.', None, 'Lightning'))
# players[0].start_judgement_phase()
