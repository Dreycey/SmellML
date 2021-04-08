# SmellML
SmellML is a tool that combines different code smelling tools for python into a nice, compact, push button tool.

![logo for SmellML](figs/logo.png)

# How to use

* Usage:
```
python SmellML.py <ML code base>
```

* Example:
```
python SmellML.py faceswap/
```


## Dependencies

```
pip install bandit
pip install pylint
pip install radon
conda install -c anaconda flake8-polyfill
conda install -c anaconda flake8
```

## Usage Commands

```
pylint faceswap/tools/
flake8 faceswap/ --ignore=E501
bandit -r pysmell/
radon cc pysmell/ -a -nc
```

## CSV of ML from [ML projects](https://serene-beach-16261.herokuapp.com/)
This helped us automate the testing of SmellML. Special thanks is given to Malinda Dilhara, Ameya Ketkar, and Professor Danny Dig.

## Manuals

* Bandit (security)
    * https://pypi.org/project/bandit/
* Pylint (structural / syntax)
    * https://pypi.org/project/pylint/
* flake8
    * https://pypi.org/project/flake8/
* Radon
    * https://pypi.org/project/radon/
