pipeline {
    agent any

    parameters {
        choice(
            name: 'ENVIRONMENT',
            choices: ['dev', 'staging', 'prod'],
            description: 'Select the environment for the Online Examination System'
        )
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/nithish474/online-exam-project-1.git'
            }
        }

        stage('Show Environment') {
            steps {
                echo "Selected environment: ${params.ENVIRONMENT}"
            }
        }

        stage('Build Online Examination System') {
            steps {
                bat 'python -m py_compile app.py'
                echo "Online Examination System built successfully for ${params.ENVIRONMENT}."
            }
        }
    }
}