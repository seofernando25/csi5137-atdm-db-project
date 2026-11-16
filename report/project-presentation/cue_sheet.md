# At-a-glance cue sheet

The full script is in `speaker_script.md`; these are prompts, not extra spoken words.

**01 · 00:00–00:37 · Testing databases without an answer key**
Four papers; one oracle problem.  | Silent hold: 2s
Delivery: Stand beside the screen, hands relaxed. Look at the centre of the room before starting. No pacing.

**02 · 00:37–01:16 · A plausible answer is not an answer key**
Wrong answers can look normal.  | Silent hold: 3s
Delivery: SHOW the large number. LOOK at the audience while asking the question. Hold the silence; do not answer immediately.

**03 · 01:16–01:56 · Compare executions, not guesses**
A consistency oracle is not a proof of correctness.  | Silent hold: 2s
Delivery: Trace the upper path once, then the lower path with an open hand. Return your gaze to the room before explaining the comparison.

**04 · 01:56–02:37 · One question, four layers**
Expression → schema history → transaction schedule.  | Silent hold: 2s
Delivery: GESTURE to the three rows in sequence. Make one small step at the transition to CODDTest, then settle.

**05 · 02:37–03:14 · Evaluate. Substitute. Compare.**
A compiler transformation becomes a test oracle.  | Silent hold: 2s
Delivery: Introduce the full paper verbally; do not read the entire subtitle. Use three small beats for the three verbs.

**06 · 03:14–03:56 · 1 / Begin with the original query**
Toy example; the highlighted expression is the transformation target.  | Silent hold: 3s
Delivery: SHOW the two small tables, then POINT once to the highlighted subquery. Give the audience time to read it; do not read every SQL token.

**07 · 03:56–04:38 · 2 / Ask the database for its value**
The auxiliary query supplies the substitution value.  | Silent hold: 2s
Delivery: Keep your position. POINT from s to twenty, then face the audience. Let the stable layout carry the transition.

**08 · 04:38–05:17 · 3 / Substitute and compare**
Same state + valid substitution → equal result.  | Silent hold: 3s
Delivery: Open your palms toward the two result columns. Pause before saying that this example agrees. NEXT only after the final sentence.

**09 · 05:17–06:00 · A row-dependent value is not one constant**
Dependent expressions need a mapping, not a global constant.  | Silent hold: 3s
Delivery: SHOW the two different outputs. Contrast them with two hands, then lower your hands for the qualification. Emphasise “invalid test”.

**10 · 06:00–06:39 · The real bug: the value is still 1**
The highlighted fragment is not a standalone bug trigger.  | Silent hold: 3s
Delivery: POINT to MIN and then the value one. Explicitly gesture to the “fragment only” caption so the audience does not mistake this for the full reproducer.

**11 · 06:39–07:23 · Equivalent value. Different answer.**
Our replay demonstrates one concrete oracle violation.  | Silent hold: 4s
Delivery: SHOW the empty result first, then the row. Hold four seconds for visual comparison. LOOK back at the audience before interpreting it.

**12 · 07:23–08:04 · The paper tests more than one example**
Evidence for complementary coverage, not universal superiority.  | Silent hold: 3s
Delivery: Read the three headline numbers slowly, from left to right. Do not infer percentages or sum unlike categories. Pause before the limitation.

**13 · 08:04–08:42 · Can history change the answer?**
The schema history becomes the transformation target.  | Silent hold: 2s
Delivery: Move once at the section change if space allows, then stop. Use “history” as the stressed word, not “database”.

**14 · 08:42–09:22 · Two histories. One intended schema.**
Equivalence includes constraints and relevant state.  | Silent hold: 2s
Delivery: Trace the upper history, then the lower path. Bring the two hands together at “equivalent”, without covering the projected content.

**15 · 09:22–10:10 · Reconstruct the state, then test it**
Generation → introspection → synthesis → comparison.  | Silent hold: 3s
Delivery: SHOW each stage with one deliberate sweep. Keep the explanation in pipeline order. Do not turn your back to read the labels.

**16 · 10:10–10:52 · Spend tests on different histories**
A useful oracle still needs useful test inputs.  | Silent hold: 2s
Delivery: Contrast repeated branches on the left with distinct branches on the right. No extra body movement; the visual transition is enough.

**17 · 10:52–11:38 · Before the rename, the relationship is simple**
The parent changes name, not its intended role.  | Silent hold: 3s
Delivery: POINT along the foreign-key arrow. Then indicate the rename statement. Keep the diagram visible during the reading hold.

**18 · 11:38–12:20 · The visible schema looks correct**
Visible metadata is not the whole internal state.  | Silent hold: 3s
Delivery: SHOW the updated arrow and parent row. Briefly point to the visible metadata label; then look to the room to set up the reveal.

**19 · 12:20–13:06 · The old name survives in the behaviour**
Same intended schema; different observed behaviour.  | Silent hold: 4s
Delivery: Contrast ERROR and inserted row with open palms. Allow four seconds for the old-versus-new names. Avoid describing an unverified internal root cause beyond the stale-reference symptom.

**20 · 13:06–13:50 · Schema testing reaches a different bug class**
Different test object, different coverage.  | Silent hold: 3s
Delivery: SHOW the reported-to-confirmed progression. Explain the twenty-one plus eight breakdown verbally. Pause before the boundary statement.

**21 · 13:50–14:32 · Change the schedule. Compare the writes.**
WSS has a scope; it is not arbitrary serializability.  | Silent hold: 2s
Delivery: Make one optional section-change step, then stand still. Slow down for “write-specific serializability”.

**22 · 14:32–15:20 · The write must not depend on an earlier read**
Scope is part of the correctness argument.  | Silent hold: 3s
Delivery: SHOW the in-scope and out-of-scope patterns. Use one contrast gesture. Emphasise “earlier, separate” to avoid implying that UPDATE cannot read rows.

**23 · 15:20–16:06 · Choose the reference schedule deliberately**
Corresponding serial order—not just any serial order.  | Silent hold: 3s
Delivery: Trace the observed finish order into the reference sequence. Then point to the comparison. Keep gestures concurrent with speech.

**24 · 16:06–16:50 · Two updates share three rows**
Simple SQL can have subtle concurrent behaviour.  | Silent hold: 3s
Delivery: SHOW a and b, then the two update statements. Do not read the entire table as a flat array. Hold while the audience links columns to writes.

**25 · 16:50–17:36 · The second update waits**
A blocking event is part of the schedule, not a failed test.  | Silent hold: 3s
Delivery: Follow time downward with one hand. Stop the gesture at WAIT. Pause there before advancing; do not narrate the later commit yet.

**26 · 17:36–18:20 · Resume, commit—and inspect the rows**
One unchanged b value is the observable symptom.  | Silent hold: 3s
Delivery: SHOW the commit, then the table. POINT once to the highlighted one. Face the audience while explaining why a reference is necessary.

**27 · 18:20–19:10 · The reference updates all three b values**
Observed mismatch; reference generated by Troc in our replay.  | Silent hold: 4s
Delivery: Contrast only the first b cell across the tables. Keep “Troc” visible and state the methodological distinction plainly. No celebratory gesture.

**28 · 19:10–20:02 · WSS finds bugs—and false positives**
Report the denominator and the false positives.  | Silent hold: 3s
Delivery: Separate the historical-study numbers from the new-testing numbers. Pause before saying “false positives”. Do not combine these populations.

**29 · 20:02–20:22 · Radar: strip the metadata**
Fourth layer: metadata.  | Silent hold: 2s
Delivery: Pause at the section slide; let the new layer register. Single position change, then stand still.

**30 · 20:22–20:58 · Same data. Strip the metadata.**
Same data, same query; only metadata differs.  | Silent hold: 2s
Delivery: Trace the two paths from the same data, then open your hand at the comparison.

**31 · 20:58–21:42 · Indexed: 1 row. Raw: 0 rows.**
Same data and query; the index changes the answer.  | Silent hold: 3s
Delivery: SHOW the two columns. Hold three seconds on the two counts. Stress that the raw copy is the correct one.

**32 · 21:42–22:16 · Metadata guidance finds more bugs**
Evidence within one study, not a general rate.  | Silent hold: 3s
Delivery: Read the pairs slowly. Pause before the limitation. Do not rank the DBMSs.

**33 · 22:16–22:50 · Our replay is narrower than the papers**
Replayed bug symptoms ≠ replicated tool evaluation.  | Silent hold: 2s
Delivery: Keep your hands relaxed. LOOK to the audience for this scope statement. No need to point at every checkmark or read file names.

**34 · 22:50–23:20 · The same pattern survives at every layer**
Same testing structure; complementary test surfaces.  | Silent hold: 3s
Delivery: Use one downward sweep over the rows, then turn fully to the audience for the complementary-coverage argument.

**35 · 23:20–24:10 · The difficult part is the equivalence claim**
The equivalence assumptions are part of the contribution.  | Silent hold: 3s
Delivery: Give each assumption one verbal beat. End the list with hands lowered. Emphasise the equivalence assumptions rather than speeding through the limitations.

**36 · 24:10–24:47 · Specify what must stay the same**
A good oracle makes an expectation executable.  | Silent hold: 2s
Delivery: Return to a neutral position. Look across the room for the four verbs. Hold after the four verbs, then deliver the closing thought. Stop—do not click into the appendix automatically.
