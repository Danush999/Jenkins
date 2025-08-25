stage('Checkout') {
  steps {
    checkout([$class: 'GitSCM',
      branches: [[name: '*/main']],
      userRemoteConfigs: [[url: 'https://github.com/Danush999/Jenkins.git' /* , credentialsId: 'github-creds' */]],
      extensions: [],
      gitTool: 'jgit'   // <-- force built-in JGit
    ])
  }
}
