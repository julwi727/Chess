from enum import Enum

class CommandType(Enum):
    NONE = 0
    MOVE = 1
    SELECT_PIECE = 2
    CLEAR_TEXT = 3
    ADD_ROW = 4

class Command:
    def __init__(self):
        self.message_queue = []

    def get_message(self):
        cmd = self.message_queue[0]
        tmp = []
        for i in range(len(self.message_queue) - 1):
            tmp.append(self.message_queue[i+1])
        
        self.message_queue = tmp
        return cmd
    
    def add_message(self, command, component_id):
        self.message_queue.append((command, component_id))

    def has_message(self):
        return len(self.message_queue) > 0

