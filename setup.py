from codecs import open as codecs_open
from setuptools import setup, find_packages


# Get the long description from the relevant file
with codecs_open('README.rst', encoding='utf-8') as f:
    long_description = f.read()


setup(name='rio-metasay',
      version='1.0.0',
      description=u"Skeleton of a Python package",
      long_description=long_description,
      classifiers=[],
      keywords='',
      author=u"Sean Gillies",
      author_email='sean.gillies@gmail.com',
      url='https://github.com/sgillies/rio-plugin-example',
      license='BSD',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'click',
          'cowpy',
          'rasterio>=0.23'
      ],
      extras_require={
          'test': ['pytest'],
      },
      entry_points="""
      [rasterio.rio_commands]
      metasay=metasay.scripts.cli:cli
      """      )