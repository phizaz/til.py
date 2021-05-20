from distutils.core import setup

# setup script
setup(
    name='til.py',
    install_requires=[
        'dateparser',
    ],
    scripts=['til/til.py'],
    packages=['til'],
    version='0.1',
)
