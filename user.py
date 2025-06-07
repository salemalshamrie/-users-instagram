# -users-instagram
import os, requests, time, random
print ('تم فك من درناوي')
# = = = = = = = = = = = =

Z = '\033[1;31m'  # احمر
X = '\033[1;33m'  # اصفر
Z1 = '\033[2;31m' # احمر ثاني
F = '\033[2;32m'  # اخضر
A = '\033[2;34m'  # ازرق
C = '\033[2;35m'  # وردي
B = '\033[2;36m'  # سماوي
Y = '\033[1;34m'  # ازرق فاتح
W = '\033[0m'     # لون عادي (reset)

def print_logo():
    logo = f"""
{C}   ____        _   _
  |  _ \\ _   _| |_| |__   ___  _ __
  | |_) | | | | __| '_ \\ / _ \\| '_ \\
  |  __/| |_| | |_| | | | (_) | | | |
  |_|    \\__, |\\__|_| |_|\\___/|_| |_|
         |___/

       [:: Python BOT ::]
{F}© 2025  - All rights reserved{W}
"""
    print(logo)

# عرض اللوجو في بداية السكربت
print_logo()

ID = input(A + "𝙴𝙽𝚃𝙰𝚁 𝙸𝙳 ➪  " + C)
print(C + "=‌=‌=‌=‌=‌=‌=‌=‌=‌=‌=‌=‌=‌=‌=‌=‌=‌=‌=‌=‌=‌=‌=‌=‌=")
tok = input(B + "𝙴𝙽𝚃𝙰𝚁 𝚃𝙾𝙺𝙴𝙽 ➪  " + C)
print(C + "=‌=‌=‌=‌=‌=‌=‌=‌=‌=‌=‌=‌=‌=‌=‌=‌=‌=‌=‌=‌=‌=‌=‌=‌=")

abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_1234567890'
abc1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

while True:
    v1 = ''.join(random.choice(abc1) for _ in range(1))
    v2 = ''.join(random.choice(abc) for _ in range(1))
    v3 = ''.join(random.choice(abc) for _ in range(1))
    user1 = v1 + v2 + v3 + '_bot'
    user2 = v1 + v2 + v3 + 'bot'
    user3 = v1 + v1 + v2 + v2 + 'bot'
    user4 = v1 + v2 + v2 + v1 + 'bot'
    hamo010 = (user1, user2, user3, user4)
    user = random.choice(hamo010)
    url = requests.get(f'https://t.me/{user}').text
    if 'tgme_username_link' in url:
        requests.get(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=ʜɪ مبروك زعيم جابلك يوزر\n=‌=‌=‌=‌=‌=‌ =‌=‌=‌=‌=‌=‌=‌=‌\n𝑈𝑆𝐸𝑅 ➪ @{user}\n=‌=‌=‌=‌=‌=‌=‌=‌=‌=‌=‌=‌=‌=‌\n𝐁𝐘 ➪ @x3_B6\n© 2025  - All rights reserved")
        print(F + 'DonE UseR : ' + user)
    else:
        print(Z + 'ErrOR UseR : ' + user)

