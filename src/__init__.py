import os

def tcc_dist_dir() -> str:
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), "tcc_dist")

def tcc_bin_path() -> str:
    base_dir = tcc_dist_dir()
    if os.name == "nt":
        return os.path.join(base_dir, "tcc.exe")
    else:
        return os.path.join(base_dir, "bin", "tcc")
    
def tcc_include_dir() -> str:
    base_dir = tcc_dist_dir()
    if os.name == "nt":
        return os.path.join(base_dir, "libtcc")
    else:
        return os.path.join(base_dir, "include")
    
def tcc_lib_dir() -> str:
    base_dir = tcc_dist_dir()
    if os.name == "nt":
        return base_dir
    else:
        return os.path.join(base_dir, "lib")
