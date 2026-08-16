pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code from GitHub'
                checkout scm
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install pytest --break-system-packages --quiet'
            }
        }
        stage('Build') {
            steps {
                sh 'python3 heatwave.py'
            }
        }
        stage('Test') {
            steps {
                sh 'python3 -m pytest test_heatwave.py -v'
            }
        }
    }
    post {
        success {
            echo 'Build and tests completed successfully.'
        }
        failure {
            echo 'Build failed - check test output above.'
        }
    }
}
