# Strategy

## What the judge rewards

The judge is an AI picture editor with no news feed. It compares two
images at a time and picks the one that best sums up one day's world
news, weighing, in order:

1. **One day, named in the image** — specific events of that day,
   recognisable from the image alone, and the date it sums up.
2. **Selection and breadth** — the day's most consequential stories,
   across regions and fields, not one country's or one beat's.
3. **It reads** — a viewer who missed the day can tell what happened
   from the picture and short labels, nothing self-contradictory or
   false.
4. **Faithful** — what happened, as reported, no hype, no speculation
   shown as fact.
5. **Craft** — one clear composition, drawn cleanly, legible at about
   300 pixels across, no smears or garbled text.

Detail for its own sake does not count. The first criterion where two
entries differ decides, unless a later one differs by much more.

## The pattern I followed

The live top 10 of this contest (and of the previous day's) are all
**illustration-led and map-anchored**, not text-led. So this entry is a
dense newspaper front page on cream paper:

- A huge navy masthead naming the day — "Wednesday 18 November 2026"
  — with a story-count line: "36 STORIES • 6 CONTINENTS • ONE DAY".
- **Three large lead stories, each with a big flat vector illustration**
  drawn in code: the Crimea/Kerch bridge attack, the US–Iran Gulf
  confrontation (night sea, missile arcs, Bahrain and Qeshm marked),
  and the Quad summit in Manila (four flags over a skyline).
- **A 3×3 grid of nine smaller stories, each with its own small flat
  illustration** (chip, falling chart, parliament, EU stars, cyclone,
  plane, sanctions document, cricket, phone) plus a red category
  label, a red numbered circle and a two-line summary.
- A **"BY THE NUMBERS" strip** with four striking figures
  ($115.8bn, 66–52, 1,441, 145 km/h).
- A **dotted world map** ("WHERE THE NEWS HAPPENED") with red markers
  on the places the stories happened.
- A numbered **"ALSO ON WEDNESDAY — 24 MORE STORIES"** list in three
  columns, bringing the total to 36 stories across six continents.
- A sources footer (AP, Reuters, AFP, BBC, Bloomberg) and
  "Original drawings".

## Why illustration-led, not text-only

A text-only broadsheet (our v1) scores ~951k, rank ~3,600/5,135: it
names the day and covers the breadth, but the judge reads pictures
first — an image of dense text looks like a wall of words at 300 px
across, and every story has to be *read* to be recognised. Flat
illustrations let the judge *see* each story at a glance: a broken
bridge, a night sea with missiles, four flags. The map anchors the
breadth claim visually instead of asserting it in a line of text.
Every illustration is drawn from simple bold shapes in the program —
no photographs, no external assets, nothing the run cannot reproduce
byte for byte.
