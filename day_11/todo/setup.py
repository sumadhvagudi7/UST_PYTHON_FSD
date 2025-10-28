from setuptools import setup, find_packages

setup(
    name="TODO CLI",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "typer[all]",
        "bcrypt",
    ],
    entry_points={
        "console_scripts": [
            "todo-cli = todo.main:app"
        ],
    },
)