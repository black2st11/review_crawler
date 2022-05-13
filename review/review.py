'''
특정 사이트에서 상품에 대해 작성한 리뷰가 삭제되는 것을 목격했으나
혹시나 정렬 순서로 인해서 리뷰가 밀려난 것 일수도 있기에 하나하나 확인 중
이렇게 하는 것은 의미가 없다 크롤러를 만들어서 필요한 리뷰만 확인하자라고 해서 시작

동작 방식
1. 해당 사이트에 대한 리뷰 리스트 페이지를 통해서 조회
2. 작성한 리뷰 별점이 ★★★ 이고 해당 리뷰에 대한 별점이 8개인 것을 확인, ★★★로 기준을 잡는 것이 추후 확인이 편하다고 생각하여 결정
3. 리뷰 별점이 ★★★ 인 경우 point index 와 동일한 comment index를 통해서 리뷰 내용 console로 해당 리뷰 메시지 출력 
4. 8개 정도의 리뷰는 손수 비교 가능해서 확인함
5. 없음.....

결과
리뷰 조작이 확실하기는 함
일단 1500 개 정도되는 리뷰에서 3 점 미만인 리뷰가 없는 것도 이상하고, 리뷰 내용이 3점치고 제품에 대해 별말이 없음
유추했을 때 제품이나 서비스에 대해 문제점을 제기했을 때 삭제 처리하는 것으로 판단되어짐
참고로 네이버페이로 주문해 리뷰남겨서 리뷰가 네이버 페이(본인만 보는 것이 가능)에서는 나타나고 해당 사이트에서는 리뷰가 없어짐(원래는 첫 페이지에 있었음)

이러면 굳이 해당 제품에 관련된 리뷰를 남겨야 하는 의문도 있고 리뷰가 조작된 것이 뻔한데 제품에 대한 신뢰성도 의심이감
심지어 선물용도로 산 것이고 이미 선물했는데 해당하는 부분에 있어서 이런 의심이 드니 선물하고도 기분도 안좋음
'''
from selenium import webdriver
from selenium.webdriver.common.by import By 
from bs4 import BeautifulSoup

options = webdriver.EdgeOptions()

driver = webdriver.Edge('./msedgedriver.exe') # 동일한 폴더에 edge 드라이버 사용
cnt = 0
for i in range(1,296):
    driver.get(f'제품 주소 리뷰 인덱스={i}') # 원래는 사이트 주소가 있지만 고소미 먹을까봐 가림
    html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser')
    
    reviews_point = soup.select('body > div > div.star_day_name > strong')
    reviews_comment = soup.select('body > div > div.option_text_file_box > div.text_file_cont > div.review_text.js_pr_contents_short')
    for i in range(len(reviews_point)):
        if reviews_point[i].text.strip() == '★★★':
            cnt +=1

            print(f'{cnt} 번째 리뷰 : {reviews_comment[i].text.strip()}')

driver.quit()