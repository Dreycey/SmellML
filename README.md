# SmellML
SmellML is a tool that combines different code smelling tools for python into a nice, compact, push button tool. 


## Dependencies

```
pip install bandit
pip install pylint
pip install radon
```

## Usage

```
 pylint faceswap/tools/
flake8 faceswap/ --ignore=E501
bandit -r pysmell/
radon cc pysmell/ -a -nc
```

## Manuals

* Bandit (security)
    * https://pypi.org/project/bandit/
* Pylint (structural / syntax)
    * https://pypi.org/project/pylint/
* flake8
    * https://pypi.org/project/flake8/
* Radon
    * https://pypi.org/project/radon/
