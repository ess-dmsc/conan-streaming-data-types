import shutil
from conans import ConanFile, CMake, tools
from conans.util import files


class StreamingDataTypesConan(ConanFile):
    name = "streaming-data-types"
    version = "5fde74d"
    license = "BSD 2-Clause"
    settings = "compiler", "arch"
    generators = "cmake"
    requires = "flatbuffers/24.3.25"

    def source(self):
        self.run("git clone https://github.com/ess-dmsc/{}.git".format(self.name))
        with tools.chdir("./{}".format(self.name)):
            self.run("git checkout {}".format(self.version))

    def build(self):
        files.mkdir("./{}/build".format(self.name))
        shutil.copyfile(
            "conanbuildinfo.cmake", "./{}/build/conanbuildinfo.cmake".format(self.name)
        )
        with tools.chdir("./{}/build".format(self.name)):
            cmake = CMake(self)
            cmake.configure(source_dir="..", build_dir=".")
            cmake.build(build_dir=".")

    def package(self):
        self.copy("*.h", dst="include", keep_path=False)
