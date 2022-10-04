from pathlib import Path
import os

def create_morphapp(path, title):
    p = Path(path)
    if p.is_dir():
        projFile = f'workspace "{title}"\n' 
        projFile += f'''    architecture "x64"
    startproject "{title}"
    '''
        projFile += '''configurations 
    {
        "Debug",
        "Release",
        "Distribution"
    }

    outputdir = "%{cfg.buildcfg}-%{cfg.system}-%{cfg.architecture}"

    include "Vendor.lua"
        '''

        # Write to project code to premake file
        with open(p.joinpath("premake5.lua").__str__(), "w") as premakeFile:
            premakeFile.write(projFile)

        # Rename folder to title
        parent = p.parent
        os.rename(p.__str__(), parent.joinpath(title).__str__())
    else:
        print(f'Invalid path {path}')
