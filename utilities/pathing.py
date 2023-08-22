import os
import subprocess
from utilities.logging import notif

# If you want to change the parameters you pass to test, change them here
# NOTE - we use "dir" for directories, and "path" for files
# -- RELATIVE PATHS -- #
rel_models_dir = "models/" # directory containing your models

rel_det_model_dir = "GroundingDINO/" # directory containing detection model
rel_det_weights_path = "groundingdino_swint_ogc.pth" # the detection model weights you want to use
rel_det_config_path = "model_config.py" # the config file for your detection model

rel_seg_model_dir = "MobileSAM/" # directory containing segmentation model
rel_seg_weights_path = "mobile_sam.pt" # the segmentation model weights you want to use

rel_output_dir = "bin/outputs" # directory to store model output images, after inference


# -- ABSOLUTE PATHS -- #
root_dir = os.getcwd() # absolute path to root directory. we join everything else to this

models_dir = os.path.join(root_dir, rel_models_dir)
det_model_dir = os.path.join(models_dir, rel_det_model_dir)
det_weights_path = os.path.join(det_model_dir, rel_det_weights_path) 
det_config_path = os.path.join(det_model_dir, rel_det_config_path)

seg_model_dir = os.path.join(models_dir, rel_seg_model_dir)
seg_weights_path = os.path.join(seg_model_dir, rel_seg_weights_path)

output_dir = os.path.join(root_dir, rel_output_dir)

endpaths = [models_dir, det_model_dir, seg_model_dir, output_dir]

# create our necessary end_paths if they don't already exist
def init_paths(given_paths=endpaths,verbose=True):
    for dir in given_paths:
        if not os.path.exists(dir):
            if verbose: notif(f"Creating directory at {dir}")
            os.makedirs(dir, exist_ok=True)
        else:
            if verbose: notif(f"{dir} VALIDATED")

if __name__ == "__main__":
    init_paths()
