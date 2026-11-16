# How Schwarzenegger Won: An Evidence-Based Analysis of California’s 2003 Gubernatorial Recall

*Analysis prepared with Claude (Anthropic) · November 1, 2026 · Companion dataset: schwarzenegger_recall_2003_dataset.xlsx (58 counties, validated to certified totals)*

## Abstract

On October 7, 2003, California voters recalled Governor Gray Davis (55.4% yes) and, on the same ballot, elected Arnold Schwarzenegger as his successor with 48.6% of votes cast on the replacement question, 17.1 points ahead of Lieutenant Governor Cruz Bustamante (31.5%). This paper asks how that outcome came about and treats the question as an empirical one. It uses the Secretary of State’s certified county-level Statement of Vote, registration data as of September 22, 2003, and clearly labeled secondary evidence (pre-election polls and news reports of exit polls). It evaluates six competing explanations against what the data can and cannot show: voter disapproval of Davis, defection from Davis’s usual coalition, changes in who voted, Schwarzenegger’s cross-party appeal, the ballot’s structure, and partisan organization. The evidence most strongly supports the first two, along with a cross-party coalition behind Schwarzenegger. The ballot-structure explanation is weak as an account of *who* won, because Schwarzenegger’s lead survives every plausible reallocation of minor-candidate votes. The partisan-organization explanation is not testable with returns data. County-level associations are very strong (county recall support correlates +0.94 with Republican registration share), but they describe places and do not identify how individual voters behaved. The paper makes no judgment about whether the outcome was good or bad, or whether Davis deserved blame for conditions in the state.

## 1. Introduction and scope

The 2003 recall was the first successful recall of a California governor and only the second of any U.S. governor. A candidate with no prior elected experience won a statewide office in a state whose registered electorate was 43.7% Democratic and 35.3% Republican. Explanations offered at the time and since differ sharply, and some of them reflect the political commitments of the person offering them. This paper therefore sets out its rules first.

- **Scope.** The research question is *how* the outcome occurred, meaning which measurable factors are consistent with it. It does not address whether the recall was legitimate, whether Davis was responsible for the energy crisis or budget deficit, or whether Schwarzenegger governed well.
- **Evidence hierarchy.** Certified returns and official registration data are primary. Pre-election polls and news reports of exit polls are secondary and labeled as such. Every explanation is graded by how much independent evidence supports it, and each grade comes with a statement of what the evidence cannot show.
- **No hidden coding.** The companion dataset contains official counts and mechanical derivations only. Descriptive labels (regions, voting systems) are documented.

## 2. Institutional background

California’s recall procedure puts two questions on one ballot. The first asks whether the incumbent should be removed. The second lists replacement candidates, and the winner needs only a plurality. A voter may vote on either question or both. A federal court ruling in 2003 affirmed that voters could vote for a successor even if they skipped the recall question. The signature threshold for the 2003 recall was 897,156, based on the November 2002 gubernatorial vote. Rep. Darrell Issa helped finance early petition efforts. The special election was estimated to cost taxpayers about $67 million. Results were certified on November 14, 2003.

The ballot listed 135 replacement candidates, close to as many as in all earlier California gubernatorial elections combined (180 candidates from 1849 to 2002). Schwarzenegger announced his candidacy in early August 2003, and Bustamante, the only major Democrat to enter the replacement race, entered later that month.

Context cited by contemporary coverage includes the 2000–01 energy crisis with rolling blackouts, a record state budget deficit estimated at $38 billion, a tripling of the vehicle license fee, and university fee increases of up to 30%. These are reported conditions, not findings of this paper.

## 3. Data

**Primary data.** The California Secretary of State’s *Statement of Vote* for the October 7, 2003 Statewide Special Election gives, for all 58 counties: votes on the recall question, votes for each replacement candidate, ballots cast (polling place and absentee), and registration by party as of September 22, 2003. The statewide historical turnout table is from the same document. Because early election-night counts understated absentee ballots, this paper uses only the certified figures. (Candidate totals in many news reports on election night, around 3.7 million for Schwarzenegger, were partial counts. The certified total is 4,206,284.)

**Validation.** County sums reconcile exactly to certified statewide totals for registered voters, Democratic and Republican registration, total ballots, recall yes and no, and the four leading candidates (all differences are zero; see the statewide_results sheet).

**Secondary data.** Pre-election polls (Gallup, Field, Time/CNN), news reports of AP/Edison–Mitofsky exit-poll findings, and a pre-election subgroup survey are included in separate sheets. Their original microdata were not obtained, so they are used only to corroborate patterns and never to compute statistics.

**Derived variables.** Registration shares (Democratic, Republican, Decline-to-State), turnout of registered voters, county recall Yes share (yes ÷ yes+no), and candidate shares are computed by formula from the official counts.

## 4. Methods

1. **Descriptive statistics** at the state, regional (nine analyst-defined regions), and county level.
2. **Correlation and ballot-weighted least squares (WLS)** at the county level. The outcome is recall Yes share or an SOS-reported candidate percentage, and the predictors are Republican and Democratic registration shares, with the remainder (mostly Decline-to-State) as the baseline. Standard errors are heteroskedasticity-robust (HC1), and weights are ballots cast. These models are descriptive. County-level associations cannot identify individual behavior (the ecological fallacy), and coefficients can fall outside 0–1 when party registration proxies for unmeasured county traits.
3. **Arithmetic margin and reallocation tests.** These ask how many votes would have had to change, or how minor-candidate votes could be reassigned, for an outcome to change. They involve no behavioral modeling.
4. **Explanation grading.** Each of six pre-stated explanations is rated *Strong*, *Moderate*, *Limited*, or *Not testable* depending on whether independent sources converge and whether the returns data can distinguish it from alternatives.

## 5. Results

### 5.1 The headline result

| Measure | Votes | Share |
|---|---|---|
| Recall: Yes | 4,976,274 | 55.4% |
| Recall: No | 4,007,783 | 44.6% |
| Schwarzenegger (R) | 4,206,284 | 48.6% |
| Bustamante (D) | 2,724,874 | 31.5% |
| McClintock (R) | 1,161,287 | 13.4%* |
| Camejo (Green) | 242,247 | 2.8% |

*Shares of votes cast in each contest. \*The SOS summary prints 13.5%; 1,161,287 ÷ 8,657,919 = 13.4%.*

A total of 9,413,494 ballots were cast, which is 61.2% of registered voters and 43.1% of eligible adults. On the recall question 429,431 ballots (4.6%) recorded no vote, and on the replacement question 755,575 (8.0%) did. Consequently, 326,138 more voters voted on the recall than on the replacement question. Schwarzenegger’s margin over Bustamante was 1,481,410 votes, and the recall’s margin was 968,491 votes. Schwarzenegger’s 4.21 million votes were fewer than the 4.98 million recall Yes votes, a reminder that the two questions drew different sets of voters.

### 5.2 Geography

Recall Yes won a majority in 43 of 58 counties. Schwarzenegger won a plurality in 50 counties and Bustamante in 8: Alameda, Marin, Mendocino, San Francisco, San Mateo, Santa Clara, Santa Cruz and Sonoma, all in the northern coastal and Bay Area region. The five counties with the highest Yes shares were Sutter (77.4%), Glenn (76.3%), Kern (75.7%), Lassen (75.4%) and Yuba (75.2%), and the five lowest were San Francisco (19.7%), Alameda (30.0%), Marin (32.5%), Santa Cruz (35.6%) and San Mateo (37.2%).

Los Angeles County was pivotal because of its size: it cast 23.4% of all ballots. Its voters narrowly rejected the recall (49.0% Yes), yet Schwarzenegger led Bustamante there 44.9% to 37.5% of governor-contest votes.

| Region | Counties | Ballots | Rep. reg. | Dem. reg. | Turnout (of reg.) | Recall Yes | Arnold (of ballots) | Bustamante (of ballots) |
|---|---|---|---|---|---|---|---|---|
| Los Angeles | 1 | 2,203,838 | 27.5% | 51.4% | 55.1% | 49.0% | 39.9% | 33.4% |
| Bay Area | 9 | 2,130,845 | 24.8% | 50.2% | 64.1% | 36.3% | 29.6% | 41.1% |
| Southern California | 4 | 1,947,784 | 44.6% | 33.9% | 63.7% | 68.7% | 56.8% | 19.8% |
| Inland Empire | 2 | 799,994 | 46.0% | 36.9% | 61.3% | 70.2% | 57.3% | 20.4% |
| San Joaquin Valley | 8 | 776,269 | 46.0% | 40.4% | 56.2% | 67.8% | 50.3% | 23.3% |
| Sacramento Region | 6 | 693,943 | 40.0% | 39.8% | 67.9% | 63.3% | 51.5% | 22.3% |
| Central Coast | 5 | 430,357 | 35.0% | 42.7% | 67.5% | 51.3% | 40.2% | 31.5% |
| North State | 13 | 300,926 | 39.8% | 37.4% | 63.6% | 62.3% | 48.3% | 22.7% |
| Sierra & Foothills | 10 | 129,538 | 45.3% | 34.1% | 71.9% | 65.0% | 50.2% | 20.4% |

*Candidate shares in this table use all ballots as the denominator, so they run about 8% below the official percentages, which use only governor-contest votes. Regions are analyst-defined groupings of counties.*

### 5.3 Association with party registration

Across the 58 counties, recall Yes share correlates +0.94 with Republican registration share, −0.82 with Democratic share, −0.63 with Decline-to-State share, and −0.08 with turnout (ballot-weighted correlations are +0.96, −0.88, −0.64 and +0.08). The 22 counties where Democratic registration exceeded Republican registration voted Yes at 45.0% in aggregate; the other 36 voted Yes at 69.1%.

| Outcome (county share) | Constant | Rep. reg. share | Dem. reg. share | Weighted R² |
|---|---|---|---|---|
| Recall Yes | −0.110 (0.216) | 1.551 (0.216) | 0.259 (0.341) | 0.920 |
| Schwarzenegger % | 0.151 (0.284) | 0.999 (0.291) | −0.051 (0.440) | 0.841 |
| Bustamante % | 0.728 (0.192) | −1.106 (0.221) | −0.039 (0.277) | 0.922 |
| McClintock % | −0.165 (0.089) | 0.464 (0.095) | 0.310 (0.133) | 0.624 |

*Ballot-weighted least squares, n = 58, robust standard errors in parentheses. Descriptive only.*

Two cautions apply. First, a Republican coefficient above 1 for the recall question (and a Democratic coefficient that is not distinguishable from zero) does not mean individual Republicans voted Yes at more than 100%. It indicates that Republican registration share acts as a proxy for county characteristics associated with recall support. Second, the Democratic and Republican shares are strongly correlated across counties (about −0.8), so their separate coefficients are imprecisely estimated. Adding turnout of registered voters raises the weighted R² to 0.944 and gives a turnout coefficient of −0.41 (SE 0.11). That conditional association is not interpreted causally here.

### 5.4 Cross-party support for Schwarzenegger

The two Republican candidates combined took 5,367,571 votes (62.0% of governor-contest votes). In all 58 counties their combined share exceeded the county’s Republican share of registration, by about 26 points on average (ballot-weighted). Registration is not turnout, and Decline-to-State registrants (16.0% of the state) are not partisans of either side. Even so, the gap is large enough to show that Schwarzenegger’s and McClintock’s combined vote was well beyond registered Republicans alone.

A bounding calculation, with the assumption stated, shows how much. If Republican registrants (5,429,356) had turned out at the statewide average rate (61.2%) and every one had voted Yes, they would have supplied about 3.32 million of the 4.98 million Yes votes, leaving at least about 1.65 million (33%) from other voters. At 75% Republican turnout the non-Republican minimum is about 0.90 million (18%). At 85% it is still about 0.36 million (7%). The minimum is therefore positive under any plausible turnout assumption.

Schwarzenegger also won a plurality in 14 of the 22 counties where Democratic registration exceeded Republican registration, including Los Angeles, Sacramento, Imperial, Merced, Stanislaus, Santa Barbara, Lake, Monterey, San Benito and Contra Costa. News reports of exit polls (secondary evidence) say about a quarter of Democrats and almost half of Hispanic voters voted to recall Davis, and that roughly six in ten voters in union households did so.

### 5.5 Did the ballot’s structure decide who won?

Because a plurality was enough, one question is whether vote-splitting between candidates mattered. The arithmetic below reassigns minor-candidate votes in ways that favor Bustamante, none of which is a behavioral prediction.

| Scenario | Schwarzenegger | Opponent total | Schwarzenegger lead |
|---|---|---|---|
| Actual result | 4,206,284 | Bustamante 2,724,874 | +1,481,410 |
| All McClintock votes go to Bustamante | 4,206,284 | 3,886,161 | +320,123 |
| All McClintock and Camejo votes also go to Bustamante | 4,206,284 | 4,128,408 | +77,876 |
| Votes that would need to switch from Schwarzenegger to Bustamante for a tie | | | 740,705 (17.6% of his votes) |
| Recall Yes votes that would need to switch to No for a recall tie | | | 484,246 (9.7% of Yes votes) |

Schwarzenegger leads even in the extreme scenario that sends every McClintock and Camejo vote to Bustamante. Vote-splitting among Republican candidates therefore did not decide the replacement result. The recall itself, with its 968,491-vote margin, did not depend on the replacement ballot at all.

### 5.6 Who voted? Turnout and electorate composition

| Election | Registered | Democratic reg. | Republican reg. | Voters | Turnout of registered |
|---|---|---|---|---|---|
| Nov 2002 general | 15,303,469 | 44.6% | 35.2% | 7,738,821 | 50.6% |
| Oct 2003 special | 15,383,526 | 43.7% | 35.3% | 9,413,494 | 61.2% |
| Nov 2006 general | 15,837,108 | 42.5% | 34.3% | 8,899,059 | 56.2% |

Turnout in the special election was 10.6 points higher than in the November 2002 general election, with 1.67 million more voters (+21.6%), while the party composition of the registered electorate barely changed (Democratic share down 0.9 points; Republican share up 0.1). The rise in participation was therefore not a story of newly registered Republicans. Whether the additional voters leaned differently from 2002 voters cannot be determined from returns, since the registration shares of non-voters are unknown. At the county level turnout is nearly uncorrelated with recall support (r = −0.08), and turnout was lowest in two large regions with very different vote patterns: Los Angeles (55.1%) and the San Joaquin Valley (56.2%).

### 5.7 Secondary evidence

| Pre-election poll | Dates | Population | Recall Yes |
|---|---|---|---|
| Gallup (CNN/USA Today) | Aug 7–10 | Registered voters (n=801) | 64% (29% no) |
| Field Poll (via Gallup) | Aug | Likely voters | 58% |
| Time/CNN | Late Sept | Likely voters | 54% (35% no) |
| CNN/USA Today/Gallup | ~Sept 28 | Probable voters | 63% (35% no) |
| **Certified result** | Oct 7 | Voters | **55.4%** (44.6% no) |

Polls ranged from 54% to 64% depending on pollster and voter screen, so the result lay inside the range but the spread was wide. News reports of AP/Edison–Mitofsky exit-poll findings say about seven in ten voters disapproved of Davis’s job performance and nearly half disapproved strongly; of those strong disapprovers, about nine in ten voted to recall and about seven in ten voted for Schwarzenegger. A Christian Science Monitor report said anti-abortion voters preferred Schwarzenegger, who supports abortion rights, over McClintock, who opposes it. These are second-hand summaries of exit-poll results and carry the caveats of that format.

## 6. Evaluating the competing explanations

| # | Explanation | What the certified returns show | What secondary sources add | Grade | What cannot be shown |
|---|---|---|---|---|---|
| 1 | Widespread disapproval of Davis | Recall passed 55.4–44.6; 43 of 58 counties voted Yes | Polls 54–64% Yes; exit polls ~7 in 10 disapproving | **Strong** | *Why* voters disapproved, and whether the disapproval was deserved |
| 2 | Defections from Davis’s usual coalition | Los Angeles (51.4% Democratic registration) voted 49.0% Yes; Yes won 7 of 22 Democratic-plurality counties | ~¼ of Democrats, ~½ of Hispanic voters, ~6 in 10 union households said Yes | **Strong** | Exact individual-level crossover (returns are aggregates) |
| 3 | A changed electorate | Turnout 61.2% vs. 50.6% in 2002; registration shares nearly unchanged | None independent | **Moderate** | Whether new voters differed from 2002 voters |
| 4 | Schwarzenegger’s cross-party appeal | Won 50 counties, including 14 of 22 Democratic-plurality counties; combined Republican candidates far exceeded Republican registration share | Anti-abortion voters preferred him to McClintock (exit-poll report) | **Moderate to strong** | Which personal traits (celebrity, centrism, outsider status) drove it |
| 5 | Ballot structure (plurality, 135 candidates, no runoff) | Schwarzenegger leads under every reallocation of McClintock/Camejo votes | Democrats’ later argument that a Democratic alternative helped the recall pass | **Limited** for who won; **Not testable** for whether the recall passed | Whether a different ballot would have changed the recall vote |
| 6 | Organized partisan effort | Petition drive had partisan funding (Issa); but the Yes vote far exceeds Republican registration | Recall backers called it bipartisan populism; opponents called it a partisan power grab | **Not testable** | Intent and the counterfactual of no organized effort |

**Reading the table.** No single explanation accounts for the outcome by itself. The returns are consistent with a sequence in which (1) a large share of the electorate disapproved of the incumbent, (2) enough members of the incumbent’s party and allied groups defected that the recall passed by 968,491 votes, and (3) the replacement vote consolidated behind the candidate who drew support across party lines, a lead too large to be altered by vote-splitting. Explanations 5 and 6 are about the process and the organization behind it, which returns cannot adjudicate; people with different views of the recall can read the same numbers and reach different conclusions about them, and this paper does not take a side on that.

## 7. Limitations

- **Aggregate data.** County returns cannot show how any individual voted. All individual-level statements (for example, how many Democrats voted Yes) rest on secondary exit-poll reports.
- **Ecological inference.** County regressions show association, not mechanism. Coefficients outside 0–1 are signs of proxying and extrapolation.
- **Registration is not turnout.** Party registration shares describe registrants, not the people who voted. The bounding exercise in 5.4 states its turnout assumptions explicitly.
- **Denominators.** SOS candidate percentages use governor-contest votes, rounded to 0.1 point. Regional candidate shares here use ballots as the denominator, and an estimate of contest votes derived from those percentages differs from the actual total by 0.1%.
- **Secondary sources.** Polls differ in population and method. Exit-poll findings are quoted from news coverage rather than original crosstabs, and the subgroup survey in the dataset is pre-election and not comparable to certified returns.
- **Small source discrepancy.** The SOS registration table lists 5,429,356 Republican registrants, while its historical table lists 5,429,256; the analysis uses the former.
- **No individual-level or precinct data.** Precinct returns, voter files and cast-vote records would permit stronger tests, especially of turnout composition and crossover.

## 8. Conclusion

The certified data show how the outcome was structurally produced. Davis lost a clear majority on the recall question, with Yes votes coming from far beyond Republican registrants. Schwarzenegger won a plurality of the replacement vote in 50 of 58 counties, including most of the large interior counties and Los Angeles, with a lead of nearly 1.5 million votes that no reallocation of minor-candidate votes erases. The strongest-supported explanations are voter disapproval of the incumbent, defection from his usual coalition, and cross-party support for the winner. The weakest are those that rest on ballot mechanics or on the intentions of the organizers, which returns cannot test. What the evidence cannot say is as important: it does not establish why voters disapproved, whether that disapproval was warranted, or whether the result was desirable. A reader’s views on those questions do not change the arithmetic above.

**Suggested extensions.** Add county-level Proposition 53 and 54 results to test whether Yes voters were also conservative on other ballot questions in the same election; merge 2002 gubernatorial county results to measure change in party vote by county; use precinct-level returns to test turnout composition; and compare with the 2021 recall in which the incumbent was retained.

## Appendix A. Reproducibility

The companion files are *schwarzenegger_recall_2003_dataset.xlsx* (10 sheets: county_data, statewide_results, region_summary, statewide_history, polls, exit_poll_reported, subgroup_survey, analysis_results, data_dictionary, sources), *county_data.csv*, and *data_and_analysis.py*, which rebuilds the dataset, validates it against the certified totals, and reproduces every statistic in this paper (results.json).

## References

1. California Secretary of State, *Statement of Vote, Statewide Special Election, October 7, 2003* (certified Nov. 14, 2003). https://elections.cdn.sos.ca.gov/sov/2003-special/sov-complete.pdf
2. Gallup News Service, “Schwarzenegger Leads California Gubernatorial Race” (Aug. 2003). https://news.gallup.com/poll/9013/schwarzenegger-leads-california-gubernatorial-race.aspx
3. Gallup, “California Recall Election: Questions and Answers” (Aug. 19, 2003). https://news.gallup.com/poll/10012/california-recall-election.aspx
4. CBS News, coverage of the recall campaign (Oct. 2003). https://www.cbsnews.com/news/let-the-games-begin-10-08-2003/
5. CNN/USA Today/Gallup poll, CNN transcript (Oct. 1, 2003). https://www.cnn.com/TRANSCRIPTS/0310/01/ltm.06.html
6. Associated Press analysis, “Revolt fueled by Davis’ shortcomings,” via Lawrence Journal-World (Oct. 8, 2003). https://www2.ljworld.com/news/2003/oct/08/analysis_revolt_fueled/
7. Christian Science Monitor, “A fresh start, a Herculean task” (Oct. 9, 2003). https://csmonitor.com/2003/1009/p01s04-uspo.html
8. Cal State Fullerton, Orange County recall survey (2003). https://calstate.fullerton.edu/News/research/2003/gov_recall.html
9. Tomás Rivera Policy Institute et al., recall survey by race/ethnicity, as reproduced on Daily Kos (Sept. 26, 2003). https://dailykos.net/archives/004333.html
10. Wikipedia, “2003 California gubernatorial recall election” (background on process and dates). https://en.wikipedia.org/wiki/2003_California_gubernatorial_recall_election
