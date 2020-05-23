# GENERAL
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 500

# Car

# Game
TIME_DELAY = 30
CAR_VELOCITY = 8

RESTART_SIGN_X = 370
RESTART_SIGN_Y = 400

SCORE_BOARD_X = 450
SCORE_BOARD_Y = 350

OUT_OF_ROAD_SIGN_X = 240
OUT_OF_ROAD_SIGN_Y = 250

GAME_OVER_SIGN_X = 330
GAME_OVER_SIGN_Y = 150

BIG_FONT = 60
SMALL_FONT = 20
SCORE_FONT = 30

# MapGenerator
MAX_SEGMENTS_TO_SIDE = 20
MIN_SEGMENTS_TO_SIDE = 1
MAX_CURVATURE_COEFFICIENT = 7
MAX_CURVATURE = 15
MAP_LENGTH = 100  # When "car" is approaching to end of map, it's being extended by next value of MAP_LENGTH,
# so actually the road length is infinite
SAFE_EXCESS = 30  # Needed to deal with list index out of range problem
# (Because of drawRoad() function is called that fast when run, so map can't be generated fast enough to extend road
# map)
MAX_LEFT_DEVIATION_OF_ROAD = -350
MAX_RIGHT_DEVIATION_OF_ROAD = 340

# MyCar
CAR_STARTING_X = 500
CAR_STARTING_Y = 390

# Obstacle
OBSTACLE_STARTING_VELOCITY = 4.0
OBSTACLE_START_POINT = 9000

# Obstacle & Car
CAR_LENGTH = 98

# ObstacleGenerator
TRAFFIC_COEFFICIENT = 50
OBSTACLES_ACCELERATION_COEFFICIENT = 10000

# ObstacleGenerator & Car
CAR_WIDTH = 50

# Road
ROAD_SPEED = 50
WAY_SEGMENT_LAST = 5

# Road & ObstacleGenerator
WAY_SEGMENT_FIRST = -2
NUMBER_OF_OBSTACLES = 10

# ScoreBoard

# WaySegment
ROAD_WIDTH = 300
ROAD_BORDER_SIZE = 10

# WaySegment & Road
WAY_LENGTH = 100
