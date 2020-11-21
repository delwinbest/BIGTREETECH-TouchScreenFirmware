Import("env")
import os
from distutils.dir_util import copy_tree, remove_tree, mkpath
import shutil 


# access to global construction environment
print(env)

# Dump construction environments (for debug purpose)
#print(env.Dump())

def after_build(source, target, env):
    dst_dir = env['PROJECT_DIR'] + "/Copy to SD Card - MKS/"
    # Backup Config File
    dst_filename = env['PROJECT_BUILD_DIR'] + "/" + env['PIOENV'] + "/config.ini"
    source_filename = dst_dir + "config.ini"
    shutil.copyfile(source_filename, dst_filename)
    # Remove any existing Folder
    if os.path.exists(dst_dir):
        remove_tree(dst_dir)
        mkpath(dst_dir)
    # Copy Bin File to SD Card Folder
    source_filename = env['PROJECT_BUILD_DIR'] + "/" + env['PIOENV'] + "/" + env['PROGNAME'] + ".bin"
    dst_filename = dst_dir + "mkstft28.bin"
    shutil.copyfile(source_filename, dst_filename)
     # Restore Config file
    source_filename = env['PROJECT_BUILD_DIR'] + "/" + env['PIOENV'] + "/config.ini"
    dst_filename = dst_dir + "config.ini"
    shutil.copyfile(source_filename, dst_filename)
    # Copy BMP folder to SD Card Folder
    src_dir = env['PROJECT_DIR'] + "/Copy to SD Card root directory to update - Unified Menu Material theme/TFT28"
    copy_tree(src_dir, dst_dir + "MKS/")
    # Copy Language Packs folder to SD Card Folder
    src_dir = env['PROJECT_DIR'] + "/Copy to SD Card root directory to update - Unified Menu Material theme/Language Packs"
    copy_tree(src_dir, dst_dir + "Language Packs")   
env.AddPostAction("buildprog", after_build)

