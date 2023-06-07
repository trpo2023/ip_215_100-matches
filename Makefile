.PHONY: all run test clean

all: run

run:
    python main.py

test:
    python -m unittest discover -s test -p '*_test.py'

clean:
    rm -rf __pycache__
