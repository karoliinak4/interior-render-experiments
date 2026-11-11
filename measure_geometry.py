"""
measure_geometry.py

How much of my sketch survives in an AI render?

For every line in my sketch, the script checks if the render has an edge
close to it. The result is a percentage: "sketch lines kept".
100% = every sketch line has a matching edge in the render.

How to run it:
    python measure_geometry.py my_sketch.jpg render1.png render2.png ...

Only makes sense when the render was made FROM the sketch (so the camera
view is the same). For two images with different cameras it gives
misleading numbers.
"""

import sys

import cv2          # OpenCV: a library for working with images
import numpy as np  # NumPy: a library for working with numbers in bulk

# --- Settings -------------------------------------------------------------

# All images get resized to this size first, so the comparison is fair.
# (My first comparison was unfair because the images had different sizes.)
WIDTH, HEIGHT = 1120, 840

# How close a render edge must be to count as "matching" a sketch line,
# as a share of the image width. 0.008 x 1120 = about 8 pixels.
TOLERANCE = 0.008

# The MyArchitectAI watermark sits in the bottom-right corner.
# We ignore that corner so the watermark doesn't count.
IGNORE_BOTTOM_RIGHT = (0.86, 0.72)  # from 86% down and 72% across


def sketch_lines(sketch_path):
    """Find the drawn lines in my sketch (dark pixels on white paper)."""
    sketch = cv2.imread(sketch_path, cv2.IMREAD_GRAYSCALE)  # load as black & white
    sketch = cv2.resize(sketch, (WIDTH, HEIGHT))            # same size as the renders
    lines = sketch < 120                                    # dark pixel = part of a line

    # switch off the watermark corner
    top = int(HEIGHT * IGNORE_BOTTOM_RIGHT[0])
    left = int(WIDTH * IGNORE_BOTTOM_RIGHT[1])
    lines[top:, left:] = False
    return lines


def render_edges(render_path):
    """Find the edges in the render: places where brightness changes sharply."""
    render = cv2.imread(render_path, cv2.IMREAD_GRAYSCALE)
    render = cv2.resize(render, (WIDTH, HEIGHT), interpolation=cv2.INTER_AREA)
    render = cv2.GaussianBlur(render, (5, 5), 0)  # soften tiny noise first
    edges = cv2.Canny(render, 50, 150)             # the Canny edge detector
    return edges > 0


def lines_kept(lines, edges):
    """What share of my sketch lines has a render edge nearby?"""
    radius = max(3, int(WIDTH * TOLERANCE))
    # "Grow" every edge by the radius, so a line counts as matched
    # if an edge is within that distance (not only on the exact pixel).
    kernel = np.ones((2 * radius + 1, 2 * radius + 1), np.uint8)
    near_an_edge = cv2.dilate(edges.astype(np.uint8), kernel) > 0

    matched = (lines & near_an_edge).sum()  # sketch pixels with an edge nearby
    total = lines.sum()                     # all sketch pixels
    return 100 * matched / total


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python measure_geometry.py sketch.jpg render1.png [render2.png ...]")
        sys.exit(1)

    sketch_path, render_paths = sys.argv[1], sys.argv[2:]
    lines = sketch_lines(sketch_path)

    print(f"{'render':45} sketch lines kept")
    for path in render_paths:
        score = lines_kept(lines, render_edges(path))
        print(f"{path:45} {score:5.1f}%")
