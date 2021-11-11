pipeline {
 environment {
        //TODO # 1 --> once you sign up for Docker hub, use that user_id here
        registry = "valikkr/public:${BUILD_NUMBER}"
        //TODO #2 - update your credentials ID after creating credentials for connecting to Docker Hub
        registryCredential = 'dockerhub_id'
        dockerImage = ''
    }
    
 agent any
  stages {
    stage('Cloning Git') {
      steps {
        checkout([$class: 'GitSCM', branches: [[name: '*/*']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/valikkr/shared1.git']]])

      }
    }
    stage('Building image') {
      steps{
        script {
          sh 'docker build -t valikkr/public .'
        }
      }
    }
    stage('Pushing Image') {
      steps{
        script {
          docker.withRegistry( '', registryCredential ) {
            sh 'docker tag flask:latest valikkr/public:${BUILD_NUMBER}'
             sh'docker push valikkr/public:${BUILD_NUMBER}'
          }
        }
      }
    }
  }
