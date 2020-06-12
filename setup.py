from distutils.core import setup
setup(
  name='swiss-snow',
  packages=['swiss-snow'],
  version='0.1',
  license='Apache License, Version 2.0',
  description='A Python module for accessing swiss snow conditions and resort status.',
  author='Seb',
  author_email='seb@seb.com',
  url='https://github.com/sebitr/swiss-snow',
  download_url='https://github.com/sebitr/swiss-snow/archive/v_01.tar.gz',
  keywords=['swiss', 'snow', 'ski', 'snowboard', 'avalanche'],
  install_requires=[
        'requests >= 2.23.0',
        'beautifulsoup4>=4.9.1',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
