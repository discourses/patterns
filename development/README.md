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

### Packages

```shell
  pip install tensorflow-directml-plugin
  pip install "dask[complete]"
```

Thus far ...

```shell
  pip freeze -f docs/filter.txt > requirements.txt
```

<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>
