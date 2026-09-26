"""Reproduce the labeled worked example; this is not an empirical study."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from instructor_insight_engine import core
outputs={'accuracy A (1 correct / 3)': core.cohort_summary([dict(learner='A',minutes=10,attempts=3,correct=1)])['A']['accuracy'], 'flag A': core.cohort_summary([dict(learner='A',minutes=10,attempts=3,correct=1)])['A']['flag']}
result={'kind':'illustrative_calculation','note':'Synthetic count example; cutoff is heuristic.','outputs':outputs}
(ROOT/'results/review_examples.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
