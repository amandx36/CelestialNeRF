# CelestialNeRF



# 🚀 Interactive 3D Reconstruction of Celestial Bodies using NeRF

This project reconstructs **photorealistic 3D models** of celestial bodies like Mars craters and asteroids using **Neural Radiance Fields (NeRF)** and real NASA image datasets.

## 🔭 What This Project Does
- Builds NeRF-based models using TensorFlow
- Converts 2D images into fully navigable 3D scenes
- Uses real data from Mars Rovers, OSIRIS-REx, and more

## 📁 Folder Structure
- `data/` - NASA image datasets
- `nerf_model/` - TensorFlow model logic (MLP, render, train)
- `scripts/` - Preprocessing and visualization
- `outputs/` - Generated scenes and model checkpoints
- `configs/` - Custom configs per dataset
- `main.py` - Project runner

## 🧠 Tech Used
- TensorFlow, NumPy, OpenCV
- NASA PDS, OSIRIS-REx datasets
- NeRF (Neural Radiance Fields)

## 🧪 How to Run

```bash
# Create virtual environment
python -m venv venv && source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run training
python main.py --config configs/mars_config.yaml



------------------------FRESH ===========================--------------------  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1



##  Getting Started

1. **Install dependencies**  
   ```bash
   pip install -r requirements.txt


# Celestial NeRF: 3D Reconstruction of Mars Surface with NeRF

##  Project Overview
This project reconstructs a 3D scene of the Martian surface (e.g., Jezero Crater) using Neural Radiance Fields (NeRF).  
Inputs: Multiple 2D images (Mastcam-Z) + camera poses → Outputs: Rendered 3D views and fly-through animation.

##  Dataset
- Source: NASA PDS Imaging Node, **Mastcam-Z Calibrated Science Bundle (Release 13)**  
- Contains images from Sols 1380–1499 (January–May 2025). Includes `.IMG` files and `.XML` metadata. :contentReference[oaicite:4]{index=4}

### Download steps:
1. Visit the PDS site and navigate to the Mars 2020 mission.
2. Click “Mastcam-Z Bundles” → select Release 13 → download zipped image bundle.
3. Extract into: `data/raw/images/`.
4. (Optional) Use PDS4 Viewer to inspect images and metadata. :contentReference[oaicite:5]{index=5}

##  Project Structure
nerf-mars-project/
├── data/
│ ├── raw/
│ │ └── images/ # Place your downloaded images here
│ └── processed/ # Preprocessed (resized/normalized) images
│ └── camera_poses.json # Camera pose data (generated via COLMAP)
├── notebooks/ # Jupyter notebooks for exploration & training
├── src/ # Project scripts (preprocess, model, train, render, utils)
├── outputs/
│ ├── renders/ # Final rendered frames or animations
│ └── models/ # Saved model checkpoints
├── README.md # (This file)
└── requirements.txt




##  Getting Started

1. **Install dependencies**  
   ```bash
   pip install -r requirements.txt





##  Getting Started

1. **Install dependencies**  
   ```bash
   pip install -r requirements.txt





    Download & prepare data

        Download images as per “Dataset Download Instructions”

        Run preprocessing:

        python src/preprocess.py --input data/raw/images --output data/processed --size 400

    Generate camera poses (COLMAP)
    Use COLMAP to estimate poses and convert them into camera_poses.json.

    Train NeRF model
    Run notebooks/03_train_nerf.ipynb or src/train.py.

    Render views
    Use src/render.py or notebooks/04_render_views.ipynb to generate novel view images and videos.

Resources & References

    [Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow] — theory reference.

    NASA PDS Mars 2020 Mission data portal.
    pds-geosciences.wustl.edu

    PDS4 Viewer tool for opening .XML labels.
    Mastcam-Z