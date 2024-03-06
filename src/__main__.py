from . import tcc_bin_path
import subprocess, sys


def main():
    # pass all args to tcc
    subprocess.run([tcc_bin_path()] + sys.argv[1:], check=True)

if __name__ == "__main__":
    main()