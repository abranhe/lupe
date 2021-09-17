# WIP

> Currently in development.

<p align="center">
  	<a href="https://pypi.org/project/lupe">
			<img src="https://cdn.abranhe.com/projects/lupe/top.png">
		</a>
</p>

<p align="center">
	Save time building command-line apps with <b><a href="https://pypi.org/project/lupe">LUPE</a></b>
</p>

<p align="center">
	<a href="https://github.com/abranhe/lupe/actions/workflows/main.yml">
		<img src="https://github.com/abranhe/lupe/actions/workflows/main.yml/badge.svg" />
	</a>
	<a href="https://app.travis-ci.com/github/abranhe/lupe">
		<img src="https://img.shields.io/travis/com/abranhe/lupe.svg?logo=travis" />
	</a>
	<a href="https://pypi.org/project/lupe">
		<img src="https://img.shields.io/pypi/v/lupe">
	</a>
	<a href="https://github.com/abranhe/lupe/blob/master/license">
		<img src="https://img.shields.io/github/license/abranhe/lupe.svg" />
	</a>
</p>

## Install

```console
$ pip install lupe
```

## Features

- Parses arguments
- Converts flags snake_case for easier use
- Negates flags when using the `--no-` prefix
- Outputs version when `-v`, `--version`
- Outputs description and supplied help text when `-h`, `--help`

## Usage

On the command line:

```console
$ python main.py dinner --mango --no-banana
```

On the app:

```python
#!/usr/bin/python
import lupe

help = """
Usage foo [input]

Options
  -h, --help      Show this help message and exit
  -v, --version   Show version and exit
  -m, --mango    Include a mango

Examples

  $ main.py dinner --mango --no-banana
"""

cli = lupe(help, {
    'flags': {
        'mango': {
            'type': 'boolen',
            'alias': 'm'
        },
        'banana': {
            'type': 'boolen',
        }
    }
})

print(cli.flags)
# {'mango': True, 'banana': False}

print(cli.inputs)
# [dinner]
```

## API

### lupe(help_message, options?)

### lupe(options)

Returns an `object` with:

- `inputs` _(Array)_ - Non-flag arguments
- `flags` _(Object)_ - Flags converted to snake_case excluding aliases
- `help` _(string)_ - The help text used with `--help`
- `show_help([exit_code=2])` _(Function)_ - Show the help text and exit with `exit_code`
- `show_version()` _(Function)_ - Show the version text and exit

#### help_message

Type: `string`

#### options

Type: `object`

Shortcut for the `help` option.

##### version

Type: `string`

Version of the command-line application.

##### flags

Type: `object`

Define argument flags.

The key is the flag name in snake_case and the value is an object with any of:

- `type`: Type of value. (Possible values: `string` `boolean` `number`)
- `alias`: Usually used to define a short flag alias.
- `default`: Default value when the flag is not specified.
- `required`: Determine if the flag is required. (Default: false)

Note that flags are always defined using a snake_case key (`my_key`), but will match arguments in kebab-case (`--my-key`).

Example:

```python
flags = {
	'unicorn': {
		'type': 'string',
		'alias': 'u',
		'default': ['rainbow', 'cat'],
		'required': True,
	}
}
```

## Credit

Based on [meow](https://github.com/sindresorhus/meow) from [@sindresorhus](https://github.com/sindresorhus)

## License

MIT © [Abraham Hernandez](https://github.com/abranhe)

<p align="center">
  	<a href="https://pypi.org/project/lupe">
			<img src="https://cdn.abranhe.com/projects/lupe/logo.svg" width="30">
		</a>
</p>
