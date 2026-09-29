pipeline {
  agent any
  stages {
    stage('Unit Tests') {
      steps {
        sh '''
          python3 -m venv venv
          . venv/bin/activate
          pip install -r requirements-dev.txt
          pytest -v
        '''
      }
    }
    stage('SonarQube Analysis') {
      steps {
        withSonarQubeEnv('sonarqube') {
          sh "${tool 'sonar-scanner'}/bin/sonar-scanner"
        }
      }
    }
    stage('Quality Gate') {
      steps {
        timeout(time: 5, unit: 'MINUTES') { waitForQualityGate abortPipeline: true }
      }
    }
  }
}
