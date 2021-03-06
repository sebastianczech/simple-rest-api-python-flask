pipeline {
    agent none

    stages {
        stage('Info') {
            agent {
                docker {
                    image 'python:3.8-alpine'
                }
            }
            steps {
                echo 'Current working directory: '

                sh 'pwd'

                echo 'List of files: '

                sh 'ls -la'
            }
        }
        stage('Build') {
            agent {
                docker {
                    image 'python:3.8-alpine'
                }
            }
            steps {
                echo 'Compile main.py..'

                sh 'python -m py_compile main.py'
            }
        }
        stage('Test unit') {
            agent {
                docker {
                    image 'qnib/pytest'
                }
            }
            steps {
                echo 'Unit testing..'

                sh 'pytest test.py --junit-xml=test-reports/report.xml '
            }
            post {
                success {
                    build wait: false, job: 'CI-CD-pipeline-acceptance-tests'
                }
                always {
                    junit 'test-reports/report.xml'
                }
            }
        }
    }
}