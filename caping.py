import requests
import time
import base64
import datetime
from requests.structures import CaseInsensitiveDict
def acaktimestamp():
    date = datetime.datetime.now()
    unix_time = int(datetime.datetime.timestamp(date)*1000)
    return unix_time


url_report = 'https://ai2.caping.co.id/v2/event/report'
data_report ='{"reports":[{"action":"browse_news","list":[{"articleType":1,"newsId":8499137,"status":1,"times":2,"totalms":40}]}]}'
header_report = CaseInsensitiveDict()
header_report['user-agent'] = 'Mozilla/5.0 (Linux; Android 11; ASUS_X01AD Build/RQ2A.210505.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36;CapingNews/5.4.2/287/D9DE14BB00E8EF2E2DA7EA0A7D7B5C8D9EB096FE1626246775403'
header_report['accept'] = 'application/json'
header_report['cookie'] = 'u=68247613;n=000000005c0530df235d75ed235d75ed'
config = f'42d0a68e525d48c3b75d79cb467221f6:{acaktimestamp()}'
config = config.encode('utf-8')
config = base64.b64encode(config)
config = config.decode('utf-8')
header_report['authorization'] = f'BASIC {config}'
header_report['ts'] = f'{acaktimestamp()}'
header_report['index'] = '9'


run = requests.post(url_report,headers = header_report,data = data_report)
print(run.text)