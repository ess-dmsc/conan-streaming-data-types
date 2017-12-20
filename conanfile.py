import os
from conans import ConanFile, CMake, tools
from conans.errors import ConanException


class StreamingDataTypesConan(ConanFile):
    name = "streaming-data-types"
    version = "<version>"
    license = "BSD 2-Clause"
    url = "https://bintray.com/ess-dmsc/streaming-data-types"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake", "virtualrunenv"

    def source(self):
        self.run("git clone https://github.com/ess-dmsc/streaming-data-types.git")
        self.run("cd streaming-data-types && git checkout <commit>")

    def build(self):
        cmake = CMake(self)

        try:
            self.output.info("Try to run cmake3")
            self.run("cmake3 --version")
            cmake_command = "cmake3"
        except ConanException:
            self.output.info("Using cmake instead of cmake3")
            cmake_command = "cmake"

        cmake.definitions["BUILD_EVERYTHING"] = "OFF"
        if tools.os_info.is_macos:
            cmake.definitions["CMAKE_MACOSX_RPATH"] = "ON"
            cmake.definitions["CMAKE_SHARED_LINKER_FLAGS"] = "-headerpad_max_install_names"

        self.run('%s streaming-data-types %s' % (cmake_command, cmake.command_line))
        self.run("%s --build . %s" % (cmake_command, cmake.build_config))

        os.rename(
            "streaming-data-types/LICENSE.md",
            "streaming-data-types/LICENSE.streaming-data-types"
        )

    def package(self):
        self.copy("*.h", dst="include/graylog_logger", src="streaming-data-types/include/graylog_logger")
        self.copy("*.hpp", dst="include/graylog_logger", src="streaming-data-types/include/graylog_logger")
        self.copy("LICENSE.*", src="streaming-data-types")

    def package_info(self):
        self.cpp_info.libs = ["graylog_logger"]
