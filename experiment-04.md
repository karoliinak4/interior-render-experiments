# Experiment 4 — Nov 2026

<!-- Draft written with Claude from Karoliina's notes. Karoliina: check the brother part and rewrite in your own words. -->

**Goal:** After discovering Fable 5 easily creates 3d models, I wanted to test it out. I took one real apartment (my parents' home), created a 3d model of it and rebuilt it three times, each time with a newer model. The first result was quite impressive and fun to create so I want to keep doing the same with all new models. I want to see how much better do AI models get at turning a real apartment into a 3D model (sometimes in just a few months).

**Input every time:** the floor plan (very basic) and around 25 photos of the rooms. I left the address and the floor plan out of this page on purpose.

I got guidance on this from my brother who is a tech engineer. Round 3 used a toolkit he put together for Claude Code.

---

### Try it yourself

- **[Round 1 in 3D (Fable 5, July)](https://claude.ai/artifact/G5kgYgDm56qwGTLdSSsH7w)**: drag to look around, room buttons on the left
- **[Round 2 in 3D (GPT-6 Astra, September)](https://claude.ai/artifact/DgagVXnPVq53nVFKwBR2Qf)**: walk around with W/A/S/D or the arrow buttons
- Round 3 in 3D: coming soon. It runs in Unreal Engine, so for now there are pictures below.

---

### Same living room, three rounds

![The same living room in Round 1, 2 and 3](E4_three-rounds_living-room.jpg)

| | Round 1 | Round 2 | Round 3 |
|---|---|---|---|
| **When** | July 2026 | September 2026 | November 2026 |
| **Model** | Claude Fable 5 | GPT-6 Astra | Claude Fable 5.2 |
| **How** | simple prompt to Claude code: "here are images and a floor plan of an apartment please create a 3d model for me." | prompt to codex: " using blender mcp build a beautiful visual 3d model of this home  and make it hyperrealsitic and accurate.  jpg. then host it on some url so i could fly and move around the render. make it first person view."| prompt 1: 
please create a hyperrealistic 3D model of this home. Look at the files and understand the struckture of this home. 
Please use ../../3d toolkit for building it -  please use blender to model it and use unreal engine to make it real. Ensure to do proper AAA tier modelling - normal maps, lighting etc. Ensure the model has both fly around and first person view mode. no need for any clicking between rooms, just an exploration tool. "
 |
| **What I saw** | right layout, but looks like a video game | massive step towards realism, but I noticed many random things and little mistakes | another level, the "wow" moment |

**Round 1:** the layout was right: sofa on the left, dining table by the window, TV on the wall. But everything is flat colours and akward shapes, and part of the wall is missing so you see the sky.

**Round 2:** going from Round 1 to 2 was a massive step towards realism. Real materials and light bouncing off the walls. But I also noticed way more random things.

**Round 3:** another level. Soft light, a real view outside, the wallpapers look like the real ones and many other little details, it even wrote the right month in the calendar and didn't miss details on home electromins,also the mirrors work.

![Round 3 rooms](E4_round3_rooms.jpg)

---

### What I learned

- **It's not only the model.** Each round I changed two things at once: the model and the prompt. So I can't say "Fable 5.2 is X times better than Fable 5". I can say the whole setup got much better.
- **More realism brings new mistakes.** Round 1 was simple, so it had a few weird things. Round 2 looked much more real, but more random things popped up.
- **The layout was right from the start.** Even Round 1 put the furniture in the right places. The big jumps were in light and materials.

### What I'd still fix

- The view outside the windows is generic. I want to use Google Maps / street view so it shows the real surroundings.
- More lived-in details: clothes, the things my parents actually have around.
- Some wallpapers repeat like a pattern from a game.

### Next I'd try

- Get Round 3 working as a 3D page too, so all three rounds can be explored in the browser.
- A screenshot from the Round 3 model is exactly the kind of input an architect gives a renderer. I want to put it through my Experiment 3 setup and see how much geometry survives.

[← Back to the front page](README.md)
