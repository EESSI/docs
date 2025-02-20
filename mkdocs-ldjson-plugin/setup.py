from setuptools import setup, find_packages

# Read requirements from requirements.txt
def read_requirements():
    with open("requirements.txt", encoding="utf-8") as f:
        return f.read().splitlines()

setup(
    name="inject_ld_json",
    version="0.1.0",
    py_modules=["inject_ld_json"],
    packages=find_packages(),
    install_requires=read_requirements(),  # Use requirements.txt
    include_package_data=True,
    entry_points={
        "mkdocs.plugins": [
            "inject_ld_json = inject_ld_json:InjectLDJsonPlugin",
        ]
    },
)
