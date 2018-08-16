from utilities import get_window_info
from serpent.game import Game
from serpent.input_controller import InputController, InputControllers
import random


TIRED_SCALE = None
TIRED_LIMIT = None
WINDOW_OFFSET = None
INPUT_CONTROLLER = None


def init_constants(game_title=u'阴阳师-网易游戏', move_window=False):
    global TIRED_SCALE
    global TIRED_LIMIT
    global WINDOW_OFFSET
    global INPUT_CONTROLLER
    config = {'window_name': game_title}
    onmyoji_game = Game(window_name=config['window_name'], move_window=move_window)
    onmyoji_game.after_launch()
    INPUT_CONTROLLER = InputController(backend=InputControllers.NATIVE_WIN32, game=onmyoji_game)
    TIRED_SCALE = 1
    TIRED_LIMIT = random.random()*100
    WINDOW_OFFSET = get_window_info(game_title)