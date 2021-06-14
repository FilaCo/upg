from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='upg',

    version='0.1.0',

    description='TBD',
    long_description=long_description,
    long_description_content_type='text/markdown',

    url='https://github.com/FilaCo/upg',

    author='FilaCo',
    author_email='awesome.chekushka@gmail.com',

    package_dir={'': 'src'},
    packages=find_packages(where='src'),

    python_requires='>=3.6, <4',

    py_modules=['pass_gen', 'ui'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'upg = ui.password_generator_cli:cli',
        ],
    },
)