# Functions for GitLab CI

# Sets up Conan by adding a remote path and authenticating the user
setup_conan() {
    local conan_name=$1
    local conan_url=$2

    echo 'Setting up Conan...'
    conan remote add "$conan_name" "$conan_url" --force
    conan user --password "$ESS_ARTIFACTORY_ECDC_CONAN_TOKEN" --remote "$conan_name" "$ESS_ARTIFACTORY_ECDC_CONAN_USER"
}

# Creates a Conan package from the specified path
conan_package_creation() {
    local conan_path=$1

    echo 'Creating Conan package...'
    conan create $conan_path ${CONAN_USER}/${CONAN_PKG_CHANNEL} --build=outdated 
}

# Uploads packages to the external Conan repository
upload_packages_to_conan_external() {
  local conan_file_path=$1

  echo 'Uploading packages to Conan External Artifactory...'
  packageNameAndVersion=$(conan inspect --attribute name --attribute version $conan_file_path | awk -F': ' '{print $2}' | paste -sd'/')
  conan upload --all --no-overwrite --remote ecdc-conan-external ${packageNameAndVersion}@${CONAN_USER}/${CONAN_PKG_CHANNEL}
}

# Uploads packages to the release Conan repository
upload_packages_to_conan_release() {
  local conan_file_path=$1

  echo 'Uploading packages to Conan Release Artifactory...'
  packageNameAndVersion=$(conan inspect --attribute name --attribute version $conan_file_path | awk -F': ' '{print $2}' | paste -sd'/')
  conan upload --no-overwrite --remote ecdc-conan-release ${packageNameAndVersion}@${CONAN_USER}/${CONAN_PKG_CHANNEL}
}