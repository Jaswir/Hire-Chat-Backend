import replicate

input = {
    "prompt": "an astronaut riding a horse on mars, hd, dramatic lighting",
    "scheduler": "K_EULER",
}

output = replicate.run(
    "stability-ai/stable-diffusion:ac732df83cea7fff18b8472768c88ad041fa750ff7682a21affe81863cbe77e4",
    input=input,
    
)
print(output)