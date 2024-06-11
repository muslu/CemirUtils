python -m pip install -U pip setuptools twine


python setup.py sdist bdist_wheel

#python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*

python -m twine upload dist/*


python -m pip install -U cemirutils


pypi-AgEIcHlwaS5vcmcCJDNkNzQ5NGEzLThmNzctNDJhZC05ZTI2LTk5NTlhNDBiMDgwYgACElsxLFsiY2VtaXJ1dGlscyJdXQACLFsyLFsiNWE1MTg1MDAtMTVmOS00MDZlLTlkNTEtYTJkZGI5NjljMDk5Il1dAAAGIBZ-_ha2PA1UcYQRXFdFwUpjMl8RG5nwcViwuNJOEzLQ