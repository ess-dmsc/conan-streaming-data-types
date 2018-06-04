import shutil
from conans import ConanFile, CMake, tools
from conans.util import files


class StreamingDataTypesConan(ConanFile):
    name = "streaming-data-types"
    version = "d429d55"
    license = "BSD 2-Clause"
    url = "https://bintray.com/ess-dmsc/streaming-data-types"
    settings = "compiler", "arch"
    generators = "cmake"
    requires = "FlatBuffers/1.9.0@ess-dmsc/stable"

    def source(self):
        self.run(
            "git clone https://github.com/ess-dmsc/{}.git".format(self.name)
        )
        with tools.chdir("./{}".format(self.name)):
            self.run("git checkout d429d55a77b45165e88749aa5354569b26d4724c")

    def build(self):
        files.mkdir("./{}/build".format(self.name))
        shutil.copyfile(
            "conanbuildinfo.cmake",
            "./{}/build/conanbuildinfo.cmake".format(self.name)
        )
        with tools.chdir("./{}/build".format(self.name)):
            cmake = CMake(self)
            cmake.configure(source_dir="..", build_dir=".")
            cmake.build(build_dir=".")

    def package(self):
        self.copy("*.h", dst="include", keep_path=False)
