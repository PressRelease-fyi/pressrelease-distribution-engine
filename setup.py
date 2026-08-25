from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pressrelease-distribution-engine",
    version="1.0.0",
    author="PressRelease.fyi",
    author_email="info@pressrelease.fyi",
    description="PressRelease Distribution Engine is a software toolkit for preparing, organizing, and managing press release distribution workflows.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://pressrelease.fyi",
    project_urls={
        "Homepage": "https://pressrelease.fyi",
        "GitHub": "https://github.com/PressRelease-fyi/pressrelease-distribution-engine",
        "Documentation": "https://pressrelease-distribution-engine.readthedocs.io",
        "PyPI": "https://pypi.org/project/pressrelease-distribution-engine",
    },
    py_modules=["pressrelease_engine"],
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Office/Business",
    ],
    keywords=[
        "pressrelease-distribution-engine",
        "press-release-distribution",
        "media-targeting",
        "pr-workflow",
        "newswire-distribution",
        "publication-tracking",
        "ai-visibility",
        "pressrelease-fyi",
    ],
    entry_points={
        "console_scripts": [
            "pr-distribute=pressrelease_engine:main",
        ],
    },
)
