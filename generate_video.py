import torch
from diffusers import DiffusionPipeline, DPMSolverMultistepScheduler
from diffusers.utils import export_to_video

def generate_video(prompt, negative_prompt=None, num_frames=16):
    # Load the pipeline
    pipe = DiffusionPipeline.from_pretrained(
        "Wan-AI/Wan2.1-T2V-14B",
        torch_dtype=torch.float16,
        variant="fp16"
    )

    # Enable memory efficient attention
    pipe.enable_xformers_memory_efficient_attention()
    
    # Use DPMSolver++ scheduler
    pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)

    # Move to GPU if available
    pipe = pipe.to("cuda" if torch.cuda.is_available() else "cpu")

    # Generate the video frames
    video_frames = pipe(
        prompt=prompt,
        negative_prompt=negative_prompt,
        num_inference_steps=25,
        num_frames=num_frames
    ).frames

    # Export to video file
    output_path = "output.mp4"
    export_to_video(video_frames, output_path)
    return output_path

if __name__ == "__main__":
    prompt = "A beautiful sunset over the ocean, cinematic, high quality"
    negative_prompt = "poor quality, blurry, bad"
    
    print("Generating video...")
    output_path = generate_video(prompt, negative_prompt)
    print(f"Video saved to: {output_path}")