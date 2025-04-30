from setuptools import setup, find_packages

setup(
    name="mealy-ultrades",
    version="1.0.0",
    author="Helena Miranda, Publio Lima, Felipe Cabral, Max de Queiroz",
    author_email="helenabpm2005@gmail.com",
    description="Extensão para criação e manipulação de autômatos de Mealy no UltraDES-Python",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/helena-mirandab/Mealy-Automaton-For-UltraDES-Python",  
    packages=find_packages(),
    py_modules=["mealy_automaton"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Topic :: Scientific/Engineering :: Control Engineering",
    ],
    python_requires='>=3.8',
    install_requires=[
        "pythonnet>=3.0.0"  # Suporte ao CLR (caso aplicável)
    ],
    include_package_data=True,
    package_data={
        '': ['README.md'],
    }
)
