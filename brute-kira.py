import zipfile
import requests
import sys

# Código da parte 1
url = sys.argv[1]
wordlist = sys.argv[2]
ext = sys.argv[3]

def write(word):
    with open("write1.txt", "a") as f1:
        f1.write(word + "\n")

with open(wordlist, "r", encoding="utf-8") as fo:
    for i in range(2000):
        word = fo.readline(10).strip()
        surl = url + word + ext
        response = requests.get(surl)
        
        if response.status_code == 200:
            print("[+] found :-", surl)
            write(word)
        else:
            print("[-] Not found :-", surl)


# Código da parte 2
try:
    filezip = "file.zip"
    wordlist = "wordlist.txt"
    
    with open(wordlist, "rb") as wordlist_file:
        for entry in wordlist_file.readlines():
            password = entry.strip()
            
            try:
                with zipfile.ZipFile(filezip, "r") as zf:
                    zf.extractall(pwd=password)
                    data = zf.namelist()[0]
                    size = zf.getinfo(data).file_size
                    print("[SUCCESS] Password >", password.decode("utf-8"))
                    break
            except:
                pass
                
    print("[FAILED] Password >", password.decode("utf-8"))
except FileNotFoundError:
    print("Zip File or wordlist not found!")
    