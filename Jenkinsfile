pipeline {
  agent any
  stages {
    stage('git_checkout') {
      steps {
        git(url: 'https://github.com/tryorfry/api_wrapper_py.git', branch: 'master')
      }
    }

  }
}