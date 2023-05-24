# Name: url_all_shortener.py
# Description: URL 리다이렉트 경로를 표시, 출력해주는 프로그램입니다.

import requests

url_file = open('urllist.txt', 'r') # URL 주소 모음 파일의 이름을 입력해주세요
output = open('output.txt', 'w')

def print_redirected_urls(url: str, cnt: int):
	try:
		while True:
			print(url)
			output.write(f"[{cnt}] : {url}\n")
			cnt += 1

			response = requests.get(url, allow_redirects=False, timeout = 2)	# Connection timed out 에러 예방
		
			if response.status_code >= 300 and response.status_code < 400:
				string = response.headers['Location']
				if string[0] == '/':
					url += response.headers['Location']
				else:
					url = response.headers['Location']
			else:
				break

	except:
		return

url = url_file.readline()[:-1]

while url:
	# print(url)
	output.write(f"Original URL: {url}\n\n")
	print_redirected_urls(url, 1)
	
	output.write("\n----------------------------------\n\n")

	url = url_file.readline()[:-1]

url_file.close()
output.close()
