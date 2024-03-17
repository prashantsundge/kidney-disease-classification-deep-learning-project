
import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_descrition = f.read()

__version__ ="0.0.0"
REPO_NAME = "kidney-disease-classification-deep-learning-project"
AUTHOR_USER_NAME="prashantsundge"
SRC_REPO ="cnnClassfier"
AUTHOR_EMAIL="prashantsundge@gmail.com"



setuptools.setup(

    name=SRC_REPO,
    version =__version__,
    author=AUTHOR_USER_NAME,
    author_email= AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_descrition =long_descrition,
    long_descrition_content="text/markdown",
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls ={
        "KIDNEY DIEASE ": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)