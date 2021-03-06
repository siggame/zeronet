import operator
import utility
import json
import client_json
import json
import game
from game_object import GameObject
from Mappable import Mappable

## @class Base
#  @brief The information on the base
class Base(Mappable):

    def __init__(self, connection, parent_game, id, owner, spawns_left, x, y):
        self._connection = connection
        self._parent_game = parent_game
        self._id = id
        self._owner = owner
        self._spawns_left = spawns_left
        self._x = x
        self._y = y

    ## @fn spawn
    #  @brief Creates a Virus on the base with certain level.
    def spawn(self, level):
        function_call = client_json.function_call.copy()
        function_call.update({"type": 'spawn'})
        function_call.get("args").update({"actor": self.id})
        function_call.get("args").update({'level': repr(level)})

        utility.send_string(self._connection, json.dumps(function_call))

        received_status = False
        status = None
        while not received_status:
            message = utility.receive_string(self._connection)
            message = json.loads(message)

            if message.get("type") == "success":
                received_status = True
                status = True
            elif message.get("type") == "failure":
                received_status = True
                status = False
            if message.get("type") == "changes":
                self._parent_game.update_game(message)

        return status

    @property
    def id(self):
        return self.id
    @property
    def owner(self):
        return self.owner
    @property
    def spawns_left(self):
        return self.spawns_left
    @property
    def x(self):
        return self.x
    @property
    def y(self):
        return self.y




