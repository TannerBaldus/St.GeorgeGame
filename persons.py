"""
St. George Game
person.py
Sage Berg
Created: 7 Dec 2014
"""

import abc
from collections import namedtuple

import actions
import weapons
from raffle import Raffle

Pronouns = namedtuple("Pronouns", ["subj", "obj", "tense"])


class Person(object):
    """
    abstract class
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __init__(self, name, attack, pronoun):
        self.name = name
        self.attack = attack
        self.pronoun = pronoun


class BlindBartender(Person):

    def __init__(self):
        self.name = "the blind bartender"
        self.attack = 1
        self.pronouns = Pronouns("he", "him", "s")
        self.options = {"a": Raffle(),
                        "b": Raffle(),
                        "c": Raffle(),
                        "d": Raffle()}
        self.options["a"].add(actions.Attack(self), weight=10)
        self.options["b"].add(actions.BoastOfYourBravery(), weight=1)
        #self.options["c"].add(TalkAboutCats)


class PrettyLady(Person):

    def __init__(self):
        self.name = "pretty lady"
        self.attack = 1
        self.pronouns = Pronouns("she", "her", "s")
        self.options = {"a": Raffle(),
                        "b": Raffle(),
                        "c": Raffle(),
                        "d": Raffle()}
        self.options["a"].add(actions.Attack(self), weight=10)
        self.options["b"].add(actions.BoastOfYourBravery(), weight=5)
        #self.options["b"].add(BuyHerADrink)
        #self.options["c"].add(TalkAboutCats)


class StGeorge(Person):

    def __init__(self):
        self.name = "St. George"
        self.attack = 100
        self.pronouns = Pronouns("he", "him", "s")
        self.options = {"a": Raffle(),
                        "b": Raffle(),
                        "c": Raffle(),
                        "d": Raffle()}
        self.options["a"].add(actions.Attack(self), weight=10)
        #self.options["b"].add(actions.BegForMoney(), weight=10)


class WealthyMerchant(Person):

    def __init__(self):
        self.name = "the wealthy merchant"
        self.attack = 7
        self.pronouns = Pronouns("he", "him", "s")
        self.options = {"a": Raffle(),
                        "b": Raffle(),
                        "c": Raffle(),
                        "d": Raffle()}
        self.options["a"].add(actions.Attack(self), weight=10)
        self.options["b"].add(actions.BoastOfYourBravery(), weight=1)
        self.options["b"].add(actions.Buy(weapons.weapons), weight=10)
