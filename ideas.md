# Features

## Scheduler
Basically Charlemagne's scheduler, but with more features, namely randomized loadouts/teams and more supported activities.

- Schedule Crucible and Gambit matches
  - "Me and my friends want to have a fun time by suffering with randomized crucible loadouts"
  - Randomized teams
- Schedule Nightfalls and other non-Raid PvE activities
- Randomized loadouts (for all activities...sadistic Nightfalls? :sweat_smile:)
  - Raids, Nightfalls, Crucible, Gambit
  - weapons, mods, subclasses, classes, aspects/fragments
- Random activity
  - for when you're bored and no one wants to pick something to do

## Raid report
Nice clean "Raid report" for a given user.

Each raid (/w name + image of raid):
    # of full clears
    fastest time
    date of last clear
    kills
    deaths
    badges (as images?): flawless, week1, day1, solo, duo, trio, combos of these

## Raid stats

### User raid stats
user's overall full clears count
user's overall full clears rank
user's overall clear count (full + checkpointed)
average full clear time across all raids
date of first raid ever attempted (include legacy)
date of first raid ever completed (include legacy)
date of latest raid completion (any raid)
date of latest raid attempt (any raid)

### Aggregate raid info
Contest mode/Day1
    Who got world's first: users, clans
    # of teams that completed
    # of players that completed
    # of teams that attempted
    # of players that attempted
    breakdown by encounter
    (refer to stats from the various post-day1 TWABs)
    Picture of contest mode emblem

Overall for a raid
    Total # of clears by all players
    # of players that completed
    # of teams that completed
    # of players that attempted
    # of unique clans
    # of clears by time range: last day/week/month/year
        filter to specific date/time ranges
        average per minute/hour/day/week for given time range
        max/min per minute/hour/day/week for given time range
        nice fancy graph plots visualizations
    # of attempts vs # of clears (success rate)
    max/min/average time for completion /w selectable time ranges
    per-encounter stats breakdown (same stat features as above, but for each encounter)
    breakdown by player region? (e.g. NA vs EU vs Oceania)
    classes and subclasses
    weapons and mods
        would be cool to see dominance of various metas over the years, e.g. LFR meta from Season of the Lost or warmind cells from Worthy/Arrivals
    top players/clans

All raids
    # of completions
    # of player/team attempts
    # of player/team clears
    # of unique clans
    top players/clans
    top raids
    Summary table with some high-level stats for each raid (e.g. # of clears, # of unique players, release date)

## Crucible and Gambit stats
get some inspiration from DestinyTracker, Trials Report.
breakdown by map
weapons, mods, classes/subclasses/aspects/fragments

## Emblems
Top emblems
Rarity
Most equipped?
breakdown by trackers that can be applied? "give me all emblems that can have a raid tracker applied"
other stats?




# Architecture/Design
MongoDB for static data.
Elasticsearch for caching data and performing aggregations and queries.

Need to design a index data model for various things, like raid stats. Get what we can from bungo API, make some inferences, maybe some stuff from other APIs (like raid report). then do queries against the data in elastic to do things like counts.
