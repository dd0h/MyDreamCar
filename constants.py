# Important Game Settings
SPEED = 50  # 30
CAR_VELOCITY = 5
TIME_DELAY = 30
CAR_PROTRUDE = 10  # Defines how many pixels of car can protrude over the way

WAY_LENGTH = 100
ROAD_WIDTH = 300

MAP_LENGTH = 100  # When "car" is approaching to end of map, it's being extended by next value of MAP_LENGTH,
# so actually the road length is infinite

SAFE_EXCESS = 30  # Needed to deal with list index out of range problem
# (Because of drawRoad() function is called that fast when run, so map can't be generated fast enough to extend road
# map)

# Graphics

WINDOW_HEIGHT = 1000
WINDOW_LENGTH = 500

BIG_FONT = 60
SMALL_FONT = 20
SCORE_FONT = 30

GAME_OVER_SIGN_X = 330
GAME_OVER_SIGN_Y = 150

OUT_OF_ROAD_SIGN_X = 240
OUT_OF_ROAD_SIGN_Y = 250

SCORE_BOARD_X = 450
SCORE_BOARD_Y = 350

RESTART_SIGN_X = 370
RESTART_SIGN_Y = 400

ROAD_BORDER_SIZE = 10

WAY_SEGMENT_FIRST = -2
WAY_SEGMENT_LAST = 5
