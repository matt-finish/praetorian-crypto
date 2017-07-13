# praetorian-crypto
This is what I have so far for the praetorian crypto challenges found at https://www.praetorian.com/challenges/crypto

I used postman for all my challenges so far. Make sure to follow the instructions on praetorian's website to get a token in order to play. After you get a token, put than in your headers section in postman. If you have problems using postman, use the code on praetorian's link above that should be able to get you started.

All passwords are in the triple buzzword format, each word starting with a capital and no spaces. Example: "SecretPasswordPizza"

### Challenge 0: 
Freebie! Use the password 'challenge' or 'password'. I can't remember which it was.

### Challenge 1: 
This is a Caesar cipher. All the values (as of now) are shifted 3 units. Go here: https://www.xarg.org/tools/caesar-cipher/ and use 3 as the key. There is your password.

### Challenge 2: 
For this one, you first need to take the base64 data and convert it to an image. You can do that here: http://freeonlinetools24.com/base64-image and make sure to mime for .png. Then right click the image and download it. Now, if you are on a Mac or a linux box, you can run the command in a terminal `xxd /path/to/file/image.png` and scroll to the very bottom. Your triple buzzword should be appended to the png file after the last cluster.

### Challenge 3: 
This one was a little trickier. Do the same thing by taking the base64 and converting it to an image. Download the image. Things that WONT work for this image: using gimp, changing contrast levels, looking at clusters, binwalk, xxd, strings command in linux and several others. What you need to do is convert the original .png file to a file format that supports just the raw pixel data. So convert the image.png file to the .ppm format. You can either use this site or your favorit Unix command: https://convertio.co/png-ppm/ then downlaod the ppm image. Now you need to open the image in a TEXT EDITOR like VIM. So, if you are on a Mac or unix box, open the image like this: `vim /path/to/file/image.ppm` and scroll to the very bottom. You will notice a pattern of letters. Write them all down and you'll notice at some point they will repeat themselves. Try all 3 combinations of the triple buzzword and try switching the order of the letters until you submit the correct password.

### Challenge 4: 
This one I'm still working on. But praetorian will give you a 4 character hash, and you are supposed to find the password from it either by brute forcing it, or by reversing the hashing process. What I have so far is a wordlist (in root directory of repo called wordlist1.txt) and the python script they provide to you (in root directory or repo called hint4.py). I am currently trying to brute force it. The way I acquired the wordlist was by using a GET request on challenge 1 and used a script to get all the possible words that they use in their backend. I have about 500 words, but I could very well be missing some. After you get the wordlist, you will need to create every possible combination with those 500 words using the triple buzzword format. So 500 X 500 X 500 is a lot. 125,000,000 combinations to be exact. (Or more if I didn't get all the words.) After you get the wordlist together, you will need to short circuit the hashing algorithm because currently it takes several seconds to spit out a hash. You need to somehow cause it so the WHILE loop doesn't iterate so many times. Currently the algorithm takes several SECONDS per hash. Considering there are about 30,000,000 seconds in a year, you'd be cracking for 4 years. After you shorten the hashing algorithm, you should be able to crack 1000's and 1000's per second.  After you do that, write a script that will brute force all 125,000,000 combinations against the hash. I don't have a current solution, but I'm working on it and I'll update as I go. Feel free to chime in if you get it working.

Optional Step. (Actually just skip it. Anything in this paragraphy just skip completely. It's only here for documentation). 
I initially used this but added it into the level4_simplified.py program:
The wordlist generator to create the 3 tripple buzzwords can be found in the root directory of the repo. To run it use `python wordlist_generator.py > output_wordlist.txt` and make sure the file `wordlist1.txt` is in the same directory as the wordlist_generator. This will create a file about 3.2 GB large. Now I'm working on a way to shorten the hashing algorithm.

Okay, so i've shortened the hashing algorithm and have uploaded my script in the root directory of the repo. It is called `level4_simplified.py`. Go into the script and change the name of the wordlist and the hash you are trying to achieve. Run it like this `python level4_simplified.py > possible_passwords.txt` because it will spit out tons of possible passwords. I have another script that will run this against the api once the possible_passwords list generates. Give it about an hour to churn out all the possible passwords.

After you have your possible_passwords.txt file, run the crypto_submit.py file (change the name of the possible_passwords.txt file if it's different) and just let it run. After it's finished, try using postman to request level 5 or try to return the hash from level 4 by looking on praetorian's website on how to get the hash. If it doesn't return the hash, you may need to re-request level 4 and get a new hash to crack and try the processess again. I'm very close to submitting the passwords to the api and I will post again soon.

### Challenge 5:

I'll post in a little bit.
