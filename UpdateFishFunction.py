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

# 更新function檔 #
function_file = 'function.text'
username = os.getlogin()
config_file = f'/Users/{username}/.dotfiles/fish/.config/fish/config.fish'

with open(function_file, 'r') as f:
    function_text = f.read()

with open(config_file, 'r+') as f:
    lines = f.readlines()
    f.seek(0)
    index = 0
    for i, line in enumerate(lines):
        if line.strip() == '# yushun\'s funstion':
            index = i
            break
    for line in lines[:index]:
        f.write(line)
    f.write(function_text)
    f.truncate()
username = os.getlogin()
subprocess.call(['sh', f'{script_dir}/ok.sh'])

# import requests
# import subprocess
# import os
# script_path = os.path.abspath(__file__)
# script_dir = script_path.rsplit("/", 1)[0]

# # 下載function.text檔案 #
# url = 'https://github.com/YC815/MyFishFunction/raw/main/function.text'
# filename = 'function.text'

# response = requests.get(url)
# response.raise_for_status()

# with open(filename, 'wb') as file:
#     file.write(response.content)

# # 更新function檔 #
# function_file = 'function.text'
# username = os.getlogin()
# config_file = f'/Users/{username}/.dotfiles/fish/.config/fish/config.fish'

# with open(function_file, 'r') as f:
#     function_text = f.read()

# with open(config_file, 'a') as f:
#     lines = f.readlines()
#     f.seek(0)
#     index = 0
#     for i, line in enumerate(lines):
#         if line.strip() == '# yushun\'s funstion':
#             index = i
#             break
#     for line in lines[:index]:
#         f.write(line)
#     f.write(function_text)
#     f.truncate()

