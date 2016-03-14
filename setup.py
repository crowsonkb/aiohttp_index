from pathlib import Path

import setuptools

here = Path(__file__).parent

setuptools.setup(
    name='aiohttp-index',
    version='0.1.dev0',
    description='aiohttp.web middleware to serve index files (e.g. index.html) when static directories are requested.',
    long_description=(here / 'README.rst').read_text(),
    url='https://github.com/crowsonkb/aiohttp_index',
    author='Katherine Crowson',
    author_email='crowsonkb@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='asyncio aiohttp',
    packages=['aiohttp_index'],
    install_requires=['aiohttp>=0.21.4'],
)
