from setuptools import setup

setup(
    name="inject_ld_json",
    py_modules=["inject_ld_json"],
    entry_points={
        "mkdocs.plugins": [
            "inject_ld_json = inject_ld_json:InjectLDJsonPlugin",
        ]
    },
)