pipeline {
  agent any
  stages {
    stage("Unit Tests") {
      steps {
        sh "python -m unittest test_calculator.py"
      }
    }
    stage("Run App") {
      steos {
        echo "sh 'python calculator.py 2 3'"
      }
    }
  }
}
