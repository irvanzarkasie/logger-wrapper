import setuptools, os, subprocess

BUILD_NUMBER = os.path.dirname(os.path.realpath(__file__)) + "/BUILD_NUMBER"
VERSION_NUMBER = os.path.dirname(os.path.realpath(__file__)) + "/VERSION_NUMBER"

BUILD_NUMBER = subprocess.run(["cat", BUILD_NUMBER], capture_output=True, text=True).stdout.split("\n")[0]
VERSION_NUMBER = subprocess.run(["cat", VERSION_NUMBER], capture_output=True, text=True).stdout.split("\n")[0]

setuptools.setup(
    name="logger-wrapper",
    version=VERSION_NUMBER + "." + BUILD_NUMBER,
    author="expecc",
    author_email="expecc@expecc.com",
    description="Common package for logging purpose",
    packages=setuptools.find_packages(),
    include_package_data=True
)