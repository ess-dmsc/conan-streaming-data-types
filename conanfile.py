import shutil
from conans import ConanFile, CMake, tools
from conans.util import files


class StreamingDataTypesConan(ConanFile):
    name = "streaming-data-types"
    version = "361bf7b"
    license = "BSD 2-Clause"
    url = "https://bintray.com/ess-dmsc/streaming-data-types"
    settings = "compiler", "arch"
    generators = "cmake"
    requires = "FlatBuffers/1.8.0@ess-dmsc/stable"

    def source(self):
        self.run(
            "git clone https://github.com/ess-dmsc/{}.git".format(self.name)
        )
        with tools.chdir("./{}".format(self.name)):
            self.run("git checkout 361bf7b3ef88ba23d01e0dcd1bfaa26619fa089d")

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
