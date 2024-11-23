from . import tcc_bin_path, tcc_lib_dir
import subprocess, sys, platform, os


def main():
    # pass all args to tcc
    tcc_bin = tcc_bin_path()
    if len(sys.argv) == 1:
        subprocess.run([tcc_bin])
        return

    tcc_lib_path = tcc_lib_dir()
    system = platform.system()

    extra_include_paths = []
    extra_library_paths = []
    if system == "Linux" or system == "Darwin":
        extra_include_paths.append(os.path.join(tcc_lib_path, "tcc", "include"))
        extra_library_paths.append(os.path.join(tcc_lib_path, "tcc"))
    if system == "Linux":
        extra_library_paths.append("/usr/lib")
        extra_library_paths.append("/usr/lib/x86_64-linux-gnu")

    args = [tcc_bin]
    for path in extra_include_paths:
        args.append("-I" + path)
    for path in extra_library_paths:
        args.append("-L" + path)
    subprocess.run(args + sys.argv[1:])


if __name__ == "__main__":
    main()
