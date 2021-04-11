# SmellML
SmellML is a tool that combines different code smelling tools for python into a nice, compact, push button tool.

![logo for SmellML](figs/logo.png)

# How to use (for a single repository or directory)

* Usage:
```
python SmellML.py <ML code base>
```

* Example:
```
python SmellML.py faceswap/
```
# How to use (for CSV with multiple github links)
* Usage:
```
python SmellML.py <path git csv> --runcsv
```

* Example:
```
python3 SmellML.py  my-software2.0-dataset-20210331.csv  --runcsv
```

* structure of csvfile
It must have a name in the first column and a git link in the second:

```
"Project Name","URL"
"charlesq34/pointnet2","https://github.com/charlesq34/pointnet2.git"
"openai/finetune-transformer-lm","https://github.com/openai/finetune-transformer-lm.git"
```

But having extra information is fine:

```
"Project Name","URL","ML libraries","Number of Contributors","Number of Stars"
"charlesq34/pointnet2","https://github.com/charlesq34/pointnet2.git","sklearn,tensorflow","3","1522"
"openai/finetune-transformer-lm","https://github.com/openai/finetune-transformer-lm.git","sklearn,tensorflow","3","1470"
```

# Extra information on the SmellML project:

### CSV of ML from [ML projects](https://serene-beach-16261.herokuapp.com/)
This helped us automate the testing of SmellML. Special thanks is given to Malinda Dilhara, Ameya Ketkar, and Professor Danny Dig.

### Dependencies

```
pip install bandit
pip install pylint
pip install radon
conda install -c anaconda flake8-polyfill
conda install -c anaconda flake8
```

### Usage Commands for underlying software

```
pylint faceswap/tools/
flake8 faceswap/ --ignore=E501
bandit -r pysmell/
radon cc pysmell/ -a -nc
```

### Manuals for underlying tools

* Bandit (security)
    * https://pypi.org/project/bandit/
* Pylint (structural / syntax)
    * https://pypi.org/project/pylint/
* flake8
    * https://pypi.org/project/flake8/
* Radon
    * https://pypi.org/project/radon/
