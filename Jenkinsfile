pipeline {
    agent {
        docker {
            image 'python:3.8-alpine'
        }
    }

    stages {
        stage('Info') {
            steps {
                echo 'Current working directory: '

                sh 'pwd'

                echo 'List of files: '

                sh 'ls -la'
            }
        }
        stage('Install') {
            steps {
                echo 'Installing packages..'

                sh 'pip install -r requirements.txt'
            }
        }
        stage('Test unit') {
            steps {
                echo 'Unit testing..'

                sh 'pytest test.py'
            }
            post {
                always {
                    junit 'target/surefire-reports/*.xml'
                }
            }
        }
        stage('Test acceptance') {
            steps {
                echo 'Acceptance testing..'
            }
        }
    }
}