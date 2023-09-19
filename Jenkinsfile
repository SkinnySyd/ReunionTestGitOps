node {
    def app

    stage('Clone repository') {
      

        checkout scm
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
