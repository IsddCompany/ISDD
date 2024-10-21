from setuptools import setup, find_packages


setup(name='ISDD',
      version='0.0.0.1',
      url='https://github.com/IsddCompany/ISDD',
      author='Jjoon0513',
      author_email='isddcompany@gmail.com',
      description='ISDD package',
      long_description=open('README.md').read(),
      long_description_content_type='text/markdown',
      install_requires=['cython'],
      packages=find_packages(exclude=[]),
      keywords=['ISDO', 'ISDD'],
      python_requests='>3.6',
      zip_safe=False,
      classifiers=[
          'License :: OSI Approved :: MIT License'
      ]
)
