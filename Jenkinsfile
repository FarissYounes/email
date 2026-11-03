def updateResponse = httpRequest(
    url: "${xldUrl}/deployit/repository/ci/${ciPath}",
    httpMode: 'PUT',
    authentication: 'XLD_CREDENTIALS',
    acceptType: 'APPLICATION_JSON',
    contentType: 'APPLICATION_JSON',
    requestBody: payload,
    validResponseCodes: '200:299'
)

echo "Modification XLD : ${updateResponse.status}"

ci.name = 'SMB02'
ci.address = '192.168.1.20'

def payload = groovy.json.JsonOutput.toJson(ci)

def ciPath = 'Infrastructure/CIA/ENVIRONMENT/SMB01'
def xldUrl = 'https://TON_XLD'

def response = httpRequest(
    url: "${xldUrl}/deployit/repository/ci/${ciPath}",
    httpMode: 'GET',
    authentication: 'XLD_CREDENTIALS',
    acceptType: 'APPLICATION_JSON',
    contentType: 'APPLICATION_JSON',
    validResponseCodes: '200'
)

def ci = new groovy.json.JsonSlurper().parseText(response.content)

echo "Type : ${ci.type}"
echo "ID : ${ci.id}"
