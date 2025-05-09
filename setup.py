from setuptools import setup, find_packages
from typing import List

def read_requirements(file_path:str) -> List[str]:
    """Reads the requirements from a file and returns a list of packages."""
    requirements=[]
    HYPHEN_E_DOT='-e .'
    with open(file_path, 'r') as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='mradul',
    author_email='mmradul38@gmail.com',
    packages=find_packages(),
    install_requires=read_requirements('requirements.txt'),
)