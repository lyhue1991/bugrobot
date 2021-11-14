import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bugrobot",
    version="0.4",
    author="PythonAiRoad",
    author_email="lyhue1991@163.com",
    description="A useful tool to monitor your running code bug by sending email or wechat message",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lyhue1991/bugrobot",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5'
)
