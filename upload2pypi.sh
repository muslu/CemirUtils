python -m pip install -U pip setuptools twine


python setup.py sdist bdist_wheel

#python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*

python -m twine upload dist/*


python -m pip install -U cemirutils


pypi-AgEIcHlwaS5vcmcCJDIwYWE2ZWYyLTFlNjMtNDZmMC05YTQ2LWQ5ZmIxYzU4YTJlMwACElsxLFsiY2VtaXJ1dGlscyJdXQACLFsyLFsiNWE1MTg1MDAtMTVmOS00MDZlLTlkNTEtYTJkZGI5NjljMDk5Il1dAAAGIGa0XseUTnbbIdTC3aUVKGfiTmpqLAH_ebZuTRP4deOB