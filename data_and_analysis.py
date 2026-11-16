"""2003 California recall: county dataset build, validation and analysis.
Source: California Secretary of State, Statement of Vote, Statewide Special Election, Oct 7 2003
(https://elections.cdn.sos.ca.gov/sov/2003-special/sov-complete.pdf). Certified Nov 14 2003.
Run: python data_and_analysis.py  -> county_data.csv, results.json"""
import io, json, numpy as np, pandas as pd
COLS="county,eligible,registered,reg_dem,reg_rep,reg_ai,reg_green,reg_lib,reg_nl,reg_pf,reg_misc,reg_dts,precincts,ballots_precinct,ballots_absentee,ballots_total,recall_yes,recall_no,recall_not_cast,arnold,bustamante,mcclintock,camejo,arnold_pct_rep,bustamante_pct_rep,mcclintock_pct_rep,camejo_pct_rep".split(",")
RAW="""Alameda,969179,706056,388457,134221,11407,17433,3594,2129,4426,6248,138141,1010,303928,118341,422269,126713,295556,0,98461,205643,39776,19289,25.6,53.5,10.4,5.1
Alpine,933,815,279,305,30,14,5,0,2,6,174,5,0,575,575,297,274,4,267,162,36,13,52.5,31.9,7.1,2.6
Amador,25387,19245,7093,8930,507,158,128,14,45,230,2140,57,9581,5705,15286,9600,4643,1043,8281,2658,2592,374,58.0,18.6,18.2,2.7
Butte,151022,115492,40046,48798,3152,2890,840,105,676,843,18142,162,44764,28707,73471,46054,25081,2336,36910,14893,11759,3075,53.4,21.6,17.1,4.5
Calaveras,32611,25154,8867,11416,644,320,350,28,74,122,3333,30,10354,8011,18365,11775,5856,734,9410,3587,3431,497,53.8,20.5,19.7,2.9
Colusa,10750,7718,2977,3582,195,24,33,4,23,20,860,14,3606,1625,5231,3821,1267,143,3159,838,783,53,64.3,17.1,16.0,1.1
Contra Costa,664023,444446,215917,143156,7406,4602,2153,677,1242,3609,65684,489,214751,106193,320944,137372,176933,6639,114187,110824,42152,11229,39.6,38.4,14.6,3.9
Del Norte,16967,12231,4624,4807,375,145,91,8,42,89,2050,18,4406,2578,6984,4315,2603,66,3522,1634,782,96,55.0,25.6,12.3,1.5
El Dorado,117933,94506,30081,45131,2320,1085,695,79,278,715,14122,110,45058,25486,70544,48946,19585,2013,41572,11211,10532,2103,61.5,16.6,15.6,3.2
Fresno,482209,343696,139047,158912,5816,1832,1302,285,573,742,35187,453,127369,62354,189723,122423,61120,6180,93375,50888,29393,1930,51.9,28.3,16.4,1.1
Glenn,15980,11436,3956,5497,298,41,38,12,45,33,1516,20,5612,1956,7568,5706,1774,88,4429,1035,1285,68,62.7,14.7,18.2,1.0
Humboldt,95911,78752,32914,23632,1835,5482,781,190,327,322,13269,81,35509,13220,48729,22861,24880,988,18756,16088,3992,3263,41.5,35.6,8.9,7.3
Imperial,76331,51109,27266,14621,953,138,184,61,239,297,7350,148,17050,6723,23773,14759,8527,487,9632,7995,2067,115,45.8,38.0,9.9,0.6
Inyo,13083,10098,3307,4852,287,110,65,6,33,63,1375,67,6716,355,7071,4689,2320,62,3610,1482,1067,96,54.2,22.3,16.1,1.5
Kern,406712,273461,99337,133162,6897,752,1417,233,598,726,30339,469,126046,34299,160345,121431,38914,0,96965,29459,26176,1055,61.7,18.8,16.7,0.7
Kings,66620,46585,18325,22015,914,109,139,43,59,539,4442,48,16149,7341,23490,15573,6184,1733,12539,5174,3835,155,56.6,23.4,17.3,0.7
Lake,44871,30187,13603,10260,857,519,217,32,108,131,4460,43,12170,6308,18478,9799,8149,530,8003,5137,2564,519,47.1,30.3,15.1,3.1
Lassen,16075,14821,4762,6509,634,72,104,17,34,79,2610,30,6531,2446,8977,6671,2178,128,5167,1306,1505,98,60.9,15.4,17.8,1.2
Los Angeles,5602765,3996700,2055962,1100758,68533,29105,20448,16647,35053,28582,641612,1786,1688701,515137,2203838,984222,1024341,195275,878747,735066,217404,51399,44.9,37.5,11.1,2.7
Madera,70981,43697,15660,21981,858,230,199,39,46,202,4482,99,16969,13769,30738,21113,8071,1554,16034,6216,5923,267,55.0,21.3,20.3,1.0
Marin,176581,143271,71445,36654,2438,4354,826,175,384,571,26424,192,68911,40126,109037,35050,72806,1181,31321,46784,9955,5539,32.1,47.9,10.2,5.7
Mariposa,13682,11774,3841,5579,330,178,98,11,39,222,1476,21,4489,3033,7522,4640,2240,642,3463,1490,1550,171,50.1,21.6,22.5,2.5
Mendocino,60938,47464,21533,12818,1239,2784,392,62,307,345,7984,106,21753,7932,29685,11900,16265,1520,9949,10510,2909,1934,37.2,39.3,10.9,7.3
Merced,124008,91107,43093,37963,1465,300,241,48,150,148,7699,114,32268,11241,43509,26641,15361,1507,20267,11191,7128,378,50.9,28.1,17.9,1.0
Modoc,6582,5259,1801,2551,154,26,41,3,7,14,662,20,2673,836,3509,2544,885,80,1909,453,636,30,60.5,14.4,20.2,1.0
Mono,9587,5979,1847,2536,182,128,66,3,16,0,1201,13,2825,877,3702,2174,1220,308,1859,772,430,79,56.7,23.6,13.2,2.5
Monterey,224201,150802,71396,51040,2846,1566,720,155,418,474,22187,91,50316,47636,97952,45222,51711,1019,37553,32139,10446,2432,41.1,35.2,11.5,2.7
Napa,86617,64374,29415,21752,1447,955,431,68,147,589,9570,114,30941,14128,45069,19839,23540,1690,16097,14115,7067,1856,39.6,34.7,17.4,4.6
Nevada,74389,61059,19079,27810,1332,1941,527,53,125,328,9864,90,24586,20208,44794,27201,16078,1515,22607,9534,6610,1851,53.9,22.8,15.8,4.5
Orange,1802699,1346003,420104,654191,25640,7661,9699,2811,3486,6817,215594,650,564469,255383,819852,589700,214718,15434,493850,130808,119504,11818,63.5,16.9,15.4,1.6
Placer,199151,165419,48372,86744,3128,1336,1056,84,278,552,23869,269,79887,44474,124361,88040,34128,2193,74764,19706,18825,3081,62.8,16.6,15.9,2.6
Plumas,16190,12693,4482,5566,393,110,80,13,38,58,1953,29,5116,3709,8825,6049,2776,0,4636,1709,1591,222,54.7,20.2,18.8,2.7
Riverside,1051221,659370,228574,319522,13887,2633,3493,1028,2350,4494,83389,833,286747,126217,412964,283923,119485,9556,239584,84683,53998,4235,60.9,21.6,13.8,1.1
Sacramento,865177,615187,267791,221718,13345,6235,3266,703,5454,2333,94342,677,269620,134480,404100,226567,153475,24058,195435,98877,52046,14247,52.4,26.5,14.0,3.9
San Benito,34566,25775,11575,8941,591,211,170,19,74,136,4058,53,9984,4646,14630,7978,6526,126,6452,4213,1836,307,48.7,31.8,13.9,2.4
San Bernardino,1097027,646444,253715,281477,15024,2666,3217,863,2751,5183,81548,803,296693,90337,387030,259719,111014,16297,218989,78718,52636,4575,60.2,21.7,14.5,1.3
San Diego,1945375,1296322,449233,541973,28616,10590,9654,5772,3276,9002,238206,1421,619031,245040,864071,530269,275151,58651,485563,192605,97198,17721,59.5,23.7,12.0,2.2
San Francisco,580024,454931,247502,57839,7808,14698,2853,989,2389,1131,119722,563,187647,81496,269143,52177,212763,4203,44665,149237,13694,14950,19.0,63.2,5.8,6.4
San Joaquin,371925,248293,106744,109623,3826,937,870,140,2121,1860,22172,351,97607,44389,141996,85153,53347,3496,63905,35868,25699,2117,48.6,27.3,19.6,1.7
San Luis Obispo,185560,137290,46772,60739,3100,2538,978,185,327,1971,20680,108,56458,39156,95614,58668,34147,2799,44665,23177,16630,2469,49.6,25.8,18.5,2.8
San Mateo,465267,342488,170002,89983,6274,4308,1895,534,1031,950,67511,422,139535,79964,219499,80109,135210,4180,68191,86854,23454,8224,35.0,44.5,12.1,4.3
Santa Barbara,266554,193458,75843,72362,3795,3932,1313,223,355,2705,32930,287,75046,52356,127402,71558,53204,2634,55473,36171,19559,3329,46.7,30.5,16.5,2.9
Santa Clara,1053457,766874,346855,223944,14084,7168,5497,909,2769,2915,162733,867,344825,115836,460661,182332,250579,27750,160807,163768,51069,15694,39.2,39.9,12.5,3.9
Santa Cruz,176024,129901,66551,29680,2153,6301,1279,209,513,1220,21995,168,62449,32310,94759,32939,59602,2218,28926,39828,7735,6044,33.3,45.9,9.0,7.0
Shasta,124666,88269,28238,43197,2485,570,639,62,204,283,12591,73,39500,18674,58174,40874,15833,1467,31949,9441,11177,633,57.9,17.1,20.3,1.2
Sierra,2547,2349,742,991,90,30,32,1,8,30,425,22,0,1632,1632,1007,457,168,842,269,285,46,55.9,17.9,19.0,3.1
Siskiyou,32382,26132,9605,10980,782,277,293,110,71,57,3957,82,11711,4626,16337,11378,4648,311,8974,3070,2403,195,58.6,20.1,15.7,1.3
Solano,265718,173144,85002,52563,3587,1126,809,143,496,1065,28353,243,80518,30937,111455,52151,53660,5644,43122,34441,15548,2603,43.4,34.7,15.7,2.7
Sonoma,328858,230601,114474,65516,4278,7482,1627,246,743,1597,34638,262,97926,74842,172768,66251,101396,5121,54651,63588,21202,8554,35.0,40.7,13.6,5.5
Stanislaus,297582,203214,88091,87798,3502,704,712,124,1441,1740,19102,164,66684,43410,110094,66938,39805,3351,46811,25034,24425,1673,46.5,24.9,24.3,1.7
Sutter,52495,38751,12930,19689,869,141,188,18,138,1288,3490,60,15365,8941,24306,17958,5244,1104,14919,3459,3957,259,64.6,15.0,17.2,1.2
Tehama,39749,28270,10201,12604,1104,127,220,17,90,194,3713,38,13097,5436,18533,13384,4954,195,10038,2772,3586,175,58.1,16.1,20.8,1.1
Trinity,10137,7406,2758,3065,242,137,84,13,29,102,976,23,3225,2025,5250,3249,1835,166,2518,1057,815,127,52.8,22.2,17.1,2.7
Tulare,213958,131694,47581,64213,2889,513,524,146,354,324,15150,164,57998,18376,76374,53893,20818,1663,40678,16943,11391,472,55.5,23.2,15.6,0.7
Tuolumne,38116,31078,11874,13641,824,338,197,27,78,204,3895,75,15495,6271,21766,13438,7637,691,10097,4799,4475,481,49.6,23.6,22.0,2.4
Ventura,502850,363881,138693,153943,7504,3481,2190,601,927,3362,53180,517,162424,77664,240088,148538,85484,6066,116722,53705,44408,4778,51.5,23.7,19.6,2.2
Yolo,118849,82445,38607,24424,1657,1995,421,87,453,685,14116,69,34408,21597,56005,27778,27936,291,22375,19489,6061,3029,42.2,36.8,11.5,5.8
Yuba,38089,25560,9270,11182,879,184,159,14,96,50,3726,45,10212,4415,14627,10905,3589,133,8632,2301,2295,225,61.9,16.5,16.5,1.7"""
df=pd.read_csv(io.StringIO(RAW),header=None,names=COLS)
REG={"Bay Area":"Alameda,Contra Costa,Marin,Napa,San Francisco,San Mateo,Santa Clara,Solano,Sonoma","Los Angeles":"Los Angeles","Southern California":"Orange,San Diego,Ventura,Imperial","Inland Empire":"Riverside,San Bernardino","Central Coast":"Monterey,San Benito,San Luis Obispo,Santa Barbara,Santa Cruz","San Joaquin Valley":"Fresno,Kern,Kings,Madera,Merced,San Joaquin,Stanislaus,Tulare","Sacramento Region":"Sacramento,Yolo,Placer,El Dorado,Sutter,Yuba","Sierra & Foothills":"Alpine,Amador,Calaveras,Inyo,Mariposa,Mono,Nevada,Plumas,Sierra,Tuolumne","North State":"Butte,Colusa,Del Norte,Glenn,Humboldt,Lake,Lassen,Mendocino,Modoc,Shasta,Siskiyou,Tehama,Trinity"}
rmap={c:r for r,v in REG.items() for c in v.split(",")}
SYS={"Punch card (Datavote)":"Alpine,Calaveras,Del Norte,El Dorado,Glenn,Imperial,Inyo,Monterey,San Benito,Tehama,Ventura,Yolo,Yuba","Punch card (Votomatic)":"Los Angeles,Mendocino,San Diego,Sierra,Solano","Punch card (Pollstar)":"Sacramento,Santa Clara","Touch screen":"Riverside,Shasta,Alameda,Plumas"}
smap={c:s for s,v in SYS.items() for c in v.split(",")}
df.insert(1,"region",df.county.map(rmap)); df.insert(2,"voting_system",df.county.map(lambda c:smap.get(c,"Mark-sense (optical scan)")))
assert df.region.notna().all() and len(df)==58
# ---- validation against certified statewide totals
OFF=dict(registered=15380536,reg_dem=6718111,reg_rep=5429356,ballots_total=9413494,recall_yes=4976274,recall_no=4007783,arnold=4206284,bustamante=2724874,mcclintock=1161287,camejo=242247)
val={k:{"dataset_sum":int(df[k].sum()),"official":v,"diff":int(df[k].sum()-v)} for k,v in OFF.items()}
bad={k:v for k,v in val.items() if v["diff"]!=0}
print("VALIDATION mismatches:",bad or "none")
# ---- derived variables
d=df.copy()
d["turnout_reg"]=d.ballots_total/d.registered
d["yes_pct"]=d.recall_yes/(d.recall_yes+d.recall_no)
for p in ["dem","rep","dts","green"]: d[p+"_share"]=d["reg_"+p]/d.registered
d["gov_votes_est"]=d.arnold/(d.arnold_pct_rep/100)
for c in ["arnold","bustamante","mcclintock","camejo"]: d[c+"_share_ballots"]=d[c]/d.ballots_total
d["rep_cand_share_ballots"]=(d.arnold+d.mcclintock)/d.ballots_total
d["arnold_plurality"]=(d.arnold>d[["bustamante","mcclintock","camejo"]].max(axis=1))
d["yes_majority"]=d.yes_pct>0.5
d.to_csv("county_data.csv",index=False)
w=d.ballots_total
def wcorr(x,y,w):
    mx,my=np.average(x,weights=w),np.average(y,weights=w)
    return float(np.sum(w*(x-mx)*(y-my))/np.sqrt(np.sum(w*(x-mx)**2)*np.sum(w*(y-my)**2)))
R={"validation":val}
R["statewide"]=dict(ballots=int(d.ballots_total.sum()),yes=int(d.recall_yes.sum()),no=int(d.recall_no.sum()),yes_share=float(d.recall_yes.sum()/(d.recall_yes.sum()+d.recall_no.sum())),
  recall_votes=int(d.recall_yes.sum()+d.recall_no.sum()),gov_votes=int(d.ballots_total.sum()-755575),skipped_replacement_vs_recall=int((d.recall_yes.sum()+d.recall_no.sum())-(d.ballots_total.sum()-755575)),
  arnold_margin_over_bust=int(d.arnold.sum()-d.bustamante.sum()),yes_margin=int(d.recall_yes.sum()-d.recall_no.sum()),
  counties_yes_majority=int(d.yes_majority.sum()),counties_arnold_plurality=int(d.arnold_plurality.sum()),
  counties_bust_plurality=int((d.bustamante>d[["arnold","mcclintock","camejo"]].max(axis=1)).sum()),
  rep_candidates_votes=int(d.arnold.sum()+d.mcclintock.sum()),dem_green_cands_votes=int(d.bustamante.sum()+d.camejo.sum()))
S=R["statewide"]; S["gov_pct"]={k:float(d[k].sum()/S["gov_votes"]) for k in ["arnold","bustamante","mcclintock","camejo"]}
S["switch_for_tie_arnold_to_bust"]=int(np.ceil(S["arnold_margin_over_bust"]/2)); S["switch_for_tie_recall"]=int(np.ceil(S["yes_margin"]/2))
S["reg_share"]=dict(dem=float(d.reg_dem.sum()/d.registered.sum()),rep=float(d.reg_rep.sum()/d.registered.sum()),dts=float(d.reg_dts.sum()/d.registered.sum()))
# ---- correlations
R["corr_unweighted"]={k:float(np.corrcoef(d[k],d.yes_pct)[0,1]) for k in ["rep_share","dem_share","dts_share","turnout_reg"]}
R["corr_weighted"]={k:wcorr(d[k].values,d.yes_pct.values,w.values) for k in ["rep_share","dem_share","dts_share","turnout_reg"]}
R["corr_arnold_pct_vs"]={k:float(np.corrcoef(d[k],d.arnold_pct_rep)[0,1]) for k in ["rep_share","dem_share","dts_share"]}
R["corr_bust_pct_vs_dem"]=float(np.corrcoef(d.dem_share,d.bustamante_pct_rep)[0,1])
# ---- WLS with HC1 robust SE (numpy)
def wls(y,X,w,names):
    X=np.column_stack([np.ones(len(y))]+X); W=np.diag(w/np.mean(w)); XtWX=np.linalg.inv(X.T@W@X); b=XtWX@X.T@W@y
    e=y-X@b; n,k=X.shape; meat=X.T@np.diag((w/np.mean(w))**2*e**2)@X; V=XtWX@meat@XtWX*n/(n-k); se=np.sqrt(np.diag(V))
    r2=1-np.sum(w*e**2)/np.sum(w*(y-np.average(y,weights=w))**2)
    return {"names":["const"]+names,"coef":b.tolist(),"se":se.tolist(),"r2_w":float(r2),"n":int(n)}
R["wls_yes"]=wls(d.yes_pct.values,[d.rep_share.values,d.dem_share.values],w.values,["rep_share","dem_share"])
R["wls_arnold"]=wls((d.arnold_pct_rep/100).values,[d.rep_share.values,d.dem_share.values],w.values,["rep_share","dem_share"])
R["wls_bust"]=wls((d.bustamante_pct_rep/100).values,[d.rep_share.values,d.dem_share.values],w.values,["rep_share","dem_share"])
R["wls_mcc"]=wls((d.mcclintock_pct_rep/100).values,[d.rep_share.values,d.dem_share.values],w.values,["rep_share","dem_share"])
R["wls_yes_turnout"]=wls(d.yes_pct.values,[d.rep_share.values,d.dem_share.values,d.turnout_reg.values],w.values,["rep_share","dem_share","turnout_reg"])
# ---- regional summary (ballot-weighted)
def agg(g):
    t=g.ballots_total.sum(); gv=g.gov_votes_est.sum()
    return pd.Series(dict(counties=len(g),ballots=int(t),registered=int(g.registered.sum()),rep_reg=g.reg_rep.sum()/g.registered.sum(),dem_reg=g.reg_dem.sum()/g.registered.sum(),
      yes_pct=g.recall_yes.sum()/(g.recall_yes.sum()+g.recall_no.sum()),arnold_pct=g.arnold.sum()/gv,bust_pct=g.bustamante.sum()/gv,mcc_pct=g.mcclintock.sum()/gv,turnout=t/g.registered.sum()))
reg=d.groupby("region").apply(agg).sort_values("ballots",ascending=False); R["regions"]=reg.reset_index().to_dict("records")
# ---- Arnold over/under-performance vs Republican registration
d["arnold_minus_rep_reg"]=d.arnold_pct_rep/100-d.rep_share
d["repcands_minus_rep_reg"]=(d.arnold_pct_rep+d.mcclintock_pct_rep)/100-d.rep_share
R["outperf"]={"mean_unweighted":float(d.arnold_minus_rep_reg.mean()),"min":d.loc[d.arnold_minus_rep_reg.idxmin(),["county","arnold_minus_rep_reg"]].tolist(),"max":d.loc[d.arnold_minus_rep_reg.idxmax(),["county","arnold_minus_rep_reg"]].tolist(),
 "repcands_minus_repreg_weighted":float(np.average(d.repcands_minus_rep_reg,weights=w)),"counties_repcands_exceed_repreg":int((d.repcands_minus_rep_reg>0).sum())}
# ---- history (SOS table) : 2002 general vs 2003 special
R["history"]=dict(g2002=dict(reg=15303469,dem=6825400,rep=5388895,voters=7738821),s2003=dict(reg=15383526,dem=6718111,rep=5429256,voters=9413494),g2004=dict(reg=16557273,voters=12589683))
H=R["history"]; H["turnout_2002"]=H["g2002"]["voters"]/H["g2002"]["reg"]; H["turnout_2003"]=H["s2003"]["voters"]/H["s2003"]["reg"]; H["added_voters"]=H["s2003"]["voters"]-H["g2002"]["voters"]
# ---- top/bottom counties
R["top_yes"]=d.nlargest(5,"yes_pct")[["county","yes_pct"]].values.tolist(); R["bottom_yes"]=d.nsmallest(5,"yes_pct")[["county","yes_pct"]].values.tolist()
R["largest5"]=d.nlargest(5,"ballots_total")[["county","ballots_total","yes_pct","arnold_pct_rep","bustamante_pct_rep"]].values.tolist()
R["bust_win_counties"]=d[d.bustamante>d[["arnold","mcclintock","camejo"]].max(axis=1)].county.tolist()
R["yes_minority_counties"]=d[~d.yes_majority].county.tolist()
d.to_csv("county_data.csv",index=False)
json.dump(R,open("results.json","w"),indent=1,default=float)
print(json.dumps({k:R[k] for k in ["statewide","corr_unweighted","corr_weighted","wls_yes","wls_arnold","wls_bust","outperf","history"]},indent=1,default=float))
print(reg.round(3).to_string()); print(R["bust_win_counties"],R["yes_minority_counties"])
