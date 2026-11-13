# Experiment 3 — Nov 2026

<!-- Draft written with Claude. Karoliina: rewrite in your own words before applying. -->

**Goal:** give the model my sketch as an image (not only as a prompt) and test out ControlNet. Can it keep my geometry AND look realistic?

**Tool:** Comfy Cloud, template "Z-Image-Turbo Fun Union ControlNet". Same model as Experiment 2, the guide was new.

**How I measured geometry:** I used Claude to run the measurement. It puts my sketch lines over the render and counts how many of them still have a matching edge nearby. Here it's fair, because the render starts from my sketch, so the camera is fixed. For realism I used my perspective.

---

### Test 1: canny guide at full strength

Canny turns my sketch into a line map, and the model has to follow the lines.

**My guess:** more similar to the sketch, the mistakes from Experiment 2 won't repeat, and the result will look like the MyArchitectAI no-style render (accurate, but a stiff sofa).

![canny strength 1.00](D_canny_strength-1.00.png)

**Result:** 95% of my sketch lines kept. Three shelves, round cushions, curtains on both sides: every mistake from Experiment 2 was fixed. But it doesn't look real at all. It even paints my drawn outlines, and the sofa is made of boxes. My guess was right.

**Lesson:** a great score can still be a bad image. Painting the lines themselves gives a perfect geometry score. So from now on I judge every result on two things: geometry (the number) and realism (my eye).

### Test 2: finding the right strength

**My guess:** as the strength goes down, realism gets better and geometry suffers. The art is to find the golden middle point.

Same prompt, same seed (0), only the strength changes:

| Strength | Sketch lines kept | What I see |
| --- | --- | --- |
| 1.00 | 95% | Outlines everywhere, box sofa |
| 0.75 | 90% | Still box sofa, thinner outlines |
| 0.60 | 73% | Room and furniture mostly in place, but still looks artificial. Floor lamp lost its shade, two strange rings float where I drew round cushions |
| 0.55 | 64% | Lamp shade back but too small and too low, sofa pushed back |
| 0.50 | 59% | Looks real, but furniture moved and shrank, pendant lamp and plant disappeared, an extra door appeared |
| 0.25 | (by eye: a different room) | What I'd call realistic, but the camera, windows and shelves changed |

| 0.75 | 0.60 | 0.50 | 0.25 |
| --- | --- | --- | --- |
| ![0.75](D_canny_strength-0.75.png) | ![0.60](D_canny_strength-0.60.png) | ![0.50](D_canny_strength-0.50.png) | ![0.25](D_canny_strength-0.25.png) |

Red = my sketch lines on top of the 0.60 render:

![overlay canny 0.60](D_overlay_canny-0.60.jpg)

**Result:** my guess was right, but the change isn't gradual. Between 0.75 and 0.50 there's a big jump. I locked 0.60 as the best balance.

**Why 0.25 looks real and 0.60 doesn't:** at 0.25 the model chooses almost everything itself: a normal camera view, natural furniture sizes, lived-in details (books, a plant, a radiator), real textures and soft daylight. At 0.60 it has to follow my sketch, which has a very wide, perfectly centred view and an empty room. So part of the realism problem is the input itself.

(The measurement gave 0.25 a score of 59%, but by eye it's clearly a different room. The wooden floor has lots of plank lines that happen to match my drawn floor lines, so the score is too kind there.)

### Test 3: a prompt for realism

Same strength (0.60) and seed, but I added photo words to the end of the prompt: *"Real interior photograph, natural afternoon sunlight through the window casting soft shadows on the floor, shot on a 35mm camera, lived-in and cosy, subtle imperfections, realistic textures on walls and fabrics."*

**My guess:** the image will be much more realistic.

| Seed 0 | Seed 1 |
| --- | --- |
| ![realism prompt seed 0](D_canny_0.60_realism-prompt_seed0.png) | ![realism prompt seed 1](D_canny_0.60_realism-prompt_seed1.png) |

**Result:** much better light, darker corners and warmer shadows, more like a phone photo. But still kind of artificial. The rings stayed. Words can't fix something that comes from the sketch lines.

**Seed check:** the layout held with seed 1, and the rings appeared again, so they're a habit and not bad luck. But the geometry score moved from 64% to 70% just because of the seed. So differences smaller than about 6 points can be random. I can't say the prompt "cost" geometry.

### Test 4: depth guide instead of canny

A depth map shows what's near and far instead of lines. Same strength (0.60), same prompt, same seed.

**My guess:** realism will improve, but geometry will suffer.

| Depth map | Result |
| --- | --- |
| ![depth map](D_depth-map.jpg) | ![depth 0.60](D_depth_0.60_realism-prompt_seed0.png) |

**Result:** realism improved impressively, but geometry didn't. 51% of my sketch lines kept (canny with the same settings: 64%). The picture became a window, the plant disappeared, the lamps were wrong, and the floor planks now run sideways.

**Why:** the depth map shows the 3D shapes well (room, sofa, tables, lamp shades), but it's blind to anything flat on a wall (window, door, picture, shelves) and to thin things (the plant, the lamp pole). The floor is flat too, so it doesn't know which way the planks run. The round cushions did come back as real cushions, no rings.

(My first depth run came out small, because the depth tool was set to 512. I re-ran it at full size: 52% vs 51%, so the size wasn't the reason.)

![overlay depth 0.60](D_overlay_depth-0.60.jpg)

---

### Test 5: depth and canny together

Canny was too strict and depth was too loose, so I wanted to try both at the same time. Depth for the 3D shapes, and canny on low strength just for the flat things depth can't see (window, door, floor lines).

Setup: depth 0.60 + canny 0.30, same prompt, same seed (0). Claude wired the second ControlNet for me, I came up with the test and the hypothesis.

**My hypothesis:** this is my golden middle point. I hoped for 65–70% geometry and a really realistic look (lights, shadows, textures looking real) with the least mistakes.

| Canny 0.60 | Depth 0.60 | Depth 0.60 + canny 0.30 |
| --- | --- | --- |
| ![canny](D_canny_0.60_realism-prompt_seed0.png) | ![depth](D_depth_0.60_realism-prompt_seed0.png) | ![both](D_combo_depth0.60_canny0.30.png) |

| Same prompt, seed 0 | Sketch lines kept |
| --- | --- |
| Canny 0.60 | 64% |
| Depth 0.60 | 51% |
| **Depth 0.60 + canny 0.30** | **67%** |

![overlay both](D_overlay_combo.jpg)

**Result:** 67%, so the geometry part of my hypothesis was right.

What worked:
- the camera and the room match my sketch again (no doorway frame like with depth)
- the floor planks go towards the back wall again, canny fixed what depth couldn't see
- window, door, picture, shelves and both lamps are where I drew them

What's still not right:
- realism is better than canny but a bit darker and less "photo" than depth alone
- the plant is still missing
- two round pillows sit on top of the sofa, exactly where I drew the cushion circles
- a thin black bar behind the sofa, from my backrest line

So it's the best balance so far, but not perfect yet.

**Seed check:** one seed isn't enough, so I ran the same setup with seed 1 and 2.

My guess: all of them will land around 67%, plus or minus 5.

| Seed 1 | Seed 2 |
| --- | --- |
| ![seed 1](D_combo_seed1.png) | ![seed 2](D_combo_seed2.png) |

| Seed | Sketch lines kept |
| --- | --- |
| 0 | 67% |
| 1 | 72% |
| 2 | 61% |
| **Average** | **about 67%** |

My guess was almost right, seed 2 was just one point under. So the 67% was normal, not luck.

The same things happen with every seed:
- the layout always matches my sketch
- the plant is always missing
- my drawn backrest line turns into a glass panel or a bar behind the sofa
- my cushion circles turn into pillows on top of the sofa

These mistakes come from my simple sketch, not from bad luck. A better, more realistic input might fix them.

### What I learned

- **Canny** sees every line: accurate, but it copies things it shouldn't (outlines, rings).
- **Depth** sees only 3D shapes: realistic, but it loses flat details and thin objects.
- **Both together** fix each other's blind spots: depth for the shapes, canny for the flat details. Best balance so far, about 67% on average over 3 seeds.
- **Strength** mostly decides *where things are*, not *how real it looks*.
- **One number is not enough.** I need the geometry score and my eye together, and I need to check more than one seed before trusting a difference.

**Next I'd try:** play with the canny strength (maybe 0.20 or 0.40), and try a better input: a sketch with a normal camera view, like architects' screenshots from 3D software.

[← Back to the front page](README.md)
