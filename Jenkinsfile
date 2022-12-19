@Library('ecdc-pipeline')
import ecdcpipeline.ContainerBuildNode
import ecdcpipeline.ConanPackageBuilder

project = "conan-streaming-data-types"

conan_user = "ess-dmsc"
conanPackageChannel = 'stable'

containerBuildNodes = [
  'centos': ContainerBuildNode.getDefaultContainerBuildNode('centos7-gcc11'),
  'debian': ContainerBuildNode.getDefaultContainerBuildNode('debian11'),
  'ubuntu': ContainerBuildNode.getDefaultContainerBuildNode('ubuntu2204'),
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

        stage("macOS: Package") {
          sh "conan create . ${conan_user}/${conanPackageChannel} \
            --build=outdated"
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
