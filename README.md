<p align="center">
  	<a href="https://pypi.org/project/lupe"><img src="https://cdn.abraham.gq/projects/lupe/top.png"></a>
</p>

<p align="center">
	When it comes to build command-line apps, there is nothing like <i><a href="https://pypi.org/project/lupe">LUPE</a></i>
</p>

<p align="center">
	<a href="https://cash.me/$19cah"><img src="https://19cah.com/badge.svg"></a>
	<a href="https://cash.me/$19cah"><img src="https://cdn.abraham.gq/badges/cash-me.svg"></a>
	<a href="https://www.patreon.com/19cah"><img src="https://cdn.abraham.gq/badges/patreon.svg" /></a>
	<a href="https://github.com/19cah/lupe/blob/master/LICENSE"><img src="https://img.shields.io/github/license/19cah/lupe.svg" /></a>
  <a href="https://travis-ci.org/19cah/lupe"><img src="https://img.shields.io/travis/19cah/lupe.svg?logo=travis" /></a>
</p>



# Install

```
$ pip install lupe
```

## Features

- Parses arguments
- Outputs version when `--version` or `-v`
- Outputs description and supplied help text when `--help` or `-h`

## Usage

> There is not mango emoji yet supported. So instead, I used  a pear, but it kinda looks the same 😒
```
$ ./foo.py dinner --mango
```

```py
#!/usr/bin/python
# -*- coding: UTF-8 -*-

from lupe import *
from foo import *

cli = lupe(`
	Usage
	  $ foo <input>

	Options
	  --mango, -m  Include a mango

	Examples
	  $ foo dinner --mango
	  	dinner 🍐
`, {
	flags: {
		mango: {
			type: 'boolean',
			alias: 'm'
		}
	}
});
/*
{
	input: ['dinner'],
	flags: {mango: true},
	...
}
*/

foo(cli.input[0], cli.flags);
```

# Credit

Based on [meow](https://github.com/sindresorhus/meow) from [@Sindresorhus](https://github.com/sindresorhus)

# Team

|[![Carlos Abraham Logo](https://avatars3.githubusercontent.com/u/21347264?s=50&v=4)](https://19cah.com)|
| :-: |
| [Carlos Abraham](https://github.com/19cah) |


# License

[MIT](https://github.com/19cah/lupe/blob/master/LICENSE) License © [Carlos Abraham](https://github.com/19cah)

<p align="center">
  	<a href="https://pypi.org/project/lupe"><img src="https://cdn.abraham.gq/projects/lupe/logo.svg" width="30"></a>
</p>
