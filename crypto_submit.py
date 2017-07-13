import requests
try: input = raw_input
except NameError: pass

# Global values
base = "http://crypto.praetorian.com/{}"
# Insert the token here
auth_token = {"Authorization":"JWT " + "insert_your_token_here"}

# Fetch the challenge and hint for level n
def fetch(n):
	url = base.format("challenge/{}/".format(n))
	resp = requests.get(url, headers=auth_token)
	resp.close()
	if resp.status_code != 200:
		raise Exception(resp.json()['detail'])
	return resp.json()

# Submit a guess for level n
def solve(n, guess):
	url = base.format("challenge/{}/".format(n))
	data = {"guess": guess}
	resp = requests.post(url, headers=auth_token, data=data)
	resp.close()
	if resp.status_code != 200:
		raise Exception(resp.json()['detail'])
	return resp.json()

# Fetch level 4
level = 4
hashes = {}
data = fetch(level)

# Submit guesses and load the password wordlist.
with open("possible_passwords.txt", "r") as wordlist:

	new_list = []

	for x in wordlist:
		new_list.append(x.strip())

	for y in new_list:
		print y
		guess = y
		h = solve(level, guess)



# If we obtained a hash add it to the dict
if 'hash' in h: hashes[level] = h['hash']
print hashes

# Display all current hash
#for k,v in hashes.items():
#	print("Level {}: {}".format(k, v))
