pipeline {
  agent any
  stages {
    stage("Unit Tests") {
      steps {
        sh "python -m unittest test_calculator.py"
      }
    }
    stage("Run App") {
      steps {
        echo "sh 'python calculator.py 2 3'"
      }
    }
  }
}
