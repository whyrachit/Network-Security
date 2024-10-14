from setuptools import find_packages,setup
from typing import List

def get_requirements() -> List[str]:
    #To return the list of requiremets
    requirement_list:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            lines=file.readlines()
            for line in lines:
                req=line.strip()
                # Ignoring the empty lines and -e .
                if req and req!= '-e .':
                    requirement_list.append(req)
    except FileNotFoundError:
        print("requirements.txt filr not found")

    return requirement_list

setup(
    name="Network Security Project",
    version="0.0.1",
    author="Rachit Yadav",
    author_email="rachityadav.ml@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)
