from setuptools import setup


def get_version(version: "setuptools_scm.ScmVersion") -> str:
    return f"{version.branch}+{version.node}"


setup(
    name="tt-support-tools",
    license="asl-2.0",
    setup_requires=["setuptools_scm"],
    use_scm_version={"version_scheme": get_version, "normalize": False},
    packages=["tt_support_tools"],
    dependencies=[
        "appdirs==1.4.4",
        "cairocffi==1.6.0",
        "CairoSVG==2.7.0",
        "certifi==2023.5.7",
        "cffi==1.15.1",
        "charset-normalizer==3.1.0",
        "click==8.1.3",
        "cssselect2==0.7.0",
        "defusedxml==0.7.1",
        "gdstk==0.9.49",
        "gitdb==4.0.10",
        "GitPython==3.1.40",
        "idna==3.4",
        "importlib-resources==5.12.0",
        "mistune==3.0.1",
        "numpy==1.24.3",
        "Pillow==9.5.0",
        "pycparser==2.21",
        "python-frontmatter==1.0.0",
        "pytz==2023.3",
        "PyYAML==6.0",
        "requests==2.31.0",
        "smmap==5.0.0",
        "stripe==5.4.0",
        "tinycss2==1.2.1",
        "urllib3==2.0.3",
        "wasmtime==9.0.0",
        "webencodings==0.5.1",
        "yowasp-runtime==1.22",
        "yowasp-yosys==0.30.0.0.post538",
        "zipp==3.15.0",
        "pre-commit==3.4.0",
    ],
)
