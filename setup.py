import os


init_paths()


os.system('python -m pip --verbose install -r requirements.txt')


os.system('python -m pip install -e setups/segment_anything setups/GroundingDINO')


os.system('python -m pip install --upgrade diffusers[torch]')


os.system('git submodule update --init --recursive')

if not os.path.isfile(det_weights_path):
    notif("NOW DOWNLOADING GROUNDINGDINO MODEL")
    os.system('wget https://github.com/IDEA-Research/GroundingDINO/releases/download/v0.1.0-alpha/groundingdino_swint_ogc.pth -P /models/GroundingDINO/')
    
if not os.path.isfile(seg_weights_path):
    notif("NOW DOWNLOADING MOBILESAM MODEL")
    os.system('wget https://github.com/ChaoningZhang/MobileSAM/raw/master/weights/mobile_sam.pt -P /models/MobileSAM/')