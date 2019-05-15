import infrastructure.command as cmd
import gui_id as gui

def log(text):
    cmd.command_queue.add_message(cmd.CommandType.ADD_ROW, gui.LEFT_TEXT_BOX, text)