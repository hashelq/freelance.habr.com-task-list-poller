# Description
A simple script that notifies you when a new task appears at freelance.habr.com

# Installation
`pip install -r`

# Usage
`python main.py` for all categories
`python main.py development_bots` for 'development' category
`python main.py development_all_inclusive development_backend` for development backend category

You can specify as much deps as you want, to get the names, go to https://freelance.habr.com/tasks, specify your query using filters on the right side and take a look at the page url, categories paramater will give you the proper category names splited by comma.
For example `https://freelance.habr.com/tasks?categories=development_all_inclusive,development_backend` equals to `development_all_inclusive` and `development_backend` categories

# License
```
            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
                    Version 2, December 2004

 Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>

 Everyone is permitted to copy and distribute verbatim or modified
 copies of this license document, and changing it is allowed as long
 as the name is changed.

            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

  0. You just DO WHAT THE FUCK YOU WANT TO.

```
