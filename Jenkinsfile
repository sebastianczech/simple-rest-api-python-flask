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
                always {
                    junit 'test-reports/report.xml'
                }
            }
        }
        stage('Test acceptance') {
            agent {
                node {
                    label 'homelab'
                }
            }
            steps {
                echo 'Acceptance testing..'

                sh 'robot --outputdir results atest/'
            }
            post {
                always {
                    step([
                        $class : 'RobotPublisher',
                        outputPath : 'results',
                        outputFileName : 'report.html',
                        disableArchiveOutput : false,
                        passThreshold : 100,
                        unstableThreshold: 95.0,
                        otherFiles : '',
                    ])
                }
            }
        }
    }
}