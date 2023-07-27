<br>

**Later**: A re-design of a few parts &rarr; inheritance & `super()`

<br>

## Development Notes

<br>

Locally, create a python environment via [`venv`](https://docs.python.org/3/library/venv.html)

```shell
  python -m venv env
```

and delete via command `rm -r env`.  Environment activation is via

```shell
  env\Scripts\activate.bat
```

within a Windows operating system; deactivation via the command `deactivate`.  List the environment's packages via

```shell
  pip list
```

Always remember to upgrade pip before populating the environment

```shell
  python -m pip install --upgrade pip
```

<br>
<br>

### Packages

```shell
  pip install tensorflow-directml-plugin
  pip install "dask[complete]"
  pip install -U scikit-learn
  pip install pytest coverage pylint pytest-cov flake8
```

Thus far ...

```shell
  pip freeze -f docs/filter.txt > requirements.txt
```

additionally, in aid of code analysis

```shell
  pylint --generate-rcfile > .pylintrc
```

<br>
<br>

### Code Analysis & Standards

`pylint` code analysis:

```shell
  python -m pylint --rcfile .pylintrc ...
```

<br>
<br>

### Snippets

Excluding `tensorflow-directml-plugin==0.4.0.dev230202` whilst trying ...

<br>
<br>

### References

* [Python Package Index](https://pypi.org)
* [pip](https://pip.pypa.io/en/stable/)


<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>
