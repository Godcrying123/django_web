from setuptools import setup, find_packages

setup(
    name='myidea',
    version='0.1',
    description='Blog System Based on Django',
    author='jackson',
    author_email='jackson@test.com',
    url='https://127.0.0.1:8000',
    license='MIT',
    packages=find_packages('.'),
    # package_dir={'': 'myidea'},
    # include_package_data=True,
    install_requires=[
        'django~=2.2.3',
        'pillow~=6.1.0',
        'django-ckeditor~=5.7.1',
        'django-redis~=4.10.0',
        'mysqlclient~=1.4.2',
        'mistune~=0.8.4',
        'xadmin~=2.0.1',
        'django-autocomplete-light~=3.3.5',
        'djangorestframework~=3.9.4',
    ],
    extras_require={
        'ipython': ['ipython==6.2.1']
    },
    scripts=[
        'manage.py',
    ],
    entry_points={
      'console_scripts': [
          'myidea_mange=manage:main',
      ]
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
    ],
)
