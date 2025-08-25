$jenkinsfile = @"
pipeline {
  agent any
  options { timestamps(); ansiColor('xterm') }

  triggers { cron('H H/12 * * *') } // optional

  stages {
    stage('Checkout') { steps { checkout scm } }

    stage('Set up venv') {
      steps {
        bat 'py --version'
        bat 'py -m venv .venv'
        bat '.venv\Scripts\python -m pip install --upgrade pip'
        bat '.venv\Scripts\pip install -r requirements.txt'
      }
    }

    stage('Unit tests') {
      steps {
        bat '.venv\Scripts\pytest -q --junitxml=test-results\junit.xml'
      }
      post {
        always {
          junit 'test-results/junit.xml'
          archiveArtifacts artifacts: 'test-results/junit.xml', fingerprint: true
        }
      }
    }
  }

  post {
    success { echo 'Build succeeded ✅' }
    failure { echo 'Build failed ❌' }
  }
}
"@

$enc = New-Object System.Text.UTF8Encoding($false)   # <- no BOM
[IO.File]::WriteAllText("$PWD\Jenkinsfile", $jenkinsfile, $enc)

git add Jenkinsfile
git commit -m "fix: save Jenkinsfile without BOM"
git push
