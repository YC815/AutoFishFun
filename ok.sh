#!/bin/bash

# 获取当前脚本文件所在的目录路径
script_dir=$(dirname "$0")

# 提示确认操作
read -p "确认要删除目录 $script_dir 及其内容吗？(y/n) " confirm
if [[ $confirm == [yY] || $confirm == [yY][eE][sS] ]]; then
    # 删除包含脚本文件的目录
    rm -rf "$script_dir"
else
    echo "已取消删除操作"
fi
