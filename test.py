
import csv

data = [
    {"year": "2020", "month": "11", "metro": "부산광역시", "city": "연제구", "houseCnt": 101583, "powerUsage": 233.96, "bill": 24292},
    {"year": "2020", "month": "11", "metro": "부산광역시", "city": "기장군", "houseCnt": 53778, "powerUsage": 198.89, "bill": 20850},
    {"year": "2020", "month": "11", "metro": "부산광역시", "city": "남구", "houseCnt": 137380, "powerUsage": 225.08, "bill": 23614},
    {"year": "2020", "month": "11", "metro": "부산광역시", "city": "수영구", "houseCnt": 97026, "powerUsage": 210.43, "bill": 21719},
    {"year": "2020", "month": "11", "metro": "부산광역시", "city": "서구", "houseCnt": 62200, "powerUsage": 192.00, "bill": 19457},
    {"year": "2020", "month": "11", "metro": "부산광역시", "city": "동구", "houseCnt": 54279, "powerUsage": 180.75, "bill": 18004},
    {"year": "2020", "month": "11", "metro": "부산광역시", "city": "동래구", "houseCnt": 126812, "powerUsage": 233.55, "bill": 24641},
    {"year": "2020", "month": "11", "metro": "부산광역시", "city": "북구", "houseCnt": 132113, "powerUsage": 235.42, "bill": 23549},
    {"year": "2020", "month": "11", "metro": "부산광역시", "city": "해운대구", "houseCnt": 191284, "powerUsage": 251.75, "bill": 27253},
    {"year": "2020", "month": "11", "metro": "부산광역시", "city": "영도구", "houseCnt": 63056, "powerUsage": 192.53, "bill": 18711},
    {"year": "2020", "month": "11", "metro": "부산광역시", "city": "부산진구", "houseCnt": 197129, "powerUsage": 209.80, "bill": 20832},
    {"year": "2020", "month": "11", "metro": "부산광역시", "city": "사하구", "houseCnt": 157980, "powerUsage": 213.40, "bill": 21058},
    {"year": "2020", "month": "11", "metro": "부산광역시", "city": "금정구", "houseCnt": 128893, "powerUsage": 205.34, "bill": 21292},
    {"year": "2020", "month": "11", "metro": "부산광역시", "city": "강서구", "houseCnt": 66613, "powerUsage": 240.14, "bill": 25956},
    {"year": "2020", "month": "11", "metro": "부산광역시", "city": "중구", "houseCnt": 31589, "powerUsage": 144.91, "bill": 13885},
    {"year": "2020", "month": "11", "metro": "부산광역시", "city": "사상구", "houseCnt": 107033, "powerUsage": 214.02, "bill": 20816}
]

# CSV 파일로 저장
with open('power_usage.csv', mode='w', newline='', encoding='EUC-KR') as file:
    writer = csv.DictWriter(file, fieldnames=["year", "month", "metro", "city", "houseCnt", "powerUsage", "bill"])
    
    # 헤더 작성
    writer.writeheader()
    
    # 데이터 작성
    writer.writerows(data)

print("CSV 파일이 'power_usage.csv'로 저장되었습니다.")
