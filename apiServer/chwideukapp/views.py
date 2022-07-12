from time import sleep
from rest_framework.views import APIView
from rest_framework.response import Response
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--single-process")
chrome_options.add_argument("--disable-dev-shm-usage")
path = '/usr/bin/chromedriver'
driver = webdriver.Chrome(path, chrome_options=chrome_options)


class ChwideukRouter(APIView):
    def get(self, request):
        return Response({'success': True})

    def post(self, request):
        driver.get('https://edi.nhis.or.kr/homeapp/wep/m/retrieveMain.xx')

        print("+" * 100)
        print(driver.title)   # 크롤링한 페이지의 title 정보
        print(driver.current_url)  # 현재 크롤링된 페이지의 url
        print("바이크 브랜드 크롤링")
        print("-" * 100)

        sleep(2)

        isPopup = True

        # 팝업창 있으면 닫기
        while isPopup:
            if (len(driver.window_handles) == 1 ):
                isPopup = False
            else:
                driver.switch_to_window(driver.window_handles[1])
                driver.close()
        
        # 메인 페이지로 이동
        driver.switch_to_window(driver.window_handles[0])

        # 브라우저인증서 로그인 클ㄹㄱ
        driver.execute_script('enableAnySignLitr(true)');
        


        title = driver.title
        url = driver.current_url

        # driver.close()
        return Response({'title': title, 'url': url})