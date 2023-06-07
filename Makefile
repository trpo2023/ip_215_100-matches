.PHONY: all clean

PYTHON := python3
MAIN := main.py
LIB := matches_game.py
TEST := test.py

all: main test

main:
	$(PYTHON) $(MAIN)

test:
	$(PYTHON) $(TEST)

clean:
	rm -f *.pyc

