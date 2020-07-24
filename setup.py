import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bitflyer_json_rpc_onsentamago",
    version="0.0.1",
    author="onsentamago",
    author_email="tamago4329@gmail.com",
    description="BitFlyer Http API package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/onsentamago/bitflyer_http_api",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3.7',
)