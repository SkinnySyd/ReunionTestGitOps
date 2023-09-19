node {
    def app

    stages {
        stage('Clone repository') {
            steps {
                // Checkout the 'Dev' branch from your GitHub repository
                checkout scmGit(
                    branches: [[name: 'Dev']],
                    userRemoteConfigs: [[url: 'https://github.com/SkinnySyd/ReunionTestGitOps.git']])
            }
        }

        // Add other stages as needed for your pipeline
    }

    stage('Build image') {
  
       app = docker.build("skinnysydcontainersregistry.azurecr.io/pylocaltestpfe")
    }

    stage('Test image') {
  

        app.inside {
            sh 'echo "Tests passed"'
        }
    }

    stage('Push image') {
        
        docker.withRegistry('https://skinnysydcontainersregistry.azurecr.io', 'azurecr') {
            app.push("${env.BUILD_NUMBER}")
        }
    }
    
    stage('Trigger ManifestUpdate') {
                echo "triggering updatemanifestjob"
                build job: 'updatemanifestdev', parameters: [string(name: 'DOCKERTAG', value: env.BUILD_NUMBER)]
        }
}
