import sys, os

try:
    import requests
    from fake_useragent import UserAgent
except:
    os.system('pip install requests')
    os.system('pip install fake_useragent')

try:
    import sys, os, requests
    from time import sleep
    from fake_useragent import UserAgent
    ua = UserAgent()
    #===============================================================
    print('''\n*******************************************************************************\n
>>> Chú ý: Mỗi 1 phút sẽ buff được 1 View, vì nếu quá nhanh sẽ làm tăng tỷ lệ thoát 
    trang, ảnh hưởng nghiêm trọng đến SEO, vậy nên nếu muốn nhanh các bạn nên chạy 
    một lúc nhiều tab để mang lại hiệu quả cao nhất có thể nhé!
    ''')
    #===============================================================
    print(">>> Lưu ý nhỏ: Mỗi link cách nhau một khoảng trống nhé\n")
    links = input(">>> Nhập những link bài viết muốn tăng Views: ")
    links = " ".join(links.split())
    links = links.split()
    print("\n")
    #===============================================================
    def buff_view(url, ua):
        uas = ua.chrome
        header = {'User-Agent':str(uas)}
        requests.get(str(url), headers = header)
        sleep(60)
    #===============================================================
    while True:
        for url in links:
            buff_view(url, ua)

except KeyboardInterrupt:
    pass
