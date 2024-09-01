#!/bin/sh

wallpaper=$(cat ~/.cache/wal/colors.json | jq '.wallpaper' | sed 's/"//g')
feh --bg-scale $wallpaper &

alacritty &
picom --config ~/.config/picom/picom.conf &

