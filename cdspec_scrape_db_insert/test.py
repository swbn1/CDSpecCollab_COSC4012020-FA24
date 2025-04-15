import pandas as pd
import os
import pathlib

if __name__ == '__main__':
    runs_path = pathlib.Path('/home/shared_workspace/CDSpecCollab_COSC4012020-FA24/cd_spec_viewer_web/cd_spec_viewer_web/cdspecruns')
    the_files = list(runs_path.glob('*.csv'))
    print(the_files)


