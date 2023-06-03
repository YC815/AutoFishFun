#!/bin/bash

# 获取当前脚本文件所在的目录路径
script_dir=$(dirname "$0")

rm -rf "$script_dir"
source "/Users/$(whoami)/.dotfiles/fish/.config/fish/config.fish"