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
config_file = '.dotfiles/fish/.config/fish/config.fish'

with open(function_file, 'r') as f:
    function_text = f.read()
username = os.getlogin()
os.chdir(f'/Users/{username}')
os.chdir(f'/Users/{username}')
with open(config_file, 'a') as f:
    f.write('\n' + function_text)

current_path = os.getcwd()
os.chdir(current_path)
subprocess.call(['sh', 'ok.sh'])
