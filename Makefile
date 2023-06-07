# Настройки компиляции и исполнения
PYTHON = python3
MAIN_FILE = main.py

# Цель по умолчанию
all: run

# Сборка и запуск программы
run:
	$(PYTHON) $(MAIN_FILE)

# Тестирование
test:
	$(PYTHON) -m unittest discover tests

# Очистка сгенерированных файлов
clean:
	rm -rf __pycache__ *.pyc

# Правило .PHONY для целей, которые не являются файлами
.PHONY: all run test clean
