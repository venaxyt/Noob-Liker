import requests, gratient, fade
from os import system

system("cls && title ππππΌπ ππππ½ πππππ / ππππππ½ : @venaxyt ")
banner = """
      β   βββββ βββββ βββ      β    ββ β  ββ βββββ   βββββ
       β  β   β β   β β  β     β    ββ βββ   ββ   β  β  ββ
   ββ  ββ β   β β   β β β β    β    ββ βββ   ββββ    ββββ
   β β  β βββββ βββββ β  ββ    ββββ ββ β  β  ββ   ββ β  β
   β  β β  v e n a x  ββββ           β   β   βββββ  β  ββ
   β   ββ                               β             
"""

def purple(text):
    system(""); faded = ""
    red = 35
    for character in text:
        red += 3
        if red > 255:
            red = 255
        faded += (f"\033[38;2;{red};0;220m{character}\033[0m")
    return faded

print(fade.purpleblue(banner))

video = input(purple("  [>] Enter the video ID : ") + "\033[38;2;60;0;230m"); print("")

def getdata(token, video):
    data = {
        "hash": token,
        "id": video,
        "type": "like",
        }
    return data

def getheaders(cookie):
    headers = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "cookie": cookie,
        }
    return headers

file = open("accounts.txt", "r", encoding="utf-8").read()
for line in file.splitlines():
    account = line.split("$!")
    token = account[0]
    cookie = account[1]
    like = requests.post("https://noobhacktube.com/aj/like-system/like", data=getdata(token, video), headers=getheaders(cookie))
    if like.text == '{"status":200,"type":"added_like"}':
        print(gratient.blue(f"  [>] Successfully liked the video ({video})"), end = "")
    elif like.text == '{"status":200,"type":"deleted_like"}':
        print(gratient.blue(f"  [>] Successfully deleted like on video ({video})"), end = "")
    else:
        print(gratient.red("  [>] An error occurred (account is probably invalid)"), end = "")
print("\n" + purple("  [>] All valid accounts liked / unliked the video"))
system("pause >nul")
