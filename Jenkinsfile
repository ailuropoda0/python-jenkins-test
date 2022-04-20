pipeline {
  agent any
  stages {
    stage('Black') {
      steps {
        sh 'python black .'
      }
    }

    stage('Testing') {
      steps {
        sh 'python -m unittest'
      }
    }

  }
}