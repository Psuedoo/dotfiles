import json
import os

from libqtile import bar
from libqtile.config import Screen

from .widgets import *

colors = os.path.expanduser("~/.cache/wal/colors.json")
colordict = json.load(open(colors))

ColorZ = colordict["colors"]["color0"]
ColorA = colordict["colors"]["color1"]
ColorB = colordict["colors"]["color2"]
ColorC = colordict["colors"]["color3"]
ColorD = colordict["colors"]["color4"]
ColorE = colordict["colors"]["color5"]
ColorF = colordict["colors"]["color6"]
ColorG = colordict["colors"]["color7"]
ColorH = colordict["colors"]["color8"]
ColorI = colordict["colors"]["color9"]

main_color = ColorF
bg_color = ColorZ
accent_color = ColorA
highlight_color = ColorE
some_other_color = ColorG

font_name = "Ubuntu Mono Bold"


widget_defaults = dict(
    font=font_name,
    fontsize=12,
    padding=3,
    background=bg_color,
    foreground=main_color,
)

extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Spacer(
                    length=15,
                ),
                widget.GroupBox(
                    fontsize=24,
                    borderwidth=3,
                    highlight_method="block",
                    active=accent_color,
                    block_highlight_text_color=main_color,
                    highlight_color=highlight_color,
                    inactive=some_other_color,
                    foreground=highlight_color,
                    this_current_screen_border=bg_color,
                    this_screen_border=bg_color,
                    other_current_screen_border=bg_color,
                    other_screen_border=bg_color,
                    urgent_border=bg_color,
                    # rounded=True,
                    disable_drag=True,
                ),
                widget.Spacer(
                    length=8,
                ),
                widget.Sep(),
                widget.Spacer(
                    length=8,
                ),
                widget.CurrentLayout(
                    foreground=accent_color,
                    fmt="Layout: {}",
                ),
                widget.Spacer(),
                widget.Memory(
                    format="Mem Used: {MemUsed: .0f}{mm}",
                    foreground=accent_color,
                    update_interval=5,
                ),
                widget.Spacer(
                    length=8,
                ),
                # TODO: Add a check to see if this is on a laptop
                widget.Backlight(
                    backlight_name="intel_backlight",
                    brightness_file="/sys/class/backlight/intel_backlight/brightness",
                    max_brightness_file="/sys/class/backlight/intel_backlight/max_brightness",
                ),
                widget.Spacer(
                    length=8,
                ),
                # TODO: Add a check to see if this is on a laptop
                widget.Battery(
                    format=" {percent:2.0%}",
                    foreground=accent_color,
                ),
                widget.Spacer(
                    length=18,
                ),
                widget.Clock(
                    format="%I:%M %p",
                ),
            ],
            30,
            border_color=some_other_color,
            # Uncommenting this will make the bar "float"
            # margin=[15, 60, 6, 30],
        ),
    ),
]
