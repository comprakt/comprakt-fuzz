# comprakt-fuzz

A fuzzer for the [MiniJava](https://pp.ipd.kit.edu/lehre/WS201819/compprakt/intern/sprachbericht.pdf) language

## Running the fuzzer

This fuzzer only works with `python2.7`. A virtual environment is recommended.

### Tl;dr

```bash
pip install virutalenv
virtualenv venv -p python2.7
source venv/bin/activate
python setup.py install
python -m comprakt-fuzz
```

### Details

As a first step you can install the fuzzer with `python setup.py install` or
alternatively with `pip install . --process-dependency-links`.

After installing it the fuzzer can be run with

```
python -m comprakt-fuzz
```

with the following options

```
optional arguments:
  -h, --help            show this help message and exit
  -o OUT_DIR, --out OUT_DIR
                        the output directory for the fuzzed files
  -n NUM                number of files that should be produced
  --vim_format          format the output files with vim
  --lexer               fuzz lexer test cases without caring about the syntax
```

Without any arguments 10 files will get generated in the directory `output`.

The fuzzer won't add any indentations, because adding this in the grammar isn't
realistic. To get nicer looking files you can use the autoident function
provided by `vim`. With the additional flag `--vim_format` every generated file
will get indented by `vim`. **Caution**: This will take way longer than just
generating ugly files.

---
## License

Licensed under either of

 * Apache License, Version 2.0, ([LICENSE-APACHE](LICENSE-APACHE) or http://www.apache.org/licenses/LICENSE-2.0)
 * MIT license ([LICENSE-MIT](LICENSE-MIT) or http://opensource.org/licenses/MIT)

at your option.

