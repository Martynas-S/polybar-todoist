# Polybar module for Todoist

A [Polybar](https://github.com/jaagr/polybar) module to show uncompleted todoist
tasks for today or for the week.

![preview](https://github.com/Martynas-S/polybar-todoist/raw/master/preview.png)

## Dependencies

```sh
pip install --user todoist-python==7.0.18
```

Tested and **works** with `todoist-python` version **7.0.18**  
Tested and **doesn't work** with `todoist-python` version **8.0.0**

## Installation

```sh
cd ~/.config/polybar
git clone https://github.com/Martynas-S/polybar-todoist
mv polybar-todoist todoist
```

and obtain the API token

```sh
python ~/.config/polybar/todoist/auth.py
```

## Polybar module

```ini
[module/todo]
type = custom/script
exec = ~/.config/polybar/todoist/todo.py
tail = true
click-left = xdg-open https://todoist.com/app
```

## Acknowledgements

The idea I got from [polybar-gmail](https://github.com/vyachkonovalov/polybar-gmail)
as well as the composition for the readme file.
