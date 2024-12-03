#import numpy as np
l1 = [
    35446,
    46314,
    33933,
    83974,
    98207,
    38488,
    95930,
    52767,
    16477,
    14481,
    29083,
    36158,
    61387,
    76932,
    36700,
    90500,
    55528,
    31179,
    22822,
    23069,
    69000,
    91611,
    10965,
    62470,
    38922,
    88317,
    49184,
    46731,
    56390,
    67724,
    60777,
    38607,
    89620,
    19492,
    12399,
    14491,
    89224,
    92053,
    61752,
    14662,
    62308,
    63106,
    98323,
    10130,
    44468,
    55055,
    21162,
    62629,
    64760,
    59948,
    93112,
    19027,
    68050,
    39607,
    72923,
    59390,
    33001,
    70458,
    36441,
    44963,
    56327,
    35920,
    56574,
    19886,
    10538,
    43629,
    40166,
    71819,
    71239,
    84091,
    27282,
    61675,
    13092,
    22564,
    73337,
    65255,
    14204,
    90941,
    12650,
    39913,
    91204,
    12353,
    86940,
    45417,
    93805,
    86595,
    95504,
    49450,
    54656,
    24239,
    39200,
    45741,
    86169,
    30646,
    28947,
    27981,
    74967,
    28791,
    58805,
    41082,
    49770,
    40558,
    38248,
    51400,
    20599,
    77640,
    54049,
    82155,
    88848,
    74986,
    84534,
    52277,
    27375,
    82985,
    44699,
    56937,
    77717,
    97383,
    94620,
    93133,
    63717,
    13006,
    20078,
    68979,
    97191,
    47911,
    48256,
    34443,
    44941,
    43750,
    16717,
    36163,
    29877,
    54069,
    21897,
    46002,
    47632,
    92150,
    47440,
    21000,
    22797,
    67853,
    30016,
    65558,
    46885,
    49714,
    40300,
    97130,
    89917,
    99566,
    53392,
    92478,
    69059,
    88594,
    25017,
    66050,
    18086,
    44548,
    91368,
    90745,
    50489,
    29928,
    81859,
    74633,
    98553,
    80866,
    24016,
    36650,
    19561,
    63484,
    58451,
    29016,
    54718,
    89003,
    68471,
    88206,
    13290,
    86949,
    77758,
    75063,
    99425,
    71300,
    88500,
    78917,
    43065,
    33189,
    46705,
    56972,
    24844,
    57908,
    15446,
    76421,
    98232,
    37640,
    35383,
    11291,
    62140,
    55579,
    83570,
    76450,
    84820,
    24416,
    45763,
    82938,
    65397,
    45162,
    71395,
    72027,
    85465,
    32751,
    65455,
    79640,
    88492,
    66028,
    23677,
    22716,
    62036,
    18882,
    24085,
    97952,
    16125,
    69534,
    42997,
    45250,
    84290,
    22335,
    47550,
    36928,
    40790,
    41540,
    16448,
    44580,
    35045,
    69798,
    50519,
    69580,
    87702,
    57895,
    20766,
    74455,
    33358,
    80944,
    71806,
    88258,
    21771,
    88011,
    95793,
    95847,
    56747,
    32448,
    93453,
    72594,
    52172,
    93959,
    74332,
    79878,
    49680,
    18265,
    95331,
    18366,
    25504,
    62474,
    31197,
    66986,
    63340,
    69519,
    21052,
    72184,
    43404,
    95052,
    27977,
    13673,
    13363,
    82059,
    52928,
    55266,
    55292,
    66838,
    85014,
    18772,
    99322,
    68363,
    45148,
    63006,
    92687,
    55913,
    45593,
    79018,
    87110,
    66328,
    54561,
    56406,
    95001,
    12373,
    65064,
    17403,
    58690,
    50959,
    40939,
    50275,
    73990,
    39728,
    64531,
    44868,
    72719,
    35784,
    13911,
    45218,
    27025,
    64719,
    22135,
    13725,
    16787,
    26004,
    83956,
    20869,
    92705,
    41237,
    47868,
    46965,
    76833,
    10593,
    91447,
    41369,
    88036,
    56077,
    83258,
    17955,
    47587,
    71731,
    43926,
    26878,
    85135,
    13199,
    55583,
    72584,
    10908,
    59612,
    72725,
    22111,
    15422,
    51152,
    14804,
    62625,
    89653,
    13230,
    83705,
    88216,
    30601,
    86040,
    76367,
    17566,
    49688,
    51987,
    99083,
    50529,
    18618,
    49357,
    83692,
    34017,
    34588,
    79808,
    76557,
    52422,
    99664,
    23712,
    10628,
    35405,
    55143,
    97421,
    17759,
    94690,
    40501,
    41037,
    70591,
    64400,
    25588,
    92616,
    65267,
    21298,
    21216,
    83830,
    69200,
    92744,
    84255,
    60019,
    72406,
    80749,
    81952,
    80454,
    32161,
    96805,
    87229,
    52706,
    54224,
    59272,
    39664,
    52726,
    17451,
    53896,
    72032,
    41654,
    45801,
    59531,
    69619,
    47931,
    37408,
    46419,
    24027,
    87213,
    59190,
    91014,
    20262,
    99705,
    77899,
    66940,
    96845,
    85833,
    24005,
    70935,
    80570,
    14398,
    34541,
    28018,
    87037,
    71966,
    46070,
    28730,
    37205,
    78756,
    92078,
    84234,
    65644,
    69979,
    26206,
    10787,
    25443,
    16577,
    83988,
    12284,
    57347,
    25269,
    26028,
    28804,
    50690,
    79036,
    70738,
    66916,
    81977,
    43130,
    97899,
    50454,
    77142,
    20238,
    25279,
    37235,
    49627,
    40512,
    84237,
    57852,
    60277,
    60816,
    48621,
    48990,
    90883,
    32060,
    47930,
    53524,
    76420,
    12331,
    93348,
    21092,
    80416,
    18172,
    83267,
    56035,
    19129,
    31465,
    64173,
    74397,
    20717,
    51944,
    71053,
    80370,
    68857,
    48914,
    41820,
    31445,
    12669,
    79174,
    45196,
    43488,
    49986,
    65806,
    48018,
    86144,
    95852,
    47095,
    96313,
    39688,
    89088,
    10994,
    44290,
    32871,
    74126,
    59913,
    37148,
    56032,
    92348,
    76049,
    28805,
    35070,
    40283,
    32870,
    87890,
    85129,
    89021,
    54444,
    60250,
    82877,
    13101,
    95310,
    99602,
    39771,
    92562,
    26053,
    99211,
    31519,
    66988,
    55719,
    47519,
    81355,
    64580,
    53953,
    28575,
    88211,
    25538,
    35298,
    11466,
    33575,
    86250,
    84467,
    59023,
    81764,
    80503,
    73651,
    74173,
    59081,
    54695,
    25202,
    90138,
    87761,
    76616,
    98411,
    87945,
    69634,
    94813,
    64622,
    46511,
    49212,
    34375,
    64884,
    94136,
    89737,
    45383,
    60780,
    60956,
    27402,
    61698,
    77163,
    30740,
    78975,
    34208,
    74233,
    95918,
    74949,
    41203,
    27671,
    38515,
    82734,
    70727,
    10326,
    83563,
    46938,
    43092,
    96771,
    32365,
    65514,
    21151,
    53822,
    89965,
    97207,
    18794,
    85061,
    29500,
    86025,
    18550,
    92402,
    58049,
    47165,
    40002,
    82066,
    99593,
    95278,
    23474,
    26508,
    13412,
    58286,
    79549,
    59275,
    59102,
    59475,
    71391,
    64011,
    34907,
    96020,
    32676,
    82228,
    85683,
    84073,
    89790,
    79448,
    57726,
    30683,
    27124,
    13404,
    47973,
    75389,
    39880,
    47176,
    77298,
    36334,
    55391,
    75215,
    89669,
    36393,
    79118,
    81448,
    51834,
    40739,
    52754,
    35389,
    31791,
    44345,
    11231,
    21968,
    78789,
    81898,
    22004,
    50202,
    83592,
    58853,
    42190,
    45830,
    81738,
    99265,
    90691,
    38908,
    20275,
    24933,
    71243,
    67641,
    63940,
    16484,
    95114,
    52206,
    45310,
    76892,
    71763,
    28803,
    19132,
    62482,
    20185,
    53459,
    86711,
    25418,
    41208,
    18696,
    25923,
    90443,
    84272,
    58778,
    83614,
    46699,
    76064,
    99080,
    18497,
    60862,
    19752,
    22338,
    66112,
    41917,
    50594,
    15550,
    61435,
    96294,
    47560,
    60387,
    76943,
    78435,
    57089,
    97691,
    30869,
    51101,
    89100,
    28552,
    50599,
    62850,
    97312,
    81531,
    69183,
    88793,
    48548,
    66705,
    71169,
    55885,
    55064,
    59988,
    89486,
    66564,
    21432,
    69247,
    15787,
    91085,
    14618,
    99031,
    80969,
    68503,
    89919,
    97125,
    36492,
    50873,
    50741,
    27193,
    13260,
    70660,
    23872,
    23133,
    18937,
    84631,
    31466,
    82842,
    96642,
    99278,
    37578,
    87003,
    43407,
    73286,
    45369,
    60219,
    92605,
    80646,
    29493,
    64968,
    67454,
    39669,
    45812,
    98524,
    68102,
    33914,
    90204,
    78331,
    41990,
    98264,
    12657,
    14876,
    86663,
    81960,
    94521,
    84699,
    65933,
    69417,
    77051,
    75075,
    33494,
    49618,
    71385,
    72195,
    62025,
    23253,
    70062,
    14577,
    72180,
    92457,
    91879,
    49809,
    73214,
    63136,
    25107,
    77516,
    84079,
    68470,
    80077,
    33487,
    98439,
    25106,
    29578,
    41763,
    38888,
    21105,
    27547,
    34649,
    98652,
    26548,
    91140,
    88522,
    18801,
    88360,
    54575,
    54004,
    50564,
    19887,
    65566,
    13908,
    38021,
    53431,
    63143,
    77152,
    95334,
    99112,
    22226,
    81497,
    56613,
    32899,
    73926,
    14710,
    81998,
    51537,
    92298,
    61627,
    25800,
    89153,
    15490,
    98839,
    88591,
    47330,
    94242,
    30493,
    47111,
    76006,
    88435,
    12581,
    52999,
    64534,
    70617,
    78842,
    72607,
    44479,
    32783,
    27725,
    71384,
    75007,
    25465,
    97702,
    87869,
    85114,
    67686,
    22260,
    67159,
    97547,
    26163,
    90733,
    62958,
    87531,
    28421,
    31349,
    62113,
    59754,
    82004,
    69805,
    73669,
    36269,
    35228,
    38938,
    88675,
    90579,
    89858,
    19686,
    16625,
    91432,
    17607,
    89530,
    40107,
    28095,
    93573,
    85006,
    19091,
    82765,
    20545,
    24106,
    60438,
    27926,
    97985,
    79204,
    91051,
    75382,
    50290,
    66045,
    61679,
    46984,
    18043,
    53300,
    57214,
    11949,
    45225,
    82542,
    11498,
    44155,
    97659,
    64945,
    10456,
    66710,
    52752,
    21492,
    10804,
    53427,
    81459,
    24486,
    94315,
    99345,
    26426,
    59747,
    78335,
    76856,
    38024,
    76867,
    25261,
    21948,
    25796,
    26541,
    85517,
    51634,
    16886,
    94563,
    94244,
    19517,
    15629,
    13661,
    54946,
    69496,
    10488,
    92729,
    28136,
    55489,
    34355,
    75542,
    70632,
    29904,
    73989,
    86241,
    82353,
    78028,
    92984,
    55747,
    17389,
    94992,
    69555,
    66820,
    96784,
    19019,
    67383,
    64708,
    20616,
    22213,
    34850,
    99572,
    76670,
    11930,
    18321,
    42025,
    99887,
    95958,
    44579,
    79387,
    82753,
    93967,
    90819,
    38322,
    10019,
    78459,
    69905,
    14796,
    14487,
    79979,
    59836,
    37308,
    63835,
    30048,
    71914,
    76352,
    74621,
    33804,
    23449,
    99868,
    57457,
    44296,
    43642,
    49243,
    28205,
    98899
]

l2 = [
    18696,
    66062,
    83974,
    34443,
    12657,
    57125,
    81859,
    12657,
    53659,
    84757,
    51122,
    15438,
    10295,
    66328,
    83181,
    70317,
    55820,
    94554,
    16886,
    99080,
    50666,
    49688,
    12657,
    27096,
    83974,
    67082,
    78816,
    90213,
    89965,
    21120,
    88500,
    91051,
    42599,
    59958,
    89965,
    21092,
    65224,
    89616,
    33001,
    46961,
    99609,
    37570,
    89620,
    47868,
    92294,
    99080,
    23460,
    83614,
    76835,
    58492,
    81859,
    67250,
    27547,
    27547,
    77124,
    45817,
    47868,
    64427,
    47868,
    70577,
    83974,
    89031,
    16410,
    20797,
    56032,
    89965,
    54408,
    87037,
    58805,
    36969,
    83974,
    83974,
    65566,
    69172,
    83623,
    88498,
    49627,
    12657,
    65455,
    16886,
    42662,
    24980,
    43602,
    86117,
    13685,
    32060,
    49974,
    18696,
    82794,
    65070,
    94275,
    65455,
    41093,
    56972,
    45593,
    18232,
    83592,
    27193,
    69918,
    52767,
    52767,
    92562,
    72945,
    16886,
    11817,
    81133,
    56972,
    36807,
    49688,
    21092,
    83372,
    53938,
    46406,
    44993,
    83974,
    87037,
    49519,
    12353,
    17706,
    79684,
    33001,
    56032,
    55429,
    18696,
    84071,
    62971,
    56784,
    47868,
    56972,
    83153,
    42999,
    79265,
    82188,
    59608,
    70982,
    35871,
    28298,
    34443,
    90606,
    89334,
    91051,
    81395,
    59612,
    65566,
    12353,
    12353,
    27547,
    33789,
    70893,
    49688,
    56972,
    44580,
    12657,
    66111,
    51845,
    49129,
    33001,
    56032,
    26310,
    82691,
    65566,
    45682,
    89620,
    95869,
    47868,
    49688,
    20910,
    33001,
    74850,
    49688,
    18696,
    32060,
    25325,
    33001,
    11145,
    89620,
    66328,
    22014,
    88623,
    96681,
    31778,
    62538,
    11195,
    56972,
    88068,
    89088,
    83036,
    50663,
    91051,
    63316,
    88452,
    36179,
    25703,
    49688,
    44539,
    12353,
    83592,
    88733,
    87934,
    35834,
    47091,
    78402,
    65455,
    66922,
    65566,
    18361,
    72305,
    97029,
    28881,
    65455,
    80742,
    10727,
    84005,
    32752,
    43498,
    26101,
    87090,
    82877,
    91061,
    56032,
    12353,
    44480,
    33448,
    68695,
    92562,
    32582,
    99080,
    73869,
    11220,
    71545,
    67875,
    45593,
    70157,
    63807,
    97965,
    16886,
    24341,
    58808,
    27547,
    59612,
    83592,
    78627,
    29266,
    82877,
    64556,
    25173,
    49627,
    45593,
    12657,
    12657,
    50250,
    74557,
    18099,
    70300,
    38126,
    67746,
    54928,
    33001,
    59612,
    33001,
    88500,
    60901,
    29540,
    49688,
    88500,
    27915,
    52553,
    27193,
    49627,
    59327,
    83614,
    18696,
    27547,
    47868,
    82877,
    25800,
    89620,
    81751,
    62704,
    89391,
    39583,
    58608,
    58708,
    27193,
    12754,
    75671,
    65455,
    51305,
    56230,
    14246,
    53594,
    14740,
    49947,
    81859,
    16886,
    75896,
    53427,
    27547,
    52963,
    47946,
    32060,
    49688,
    74946,
    56972,
    27906,
    16310,
    26147,
    21092,
    54743,
    65566,
    12657,
    71262,
    49149,
    27547,
    25800,
    65750,
    49627,
    33001,
    54678,
    44772,
    67617,
    96338,
    12858,
    18696,
    97875,
    40100,
    73796,
    99080,
    12353,
    21884,
    76598,
    21142,
    21092,
    91051,
    72621,
    63423,
    82877,
    45593,
    95288,
    82877,
    16886,
    97377,
    61202,
    53427,
    38262,
    39503,
    39416,
    34340,
    23296,
    70921,
    32060,
    62842,
    26555,
    27192,
    16886,
    28284,
    92562,
    27193,
    27547,
    12353,
    65455,
    56032,
    83614,
    73787,
    83974,
    89620,
    79497,
    89633,
    97586,
    13687,
    32060,
    46885,
    39940,
    85460,
    40719,
    83974,
    12353,
    83974,
    12288,
    82152,
    24498,
    95148,
    34443,
    83974,
    72646,
    33001,
    89620,
    83614,
    73514,
    27193,
    15624,
    12657,
    45593,
    21688,
    33221,
    81859,
    89965,
    88500,
    53746,
    58280,
    56972,
    83606,
    76761,
    56972,
    65455,
    88500,
    15916,
    27677,
    99080,
    89400,
    71907,
    77947,
    52969,
    17001,
    98899,
    12657,
    16886,
    89620,
    72223,
    48677,
    92562,
    81859,
    83183,
    92562,
    90231,
    34443,
    83974,
    56032,
    65566,
    83974,
    88687,
    22235,
    83974,
    57474,
    40074,
    70635,
    81859,
    86943,
    11918,
    12657,
    16886,
    45386,
    52805,
    77340,
    72129,
    63115,
    71491,
    96652,
    46885,
    58805,
    98026,
    97303,
    33793,
    99451,
    49627,
    83614,
    84495,
    15742,
    18675,
    65767,
    53427,
    99080,
    62202,
    65455,
    47035,
    33001,
    56032,
    55589,
    16886,
    72983,
    48516,
    40456,
    62693,
    66930,
    47868,
    31836,
    12657,
    83592,
    33001,
    70918,
    12819,
    72328,
    27547,
    56032,
    90951,
    33001,
    53931,
    99080,
    38918,
    56972,
    22048,
    27193,
    39514,
    85882,
    89620,
    92562,
    58805,
    89620,
    45593,
    86998,
    56972,
    27193,
    45593,
    49668,
    69396,
    35109,
    83974,
    24108,
    23837,
    45593,
    74542,
    46272,
    47868,
    21092,
    11410,
    84836,
    23016,
    52767,
    15651,
    99080,
    66125,
    44178,
    87037,
    61194,
    67527,
    81299,
    52767,
    14876,
    89620,
    34142,
    37927,
    67645,
    83371,
    40028,
    23345,
    96106,
    33194,
    66440,
    12353,
    18696,
    59305,
    53562,
    91051,
    58973,
    18696,
    65455,
    65566,
    38453,
    27547,
    43565,
    53680,
    98899,
    26486,
    12657,
    89620,
    64725,
    92562,
    21092,
    18696,
    70971,
    23916,
    81859,
    95813,
    59612,
    16739,
    34100,
    56032,
    25216,
    78097,
    74327,
    83974,
    99080,
    88571,
    14179,
    47868,
    65566,
    47868,
    56032,
    20386,
    92813,
    25800,
    33001,
    45593,
    58588,
    65566,
    57693,
    21390,
    25800,
    91810,
    66328,
    49039,
    20005,
    23172,
    82877,
    93001,
    29962,
    74091,
    69893,
    16886,
    82877,
    81859,
    71414,
    12657,
    82877,
    33508,
    32060,
    78711,
    35717,
    25448,
    87684,
    83592,
    65455,
    49481,
    27193,
    27193,
    65566,
    48353,
    64987,
    33001,
    49627,
    91054,
    42717,
    66328,
    65566,
    74353,
    65566,
    32110,
    32060,
    90141,
    25763,
    75035,
    32060,
    40175,
    50282,
    27719,
    33001,
    21092,
    47868,
    49990,
    49688,
    56972,
    36568,
    30926,
    27193,
    58125,
    32060,
    12353,
    62528,
    84635,
    69626,
    51107,
    79346,
    68523,
    99080,
    12353,
    99469,
    38910,
    20889,
    89965,
    24939,
    83614,
    13684,
    34940,
    46405,
    80965,
    65455,
    68999,
    94531,
    25077,
    25055,
    65455,
    16017,
    65455,
    47868,
    18696,
    70965,
    97960,
    38086,
    21953,
    92562,
    27547,
    45593,
    10136,
    32890,
    27547,
    28452,
    12353,
    77196,
    27547,
    53427,
    32195,
    82202,
    45593,
    96715,
    88975,
    32060,
    77044,
    49627,
    45593,
    87312,
    89620,
    18696,
    76316,
    17127,
    49688,
    99080,
    21092,
    89620,
    27547,
    45593,
    54914,
    56972,
    45593,
    56032,
    16358,
    12353,
    66328,
    38915,
    45971,
    62229,
    73083,
    49688,
    12657,
    82877,
    12353,
    46480,
    91051,
    18696,
    12657,
    81859,
    34656,
    18696,
    27547,
    99250,
    89620,
    50852,
    40621,
    34336,
    49627,
    18350,
    97019,
    70754,
    16614,
    21092,
    44363,
    59612,
    43149,
    92643,
    18696,
    47988,
    12811,
    91257,
    25800,
    16886,
    56032,
    52921,
    92562,
    34245,
    13668,
    59590,
    20381,
    21373,
    17121,
    13737,
    97505,
    12560,
    13560,
    46045,
    12578,
    89846,
    89620,
    46940,
    30362,
    44987,
    56972,
    81859,
    41628,
    47868,
    65455,
    49627,
    81859,
    16886,
    61232,
    12657,
    53427,
    97285,
    49688,
    65455,
    99080,
    18306,
    45956,
    12935,
    35901,
    93929,
    81859,
    49627,
    21746,
    49627,
    82877,
    59612,
    85476,
    96912,
    37966,
    51315,
    70379,
    66328,
    81859,
    27197,
    33001,
    83017,
    99080,
    42385,
    93192,
    81859,
    51863,
    65566,
    49688,
    16886,
    94999,
    84555,
    47868,
    25800,
    89560,
    66913,
    32060,
    59039,
    56498,
    23626,
    72999,
    48753,
    33001,
    35814,
    59612,
    49749,
    27547,
    83974,
    38771,
    25606,
    97620,
    83974,
    49627,
    14185,
    82877,
    46741,
    18696,
    89208,
    51926,
    91090,
    26114,
    65566,
    17667,
    81596,
    98911,
    81141,
    32060,
    81859,
    97990,
    12353,
    32060,
    16886,
    79445,
    83974,
    47018,
    53073,
    82286,
    92110,
    17868,
    42706,
    12353,
    89458,
    77228,
    97413,
    27547,
    12657,
    89620,
    71041,
    83974,
    18696,
    49627,
    81859,
    83974,
    45593,
    56032,
    41567,
    70856,
    18696,
    45593,
    12657,
    24253,
    49627,
    88622,
    16886,
    89965,
    89810,
    83614,
    82877,
    96422,
    81859,
    35777,
    56988,
    21092,
    90453,
    78410,
    81859,
    22918,
    65566,
    27547,
    56972,
    13416,
    53035,
    52940,
    16886,
    68386,
    63909,
    70233,
    70763,
    89620,
    29799,
    88192,
    81859,
    16886,
    65455,
    28188,
    55257,
    89620,
    76062,
    27547,
    44580,
    49407,
    34513,
    29546,
    23929,
    98484,
    31195,
    82759,
    83614,
    47203,
    64125,
    63802,
    18696,
    32505,
    23426,
    32060,
    83964,
    47868,
    76179,
    99080,
    71317,
    53368,
    48586,
    46831,
    53147,
    83641,
    21015,
    18696,
    29411,
    88500,
    26798,
    92681,
    99080,
    42448,
    12353,
    92061,
    89965,
    12996,
    36736,
    92372,
    91013,
    99080,
    57447,
    75845,
    48242,
    18696,
    34443,
    27308,
    52098,
    66336,
    35403,
    12353,
    37576,
    16060,
    98743,
    17417,
    66300,
    12353,
    56032,
    88500,
    79432,
    99080,
    56972,
    56972,
    98899,
    33001,
    27547,
    83513,
    36718,
    99921,
    90701,
    27193,
    19172
]

l1.sort()
l2.sort()
total = 0
for n1, n2 in zip(l1, l2):
    d = n1 - n2 if n1 >= n2 else n2 - n1
    total += d
print(total)

i = 0
j = 0
total = 0
while i < len(l1) and j < len(l2):
    num_l = l1[i]
    num_r = l2[j]

    if num_l == num_r:
        total += num_l
        j += 1
    elif num_l > num_r:
        j += 1
    else:
        i += 1
print(total)




