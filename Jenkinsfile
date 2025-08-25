stage('Checkout') {
  steps {
    checkout([$class: 'GitSCM',
      userRemoteConfigs: [[url: 'https://github.com/Danush999/Jenkins.git']],
      branches: [[name: '*/main']],
      extensions: [] // minimal
    ])
  }
}
