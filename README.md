# Wan2.1 Text-to-Video Setup

This repository contains the setup and implementation for running the Wan2.1 Text-to-Video model from Hugging Face.

## Requirements

- NVIDIA GPU with at least 16GB VRAM (recommended)
- CUDA compatible system
- Python 3.8 or higher

## Installation

1. Clone this repository:
```bash
git clone https://github.com/DSMPromo/wan2-1-setup.git
cd wan2-1-setup
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the example script:
```bash
python generate_video.py
```

The script will generate a video based on the default prompt and save it as `output.mp4`.

### Customizing Generation

You can modify the `generate_video.py` script to:
- Change the prompt
- Adjust the number of frames
- Modify generation parameters
- Add custom negative prompts

## Model Details

The Wan2.1 T2V model is a text-to-video generation model that can create short video clips based on text descriptions. It uses a diffusion-based approach and supports various creative prompts.

## Resources

- [Model Card on Hugging Face](https://huggingface.co/Wan-AI/Wan2.1-T2V-14B)
- [Diffusers Documentation](https://huggingface.co/docs/diffusers/index)

## Notes

- The first run will download the model weights (approximately 14GB)
- Generation time varies depending on your hardware
- For best results, use detailed and descriptive prompts