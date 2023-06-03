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

with open(config_file, 'r+') as f:
    lines = f.readlines()
    f.seek(0)
    function_start = None
    for i, line in enumerate(lines):
        if line.strip() == '# yushun\'s funstion':
            function_start = f.tell()
            break

    if function_start is not None:
        f.truncate(function_start)  # 截断文件到函数起始位置
        f.write('\n')  # 添加换行
        f.write(function_text)  # 添加函数文本

username = os.getlogin()
subprocess.call(['sh', f'{script_dir}/ok.sh'])
