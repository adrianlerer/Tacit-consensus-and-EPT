# CT1 Viability Test - Technical Protocol

## Objective
Validate CT1 (Narrative Stability) measurement before investing writing time.
Test hypothesis: CT1_ARG > CT1_CHL (high lock-in > low lock-in)

## Sample Design
- **Argentina:** 10 speeches (Menem 1994-95, Kirchner 2004-05, Milei 2024)
- **Chile:** 10 speeches (Lagos 2002-03, Bachelet 2015-16, Boric 2023-24)
- **Uruguay:** 10 speeches (Vázquez 2006-07, Mujica 2011-12, Lacalle Pou 2021-22)

## Technical Stack
1. **Scraping:** Python requests + BeautifulSoup
2. **Preprocessing:** spaCy Spanish model (es_core_news_md)
3. **Topic Modeling:** sklearn LatentDirichletAllocation (n_topics=20, random_state=42)
4. **CT1 Calculation:** Pearson correlation(Topic_Distribution_Gov_t, Topic_Distribution_Gov_t-1)

## Expected Results (Theory Prediction)
- CT1_ARG: 0.70-0.80 (high narrative stability)
- CT1_CHL: 0.30-0.40 (low narrative stability)
- CT1_URU: 0.55-0.65 (moderate)

## Decision Rule
- **If CT1_ARG > CT1_CHL:** Proceed with full paper (theory validated)
- **If CT1_ARG < CT1_CHL:** STOP and re-theorize (theory falsified)

## Estimated Execution
- **Time:** 4-6 hours (scraping + processing + analysis)
- **Cost:** $0 (uses free public data + open-source tools)
- **Risk:** Low (can abort if corpus quality insufficient)

## Deliverable
- Brief report (2 pages) with:
  - Table: CT1 scores by country
  - Sample speeches processed
  - Interpretation vs. theory
  - Recommendation: proceed/revise/abort
