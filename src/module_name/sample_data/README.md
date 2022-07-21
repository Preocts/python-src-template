Files in this directory will be included in the install if they are defined in
the `[tool.setuptools.package-data]` section of the `pyproject.toml`. Path is
relative to the `where` target.

```ini
[tool.setuptools.packages.find]
where = ["src"]  # ["."] by default
include = ["*"]  # ["*"] by default
exclude = ["tests"]  # empty by default
namespaces = true  # true by default

[tool.setuptools.package-data]
"module_name.sample_data" = ["*.csv"]
```
