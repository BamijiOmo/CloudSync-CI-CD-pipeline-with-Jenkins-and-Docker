pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Run App') {
            steps {
                sh 'python3 src/app.py & sleep 5'
                sh 'curl -s http://localhost:5000'
            }
        }

        stage('Docker Build') {
            steps {
                script {
                    docker.build('cloudsync-image')
                }
            }
        }

        stage('Deploy') {
            steps {
                echo '🚀 Deployment step placeholder — customize for S3, EC2, or multi-env rollout.'
            }
        }
    }
}

