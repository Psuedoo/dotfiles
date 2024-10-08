import json
import os

from libqtile import bar
from libqtile.config import Screen
from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration

is_laptop = os.path.exists("/sys/class/backlight/intel_backlight/brightness")

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
bar_height = 40

default_font_size = 12
widget_font_size = 24

if is_laptop:
    default_font_size = 22
    widget_font_size = 32

widget_defaults = dict(
    font=font_name,
    fontsize=default_font_size,
    padding=3,
    background=bg_color,
    foreground=main_color,
)

extension_defaults = widget_defaults.copy()


powerline = {
    "decorations": [
        PowerLineDecoration(
            path="forward_slash",
        )
    ]
}


laptop_widgets = [
    widget.Spacer(
        length=18,
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
        length=8,
    ),
]

other_widgets = [
    widget.Spacer(length=15),
    widget.GroupBox(
        fontsize=widget_font_size,
        borderwidth=3,
        highlight_method="line",
        block_highlight_text_color=main_color,
        highlight_color=bg_color,
        active=accent_color,
        inactive=some_other_color,
        foreground=highlight_color,
        this_screen_border=bg_color,
        other_current_screen_border=bg_color,
        other_screen_border=bg_color,
        urgent_border=bg_color,
        disable_drag=True,
        **powerline
    ),
    widget.Spacer(length=8, **powerline),
    widget.CurrentLayout(
        foreground=bg_color, background=main_color, fmt="Layout: {}", **powerline
    ),
    widget.Spacer(foreground=main_color, background=main_color, **powerline),
    # widget.Memory(
    #     format="Mem Used: {MemUsed: .0f}{mm}",
    #     foreground=accent_color,
    #     update_interval=5,
    # ),
    widget.Clock(
        format="%I:%M %p",
    ),
]

display_widgets = other_widgets

if is_laptop:
    display_widgets += laptop_widgets

screens = [
    Screen(
        top=bar.Bar(
            display_widgets,
            bar_height,
            border_color=some_other_color,
            # Uncommenting this will make the bar "float"
            # margin=[15, 60, 6, 30],
        ),
    ),
]
