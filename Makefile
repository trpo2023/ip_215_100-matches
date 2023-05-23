.PHONY: all clean

PYTHON = python3

all: main

game: main.py welcome.py input.py player.py
	$(PYTHON) game.py

