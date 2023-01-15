import requests,io
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
from datetime import date
import pandas as pd

software_names = [SoftwareName.CHROME.value]
operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]
user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)
user_agents = user_agent_rotator.get_user_agents()
user_agent = user_agent_rotator.get_random_user_agent()


cookie2="CFID=23177110; CFTOKEN=9c8dd389bab00678-F46FE363-C180-6564-6B343C855C53A8F0; HASLOGGEDIN=""; nlbi_1875454=oBNQG3Rh8ya9nMcj5D1AxQAAAADdALhpueiEIn6A2o8c1wP8; visid_incap_1875454=OoENKy+cTLieYRb7/L8VwZWHvGMAAAAAQUIPAAAAAAC8qqFqm8CxlFn6Lv+giMx9; _gcl_au=1.1.368813085.1673299863; usi_id=hanl71_1673299863; calltrk_referrer=https%3A//colab.research.google.com/; calltrk_landing=https%3A//www.aaii.com/sentimentsurvey/sent_results; calltrk_session_id=a2556e8e-47d0-4a83-811c-f60cd0f8a381; hubspotutk=9f422165b8d71dc9ecb17532511c5933; __hssrc=1; addshoppers.com=2%7C1%3A0%7C10%3A1673299864%7C15%3Aaddshoppers.com%7C44%3ANjE2ZGM3OTU5NjM4NDI1ZDk0MzYxYmM3M2M2YjEwOGU%3D%7Cf09d60494d4ea2e93b41ad5c4ce37b2cff9740d1c2b24642263c351633efc114; EMAILSIGNUPSENT=0; __utma=221881480.900535306.1673299863.1673301386.1673301386.1; __utmc=221881480; __utmz=221881480.1673301386.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); incap_ses_1460_1875454=6K/rM+3L+A/ww5vzpfZCFDUGvWMAAAAA6n5WGMNGxfzDJyytHbZQaQ==; incap_ses_1172_1875454=p4/EbwNI/3oZr9LslMhDEF8LvWMAAAAAv6oHLff5hRMyr/OR6LtoUQ==; incap_ses_1169_1875454=/n8oNDbxfkB+wwJWGyA5EHcQvWMAAAAAGq9RO3nMUXKm/63XScLGJA==; ubvt=83b723d8-5dd4-4abb-89c0-8a2cf1a51399; incap_ses_1191_1875454=H9KuYh3DwgiSopqGaEiHEGaawGMAAAAAspPcmL6jIxAvxOWuPghwBA==; _gid=GA1.2.172637784.1673575744; incap_ses_358_1875454=yl8lTwX/o1VnQcGt99/3BGHzwGMAAAAA6ixNqroHY7x8b4wuN0bXZg==; expectedValue=85.5; JSESSIONID=436CD193E60322BA4E520B23898A74B1.cfusion; __hstc=242524765.9f422165b8d71dc9ecb17532511c5933.1673299864417.1673575748667.1673591666737.6; reese84=3:wY++i5moH92NtAaRNMBW0w==:yJq5H9dxTiJUnroANL7JufsEH8HihhGUX+uEd78mn/VpfPYxdcrYgjpvjVGO1lcNPXNzUwLeleZExtGJwsl1pCf6PRvzRJsu8VB0tDR7DnTmk5mI+/JvAs5kqvKCYUjwKEuXyUfXxuHkWlfUhXvwxnUbDQ4w/kkxQOWy8hWI0nKtIO/gUTysmS6Zn0z+rHRVDTY0p+0G9c5/1J74sVdiUShzNdS1zCRjYfgES7lK8Fydx8JWyeHQZKTKDIEvjK0OPBr/1uExi3Fj/SxwVcRmPLxqINEywLItPIpzKMPtIkWOMxp3oKOB2qAj5WEKj8Gr8dnBn9+W3IaoY4axyjEWe/YVRD6oAzfwjTQN9FJosKO7sBWYtlk4X8cSp8I36OFQjgwXFv9kgyzvUp3/UprhT0XSgyK68LJf7hfYdzQtokixe7nv02Q/QMkVmqPqsChYM6qbWzQefnS8O/yl1rPdcLJ9/BHQtytgrogvWqsPti8=:KgwfUWO/NGwJ1OTWn/NkrGyexbQac5UcJfrRmiVhXKQ=; nlbi_1875454_2147483392=ke9lXLWOgTEo5rNc5D1AxQAAAAAqQpexOIQZhcy9ojkm9KcT; _ga=GA1.2.900535306.1673299863; __hssc=242524765.2.1673591666737; _ga_M82LSVK8P9=GS1.1.1673590994.6.1.1673593271.0.0.0"

headers = {
'user-agent': user_agent,
'referer': 'https://www.aaii.com/sentimentsurvey/sent_results',
'accept-encoding': 'gzip, deflate,br',
'accept-language': 'en-US,en;q=0.9,tr;q=0.8,ru;q=0.7',
"accept":"*/*",
"cookie": cookie2,
"scheme":"https",
"sec-ch-ua": '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
"sec-ch-ua-mobile":"?0",
"sec-ch-ua-platform": "macOS",
"sec-fetch-dest": "script",
"sec-fetch-mode": "no-cors",
"sec-fetch-site": "same-origin"
}


aaii = "https://www.aaii.com/files/surveys/sentiment.xls"
response = requests.get(aaii, headers=headers)
print(response.content)
dataframe = pd.read_excel(io.BytesIO(response.content))