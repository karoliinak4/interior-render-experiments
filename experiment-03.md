# Experiment 3 — Nov 2026

**Goal:** give the model my sketch as an image (not only as a prompt) and test out ControlNet. Can it keep my geometry AND look realistic?

**Tool:** Comfy Cloud, template "Z-Image-Turbo Fun Union ControlNet". Same model as Experiment 2, the guide was new.

**How I measured geometry:** I used Claude to run the measurement. It puts my sketch lines over the render and counts how many of them still have a matching edge nearby. Here it's fair, because the render starts from my sketch, so the camera is fixed. For realism I used my perspective.

**How I worked:** this experiment was also for learning the tool, ComfyUI and how ControlNet guides work. I studied with Claude: I asked it to explain the concepts, to make me guess the result before every test, and to explain why things happened. I ran the tests in ComfyUI and judged the realism myself. Claude ran the geometry measurement.

**What I learned about ComfyUI:** ComfyUI works with nodes, boxes connected with wires. Each node does one step, and nothing happens unless a node does it. The nodes I used and what they do:
- **Load model:** loads the image model (Z-Image Turbo)
- **Prompt:** my text description
- **Empty image:** sets the image size
- **KSampler:** actually makes the image; the seed and steps are set here
- **VAE Decode:** turns the result into a picture I can see
- **Canny:** turns my sketch into a line map
- **Depth Anything:** turns my sketch into a near/far map
- **Apply ControlNet:** makes the model follow the map, and strength says how much

I also learned to switch a node off without deleting it (bypass), and that a fixed seed lets me compare runs fairly.

**Why canny and depth:** this model supports 8 guides (canny, depth, MLSD, HED, scribble, gray, pose and inpainting). I started with canny and depth because they came ready in the template and they're opposites: canny follows lines, depth follows 3D shapes. Comparing opposites seemed like the best way to learn how guides work. Later I learned that MLSD only follows straight lines and is made for architecture, so it might keep my walls and windows without turning my cushion circles into rings. That's my next test.

---

### Test 1: canny guide usage

Canny turns my sketch into a line map, and the model has to follow the lines.

**My guess:** more similar to the sketch, the mistakes from Experiment 2 won't repeat, and the result will look accurate but not very realistic.

![canny strength 1.00](D_canny_strength-1.00.png)

**Result:** 95% (measured by Claude) of my sketch lines are matching. Mistakes from Experiment 2 were fixed but it doesn't look real at all. My guess was right.

**Lesson:** a great score can still be a bad image. Painting the lines themselves gives an amazing geometry score. From now I judge every result on two things: geometry (the number) and realism (my eye).

### Test 2: finding the right strength

**My guess:** as the canny strength goes down, realism gets better and geometry suffers. The art is to find the golden middle ground.

Same prompt, same seed (0), only the strength changes:

| Strength | Sketch lines kept | What I see |
| --- | --- | --- |
| 1.00 | 95% | Thick outlines everywhere, strange sofa |
| 0.75 | 90% | The sofa is still strange, thinner outlines |
| 0.60 | 73% | Room and furniture mostly in place, but still looks artificial. Floor lamp lost the shade, two strange rings float instead of round cushions |
| 0.55 | 64% | Lamp shade is back but too small and too low, sofa is pushed back |
| 0.50 | 59% | Looks real, but furniture moved and shrank, ceiling lamp shade and plant disappeared, an extra door appeared |
| 0.25 | (visually looks like a different room) | What I'd call realistic, but it's not recognisable |

| 0.75 | 0.60 | 0.50 | 0.25 |
| --- | --- | --- | --- |
| ![0.75](D_canny_strength-0.75.png) | ![0.60](D_canny_strength-0.60.png) | ![0.50](D_canny_strength-0.50.png) | ![0.25](D_canny_strength-0.25.png) |

Red = my sketch lines on top of the 0.60 strength canny render:

![overlay canny 0.60](D_overlay_canny-0.60.jpg)

**Result:** my guess was right but surprisingly between 0.75 and 0.50 there's a big difference. I chose 0.60 as the best balance and locked it.

**Why 0.25 looks real and 0.60 doesn't:** at 0.25 the model chooses almost everything itself: the camera view, furniture sizes, details (books, a plant, a radiator), textures and the light. At 0.60 it still follows my sketch quite accurately. I guess part of the realism problem is my weak and basic sketch.

(The measurement gave 0.25 a score of 59%, but visually it looks like a different room) 

### Test 3: a prompt for realism

Same strength (0.60) and seed, but I added photo words to the end of the prompt: *"Real interior photograph, natural afternoon sunlight through the window casting soft shadows on the floor, shot on a 35mm camera, lived-in and cosy, subtle imperfections, realistic textures on walls and fabrics."*

**My guess:** the image will be much more realistic on high strength.

| Seed 0 | Seed 1 |
| --- | --- |
| ![realism prompt seed 0](D_canny_0.60_realism-prompt_seed0.png) | ![realism prompt seed 1](D_canny_0.60_realism-prompt_seed1.png) |

**Result:** more realistic light, darker corners and more intense shadows. Still a little artificial. The random rings stayed. A better prompt can't fix something that comes from the sketch lines.

**Seed change:** the layout held with seed 1, the rings appeared again, so they were probably not bad luck. The geometry accuracy moved from 64% to 70% just because of the seed. So small differences (under ~6 points) can be just random.

### Test 4: depth guide instead of canny

A depth map shows what's near and far instead of lines. I used the same strength (0.60), same prompt and same seed.

**My guess:** realism will improve but geometry will suffer.

| Depth map | Result |
| --- | --- |
| ![depth map](D_depth-map.jpg) | ![depth 0.60](D_depth_0.60_realism-prompt_seed0.png) |

**Result:** realism improved noticeably but geometry didn't. 51% of my sketch lines matched (with canny 64%). Errors: the picture became a window, the plant disappeared, the lamps were wrong, and the floor planks run sideways.

**Why:** the depth map shows the room and the items ( sofa, tables, lamp shades) but doesn't recognise flat items on a wall (window, door, picture, shelves) and things that are too small or thin. The floor is flat so it doesn't know which way it runs. The round cushions did come back as real cushions, rings are gone.


![overlay depth 0.60](D_overlay_depth-0.60.jpg)

---

### Test 5: depth guide and canny guide together

Canny was too strict and depth was too abstract. I wanted to try both at the same time.

Setup: depth 0.60 + canny 0.30, same prompt, same seed (0). Depth holds the shapes, so I used canny on low strength (0.30), just for the flat things depth can't see (window, door, floor lines). After trying to wire it manually myself, I got an error and asked Claude to wire the second ControlNet for me, to fix my mistake. I came up with the hypothesis.

**My hypothesis:** this is my golden middle point. I hoped for 65–70% geometry and a really realistic look (lights, shadows, textures looking real) with the minimal mistakes.

| Canny 0.60 | Depth 0.60 | Depth 0.60 + canny 0.30 |
| --- | --- | --- |
| ![canny](D_canny_0.60_realism-prompt_seed0.png) | ![depth](D_depth_0.60_realism-prompt_seed0.png) | ![both](D_combo_depth0.60_canny0.30.png) |

| Same prompt, seed 0 | Sketch lines kept |
| --- | --- |
| Canny 0.60 | 64% |
| Depth 0.60 | 51% |
| **Depth 0.60 + canny 0.30** | **67%** |

![overlay both](D_overlay_combo.jpg)

**Result:** 67% geometry accuracy so I was right about that.

What worked:
- the room generally matches my sketch.
- the floor planks are correct and canny fixed what depth couldn't see.
- Most items are matching the sketch.

What didn't:
- realism improved compared to canny but a bit too dark.
- the plant is still missing.
- two round pillows sit on top of the sofa, which is not a bad outcome actually but also not accurate.
- a random black bar behind the sofa.

the best balance so far but not perfect.

**Seed check:** one seed isn't enough, I ran the same setup with seed 1 and 2.

My guess: all of them will match around 65%, +/- 5.

| Seed 1 | Seed 2 |
| --- | --- |
| ![seed 1](D_combo_seed1.png) | ![seed 2](D_combo_seed2.png) |

| Seed | Sketch lines kept |
| --- | --- |
| 0 | 67% |
| 1 | 72% |
| 2 | 61% |
| **Average** | **about 67%** |

My guess was almost right. Meaning 67% accuracy was normal, not luck.

The same things happen with all tested seeds:
- the layout matches my sketch
- the plant is always missing
- my drawn backrest line turns into a glass panel or a bar behind the sofa
- my cushion circles turn into pillows on top of the sofa

These mistakes come from my simple and weak sketch, most probably. A better and more realistic input should fix them.

### What I learned

- **Canny** sees every line, especially on high strength: It's accurate, but doesn't always understand what things are.
- **Depth** sees only 3D shapes: realistic but loses flat details and thin objects. Required a stronger input.
- **Both together** slightly fix each other's weaknesses: depth for the shapes, canny for the flat details. Best balance so far.
- **Strength** decides *where things are* not *how real is it*.
- **One number is not enough.** I need the geometry score and my own visual perspective and I need to check more than one seed before trusting a difference. Everything requires testing different versions and change of setting details.

**Next I'd try:** MLSD instead of canny (alone and together with depth), and a more professional sketch like architects would use.

[← Back to the front page](README.md)
