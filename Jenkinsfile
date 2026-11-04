
def envResponse = httpRequest(
    url: "${XLD_URL}/deployit/repository/ci/${environmentPath}",
    httpMode: 'GET',
    authentication: env.XLD_CRED_ID,
    customHeaders: [
        [name: 'Accept', value: 'application/xml']
    ],
    validResponseCodes: '200'
)

def envXml = envResponse.content

println("Environment XML:")
println(envXml)

def updateResponse = httpRequest(
    url: "${XLD_URL}/deployit/repository/ci/${environmentPath}",
    httpMode: 'PUT',
    authentication: env.XLD_CRED_ID,
    customHeaders: [
        [name: 'Accept', value: 'application/xml'],
        [name: 'Content-Type', value: 'application/xml']
    ],
    requestBody: updatedEnvXml,
    validResponseCodes: '200:299'
)
