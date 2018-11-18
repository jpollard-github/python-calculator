pipeline {
  agent {
    node {
      label 'python3'
    }
  }
  stages {
    stage("Unit Tests") {
      steps {
        sh "python3 -m unittest test_calculator.py"
      }
    }
    stage("Run App") {
      steps {
        echo "sh 'python3 calculator.py 2 3'"
      }
    }
  }
}
