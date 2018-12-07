from setuptools import setup

setup(
    author='Learning Equality',
    author_email='aron@learningequality.org',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    description='',
    install_requires=['SQLAlchemy>=1.1.10', 'futures>=3.1.1'],
    keywords=('queue', 'async'),
    license='MIT',
    long_description='',
    name='iceqube',
    package_data={},
    package_dir={'': "src"},
    packages=[
        'iceqube',
        'iceqube.common',
        'iceqube.messaging',
        'iceqube.messaging.backends',
        'iceqube.scheduler',
        'iceqube.storage',
        'iceqube.storage.backends',
        'iceqube.worker',
        'iceqube.worker.backends'
    ],
    url='https://github.com/learningequality/iceqube',
    version='0.0.5',
    zip_safe=True
)
