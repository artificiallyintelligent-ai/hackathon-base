from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(
    name='hackathon',
    version='0.0.0',
    description='This is a general hackathon wrapper.',
    url='https://github.com/artificiallyintelligent-ai/hackathon-base.git',

    long_description=long_description,
    long_description_content_type='text/x-rst',

    author='Jason Zeng',
    author_email='jasonzeng124@gmail.com',
    license='MIT License',

    packages=['hackathon'],
    python_requires='>=3.8',

    install_requires=[
        'RestrictedPython',
    ],

    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 1 - Planning',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
