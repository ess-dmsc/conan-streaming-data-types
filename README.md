# conan-streaming-data-types

Conan package for [streaming-data-types](https://gitlab.esss.lu.se/ecdc/ess-dmsc/conan-streaming-data-types) ([github mirror](https://github.com/ess-dmsc/streaming-data-types)).

## Updating the conan package

If you have made some changes to _streaming-data-types_ and subsequently also want to update the conan-package, follow these instructions:

1. Edit line 8 of the _conanfile.py_-file in this repository to checkout the version of _streaming-data-types_ that you want to package. Note that this is used to indicate the version of the conan package.

2. When in the directory of the local copy of _conan-streaming-data-types_, execute this command:

   ```
   conan create . streaming-data-types/XXXXXXX@ess-dmsc/stable --build
   ```

   Where **XXXXXXX** is the first 7 characters in the SHA of the commit of _streaming-data-types_ that you are using. Note that this is used to indicate the version of the conan package.

3. Upload the new package to the relevant conan package repository by executing:

   ```
   conan upload streaming-data-types/XXXXXXX@ess-dmsc/stable --remote alias_of_repository
   ```

   Where **XXXXXXX** is the version of the conan package as mentioned above and **alias_of_repository** is exactly what it says. You can list all the repositories that your local conan installation is aware of by running: `conan remote list`; it is probably `ecdc-conan-virtual`.
