import requests
from requests.structures import CaseInsensitiveDict
import time
def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = 'Menunggu: {:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
while True:
    url_api = "https://app.v-tube.biz/api/todayVideoCount"
    url_ad = "https://app.v-tube.biz/api/completeAWatch"
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"

    data1 = '{"userId": "815302","sessionToken": "WVdAHwja4W7sxzL","virtualDeviceId": "46707c48d534bcec16664273e9cd232f","timestamp": 1626424712340,"version": "3.0.8","sign": "97c09fc182a9b822afd86650aa25baf9"}'
    data2 = data1
    cek_count = requests.post(url_api, headers=headers, data=data1)
    print(cek_count.text)
    cek_anu = cek_count.json()
    cek_anu = cek_anu['value']
    cek_complet = cek_anu['isComplete']
    cek_count = cek_anu['count']
    if cek_complet == True:
        print('Boss anda sudah klaim lo')
        break
    if cek_count == 10:
        print('Udah Complet Boss!')
        break
    cek_asu = requests.post(url_ad, headers=headers, data=data2)
    cek_asu = cek_asu.json()
    cek_code = cek_asu['code']
    if cek_code == 0:
        print("Berhasil Lihat Iklan!")
        print('Count Iklan: ',cek_count)
    else:
        print('Count Iklan: ',cek_count)
        cek_error = cek_asu['message']
        num = ""
        for c in cek_error:
            if c.isdigit():
                num = num + c
        waktu = 60
        num = int(num) * waktu
        countdown(int(num))




