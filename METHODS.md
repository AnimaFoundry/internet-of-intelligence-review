# Review methods and evidence limits

Supplement to *Low-Power Sensing for an Internet of Intelligence: Materials, Distributed Architectures, and World-Model Learning*.

Review date: 16 October 2026 (Asia/Shanghai). Manuscript version: 1.0.0. This supplement describes the evidence procedure used for this release; it is not a prospectively registered protocol.

## 1. Review design and scope

The manuscript is a **critical integrative review**. It connects representative evidence from materials and energy conversion, distributed sensing and embedded computation, and world-model learning and deployment. It is not a systematic or exhaustive literature review, meta-analysis, bibliometric census, experimental replication, or novelty-priority assessment. The research question is conditional: under what physical, informational and computational constraints can distributed low-power sensing improve useful learning and return capabilities to heterogeneous endpoints?

Three domain research passes developed evidence records for materials and energy, implemented architectures, and world-model learning. A cross-domain pass checked prior reviews, the scope of the proposed contribution, and claims spanning those domains. The process combined web searches, primary-source lookup, examination of official records, and follow-up inspection of relevant passages. It did not use a reproducible export of a complete bibliographic database. Search results and source accessibility changed which full texts could be inspected.

The release bibliography contains **49 cited sources**. This number is the count of distinct entries in [references.json](references.json), matched to distinct citation identifiers in [manuscript.md](manuscript.md). It is not the number of search hits, screened records, eligible experiments, independent replications, or fully read papers. No counts of initially retrieved or excluded records, screening-agreement statistic, or PRISMA flow are claimed. Sources considered in working notes but not cited in the manuscript are not part of that count.

## 2. Search approach and representative queries

Search families covered Internet of Intelligence terminology and surveys; low-power silicon, organic, flexible, two-dimensional and in-memory electronics; energy harvesting and intermittent execution; Smart Dust, TinyOS, constrained Internet protocols, fog and TinyML; and world models, robot datasets, federated learning, compression and updates. Discovery results were followed to identifiable primary, institutional, conference, publisher or standards sources whenever feasible. Search-result summaries of third-party commentary were not used as substitutes for unavailable experimental methods.

The following are **verbatim examples of queries actually executed**, retained from the research passes. They are representative examples, not a complete query/result log or a comprehensive search strategy.

### Architecture and overlap pass

| Query string | Purpose in the review |
| --- | --- |
| `Smart Dust autonomous sensing communication cubic millimeter Kahn Katz Pister 1999 paper` | Locate the early miniature-sensing architecture and distinguish its proposal from implemented deployment |
| `TinyOS An Operating System for Sensor Networks 2005 Levis paper` | Find historical operating-system and sensor-network sources, followed by inspection of the relevant 2004 NSDI paper |
| `MCUNet Tiny Deep Learning on IoT Devices 2020 Lin Song Gan Han NeurIPS` | Locate the primary MCU inference paper and verify hardware and quantization conditions |
| `site.usenix.org Alpaca intermittent execution tasks 2017 Lucia Maeng` | Search for intermittent-execution evidence; subsequent lookup found the author-hosted 2017 manuscript |
| `"TinyML" survey 2024 2025 energy harvesting review edge AI architecture arxiv` | Identify overlapping reviews and later literature on constrained learning |
| `"Cross-Layer Energy Management in Embedded AIoT Sensor Networks"` | Verify the closely related 2026 review and its publication metadata |

### Materials and energy pass

| Query string | Purpose in the review |
| --- | --- |
| `site.nature.com PlasticARM 2021 32 bit microprocessor metal oxide transistors 21 mW` | Locate the flexible processor demonstration; the query's power figure was not accepted as a manuscript fact |
| `"Ultralow-power organic complementary circuits" Nature Klauk 2007` | Locate the primary low-voltage organic-circuit report |
| `"Flexible triboelectric generator" site.sciencedirect.com/science/article/pii` | Locate the original triboelectric paper and its operating conditions |
| `site.nature.com indoor photovoltaics autonomous sensors 2020 dye sensitized solar cells 34 percent 1000 lux` | Explore harvesting/learning integration; the final cited source was verified separately at its publisher |
| `"Ambient Backscatter" "Vincent Liu" Washington pdf 2013` | Locate the author-hosted communication prototype paper |
| `"Mementos: System Support" "pdf" "2011" Ransford Fu` | Locate intermittent-execution work and distinguish the inspected technical report from the later publication |

### World-model learning pass

| Query string | Purpose in the review |
| --- | --- |
| `DreamerV3 Mastering Diverse Control Tasks through World Models Nature 2025 Hafner` | Locate the world-model publication and its earlier manuscript |
| `V-JEPA 2 self-supervised video models enable understanding prediction planning arxiv 2025` | Locate the video-representation and action-conditioned planning study |
| `Open X Embodiment Robotic Learning Datasets RT-X Models arxiv 2023 negative transfer` | Inspect heterogeneous-learning results, including adverse cases |
| `site.arxiv.org Training Compute-Optimal Large Language Models Hoffmann 2022 2203.15556` | Locate the language-model scaling study and limit its transfer to sensor learning |
| `site.proceedings.mlr.press Communication-Efficient Learning Deep Networks Decentralized Data McMahan 2017` | Locate the primary federated-learning conference record |
| `Toward Causal Representation Learning Schölkopf Locatello 2021 Proceedings IEEE doi` | Resolve bibliographic identity and causal-learning context |

### Cross-domain framing and update checks

| Query string | Purpose in the review |
| --- | --- |
| `"Internet of Intelligence" survey materials world models sensors` | Establish existing terminology and related review coverage |
| `"Internet of Intelligence" "2205.08977"` | Verify the identifiable Internet of Intelligence survey |
| `battery-free sensors world models survey foundation models edge artificial intelligence 2025 2026` | Check overlap among sensor, edge and world-model research |
| `site.rfc-editor.org RFC 9019 firmware update architecture internet things` | Verify official update-architecture guidance |
| `site.rfc-editor.org RFC 9124 manifest information model firmware updates internet things` | Verify the official manifest information model and publication status |

Exploratory years, names and numbers inside a query are search inputs, not accepted facts or bibliographic assertions. In particular, the PlasticARM `21 mW` query term is not used as a manuscript measurement, and the photovoltaic query's numerical terms are not independently accepted evidence. The Smart Dust source cited in the paper is the 2000 journal article, the inspected TinyOS source is the 2004 NSDI paper, and the inspected Mementos report is dated 2010. A query need not have directly returned the final source: follow-up searches and author/institutional links were also used. The failed or indirect Alpaca lookup is not described as a successful USENIX retrieval.

## 3. Source selection and claim inclusion

Selection was purposive and iterative. Sources were retained when they supplied an identifiable example or a boundary relevant to the research question. The selection principles were applied during synthesis and are reported here retrospectively; they were not preregistered eligibility rules.

Primary device, circuit, chip, system and learning papers were preferred for experimental claims. Official datasheets supplied component specifications, which were kept separate from independent measurements of complete products. Official standards and architecture documents supplied protocol semantics and design terminology. Related reviews supplied intellectual context and overlap; citing a review did not count as independently reproducing the experiments that it summarized. Historical sources were retained when necessary to prevent unsupported claims that miniature sensing, distributed intelligence or embedded learning had just been invented.

Representative inclusion decisions were:

- **M01 and M02:** retain conventional silicon and a commercial FRAM MCU as comparison baselines, rather than considering emerging materials alone.
- **M08:** retain an integrated photovoltaic/learning demonstration because it directly qualifies any claim that harvesting, wireless sensing and learning have never been connected experimentally.
- **A02:** retain TinyOS implementation and application evidence while distinguishing it from a contemporary deployment audit.
- **A07:** retain MCUNet with its device, memory and quantization conditions rather than an unspecified MCU accuracy claim.
- **R2 and R5:** retain established Internet of Intelligence and cross-layer energy reviews because they substantially overlap with the proposed synthesis.
- **W3 and W5:** retain bounded adverse results from heterogeneous policy learning instead of reporting only improvements.

Claims were omitted or narrowed when the inspected evidence did not establish the required measurement boundary, operating conditions, version or experimental interpretation. Broad market forecasts, universal adoption timelines, untraceable efficiency claims and conclusions requiring unavailable underlying methods were not accepted as quantitative evidence. These are scope decisions, not a finding that every excluded claim is false.

## 4. Reading depth, evidence type and versions

[references.json](references.json) records an identifier, authors, title, year, publication information, source URL, access date, `evidence_type` and `reading_scope` for each cited source. Reading depth is deliberately not uniform:

| Reading category | What it supports | What it does not imply |
| --- | --- | --- |
| Relevant full-text sections or official document passages inspected | Claims tied to the inspected methods, tables or definitions | Every appendix, implementation or cited predecessor was audited |
| Identifiable indexed primary passages inspected | Narrow claims available in publisher/author text returned by search | Unavailable full methods were read or independently verified |
| Abstract and bibliographic record inspected | Bibliographic identification and appropriately limited high-level statements | Detailed numerical comparisons or implementation conclusions absent from the abstract |
| Related review inspected at the stated depth | Existing coverage, terminology and research overlap | Independent experimental replication or proof of an exclusive research gap |

Some publisher pages could not be opened directly although indexed primary abstracts or passages were available. These access limits remain in the records. An author-hosted manuscript can support a reading where the publisher text is unavailable, but it is identified as such. No paywall, authentication or restricted-access workaround is represented as part of this review.

Publication and inspected-version differences are retained. Mementos is cited through its inspected 2010 technical report, rather than silently substituted with its later publication. Dreamer and DROID have publication records and preprint versions that must not be merged indiscriminately. Standards-track base RFCs are distinguished from Informational guidance: RFC 9019 and RFC 9124 are Informational. Not all subsequent RFC updates were audited, so the paper does not offer a complete current implementation profile.

No device experiment, field deployment, model training run or operational dataset was independently reproduced. Internal AI-agent checking compared claims and source records; it is not independent human peer review and does not eliminate correlated errors.

## 5. Important excluded interpretations

The following examples document why prominent numbers or stronger interpretations were not used. They are not a complete list of rejected records.

| Source or topic | Interpretation excluded from the manuscript | Reason |
| --- | --- | --- |
| Phoenix processor, M01 | Sleep power as continuous inference or complete wireless-node power | Different workload and measurement boundary |
| Flexible and two-dimensional processors, M04–M05 | Flexibility or channel thickness as proof of superior full-node energy, manufacturability or autonomy | Those properties do not establish a matched system comparison |
| Harvesting, M06–M08 | Peak output or favorable illumination as continuous available power in arbitrary objects | Excitation, illuminated area, storage and outages matter |
| MCUNet, A07 | 70.7% ImageNet accuracy on an unspecified MCU or under a generic int8 setting | The retained result is tied to the stated H743 memory budget and 4-bit experiment |
| Loihi 2 algorithms, A16 | Emulated-hardware efficiency as measured node energy | The inspected experiments explicitly use emulation |
| Mixed-signal in-memory chip, A11 | Combining a peak throughput mode with accuracy from a different mode | This would create an operating point not measured in the source |
| DROID, W4 | An unqualified task count assembled across versions | Inspected versions differ; the manuscript retains other supported dataset quantities |
| Open X-Embodiment and Octo, W3–W5 | Bounded policy successes or failures as universal world-model performance | Task, model, embodiment and evaluation scope differ |
| Language-model scaling, W6 | A sensor-world-model scaling law or predicted training duration | The experimental domain and workload are different |
| Federated learning and LoRA, W7–W12 | Automatic privacy, decentralized governance, or endpoint feasibility from update size alone | Protocol threat models and the retained base model remain relevant |

An optional neuromorphic-flight paper was not used for performance claims after an erratum was identified whose substantive correction had not been checked. The manuscript does not import its advertised numerical gains. More generally, an omitted number is not replaced by an estimate that appears to come from the source.

## 6. Synthesis and quantitative illustrations

The synthesis compares dependencies across material/device, chip, complete node, gateway, network, training and deployment boundaries. It does not pool efficiency estimates across them. Where a number is used, its workload, precision, power state, illumination or other relevant condition is retained. Closely related reviews are explicitly acknowledged; additive energy balances, layered architectures and model compression are not claimed as new inventions.

The traffic, hypothetical training-throughput and update-energy examples in [scripts/budget_example.py](scripts/budget_example.py) are newly written arithmetic, using declared assumptions and decimal units. They are not measurements, fitted scaling laws, device specifications, or forecasts. Reproducing the arithmetic tests whether the reported calculation follows from those assumptions; it does not validate the assumptions, a physical implementation or the expected utility of additional observations.

The research agenda is prospective. No experiment in that agenda is claimed to have been conducted. For a future bounded study, the manuscript calls for a predeclared task and baseline, independent experimental units, held-out evaluation, meaningful improvement and noninferiority margins, and explicit failure or inconclusive outcomes. Those proposed future requirements do not retroactively preregister this review. Statistical nonsignificance alone is not treated as evidence of equivalence.

## 7. Limitations and rights

The corpus is selective, with publication, accessibility and author-choice biases. English-language search terms and readily accessible sources may underrepresent relevant work. The breadth of the question exceeds the depth available for every subfield; packaging economics, lifetime field evidence and manufacturing comparisons are especially incomplete. The review establishes neither an exclusive research gap nor that a particular material or architecture is the dominant bottleneck in every application.

The release provides original synthesis, bibliographic metadata and illustrative tools. It does not redistribute source papers, source figures, third-party implementations, raw datasets or model weights. Sources retain their own rights. A public paper, open repository or open-source license does not establish patent freedom to operate. This review makes no patent-clearance determination and does not offer a cleared device or implementation.
