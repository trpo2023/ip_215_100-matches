# Компилятор и флаги
CC = gcc
CFLAGS = -Wall -Wextra

# Имена исполняемого файла и библиотеки
EXECUTABLE = matches_game
LIBRARY = libgame.so

# Основная цель: сборка исполняемого файла
all: $(EXECUTABLE)

# Сборка исполняемого файла
$(EXECUTABLE): main.o $(LIBRARY)
	$(CC) $(CFLAGS) -o $@ $< -L. -lgame

# Сборка объектного файла main.o
main.o: main.c game.h
	$(CC) $(CFLAGS) -c $<

# Сборка библиотеки
$(LIBRARY): game.o
	$(CC) $(CFLAGS) -shared -o $@ $<

# Сборка объектного файла game.o
game.o: game.c game.h
	$(CC) $(CFLAGS) -fPIC -c $<

# Очистка собранных файлов
clean:
	rm -f $(EXECUTABLE) $(LIBRARY) *.o
