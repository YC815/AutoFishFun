#!/bin/bash
source "/Users/$(whoami)/.dotfiles/fish/.config/fish/config.fish"
script_dir=$(dirname "$0")
rm -rf "$script_dir"
