from diffusers import StableDiffusionPipeline
import torch

def generate_image(prompt: str, output_path: str = "output.png"):
    pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5", 
        torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
    )

    if torch.cuda.is_available():
        pipe = pipe.to("cuda")
        print("✅ GPU detected: Using CUDA")
    else:
        print("⚠️ No GPU found: Running on CPU (slow)")

    print(f"🎨 Generating image for prompt: '{prompt}'")
    image = pipe(prompt).images[0]

    image.save(output_path)
    print(f"✅ Image saved at: {output_path}")

if __name__ == "__main__":
    user_prompt = input("Enter your prompt for the image: ")
    generate_image(user_prompt, "generated_image.png")
