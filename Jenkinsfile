pipeline{
    agent any
    stages{
        stage("Build Docker Image"){
            steps{
                echo 'Build Docker Image'
                bat 'docker build -t mypythonapp .'
            }
        }
        stage('Docker login'){
            steps{
                bat 'docker login -u niharika345 -p Niharika@03'
            }
        }
        stage('Push docker image to docker hub'){
            steps{
                echo 'Pushing Docker Image to Docker Hub'
                bat 'docker tag <imagename> niharika345/devopsexam:latest'
                bat 'docker push niharika345/devopsexam:latest'
            }
        }
        stage('Deploy to kubernetes'){
            steps{
                bat 'kubectl apply -f deployment.yaml'
                bat 'kubectl apply -f service .yaml'
            }
        }
    }
}