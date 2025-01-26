from setuptools import setup
import os, datetime, subprocess
import shutil

from wheel.bdist_wheel import bdist_wheel as _bdist_wheel


class genericpy_bdist_wheel(_bdist_wheel):
    def finalize_options(self):
        _bdist_wheel.finalize_options(self)
        self.root_is_pure = False

    def get_tag(self):
        python, abi, plat = _bdist_wheel.get_tag(self)
        python, abi = "py3", "none"
        if os.environ.get("CIBUILDWHEEL", "0") == "1":
            # pypi does not allow linux_x86_64 wheels to be uploaded
            if plat == "linux_x86_64":
                plat = "manylinux2014_x86_64"
            elif plat == "linux_aarch64":
                plat = "manylinux2014_aarch64"
        return python, abi, plat


cmdclass = {"bdist_wheel": genericpy_bdist_wheel}


# cd to `tinycc` directory and build tinycc
# For *nix
# run:
#     ./configure
#    make
#    make test
#    make install
# For Windows
# run:
#     win32\build-tcc.bat -c cl -t 64
def build_tinycc():
    this_directory = os.path.abspath(os.path.dirname(__file__))
    tinycc_dir = os.path.join(this_directory, "tinycc")

    # if tinycc dir does not exist, clone it
    if not os.path.exists(tinycc_dir):
        subprocess.run(
            ["git", "clone", "--depth", "1", "git://repo.or.cz/tinycc.git"],
            cwd=this_directory,
            check=True,
        )

    if os.name == "nt":
        win32_dir = os.path.join(tinycc_dir, "win32")
        subprocess.run(
            [os.path.join(win32_dir, "build-tcc.bat"), "-c", "cl", "-t", "64"],
            cwd=win32_dir,
            check=True,
        )
    else:
        subprocess.run(
            ["./configure", "--prefix=tcc_dist", "--disable-static"],
            cwd=tinycc_dir,
            check=True,
        )
        subprocess.run(["make", 'CFLAGS="-fPIC"'], cwd=tinycc_dir, check=True)
        subprocess.run(["make", "install"], cwd=tinycc_dir, check=True)
        subprocess.run(["make", "clean"], cwd=tinycc_dir, check=True)
        subprocess.run(
            ["./configure", "--prefix=tcc_dist", "--enable-static"],
            cwd=tinycc_dir,
            check=True,
        )
        subprocess.run(["make", 'CFLAGS="-fPIC"'], cwd=tinycc_dir, check=True)
        subprocess.run(["make", "install"], cwd=tinycc_dir, check=True)


build_tinycc()

this_directory = os.path.abspath(os.path.dirname(__file__))

# get current utc date and set the version to YYYY.MM.DD
version = datetime.datetime.now(datetime.timezone.utc).strftime("%Y.%m.%d")

long_description = """
tccbox is a python package that packs tiny c compiler for different platforms.

It uses the active branch at https://repo.or.cz/tinycc.git to build and release new versions.

Please visit the [repo](https://github.com/metab0t/tccbox) for more information.
"""

from tempfile import TemporaryDirectory

with TemporaryDirectory() as temp_dir:
    base_dir = os.path.abspath(os.path.dirname(__file__))
    tinycc_dir = os.path.join(this_directory, "tinycc")

    old_name = new_name = "tcc_dist"
    if os.name == "nt":
        old_name = "win32"
    shutil.copytree(
        os.path.join(tinycc_dir, old_name),
        os.path.join(temp_dir, new_name),
        dirs_exist_ok=True,
    )

    for fname in ["__init__.py", "__main__.py"]:
        shutil.copy2(
            os.path.join(base_dir, "src", fname), os.path.join(temp_dir, fname)
        )

    setup(
        name="tccbox",
        version=version,
        cmdclass=cmdclass,
        author="Yue Yang",
        author_email="metab0t@outlook.com",
        url="https://github.com/metab0t/tccbox",
        description="tccbox: pack platform specific tiny c compiler",
        long_description=long_description,
        long_description_content_type="text/markdown",
        license="LGPL",
        packages=["tccbox"],
        zip_safe=False,
        package_dir={"tccbox": temp_dir},
        package_data={
            "tccbox": [
                "tcc_dist/**",
            ]
        },
    )
