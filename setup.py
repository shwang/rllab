from setuptools import setup, find_packages

setup(
    name='rllab',
    packages=['rllab', 'sandbox'],
    install_requires=[
        'cloudpickle',
        'six~=1.12.0',
        'Flask~=1.1.1',
        'numpy~=1.16.4',
        'scipy~=1.3.0',
        'joblib~=0.13.2',
        'pandas~=0.24.2',
        'matplotlib~=3.1.0',
        'Box2D==2.3.2',
        'PyOpenGL==3.1.0',
        'boto3==1.9.210',
        'botocore==1.12.210',
        'cached_property~=1.5.1',
        'python_dateutil~=2.8.0',
        'rllab@git+https://github.com/shwang/rllab.git'
        'gym==0.14.0',
        'hyperopt==0.1.2',
        'ipdb==0.12.2',
        'lasagne==0.1',
        'Mako~=1.1.0',
        'memory_profiler==0.55.0',
        'nose2~=0.9.1',
        'plotly~=4.1.0',
        'polling==0.3.0',
        'pygame==1.9.6',
        'pyprind==2.11.2',
        'sphinx_rtd_theme==0.4.3',
        'tensorflow~=1.14.0',
        'theano~=1.0.4',
        ],
    version='0.1.0',
)
