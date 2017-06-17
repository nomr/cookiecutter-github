# cookiecutter-github
[![Travis](https://img.shields.io/travis/nomr/cookiecutter-github.svg?style=flat-square)](https://travis-ci.org/nomr/cookiecutter-github)

A cookiecutter for github based projects

## Versioning
This project adheres to [Semantic Versioning](http://semver.org/).

## Installation
Install or update your `cookiecutter` environment:
```bash
conda env create nomr/ck || conda env update nomr/ck
```

## Usage
Generate a new Cookiecutter template layout:
```bash
cookiecutter gh:nomr/cookiecutter-github
```

## Contributing
We follow github flow.

### Continuous Testing
```bash
pytest --looponfail
```

## License
This project is licensed under the terms of the [MIT License](/LICENSE)
