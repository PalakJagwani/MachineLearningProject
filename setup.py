## This setup.py file will be responsible in creating/building my machine learning application as a package
from setuptools import find_packages, setup
from typing import List
    

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str] :
    ## This function will return the list of requirements

    requirements = []
    with open(file_path) as file_obj :
        requirements = file_obj.readlines()
        requirements = [requirement.replace('\n', " ") for requirement in requirements]
        if HYPEN_E_DOT in requirements : 
            requirements.remove(HYPEN_E_DOT)
    
    return requirements
        


## meta-data info about the entire project
setup(
    name='mlproject',
    version='0.0.1',
    author='Palak',
    author_email='jagwanipalak02@gmail.com',
    packages=find_packages(), ## this find_package() will run and find in which folder do you have __init__.py and will build that package(src in our case) and once it's build you can import it wherever you want(entire project development will happen in src package)
    install_requires = get_requirements('requirements.txt'),
)

## So, i can either install this setup.py or make it run when in want to install all packages  ( -e . in requirement.txt will automatically trigger setup.py 