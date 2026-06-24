# Principle Extraction Architecture: Phase 1

## 1. System Vision

The **Akshat Reasoning System** aims to discover *HOW* Akshat Shrivastava thinks, not merely what he says. Instead of acting as an archive for content, market commentary, or stock picks, the system's objective is to extract, map, and utilize the recurring investing principles and mental models that drive those decisions.

By synthesizing core decision-making frameworks into actionable principles, this system will form the foundation for automated reasoning, opportunity scanning, and future decision-making mimicking the underlying investment philosophy.

## 2. Problem Definition

Current iterations of knowledge systems often devolve into full-text search engines or trivia archives. The primary challenge is elevating raw source material (e.g., transcripts, posts) into abstract, recurring mental models without losing the underlying evidence.

We must:
- Differentiate between a "fact" (e.g., "Apple is trading at $150") and a "principle" (e.g., "Buy dominant tech franchises when trading below historical mean PE").
- Filter out noise, individual stock names, and transient market commentary.
- Correlate identical concepts expressed differently across multiple sources and time periods.

## 3. Principle Definition

A **Principle** is a repeatable investing decision framework used across multiple years, multiple topics, and multiple content sources.

*   **What it IS:** A generalized mental model (e.g., "Follow demographic shifts", "Follow capital allocation", "Prefer founder-led businesses").
*   **What it is NOT:** Stock names, company names, specific portfolio holdings, single predictions, or localized market commentary.

## 4. Architecture Options

To automatically extract principles from the repository, we must evaluate different natural language processing and clustering approaches:

### Option A: Rule-Based / Keyword Matching
- **Approach:** Use regex, TF-IDF, and predefined dictionaries to search for specific phrases like "rule of thumb", "always buy", "never invest".
- **Pros:** Fast, deterministic, no external dependencies, very transparent.
- **Cons:** Extremely rigid. Misses nuances. Cannot cluster conceptually similar principles described with different vocabulary.

### Option B: Embedding-Based (Semantic Clustering)
- **Approach:** Generate dense vector embeddings for source segments. Use clustering algorithms (e.g., DBSCAN, K-Means) to group semantically similar paragraphs.
- **Pros:** Excellent at capturing latent themes and unifying different vocabulary into a single concept.
- **Cons:** Opaque ("black box"), requires external or heavy local models, prone to clustering similar "facts" rather than similar "frameworks".

### Option C: Hybrid Pipeline (Extraction + Semantic Merging + Symbolic Verification)
- **Approach:**
    1. *Heuristic Parsing*: Filter out non-actionable sentences.
    2. *Semantic Extraction*: Use embeddings or light-weight language models to extract generalized concepts from the filtered segments.
    3. *Clustering*: Cluster concepts to detect themes.
    4. *Symbolic Verification*: Ensure the cluster has temporal diversity (spans years) and source diversity (multiple documents).
- **Pros:** Combines the semantic flexibility of Option B with the deterministic rigor and evidence-tracking of Option A.

## 5. Recommended Architecture

**Option C: Hybrid Pipeline** is the recommended architecture.
It bridges the gap between the messy reality of natural language and the strict structural requirements of our Reasoning System. By using embeddings/LLMs *only* for candidate generation and semantic merging, and relying on deterministic logic for scoring, time-persistence checks, and evidence mapping, we maintain trust and auditability.

## 6. Extraction Pipeline

The extraction process will follow a strict, multi-stage pipeline:

1.  **Source Parsing:** Scan Tier 1 (`knowledge/`), Tier 2 (`raw_sources/`), and Tier 3 (`skills/`). Ignore system directories.
2.  **Concept Extraction:** Isolate declarative, instructive, or philosophical statements. Strip out specific company names using Named Entity Recognition (NER) or local masking.
3.  **Theme Detection:** Cluster extracted concepts using semantic similarity.
4.  **Principle Candidate Generation:** Formulate a generalized "Principle" from the cluster.
5.  **Evidence Mapping:** Link the original source quotes, file paths, and timestamps back to the Candidate Principle.
6.  **Principle Scoring:** Calculate a Confidence Score based on the evidence.
7.  **Principle Catalog:** Commit the finalized Principle to the `knowledge/principles/` architecture.

## 7. Evidence Model

Every Principle must be strictly anchored to its underlying evidence. The system cannot "hallucinate" a principle.
- **Source Reference:** Exact file path.
- **Snippet:** The verbatim quote supporting the principle.
- **Date/Time:** When it was stated.
- **Context:** The broader topic being discussed.

## 8. Confidence Model

A principle's strength is defined by its recurrence and consistency, not just the volume of words.
The proposed Confidence Model is a weighted formula:

**Confidence Score = (F + C + T + Q) - P**

Where:
*   **F (Frequency):** Raw count of supporting evidence snippets. (Diminishing returns applied).
*   **C (Cross-source occurrence):** Bonus if found across different formats (e.g., YouTube vs. Paid Post).
*   **T (Time persistence):** Bonus if the evidence spans multiple years.
*   **Q (Evidence quality):** Weight multiplier based on the source Tier (Tier 1 > Tier 2 > Tier 3).
*   **P (Penalty for Inconsistency):** Subtracted points for contradictory statements or low clustering cohesion.

*Example Scale: 0-100.* Principles scoring above a defined threshold (e.g., 75) are promoted to "Core Principles".

## 9. Failure Modes & Risks

1.  **Over-fitting to recent content:** The system might overweight a recent macro trend and misclassify it as a "timeless principle." *(Mitigation: Strong time-persistence (T) weighting in the Confidence Model).*
2.  **Entity Leakage:** Failing to strip out stock names, leading to a principle like "Always buy Apple". *(Mitigation: Strict NER masking before extraction).*
3.  **Vague Platitudes:** Generating useless principles like "Make good decisions." *(Mitigation: The Evidence Model must require actionable frameworks).*

## 10. Future Integration Plan

This Principle Extraction Engine is merely Phase 1. Once operational, the Principles will integrate into:

*   **Trend Templates:** Aligning current macro trends with established principles to validate narratives.
*   **Opportunity Scanner:** Automatically evaluating new market data or asset classes against the Principle Catalog.
*   **Doubt Engine:** Using Principles to challenge newly ingested content or user queries that contradict established frameworks.
*   **Stock Discovery Engine:** Sifting through fundamental data using the extracted mental models (e.g., filtering for "founder-led, high ROCE, temporary drawdown") rather than hardcoded formulas.
