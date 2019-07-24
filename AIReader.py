import base64,urllib.parse,urllib.request,urllib.error,json

def scan(name):

    access_token = '24.14d4cf2e93345ddfe663236f90aaddb1.2592000.1565819100.282335-16814012'
    url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic?access_token=' + access_token

    print("Please wait")
    f = open(name, 'rb')
# encode picture to base64
    img = base64.b64encode(f.read())
    params = {"image": img}
    params = urllib.parse.urlencode(params)
    data = params.encode('utf-8')
    r = urllib.request.Request(url,data=data)
    r.add_header('Content-Type', 'application/x-www-form-urlencoded')
    r = urllib.request.urlopen(r)
    content = r.read().decode()
    if(content):
        js = json.loads(content)
        js = js['words_result']
        st=''
        for i in range(len(js)):
            g = str(js[i])
            st+=g[11:len(g)-2]
            st+=" "
        return st