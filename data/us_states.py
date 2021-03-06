# -*- coding: utf-8 -*-

# See http://en.wikipedia.org/wiki/List_of_U.S._state_abbreviations
# WARNING: The name of each state should be in French
# (e.g. "Floride", not "Florida")
US_STATES = {'AK': 'Alaska',
             'AL': 'Alabama',
             'AR': 'Arkansas',
             'AZ': 'Arizona',
             'Ala.': 'Alabama',
             'Alas.': 'Alaska',
             'Alaska': 'Alaska',
             'Ariz.': 'Arizona',
             'Ark.': 'Arkansas',
             'Az.': 'Arizona',
             'CA': 'Californie',
             'CF': 'Californie',
             'CL': 'Colorado',
             'CO': 'Colorado',
             'CT': 'Connecticut',
             'Ca.': 'Californie',
             'Cal.': 'Californie',
             'Cali.': 'Californie',
             'Calif.': 'Californie',
             'Col.': 'Colorado',
             'Colo.': 'Colorado',
             'Conn.': 'Connecticut',
             'Ct.': 'Connecticut',
             'D.C.': 'District of ColuFederal district',
             'DC': 'District of ColuFederal district',
             'DE': 'Delaware',
             'DL': 'Delaware',
             'De.': 'Delaware',
             'Del.': 'Delaware',
             'FL': 'Floride',
             'Fl.': 'Floride',
             'Fla.': 'Floride',
             'Flor.': 'Floride',
             'GA': u'Géorgie',
             'Ga.': u'Géorgie',
             'H.I.': 'Hawaii',
             'HA': 'Hawaii',
             'HI': 'Hawaii',
             'Hawaii': 'Hawaii',
             'IA': 'Iowa',
             'ID': 'Idaho',
             'IL': 'Illinois',
             'IN': 'Indiana',
             'Ia.': 'Iowa',
             'Id.': 'Idaho',
             'Ida.': 'Idaho',
             'Idaho': 'Idaho',
             'Il.': 'Illinois',
             "Ill's": 'Illinois',
             'Ill.': 'Illinois',
             'Ills.': 'Illinois',
             'In.': 'Indiana',
             'Ind.': 'Indiana',
             'Ioa.': 'Iowa',
             'Iowa': 'Iowa',
             'KA': 'Kansas',
             'KS': 'Kansas',
             'KY': 'Kentucky',
             'Ka.': 'Kansas',
             'Kan.': 'Kansas',
             'Kans.': 'Kansas',
             'Ks.': 'Kansas',
             'Ky.': 'Kentucky',
             'LA': 'Louisiane',
             'La.': 'Louisiane',
             'MA': 'Massachusetts',
             'MC': 'Michigan',
             'MD': 'Maryland',
             'ME': 'Maine',
             'MI': 'Mississippi',
             'MN': 'Minnesota',
             'MO': 'Missouri',
             'MS': 'Mississippi',
             'MT': 'Montana',
             'Maine': 'Maine',
             'Mass.': 'Massachusetts',
             'Md.': 'Maryland',
             'Me.': 'Maine',
             'Mich.': 'Michigan',
             'Minn.': 'Minnesota',
             'Miss.': 'Mississippi',
             'Mn.': 'Minnesota',
             'Mo.': 'Missouri',
             'Mont.': 'Montana',
             'N. Car.': 'Caroline du Nord',
             'N. Dak.': 'Dakota du Nord',
             'N. Mex.': 'Nouveau-Mexique',
             'N. York': 'New York',
             'N.C.': 'Caroline du Nord',
             'N.D.': 'Dakota du Nord',
             'N.H.': 'New Hampshire',
             'N.J.': 'New Jersey',
             'N.M.': 'Nouveau-Mexique',
             'N.Y.': 'New York',
             'NB': 'Nebraska',
             'NC': 'Caroline du Nord',
             'ND': 'Dakota du Nord',
             'NE': 'Nebraska',
             'NH': 'New Hampshire',
             'NJ': 'New Jersey',
             'NM': 'Nouveau-Mexique',
             'NV': 'Nevada',
             'NY': 'New York',
             'Neb.': 'Nebraska',
             'Nebr.': 'Nebraska',
             'Nev.': 'Nevada',
             'New M.': 'Nouveau-Mexique',
             'NoDak': 'Dakota du Nord',
             'Nv.': 'Nevada',
             'O.': 'Ohio',
             'OH': 'Ohio',
             'OK': 'Oklahoma',
             'OR': 'Oregon',
             'Oh.': 'Ohio',
             'Ohio': 'Ohio',
             'Ok.': 'Oklahoma',
             'Okla.': 'Oklahoma',
             'Or.': 'Oregon',
             'Ore.': 'Oregon',
             'Oreg.': 'Oregon',
             'PA': 'Pennsylvanie',
             'Pa.': 'Pennsylvanie',
             'R.I.': 'Rhode Island',
             'R.I. & P.P.': 'Rhode Island',
             'RI': 'Rhode Island',
             'S. Car.': 'Caroline du Sud',
             'S. Dak.': 'Dakota du Sud',
             'S.C.': 'Caroline du Sud',
             'S.D.': 'Dakota du Sud',
             'SC': 'Caroline du Sud',
             'SD': 'Dakota du Sud',
             'SoDak': 'Dakota du Sud',
             'State': 'Utah',
             'TN': 'Tennessee',
             'TX': 'Texas',
             'Tenn.': 'Tennessee',
             'Tex.': 'Texas',
             'Texas': 'Texas',
             'Tn.': 'Tennessee',
             'Tx.': 'Texas',
             'US-AL': 'Alabama',
             'US-AR': 'Arkansas',
             'US-AZ': 'Arizona',
             'US-CA': 'Californie',
             'US-CO': 'Colorado',
             'US-CT': 'Connecticut',
             'US-DC': 'District of ColuFederal district',
             'US-DE': 'Delaware',
             'US-FL': 'Floride',
             'US-GA': u'Géorgie',
             'US-IL': 'Illinois',
             'US-IN': 'Indiana',
             'US-KY': 'Kentucky',
             'US-LA': 'Louisiane',
             'US-MA': 'Massachusetts',
             'US-MD': 'Maryland',
             'US-MI': 'Michigan',
             'US-MN': 'Minnesota',
             'US-MO': 'Missouri',
             'US-MS': 'Mississippi',
             'US-MT': 'Montana',
             'US-NC': 'Caroline du Nord',
             'US-ND': 'Dakota du Nord',
             'US-NE': 'Nebraska',
             'US-NH': 'New Hampshire',
             'US-NJ': 'New Jersey',
             'US-NM': 'Nouveau-Mexique',
             'US-NY': 'New York',
             'US-OK': 'Oklahoma',
             'US-PA': 'Pennsylvanie',
             'US-RI': 'Rhode Island',
             'US-SC': 'Caroline du Sud',
             'US-SD': 'Dakota du Sud',
             'US-TN': 'Tennessee',
             'US-VA': 'Virginia',
             'US-VT': 'Vermont',
             'US-WA': 'Washington',
             'US-WI': 'Wisconsin',
             'US-WV': 'Virginie occidentale',
             'US-WY': 'Wyoming',
             'UT': 'Utah',
             'Ut.': 'Utah',
             'Utah': 'Utah',
             'VA': 'Virginia',
             'VT': 'Vermont',
             'Va.': 'Virginia',
             'Vt.': 'Vermont',
             'W. Va.': 'Virginie occidentale',
             'W. Virg.': 'Virginie occidentale',
             'W.V.': 'Virginie occidentale',
             'W.Va.': 'Virginie occidentale',
             'WA': 'Washington',
             'WI': 'Wisconsin',
             'WN': 'Washington',
             'WS': 'Wisconsin',
             'WV': 'Virginie occidentale',
             'WY': 'Wyoming',
             'Wa.': 'Washington',
             'Wash.': 'Washington',
             'Wash. D.C.': 'District of ColuFederal district',
             'Wi.': 'Wisconsin',
             'Wis.': 'Wisconsin',
             'Wisc.': 'Wisconsin',
             'Wn.': 'Washington',
             'Wy.': 'Wyoming',
             'Wyo.': 'Wyoming'}
