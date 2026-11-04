def oldPath = "Infrastructure/BIPD3/BIPPR/78-PRD/OLD_NAME"
def newName = "sql2-NEW_NAME"

// 1. Renommer l'objet
def renameResponse = httpRequest(
    url: "${XLD_URL}/deployit/repository/rename/${oldPath}?newName=${newName}",
    httpMode: 'POST',
    authentication: env.XLD_CRED_ID,
    acceptType: 'APPLICATION_XML',
    validResponseCodes: '200:299'
)

println("Rename status: ${renameResponse.status}")

// 2. Construire le nouveau chemin
def newPath = "Infrastructure/BIPD3/BIPPR/78-PRD/${newName}"

// 3. GET du nouvel objet
def getResponse = httpRequest(
    url: "${XLD_URL}/deployit/repository/ci/${newPath}",
    httpMode: 'GET',
    authentication: env.XLD_CRED_ID,
    acceptType: 'APPLICATION_XML',
    validResponseCodes: '200'
)

// 4. Modifier address
def root = new XmlParser(false, false).parseText(getResponse.content)

root.address[0].value = "NOUVELLE_ADRESSE"

// 5. Générer XML
def writer = new StringWriter()
new XmlNodePrinter(new PrintWriter(writer)).print(root)

// 6. PUT
def putResponse = httpRequest(
    url: "${XLD_URL}/deployit/repository/ci/${newPath}",
    httpMode: 'PUT',
    authentication: env.XLD_CRED_ID,
    contentType: 'APPLICATION_XML',
    acceptType: 'APPLICATION_XML',
    requestBody: writer.toString(),
    validResponseCodes: '200:299'
)

println("Update status: ${putResponse.status}")

def parser = new XmlParser(false, false)
def root = parser.parseText(xml)

// Modification du nom de l'objet
root.@id = "Infrastructure/BIPD3/BIPPR/78-PRD/sql2-NEW_NAME"

// Modification de l'adresse
root.address[0].value = "192.168.X.X"

ggggggg



// Génération du XML
def writer = new StringWriter()
def printer = new XmlNodePrinter(new PrintWriter(writer))
printer.preserveWhitespace = true
printer.print(root)

def updatedXml = writer.toString()

def putResponse = httpRequest(
    url: "${XLD_URL}/deployit/repository/ci/${objectPath}",
    httpMode: 'PUT',
    authentication: env.XLD_CRED_ID,
    acceptType: 'APPLICATION_XML',
    contentType: 'APPLICATION_XML',
    requestBody: updatedXml,
    validResponseCodes: '200:299'
)

println("PUT response: ${putResponse.content}")

