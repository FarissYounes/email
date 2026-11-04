// Nouveau nom complet de l'objet dans le repository
def newObjectId = "Infrastructure/${params.CIA_TECH}/${params.CIA}/${xldEnvironment}-${ENVIRONMENT_TRIGRAM}/${PROJECT_KEY}/${NEW_SMBHOST_OBJECT_NAME}"

// Mise à jour de l'ID dans le XML
root.attributes().put('id', newObjectId)

// Génération du XML modifié
def writer = new StringWriter()
def printer = new XmlNodePrinter(new PrintWriter(writer))
printer.preserveWhitespace = true
printer.print(root)

def updatedXml = writer.toString()

// Vérifier que le nouvel objet n'existe pas déjà
def checkResponse = httpRequest(
    url: "${XLD_URL}/deployit/repository/ci/${newObjectId}",
    httpMode: 'GET',
    authentication: env.XLD_CRED_ID,
    customHeaders: [
        [name: 'Accept', value: 'application/xml']
    ],
    validResponseCodes: '200,404'
)

if (checkResponse.status == 200) {
    error("L'objet ${newObjectId} existe déjà dans XL Deploy")
}

// Création du nouvel objet
def postResponse = httpRequest(
    url: "${XLD_URL}/deployit/repository/ci/${newObjectId}",
    httpMode: 'POST',
    authentication: env.XLD_CRED_ID,
    customHeaders: [
        [name: 'Accept', value: 'application/xml'],
        [name: 'Content-Type', value: 'application/xml']
    ],
    requestBody: updatedXml,
    validResponseCodes: '200:299'
)

echo "XLD creation HTTP status: ${postResponse.status}"
echo "New SmbHost object created successfully"
println(postResponse.content)
