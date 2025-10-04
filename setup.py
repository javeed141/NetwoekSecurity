from typing import List
from setuptools import find_packages,setup

def get_requirements()->List[str]:
    requirements_lst:List[str]=[]
    try:
        with open("requirements.txt") as file:
            # Read lines from the file 
            lines=file.readlines()
            # Process each line 
            for line in lines:
                requirement=line.strip()
                if requirement and requirement!='-e .':
                    requirements_lst.append(requirement)
            


    except FileNotFoundError:
        print("File not Found")
    return requirements_lst

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="JaveedShaik",
    author_email="dspexam123@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)