from distutils.core import setup
from setuptools import find_packages

setup(
  name = 'solar_panel_rl',
  packages = find_packages(),
  install_requires=['simple_rl', 'numpy', 'matplotlib', 'pytz'],
  version=0.1,
  description = 'Solar panel optimization with Reinforcement Learning in Python.',
  long_description = 'Solar panel optimization with Reinforcement Learning in Python.',
  author = 'Author',
  author_email = 'email@domain.com',
  url = 'https://todo',
  download_url = 'https://todo',
  keywords = ['Solar', 'Panel', 'Reinforcement Learning'],
  classifiers = [],
)