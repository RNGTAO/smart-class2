import urllib3
import base64
from urllib.parse import urlencode
import CONFIG

# 人脸检测，人脸识别模型部署在服务器上面
def fa_check(picpath):
    access_token = CONFIG.access_token
    http=urllib3.PoolManager()
    print(picpath)
    url='https://aip.baidubce.com/rest/2.0/face/v3/detect?access_token='+access_token
    f = open(picpath,'rb')
    img = base64.b64encode(f.read())
    params={'image':''+str(img,'utf-8')+'','image_type':'BASE64','face_field':'age,beauty,faceshape,gender,glasses'}
    params=urlencode(params)
    request=http.request('POST',
                          url,
                          body=params,
                          headers={'Content-Type':'application/json'})

    result = str(request.data,'utf-8')
    result_sp = result.split('"')
    if(result_sp[5]=="SUCCESS"):
        isface = True
        face_num_sp = result_sp[16]
        face_num = face_num_sp[1:-1]
        return float(face_num)
    else:
        isface = False
        print("没有检测到人")
        return(0)

