from __future__ import print_function, unicode_literals
import random
from pprint import pprint
from PyInquirer import prompt, Separator
from examples import custom_style_2


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
    if (self.character_ability5 == None) and (self.character_ability4 == None) and (self.character_ability3 == None) and (self.character_ability2 == None):
        return f"   - {self.character_ability1}"
    elif (self.character_ability5 == None) and (self.character_ability4 == None) and (self.character_ability3 == None):
        return f"   - {self.character_ability1} \n   - {self.character_ability2}"
    elif (self.character_ability5 == None) and (self.character_ability4 == None):
        return f"   - {self.character_ability1} \n   - {self.character_ability2} \n   - {self.character_ability3}"
    elif (self.character_ability5 == None):
        return f"   - {self.character_ability1} \n   - {self.character_ability2} \n   - {self.character_ability3} \n   - {self.character_ability4}"
    else:
        return f"   - {self.character_ability1} \n   - {self.character_ability2} \n   - {self.character_ability3} \n   - {self.character_ability4} \n   - {self.character_ability5}"


def check_allegiances_in_play():
    allegiances = []
    for player in players:
        allegiances.append(player.allegiance)
    allegiances = set(allegiances)
    return len(allegiances)


# A class for handling individual characters
class Character:
    def __init__(self, character, allegiance, health, gender, character_ability1, character_ability2=None, character_ability3=None, character_ability4=None, character_ability5=None):
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
        if (self.character_ability5 == None) and (self.character_ability4 == None) and (self.character_ability3 == None) and (self.character_ability2 == None):
            return f"   - {self.character_ability1}"
        elif (self.character_ability5 == None) and (self.character_ability4 == None) and (self.character_ability3 == None):
            return f"   - {self.character_ability1} \n   - {self.character_ability2}"
        elif (self.character_ability5 == None) and (self.character_ability4 == None):
            return f"   - {self.character_ability1} \n   - {self.character_ability2} \n   - {self.character_ability3}"
        elif (self.character_ability5 == None):
            return f"   - {self.character_ability1} \n   - {self.character_ability2} \n   - {self.character_ability3} \n   - {self.character_ability4}"
        else:
            return f"   - {self.character_ability1} \n   - {self.character_ability2} \n   - {self.character_ability3} \n   - {self.character_ability4} \n   - {self.character_ability5}"


# A class for handling the character-deck (mostly for selection purposes and Zuo Ci)
class CharacterDeck:
    def __init__(self, character_deck):
        self.contents = []
        self.contents = character_deck

    def list_characters(self):
        output = []
        for card in self.contents:
            output.append(str(card))
        return output

    def add_to_top(self, card):
        self.contents.insert(0, card)

    def shuffle(self):
        random.shuffle(self.contents)

    def view(self, num=1):
        for card in self.contents[:num]:
            print(' ')
            print(card)


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
              "Garden of Lust: Whenever you use an ATTACK on a female character or vice-versa, the targeted character needs to use two DODGE cards to successfully evade the attack.",
              "Disintegrate: At the end of every turn, if your health is not the least or among the least, you must either lose one unit of health, or reduce your maximum health by one unit.",
              "Tyrant (Ruler Ability): Whenever another Hero character causes damage to any other player, you can flip a judgement card. If the judgement card is of the suit SPADES, you can regain one unit of health."),
    Character("Yuan Shao", "Heroes", 4, "Male",
              "Random Strike: You can use any two hand-cards which have the same suit as RAIN OF ARROWS.",
              "Bloodline (Ruler Ability): Your maximum hand-limit is increased by two for each other Hero character still alive."),
    Character("Zhang Jiao", "Heroes", 3, "Male",
              "Lightning Strike: Whenever you use a DODGE card, you can target any other player to make a judgement. If the judgement card is of the suit SPADES, the target player suffers two points of lightning damage.",
              "Dark Sorcery: You can exchange the judgement card of any player before it takes effect, with any of your CLUBS or SPADES, either on-hand or equipped.",
              "Amber Sky (Ruler Ability): All Hero characters can give you a DODGE or LIGHTNING card during their individual turns.")
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
              "Impetus: Every one of your black-suited on-hand cards may be used as DODGE.",
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
              "Heavenly Scent: Whenever you recieve damage, you can choose to pass the damage onto any other player by discarding an on-hand card that has the suit HEARTS. The victim that recieves the damage gets to draw X number of cards from the deck, X being the amount of health missing from the maximum level after damage.",
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
              "Descend into Chaos (Single-Use Ability): During your action phase, you can force every player, other than yourself, to use an ATTACK on another player with the least distance away. If a player is unable to do so, the player will lose one unit of health. Recipients of the ATTACK need to DEFEND to evade. This ability will proceed in succession starting from the player on your right.",
              "Behind the Curtain: You cannot become the target of any black-suited tool cards."),
    Character("Ling Ju", "Heroes", 3, "Female",
              "Deplete Karma: Whenever you are damaged by another player whose health level is greater than your own, you can discard a red-suited hand-card to reduce the damage by one. If you damage another player whose health is no lower than your own, you can discard black-suited hand-card to increase the damage by one.",
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

    def show_hand(self, *char_name):
        pass

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

    def give_to_player(self, card):
        pass


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
        self.rites = []
        self.terrains = []
        self.previous_turn_health = None

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

# In-game checks
    def calculate_targets_in_physical_range(self, player_index):
        output = []
        for (target_index, target) in enumerate(players):
            if target_index != player_index:
                distance = abs(target_index - player_index)
                if distance > len(players) / 2:
                    distance = len(players) - distance
                if distance - (players[player_index].check_horsemanship() + (len(players[player_index].equipment_offensive_horse) + 1)) + (len(target.equipment_defensive_horse)) <= 0:
                    output.append(target_index)
        return output

    def calculate_targets_in_extended_physical_range(self, player_index):
        output = []
        for (target_index, target) in enumerate(players):
            if target_index != player_index:
                distance = abs(target_index - player_index)
                if distance > len(players) / 2:
                    distance = len(players) - distance
                if distance - (players[player_index].check_horsemanship() + (len(players[player_index].equipment_offensive_horse) + 2)) + (len(target.equipment_defensive_horse)) <= 0:
                    output.append(target_index)
        return output

    def calculate_targets_in_weapon_range(self, player_index):
        output = []
        for (target_index, target) in enumerate(players):
            if target_index != player_index:
                distance = abs(target_index - player_index)
                if distance > len(players) / 2:
                    distance = len(players) - distance
                if distance - (players[player_index].check_horsemanship() + (len(players[player_index].equipment_offensive_horse)) + (players[player_index].weapon_range)) + (len(target.equipment_defensive_horse)) <= 0:
                    output.append(target_index)
        return output

    def create_targeting_menu(self, range_type="Weapon"):
        if range_type == "Physical":
            if self.check_talent():
                output_str = [
                    Separator("------<Cannot target yourself>------")]
                for player in players[1:]:
                    output_str.append(str(player))
                return (output_str)
            reachable_indexes = self.calculate_targets_in_physical_range(0)
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

        if range_type == "Extended Physical":
            reachable_indexes = self.calculate_targets_in_extended_physical_range(
                0)
            if self.check_talent():
                output_str = [
                    Separator("------<Cannot target yourself>------")]
                for player in players[1:]:
                    output_str.append(str(player))
                return (output_str)
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
            reachable_indexes = self.calculate_targets_in_weapon_range(0)
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

    def check_activatable_abilities(self):
        return ["Character_Ability_X", "Character_Ability_Y", "Character_Ability_Z"]

    def check_break_brink_loop(self, amount_healed):
        if self.current_health < (0 + amount_healed):
            return True
        else:
            return False

    def check_brink_of_death_loop(self, dying_player_index=0, source_player_index=0):
        if dying_player_index == None:
            dying_player_index = 0
        if source_player_index == None:
            source_player_index = 0
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
            if self.current_health < 1:
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
            else:
                print(
                    f"{players[dying_player_index].character} has been successfully healed back to {players[dying_player_index].current_health}/{players[dying_player_index].max_health} HP.")

    def check_pending_judgements(self):
        if self.pending_judgements == []:
            pass
        else:
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
                    # Add checks for Sima Yi and Zhang Jiao
                    self.check_envy_of_heaven()
                    if judgement_card.suit == "Hearts":
                        print(
                            f"{self.character}'s judgement card is a {judgement_card} and therefore {pending_judgement} has no effect.")
                    else:
                        print(
                            f"{self.character}'s judgement card is a {judgement_card} and thus they miss their action-phase of this turn.")
                        # SKIP ACTION PHASE OF TURN!
                        self.acedia_active = True
                    discard_deck.add_to_top(pending_judgement)
                if pending_judgement.effect2 == 'Lightning':
                    print(
                        f"{self.character} must face judgement for LIGHTNING; (needs anything but TWO to NINE of SPADES or else they suffer THREE points of lightning damage)! If no hit, LIGHTNING will pass onto {players[1].character}.")
                    main_deck.discard_from_deck()
                    judgement_card = discard_deck.contents[0]
                    print(f"{self.character} flipped a {judgement_card}.")
                    # Add checks for Sima Yi and Zhang Jiao
                    self.check_envy_of_heaven()
                    if judgement_card.suit == "Spades" and (10 > judgement_card.rank > 1):
                        print(
                            f"{self.character}'s judgement card is a {judgement_card} and therefore {pending_judgement} deals THREE DAMAGE!")
                        self.current_health -= 3
                        if self.current_health < 1:
                            if self.check_brink_of_death_loop(0, "None") == "Break":
                                return "Break"
                        self.check_eternal_loyalty(3)
                        discard_deck.add_to_top(pending_judgement)
                    elif len(players[1].pending_judgements) > 0:
                        for possible_lightning in players[1].pending_judgements:
                            if possible_lightning.effect2 == 'Lightning':
                                if len(players) < 3:
                                    print(
                                        f"{self.character}'s judgement card is a {judgement_card}, but there are no other players to pass to, so it gets discarded.")
                                    discard_deck.add_to_top(pending_judgement)
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
                    # Add checks for Sima Yi and Zhang Jiao
                    self.check_envy_of_heaven()
                    if judgement_card.suit == "Clubs":
                        print(
                            f"{self.character}'s judgement card is a {judgement_card} and therefore {pending_judgement} has no effect.")
                    else:
                        print(
                            f"{self.character}'s judgement card is a {judgement_card} and thus they miss their drawing-phase of this turn.")
                        # SKIP DRAWING PHASE OF TURN!
                        self.rations_depleted_active = True
                    discard_deck.add_to_top(pending_judgement)

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

    def create_str_nonblind_menu(self, append_judgements=False, omit_item=None):
        cards_discardable = (len(self.hand_cards.contents) + len(self.equipment_weapon) + len(
            self.equipment_armor) + len(self.equipment_offensive_horse) + len(self.equipment_defensive_horse))
        if append_judgements == 1:
            cards_discardable += len(self.pending_judgements)
        if cards_discardable > 0:
            options_str = []
            options_str.append(
                Separator("-----------------HAND--CARDS-----------------"))
            for card in self.hand_cards.contents:
                options_str.append(str(card))
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
                player.check_unnatural_death(cards_discarded)
            while len(self.pending_judgements) > 0:
                discard_deck.add_to_top(self.pending_judgements.pop())

    def reset_once_per_turn(self):
        self.attacks_this_turn = 0
        self.used_green_salve = False

# Equipment-card checks
    def armor_black_shield(self, attack_card):
        if len(self.equipment_armor) > 0:
            if self.equipment_armor[0].effect == "Black Shield":
                if attack_card.suit == "Spades" or attack_card.suit == "Clubs":
                    print(
                        f"  >> {self.character} has {self.equipment_armor[0]} equipped, and therefore CANNOT be affected by black attack cards. ({attack_card} discarded as normal)")
                    return True
            else:
                return False

    def armor_eight_trigrams(self):
        if len(self.equipment_armor) > 0:
            if self.equipment_armor[0].effect == "Eight-Trigrams":
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
                    # Add checks for Sima Yi and Zhang Jiao
                    self.check_envy_of_heaven()
                    if judgement_card.suit == "Hearts" or "Diamonds":
                        return (True, judgement_card)
                    else:
                        return (False, None)
        else:
            return (False, None)

    def check_weapon_axe(self, target_index=0):
        if target_index == None:
            target_index = 0
        if len(self.equipment_weapon) > 0:
            if self.equipment_weapon[0].effect == "Axe":
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
                            False, omit_item="Weapon")
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
                        players[target_index].current_health -= damage_dealt
                        print(
                            f"  >> {self.character} has forced the damage to {players[target_index].character}, by using {self.equipment_weapon[0]}, and discarding two cards ({players[target_index].current_health}/{players[target_index].max_health} HP remaining).")
                        self.check_insanity(target_index)
                        for player_index, player in enumerate(players):
                            if player.current_health < 1:
                                if players[player_index].check_brink_of_death_loop(player_index, 0) == "Break":
                                    return "Break"
                        players[target_index].check_eternal_loyalty(
                            damage_dealt)
                        if players[target_index].check_eye_for_an_eye(
                                source_player_index=0, mode="Activate") == "Break":
                            return "Break"
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
                    selected_1 = answer.get('Selected')
                    options.pop(selected_1)
                    options.insert(selected_1, Separator(
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
                            f"  >> {self.character} used the Sky Scorcher Halberd to hit an extra player, {players[selected_1].character}!!!")
                        return [1, selected_1]
                    selected_2 = answer.get('Selected')
                    print(
                        f"  >> {self.character} used the Sky Scorcher Halberd to hit two extra players, {players[selected_1].character} and {players[selected_2].character}!!!")
                    return [2, selected_1, selected_2]

    def check_weapon_zhuge_crossbow(self):
        if len(self.equipment_weapon) > 0:
            if self.equipment_weapon[0].effect == "Zhuge Crossbow":
                print(
                    f"  >> {self.character} has {self.equipment_weapon[0]} equipped, and therefore has no limit to the amount of attacks per turn.")
                return True

# Still TO DO:
    def check_weapon_serpent_spear(self):
        pass

# Using/discarding cards from a players' hand
    def use_card_effect(self, card_index, card):
        print(" ")
        popping = False
        # card.type == 'Basic':
        if card.effect2 == 'Attack':
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

                    print(f"{card} - Once per turn, you can use this card to attack any player within your attacking range. They must play a DEFEND or else suffer one damage.")
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
                else:
                    print(
                        f"{self.character}: You have insufficient range to reach anyone with {card}.")
            elif (self.attacks_this_turn > 0):
                print(
                    f"{self.character}: You can only play one ATTACK card per turn.")

        if card.effect2 == 'Defend':
            print(
                f"{self.character}: {card} can only be played as a reaction.")

        if card.effect2 == 'Peach':
            if self.max_health > self.current_health:
                print(f"{card} - During your turn, you can use this card to recover one unit of missing health. Additionally, whenever a player is on the brink of death, any player can use a PEACH to make them recover one unit of health.")
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
        if card.effect2 == 'Barbarians':
            pass

        if card.effect2 == 'Granary':
            pass

        if card.effect2 == 'Peach Gardens':
            print(f"{card} - {card.flavour_text}")
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
                        current_health += 1
                        print(
                            f"{player.character} has been healed by one. ({player.current_health}/{player.max_health} HP remaining)")

        if card.effect2 == 'Rain of Arrows':
            print(f"{card} - {card.flavour_text}")
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
                    f"{self.character} has activated {card}. All damaged players will take one damage (unless defended or negated).")
                discarded = self.hand_cards.contents.pop(card_index)
                self.check_one_after_another()
                self.check_wisdom()
                discard_deck.add_to_top(discarded)
                for player in players[1:]:
                    roa_response = player.use_reaction_effect(
                        "Defend", discarded, 0, player)
                    if type(roa_response) == Card:
                        if (roa_response.effect == "Defend") or (roa_response.effect2 == "Defend"):
                            print(
                                f"{player.character} successfully response {discarded} with {roa_response}.")
                    else:
                        print(
                            f"{player.character} failed to defend from {discarded}, and takes one damage ({player.current_health}/{player.max_health} HP remaining).")
                        player.current_health -= 1
                        self.check_insanity(player)
                        if player.current_health < 1:
                            for player_index, player in enumerate(players[player_index:]):
                                if player.current_health < 1:
                                    players[player_index].check_brink_of_death_loop(
                                        player_index, 0)
                            for player_index, player in enumerate(players[:player_index]):
                                if player.current_health < 1:
                                    players[player_index].check_brink_of_death_loop(
                                        player_index, 0)
                        if player.current_health > 0:
                            players[player].check_eternal_loyalty(1)
                        if players[player].check_eye_for_an_eye(source_player_index=0, mode="Activate") == "Break":
                            break
                        players[player].check_plotting_for_power(
                            1, mode="Reaction")
                        players[player].check_retaliation(0, 1)

        if card.effect2 == 'Coerce':
            pass

        if card.effect2 == 'Dismantle':
            options_str = list_character_options(players[::])
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
                f"{card} - You can target any player and discard one of their cards, on-hand or equipped.")
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
                cards_discardable = (len(players[selected].hand_cards.contents) + len(players[selected].equipment_weapon) + len(
                    players[selected].equipment_armor) + len(players[selected].equipment_offensive_horse) + len(players[selected].equipment_defensive_horse) + len(players[selected].pending_judgements))

                if cards_discardable == 0:
                    print(
                        f"{players[selected].character} has no cards that can be dismantled.")
                    return False

                if cards_discardable > 0:
                    if players[selected] == players[0]:
                        options_str = players[0].create_str_nonblind_menu(True)
                    else:
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

        if card.effect2 == 'Duel':
            pass

        if card.effect2 == 'Negate':
            print(
                f"{self.character}: {card} can only be played as a reaction.")

        if card.effect2 == 'Greed':
            print(f"{card} - {card.flavour_text}")
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

        if card.effect2 == 'Steal':
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

                print(f"{card} - You can use this card on a player within physical range to take a card from them (on-hand or equipped) and add it to your hand.")
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
        if card.effect2 == 'Acedia':
            options_str = []
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
            selected = ((answer.get('Selected')) + 1)
            if players[selected].check_humility():
                return (' ')

            print(f"{card} - You can place Delay-Tool on any other player. The target must perform a judgement for this card. If it is not HEARTS, they forfeit their action-phase.")
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

        if card.effect2 == 'Lightning':
            for possible_lightning in self.pending_judgements:
                if possible_lightning.effect2 == 'Lightning':
                    print(
                        f"{self.character}: You cannot play a LIGHTNING when you already have one active on yourself.")
            else:

                print(f"{card} - {card.flavour_text}")
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
                    if card_index == "Special":
                        pass
                    else:
                        discarded = self.hand_cards.contents.pop(
                            card_index)
                    self.check_one_after_another()
                    self.pending_judgements.append(card)
                    print(f"{self.character} has called {card}.")

        if card.effect2 == 'Rations Depleted':
            choices_index = self.calculate_targets_in_extended_physical_range(
                0)

            if len(choices_index) > 0:
                options_str = self.create_targeting_menu("Extended Physical")
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

                print(f"{card} - You can place Delay-Tool on any other player in physical range. The target must perform a judgement for this card. If it is not CLUBS, they forfeit their draw-phase.")
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

    def activate_attack(self, discarded, selected):
        if players[selected].check_relish(source_player_index=0, mode="Activate"):
            return(' ')
        self.check_weapon_gender_swords(selected)
        if self.check_weapon_black_pommel():
            print(
                f"  >> {self.character} has {self.equipment_weapon[0]} equipped, and therefore ignores any armor when attacking.")
        elif players[selected].armor_black_shield(discarded):
            return(' ')
        if self.check_fearsome_archer(discarded, selected):
            return(' ')
        if self.check_iron_cavalry(discarded, selected):
            return(' ')
        attack_defended = players[selected].use_reaction_effect(
            "Defend", discarded, 0, selected)
        if type(attack_defended) == Card:
            if (attack_defended.effect == "Defend") or (attack_defended.effect2 == "Defend"):
                print(
                    f"{players[selected].character} successfully defended the attack with {attack_defended}.")
                self.check_weapon_axe(selected)
                self.check_fearsome_advance(
                    discarded, selected)
                players[selected].check_lightning_strike()
                self.check_weapon_green_dragon_halberd(selected)
            elif attack_defended.effect == 0:
                pass
        else:
            if self.check_weapon_frost_blade(selected, "Check"):
                return(' ')
            if self.check_backstab(discarded, selected):
                return(' ')
            if players[selected].check_reckless(discarded, 0):
                return(' ')
            damage_dealt = 1
            players[selected].current_health -= damage_dealt
            print(
                f"{self.character} attacked {players[selected].character}, dealing {damage_dealt} damage. ({players[selected].current_health}/{players[selected].max_health} HP remaining)")
            self.check_weapon_huangs_longbow(selected)
            self.check_insanity(selected)
            for player_index, player in enumerate(players):
                if player.current_health < 1:
                    if players[player_index].check_brink_of_death_loop(player_index, 0) == "Break":
                        return "Break"
            players[selected].check_eternal_loyalty(
                damage_dealt)
            if players[selected].check_eye_for_an_eye(
                    source_player_index=0, mode="Activate") == "Break":
                return(' ')
            players[selected].check_plotting_for_power(
                damage_dealt, mode="Reaction")
            players[selected].check_retaliation(0, damage_dealt)

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
                if self.check_first_aid(player_index, "Check"):
                    options_str.append("  >> Character Ability: First Aid")
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
                elif options_str[card_index] == "  >> Character Ability: First Aid":
                    if (self.check_first_aid(player_index, "Activate")):
                        output_value += 1
                        bonus_output = players[player_index].check_rescued(
                            reacting_player_index)
                        if bonus_output == 1:
                            output_value += bonus_output
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
                    if players[player_index].check_break_brink_loop(output_value):
                        reactions_possible = False
                        return(output_value)

            elif response_required == "Defend" and card_played.effect2 == "Attack":
                self.check_ardour(card_played)

                if not players[player_index].check_weapon_black_pommel():
                    armor_check = self.armor_eight_trigrams(
                    )
                    if armor_check[0]:
                        return(armor_check[1])

                options_str = self.hand_cards.list_cards()
                options_str.append(
                    Separator("--------------------Other--------------------"))
                if self.check_impetus(player_index, "Check"):
                    options_str.append("  >> Character Ability: Impetus")
                options_str.append("Do nothing.")

                question = [
                    {
                        'type': 'list',
                        'name': 'Selected',
                        'message': f"{self.character}: You are being attacked by {players[player_index].character} using {card_played}; please choose a response (a DEFEND card or do nothing)!",
                        'choices': options_str,
                        'filter': lambda card: options_str.index(card)
                    },
                ]
                answer = prompt(question, style=custom_style_2)
                card_index = answer.get('Selected')
                if options_str[card_index] == "Do nothing.":
                    reactions_possible = False
                    return(0)

                elif options_str[card_index] == "  >> Character Ability: Impetus":
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

            elif response_required == "Defend" and card_played.effect2 == "Rain of Arrows":

                options_str = self.hand_cards.list_cards()
                options_str.append(
                    Separator("--------------------Other--------------------"))
                if self.check_impetus(player_index, "Check"):
                    options_str.append("  >> Character Ability: Impetus")
                options_str.append("Do nothing.")

                question = [
                    {
                        'type': 'list',
                        'name': 'Selected',
                        'message': f"{self.character}: You are being attacked by {players[player_index].character} using {card_played}; please choose a response (a DEFEND card or do nothing)!",
                        'choices': options_str,
                        'filter': lambda card: options_str.index(card)
                    },
                ]
                answer = prompt(question, style=custom_style_2)
                card_index = answer.get('Selected')
                if options_str[card_index] == "Do nothing.":
                    reactions_possible = False
                    return(0)

                elif options_str[card_index] == "  >> Character Ability: Impetus":
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
                    self.check_warrior_woman()

                if discarded_index == (len(self.hand_cards.contents) + 3):
                    card = self.equipment_armor.pop()
                    discard_deck.add_to_top(card)
                    print(
                        f"{self.character} has discarded {card} from their armor-slot.")
                    self.check_warrior_woman()

                if discarded_index == (len(self.hand_cards.contents) + 4):
                    card = self.equipment_offensive_horse.pop()
                    discard_deck.add_to_top(card)
                    print(
                        f"{self.character} has discarded {card} from their horse-slot.")
                    self.check_warrior_woman()

                if discarded_index == (len(self.hand_cards.contents) + 5):
                    card = self.equipment_defensive_horse.pop()
                    discard_deck.add_to_top(card)
                    print(
                        f"{self.character} has discarded {card} from their horse-slot.")
                    self.check_warrior_woman()
            num -= 1

# Ability checks
    def check_ardour(self, card):
        if (self.character_ability1 == "Ardour: Whenever you use or become the target of any DUEL or red-suited ATTACK cards, you can draw a card." or self.character_ability2 == "Ardour: Whenever you use or become the target of any DUEL or red-suited ATTACK cards, you can draw a card." or self.character_ability3 == "Ardour: Whenever you use or become the target of any DUEL or red-suited ATTACK cards, you can draw a card." or self.character_ability4 == "Ardour: Whenever you use or become the target of any DUEL or red-suited ATTACK cards, you can draw a card." or self.character_ability5 == "Ardour: Whenever you use or become the target of any DUEL or red-suited ATTACK cards, you can draw a card."):
            if (card.effect == "Duel") or (card.effect == "Attack" and (card.suit == "Hearts" or card.suit == "Diamonds")):
                print(
                    f"  >> Character Ability: Ardour; {self.character} used or was target of {card} (a DUEL or red-suited ATTACK). He draws a card.")
                self.hand_cards.draw(main_deck, 1, False)

    def check_backstab(self, discarded, selected_index=0):
        if selected_index == None:
            selected_index = 0
        if (self.character_ability1 == "Backstab: Whenever you use an ATTACK to cause damage to a player within your physical range, you can flip a judgement card. If the judgement is not HEARTS, no damage is caused, and instead you cause the target to reduce their maximum health by 1." or self.character_ability2 == "Backstab: Whenever you use an ATTACK to cause damage to a player within your physical range, you can flip a judgement card. If the judgement is not HEARTS, no damage is caused, and instead you cause the target to reduce their maximum health by 1." or self.character_ability3 == "Backstab: Whenever you use an ATTACK to cause damage to a player within your physical range, you can flip a judgement card. If the judgement is not HEARTS, no damage is caused, and instead you cause the target to reduce their maximum health by 1." or self.character_ability4 == "Backstab: Whenever you use an ATTACK to cause damage to a player within your physical range, you can flip a judgement card. If the judgement is not HEARTS, no damage is caused, and instead you cause the target to reduce their maximum health by 1." or self.character_ability5 == "Backstab: Whenever you use an ATTACK to cause damage to a player within your physical range, you can flip a judgement card. If the judgement is not HEARTS, no damage is caused, and instead you cause the target to reduce their maximum health by 1."):
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
                    # Add checks for Sima Yi and Zhang Jiao
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
                        players[selected_index].current_health -= damage_dealt
                        print(
                            f"{self.character}'s judgement card is a {judgement_card} and therefore Backstab does not apply. Damage dealt as normal; {damage_dealt} damage to {players[selected_index].character}. ({players[selected_index].current_health}/{players[selected_index].max_health} HP remaining)")
                        for player_index, player in enumerate(players):
                            if player.current_health < 1:
                                players[player_index].check_brink_of_death_loop(
                                    player_index, 0)
                    return True

    def check_berserk(self):
        if (self.character_ability1 == "Berserk: There is no limit on how many times you can ATTACK during your turn." or self.character_ability2 == "Berserk: There is no limit on how many times you can ATTACK during your turn." or self.character_ability3 == "Berserk: There is no limit on how many times you can ATTACK during your turn." or self.character_ability4 == "Berserk: There is no limit on how many times you can ATTACK during your turn." or self.character_ability5 == "Berserk: There is no limit on how many times you can ATTACK during your turn."):
            print(
                f"  >> Character Ability: Berserk; {self.character} has no limit to the amount of attacks they can play.")
            return True

    def check_bloodline(self):
        if (self.role == 'Emperor') or (self.character_ability2 == "False Ruler: You possess the same ruler ability as the current emperor."):
            if (self.character_ability1 == "Bloodline (Ruler Ability): Your maximum hand-limit is increased by two for each other Hero character still alive." or self.character_ability2 == "Bloodline (Ruler Ability): Your maximum hand-limit is increased by two for each other Hero character still alive." or self.character_ability3 == "Bloodline (Ruler Ability): Your maximum hand-limit is increased by two for each other Hero character still alive." or self.character_ability4 == "Bloodline (Ruler Ability): Your maximum hand-limit is increased by two for each other Hero character still alive." or self.character_ability5 == "Bloodline (Ruler Ability): Your maximum hand-limit is increased by two for each other Hero character still alive."):
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
        if dying_player_index == None:
            dying_player_index = 0
        if (self.character_ability1 == "Burning Heart (Single-Use Ability): When you kill another character, you can exchange role cards with the player you just killed. You cannot activate this ability if you are the emperor, or just killed the emperor." or self.character_ability2 == "Burning Heart (Single-Use Ability): When you kill another character, you can exchange role cards with the player you just killed. You cannot activate this ability if you are the emperor, or just killed the emperor." or self.character_ability3 == "Burning Heart (Single-Use Ability): When you kill another character, you can exchange role cards with the player you just killed. You cannot activate this ability if you are the emperor, or just killed the emperor." or self.character_ability4 == "Burning Heart (Single-Use Ability): When you kill another character, you can exchange role cards with the player you just killed. You cannot activate this ability if you are the emperor, or just killed the emperor." or self.character_ability5 == "Burning Heart (Single-Use Ability): When you kill another character, you can exchange role cards with the player you just killed. You cannot activate this ability if you are the emperor, or just killed the emperor."):
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
        if self.character_ability2 == "Conduit (Awakening Ability): At the beginning of your turn, if you have three or more TERRAINS, you must reduce your maximum health by one unit. You then permanently gain the ability 'Blitz'.":
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

    def check_dashing_hero(self):
        if (self.character_ability1 == "Dashing Hero: Draw an extra card at the start of your turn." or self.character_ability2 == "Dashing Hero: Draw an extra card at the start of your turn." or self.character_ability3 == "Dashing Hero: Draw an extra card at the start of your turn." or self.character_ability4 == "Dashing Hero: Draw an extra card at the start of your turn." or self.character_ability5 == "Dashing Hero: Draw an extra card at the start of your turn."):
            print(
                f"  >> Character Ability: Dashing Hero; {self.character} draws an extra card from the deck in their drawing phase.")
            return True

    def check_disintegrate(self):
        if (self.character_ability1 == "Disintegrate: At the end of every turn, if your health is not the least or among the least, you must either lose one unit of health, or reduce your maximum health by one unit." or self.character_ability2 == "Disintegrate: At the end of every turn, if your health is not the least or among the least, you must either lose one unit of health, or reduce your maximum health by one unit." or self.character_ability3 == "Disintegrate: At the end of every turn, if your health is not the least or among the least, you must either lose one unit of health, or reduce your maximum health by one unit." or self.character_ability4 == "Disintegrate: At the end of every turn, if your health is not the least or among the least, you must either lose one unit of health, or reduce your maximum health by one unit." or self.character_ability5 == "Disintegrate: At the end of every turn, if your health is not the least or among the least, you must either lose one unit of health, or reduce your maximum health by one unit."):
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

    def check_divinity(self):
        if self.character_ability2 == "Divinity (Awakening Ability): If, at the start of your turn, your health is one unit, you must reduce your maximum health by one. After which you permanently gain the abilities 'Dashing Hero' and 'Lingering Spirit'.":
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

    def check_eclipse_the_moon(self):
        if (self.character_ability2 == "Eclipse the Moon: At the end of your turn, you may draw an additional card from the deck." or self.character_ability3 == "Eclipse the Moon: At the end of your turn, you may draw an additional card from the deck." or self.character_ability4 == "Eclipse the Moon: At the end of your turn, you may draw an additional card from the deck." or self.character_ability5 == "Eclipse the Moon: At the end of your turn, you may draw an additional card from the deck."):
            print(
                f"  >> Character Ability: Eclipse the Moon; {self.character} draws an extra card from the deck in their end-phase.")
            self.hand_cards.draw(main_deck, 1, False)

    def check_eiron(self):
        if (self.role == 'Emperor') or (self.character_ability2 == "False Ruler: You possess the same ruler ability as the current emperor.") or (self.character_ability3 == "False Ruler: You possess the same ruler ability as the current emperor."):
            if (self.character_ability3 == "Eiron (Awakening/Ruler Ability): At the start of your turn, if your health is the least or among the least, you must raise your maximum health by one unit, regain one unit of health, and permanently gain the ability 'Rouse'." or self.character_ability4 == self.character_ability3 == "Eiron (Awakening/Ruler Ability): At the start of your turn, if your health is the least or among the least, you must raise your maximum health by one unit, regain one unit of health, and permanently gain the ability 'Rouse'."):
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
        if (self.character_ability1 == "Empty City: When you have no hand-cards, you cannot become the target of an ATTACK or a DUEL." or self.character_ability2 == "Empty City: When you have no hand-cards, you cannot become the target of an ATTACK or a DUEL." or self.character_ability3 == "Empty City: When you have no hand-cards, you cannot become the target of an ATTACK or a DUEL." or self.character_ability4 == "Empty City: When you have no hand-cards, you cannot become the target of an ATTACK or a DUEL." or self.character_ability5 == "Empty City: When you have no hand-cards, you cannot become the target of an ATTACK or a DUEL."):
            if len(self.hand_cards.contents) == 0:
                print(
                    f"  >> Character Ability; Empty City: {self.character} has no hand-cards, and therefore cannot be targeted by ATTACK or DUEL.")
                return True

    def check_envy_of_heaven(self):
        if (self.character_ability1 == "Envy of Heaven: You can obtain any judgement card that you flip over." or self.character_ability2 == "Envy of Heaven: You can obtain any judgement card that you flip over." or self.character_ability3 == "Envy of Heaven: You can obtain any judgement card that you flip over." or self.character_ability4 == "Envy of Heaven: You can obtain any judgement card that you flip over." or self.character_ability5 == "Envy of Heaven: You can obtain any judgement card that you flip over."):
            print(
                f"  >> Character Ability: Envy of Heaven; The top judgement card has been added to {self.character}'s hand before it takes effect.")
            self.hand_cards.draw(discard_deck, 1, False)

    def check_eternal_loyalty(self, damage_dealt):
        if (self.character_ability1 == "Eternal Loyalty: For every one unit of damage you suffer, you can allow any player of your choice (including yourself) to replenish that player’s on-hand cards to their maximum health level." or self.character_ability2 == "Eternal Loyalty: For every one unit of damage you suffer, you can allow any player of your choice (including yourself) to replenish that player’s on-hand cards to their maximum health level." or self.character_ability3 == "Eternal Loyalty: For every one unit of damage you suffer, you can allow any player of your choice (including yourself) to replenish that player’s on-hand cards to their maximum health level." or self.character_ability4 == "Eternal Loyalty: For every one unit of damage you suffer, you can allow any player of your choice (including yourself) to replenish that player’s on-hand cards to their maximum health level." or self.character_ability5 == "Eternal Loyalty: For every one unit of damage you suffer, you can allow any player of your choice (including yourself) to replenish that player’s on-hand cards to their maximum health level."):
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
                    Separator("--------------------OTHER--------------------"))
                options.append("Blank")
                options_str.append("Cancel")
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

    def check_eye_for_an_eye(self, source_player_index=0, mode="Activate"):
        if source_player_index == None:
            source_player_index = 0
        for player_index, player in enumerate(players):
            if (player.character_ability1 == "Eye for an Eye: For every instance that you suffer damage, you can flip a judgement card. If the judgement is not HEARTS, the character that damaged you must choose between the following options; lose one unit of health, or discard any two on-hand cards." or player.character_ability2 == "Eye for an Eye: For every instance that you suffer damage, you can flip a judgement card. If the judgement is not HEARTS, the character that damaged you must choose between the following options; lose one unit of health, or discard any two on-hand cards." or player.character_ability3 == "Eye for an Eye: For every instance that you suffer damage, you can flip a judgement card. If the judgement is not HEARTS, the character that damaged you must choose between the following options; lose one unit of health, or discard any two on-hand cards." or player.character_ability4 == "Eye for an Eye: For every instance that you suffer damage, you can flip a judgement card. If the judgement is not HEARTS, the character that damaged you must choose between the following options; lose one unit of health, or discard any two on-hand cards." or player.character_ability5 == "Eye for an Eye: For every instance that you suffer damage, you can flip a judgement card. If the judgement is not HEARTS, the character that damaged you must choose between the following options; lose one unit of health, or discard any two on-hand cards."):
                retaliator_index = player_index
        if (self.character_ability1 == "Eye for an Eye: For every instance that you suffer damage, you can flip a judgement card. If the judgement is not HEARTS, the character that damaged you must choose between the following options; lose one unit of health, or discard any two on-hand cards." or self.character_ability2 == "Eye for an Eye: For every instance that you suffer damage, you can flip a judgement card. If the judgement is not HEARTS, the character that damaged you must choose between the following options; lose one unit of health, or discard any two on-hand cards." or self.character_ability3 == "Eye for an Eye: For every instance that you suffer damage, you can flip a judgement card. If the judgement is not HEARTS, the character that damaged you must choose between the following options; lose one unit of health, or discard any two on-hand cards." or self.character_ability4 == "Eye for an Eye: For every instance that you suffer damage, you can flip a judgement card. If the judgement is not HEARTS, the character that damaged you must choose between the following options; lose one unit of health, or discard any two on-hand cards." or self.character_ability5 == "Eye for an Eye: For every instance that you suffer damage, you can flip a judgement card. If the judgement is not HEARTS, the character that damaged you must choose between the following options; lose one unit of health, or discard any two on-hand cards."):
            if mode == "Activate":
                print(' ')
                question = [
                    {
                        'type': 'list',
                        'name': 'Selected',
                        'message': f'{self.character}: Choose to activate Eye for an Eye, and and force {players[source_player_index].character} to either take one damage or discard two hand-cards?',
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
                # Add checks for Sima Yi and Zhang Jiao
                if judgement_card.suit != "Hearts":
                    print(
                        f"{self.character}'s judgement card is a {judgement_card} and therefore {players[source_player_index].character} must suffer one damage or discard two hand-cards.")
                    players[source_player_index].check_eye_for_an_eye(
                        retaliator_index, "Reaction")
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
                self.current_health -= 1
                print(
                    f"{self.character} suffered one damage from {players[retaliator_index].character}'s an Eye for an Eye ({self.current_health}/{self.max_health} HP remaining).")
                for player_index, player in enumerate(players):
                    if player.current_health < 1:
                        if players[player_index].check_brink_of_death_loop(player_index, retaliator_index) == "Break":
                            return "Break"
                self.check_eternal_loyalty(1)
                self.check_retaliation(retaliator_index, 1)
                self.check_plotting_for_power(1, "Reaction")
            if answer.get('Selected') == 'Discard two cards.':
                self.hand_cards.discard_from_hand(2)
                print(
                    f"{self.character} discarded two hand-cards due to {players[retaliator_index].character}'s an Eye for an Eye.")
                self.check_one_after_another()

    def check_false_ruler(self):
        if self.character_ability2 == "False Ruler: You possess the same ruler ability as the current emperor.":
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
                        self.character_ability3 = "Amber Sky (Ruler Ability): All Hero characters can give you a DODGE or LIGHTNING card during their individual turns."
        elif self.character_ability3 == "False Ruler: You possess the same ruler ability as the current emperor.":
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
                        self.character_ability4 = "Amber Sky (Ruler Ability): All Hero characters can give you a DODGE or LIGHTNING card during their individual turns."

    def check_fearsome_advance(self, discarded, selected_index=0):
        if selected_index == None:
            selected_index = 0
        cards_discardable = (len(players[selected_index].hand_cards.contents) + len(players[selected_index].equipment_weapon) + len(
            players[selected_index].equipment_armor) + len(players[selected_index].equipment_offensive_horse) + len(players[selected_index].equipment_defensive_horse))
        if cards_discardable > 0:
            if (self.character_ability1 == "Fearsome Advance: Whenever your ATTACK is evaded by a DEFEND, you can discard one of your opponents cards (on-hand or equipped)." or self.character_ability2 == "Fearsome Advance: Whenever your ATTACK is evaded by a DEFEND, you can discard one of your opponents cards (on-hand or equipped)." or self.character_ability3 == "Fearsome Advance: Whenever your ATTACK is evaded by a DEFEND, you can discard one of your opponents cards (on-hand or equipped)." or self.character_ability4 == "Fearsome Advance: Whenever your ATTACK is evaded by a DEFEND, you can discard one of your opponents cards (on-hand or equipped)." or self.character_ability5 == "Fearsome Advance: Whenever your ATTACK is evaded by a DEFEND, you can discard one of your opponents cards (on-hand or equipped)."):
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

    def check_fearsome_archer(self, discarded, selected_index=0):
        if selected_index == None:
            selected_index = 0
        if (self.character_ability1 == "Fearsome Archer: During your action phase, your ATTACK cards cannot be evaded by a DEFEND under the following two conditions: the number of on-hand cards of the target player is less than or equal to your attacking range; or the number of on-hand cards of the target player is more than or equal to the units of health you have remaining." or self.character_ability2 == "Fearsome Archer: During your action phase, your ATTACK cards cannot be evaded by a DEFEND under the following two conditions: the number of on-hand cards of the target player is less than or equal to your attacking range; or the number of on-hand cards of the target player is more than or equal to the units of health you have remaining." or self.character_ability3 == "Fearsome Archer: During your action phase, your ATTACK cards cannot be evaded by a DEFEND under the following two conditions: the number of on-hand cards of the target player is less than or equal to your attacking range; or the number of on-hand cards of the target player is more than or equal to the units of health you have remaining." or self.character_ability4 == "Fearsome Archer: During your action phase, your ATTACK cards cannot be evaded by a DEFEND under the following two conditions: the number of on-hand cards of the target player is less than or equal to your attacking range; or the number of on-hand cards of the target player is more than or equal to the units of health you have remaining." or self.character_ability5 == "Fearsome Archer: During your action phase, your ATTACK cards cannot be evaded by a DEFEND under the following two conditions: the number of on-hand cards of the target player is less than or equal to your attacking range; or the number of on-hand cards of the target player is more than or equal to the units of health you have remaining."):
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
                    damage_dealt = 1
                    players[selected_index].current_health -= damage_dealt
                    print(
                        f"  >> Character Ability: Fearsome Archer; {self.character} attacked {players[selected_index].character} with an undodgable {discarded}, dealing {damage_dealt} damage. ({players[selected_index].current_health}/{players[selected_index].max_health} HP remaining)")
                    for player_index, player in enumerate(players):
                        if player.current_health < 1:
                            players[player_index].check_brink_of_death_loop(
                                player_index, 0)
                    players[selected_index].check_eternal_loyalty(1)
                    players[selected_index].check_eye_for_an_eye(
                        0, "Activate")
                    players[selected_index].check_plotting_for_power(
                        damage_dealt, mode="Reaction")
                    players[selected_index].check_retaliation(0, damage_dealt)
                    return True

    def check_first_aid(self, dying_player_index=0, mode="Check"):
        if (self.character_ability1 == "First Aid: Outside of your turn, you can use any red-suited cards (on-hand or equipped) as a PEACH." or self.character_ability2 == "First Aid: Outside of your turn, you can use any red-suited cards (on-hand or equipped) as a PEACH." or self.character_ability3 == "First Aid: Outside of your turn, you can use any red-suited cards (on-hand or equipped) as a PEACH." or self.character_ability4 == "First Aid: Outside of your turn, you can use any red-suited cards (on-hand or equipped) as a PEACH." or self.character_ability5 == "First Aid: Outside of your turn, you can use any red-suited cards (on-hand or equipped) as a PEACH."):
            if mode == "Check":
                return True

            if mode == "Activate":
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
                        if discarded_index == (len(self.hand_cards.contents) + 7):
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

    def check_goddess_luo(self):
        if (self.character_ability1 == "Goddess Luo: At the beginning of your turn, you flip a judgement card. If the judgement is a black-suited, you may choose to flip another. This process continues until you flip a red-suited card. The red card is discarded and all black-suited cards are added to your hand." or self.character_ability2 == "Goddess Luo: At the beginning of your turn, you flip a judgement card. If the judgement is a black-suited, you may choose to flip another. This process continues until you flip a red-suited card. The red card is discarded and all black-suited cards are added to your hand." or self.character_ability3 == "Goddess Luo: At the beginning of your turn, you flip a judgement card. If the judgement is a black-suited, you may choose to flip another. This process continues until you flip a red-suited card. The red card is discarded and all black-suited cards are added to your hand." or self.character_ability4 == "Goddess Luo: At the beginning of your turn, you flip a judgement card. If the judgement is a black-suited, you may choose to flip another. This process continues until you flip a red-suited card. The red card is discarded and all black-suited cards are added to your hand." or self.character_ability5 == "Goddess Luo: At the beginning of your turn, you flip a judgement card. If the judgement is a black-suited, you may choose to flip another. This process continues until you flip a red-suited card. The red card is discarded and all black-suited cards are added to your hand."):
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
                if answer.get('Selected') == 'Yes':
                    main_deck.check_if_empty(main_deck, discard_deck)
                    judgement_card = main_deck.remove_from_top()
                    print(
                        f"{self.character}'s judgement card is a {judgement_card}.")
                    # Add checks for Sima Yi and Zhang Jiao
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
        if source_player_index == None:
            source_player_index = 0
        if (self.character_ability1 == "Heartbreak: Whenever a player kills you, they lose all of their character abilities for the rest of the game." or self.character_ability2 == "Heartbreak: Whenever a player kills you, they lose all of their character abilities for the rest of the game." or self.character_ability3 == "Heartbreak: Whenever a player kills you, they lose all of their character abilities for the rest of the game." or self.character_ability4 == "Heartbreak: Whenever a player kills you, they lose all of their character abilities for the rest of the game." or self.character_ability5 == "Heartbreak: Whenever a player kills you, they lose all of their character abilities for the rest of the game."):
            print(
                f"  >> Character Ability: Heartbreak; {players[source_player_index]} loses all their character-abilities after killing {self.character}.")
            players[source_player_index].character_ability1 = None
            players[source_player_index].character_ability2 = None
            players[source_player_index].character_ability3 = None
            players[source_player_index].character_ability4 = None
            players[source_player_index].character_ability5 = None

    def check_horsemanship(self):
        if (self.character_ability1 == "Horsemanship: You will always be -1 distance in any range calculations." or self.character_ability2 == "Horsemanship: You will always be -1 distance in any range calculations." or self.character_ability3 == "Horsemanship: You will always be -1 distance in any range calculations." or self.character_ability4 == "Horsemanship: You will always be -1 distance in any range calculations." or self.character_ability5 == "Horsemanship: You will always be -1 distance in any range calculations."):
            return(1)
        else:
            return(0)

    def check_humility(self):
        if (self.character_ability1 == "Humility: You cannot become the target of STEAL or ACEDIA." or self.character_ability2 == "Humility: You cannot become the target of STEAL or ACEDIA." or self.character_ability3 == "Humility: You cannot become the target of STEAL or ACEDIA." or self.character_ability4 == "Humility: You cannot become the target of STEAL or ACEDIA." or self.character_ability5 == "Humility: You cannot become the target of STEAL or ACEDIA."):
            print(
                f"  >> Character Ability: Humility; {self.character} cannot be targeted by STEAL or ACEDIA.")
            return True

    def check_iron_cavalry(self, discarded, selected_index=0):
        if selected_index == None:
            selected_index = 0
        if (self.character_ability1 == "Iron Cavalry: Whenever you ATTACK a player, you can flip a judgement card. If it is red, the ATTACK cannot be dodged." or self.character_ability2 == "Iron Cavalry: Whenever you ATTACK a player, you can flip a judgement card. If it is red, the ATTACK cannot be dodged." or self.character_ability3 == "Iron Cavalry: Whenever you ATTACK a player, you can flip a judgement card. If it is red, the ATTACK cannot be dodged." or self.character_ability4 == "Iron Cavalry: Whenever you ATTACK a player, you can flip a judgement card. If it is red, the ATTACK cannot be dodged." or self.character_ability5 == "Iron Cavalry: Whenever you ATTACK a player, you can flip a judgement card. If it is red, the ATTACK cannot be dodged."):
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
                # Add checks for Sima Yi and Zhang Jiao
                if judgement_card.suit == "Diamonds" or judgement_card.suit == "Hearts":
                    damage_dealt = 1
                    players[selected_index].current_health -= damage_dealt
                    print(
                        f"{self.character}'s judgement card is a {judgement_card} and therefore {discarded} cannot be dodged, dealing {damage_dealt} damage to {players[selected_index].character}. ({players[selected_index].current_health}/{players[selected_index].max_health} HP remaining)")
                    for player_index, player in enumerate(players):
                        if player.current_health < 1:
                            players[player_index].check_brink_of_death_loop(
                                player_index, 0)
                    players[selected_index].check_eternal_loyalty(1)
                    players[selected_index].check_eye_for_an_eye(
                        0, "Activate")
                    players[selected_index].check_plotting_for_power(
                        damage_dealt, mode="Reaction")
                    players[selected_index].check_retaliation(0, damage_dealt)
                    return True
                else:
                    print(
                        f"{self.character}'s judgement card is a {judgement_card} and Iron Cavalry has no effect.")

    def check_impetus(self, source_player_index, mode="Check"):
        if (self.character_ability1 == "Impetus: Every one of your black-suited on-hand cards may be used as DODGE." or self.character_ability2 == "Impetus: Every one of your black-suited on-hand cards may be used as DODGE." or self.character_ability3 == "Impetus: Every one of your black-suited on-hand cards may be used as DODGE." or self.character_ability4 == "Impetus: Every one of your black-suited on-hand cards may be used as DODGE." or self.character_ability5 == "Impetus: Every one of your black-suited on-hand cards may be used as DODGE."):
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
                        if discarded_index == (len(self.hand_cards.contents) + 7):
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
        if selected_index == None:
            selected_index = 0
        if (self.character_ability1 == "Insanity: Whenever you cause damage to any player within your physical range, you regain one unit of health for every unit of damage caused." or self.character_ability2 == "Insanity: Whenever you cause damage to any player within your physical range, you regain one unit of health for every unit of damage caused." or self.character_ability3 == "Insanity: Whenever you cause damage to any player within your physical range, you regain one unit of health for every unit of damage caused." or self.character_ability4 == "Insanity: Whenever you cause damage to any player within your physical range, you regain one unit of health for every unit of damage caused." or self.character_ability5 == "Insanity: Whenever you cause damage to any player within your physical range, you regain one unit of health for every unit of damage caused."):
            possible_indexes = self.calculate_targets_in_physical_range(0)
            possible_targets = []
            for target in possible_indexes:
                possible_targets.append(players[target])
            if (players[selected_index]) in possible_targets:
                if self.max_health > self.current_health:
                    self.current_health += 1
                print(
                    f"  >> Character Ability: Insanity; {self.character} regains one unit of health for damaging {players[selected_index]}, within their physical range. ({self.current_health}/{self.max_health} HP remaining)")

    def check_insurrection(self):
        if self.character_ability2 == "Insurrection (Awakening Ability): Whenever you begin your turn with three or more RITES, you must either recover one unit of health or draw two cards. You must then decrease your maximum health by one and permanently gain the ability 'Rejection'.":
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

    def check_lightning_strike(self):
        if (self.character_ability1 == "Lightning Strike: Whenever you use a DODGE card, you can target any other player to make a judgement. If the judgement card is of the suit SPADES, the target player suffers two points of lightning damage." or self.character_ability2 == "Lightning Strike: Whenever you use a DODGE card, you can target any other player to make a judgement. If the judgement card is of the suit SPADES, the target player suffers two points of lightning damage." or self.character_ability3 == "Lightning Strike: Whenever you use a DODGE card, you can target any other player to make a judgement. If the judgement card is of the suit SPADES, the target player suffers two points of lightning damage." or self.character_ability4 == "Lightning Strike: Whenever you use a DODGE card, you can target any other player to make a judgement. If the judgement card is of the suit SPADES, the target player suffers two points of lightning damage." or self.character_ability5 == "Lightning Strike: Whenever you use a DODGE card, you can target any other player to make a judgement. If the judgement card is of the suit SPADES, the target player suffers two points of lightning damage."):
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
                # Add checks for Sima Yi and Zhang Jiao
                players[selected_index].check_envy_of_heaven()
                if judgement_card.suit == "Spades":
                    damage_dealt = 2
                    players[selected_index].current_health -= damage_dealt
                    print(
                        f"  >> Character Ability: Lightning Strike; {players[selected_index].character}'s judgement card is a {judgement_card} and therefore they take two lightning damage ({players[selected_index].current_health}/{players[selected_index].max_health} HP remaining).")
                    for player_index, player in enumerate(players):
                        if (player.character_ability1 == "Lightning Strike: Whenever you use a DODGE card, you can target any other player to make a judgement. If the judgement card is of the suit SPADES, the target player suffers two points of lightning damage." or player.character_ability2 == "Lightning Strike: Whenever you use a DODGE card, you can target any other player to make a judgement. If the judgement card is of the suit SPADES, the target player suffers two points of lightning damage." or player.character_ability3 == "Lightning Strike: Whenever you use a DODGE card, you can target any other player to make a judgement. If the judgement card is of the suit SPADES, the target player suffers two points of lightning damage." or player.character_ability4 == "Lightning Strike: Whenever you use a DODGE card, you can target any other player to make a judgement. If the judgement card is of the suit SPADES, the target player suffers two points of lightning damage." or player.character_ability5 == "Lightning Strike: Whenever you use a DODGE card, you can target any other player to make a judgement. If the judgement card is of the suit SPADES, the target player suffers two points of lightning damage."):
                            dodging_player_index = player_index
                    for player_index, player in enumerate(players):
                        if player.current_health < 1:
                            players[player_index].check_brink_of_death_loop(
                                player_index, dodging_player_index)
                    players[selected_index].check_eternal_loyalty(
                        damage_dealt)
                    players[selected_index].check_eye_for_an_eye(
                        dodging_player_index, "Activate")
                    players[selected_index].check_plotting_for_power(
                        damage_dealt, mode="Reaction")
                    players[selected_index].check_retaliation(
                        dodging_player_index, damage_dealt)
                else:
                    print(
                        f"  >> Character Ability: Lightning Strike; {players[selected_index].character}'s judgement card is a {judgement_card} and thus nothing happens.")

    def check_mediocrity(self, phase="Draw"):
        if (self.character_ability1 == "Mediocrity: During your drawing phase, you draw an extra X cards, X being the total number of allegiances still in play. During your discard phase, you must discard at least as many card as there are allegiances still in play. If you have less cards than there are allegiances, you must discard all of them." or self.character_ability2 == "Mediocrity: During your drawing phase, you draw an extra X cards, X being the total number of allegiances still in play. During your discard phase, you must discard at least as many card as there are allegiances still in play. If you have less cards than there are allegiances, you must discard all of them." or self.character_ability3 == "Mediocrity: During your drawing phase, you draw an extra X cards, X being the total number of allegiances still in play. During your discard phase, you must discard at least as many card as there are allegiances still in play. If you have less cards than there are allegiances, you must discard all of them." or self.character_ability4 == "Mediocrity: During your drawing phase, you draw an extra X cards, X being the total number of allegiances still in play. During your discard phase, you must discard at least as many card as there are allegiances still in play. If you have less cards than there are allegiances, you must discard all of them." or self.character_ability5 == "Mediocrity: During your drawing phase, you draw an extra X cards, X being the total number of allegiances still in play. During your discard phase, you must discard at least as many card as there are allegiances still in play. If you have less cards than there are allegiances, you must discard all of them."):
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
        if (self.character_ability1 == "One After Another: Whenever you use or lose your last on-hand card, you can immediately draw one card from the deck." or self.character_ability2 == "One After Another: Whenever you use or lose your last on-hand card, you can immediately draw one card from the deck." or self.character_ability3 == "One After Another: Whenever you use or lose your last on-hand card, you can immediately draw one card from the deck." or self.character_ability4 == "One After Another: Whenever you use or lose your last on-hand card, you can immediately draw one card from the deck." or self.character_ability5 == "One After Another: Whenever you use or lose your last on-hand card, you can immediately draw one card from the deck."):
            if len(self.hand_cards.contents) == 0:
                print(
                    f"  >> Character Ability: One After Another; {self.character} can draw a card whenever they use or lose their last on-hand card.")
                self.hand_cards.draw(main_deck, 1, False)

    def check_plotting_for_power(self, damage_dealt, phase="Reaction"):
        if (self.character_ability1 == "Plotting for Power: For every unit of damage you recieve, you can choose to draw one card and then set one hand-card face down as a RITE. Your hand limit is increased by one for each RITE." or self.character_ability2 == "Plotting for Power: For every unit of damage you recieve, you can choose to draw one card and then set one hand-card face down as a RITE. Your hand limit is increased by one for each RITE." or self.character_ability3 == "Plotting for Power: For every unit of damage you recieve, you can choose to draw one card and then set one hand-card face down as a RITE. Your hand limit is increased by one for each RITE." or self.character_ability4 == "Plotting for Power: For every unit of damage you recieve, you can choose to draw one card and then set one hand-card face down as a RITE. Your hand limit is increased by one for each RITE." or self.character_ability5 == "Plotting for Power: For every unit of damage you recieve, you can choose to draw one card and then set one hand-card face down as a RITE. Your hand limit is increased by one for each RITE."):
            if phase == "Reaction":
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

            if phase == "Discard":
                limit_increase = len(self.rites)
                if limit_increase > 0:
                    print(
                        f"  >> Character Ability: Plotting for Power; {self.character}'s hand limit is increased by {limit_increase} (one for every RITE).")
                return limit_increase

    def check_raid(self):
        if (self.character_ability1 == "Raid: In your drawing phase, you can choose to forgo drawing cards from the deck and, instead, draw one on-hand card from a maximum of two other players." or self.character_ability2 == "Raid: In your drawing phase, you can choose to forgo drawing cards from the deck and, instead, draw one on-hand card from a maximum of two other players." or self.character_ability3 == "Raid: In your drawing phase, you can choose to forgo drawing cards from the deck and, instead, draw one on-hand card from a maximum of two other players." or self.character_ability4 == "Raid: In your drawing phase, you can choose to forgo drawing cards from the deck and, instead, draw one on-hand card from a maximum of two other players." or self.character_ability5 == "Raid: In your drawing phase, you can choose to forgo drawing cards from the deck and, instead, draw one on-hand card from a maximum of two other players."):
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
                        Separator("-------------OTHER-OPTIONS-------------"))
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
                    target_1_index = answer.get('Selected')

                    if target_1_index == (len(players) + 1):
                        return self.check_raid()

                    targets_str.pop(target_1_index)
                    targets_str.insert(target_1_index, Separator(
                        f"--{players[target_1_index].character} (Already selected)--"))
                    target_1 = targets[target_1_index]
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
                    target_2_index = answer.get('Selected')
                    target_2 = targets[target_2_index]

                    if target_2 == "Cancel":
                        return self.check_raid()
                    else:
                        print(' ')
                        options_str = target_1.create_str_blind_menu()

                        question = [
                            {
                                'type': 'list',
                                'name': 'Selected',
                                'message': f"{self.character}: Please select which card you would like to take from {target_1.character}'s hand:",
                                'choices': options_str,
                                'filter': lambda card: options_str.index(card)
                            },
                        ]
                        answer = prompt(question, style=custom_style_2)
                        card_stolen_index = answer.get('Selected')

                        if card_stolen_index <= len(target_1.hand_cards.contents):
                            card_stolen = target_1.hand_cards.contents.pop(
                                card_stolen_index - 1)
                            self.hand_cards.add_to_top(card_stolen)
                            print(
                                f"  >> Character Ability: Raid; {self.character} has drawn {card_stolen} from {target_1.character}'s hand.")
                            target_1.check_one_after_another()
                            activated_raid = False

                    if target_2 != "Target noone else":
                        print(' ')
                        options_str = target_2.create_str_blind_menu()

                        question = [
                            {
                                'type': 'list',
                                'name': 'Selected',
                                'message': f"{self.character}: Please select which card you would like to take from {target_2.character}'s hand:",
                                'choices': options_str,
                                'filter': lambda card: options_str.index(card)
                            },
                        ]
                        answer = prompt(question, style=custom_style_2)
                        card_stolen_index = answer.get('Selected')

                        if card_stolen_index <= len(target_2.hand_cards.contents):
                            card_stolen = target_2.hand_cards.contents.pop(
                                card_stolen_index - 1)
                            self.hand_cards.add_to_top(card_stolen)
                            print(
                                f"  >> Character Ability: Raid; {self.character} has drawn {card_stolen} from {target_2.character}'s hand.")
                            target_2.check_one_after_another()
                            activated_raid = False
                    return True

    def check_reckless(self, card, source_player_index=0):
        if source_player_index == None:
            source_player_index = 0
        if (self.character_ability1 == "Reckless: Every instance that you suffer damage from a red-suited ATTACK, or a WINE ATTACK, your maximum health limit is reduced by one instead." or self.character_ability2 == "Reckless: Every instance that you suffer damage from a red-suited ATTACK, or a WINE ATTACK, your maximum health limit is reduced by one instead." or self.character_ability3 == "Reckless: Every instance that you suffer damage from a red-suited ATTACK, or a WINE ATTACK, your maximum health limit is reduced by one instead." or self.character_ability4 == "Reckless: Every instance that you suffer damage from a red-suited ATTACK, or a WINE ATTACK, your maximum health limit is reduced by one instead." or self.character_ability5 == "Reckless: Every instance that you suffer damage from a red-suited ATTACK, or a WINE ATTACK, your maximum health limit is reduced by one instead."):
            if card.suit == "Hearts" or card.suit == "Diamonds" or card.effect2 == "Wine-Attack":
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
        if self.character_ability2 == "Recommence the Legacy (Awakening Ability): If at the start of your turn, you have no on-hand cards, you must either regain one unit of health or draw two cards, and then reduce your maximum health limit by one. You then permanently gain the ability 'Astrology'.":
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
        if source_player_index == None:
            source_player_index = 0
        if mode == "Activate":
            if (self.character_ability1 == "Relish: Whenever another player targets an ATTACK against you, they must discard a basic card, or else that ATTACK has no net effect on you." or self.character_ability2 == "Relish: Whenever another player targets an ATTACK against you, they must discard a basic card, or else that ATTACK has no net effect on you." or self.character_ability3 == "Relish: Whenever another player targets an ATTACK against you, they must discard a basic card, or else that ATTACK has no net effect on you." or self.character_ability4 == "Relish: Whenever another player targets an ATTACK against you, they must discard a basic card, or else that ATTACK has no net effect on you." or self.character_ability5 == "Relish: Whenever another player targets an ATTACK against you, they must discard a basic card, or else that ATTACK has no net effect on you."):
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
                if (player.character_ability1 == "Relish: Whenever another player targets an ATTACK against you, they must discard a basic card, or else that ATTACK has no net effect on you." or player.character_ability2 == "Relish: Whenever another player targets an ATTACK against you, they must discard a basic card, or else that ATTACK has no net effect on you." or player.character_ability3 == "Relish: Whenever another player targets an ATTACK against you, they must discard a basic card, or else that ATTACK has no net effect on you." or player.character_ability4 == "Relish: Whenever another player targets an ATTACK against you, they must discard a basic card, or else that ATTACK has no net effect on you." or player.character_ability5 == "Relish: Whenever another player targets an ATTACK against you, they must discard a basic card, or else that ATTACK has no net effect on you."):
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
        if reacting_player_index == None:
            reacting_player_index = 0
        if (self.role == 'Emperor') or (self.character_ability2 == "False Ruler: You possess the same ruler ability as the current emperor."):
            if (self.character_ability1 == "Rescued (Ruler Ability): Whenever another member of Wu uses a PEACH to save you from the brink of death, it provides you with two units of health." or self.character_ability2 == "Rescued (Ruler Ability): Whenever another member of Wu uses a PEACH to save you from the brink of death, it provides you with two units of health." or self.character_ability3 == "Rescued (Ruler Ability): Whenever another member of Wu uses a PEACH to save you from the brink of death, it provides you with two units of health." or self.character_ability4 == "Rescued (Ruler Ability): Whenever another member of Wu uses a PEACH to save you from the brink of death, it provides you with two units of health." or self.character_ability5 == "Rescued (Ruler Ability): Whenever another member of Wu uses a PEACH to save you from the brink of death, it provides you with two units of health."):
                if players[reacting_player_index].character != self.character:
                    if players[reacting_player_index].allegiance == "Wu":
                        print(
                            f"  >> Character Ability: Rescued (Ruler Ability): {self.character} was saved from the brink of death by a member of Wu, and therefore recovers two health!")
                        return (1)
        else:
            return (0)

    def check_restraint(self):
        if (self.character_ability1 == "Restraint: If you did not use any ATTACK cards during your action phase, you can skip your discard phase." or self.character_ability2 == "Restraint: If you did not use any ATTACK cards during your action phase, you can skip your discard phase." or self.character_ability3 == "Restraint: If you did not use any ATTACK cards during your action phase, you can skip your discard phase." or self.character_ability4 == "Restraint: If you did not use any ATTACK cards during your action phase, you can skip your discard phase." or self.character_ability5 == "Restraint: If you did not use any ATTACK cards during your action phase, you can skip your discard phase."):
            if self.attacks_this_turn == 0:
                print(
                    f"  >> Character Ability; Restraint: {self.character} skips their discard phase.")
                return True

    def check_retaliation(self, source_player_index=0, damage_dealt=1):
        if source_player_index == None:
            source_player_index = 0
        if (self.character_ability1 == "Retaliation: For every one unit of damage you recieve, you can take one card (whether on-hand or equipped) from the player who was the source of that damage." or self.character_ability2 == "Retaliation: For every one unit of damage you recieve, you can take one card (whether on-hand or equipped) from the player who was the source of that damage." or self.character_ability3 == "Retaliation: For every one unit of damage you recieve, you can take one card (whether on-hand or equipped) from the player who was the source of that damage." or self.character_ability4 == "Retaliation: For every one unit of damage you recieve, you can take one card (whether on-hand or equipped) from the player who was the source of that damage." or self.character_ability5 == "Retaliation: For every one unit of damage you recieve, you can take one card (whether on-hand or equipped) from the player who was the source of that damage."):
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
        if (self.character_ability2 == "Second Wind (Single-Use Ability): Once per game, at the beginning of your turn, you can return to the same amount of health that you had at the end of your previous turn. You draw a card for each unit of health that changes."):
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

    def check_talent(self):
        if (self.character_ability1 == "Talent: You can use tool cards without range restrictions." or self.character_ability2 == "Talent: You can use tool cards without range restrictions." or self.character_ability3 == "Talent: You can use tool cards without range restrictions." or self.character_ability4 == "Talent: You can use tool cards without range restrictions." or self.character_ability5 == "Talent: You can use tool cards without range restrictions."):
            print(
                f"  >> Character Ability: Talent; {self.character} has no range restriction on their tool cards.")
            return True

    def check_unnatural_death(self, cards_discarded):
        if cards_discarded == None:
            return (' ')
        if self.current_health == 0:
            return (' ')
        if (self.character_ability1 == "Unnatural Death: You can immediately take possession of all cards (both on-hand and equipped) of any player that dies." or self.character_ability2 == "Unnatural Death: You can immediately take possession of all cards (both on-hand and equipped) of any player that dies." or self.character_ability3 == "Unnatural Death: You can immediately take possession of all cards (both on-hand and equipped) of any player that dies." or self.character_ability4 == "Unnatural Death: You can immediately take possession of all cards (both on-hand and equipped) of any player that dies." or self.character_ability5 == "Unnatural Death: You can immediately take possession of all cards (both on-hand and equipped) of any player that dies."):
            print(
                f"  >> Character Ability: Unnatural Death; All discarded hands are added to the hand of {self.character}.")
            self.hand_cards.draw(discard_deck, cards_discarded, False)

    def check_warrior_woman(self):
        if (self.character_ability1 == "Warrior Woman: Whenever any equipped card is removed from your equipment, you can immediately draw two cards from the deck." or self.character_ability2 == "Warrior Woman: Whenever any equipped card is removed from your equipment, you can immediately draw two cards from the deck." or self.character_ability3 == "Warrior Woman: Whenever any equipped card is removed from your equipment, you can immediately draw two cards from the deck." or self.character_ability4 == "Warrior Woman: Whenever any equipped card is removed from your equipment, you can immediately draw two cards from the deck." or self.character_ability5 == "Warrior Woman: Whenever any equipped card is removed from your equipment, you can immediately draw two cards from the deck."):
            print(
                f"  >> Character Ability: Warrior Woman; {self.character} immediately draws two cards from the deck whenever their equipment card is destroyed/removed/replaced.")
            self.hand_cards.draw(main_deck, 2, False)

    def check_wisdom(self):
        if (self.character_ability1 == "Wisdom: Whenever you use a non-delay tool card, you immediately draw a card from the deck." or self.character_ability2 == "Wisdom: Whenever you use a non-delay tool card, you immediately draw a card from the deck." or self.character_ability3 == "Wisdom: Whenever you use a non-delay tool card, you immediately draw a card from the deck." or self.character_ability4 == "Wisdom: Whenever you use a non-delay tool card, you immediately draw a card from the deck." or self.character_ability5 == "Wisdom: Whenever you use a non-delay tool card, you immediately draw a card from the deck."):
            print(
                f"  >> Character Ability: Wisdom; {self.character} immediately draws a card from the deck after using a non-delay tool card.")
            self.hand_cards.draw(main_deck, 1, False)

# Activatable abilities (reusable)
    def activate_blockade(self):
        if (self.character_ability1 == "Blockade: During your action phase, you can choose to use any of your basic or equipment cards with suit CLUBS or SPADES as RATIONS DEPLETED with a physical range of -1 in distance calculations. RATIONS DEPLETED acts as a time-delay tool card, in which a player will have to flip a judgement at the start of their turn. If the judgement is any suit other than CLUBS, the target fails the judgement and must skip their drawing phase." or self.character_ability2 == "Blockade: During your action phase, you can choose to use any of your basic or equipment cards with suit CLUBS or SPADES as RATIONS DEPLETED with a physical range of -1 in distance calculations. RATIONS DEPLETED acts as a time-delay tool card, in which a player will have to flip a judgement at the start of their turn. If the judgement is any suit other than CLUBS, the target fails the judgement and must skip their drawing phase." or self.character_ability3 == "Blockade: During your action phase, you can choose to use any of your basic or equipment cards with suit CLUBS or SPADES as RATIONS DEPLETED with a physical range of -1 in distance calculations. RATIONS DEPLETED acts as a time-delay tool card, in which a player will have to flip a judgement at the start of their turn. If the judgement is any suit other than CLUBS, the target fails the judgement and must skip their drawing phase." or self.character_ability4 == "Blockade: During your action phase, you can choose to use any of your basic or equipment cards with suit CLUBS or SPADES as RATIONS DEPLETED with a physical range of -1 in distance calculations. RATIONS DEPLETED acts as a time-delay tool card, in which a player will have to flip a judgement at the start of their turn. If the judgement is any suit other than CLUBS, the target fails the judgement and must skip their drawing phase." or self.character_ability5 == "Blockade: During your action phase, you can choose to use any of your basic or equipment cards with suit CLUBS or SPADES as RATIONS DEPLETED with a physical range of -1 in distance calculations. RATIONS DEPLETED acts as a time-delay tool card, in which a player will have to flip a judgement at the start of their turn. If the judgement is any suit other than CLUBS, the target fails the judgement and must skip their drawing phase."):
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

                    if discarded_index == (len(self.hand_cards.contents) + 7):
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
                                discard_deck.contents.pop()
                                self.equipment_weapon.append(card)
                                self.weapon_range = card.weapon_range
                            if armor_popped:
                                discard_deck.contents.pop()
                                self.equipment_armor.append(card)
                            if off_horse_popped:
                                discard_deck.contents.pop()
                                self.equipment_offensive_horse.append(card)
                            if def_horse_popped:
                                discard_deck.contents.pop()
                                self.equipment_defensive_horse.append(card)
                            else:
                                self.hand_cards.draw(discard_deck, 1, False)
                            print(
                                f"{self.character} cancelled using their effect, and {card} was returned.")
                    else:
                        print(
                            f"{options[discarded_index]} cannot be used as RATIONS DEPLETED as it is not a black-suited, basic/equipment card.")

    def activate_national_colours(self):
        if (self.character_ability1 == "National Colours: During your action phase, you can use any of your cards (on-hand or equipped) with a DIAMONDS suit as ACEDIA." or self.character_ability2 == "National Colours: During your action phase, you can use any of your cards (on-hand or equipped) with a DIAMONDS suit as ACEDIA." or self.character_ability3 == "National Colours: During your action phase, you can use any of your cards (on-hand or equipped) with a DIAMONDS suit as ACEDIA." or self.character_ability4 == "National Colours: During your action phase, you can use any of your cards (on-hand or equipped) with a DIAMONDS suit as ACEDIA." or self.character_ability5 == "National Colours: During your action phase, you can use any of your cards (on-hand or equipped) with a DIAMONDS suit as ACEDIA."):
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
                            'message': f'{self.character}: Please select a card to use as ACEDIA?',
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

                    if discarded_index == (len(self.hand_cards.contents) + 7):
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
                                discard_deck.contents.pop()
                                self.equipment_weapon.append(card)
                                self.weapon_range = card.weapon_range
                            if armor_popped:
                                discard_deck.contents.pop()
                                self.equipment_armor.append(card)
                            if off_horse_popped:
                                discard_deck.contents.pop()
                                self.equipment_offensive_horse.append(card)
                            if def_horse_popped:
                                discard_deck.contents.pop()
                                self.equipment_defensive_horse.append(card)
                            else:
                                self.hand_cards.draw(discard_deck, 1, False)
                            print(
                                f"{self.character} cancelled using their effect, and {card} was returned.")
                    else:
                        print(
                            f"{options[discarded_index]} cannot be used as ACEDIA as is it not DIAMONDS.")

    def activate_surprise(self):
        if (self.character_ability1 == "Surprise: During your action phase, you can use any of your black-suited cards (on-hand or equipped) as DISMANTLE." or self.character_ability2 == "Surprise: During your action phase, you can use any of your black-suited cards (on-hand or equipped) as DISMANTLE." or self.character_ability3 == "Surprise: During your action phase, you can use any of your black-suited cards (on-hand or equipped) as DISMANTLE." or self.character_ability4 == "Surprise: During your action phase, you can use any of your black-suited cards (on-hand or equipped) as DISMANTLE." or self.character_ability5 == "Surprise: During your action phase, you can use any of your black-suited cards (on-hand or equipped) as DISMANTLE."):
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
                            'message': f'{self.character}: Please select a card to use as DISMANTLE?',
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

                    if discarded_index == (len(self.hand_cards.contents) + 7):
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
                                discard_deck.contents.pop()
                                self.equipment_weapon.append(card)
                                self.weapon_range = card.weapon_range
                            if armor_popped:
                                discard_deck.contents.pop()
                                self.equipment_armor.append(card)
                            if off_horse_popped:
                                discard_deck.contents.pop()
                                self.equipment_offensive_horse.append(card)
                            if def_horse_popped:
                                discard_deck.contents.pop()
                                self.equipment_defensive_horse.append(card)
                            else:
                                self.hand_cards.draw(discard_deck, 1, False)
                            print(
                                f"{self.character} cancelled using their effect, and {card} was returned.")
                    else:
                        print(
                            f"{options[discarded_index]} cannot be used as DISMANTLE as it is not black-suited.")

    def activate_trojan_flesh(self):
        if (self.character_ability1 == "Trojan Flesh: During your action phase, you can choose to lose one unit of health to draw two more cards from the deck. This ability can be used repeatedly in a turn." or self.character_ability2 == "Trojan Flesh: During your action phase, you can choose to lose one unit of health to draw two more cards from the deck. This ability can be used repeatedly in a turn." or self.character_ability3 == "Trojan Flesh: During your action phase, you can choose to lose one unit of health to draw two more cards from the deck. This ability can be used repeatedly in a turn." or self.character_ability4 == "Trojan Flesh: During your action phase, you can choose to lose one unit of health to draw two more cards from the deck. This ability can be used repeatedly in a turn." or self.character_ability5 == "Trojan Flesh: During your action phase, you can choose to lose one unit of health to draw two more cards from the deck. This ability can be used repeatedly in a turn."):
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

# Activatable abilities (once-per-turn)
    def activate_green_salve(self):
        if (self.character_ability1 == "Green Salve: During your action phase, you can discard any card and allow any player to regain one unit of health. Limited to one use per turn." or self.character_ability2 == "Green Salve: During your action phase, you can discard any card and allow any player to regain one unit of health. Limited to one use per turn." or self.character_ability3 == "Green Salve: During your action phase, you can discard any card and allow any player to regain one unit of health. Limited to one use per turn." or self.character_ability4 == "Green Salve: During your action phase, you can discard any card and allow any player to regain one unit of health. Limited to one use per turn." or self.character_ability5 == "Green Salve: During your action phase, you can discard any card and allow any player to regain one unit of health. Limited to one use per turn."):
            cards_discardable = (len(self.hand_cards.contents) + len(self.equipment_weapon) + len(
                self.equipment_armor) + len(self.equipment_offensive_horse) + len(self.equipment_defensive_horse))
            if not self.used_green_salve:
                if cards_discardable > 0:
                    options_str = []
                    choices = []
                    for player_index, player in enumerate(players):
                        if player.max_health > player.current_health:
                            options_str.append(str(players[player_index]))
                            choices.append(players[player_index])
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
                        if answer.get('Selected') == len(options_str) - 1:
                            return(' ')
                        else:
                            player_healed_index = answer.get('Selected')

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

                            if discarded_index == (len(self.hand_cards.contents) + 7):
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

                            choices[player_healed_index].current_health += 1
                            self.used_green_salve = True
                            print(
                                f"  >> Character Ability: Green Salve; {self.character} discarded {card} to heal {choices[player_healed_index].character} by one! ({choices[player_healed_index].current_health}/{choices[player_healed_index].max_health} HP remaining)")

# Game-state
# Beginning Phase
    def start_beginning_phase(self):
        print(" ")
        self.reset_once_per_turn()
        # Check for Zuo Ci; Shapeshift
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
        # Check for Sima Yi; Devil // Zhang Jiao; Dark Sorcery - these to be incorporated within below command!
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
            # Check for Xu Chu; Bare the Chest
            # Check for Zhang He; Flexibility
            if self.check_raid():
                return self.start_action_phase()
            return self.start_drawing_phase()

# Drawing Phase
    def start_drawing_phase(self):
        print(" ")
        cards_drawn = 0
        message = True
        # Checks for Lu Su; Altruism
        if self.check_dashing_hero():
            cards_drawn += 1
            message = False
        if self.check_mediocrity("Draw"):
            cards_drawn += check_allegiances_in_play()
            message = False
        # Checks for Sun Ce; Dashing Hero
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
                Separator("------------------Abilities------------------"))
            activatable_abilities = self.check_activatable_abilities()
            for ability in activatable_abilities:
                options.append(ability)
            options.append(
                Separator("--------------------Other--------------------"))
            options.append('End action-phase')
            message = f"{self.character}, it is your action-phase: Please choose an option:"

            question = [
                {
                    'type': 'list',
                    'name': 'Selected',
                    'message': message,
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
            elif action_taken_index <= ((len(playing_card_options) + len(activatable_abilities)) + 1):
                print(
                    f"{self.character} has used their ability: {options[action_taken_index]}")
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
            limit_increase_1 = self.check_bloodline()
            limit_increase_2 = self.check_plotting_for_power(0, "Discard")
            if limit_increase_1 == None:
                limit_increase_1 = 0
            if limit_increase_2 == None:
                limit_increase_2 = 0
            limit_increase = limit_increase_1 + limit_increase_2

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
        # Checks for Zuo Ci; Shapeshift
        # Cycles to next player
        players.append(players.pop(0))
        # NEEDED FOR LATER to make infinite loop, commenting out for now!
        # return players[0].start_beginning_phase()


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


# Select Picking Mode and Characters
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
    if roles_dictionary["Emperor"] == 1 and roles_dictionary["Rebel"] == 0 and roles_dictionary["Spy"] == 0:
        print("Emperor and Advisor(s) win.")
    elif roles_dictionary["Spy"] == 1 and roles_dictionary["Emperor"] == 0 and roles_dictionary["Advisor"] == 0 and roles_dictionary["Rebel"] == 0:
        print("Spy wins.")
    elif roles_dictionary["Emperor"] == 0:
        print("Rebel(s) win.")
    pass


# Game-Setup
# Game-Setup
# Game-Setup
game_started = False
[number_of_players_output, roles_dictionary,
    roles_list, picking_format_output] = setup_loop()
random.shuffle(roles_list)
roles_list.append(roles_list.pop(roles_list.index("Emperor")))
players = generate_players()
[shu_emperor_cards, wei_emperor_cards, wu_emperor_cards, hero_emperor_cards, shu_character_cards, wei_character_cards, wu_character_cards,
    hero_character_cards, all_emperor_cards, all_character_cards, character_card_discard_pile] = generate_character_decks()
player_assignment()


# Card handling
main_deck = Deck(all_cards)
discard_deck = Deck([])
main_deck.shuffle()
print("The deck has been shuffled!")
for player in players:
    player.hand_cards.draw(main_deck, 4, False)
print("All players have been dealt 4 cards!")
game_started = True


# if someone dies~
# roles_dictionary['Role'] -= 1
# check_win_conditions()

# how to reference players~
# players[0].hand_cards.draw(main_deck, 4)
# players[0].hand_cards.view_hand()
# players[0].hand_cards.discard_from_hand(2)
# players[0].equipment_weapon.append(Card(6, 'Six', 'Spades', 'Weapon', 'Black Pommel', 'When equipped, the wielder ignores any armor of their targets.', 2))
# players[1].equipment_armor.append(Card(2, 'Two', 'Spades', 'Armor', 'Eight-Trigrams', 'When equipped: whenever a DEFEND is needed, the wearer can perform a judgement. If it is red, the DEFEND is considered to be played.'))
# players[1].pending_judgements.append(Card('6', 'Six', 'Spades', 'Delay-Tool', 'Acedia', 'You can place Delay-Tool on any other player. The target must perform a judgement for this card. If it is not HEARTS, they forfeit their action-phase.', None, 'Acedia'))
# players[1].pending_judgements.append(Card('6', 'Six', 'Spades', 'Delay-Tool', 'Lightning', 'You can place Delay-Tool on any other player. The target must perform a judgement for this card. If it is not HEARTS, they forfeit their action-phase.', None, 'Lightning'))
# players[0].start_judgement_phase()


# Gameplay
print(' ')
players[0].hand_cards.draw(main_deck, 50)
# players[1].hand_cards.draw(main_deck, 25)
# players[0].hand_cards.use_card_effect()
# print(players[0].calculate_targets_in_physical_range(0))
# print(players[0].calculate_targets_in_weapon_range(0))
# players[0].start_action_phase()

players[0].current_health = 50
players[1].current_health = 1
# players[0].role = 'Rebel'
players[0].start_beginning_phase()
# players[0].start_beginning_phase()
# players[0].start_beginning_phase()
