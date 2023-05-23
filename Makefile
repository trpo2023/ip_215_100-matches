.PHONY: all clean

PYTHON = python3

all: game

game: game.py welcome.py input.py player.py
	$(PYTHON) game.py

