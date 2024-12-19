from Utils import map_gen
import time
import os
from pathlib import Path
import sys
import shutil

if not len(sys.argv) > 1:
    print('Usage: ' + sys.argv[0])
    print('For example, to execute type1, execut ' + sys.argv[0] + " type1.")
    exit()

home = str(Path.home())
ego_dir = os.path.join(home, 'ego-planner/src/planner/plan_manage')

if not os.path.exists(ego_dir):
    print('Please make sure ego-planner has been correctly installed in your home directory')
    exit()

src_dir = os.path.dirname(os.path.abspath(__file__))
launch_folder = sys.argv[1] + "/launch"
launch_folder_path = os.path.join(src_dir, launch_folder)

if os.path.exists(launch_folder_path):
    dst_dir = ego_dir
    dst_folder_path = os.path.join(dst_dir, "launch")

    if os.path.exists(dst_folder_path):
        shutil.rmtree(dst_folder_path)

    shutil.copytree(launch_folder_path, dst_folder_path)

else:
    print("Launch file not exist, only publishing the map")




map_generator = map_gen.MapGenerator(0.1, height = 2.2, size = 0.2, z_global = -0.2)
map_generator.read_map(sys.argv[1] + "/map")
map_generator.map_pub()
a = input("Press \"enter\" to stop map publishing")
map_generator.map_pub_stop()


