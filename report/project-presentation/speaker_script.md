# CSI 5137 — Speaker script and delivery plan

**Deck:** Testing databases without an answer key. 36 main slides; 6 backup slides. Student course project, not an official university presentation.

## Timing model — estimate, not a stopwatch guarantee

The main-route count includes spoken prose only. Cues, titles, citations and backup answers are excluded. English words are counted by the regular expression in `source/build_deck.py`; contractions/hyphenated compounds count as one. SQL is explained, not read token by token.

For each main slide: `seconds = 60 × spoken words / 120 + explicit silent hold + 1 second to advance`. The last main slide has no advance allowance. Gestures and gaze changes happen during speech and are not double-counted. Ordinary phrasing is absorbed into the gross speaking-rate assumption; the extra holds below are intentionally silent.

The 120-wpm planning rate is an authored choice. Microsoft suggests a broad 100–165-wpm range, while Trent recommends roughly 100–120 for formal delivery. Neither source guarantees a duration for this talk. Exact holds of 2–4 seconds are reading/rehearsal choices, not scientifically optimal constants.

## Cue conventions

- `[SHOW]`: direct attention to content already visible. No hidden object animations are required.
- `[PAUSE Ns]`: deliberate silence; do not fill it with extra commentary.
- `[LOOK]`, `[GESTURE]`, `[MOVE]`: optional delivery guidance, performed during speech unless inside the marked pause. Stay seated or at a lectern when appropriate; movement is not mandatory.
- `[NEXT]`: advance once at the end of the slide. Slides 6–8, 17–19 and 24–27 form progressive visual sequences. Do not click midway through a sentence.

## Rehearsal procedure

Record a two-minute representative method section, including its prescribed pauses. Calculate actual spoken wpm using the transcript and subtract only the explicit holds from the recording time. Rehearse the full talk next; a formula is not a substitute. Aim to finish the main route at roughly 23–24 minutes and use the remaining time for recovery or questions. If your pace is nearer 110 wpm, shorten the script before presenting; do not simply rush the technical parts.

Use natural pauses and meaningful gestures rather than acting every instruction. Point briefly, return your gaze to the audience, and move only at the four section changes. No continuous pacing, laser-pointer circling, or turning your back to read slides. For remote delivery, remain seated and gesture within camera view.

## Main-route checkpoints

- End of Opening: **02:14** (model).
- End of Coddtest: **07:05** (model).
- End of Ddlcheck: **12:01** (model).
- End of Writecheck: **17:36** (model).
- End of Radar: **19:49** (model).
- End of Synthesis: **22:13** (model).

**Main-route total: 2,400 spoken words + 98s explicit silence + 35s transitions = 22:13 at 120 wpm.**
**Remaining to 25:00: 02:47.** This is contingency, not a promise of exact delivery.

| Assumed speaking rate | Model duration |
|---|---|
| 110 wpm | 24:02 |
| 115 wpm | 23:05 |
| 120 wpm | 22:13 |
| 125 wpm | 21:25 |
| 130 wpm | 20:41 |

If the 25 minutes must include a full question period, shorten the main route further. The current reserve is not a five-minute Q&A allocation.

## Main script


### 01 · Testing databases without an answer key

**00:00–00:37 · 68 spoken words · 2s silent hold**

[PACE] 120 wpm. [SHOW] Four papers; one oracle problem.

[LOOK]Briefly check the highlighted element, then return your gaze to the audience.
[GESTURE] Hands relaxed; a small emphasis gesture is enough.
[MOVE] Stay in place; do not pace.
[DELIVERY] Stand beside the screen, hands relaxed. Look at the centre of the room before starting. No pacing.

A database can finish a query successfully and still give the wrong answer. This project compares four papers that turn that problem into something testable. Instead of predicting every answer, they construct another execution whose result should agree.

**[PAUSE 2s]** Let the audience read or compare the visual.

We will move from expressions, to schema histories, to transactions, and to metadata. For each paper, I will explain the method, examine the evidence, and show a small MySQL example.

**[NEXT]** Advance once.

Sources: [C], [D], [W], [A]. See the reference list below.


### 02 · A plausible answer is not an answer key

**00:37–01:08 · 54 spoken words · 3s silent hold**

[PACE] 120 wpm. [SHOW] Wrong answers can look normal.

[LOOK]Briefly check the highlighted element, then return your gaze to the audience.
[GESTURE] Hands relaxed; a small emphasis gesture is enough.
[MOVE] Stay in place; do not pace.
[DELIVERY] SHOW the large number. LOOK at the audience while asking the question. Hold the silence; do not answer immediately.

Imagine that a query returns forty two. The automated tester needs a rule for deciding whether the result is correct. That rule is called a test oracle.

**[PAUSE 3s]** Let the audience read or compare the visual.

Maintaining a second, fully independent implementation of every SQL feature is expensive. These papers instead look for consistency relations that can be checked using the database itself.

**[NEXT]** Advance once.

Sources: [C], [D], [W]. See the reference list below.


### 03 · Compare executions, not guesses

**01:08–01:38 · 55 spoken words · 2s silent hold**

[PACE] 120 wpm. [SHOW] A consistency oracle is not a proof of correctness.

[LOOK]Briefly check the highlighted element, then return your gaze to the audience.
[GESTURE] One open-hand contrast or one directional trace; then return to neutral.
[MOVE] Stay in place; do not pace.
[DELIVERY] Trace the upper path once, then the lower path with an open hand. Return your gaze to the room before explaining the comparison.

Construct a related execution, changing one aspect while preserving the semantics that matter. Run both and compare their observations. A disagreement is a candidate bug because the relation says those observations should match.

**[PAUSE 2s]** Let the audience read or compare the visual.

Agreement does not prove correctness: both executions might make the same mistake. And a disagreement can come from a bad equivalence assumption.

**[NEXT]** Advance once.

Sources: [C], [D], [W]. See the reference list below.


### 04 · One question, four layers

**01:38–02:14 · 66 spoken words · 2s silent hold**

[PACE] 120 wpm. [SHOW] Expression → schema history → transaction schedule.

[LOOK]Briefly check the highlighted element, then return your gaze to the audience.
[GESTURE] One open-hand contrast or one directional trace; then return to neutral.
[MOVE] Stay in place; do not pace.
[DELIVERY] GESTURE to the three rows in sequence. Make one small step at the transition to CODDTest, then settle.

The four papers change different objects. CODDTest changes an expression using values already computed by the database. DDLCheck changes the history used to construct a schema. WriteCheck changes a transaction schedule and compares the resulting writes. Radar removes metadata and compares query results.

**[PAUSE 2s]** Let the audience read or compare the visual.

This is our organising question: what changes, what must stay equivalent, and what do we compare? The methods are related, but not interchangeable.

**[NEXT]** Advance once.

Sources: [C], [D], [W]. See the reference list below.


### 05 · Evaluate. Substitute. Compare.

**02:14–02:50 · 65 spoken words · 2s silent hold**

[PACE] 120 wpm. [SHOW] A compiler transformation becomes a test oracle.

[LOOK]Briefly check the highlighted element, then return your gaze to the audience.
[GESTURE] Hands relaxed; a small emphasis gesture is enough.
[MOVE] Optional single position change at this section boundary; then stand still. Stay seated if appropriate.
[DELIVERY] Introduce the full paper verbally; do not read the entire subtitle. Use three small beats for the three verbs.

CODDTest, by Chi Zhang and Manuel Rigger, appeared in the twenty twenty five SIGMOD issue of PACMMOD. Its insight comes from compiler optimisations: constant folding and constant propagation.

**[PAUSE 2s]** Let the audience read or compare the visual.

The method evaluates an expression through an auxiliary query, constructs a version using its value, and checks whether the original and transformed queries agree. Subqueries are especially useful here because earlier predicate based oracles can miss them.

**[NEXT]** Advance once.

Sources: [C]. See the reference list below.


### 06 · 1 / Begin with the original query

**02:50–03:26 · 65 spoken words · 3s silent hold**

[PACE] 120 wpm. [SHOW] Toy example; the highlighted expression is the transformation target.

[LOOK]Briefly check the highlighted element, then return your gaze to the audience.
[GESTURE] One open-hand contrast or one directional trace; then return to neutral.
[MOVE] Stay in place; do not pace.
[DELIVERY] SHOW the two small tables, then POINT once to the highlighted subquery. Give the audience time to read it; do not read every SQL token.

Here is an illustrative example, not a bug report. Table t contains ten, thirty, and sixty. Table s contains ten and thirty. The query keeps values from t that are greater than the average of s. We have highlighted just the subquery that will be transformed.

**[PAUSE 3s]** Let the audience read or compare the visual.

The tester is not comparing arbitrary rewrites. It relates an expression to its value in the current database state.

**[NEXT]** Advance once.

Sources: [C]. See the reference list below.


### 07 · 2 / Ask the database for its value

**03:26–04:04 · 68 spoken words · 2s silent hold**

[PACE] 120 wpm. [SHOW] The auxiliary query supplies the substitution value.

[LOOK]Briefly check the highlighted element, then return your gaze to the audience.
[GESTURE] One open-hand contrast or one directional trace; then return to neutral.
[MOVE] Stay in place; do not pace.
[DELIVERY] Keep your position. POINT from s to twenty, then face the audience. Let the stable layout carry the transition.

The auxiliary query evaluates the average. Ten and thirty average to twenty. The subquery is independent of the current row in t, so a single value can represent it throughout the original query.

**[PAUSE 2s]** Let the audience read or compare the visual.

Notice what we did not build: a separate SQL interpreter. We used the system under test to obtain the value. The comparison then relies on running the computation in different contexts to expose inconsistent behaviour.

**[NEXT]** Advance once.

Sources: [C]. See the reference list below.


### 08 · 3 / Substitute and compare

**04:04–04:34 · 52 spoken words · 3s silent hold**

[PACE] 120 wpm. [SHOW] Same state + valid substitution → equal result.

[LOOK]Briefly check the highlighted element, then return your gaze to the audience.
[GESTURE] One open-hand contrast or one directional trace; then return to neutral.
[MOVE] Stay in place; do not pace.
[DELIVERY] Open your palms toward the two result columns. Pause before saying that this example agrees. NEXT only after the final sentence.

Now replace the subquery with twenty. Both versions should return thirty and sixty. CODDTest repeatedly generates such comparisons.

**[PAUSE 3s]** Let the audience read or compare the visual.

The relation is conditional. The database state must remain unchanged between evaluations, and the replacement must preserve the relevant value and type behaviour. Then a mismatch becomes a focused report: one expression behaved inconsistently.

**[NEXT]** Advance once.

Sources: [C]. See the reference list below.


### 09 · A row-dependent value is not one constant

**04:34–05:17 · 79 spoken words · 3s silent hold**

[PACE] 120 wpm. [SHOW] Dependent expressions need a mapping, not a global constant.

[LOOK]Briefly check the highlighted element, then return your gaze to the audience.
[GESTURE] One open-hand contrast or one directional trace; then return to neutral.
[MOVE] Stay in place; do not pace.
[DELIVERY] SHOW the two different outputs. Contrast them with two hands, then lower your hands for the qualification. Emphasise “invalid test”.

There is an important wrinkle. If the expression contains a column from the current row, its value can vary. Here, b plus five is twelve in one row and seventeen in another. Replacing every occurrence with twelve would be an invalid test, not a database bug.

**[PAUSE 3s]** Let the audience read or compare the visual.

CODDTest handles dependent expressions by recording a mapping from the relevant input values to the evaluated result, represented with a case expression. It must preserve row dependence, null behaviour, and data type semantics.

**[NEXT]** Advance once.

Sources: [C]. See the reference list below.


### 10 · The real bug: the value is still 1

**05:17–05:50 · 59 spoken words · 3s silent hold**

[PACE] 120 wpm. [SHOW] The highlighted fragment is not a standalone bug trigger.

[LOOK]Briefly check the highlighted element, then return your gaze to the audience.
[GESTURE] One open-hand contrast or one directional trace; then return to neutral.
[MOVE] Stay in place; do not pace.
[DELIVERY] POINT to MIN and then the value one. Explicitly gesture to the “fragment only” caption so the audience does not mistake this for the full reproducer.

Our real example is MySQL bug one one one two four one. The table contains a single true value, represented numerically as one. The transformed query substitutes that one for the subquery result.

**[PAUSE 3s]** Let the audience read or compare the visual.

The complete test also contains a surrounding regular expression, a like comparison, and a case expression, all unchanged. The membership fragment alone is not the reproducer.

**[NEXT]** Advance once.

Sources: [C], [R]. See the reference list below.


### 11 · Equivalent value. Different answer.

**05:50–06:28 · 65 spoken words · 4s silent hold**

[PACE] 120 wpm. [SHOW] Our replay demonstrates one concrete oracle violation.

[LOOK]Briefly check the highlighted element, then return your gaze to the audience.
[GESTURE] One open-hand contrast or one directional trace; then return to neutral.
[MOVE] Stay in place; do not pace.
[DELIVERY] SHOW the empty result first, then the row. Hold four seconds for visual comparison. LOOK back at the audience before interpreting it.

On our MySQL eight point zero point thirty two instance, the original subquery form returns no row. The constant form returns the row containing one.

**[PAUSE 4s]** Let the audience read or compare the visual.

This illustrates the paper’s oracle: changing the evaluation context reveals inconsistent behaviour. It is still a reproduction of a selected historical test case, not a rerun of the authors’ entire experiment or a claim that we independently discovered the bug.

**[NEXT]** Advance once.

Sources: [R]. See the reference list below.


### 12 · The paper tests more than one example

**06:28–07:05 · 66 spoken words · 3s silent hold**

[PACE] 120 wpm. [SHOW] Evidence for complementary coverage, not universal superiority.

[LOOK]Briefly check the highlighted element, then return your gaze to the audience.
[GESTURE] Hands relaxed; a small emphasis gesture is enough.
[MOVE] Stay in place; do not pace.
[DELIVERY] Read the three headline numbers slowly, from left to right. Do not infer percentages or sum unlike categories. Pause before the limitation.

The authors evaluated five database systems and reported forty five previously unknown bugs, including twenty four logic bugs. Their analysis found eleven of those logic bugs were not detected by the compared NoREC, TLP, and DQE oracles when applied to those cases.

**[PAUSE 3s]** Let the audience read or compare the visual.

That supports the claim of complementary coverage, not universal superiority. The contribution is broader oracle coverage, especially around subqueries, not simply more random queries.

**[NEXT]** Advance once.

Sources: [C]. See the reference list below.


### 13 · Can history change the answer?

**07:05–07:37 · 58 spoken words · 2s silent hold**

[PACE] 120 wpm. [SHOW] The schema history becomes the transformation target.

[LOOK]Briefly check the highlighted element, then return your gaze to the audience.
[GESTURE] Hands relaxed; a small emphasis gesture is enough.
[MOVE] Optional single position change at this section boundary; then stand still. Stay seated if appropriate.
[DELIVERY] Move once at the section change if space allows, then stop. Use “history” as the stressed word, not “database”.

DDLCheck moves outward, from an expression to an entire schema. It targets schema related logic bugs that can be difficult for query focused testing to reach.

**[PAUSE 2s]** Let the audience read or compare the visual.

Its question: should later operations differ merely because equivalent schemas were built differently? A rename, an alteration, or a dropped object can leave internal state that the visible schema does not reveal.

**[NEXT]** Advance once.

Sources: [D]. See the reference list below.


### 14 · Two histories. One intended schema.

**07:37–08:12 · 65 spoken words · 2s silent hold**

[PACE] 120 wpm. [SHOW] Equivalence includes constraints and relevant state.

[LOOK]Briefly check the highlighted element, then return your gaze to the audience.
[GESTURE] One open-hand contrast or one directional trace; then return to neutral.
[MOVE] Stay in place; do not pace.
[DELIVERY] Trace the upper history, then the lower path. Bring the two hands together at “equivalent”, without covering the projected content.

The upper path builds a schema through a longer sequence of creation and alteration operations. The lower path creates the equivalent final schema directly. The same subsequent workload is then applied to both.

**[PAUSE 2s]** Let the audience read or compare the visual.

Equivalent does not mean that the tables merely have the same column names. Constraints, indexes, types, and the relevant initial state must agree. That makes schema reconstruction part of the oracle itself.

**[NEXT]** Advance once.

Sources: [D]. See the reference list below.


### 15 · Reconstruct the state, then test it

**08:12–08:52 · 70 spoken words · 3s silent hold**

[PACE] 120 wpm. [SHOW] Generation → introspection → synthesis → comparison.

[LOOK]Briefly check the highlighted element, then return your gaze to the audience.
[GESTURE] One open-hand contrast or one directional trace; then return to neutral.
[MOVE] Stay in place; do not pace.
[DELIVERY] SHOW each stage with one deliberate sweep. Keep the explanation in pipeline order. Do not turn your back to read the labels.

The tool first generates a DDL sequence and executes it. It extracts information about the resulting schema, then synthesises a simpler sequence that recreates that schema in a second database. Finally, it applies matching data manipulation and query operations and compares their observable behaviour.

**[PAUSE 3s]** Let the audience read or compare the visual.

That lets the same workload probe whether the original sequence left inconsistent internal metadata. The tested object includes schema evolution, not just the final select statement.

**[NEXT]** Advance once.

Sources: [D]. See the reference list below.


### 16 · Spend tests on different histories

**08:52–09:26 · 62 spoken words · 2s silent hold**

[PACE] 120 wpm. [SHOW] A useful oracle still needs useful test inputs.

[LOOK]Briefly check the highlighted element, then return your gaze to the audience.
[GESTURE] One open-hand contrast or one directional trace; then return to neutral.
[MOVE] Stay in place; do not pace.
[DELIVERY] Contrast repeated branches on the left with distinct branches on the right. No extra body movement; the visual transition is enough.

The paper also addresses a practical problem: many generated DDL sequences are redundant. DDLCheck therefore includes sequence optimisation intended to improve the diversity and usefulness of the generated tests.

**[PAUSE 2s]** Let the audience read or compare the visual.

The authors evaluate this component with an ablation, rather than treating the generator as an invisible implementation detail. The oracle supplies the comparison, but the generator determines which internal states the comparison reaches.

**[NEXT]** Advance once.

Sources: [D]. See the reference list below.


### 17 · Before the rename, the relationship is simple

**09:26–10:12 · 84 spoken words · 3s silent hold**

[PACE] 120 wpm. [SHOW] The parent changes name, not its intended role.

[LOOK]Briefly check the highlighted element, then return your gaze to the audience.
[GESTURE] One open-hand contrast or one directional trace; then return to neutral.
[MOVE] Stay in place; do not pace.
[DELIVERY] POINT along the foreign-key arrow. Then indicate the rename statement. Keep the diagram visible during the reading hold.

In our reproduced case, a child table has a foreign key pointing to the parent table named t zero. The parent key is unique. The test then renames the parent to t two using the copy algorithm. That algorithm choice is part of this particular reproducer.

**[PAUSE 3s]** Let the audience read or compare the visual.

The intended relationship is unchanged: the child should still refer to the same parent, now under its new name. We are not changing the child’s logical requirement, only the path by which the schema reaches its final form.

**[NEXT]** Advance once.

Sources: [D], [R]. See the reference list below.


### 18 · The visible schema looks correct

**10:12–10:46 · 62 spoken words · 3s silent hold**

[PACE] 120 wpm. [SHOW] Visible metadata is not the whole internal state.

[LOOK]Briefly check the highlighted element, then return your gaze to the audience.
[GESTURE] One open-hand contrast or one directional trace; then return to neutral.
[MOVE] Stay in place; do not pace.
[DELIVERY] SHOW the updated arrow and parent row. Briefly point to the visible metadata label; then look to the room to set up the reveal.

After the rename, the visible schema says that the child references t two. We insert the value one into the parent. So an insert of one into the child should satisfy the foreign key.

**[PAUSE 3s]** Let the audience read or compare the visual.

But visible metadata is not necessarily the full internal state. DDLCheck’s second construction path gives us a control: create this final schema directly and perform the same inserts.

**[NEXT]** Advance once.

Sources: [D], [R]. See the reference list below.


### 19 · The old name survives in the behaviour

**10:46–11:26 · 70 spoken words · 4s silent hold**

[PACE] 120 wpm. [SHOW] Same intended schema; different observed behaviour.

[LOOK]Briefly check the highlighted element, then return your gaze to the audience.
[GESTURE] One open-hand contrast or one directional trace; then return to neutral.
[MOVE] Stay in place; do not pace.
[DELIVERY] Contrast ERROR and inserted row with open palms. Allow four seconds for the old-versus-new names. Avoid describing an unverified internal root cause beyond the stale-reference symptom.

The evolved schema rejects the child insert. Its error message still refers to the old parent name, t zero. Yet the directly constructed equivalent schema accepts the same insert. Our replay captures that contrast on the same MySQL version used for the expression example.

**[PAUSE 4s]** Let the audience read or compare the visual.

This is what makes the demonstration compelling: the schema presented to the user references one name, while the failing operation exposes a stale reference to another.

**[NEXT]** Advance once.

Sources: [D], [R]. See the reference list below.


### 20 · Schema testing reaches a different bug class

**11:26–12:01 · 61 spoken words · 3s silent hold**

[PACE] 120 wpm. [SHOW] Different test object, different coverage.

[LOOK]Briefly check the highlighted element, then return your gaze to the audience.
[GESTURE] Hands relaxed; a small emphasis gesture is enough.
[MOVE] Stay in place; do not pace.
[DELIVERY] SHOW the reported-to-confirmed progression. Explain the twenty-one plus eight breakdown verbally. Pause before the boundary statement.

Across six database systems, DDLCheck submitted thirty four reports. Twenty nine were confirmed as previously unknown bugs: twenty one schema related bugs and eight crashes. Nine had been fixed at the paper’s reporting point.

**[PAUSE 3s]** Let the audience read or compare the visual.

The contribution is targeted schema coverage, not evidence that schema testing subsumes query testing. Its boundary remains the ability to construct genuinely equivalent schemas and meaningful workloads.

**[NEXT]** Advance once.

Sources: [D]. See the reference list below.


### 21 · Change the schedule. Compare the writes.

**12:01–12:42 · 77 spoken words · 2s silent hold**

[PACE] 120 wpm. [SHOW] WSS has a scope; it is not arbitrary serializability.

[LOOK]Briefly check the highlighted element, then return your gaze to the audience.
[GESTURE] Hands relaxed; a small emphasis gesture is enough.
[MOVE] Optional single position change at this section boundary; then stand still. Stay seated if appropriate.
[DELIVERY] Make one optional section-change step, then stand still. Slow down for “write-specific serializability”.

WriteCheck, by Ziyu Cui and colleagues, is the third twenty twenty five paper. It asks whether a simpler property can expose important transaction bugs without checking every aspect of transaction semantics. The property is called write specific serializability, or WSS.

**[PAUSE 2s]** Let the audience read or compare the visual.

The focus is the final database state produced by writes. This is not a claim that every read committed execution must be fully serializable. The paper restricts the transactions being tested and defines the corresponding reference schedules.

**[NEXT]** Advance once.

Sources: [W]. See the reference list below.


### 22 · The write must not depend on an earlier read

**12:42–13:27 · 81 spoken words · 3s silent hold**

[PACE] 120 wpm. [SHOW] Scope is part of the correctness argument.

[LOOK]Briefly check the highlighted element, then return your gaze to the audience.
[GESTURE] One open-hand contrast or one directional trace; then return to neutral.
[MOVE] Stay in place; do not pace.
[DELIVERY] SHOW the in-scope and out-of-scope patterns. Use one contrast gesture. Emphasise “earlier, separate” to avoid implying that UPDATE cannot read rows.

The restriction concerns writes that depend on values obtained by earlier, separate read statements. Those application level read then compute then write patterns are outside the central setting. Reading a value inside the write statement itself is different; an update that increments a column can still be in scope.

**[PAUSE 3s]** Let the audience read or compare the visual.

This restriction lets the paper focus on write effects while tolerating some read differences. Without it, comparing final states to a serial execution could label legitimate weak isolation behaviour as a bug.

**[NEXT]** Advance once.

Sources: [W]. See the reference list below.


### 23 · Choose the reference schedule deliberately

**13:27–14:06 · 70 spoken words · 3s silent hold**

[PACE] 120 wpm. [SHOW] Corresponding serial order—not just any serial order.

[LOOK]Briefly check the highlighted element, then return your gaze to the audience.
[GESTURE] One open-hand contrast or one directional trace; then return to neutral.
[MOVE] Stay in place; do not pace.
[DELIVERY] Trace the observed finish order into the reference sequence. Then point to the comparison. Keep gestures concurrent with speech.

WriteCheck executes a concurrent schedule and observes how its transactions finish. It constructs a corresponding serial schedule using first commit or rollback, first scheduled. It then recreates the initial database, runs the reference, and compares the final states.

**[PAUSE 3s]** Let the audience read or compare the visual.

The paper defines transaction level and statement level variants, with different treatment of transaction boundaries and aborted work. The central contrast is concurrent write effects versus those of a carefully constructed reference.

**[NEXT]** Advance once.

Sources: [W]. See the reference list below.


### 24 · Two updates share three rows

**14:06–14:44 · 68 spoken words · 3s silent hold**

[PACE] 120 wpm. [SHOW] Simple SQL can have subtle concurrent behaviour.

[LOOK]Briefly check the highlighted element, then return your gaze to the audience.
[GESTURE] One open-hand contrast or one directional trace; then return to neutral.
[MOVE] Stay in place; do not pace.
[DELIVERY] SHOW a and b, then the two update statements. Do not read the entire table as a flat array. Hold while the audience links columns to writes.

Here is the historical MySQL case associated with our transaction demonstration. The initial rows contain null, two, and null in column a, with one, two, and three in column b. Transaction one sets every a value to ten. Transaction two sets b to twenty wherever a is true.

**[PAUSE 3s]** Let the audience read or compare the visual.

Both transactions use read committed isolation. We submit the second update while the first transaction still holds its changes uncommitted.

**[NEXT]** Advance once.

Sources: [R], [T]. See the reference list below.


### 25 · The second update waits

**14:44–15:22 · 69 spoken words · 3s silent hold**

[PACE] 120 wpm. [SHOW] A blocking event is part of the schedule, not a failed test.

[LOOK]Briefly check the highlighted element, then return your gaze to the audience.
[GESTURE] One open-hand contrast or one directional trace; then return to neutral.
[MOVE] Stay in place; do not pace.
[DELIVERY] Follow time downward with one hand. Stop the gesture at WAIT. Pause there before advancing; do not narrate the later commit yet.

Transaction one begins and executes its update, but does not commit yet. Transaction two begins and submits its update. The replay records that the second update blocks while transaction one is still active.

**[PAUSE 3s]** Let the audience read or compare the visual.

The wait indication is not the test crashing. It is the harness recording a blocked statement so the other transaction can continue. Next, transaction one commits, the blocked work resumes, and we inspect the final rows.

**[NEXT]** Advance once.

Sources: [R], [T]. See the reference list below.


### 26 · Resume, commit—and inspect the rows

**15:22–16:07 · 81 spoken words · 3s silent hold**

[PACE] 120 wpm. [SHOW] One unchanged b value is the observable symptom.

[LOOK]Briefly check the highlighted element, then return your gaze to the audience.
[GESTURE] One open-hand contrast or one directional trace; then return to neutral.
[MOVE] Stay in place; do not pace.
[DELIVERY] SHOW the commit, then the table. POINT once to the highlighted one. Face the audience while explaining why a reference is necessary.

Transaction one commits. The second update resumes, and transaction two commits. In the observed final state, every a value is ten, but the first row still has b equal to one. The other two rows have b equal to twenty.

**[PAUSE 3s]** Let the audience read or compare the visual.

The result looks ordinary until we compare it with a reference. The table is preferable to a flattened log array because it shows exactly which attribute differs. We have highlighted the first b value, not an entire transaction or every row.

**[NEXT]** Advance once.

Sources: [R], [T]. See the reference list below.


### 27 · The reference updates all three b values

**16:07–16:48 · 73 spoken words · 4s silent hold**

[PACE] 120 wpm. [SHOW] Observed mismatch; reference generated by Troc in our replay.

[LOOK]Briefly check the highlighted element, then return your gaze to the audience.
[GESTURE] One open-hand contrast or one directional trace; then return to neutral.
[MOVE] Stay in place; do not pace.
[DELIVERY] Contrast only the first b cell across the tables. Keep “Troc” visible and state the methodological distinction plainly. No celebratory gesture.

The Troc replay’s MVCC based oracle expects all three b values to be twenty. Its observed state retains one in the first row, so the harness reports an inconsistent final database state. A serial execution with transaction one before transaction two gives the same intuitive all twenty outcome.

**[PAUSE 4s]** Let the audience read or compare the visual.

Our recorded reference comes from Troc’s oracle; it is not a direct run of WriteCheck’s reference schedule generator. The two tools justify their comparisons differently.

**[NEXT]** Advance once.

Sources: [R], [T], [W]. See the reference list below.


### 28 · WSS finds bugs—and false positives

**16:48–17:36 · 88 spoken words · 3s silent hold**

[PACE] 120 wpm. [SHOW] Report the denominator and the false positives.

[LOOK]Briefly check the highlighted element, then return your gaze to the audience.
[GESTURE] Hands relaxed; a small emphasis gesture is enough.
[MOVE] Stay in place; do not pace.
[DELIVERY] Separate the historical-study numbers from the new-testing numbers. Pause before saying “false positives”. Do not combine these populations.

The paper first studies thirty five critical transaction bugs. Thirty two violate WSS. That is ninety one point four percent of this historical sample, not of all database bugs. In its testing campaign, WriteCheck reports twenty two unique violations and eleven confirmed new critical transaction bugs.

**[PAUSE 3s]** Let the audience read or compare the visual.

The table also includes nine false positives, highlighting differences in database design and semantics. The empirical claim is that a relatively simple write focused property catches many important cases in the studied setting, not that every reported discrepancy is automatically a defect.

**[NEXT]** Advance once.

Sources: [W]. See the reference list below.


### 29 · Radar: strip the metadata

**17:36–17:58 · 36 spoken words · 2s silent hold**

[PACE] 120 wpm. [SHOW] Fourth layer: metadata.

[LOOK]Briefly check the highlighted element, then return your gaze to the audience.
[GESTURE] Hands relaxed; a small emphasis gesture is enough.
[MOVE] Optional single position change at this section boundary; then stand still. Stay seated if appropriate.
[DELIVERY] Pause at the section slide; let the new layer register. Single position change, then stand still.

The fourth layer is metadata. Radar asks whether a database should answer a query the same way with or without its indexes and other metadata.

**[PAUSE 2s]** Let the audience read or compare the visual.

That turns a missing index into a control, not a shortcut.

**[NEXT]** Advance once.

Sources: [A]. See the reference list below.


### 30 · Same data. Strip the metadata.

**17:58–18:30 · 59 spoken words · 2s silent hold**

[PACE] 120 wpm. [SHOW] Same data, same query; only metadata differs.

[LOOK]Briefly check the highlighted element, then return your gaze to the audience.
[GESTURE] One open-hand contrast or one directional trace; then return to neutral.
[MOVE] Stay in place; do not pace.
[DELIVERY] Trace the two paths from the same data, then open your hand at the comparison.

Radar builds a raw copy of the database. It keeps the data but drops metadata such as indexes. The same query runs on both copies. Metadata may change the plan, but not the correct result, so a mismatch is a candidate bug.

**[PAUSE 2s]** Let the audience read or compare the visual.

The raw copy is the control. It is still the same DBMS, so agreement is not proof.

**[NEXT]** Advance once.

Sources: [A]. See the reference list below.


### 31 · Indexed: 1 row. Raw: 0 rows.

**18:30–19:14 · 81 spoken words · 3s silent hold**

[PACE] 120 wpm. [SHOW] Same data and query; the index changes the answer.

[LOOK]Briefly check the highlighted element, then return your gaze to the audience.
[GESTURE] Hands relaxed; a small emphasis gesture is enough.
[MOVE] Stay in place; do not pace.
[DELIVERY] SHOW the two columns. Hold three seconds on the two counts. Stress that the raw copy is the correct one.

On MySQL eight point zero point thirty two, we replayed bug one one zero one two five. Both databases hold table t zero with one DOUBLE ZEROFILL column and the value zero. Only the indexed copy adds a descending index on that column.

**[PAUSE 3s]** Let the audience read or compare the visual.

Data and query are identical. The indexed copy counts one matching row; the raw copy counts none. The raw result is correct, so the indexed answer is the bug. This is one replayed case, not Radar's own tool.

**[NEXT]** Advance once.

Sources: [R]. See the reference list below.


### 32 · Metadata guidance finds more bugs

**19:14–19:49 · 61 spoken words · 3s silent hold**

[PACE] 120 wpm. [SHOW] Evidence within one study, not a general rate.

[LOOK]Briefly check the highlighted element, then return your gaze to the audience.
[GESTURE] Hands relaxed; a small emphasis gesture is enough.
[MOVE] Stay in place; do not pace.
[DELIVERY] Read the pairs slowly. Pause before the limitation. Do not rank the DBMSs.

The authors report ablations. With metadata guidance, TiDB yields nineteen unique bugs in twelve hours, against twelve without. Across five systems the totals are twenty two against fourteen.

**[PAUSE 3s]** Let the audience read or compare the visual.

Developers confirmed thirty eight new bugs, thirty of them metadata related. This supports metadata diversity under a fixed budget. It does not show the gain holds for another generator or a patched version.

**[NEXT]** Advance once.

Sources: [A]. See the reference list below.


### 33 · Our replay is narrower than the papers

**19:49–20:23 · 62 spoken words · 2s silent hold**

[PACE] 120 wpm. [SHOW] Replayed bug symptoms ≠ replicated tool evaluation.

[LOOK]Briefly check the highlighted element, then return your gaze to the audience.
[GESTURE] Hands relaxed; a small emphasis gesture is enough.
[MOVE] Stay in place; do not pace.
[DELIVERY] Keep your hands relaxed. LOOK to the audience for this scope statement. No need to point at every checkmark or read file names.

Our project reproduced selected historical symptoms on one MySQL release. The query, schema, and metadata examples are small direct replays. For the transaction case, we used a pinned Troc artifact and preserved its observed and oracle outputs.

**[PAUSE 2s]** Let the audience read or compare the visual.

This gives us concrete examples and a reproducible teaching artifact, but it does not establish comparative coverage, discovery rates, or a full replication of WriteCheck.

**[NEXT]** Advance once.

Sources: [R], [T], [C], [D], [W], [A]. See the reference list below.


### 34 · The same pattern survives at every layer

**20:23–20:53 · 52 spoken words · 3s silent hold**

[PACE] 120 wpm. [SHOW] Same testing structure; complementary test surfaces.

[LOOK]Briefly check the highlighted element, then return your gaze to the audience.
[GESTURE] One open-hand contrast or one directional trace; then return to neutral.
[MOVE] Stay in place; do not pace.
[DELIVERY] Use one downward sweep over the rows, then turn fully to the audience for the complementary-coverage argument.

Now compare the papers directly. CODDTest changes an expression. DDLCheck changes the construction history. WriteCheck changes the schedule and compares write effects under its assumptions. Radar changes the metadata and compares query results.

**[PAUSE 3s]** Let the audience read or compare the visual.

An expression transformation does not necessarily visit schema evolution paths. Equivalent schema construction does not necessarily exercise transaction interleavings.

**[NEXT]** Advance once.

Sources: [C], [D], [W], [A]. See the reference list below.


### 35 · The difficult part is the equivalence claim

**20:53–21:36 · 78 spoken words · 3s silent hold**

[PACE] 120 wpm. [SHOW] The equivalence assumptions are part of the contribution.

[LOOK]Briefly check the highlighted element, then return your gaze to the audience.
[GESTURE] Hands relaxed; a small emphasis gesture is enough.
[MOVE] Stay in place; do not pace.
[DELIVERY] Give each assumption one verbal beat. End the list with hands lowered. Emphasise the equivalence assumptions rather than speeding through the limitations.

The critical question is not simply whether two outputs differ. For CODDTest, that means valid values, types, and row dependence. For DDLCheck, it means a faithful reconstruction of the schema and state. For WriteCheck, it means the right transaction restrictions and database semantics. For Radar, it means metadata that should not alter results.

**[PAUSE 3s]** Let the audience read or compare the visual.

A useful follow up study would examine which assumptions cause shared blind spots or false positives, rather than comparing raw bug totals as a leaderboard.

**[NEXT]** Advance once.

Sources: [C], [D], [W], [A]. See the reference list below.


### 36 · Specify what must stay the same

**21:36–22:13 · 70 spoken words · 2s silent hold**

[PACE] 120 wpm. [SHOW] A good oracle makes an expectation executable.

[LOOK]Briefly check the highlighted element, then return your gaze to the audience.
[GESTURE] Hands relaxed; a small emphasis gesture is enough.
[MOVE] Stay in place; do not pace.
[DELIVERY] Return to a neutral position. Look across the room for the four verbs. Hold after the four verbs, then deliver the closing thought. Stop—do not click into the appendix automatically.

The main takeaway is this: when predicting the answer is hard, specify what must stay the same. Substitute an expression. Reconstruct a schema. Reschedule transactions. Strip metadata. Then test the relation, while being explicit about its assumptions.

**[PAUSE 2s]** Let the audience read or compare the visual.

These four papers show how a compact correctness idea can reach deep implementation behaviour. Our MySQL replays make those ideas tangible, but the general lesson is the design of the oracle. Thank you.

**[STOP]** Invite questions. Do not enter the appendix automatically.

Sources: [C], [D], [W], [A], [R]. See the reference list below.


## Backup answers — outside the timed route


### 37 · The complete changing-predicate context

**Backup / outside timed route · 31 spoken words · 0s silent hold**

[PACE] 120 wpm. [SHOW] Full context matters.

[LOOK]Briefly check the highlighted element, then return your gaze to the audience.
[GESTURE] Hands relaxed; a small emphasis gesture is enough.
[MOVE] Stay in place; do not pace.
[DELIVERY] Use only if asked. Do not read every SQL token.

The membership fragment is not a standalone reproducer. These two predicate forms keep the regular expression, like comparison, and case expression unchanged. Refer to the repository script for an executable copy.

**[BACKUP]** Return to the discussion.

Sources: [C], [R]. See the reference list below.


### 38 · The foreign-key case in six lines

**Backup / outside timed route · 29 spoken words · 0s silent hold**

[PACE] 120 wpm. [SHOW] Same final schema; different construction.

[LOOK]Briefly check the highlighted element, then return your gaze to the audience.
[GESTURE] Hands relaxed; a small emphasis gesture is enough.
[MOVE] Stay in place; do not pace.
[DELIVERY] Point to ALGORITHM COPY; it is part of this case.

This is the compact schema-history sequence. The directly created control starts with the renamed parent table and skips the alteration. These statements are representative SQL from the reproduced case.

**[BACKUP]** Return to the discussion.

Sources: [D], [R]. See the reference list below.


### 39 · Two WSS variants—not full serializability

**Backup / outside timed route · 52 spoken words · 0s silent hold**

[PACE] 120 wpm. [SHOW] Keep the property, the generator and the harness distinct.

[LOOK]Briefly check the highlighted element, then return your gaze to the audience.
[GESTURE] Hands relaxed; a small emphasis gesture is enough.
[MOVE] Stay in place; do not pace.
[DELIVERY] Use the table to distinguish the property from the reference generator and from our Troc replay.

The paper defines transaction-level and statement-level WSS. The first compares with a corresponding serial transaction execution. The latter removes aborted transactions and transaction boundaries from committed work before the reference execution. These variants are not a statement that every read observation is serializable. Savepoint and rollback details require the paper’s full definitions.

**[BACKUP]** Return to the discussion.

Sources: [W]. See the reference list below.


### 40 · What the evaluations establish

**Backup / outside timed route · 53 spoken words · 0s silent hold**

[PACE] 120 wpm. [SHOW] Do not rank DBMS reliability from these totals.

[LOOK]Briefly check the highlighted element, then return your gaze to the audience.
[GESTURE] Hands relaxed; a small emphasis gesture is enough.
[MOVE] Stay in place; do not pace.
[DELIVERY] Answer the methodological question, rather than reading all the counts.

The reported bug totals measure different populations, tool scopes, and experiments. CODDTest compares other oracles on found cases; DDLCheck investigates schema coverage and a generator ablation; WriteCheck combines a historical study with new testing; Radar reports a TiDB and five-system ablation. Raw bug totals are not a reliability ranking of the tested databases.

**[BACKUP]** Return to the discussion.

Sources: [C], [D], [W], [A]. See the reference list below.


### 41 · Research sources

**Backup / outside timed route · 27 spoken words · 0s silent hold**

[PACE] 120 wpm. [SHOW] Primary papers and reproduction evidence are separate sources.

[LOOK]Briefly check the highlighted element, then return your gaze to the audience.
[GESTURE] Hands relaxed; a small emphasis gesture is enough.
[MOVE] Stay in place; do not pace.
[DELIVERY] Keep this slide available during questions.

These are the four primary papers, with links in the notes and in the project’s papers folder. Our evidence files and the Troc artifact are cited separately.

**[BACKUP]** Return to the discussion.

Sources: [C], [D], [W], [A], [R], [T]. See the reference list below.


### 42 · Delivery and visual-design sources

**Backup / outside timed route · 47 spoken words · 0s silent hold**

[PACE] 120 wpm. [SHOW] Model timing; measure actual delivery.

[LOOK]Briefly check the highlighted element, then return your gaze to the audience.
[GESTURE] Hands relaxed; a small emphasis gesture is enough.
[MOVE] Stay in place; do not pace.
[DELIVERY] Not a spoken main-route slide. Use the speaker script for calibration details.

The typography and palette follow uOttawa’s public Horizon guidance. The timing model counts the spoken words and adds explicit pauses and slide changes. The gesture and pause cues support comprehension; they are not a requirement to perform mechanically. A real rehearsal is needed to calibrate the duration.

**[BACKUP]** Return to the discussion.

Sources: [B], [P]. See the reference list below.


## Research and delivery references

[C] Chi Zhang and Manuel Rigger. Constant Optimization Driven Database System Testing. Proc. ACM Manag. Data 3(1), article 24, 2025. https://doi.org/10.1145/3709674 ; public preprint https://arxiv.org/abs/2501.11252

[D] Jiansen Song et al. Detecting Schema-Related Logic Bugs in Relational DBMSs via Equivalent Database Construction. PVLDB 18(7), 2281–2294, 2025. https://www.vldb.org/pvldb/vol18/p2281-song.pdf

[W] Ziyu Cui et al. Simple Testing Can Expose Most Critical Transaction Bugs: Understanding and Detecting Write-Specific Serializability Violations in Database Systems. PVLDB 18(8), 2547–2560, 2025. https://www.vldb.org/pvldb/vol18/p2547-cui.pdf

[A] Jiansen Song et al. Detecting Metadata-Related Logic Bugs in Database Systems via Raw Database Construction (Radar). PVLDB 17(8), 1884–1897, 2024. https://www.vldb.org/pvldb/vol17/p1884-song.pdf ; https://doi.org/10.14778/3659437.3659445

[R] Project evidence: results/coddtest_111241.txt, results/ddlcheck_114904.txt, results/writecheck_104833.txt, results/radar_110125.txt. MySQL 8.0.32, reproduced in the class project. The transaction replay uses Troc, not the WriteCheck implementation. https://github.com/seofernando25/csi5137-atdm-db-project.

[T] Troc artifact, pinned commit a6d50e3f596b356137d2f8c3c8b31a61bf7fe2c5. https://github.com/criszy/Troc ; case cases/mysql104833.txt. Also listed in WriteCheck/detected-bugs.md at https://github.com/tcse-iscas/WriteCheck .

[B] University of Ottawa, Horizon visual identity: https://www.uottawa.ca/about-us/administration-services/brand . Garnet #8F001A; charcoal #2D2D2C; polar grey #F2F2F2. Typography: Work Sans and Spectral. Logo source: https://www.uottawa.ca/themes/custom/uottawa/dist/assets/logo.png . Accessed 2026-09-28.

[P] Delivery guidance: Microsoft Speaker Coach https://support.microsoft.com/en-us/powerpoint/suggestions-from-speaker-coach ; Trent University Academic Skills https://www.trentu.ca/academicskills/how-guides/how-present-university-and-beyond/delivering-oral-presentation-public-speaking ; Toastmasters https://www.toastmasters.org/resources/public-speaking-tips/gestures-and-body-language . Accessed 2026-09-28. Exact pause lengths are authored rehearsal choices, not empirically optimal constants.
