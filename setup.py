import setuptools


def readme():
    with open('README.rst') as f:
        return f.read()

setuptools.setup(
    name='srx_segmenter',
    version='0.0.1',
    packages=['.'],
    description="Segment text with SRX",
    long_descriptiondescription=readme(),
    classifiers=[
        'Topic :: Utilities',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.4',
    ],
    license='GPLv3',
    author='Motoki Naruse',
    author_email='motoki@naru.se',
    url='https://github.com/narusemotoki/srx_segmenter',
    keywords='Translation, Segmentation, SRX',
    zip_safe=False,
    install_requires=[
        'lxml',
        'regex',
        'mypy-lang',
    ],
    extras_require={
        'test': [
            'nose',
            'rednose',
            'coverage',
            'flake8',
        ],
    }
)
