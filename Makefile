	import os
import glob

APP_NAME = "matches"
APP_TEST_NAME = "matchestest"

CFLAGS = "-Wall -Wextra -Werror"
CPPFLAGS = "-I thirdparty -I src -MP -MMD"
GDB = "-g -O0"

BIN_DIR = "bin"
OBJ_DIR = "obj"
SRC_DIR = "src"
TEST_DIR = "test"

APP_PATH = os.path.join(BIN_DIR, APP_NAME)
LIB_PATH = os.path.join(OBJ_DIR, SRC_DIR, LIB_NAME + ".a")
TEST_PATH = os.path.join(BIN_DIR, TEST_DIR, APP_TEST_NAME)

SRC_EXT = "c"

APP_SOURCES = glob.glob(os.path.join(SRC_DIR, APP_NAME, f"*.{SRC_EXT}"))
APP_OBJECTS = [os.path.join(OBJ_DIR, src.replace(SRC_DIR, "") + ".o") for src in APP_SOURCES]
APP_TEST_SOURCES = glob.glob(os.path.join(TEST_DIR, f"*.{SRC_EXT}"))
APP_TEST_OBJECTS = [os.path.join(OBJ_DIR, src.replace(TEST_DIR, "") + ".o") for src in APP_TEST_SOURCES]

LIB_SOURCES = glob.glob(os.path.join(SRC_DIR, f"*.{SRC_EXT}"))
LIB_OBJECTS = [os.path.join(OBJ_DIR, src.replace(SRC_DIR, "") + ".o") for src in LIB_SOURCES]

DEPS = [obj.replace(".o", ".d") for obj in APP_OBJECTS + LIB_OBJECTS]

def execute_command(command):
		print(command)
		os.system(command)

def create_directory(directory):
    if not os.path.exists(directory):
			os.makedirs(directory)

def build_target(target, objects, additional_flags=""):
    command = f"gcc {CFLAGS} {GDB} {CPPFLAGS} {additional_flags} {' '.join(objects)} -o {target} -lm"
		execute_command(command)

def compile_source(source, object_file, additional_flags=""):
    command = f"gcc -c {CFLAGS} {GDB} {CPPFLAGS} {additional_flags} {source} -o {object_file}"
		execute_command(command)

def clean():
		execute_command(f"rm -f {APP_PATH} {LIB_PATH} {TEST_PATH}")
		execute_command(f"find {OBJ_DIR} -name '*.o' -exec rm -f {{}} \;")
		execute_command(f"find {OBJ_DIR} -name '*.d' -exec rm -f {{}} \;")

def all():
		create_directory(BIN_DIR)
		create_directory(OBJ_DIR)
		create_directory(os.path.join(OBJ_DIR, SRC_DIR, LIB_NAME))

		build_target(APP_PATH, APP_OBJECTS + [LIB_PATH])

def test():
	create_directory(BIN_DIR)
	create_directory(OBJ_DIR)
	create_directory(os.path.join(OBJ_DIR, TEST_DIR))
	build_target(TEST_PATH, APP_TEST_OBJECTS + [LIB_PATH])

if __name__ == "__main__":
		all()
