import os
import pathlib

from game.runner import main

workdir = pathlib.Path(__file__).parent.parent

if __name__ == "__main__":
    os.chdir(workdir)
    main()
