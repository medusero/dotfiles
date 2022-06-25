# SOFTWARE.

import os
import subprocess
from libqtile import hook

from libqtile import qtile
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

from qtile_extras import widget
from qtile_extras.widget.decorations import BorderDecoration

mod = "mod4"
terminal = guess_terminal()


########################
###  BAR VARIABLES   ###
########################

widgets_font = "Ubuntu Mono Nerd Font Bold"
widgets_font_sze = 14
widgets_padding = 4

bar_color = "#11111b"
bar_sze = 20

#Catppuccin Mocha colors
rosewater_color = '#f5e0dc'
flamingo_color = '#f2cdcd'
pink_color = '#f5c2e7'
mauve_color = '#cba6f7'
red_color = '#f38ba8'
maroon_color = '#eba0ac'
peach_color = '#fab387'
yellow_color = '#f9e2af'
green_color = '#a6e3a1'
teal_color = '#94e2d5'
sky_color = '#89dceb'
sapphire_color = '#74c7ec'
blue_color = '#89b4fa'
lavender_color = '#b4befe'
base_color = '#1e1e2e'
fg_color = '#cdd6f4'
bg_color = '#11111b'

###########################
####        KEYS        ###
###########################

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "Left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "Down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod, "control"], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn("alacritty -e fish"), desc="Launch terminal"),
    Key([mod], "b", lazy.spawn("firefox"), desc="Launch Firefox"),
    Key([mod, "shift"], "b", lazy.spawn("firefox --private-window"), desc="Launch Firefox in private mode"),
    Key([mod], "n", lazy.spawn("thunar"), desc="Launch Thunar"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    
    #Launch Rofi  
    Key([mod], "r", lazy.spawn("rofi -show drun"), desc="spawn rofi"),
    Key([mod], "w", lazy.spawn("rofi -show window"), desc="spawn rofi mode windows"),
    Key([mod], "c", lazy.spawn("rofi -modi 'clipboard:greenclip print' -show clipboard"), desc="spawn rofi-greenclip"),

    Key([mod], "x", lazy.spawn("archlinux-logout"), desc="Logout menu"),

    #Volume  Keys
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pulsemixer --change-volume +5 --max-volume 100")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pulsemixer --change-volume -5 --max-volume 100")),
    Key([], "XF86AudioMute", lazy.spawn("pulsemixer --toggle-mute")),

    #Brightness Keys
    Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight + 5")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight - 5")),

]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )
    

layouts = [
    layout.Columns(
        border_focus= blue_color, 
        border_normal= base_color, 
        border_width=3,
        border_on_single=False,
        margin= [7, 7, 7, 7],
    ),

    layout.Max(),
]

widget_defaults = dict(
    font = widgets_font,
    fontsize = widgets_font_sze,
    padding = widgets_padding,
)
extension_defaults = widget_defaults.copy()

decor_battery = {
    "decorations": [
        BorderDecoration(colour=sapphire_color, border_width = [0, 0, 2, 0], padding = 4, padding_y = 0)
    ],
}

decor_memory = {
    "decorations": [
        BorderDecoration(colour=yellow_color, border_width = [0, 0, 2, 0], padding = 4, padding_y = 0)
    ],
}

decor_cpu = {
    "decorations": [
        BorderDecoration(colour=pink_color, border_width = [0, 0, 2, 0], padding = 4, padding_y = 0)
    ],
}

decor_volume = {
    "decorations": [
        BorderDecoration(colour=green_color, border_width = [0, 0, 2, 0], padding = 4, padding_y = 0)
    ],
}

decor_weather = {
    "decorations": [
        BorderDecoration(colour=peach_color, border_width = [0, 0, 2, 0], padding = 4, padding_y = 0)
    ],
}

decor_clock = {
    "decorations": [
        BorderDecoration(colour=mauve_color, border_width = [0, 0, 2, 0], padding = 4, padding_y = 0)
    ],
}

decor_root = {
    "decorations": [
        BorderDecoration(colour=flamingo_color, border_width = [0, 0, 2, 0], padding = 4, padding_y = 0)
    ],
}

decor_home = {
    "decorations": [
        BorderDecoration(colour=lavender_color, border_width = [0, 0, 2, 0], padding = 4, padding_y = 0)
    ],
}

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    font = "Ubuntu Nerd Mono Bold",
                    active = red_color,
                    inactive = sky_color,
                    disable_drag = True,
                    highlight_method = 'line',
                    use_mouse_wheel = True,
                    background = bg_color,
                    this_current_screen_border = red_color,
                    margin_x = 0,
                    margin_y = 5,
                    ),

                widget.Sep(
                    foreground = fg_color
                    ),
                
                widget.CurrentLayout(
                    foreground = lavender_color,
                    ),

                widget.Sep(
                    foreground = fg_color
                    ),
                
                 widget.WindowCount(                    
                    show_zero = True,
                    foreground = lavender_color,
                    fmt='{}',
                    ),

                widget.Sep(
                    foreground = fg_color
                    ),
                
                widget.WindowName(                    
                    foreground = lavender_color,
                    empty_group_string = 'Qtile',
                    ),

                widget.Spacer(
                    bar.STRETCH,
                    background = None,
                    ),
                
                widget.Memory(                   
                    format = '兩{MemUsed: .0f}{mm}',
                    foreground = yellow_color,
                    padding = 4,
                    **decor_memory
                    ),

                widget.CPU(                    
                    format = '礪 {load_percent}%',
                    foreground = pink_color,
                    padding = 4,
                    **decor_cpu
                    ),

                widget.Volume(
                    fmt = '  {}',
                    foreground = sapphire_color,
                    **decor_volume
                    ),

                widget.Battery(
                    format = '{char} {percent:2.0%}',
                    foreground = green_color,
                    low_background = '#ff5555',
                    low_foreground = '#ffffff',
                    low_percentage = 0.3,
                    discharge_char = '',
                    charge_char = '',
                    empty_char = '',
                    full_char = '',
                    unknown_char = '',
                    update_interval = 20,
                    padding = 7,
                    **decor_battery
                    ),

                widget.DF(
                    format = ' {f}{m}',
                    partition = '/',
                    foreground = flamingo_color,
                    visible_on_warn = False,
                    **decor_root
                    ),
                
                widget.DF(
                    format = ' {f}{m}',
                    partition = '/home',
                    foreground = lavender_color,
                    visible_on_warn = False,
                    **decor_home
                    ),
                
                widget.OpenWeather(
                    app_key = '4ff4b1e14f471ad530998571ec6d6dc0',
                    cityid = '3128760',
                    foreground = peach_color,
                    **decor_weather
                    ),

                widget.Clock(
                    format = "  %a %d %b %Y, %H:%H",
                    padding = 4,
                    foreground = mauve_color,
                    **decor_clock
                    ),
            ],

            bar_sze, 
            background = bg_color,
            margin = [7, 7, 0, 7]
         ), 
     ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(title="lxappearance"),
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    subprocess.Popen([home + '/.config/qtile/autostart.sh'])
    
