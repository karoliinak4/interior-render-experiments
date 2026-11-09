# Learning log

One entry per day. What I tried, what broke, what I learned.

---

## Day 1 — 9 Nov 2026

**Goal:** See how an AI interior renderer handles a real room and a line sketch, and where it breaks.

**Tool:** MyArchitectAI (free trial, 6 of 10 renders used)

**Inputs:**
- A: a photo of my living room (iPhone, normal 1x lens, evening light)
- B: a simple line sketch of a living room (made with Claude to simulate an architect's drawing)

### Test 1: changing the floor in my living-room photo

| Try | Prompt | Mask | Result |
| --- | --- | --- | --- |
| 1 | "Replace the light wooden floor with a dark walnut wooden floor…" (verb first) | Part of the floor | Uneven colour, old floor still visible near the window and under the dining table, planks changed direction |
| 2 | "Dark walnut wooden floor, wide planks, matte finish" (describes the result, from the in-app tip) | Whole floor, including under the furniture and over the chair legs | Even colour, the chair and table legs survived, the rest of the room unchanged. Colour came out reddish, not walnut |

**What I learned:** the app's own tip ("don't use verbs, describe the result") contradicts the help guide, which says to start with a verb. The app was right in my test.

**Honest problem:** I changed two things at once (prompt style AND mask), so I can't say which one fixed it.

### Test 2: does the style library change the geometry?

I laid my sketch lines over each render and measured how many of my lines still have a matching edge in the render (same image size, 3 tolerance levels).

| Render | Strict | Medium | Loose |
| --- | --- | --- | --- |
| No style | 71% | 74% | 79% |
| Style + daylight edit | 52% | 62% | 75% |
| With style | 40% | 53% | 68% |

**What I saw:**
- With style: looks beautiful and realistic, but the door, floor lamp, side table and picture moved or grew, and the lamp shade changed shape.
- No style: almost everything stays where I drew it, but the sofa looks like a stiff box. It copies my drawing too literally.

**The trade-off:** accurate geometry vs. realistic look. I want both.

**My mistake:** my first comparison used images of different sizes, which isn't fair. I re-ran it at the same size and the ranking stayed the same.

**Open question:** the daylight edit (made from the styled render) moved things *closer* to my sketch. I don't know why yet.

**Next:** set up ComfyUI and try ControlNet. Can it keep the geometry AND make the furniture look real?
