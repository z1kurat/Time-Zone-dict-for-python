from setuptools import setup, find_packages

def readme():
  with open('README.md', 'r') as f:
    return f.read()

setup(
  name='time_zone_dict',
  version='1.0.0',
  author='z1kurat',
  author_email='novorozhbitov@mail.com',
  description='Time Zone dict',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='not',
  packages=find_packages(),
  install_requires=['requests>=2.25.1'],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='example python',
  project_urls={
    'Documentation': 'link'
  },
  python_requires='>=3.7'
)
