from setuptools import find_packages, setup
from typing import List



def get_requirements(file_path:str) -> List[str]:
    '''
    This function will return the list of requirements and read 
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements ]

        if '-e .' in requirements:
            requirements.remove('-e .')

    return requirements

setup(
    name  = "ML Project",
    version= '0.0.1',
    author="Raj",
    author_email="rajasekhar@gmail.com",
    packages=find_packages(),
    install_requires  = get_requirements('requirements.txt')
)