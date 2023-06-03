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
config_file = '.dotfiles/fish/.config/fish/config.fish'

# 读取function.text文件内容
with open(function_file, 'r') as f:
    function_text = f.read()

os.chdir('/Users/user')
# 打开config.fish文件并进行内容替换和写入
with open(config_file, 'r+') as f:
    lines = f.readlines()
    f.seek(0)  # 将文件指针移动到文件开头

    # 查找"# yushun's funstion"所在行的索引
    index = 0
    for i, line in enumerate(lines):
        if line.strip() == '# yushun\'s funstion':
            index = i
            break

    # 删除从"# yushun's funstion"行开始的所有内容
    for line in lines[:index]:
        f.write(line)

    # 写入新内容
    f.write(function_text)
    f.truncate()

subprocess.call(['sh', 'ok.sh'])
