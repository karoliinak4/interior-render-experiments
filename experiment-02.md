# Experiment 2 — Nov 2026

**Goal:** Learn ComfyUI basics before trying ControlNet. I wanted to understand what actually controls an AI image: the prompt, the seed, or both.

**Tool:** Comfy Cloud (5 free runs), Z-Image Turbo template (text-to-image, 1024 × 768, 8 steps)

**Why this experiment:** after testing MyArchitectAI in Experiment 1, I wanted to understand what might be happening behind the scenes, the engine of a tool like that. So I started learning ComfyUI, where you build the whole process yourself step by step. This was my first time ever using it, so it's a learning experiment. Before testing anything complicated, I wanted to understand the basic building blocks. I studied with Claude: I asked it to explain the concepts and to make me guess the result before every test. I ran the tests myself.

### Test 1: does the same seed give the same image?

I ran the same prompt twice with seed 0.

- After my first run, the seed suddenly showed a random long number. I found out the setting next to the seed was on "randomize", so ComfyUI picks a new seed after every run.
- I switched it to "fixed", set the seed back to 0 and ran again.
- **Result:** exactly the same image, pixel for pixel.

**What I learned:** same seed + same settings = same image. This matters because now I can change one thing at a time and know what caused the difference.

### Test 2: what does the seed change?

Prompt: "photorealistic modern living room, large window, wooden floor, soft daylight"

| Seed 0 | Seed 1 |
| --- | --- |
| ![seed 0](C_run1_short-prompt_seed0.png) | ![seed 1](C_run3_short-prompt_seed1.png) |

**My guess:** small changes, some colours and materials.

**Result:** colours and materials stayed close, but it was a different room: different windows, a round table instead of a square one, a kitchen instead of a desk, extra furniture. Funny detail: both times a beige L-shaped sofa, probably the model's idea of a "modern living room".

**What I learned:** the prompt decides *what* is in the room, the seed decides *how it's arranged*. With a short prompt, the seed changes the whole layout.

### Test 3: can a very detailed prompt describe my sketch?

I described my Experiment 1 sketch in a long prompt and ran it with seed 0 and seed 1.
The prompt I used:

> photorealistic living room seen straight on from the doorway, one-point perspective. Back wall: a two-pane window on the left half with sheer curtains on both sides, three floating wooden shelves on the right half. A grey three-seat fabric sofa with two round cushions against the back wall. A rectangular wooden coffee table in front of the sofa on a light rug. Left wall: a framed picture, a floor lamp and a small side table. Right wall: a white door. Light oak floor with planks running toward the back wall. Soft daylight.

| My sketch | Seed 0 | Seed 1 |
| --- | --- | --- |
| ![sketch](B_input_line-sketch.jpg) | ![long prompt seed 0](C_run4_long-prompt_seed0.png) | ![long prompt seed 1](C_run5_long-prompt_seed1.png) |

**My guess:** similar to my sketch, but not recognisably the same room.

**Result (seed 0):** about 7 of 10 details right. Wrong: two shelves instead of three, square cushions instead of round, a curtain only on one side. It even drew the doorway frame because I wrote "seen from the doorway". And the furniture is not where I drew it.

**My guess for seed 1:** colours and materials stay but the exact shades change ("grey" can be many greys), the layout changes, one mistake gets fixed, the shelf count stays wrong.

**Result (seed 1):**
- Shades changed: right (the cushions went from beige to grey)
- Shelf count still wrong: right
- Layout changes: wrong, it was almost the same room, the camera just moved back a bit
- One mistake fixed: wrong, the same mistakes came back

**What I learned:**
- The mistakes repeated, so they look like the model's habits, not bad luck. Counting things (three shelves) seems hard for it.
- The more detailed the prompt, the less the seed changes the layout.
- But words alone can't put things where I want them. The sketch has to go into the model as an image.


### Checking what I need for next time

After my research I started looking for some models from the Comfy Cloud model library. It has what I need, I will learn as I go:
- **Juggernaut-XL v9**: a photorealistic SDXL model
- **ControlNet depth** and **ControlNet canny** for SDXL
- **Depth Anything**: makes a depth map from my sketch

[← Back to the front page](README.md)
