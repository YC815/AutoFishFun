import requests
import subprocess
import os

# 下載function.text檔案 #
url = 'https://github.com/YC815/MyFishFunction/raw/main/function.text'
filename = 'function.text'

response = requests.get(url)
response.raise_for_status()

with open(filename, 'wb') as file:
    file.write(response.content)

# 寫入內容 #
function_file = 'function.text'
username = os.getlogin()
config_file = f'/Users/{username}/.dotfiles/fish/.config/fish/config.fish'

with open(function_file, 'r') as f:
    function_text = f.read()
with open(config_file, 'a') as f:
    f.write('\n' + function_text)

subprocess.call(['sh', 'autofishfun/ok.sh'])
