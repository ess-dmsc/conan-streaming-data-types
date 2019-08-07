# conan-streaming-data-types

Conan package for streaming-data-types (https://github.com/ess-dmsc/streaming-data-types)
(experimental).

## Updating the conan package

If you have made some changes to *streaming-data-types* and subsequently also want to update the conan-package, follow these instructions:

1. Edit line 8 of the *conanfile.py*-file in this repository to checkout the version of *streaming-data-types* that you want to package.
	Note that this is used to indicate the version of the conan package.

2. Edit line 9 of *Jenkinsfile* and set `conanPackageChannel` to `testing`.

3. Conan package should be automaticaly build and after some time will be available as `streaming-data-types/XXXXXXX@ess-dmsc/testing`



### Alternatively
1. Edit line 8 of the *conanfile.py*-file in this repository to checkout the version of *streaming-data-types* that you want to package.
	Note that this is used to indicate the version of the conan package.

2. Edit line 9 of *Jenkinsfile* to set `conanPackageChannel` to `testing`.

3. When in the directory of the local copy of *conan-streaming-data-types*, execute this command:

	```
	conan create . streaming-data-types/XXXXXXX@ess-dmsc/stable
	```
	Where **XXXXXXX** is the first 7 characters in the SHA of the commit of *streaming-data-types* that you are using. Note that this is used to indicate the version of the conan package.

4. Upload the new package to the relevant conan package repository by executing:

	```
	conan upload streaming-data-types/XXXXXXX@ess-dmsc/stable --remote alias_of_repository
	```

	Where **XXXXXXX** is the version of the conan package as mentioned above and **alias\_of\_repository** is exactly what it says. You can list all the repositories that your local conan installation is aware of by running: `conan remote list`.
