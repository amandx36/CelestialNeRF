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
