
pipeline {
    agent any

    parameters {
        string(name: 'CIA', defaultValue: '', description: 'CIA')
        string(name: 'PROJECT_KEY', defaultValue: '', description: 'Project key')
        string(name: 'FOLDER_PARENT', defaultValue: '', description: 'Parent folder')
        string(name: 'ENVIRONEMENT', defaultValue: '', description: 'Environment')
    }

    environment {
        XLD_BASE_URL = 'https://<xld-host>:<port>/deployit'
        XLD_CREDENTIALS = 'xld-credentials'
    }

    stages {
        stage('Lister les enfants XL Deploy') {
            steps {
                script {
                    def parentPath = [
                        'Infrastructure',
                        params.FOLDER_PARENT,
                        params.CIA,
                        params.ENVIRONEMENT,
                        params.PROJECT_KEY
                    ].findAll { it?.trim() }.join('/')

                    echo "Chemin recherché : ${parentPath}"

                    withCredentials([
                        usernamePassword(
                            credentialsId: env.XLD_CREDENTIALS,
                            usernameVariable: 'XLD_USER',
                            passwordVariable: 'XLD_PASSWORD'
                        )
                    ]) {
                        def queryUrl =
                            "${env.XLD_BASE_URL}/repository/query" +
                            "?parent=${java.net.URLEncoder.encode(parentPath, 'UTF-8')}" +
                            "&resultsPerPage=-1"

                        def response = httpRequest(
                            url: queryUrl,
                            httpMode: 'GET',
                            authentication: env.XLD_CREDENTIALS,
                            acceptType: 'APPLICATION_XML',
                            validResponseCodes: '200'
                        )

                        def xml = new XmlSlurper(false, false)
                            .parseText(response.content)

                        // Extraction des IDs des CI retournés par XL Deploy
                        def ciIds = []
                        xml.depthFirst().each { node ->
                            def id = node.attributes()['id']
                            if (id) {
                                ciIds << id.toString()
                            }
                        }

                        ciIds = ciIds.unique()

                        echo "Nombre de CI trouvés : ${ciIds.size()}"
                        ciIds.each { echo "CI : ${it}" }

                        // Recherche des CI dont l'identifiant contient "php"
                        def phpInstances = ciIds.findAll {
                            it.toLowerCase().contains('php')
                        }

                        echo "Instances contenant PHP : ${phpInstances.size()}"

                        if (phpInstances.isEmpty()) {
                            echo 'Aucune instance contenant PHP trouvée.'
                        }

                        def results = []

                        phpInstances.each { instanceId ->
                            echo "Recherche des applications sur : ${instanceId}"

                            def encodedInstanceId = instanceId
                                .split('/')
                                .collect {
                                    java.net.URLEncoder.encode(it, 'UTF-8')
                                }
                                .join('/')

                            def deployedUrl =
                                "${env.XLD_BASE_URL}/host/" +
                                "${encodedInstanceId}/deployed-applications"

                            try {
                                def deployedResponse = httpRequest(
                                    url: deployedUrl,
                                    httpMode: 'GET',
                                    authentication: env.XLD_CREDENTIALS,
                                    acceptType: 'APPLICATION_XML',
                                    validResponseCodes: '200'
                                )

                                def deployedXml = new XmlSlurper(false, false)
                                    .parseText(deployedResponse.content)

                                def appIds = []
                                deployedXml.depthFirst().each { node ->
                                    def id = node.attributes()['id']
                                    if (id) {
                                        appIds << id.toString()
                                    }
                                }

                                appIds = appIds.unique()

                                if (appIds.isEmpty()) {
                                    echo "Aucun déploiement trouvé sur ${instanceId}"
                                }

                                appIds.each { appId ->
                                    results << [
                                        instance: instanceId,
                                        application: appId,
                                        environment: params.ENVIRONEMENT
                                    ]
                                }
                            } catch (Exception e) {
                                echo "Erreur sur ${instanceId} : ${e.message}"
                            }
                        }

                        echo '========== RÉSULTATS =========='

                        if (results.isEmpty()) {
                            echo 'Aucune application déployée trouvée.'
                        } else {
                            results.each { result ->
                                echo """
Instance     : ${result.instance}
Application  : ${result.application}
Environnement: ${result.environment}
--------------------------------
"""
                            }
                        }

                        // Archive les résultats pour les consulter après le build.
                        writeFile(
                            file: 'xld-results.json',
                            text: groovy.json.JsonOutput.prettyPrint(
                                groovy.json.JsonOutput.toJson(results)
                            )
                        )
                        archiveArtifacts(
                            artifacts: 'xld-results.json',
                            fingerprint: true
                        )
                    }
                }
            }
        }
    }
}
