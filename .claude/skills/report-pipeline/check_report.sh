#!/usr/bin/env bash
# Automated gate for report/project1-latex. Prints PASS/WARN/FAIL lines; exits 1 on any FAIL.
# Usage: bash .claude/skills/report-pipeline/check_report.sh [--no-build]
set -u
ROOT="$(git -C "$(dirname "$0")" rev-parse --show-toplevel)"
DIR="$ROOT/report/project1-latex"
cd "$DIR" || exit 2
fail=0
say() { printf '%-5s %s\n' "$1" "$2"; [ "$1" = FAIL ] && fail=1; return 0; }

if [ "${1:-}" != "--no-build" ]; then
  if xelatex -interaction=nonstopmode -halt-on-error main.tex >/dev/null 2>&1 &&
     xelatex -interaction=nonstopmode -halt-on-error main.tex >/dev/null 2>&1; then
    say PASS "xelatex built main.pdf twice (exit 0)"
  else
    say FAIL "xelatex failed; see main.log: $(grep -m1 '^!' main.log)"
  fi
fi

pages=$(pdfinfo main.pdf | awk '/^Pages/{print $2}')
if [ "$pages" -ge 10 ] && [ "$pages" -le 20 ]; then say PASS "page count $pages (10-20)"; else say FAIL "page count $pages outside 10-20"; fi

grep -q '\\documentclass\[11pt' main.tex && say PASS "11 pt class option" || say FAIL "class option is not 11pt"
if pdffonts main.pdf | grep -q -E 'LiberationSerif|TimesNewRoman|Times-Roman'; then say PASS "Times-metric body font embedded"; else say FAIL "no Times-metric body font in PDF"; fi

und=$(grep -c -E 'undefined|Reference .* undefined|Citation .* undefined' main.log)
[ "$und" -eq 0 ] && say PASS "no undefined references or citations" || say FAIL "$und undefined reference/citation warnings"
multi=$(grep -c 'multiply defined' main.log)
[ "$multi" -eq 0 ] && say PASS "no duplicate labels" || say FAIL "duplicate labels: $(grep 'multiply defined' main.log | sed 's/.*Label .\(.*\). multiply.*/\1/' | sort -u | tr '\n' ' ')"
ovf=$(grep -c '^Overfull' main.log)
[ "$ovf" -eq 0 ] && say PASS "no overfull boxes" || say WARN "$ovf overfull boxes"

python3 - "$DIR" <<'PY'
import re, sys, pathlib
d = pathlib.Path(sys.argv[1])
src = "".join(f.read_text() for f in sorted(d.glob("*.tex")))
prose = "".join(f.read_text() for f in sorted(d.glob("*.tex")) if f.name not in ("main.tex", "refs.tex"))
fails = 0
def out(kind, msg):
    global fails
    print(f"{kind:<5} {msg}")
    fails += kind == "FAIL"

labels = re.findall(r"\\label\{([^}]+)\}", src)
refs = set(re.findall(r"\\(?:ref|autoref|cref|hyperref)\{([^}]+)\}|\\hyperref\[([^\]]+)\]", src)
           and sum((list(t) for t in re.findall(r"\\(?:ref|autoref|cref)\{([^}]+)\}|\\hyperref\[([^\]]+)\]", src)), []))
floats = [l for l in labels if l.split(":")[0] in ("fig", "tab", "alg")]
unref = [l for l in floats if l not in refs]
out("PASS" if not unref else "FAIL", "every float referenced in text" if not unref else f"floats never referenced: {unref}")

cites = set(k.strip() for grp in re.findall(r"\\cite(?:\[[^\]]*\])?\{([^}]+)\}", src) for k in grp.split(","))
bib = re.findall(r"\\bibitem\{([^}]+)\}", src)
unused = [b for b in bib if b not in cites]
out("PASS" if not unused else "FAIL", "every reference cited" if not unused else f"references never cited: {unused}")

need = ["sec:intro", "sec:problem", "sec:formal", "sec:detailed", "alg:oracle", "sec:motivation",
        "sec:related", "sec:experiments", "sec:discussion", "sec:conclusions", "sec:llm"]
miss = [n for n in need if n not in labels]
out("PASS" if not miss else "FAIL", "required guide sections present" if not miss else f"missing required labels: {miss}")

text = re.sub(r"%.*", "", prose)
banned = ["crucial", "delve", "landscape", "leverage", "underscore", "seamless", "robust",
          "comprehensive", "cutting-edge", "state-of-the-art", "paramount", "pivotal",
          "In summary", "Moreover", "Furthermore", "Notably", "Importantly", "plays a key role",
          "Picture a", "Imagine a", "Back to the", "trick", "home turf", "pile of", "secret sauce",
          "the catch", "Here is", "Enter ", "game", "magic", "boils down", "at the end of the day",
          "it is important to note", "in order to", "groundbreaking", "game-changer", "tapestry"]
hits = [(w, len(re.findall(r"\b" + re.escape(w) + r"\b", text, re.I))) for w in banned]
hits = [h for h in hits if h[1]]
out("PASS" if not hits else "FAIL", "no banned words" if not hits else f"banned words: {hits}")

plain = re.sub(r"\\[a-zA-Z]+\*?(\[[^\]]*\])?", " ", text)
words = len(re.findall(r"[A-Za-z]{2,}", plain))
pages = max(1, words / 700)
notx = len(re.findall(r",\s+not\s+(?:a|an|the)?\s*\w+", text)) + len(re.findall(r"\brather than\b", text))
out("PASS" if notx <= pages else "WARN", f"'X, not Y' / 'rather than' contrasts: {notx} (budget {pages:.0f}, about one per page)")
rq = len(re.findall(r"\?\s", plain))
out("PASS" if rq <= 8 else "WARN", f"rhetorical questions: {rq} (budget 8)")
boxes = len(re.findall(r"\\begin\{takeaway\}", text))
out("PASS" if boxes <= 7 else "WARN", f"takeaway boxes: {boxes} (budget 7)")
sents = [x for x in re.split(r"(?<=[.!?])\s+(?=[A-Z])", plain) if len(x.split()) > 0]
short = sum(1 for x in sents if len(x.split()) < 7)
ratio = short / max(1, len(sents))
out("PASS" if ratio <= 0.08 else "FAIL", f"fragment sentences (<7 words): {ratio:.0%} of {len(sents)} (budget 8%)")
caps = re.findall(r"\\caption(?:of)?\{figure\}\{\\textbf\{([^}]*)\}|\\caption\{\\textbf\{([^}]*)\}", src)
caps = [a or b for a, b in caps]
slogan = [c for c in caps if len(c.split()) <= 6 and "," in c.rstrip(",. ")]
out("PASS" if not slogan else "WARN", "caption titles describe content" if not slogan else f"slogan-like caption titles: {slogan}")
print(f"INFO  prose words: {words}")
sys.exit(1 if fails else 0)
PY
[ $? -eq 0 ] || fail=1

[ "$fail" -eq 0 ] && echo "GATE PASS" || echo "GATE FAIL"
exit "$fail"
