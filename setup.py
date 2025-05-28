from setuptools import setup, find_packages

setup(
    name="remla2025-team19-lib-ml",
    version="0.0.1",
    author="Team 19",
    description="ML preprocessing library for restaurant sentiment analysis",
    url="https://github.com/remla2025-team19/lib-ml",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pandas==2.2.3",
        "nltk==3.9.1",
        "scikit-learn==1.6.1"
    ],
    python_requires="==3.11.12",
)