pipeline {
    agent any
    triggers {
        pollSCM('H/5 * * * *') // Checks for changes every 5 minutes
    }
    stages {
        stage('checkout') {
            steps {
                checkout scmGit(branches: [[name: 'main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/AnilChowdarypoka/elastic_search_crypto_data']])
            }
        }
        stage('build') {
            steps {
                sh 'python3 crypto_data_ingestion.py'
            }
        }
    }
}
