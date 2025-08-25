node {
  timestamps {
    stage('Checkout') {
      // In Scripted, there is NO "steps" block
      git url: 'https://github.com/Danush999/Jenkins.git', branch: 'main'
    }

    stage('Build') {
      echo "Running build..."
      // sh 'make build'
    }

    stage('Test') {
      echo "Running tests..."
      // sh 'pytest -q'
      // junit 'reports/test-results/*.xml'
    }

    stage('Archive') {
      archiveArtifacts artifacts: 'artifacts/**/*', allowEmptyArchive: true
    }
  }
}
