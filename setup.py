from setuptools import find_packages, setup

setup(name='calculadora',
      version='0.21.1',
      packages=find_packages(include=('src', 'src.*')),
      include_package_data=True,
      install_requires=[
          'papermill~=2.3.3', 'pygit2~=1.10.1', 'pandas==1.5.1',
          'python-json-logger~=2.0.2', 'libcst~=0.4.5', 'pyxlsb~=1.0.9',
          'unidecode~=1.3.4', 'ipywidgets~=8.0.2', 'IPython~=8.4.0',
          'ddtrace~=1.1.4', 'dtale==2.6.0', 'requests~=2.28.0', 'flask~=2.1.2',
          'pyjwt~=2.5.0', 'webargs~=8.1.0', 'psycopg2-binary~=2.9.3',
          'SQLAlchemy~=1.4.37', 'pyarrow~=8.0.0', 'faker~=13.1.0',
          'werkzeug~=2.1.2', 'apispec~=5.2.2', 'marshmallow~=3.16.0',
          'webargs~=8.1.0', 'urllib3~=1.26.9', 'xarray==2022.3.0',
          'kubernetes~=24.2.0', 'pymongo[srv]~=4.2.0', 'flask-cors~=3.0.10'
      ],
      extras_require={
          'dev': [
              'pytest~=7.0.1', 'pytest-cov~=3.0.0', 'mypy~=0.961',
              'yapf~=0.32.0', 'isort~=5.10.1', 'pylint~=2.13.3',
              'pandas-stubs~=1.2.0.49', 'sqlalchemy[mypy]',
              'types-pytz~=2021.3.6', 'types-urllib3~=1.26.15',
              'types-Flask~=1.1.6', 'types-requests~=2.27.30',
              'mongomock~=4.1.2', 'types-Flask-Cors~=3.0.8'
          ]
      })
