import os, sys
def import_dir(path):
    _i = os.path.abspath(path)
    
    if _i not in sys.path:
        sys.path.insert(1, _i)
        return f"{_i} added to path"
    
    return ""