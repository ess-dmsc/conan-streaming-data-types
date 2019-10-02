@Library('ecdc-pipeline')
import ecdcpipeline.ContainerBuildNode
import ecdcpipeline.ConanPackageBuilder

project = "conan-streaming-data-types"

conan_remote = "ess-dmsc-local"
conan_user = "ess-dmsc"
conanPackageChannel = 'testing'

containerBuildNodes = [
  'centos': ContainerBuildNode.getDefaultContainerBuildNode('centos7'),
  'debian9': ContainerBuildNode.getDefaultContainerBuildNode('debian9'),
  'ubuntu1804': ContainerBuildNode.getDefaultContainerBuildNode('ubuntu1804'),
  'alpine': ContainerBuildNode.getDefaultContainerBuildNode('alpine')
]

packageBuilder = new ConanPackageBuilder(this, containerBuildNodes, conanPackageChannel)
packageBuilder.defineRemoteUploadNode('centos')

builders = packageBuilder.createPackageBuilders { container ->
  packageBuilder.addConfiguration(container)
}

def get_macos_pipeline() {
  return {
    node('macos') {
      cleanWs()
      // temporary until we have migrated to official flatbuffers conan package
      // in our our repositories, otherwise case difference in package name causes
      // conan to fail
      sh "conan remove -f FlatBuffers/*"
      dir("${project}") {
        stage("macOS: Checkout") {
          checkout scm
        }  // stage

        stage("macOS: Conan setup") {
          withCredentials([
            string(
              credentialsId: 'local-conan-server-password',
              variable: 'CONAN_PASSWORD'
            )
          ]) {
            sh "conan user \
              --password '${CONAN_PASSWORD}' \
              --remote ${conan_remote} \
              ${conan_user} \
              > /dev/null"
          }  // withCredentials
        }  // stage

        stage("macOS: Package") {
          sh "conan create . ${conan_user}/${conanPackageChannel} \
            --build=outdated"

            pkg_name_and_version = sh(
              script: "./get_conan_pkg_name_and_version.sh",
              returnStdout: true
            ).trim()
        }  // stage

        stage("macOS: Upload") {
          sh "upload_conan_package.sh conanfile.py \
            ${conan_remote} \
            ${conan_user} \
            ${conanPackageChannel}"
        }  // stage

        stage("macOS: Upload") {
          sh "conan upload \
            --all \
            ${conan_upload_flag} \
            --remote ${conan_remote} \
            ${pkg_name_and_version}@${conan_user}/${conanPackageChannel}"
        }  // stage
      }  // dir
    }  // node
  }  // return
}  // def

node {
  checkout scm
  builders['macOS'] = get_macos_pipeline()
  parallel builders
  cleanWs()
}
