# write setup.py for packaging the project
from setuptools import setup, find_packages # type: ignore
from typing import List
HYPHEN_E_DOT='-e .'

# create funcation get_requirments for install requirments.txt take is as str and list 
def get_requirements(file_path:str) -> List[str]:
    requirements=[]
    with open(file_path) as f:
        requirements=f.readlines()  
        requirements=[req.replace("\n","") for req in requirements]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

## create setup params  for my mlproject   and take lib details from requirments.txt   
setup(
    name='mlproject',
    version='0.1',
    packages=find_packages(),
    author='Subhra',
    author_email='subhra1973@gmail.com',
    description='A machine learning project',
    install_requires=get_requirements('requirements.txt')
    # add more metadata as needed
    )

