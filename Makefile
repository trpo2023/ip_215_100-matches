	import os

CC = "gcc"
CFLAGS = "-Wall -Wextra -Wpedantic"
LIBRARY = "libmatches.a"
SRC_DIR = "src"
OBJ_DIR = "obj"
BUILD_DIR = "build"

LIB_SRC = os.path.join(SRC_DIR, "lib", "matches_game.c")
MAIN_SRC = os.path.join(SRC_DIR, "main.c")

LIB_OBJ = os.path.join(OBJ_DIR, "%s.o" % os.path.splitext(os.path.basename(LIB_SRC))[0])
MAIN_OBJ = os.path.join(OBJ_DIR, "%s.o" % os.path.splitext(os.path.basename(MAIN_SRC))[0])

EXECUTABLE = os.path.join(BUILD_DIR, "game")

THIRDPARTY_DIR = "thirdparty"

TEST_SRC_DIR = "test"
TEST_OUT_NAME = "matches-test"
TEST_OBJ_DIR = os.path.join(OBJ_DIR, TEST_OUT_NAME)
TEST_OBJECTS = [os.path.join(TEST_OBJ_DIR, "ctest.o"), os.path.join(TEST_OBJ_DIR, "main.o")]

def prepare():
		os.makedirs(os.path.join(".", BUILD_DIR, TEST_OUT_NAME), exist_ok=True)
		os.makedirs(os.path.join(".", OBJ_DIR, TEST_OUT_NAME), exist_ok=True)

def build_executable():
	os.system("%s %s -o %s %s -I %s -L %s -lmatches" % (CC, CFLAGS, EXECUTABLE, " ".join([MAIN_OBJ, LIB_OBJ]), SRC_DIR, BUILD_DIR))

def build_library():
		os.system("ar rcs %s %s" % (os.path.join(BUILD_DIR, LIBRARY), LIB_OBJ))

def build_test():
		os.system("%s %s %s -I%s -I%s -L%s -lmatches -w -o %s" % (CC, " ".join(TEST_OBJECTS), THIRDPARTY_DIR, SRC_DIR, BUILD_DIR, os.path.join(BUILD_DIR, TEST_OUT_NAME, TEST_OUT_NAME)))

def compile_lib_obj():
		os.system("%s %s -c %s -o %s" % (CC, CFLAGS, LIB_SRC, LIB_OBJ))

def compile_main_obj():
		os.system("%s %s -c %s -o %s -I %s" % (CC, CFLAGS, MAIN_SRC, MAIN_OBJ, SRC_DIR))

def compile_test_objs():
    for test_file in os.listdir(TEST_SRC_DIR):
        if test_file.endswith(".c"):
            test_src = os.path.join(TEST_SRC_DIR, test_file)
            test_obj = os.path.join(TEST_OBJ_DIR, "%s.o" % os.path.splitext(test_file)[0])
				os.system("%s -I%s -I%s -L%s -lmatches -c %s -w -o %s" % (CC, THIRDPARTY_DIR, SRC_DIR, BUILD_DIR, test_src, test_obj))

def clean():
		os.system("rm -f -r %s/*.o %s %s %s" % (OBJ_DIR, LIBRARY, EXECUTABLE, BUILD_DIR))

def run():
		os.system("./%s" % EXECUTABLE)

def test():
		os.system("./%s" % os.path.join(BUILD_DIR, TEST_OUT_NAME, TEST_OUT_NAME))

if __name__ == "__main__":
		prepare()
		compile_lib_obj()
		compile_main_obj()
		build_library()
		build_executable()
		compile_test_objs()
		build_test()
