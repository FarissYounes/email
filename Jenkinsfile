
stage('Update SmbHost Object') {
    when {
        expression {
            env.OBJECT_EXISTENCE_STATUS != 'true'
        }
    }

    steps {
        script {

            def xldEnvironment = xldEnvironmentMapping(params.ENVIRONMENT_TRIGRAM)

            def ciaCiPath = "Infrastructure/CIA/${params.CIA}"

            // 1. GET : Recuperer le contenu du CI
            def response = httpRequest(
                url: "${XLD_URL}/deployit/repository/ci/${SMBHOST_OBJECT_NAME}",
                httpMode: 'GET',
                authentication: env.XLD_CRED_ID,
                acceptType: 'APPLICATION_JSON',
                contentType: 'APPLICATION_JSON',
                validResponseCodes: '200'
            )

            def ciaCi = new groovy.json.JsonSlurper().parseText(response.content)

            echo "CI retrieved successfully"
            echo "CI ID: ${ciaCi.id}"
            echo "CI Type: ${ciaCi.type}"

            // 2. REPLACE : Modifier les proprietes
            assert ciaCi.type == 'overthere.SmbHost' :
                "Invalid CI type: ${ciaCi.type}"

            ciaCi.name = params.NEW_SMBHOST_NAME
            ciaCi.address = params.NEW_SMBHOST_ADDRESS

            echo "New name: ${ciaCi.name}"
            echo "New address: ${ciaCi.address}"

            // Convertir l'objet modifie en JSON
            def updatedCi = groovy.json.JsonOutput.toJson(ciaCi)

            // 3. PUT : Envoyer les modifications vers XLD
            def putResponse = httpRequest(
                url: "${XLD_URL}/deployit/repository/ci/${SMBHOST_OBJECT_NAME}",
                httpMode: 'PUT',
                authentication: env.XLD_CRED_ID,
                acceptType: 'APPLICATION_JSON',
                contentType: 'APPLICATION_JSON',
                requestBody: updatedCi,
                validResponseCodes: '200:299'
            )

            echo "XLD update HTTP status: ${putResponse.status}"
            echo "SmbHost object updated successfully!"

        }
    }
}
