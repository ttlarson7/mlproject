from setuptools import find_packages, setup
from typing import List


HYPHEN_E_DOT ='-e .'
def get_requirements(file_path:str)->List[str]:
    """
    This function returns the list of packages required for this project
    """
    requirements = []
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
            
    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    author="Taz",
    author_email="tazlarson120@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)