.PHONY: all clean

PYTHON = python3

all: make.py

game: main.py welcome.py input.py player.py game.py
	$(PYTHON) main.py

