from setuptools import setup, find_packages

with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name = "xjt",
    version = "1.0.0",
    author = "ghostccamm",
    packages = find_packages(),
    python_requires = ">=3.9",
    install_requires = required,
    zip_safe = True,
    entry_points = {
        "console_scripts" : [
            "xjt = xjt.run:main"
        ]
    },
    package_data = {
        'xjt.data' : ['burp.jpg']
    }
)
