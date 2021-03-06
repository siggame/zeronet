import operator
import utility
import json
import client_json
import json
import game
from game_object import GameObject
from Mappable import Mappable

## @class Tile
class Tile(Mappable):

    def __init__(self, connection, parent_game, id, owner, x, y):
        self._connection = connection
        self._parent_game = parent_game
        self._id = id
        self._owner = owner
        self._x = x
        self._y = y


    @property
    def id(self):
        return self._id
    @property
    def owner(self):
        return self._owner
    @property
    def x(self):
        return self._x
    @property
    def y(self):
        return self._y




