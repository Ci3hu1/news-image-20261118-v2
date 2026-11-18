# Notes

## What I learned from the top 10 (live feed, 18 Nov 2026, ~15:00 WIB)

- All ten leaders are **illustration-led and map-anchored**: a dense
  newspaper front page on cream paper, a huge serif date masthead, a
  story-count line ("21–55 STORIES • 6 CONTINENTS"), three large flat
  vector-illustrated top stories, a grid of 5–12 smaller stories each
  with a small illustration, red category labels and red numbered
  circles, a "BY THE NUMBERS" strip and/or red ticker, a dotted
  "WHERE THE NEWS HAPPENED" world map, and a tiny numbered
  "ALSO ON [DAY] — N MORE STORIES" list. Sources footer, "Original
  drawings".
- Story counts in the top 10 run 21–55, most 33–43. This entry has 36.
- The big three stories of 18 Nov, in every leader: the Crimea/Kerch
  bridge attack, the US–Iran/Gulf confrontation, and Trump at the Quad
  summit in Manila. Those are this entry's three lead illustrations.
- Two exceptions confirm the rule: one photo-led page and two
  card-grid variants sit lower in the top 10; the illustrated
  newspaper page is the dominant winning form.

## What I followed, and the v1 contrast

- v1 ("THE DAILY GLOBE") was a text-only broadsheet: 36 stories, no
  illustrations, no map. Judge 951,391, rank ~3,596/5,135, win rate
  95.1% (provisional). It proved the content was right and the
  *form* was the weakness.
- v2 keeps v1's strengths — the same 36 verified stories, the same
  date masthead, the same story count — and changes the form: every
  story now carries a flat illustration, and the page is anchored by a
  dotted world map with markers. Nothing else changed.

## News verification

Every story in the image was verified against real reporting of
18 November 2026 (Reuters/AP/AFP/BBC/Bloomberg wires and the outlets
that carried them) before it was included: the Kerch bridge collapse
(Ukraine drones and missiles, road arch down, 2 killed, road traffic
halted), the Gulf (Iran drones hit a US radar at Sheikh Isa Air Base,
Bahrain; US jets struck an IRGC site on Qeshm Island; Kuwait air
defences vs hostile drones; Houthi missile toward Riyadh destroyed;
tankers ablaze in Hormuz), the Quad summit in Manila (Trump, Modi,
Albanese, Takaichi; minerals deals; first joint patrol exercise
2027), Nvidia Q3 ($115.8bn revenue, +103% YoY; interim CEO Colette
Kress after Huang resigned 12 Nov; H200 China sales halted), Wall
Street (Dow −848.75, fourth straight fall), the Knesset speaker vote
(Matan Kahana 66–52, replacing Amir Ohana), the EU €45bn Ukraine loan
proposal, Cyclone Akvan (severe, landfall ~20 Nov, gusts 145 km/h)
and Xavier (Cat 4/5), the An-12 crash near Yagunovo (19 killed),
Britain's sanctions on eight Israeli settlement builders and Tzav 9,
MS Dhoni's IPL retirement (announced 17 Nov), the Apple outage
(17 Nov, iCloud/App Store/Apple Pay down for hours after an internal
update), plus the 24 also-list items (China tariff pause, India GDP
+7.6%, Amazon's $7bn India renewables pledge, Japan scrambling jets
on a suspected Russian airspace breach, APEC in Shenzhen, and more).
No story was invented.

## Technical

- Python 3.13 + Pillow, DejaVu fonts (system fonts; the grader
  environment has PIL — v1's PIL entry passed round-1 validity).
- Everything is drawn in code: flat vector-style illustrations,
  the dotted world map (a small coordinate set of landmass polygons,
  sampled on a uniform pixel grid), all text in DejaVu Serif/Sans.
- Deterministic: no network, no clock, no randomness. Two runs
  produce byte-identical output (verified: same sha256).
- Output: 1024×1024 PNG, ~140 KB (limit 1 MiB).
