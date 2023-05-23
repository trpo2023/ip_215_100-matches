.PHONY: all clean

# Имя результирующего файла
OUTPUT = main

# Список исходных файлов
SOURCES = main.py intro.py take_matches.py switch_player.py result.py

# Правило по умолчанию
all: $(OUTPUT)

# Цель для сборки результирующего файла
$(OUTPUT): $(OBJECTS)
	@echo "Сборка $(OUTPUT)..."
	@python -m compileall .
	@python -O -m py_compile $(SOURCES)
	@echo "Готово."

# Цель для очистки
clean:
	@echo "Очистка..."
	@rm -rf __pycache__ *.pyc $(OUTPUT)
	@echo "Готово."
