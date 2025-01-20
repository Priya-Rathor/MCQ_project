from setuptools import find_packages,setup

setup(
    name='mcqgenerator',
    version='0.0.1',
    author='Priya rathor',
    author_email="rathorpriya1718@gmail.com",
    install_requires=["openia","langchain","streamlit","pyhton-detenv","PyPDF2"],
    packages = find_packages()
)