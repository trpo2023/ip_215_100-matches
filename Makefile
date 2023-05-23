.PHONY: all clean

PYTHON = python3

all: main.py

game: main.py welcome.py input.py player.py game.py
	$(PYTHON) main.py

