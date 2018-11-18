pipeline {
  agent any
  stages {
    stage("Unit Tests") {
      sh "python -m unittest test_calculator.py"
    }
    stage("Run App") {
      echo "sh 'python calculator.py 2 3'"
    }
  }
}
