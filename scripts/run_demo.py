import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from instructor_insight_engine.core import cohort_summary, class_signals

events=[{'learner':'A','attempts':3,'correct':1,'minutes':15},{'learner':'B','attempts':3,'correct':3,'minutes':12}]
summary=cohort_summary(events)
print('Learner summaries:', summary)
print('Class signals:', class_signals(summary))
