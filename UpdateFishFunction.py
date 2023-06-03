import requests
import subprocess
import os

script_path = os.path.abspath(__file__)
script_dir = script_path.rsplit("/", 1)[0]

# 下载function.text文件 #
url = 'https://github.com/YC815/MyFishFunction/raw/main/function.text'
filename = 'function.text'

response = requests.get(url)
response.raise_for_status()

with open(filename, 'wb') as file:
    file.write(response.content)

# 更新function文件 #
function_file = 'function.text'
username = os.getlogin()
config_file = f'/Users/{username}/.dotfiles/fish/.config/fish/config.fish'

with open(function_file, 'r') as f:
    function_text = f.read()

with open(config_file, 'r') as f:
    lines = f.readlines()

index = None
for i, line in enumerate(lines):
    if line.strip() == '# yushun\'s function':
        index = i
        break

if index is not None:
    lines = lines[:index]  # 删除 # yushun's funstion 及之后的代码

lines.append('\n')  # 添加换行
lines.append(function_text)  # 添加函数文本

with open(config_file, 'w') as f:
    f.writelines(lines)

username = os.getlogin()
subprocess.call(['sh', f'{script_dir}/ok.sh'])
