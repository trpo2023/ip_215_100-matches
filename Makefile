.PHONY: all clean

# Имя результирующего файла
OUTPUT = main

all: main test

main:
	$(PYTHON) $(MAIN)

test:
	$(PYTHON) $(TEST)

clean:
	rm -f *.pyc

