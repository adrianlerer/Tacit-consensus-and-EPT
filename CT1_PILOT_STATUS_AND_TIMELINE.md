# CT1 Pilot Argentina - Status and Execution Timeline

**Date:** November 17, 2025, 00:17 UTC  
**Status:** READY TO EXECUTE - Corpus verified, awaiting final authorization

---

## ✅ CORPUS AVAILABILITY CONFIRMED

### **Official Source: Cámara de Diputados Argentina**
**URL:** https://www2.hcdn.gob.ar/secparl/dgral_info_parlamentaria/dip/documentos/mensajes_presidenciales.html

**Archive Status:** ✅ ALL TARGET SPEECHES AVAILABLE

### **Target Speeches Verified:**

| President | Year | Type | Status |
|-----------|------|------|--------|
| **Menem** | 1994 | Apertura Sesiones Ordinarias | ✅ Available (PDF) |
| **Menem** | 1995 | Apertura Sesiones Ordinarias | ✅ Available (PDF) |
| **Menem** | 1996 | Apertura Sesiones Ordinarias | ✅ Available (PDF) |
| **Kirchner** | 2003 | Asunción Presidencial (25/05) | ✅ Available (PDF) |
| **Kirchner** | 2004 | Apertura Sesiones Ordinarias | ✅ Available (PDF) |
| **Kirchner** | 2005 | Apertura Sesiones Ordinarias | ✅ Available (PDF) |
| **Macri** | 2015 | Asunción Presidencial (10/12) | ✅ Available (PDF) |
| **Macri** | 2016 | Apertura Sesiones Ordinarias | ✅ Available (PDF) |
| **Macri** | 2017 | Apertura Sesiones Ordinarias | ✅ Available (PDF) |
| **Milei** | 2023 | Asunción Presidencial (10/12) | ✅ Available (PDF) |

**Total:** 10 speeches across 4 ideologically opposed governments

---

## 🎯 TEST HYPOTHESIS

**Core Hypothesis:**
Despite ideological opposition (Menem liberal, Kirchner statist, Macri pro-market, Milei libertarian), governments exhibit **high narrative stability** on labor/social protection topics, indicating tacit consensus on core institutional arrangements.

**Operationalization:**
```
CT1 = Average(Pearson_Corr(Topic_Distribution_Gov_i, Topic_Distribution_Gov_j))
```

Where Topic_Distribution extracted via LDA (n_topics=20) focusing on "core" topics:
- Labor rights / worker protection
- Social justice / distributive policy  
- State role in economy
- Union relations

**Expected Result (Theory Prediction):**
- Corr(Menem, Kirchner) on core topics: **0.65-0.75**
- Corr(Kirchner, Macri) on core topics: **0.60-0.70**
- Corr(Macri, Milei) on core topics: **0.50-0.65** (Milei more disruptive but within bounds)
- **Average CT1: 0.60** (>0.55 threshold = tacit consensus confirmed)

**Decision Rule:**
- ✅ Average >0.55 → **Proceed Week 2 drafting** (hypothesis confirmed)
- ⚠️ Average 0.35-0.55 → **Proceed with hedging** (ambiguous evidence)
- ❌ Average <0.35 → **Re-theorization required** (hypothesis falsified)

---

## ⏱️ EXECUTION TIMELINE (2-3 Hours)

### **Phase 1: Corpus Acquisition (30 minutes)**
- **Task:** Download 10 PDFs from Cámara de Diputados
- **Method:** Direct download via requests library
- **Output:** 10 PDF files in `/corpus/argentina/`
- **Estimated time:** 30 min (includes PDF text extraction)

### **Phase 2: Preprocessing (30 minutes)**
- **Task:** Clean and prepare text for NLP
- **Steps:**
  1. Extract text from PDFs (PyPDF2 or pdfplumber)
  2. Remove boilerplate (header, footer, metadata)
  3. Tokenization (Spanish)
  4. Remove stopwords (NLTK Spanish + custom political stopwords)
  5. Lemmatization (spaCy `es_core_news_lg`)
- **Output:** 10 preprocessed .txt files
- **Estimated time:** 30 min

### **Phase 3: Topic Modeling (45 minutes)**
- **Task:** LDA topic extraction
- **Method:** sklearn LatentDirichletAllocation
- **Parameters:**
  ```python
  LDA(
      n_components=20,
      max_iter=100,
      learning_method='batch',
      learning_offset=50.,
      random_state=42,
      doc_topic_prior=0.1,  # alpha
      topic_word_prior=0.01  # beta
  )
  ```
- **Output:** 
  - 20 topics with top 10 keywords each
  - Topic distribution per speech (10×20 matrix)
- **Estimated time:** 45 min

### **Phase 4: Core Topic Identification (15 minutes)**
- **Task:** Manual validation of "core" vs "non-core" topics
- **Method:** Inspect top keywords, classify as:
  - **Core:** labor, worker, union, social, protection, rights, state role
  - **Non-core:** infrastructure, foreign policy, cultural, ceremonial
- **Expected:** 5-7 core topics out of 20
- **Output:** List of core topic IDs
- **Estimated time:** 15 min (human judgment required)

### **Phase 5: CT1 Calculation (15 minutes)**
- **Task:** Calculate inter-government correlations
- **Method:**
  1. Average topic distributions by president:
     - Menem_avg = mean(Speech_1994, Speech_1995, Speech_1996)
     - Kirchner_avg = mean(Speech_2003, Speech_2004, Speech_2005)
     - Macri_avg = mean(Speech_2015, Speech_2016, Speech_2017)
     - Milei = Speech_2023 (single speech)
  2. Extract core topic proportions only
  3. Calculate Pearson correlation matrix (4×4)
  4. Average off-diagonal correlations
- **Output:** Correlation matrix + average CT1 score
- **Estimated time:** 15 min

### **Phase 6: Report Generation (15 minutes)**
- **Task:** Create 2-page executive report
- **Content:**
  - Correlation matrix table
  - Interpretation vs. hypothesis
  - Sample speeches processed
  - Top 3 core topics identified
  - Recommendation: Proceed/Revise/Abort
- **Output:** `CT1_PILOT_REPORT.md` (2 pages)
- **Estimated time:** 15 min

---

## 📊 EXPECTED DELIVERABLE

### **CT1 Pilot Report (2 pages)**

**Section 1: Executive Summary (0.5 page)**
- Hypothesis tested
- Corpus processed (10 speeches, 4 governments)
- Result: Average CT1 = X.XX
- Decision: Proceed/Revise/Abort + justification

**Section 2: Correlation Matrix (0.5 page)**

| Government | Menem | Kirchner | Macri | Milei |
|------------|-------|----------|-------|-------|
| Menem      | 1.00  | 0.XX     | 0.XX  | 0.XX  |
| Kirchner   | 0.XX  | 1.00     | 0.XX  | 0.XX  |
| Macri      | 0.XX  | 0.XX     | 1.00  | 0.XX  |
| Milei      | 0.XX  | 0.XX     | 0.XX  | 1.00  |

**Average CT1 (core topics only):** X.XX

**Section 3: Core Topics Identified (0.5 page)**

Example format:
- **Topic 3:** protección, trabajador, derechos, laboral, sindical (Core: Labor rights)
- **Topic 7:** justicia, social, distribución, equidad, inclusión (Core: Social justice)
- **Topic 12:** estado, mercado, intervención, economía, regulación (Core: State role)

**Section 4: Sample Speeches (0.5 page)**
- List of 10 speeches processed with dates and word counts
- Confirmation all are official Cámara de Diputados sources

---

## 🚦 EXECUTION STATUS

**Current Status:** ✅ READY TO EXECUTE

**Blockers:** None identified
- ✅ Corpus availability: Confirmed
- ✅ Source reliability: Official government archive
- ✅ Technical capacity: Python + spaCy + sklearn installed
- ✅ Timeline: 2-3 hours realistic

**Awaiting:** Final authorization from Adrian to begin execution

---

## 💾 TECHNICAL REQUIREMENTS

**Python Libraries:**
```python
requests==2.31.0
beautifulsoup4==4.12.2
pdfplumber==0.10.3  # PDF text extraction
nltk==3.8.1         # Spanish stopwords
spacy==3.7.2        # Lemmatization
scikit-learn==1.3.2 # LDA topic modeling
pandas==2.1.3       # Data manipulation
numpy==1.26.2       # Numerical operations
```

**spaCy Model:**
```bash
python -m spacy download es_core_news_lg
```

**Estimated Disk Space:** 50-100 MB (PDFs + processed text)

---

## 🎯 DECISION POINT

### **Adrian, please confirm ONE of the following:**

**OPTION A: Execute CT1 Pilot NOW**
- I authorize Genspark to proceed with 2-3 hour analysis
- Expected delivery: Tomorrow November 18, 2025 (24h)
- No additional input needed from me

**OPTION B: Provide Speeches Myself (Faster)**
- I will provide 10 speeches as .txt files within 6-8 hours
- Genspark processes immediately upon receipt (1.5h execution)
- Expected delivery: Tomorrow morning (12-16h total)

**OPTION C: Defer CT1 Test**
- Proceed with Week 2 drafting WITHOUT empirical CT1 validation
- Mark CT1 as "future work" in paper
- Risk: No preliminary evidence for conceptual claims

---

## 🔴 MY RECOMMENDATION

**Execute OPTION A (CT1 Pilot NOW)**

**Rationale:**
1. **Low Risk:** 2-3 hours execution time, $0 cost, official sources
2. **High Value:** Validates core mechanism BEFORE writing 28 pages
3. **Decision Clarity:** Provides clear Proceed/Revise/Abort signal
4. **Timeline Preservation:** 24h delivery still within Week 1 buffer

**If you confirm OPTION A, I will:**
1. Begin execution immediately (within 1 hour of confirmation)
2. Deliver preliminary results in 12h (correlation matrix)
3. Deliver final 2-page report in 24h (tomorrow evening)

**Awaiting your confirmation to proceed.** 🚀

---

**END OF STATUS REPORT**

**Next Action:** Await Adrian's authorization (A/B/C)
