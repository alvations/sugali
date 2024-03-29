# -*- coding: utf-8 -*-

from collections import defaultdict

headerline = "wals code  glottocode  name  latitude  longitude  macroarea  genus  family  sample 100  sample 200"
wals_tsv = """bnn  bann1247  Banoni  -6.41666666667  155.25  Papunesia  Oceanic  Austronesian  False  False
ard  aran1237  Arandai  -2.08333333333  133.0  Papunesia  South Bird's Head  Marind  False  False
klw  kili1268  Kiliwa  31.3333333333  -115.666666667  North America  Yuman  Hokan  False  False
mnm  mana1295  Manam  -4.0  145.0  Papunesia  Oceanic  Austronesian  False  False
pil  pile1238  Pileni  -10.2166666667  166.216666667  Papunesia  Oceanic  Austronesian  False  False
koa  koas1236  Koasati  34.8333333333  -85.1666666667  North America  Muskogean  Muskogean  True  True
tpr  tupu1244  Tupuri  10.1666666667  14.75  Africa  Adamawa  Niger-Congo  False  False
hix  hixk1239  Hixkaryana  -1.0  -59.0  South America  Cariban  Cariban  True  True
lbu  lund1266  Lunda  -10.6666666667  24.0  Africa  Bantoid  Niger-Congo  False  False
tkl  take1257  Takelma  42.5  -123.0  North America  Takelma  Takelma  False  False
knp  ngka1235  Kanum (Ngkâlmpw)  -8.66666666667  140.916666667  Papunesia  Morehead and Upper Maro Rivers  Morehead and Upper Maro Rivers  False  False
knb  badi1247  Kanum (Bädi)  -8.83333333333  140.75  Papunesia  Morehead and Upper Maro Rivers  Morehead and Upper Maro Rivers  False  False
mor  morm1235  Mor  -2.95  135.75  Papunesia  South Halmahera - West New Guinea  Austronesian  False  False
rag  hano1246  Raga  -15.5  168.166666667  Papunesia  Oceanic  Austronesian  False  False
pmn  nort2966  Pomo (Northern)  39.3333333333  -123.5  North America  Pomoan  Hokan  False  False
far  faro1244  Faroese  62.0  -7.0  Eurasia  Germanic  Indo-European  False  False
ang  ango1254  Anggor  -3.75  141.166666667  Papunesia  Senagi  Senagi  False  False
atk  atak1252  Atakapa  30.0  -93.5  North America  Atakapa  Atakapa  False  False
kla  klao1243  Klao  4.75  -8.75  Africa  Kru  Niger-Congo  False  False
idu  idum1241  Idu  29.3333333333  95.8333333333  Eurasia  Digaroan  Sino-Tibetan  False  False
mis  misk1235  Miskito  14.0  -83.6666666667  North America  Misumalpan  Misumalpan  False  False
cde  maqu1238  Carib (De'kwana)  5.5  -65.0  South America  Cariban  Cariban  False  False
kui  kuii1252  Kui (in India)  20.0  83.5  Eurasia  South-Central Dravidian  Dravidian  False  False
kiu  kuii1253  Kui (in Indonesia)  -8.43333333333  124.55  Papunesia  Greater Alor  Timor-Alor-Pantar  False  False
grn  fare1241  Gurenne  10.8333333333  -0.916666666667  Africa  Gur  Niger-Congo  False  False
ngg  nang1259  Ngan'gityemerri  -14.25  130.416666667  Australia  Southern Daly  Australian  False  False
ngk  nang1259  Ngankikurungkurr  -14.0  130.5  Australia  Southern Daly  Australian  False  False
rgn  nort2994  Roglai (Northern)  12.1666666667  108.833333333  Eurasia  Malayo-Sumbawan  Austronesian  False  False
ngt  tang1336  Naga (Tangkhul)  25.0  94.5  Eurasia  Kuki-Chin  Sino-Tibetan  False  False
tza  tzel1254  Tzeltal (Aguacatenango)  16.4166666667  -92.5  North America  Mayan  Mayan  False  False
tzb  tzel1255  Tzeltal (Bachajón)  16.9166666667  -92.0  North America  Mayan  Mayan  False  False
tzt  tzel1254  Tzeltal (Tenejapa)  16.6666666667  -92.3333333333  North America  Mayan  Mayan  False  False
tze  tzel1253  Tzeltal  16.8333333333  -92.25  North America  Mayan  Mayan  False  False
saa  saaa1240  Sa'a  -9.61666666667  161.45  Papunesia  Oceanic  Austronesian  False  False
ctm  chit1248  Chitimacha  29.6666666667  -91.0  North America  Chitimacha  Chitimacha  False  False
ilo  ilok1237  Ilocano  16.0  121.0  Papunesia  Northern Luzon  Austronesian  False  False
bbu  bara1361  Barambu  3.5  27.0  Africa  Ubangi  Niger-Congo  False  False
wan  ngur1261  Wangkumara  -27.3333333333  143.0  Australia  Pama-Nyungan  Australian  False  False
prh  pira1253  Pirahã  -7.0  -62.0  South America  Mura  Mura  True  True
kmp  kuni1267  Kunimaipa  -8.0  146.833333333  Papunesia  Goilalan  Trans-New Guinea  False  False
lla  lamu1254  Lamu-Lamu  -14.8333333333  144.5  Australia  Pama-Nyungan  Australian  False  False
paa  paaa1242  Pa'a  11.0  9.25  Africa  West Chadic  Afro-Asiatic  False  False
amk  amar1274  Amarakaeri  -12.5  -70.5  South America  Harakmbet  Harakmbet  False  False
lov  lave1248  Loven  15.0  106.333333333  Eurasia  Bahnaric  Austro-Asiatic  False  False
yrm  yuru1243  Yurimangí  3.83333333333  -77.0  South America  Yurimangí  Yurimangí  False  False
yuc  yuch1247  Yuchi  35.75  -86.75  North America  Yuchi  Yuchi  False  True
mwo  motl1237  Mwotlap  -13.5833333333  167.583333333  Papunesia  Oceanic  Austronesian  False  False
dsh  dani1285  Danish  56.0  10.0  Eurasia  Germanic  Indo-European  False  False
dab  maza1304  Daba  10.1666666667  13.75  Africa  Biu-Mandara  Afro-Asiatic  False  False
otm  mezq1235  Otomí (Mezquital)  20.1666666667  -99.1666666667  North America  Otomian  Oto-Manguean  True  True
osm  quer1236  Otomí (Santiago Mexquititlan)  20.0833333333  -100.083333333  North America  Otomian  Oto-Manguean  False  False
oix  ixte1237  Otomí (Ixtenco)  19.0833333333  -97.9166666667  North America  Otomian  Oto-Manguean  False  False
ben  beng1280  Bengali  24.0  90.0  Eurasia  Indic  Indo-European  False  False
bec  chit1275  Bengali (Chittagong)  22.3333333333  91.8333333333  Eurasia  Indic  Indo-European  False  False
shp  nort1527  Sahaptin (Northern)  46.5  -120.0  North America  Sahaptian  Penutian  False  False
smt  umat1237  Sahaptin (Umatilla)  45.6666666667  -118.5  North America  Sahaptian  Penutian  False  False
chy  chay1248  Chayahuita  -5.5  -77.0  South America  Cahuapanan  Cahuapanan  False  False
kku  kork1243  Korku  22.5  78.5  Eurasia  Munda  Austro-Asiatic  False  False
hyo  asho1236  Hyow  22.0833333333  92.4166666667  Eurasia  Kuki-Chin  Sino-Tibetan  False  False
ho  hooo1248  Ho  22.0  86.0  Eurasia  Munda  Austro-Asiatic  False  False
tbs  taba1259  Tabassaran  41.8333333333  47.9166666667  Eurasia  Lezgic  Nakh-Daghestanian  False  False
arw  nucl1235  Armenian (Western)  38.5  43.5  Eurasia  Armenian  Indo-European  False  False
arm  nucl1235  Armenian (Eastern)  40.0  45.0  Eurasia  Armenian  Indo-European  False  True
arz  nucl1235  Armenian (Iranian)  32.6666666667  51.6666666667  Eurasia  Armenian  Indo-European  False  False
agc  cent2084  Agta (Central)  17.9666666667  121.833333333  Papunesia  Greater Central Philippine  Austronesian  False  False
mig  miga1249  Migama  12.1666666667  19.8333333333  Africa  East Chadic  Afro-Asiatic  False  False
ggu  gure1255  Gureng Gureng  -25.25  151.0  Australia  Pama-Nyungan  Australian  False  False
mlu  male1289  Maleu  -5.71666666667  148.416666667  Papunesia  Oceanic  Austronesian  False  False
gay  gayo1244  Gayo  4.5  97.5  Papunesia  Northwest Sumatra-Barrier Islands  Austronesian  False  False
ctc  cuic1234  Cuicatec  17.8333333333  -96.8333333333  North America  Mixtecan  Oto-Manguean  False  False
nab  naba1256  Nabak  -6.41666666667  147.0  Papunesia  Finisterre-Huon  Trans-New Guinea  False  False
hia  cari1279  Hianacoto  0.833333333333  -71.0  South America  Cariban  Cariban  False  False
skm  suku1261  Sukuma  -2.83333333333  32.0  Africa  Bantoid  Niger-Congo  False  False
fin  finn1318  Finnish  62.0  25.0  Eurasia  Finnic  Uralic  True  True
ung  ngar1284  Ungarinjin  -16.3333333333  126.0  Australia  Wororan  Australian  False  True
sup  supy1237  Supyire  11.5  -5.58333333333  Africa  Gur  Niger-Congo  True  True
nau  naur1243  Nauruan  -0.5  166.916666667  Papunesia  Oceanic  Austronesian  False  False
ykt  yaku1245  Yakut  62.0  130.0  Eurasia  Turkic  Altaic  False  False
lnd  band1344  Linda  6.5  20.75  Africa  Ubangi  Niger-Congo  False  False
sao  saho1246  Saho  14.75  39.75  Africa  Eastern Cushitic  Afro-Asiatic  False  False
mmb  mbul1263  Mangap-Mbula  -5.66666666667  148.083333333  Papunesia  Oceanic  Austronesian  False  False
nup  nupe1254  Nupe  9.16666666667  5.41666666667  Africa  Nupoid  Niger-Congo  False  False
klh  kala1372  Kalasha  35.0  72.0  Eurasia  Indic  Indo-European  False  False
skn  guah1255  Sikuani  6.25  -71.5  South America  Guahiban  Guahiban  False  False
ghb  guah1255  Guahibo  5.0  -69.0  South America  Guahiban  Guahiban  False  False
woi  kama1365  Woisika  -8.25  124.833333333  Papunesia  Greater Alor  Timor-Alor-Pantar  False  False
lat  latv1249  Latvian  57.0  24.0  Eurasia  Baltic  Indo-European  False  True
dok  ngom1268  Doko  3.0  23.0833333333  Africa  Bantoid  Niger-Congo  False  False
nbe  ngom1268  Ngombe  3.0  23.0  Africa  Bantoid  Niger-Congo  False  False
mbe  mber1257  Mbere  -0.5  14.0  Africa  Bantoid  Niger-Congo  False  False
cyv  cayu1262  Cayuvava  -13.5  -65.5  South America  Cayuvava  Cayuvava  False  True
nsy  assy1241  Neo-Aramaic (Assyrian)  36.0  41.0  Eurasia  Semitic  Afro-Asiatic  False  False
der  dera1245  Dla (Proper)  -3.58333333333  141.0  Papunesia  Senagi  Senagi  False  False
pnn  pang1290  Pangasinan  15.9166666667  120.333333333  Papunesia  Northern Luzon  Austronesian  False  False
bbw  gunw1252  Bininj Gun-Wok  -12.5  133.75  Australia  Gunwinygic  Australian  False  False
zso  zulu1248  Zulu (Southern)  -31.0  30.0  Africa  Bantoid  Niger-Congo  False  False
zno  zulu1248  Zulu (Northern)  -28.0  31.0  Africa  Bantoid  Niger-Congo  False  False
zul  zulu1248  Zulu  -30.0  30.0  Africa  Bantoid  Niger-Congo  True  True
sio  sioo1240  Sio  -5.95  147.333333333  Papunesia  Oceanic  Austronesian  False  False
mou  moru1253  Moru  4.75  29.75  Africa  Moru-Ma'di  Nilo-Saharan  False  False
myr  mats1244  Matsés  -5.41666666667  -73.25  South America  Panoan  Panoan  False  False
msn  mais1250  Maisin  -9.5  149.166666667  Papunesia  Oceanic  Austronesian  False  False
cve  chua1250  Chuave  -6.11666666667  145.116666667  Papunesia  Chimbu  Trans-New Guinea  False  False
dob  dobe1238  Dobel  -6.25  134.666666667  Papunesia  Central Malayo-Polynesian  Austronesian  False  False
zen  zena1248  Zenaga  17.3333333333  -16.0  Africa  Berber  Afro-Asiatic  False  False
bti  beto1236  Betoi  7.16666666667  -71.25  South America  Betoi  Betoi  False  False
kgr  kagu1239  Kagulu  -6.33333333333  37.0  Africa  Bantoid  Niger-Congo  False  False
kya  kuku1273  Kuku-Yalanji  -16.0  145.0  Australia  Pama-Nyungan  Australian  False  False
bhn  bahi1254  Bahinemo  -4.58333333333  142.833333333  Papunesia  Sepik Hill  Sepik  False  False
cog  cogu1240  Cogui  11.0  -73.8333333333  South America  Aruak  Chibchan  False  False
mpu  mpur1239  Mpur  -0.75  133.25  Papunesia  Kebar  West Papuan  False  False
hmb  huam1247  Huambisa  -4.0  -78.0  South America  Jivaroan  Jivaroan  False  False
qch  kich1262  Quiché  15.0  -91.4166666667  North America  Mayan  Mayan  False  False
dou  dout1240  Doutai  -3.33333333333  138.166666667  Papunesia  Lakes Plain  Lakes Plain  False  False
cem  cemu1238  Cèmuhî  -20.8333333333  165.166666667  Papunesia  Oceanic  Austronesian  False  False
tld  tala1285  Talaud  4.25  126.75  Papunesia  Sangiric  Austronesian  False  False
hlp  hava1248  Hualapai  35.5  -113.75  North America  Yuman  Hokan  False  False
dms  dima1251  Dimasa  25.5  93.0  Eurasia  Bodo-Garo  Sino-Tibetan  False  False
yah  yama1264  Yahgan  -55.0  -68.0  South America  Yámana  Yámana  False  False
aly  alya1239  Alyawarra  -22.5  135.0  Australia  Pama-Nyungan  Australian  False  False
mny  marg1253  Margany  -27.0  144.5  Australia  Pama-Nyungan  Australian  False  False
awn  awng1244  Awngi  10.8333333333  36.6666666667  Africa  Central Cushitic  Afro-Asiatic  False  False
jeb  jebe1250  Jebero  -5.41666666667  -76.5  South America  Cahuapanan  Cahuapanan  False  False
neh  neha1247  Nehan  -4.5  154.2  Papunesia  Oceanic  Austronesian  False  False
ntu  nene1249  Nenets (Tundra)  70.0  76.0  Eurasia  Samoyedic  Uralic  False  False
nen  nene1249  Nenets  69.0  72.0  Eurasia  Samoyedic  Uralic  False  True
crg  east2555  Chiriguano  -23.6666666667  -64.3333333333  South America  Tupi-Guaraní  Tupian  False  False
gua  para1311  Guaraní  -26.0  -56.0  South America  Tupi-Guaraní  Tupian  True  True
bna  jama1261  Banawá  -7.0  -65.0  South America  Arauan  Arauan  False  False
amx  anam1248  Anamuxra  -4.66666666667  145.0  Papunesia  Madang  Trans-New Guinea  False  False
hil  hili1240  Hiligaynon  10.25  123.0  Papunesia  Greater Central Philippine  Austronesian  False  False
ass  assa1263  Assamese  26.0  93.0  Eurasia  Indic  Indo-European  False  False
tbl  tabl1243  Tabla  -2.45  140.416666667  Papunesia  Sentani  Sentani  False  False
mba  mbaa1245  Mba  1.0  25.0  Africa  Ubangi  Niger-Congo  False  False
ogb  ogbi1239  Ogbia  4.66666666667  6.25  Africa  Cross River  Niger-Congo  False  False
alw  alaw1244  Alawa  -15.1666666667  134.25  Australia  Maran  Australian  False  False
nif  niua1240  Niuafo'ou  -15.5666666667  -175.616666667  Papunesia  Oceanic  Austronesian  False  False
ura  urav1235  Ura  -18.6666666667  169.083333333  Papunesia  Oceanic  Austronesian  False  False
mss  sout2985  Miwok (Southern Sierra)  37.5  -120.0  North America  Miwok  Penutian  False  True
tbu  tebu1238  Tubu  16.0  15.0  Africa  Western Saharan  Nilo-Saharan  False  False
tgl  tsha1245  Tshangla  27.8333333333  92.1666666667  Eurasia  Bodic  Sino-Tibetan  False  False
efi  efik1245  Efik  4.91666666667  8.5  Africa  Cross River  Niger-Congo  False  False
sba  sali1298  Sáliba (in Colombia)  6.0  -70.0  South America  Sáliba  Sáliban  False  False
luo  luok1236  Luo  -0.5  34.75  Africa  Nilotic  Nilo-Saharan  False  False
awp  awac1239  Awa Pit  1.5  -78.25  South America  Barbacoan  Barbacoan  False  True
pec  pech1241  Pech  15.0  -85.5  North America  Paya  Chibchan  False  False
nyr  nyan1301  Nyangumarda  -20.0  121.0  Australia  Pama-Nyungan  Australian  False  False
dig  diga1241  Digaro  28.4166666667  96.0  Eurasia  Digaroan  Sino-Tibetan  False  False
bni  bini1246  Bini  6.41666666667  5.83333333333  Africa  Edoid  Niger-Congo  False  False
jeh  jehh1245  Jeh  15.1666666667  107.833333333  Eurasia  Bahnaric  Austro-Asiatic  False  False
bhi  bhil1251  Bhili  22.0  73.0  Eurasia  Indic  Indo-European  False  False
cmy  taba1266  Chontal Maya  18.1666666667  -92.5833333333  North America  Mayan  Mayan  False  False
chx  lowl1260  Chontal (Huamelultec Oaxaca)  16.0  -95.75  North America  Tequistlatecan  Tequistlatecan  False  False
cho  high1242  Chontal (Highland)  16.25  -95.75  North America  Tequistlatecan  Tequistlatecan  False  False
ewo  ewon1239  Ewondo  4.0  12.0  Africa  Bantoid  Niger-Congo  False  False
khl  turk1303  Khalaj  35.0  50.0  Eurasia  Turkic  Altaic  False  False
mbl  mbol1247  Mbole  -0.666666666667  24.6666666667  Africa  Bantoid  Niger-Congo  False  False
kij  kitj1240  Kitja  -17.5  127.75  Australia  Djeragan  Australian  False  False
mya  maya1282  Ma'ya  -1.25  130.916666667  Papunesia  South Halmahera - West New Guinea  Austronesian  False  False
bao  bona1250  Bao'an  35.75  102.833333333  Eurasia  Mongolic  Altaic  False  False
guu  gugu1255  Guugu Yimidhirr  -15.0  144.833333333  Australia  Pama-Nyungan  Australian  False  False
cua  cuaa1241  Cua  15.25  108.5  Eurasia  Bahnaric  Austro-Asiatic  False  False
gah  alek1238  Gahuku  -6.0  145.416666667  Papunesia  Eastern Highlands  Trans-New Guinea  False  False
wry  wara1290  Waray (in Australia)  -13.1666666667  131.25  Australia  Waray  Australian  False  False
mzn  maza1291  Mazanderani  36.5  52.0  Eurasia  Iranian  Indo-European  False  False
cmx  como1259  Comox  50.1666666667  -125.0  North America  Central Salish  Salishan  False  False
mpo  myen1241  Mpongwe  -1.25  9.5  Africa  Bantoid  Niger-Congo  False  False
hpd  hupd1244  Hup  0.166666666667  -69.25  South America  Nadahup  Nadahup  False  False
ysi  sire1246  Yupik (Sirenik)  64.5  -174.0  Eurasia  Eskimo  Eskimo-Aleut  False  False
goe  goem1240  Goemai  8.66666666667  9.75  Africa  West Chadic  Afro-Asiatic  False  False
sry  sira1267  Siraiya  23.0  120.25  Papunesia  Paiwanic  Austronesian  False  False
tat  tata1257  Tatana'  5.5  115.5  Papunesia  North Borneo  Austronesian  False  False
pno  nort2954  Paiute (Northern)  42.0  -118.0  North America  Numic  Uto-Aztecan  False  False
bre  bret1244  Breton  48.0  -3.0  Eurasia  Celtic  Indo-European  False  False
mbz  mbee1250  Mbe'  6.28333333333  11.0833333333  Africa  Bantoid  Niger-Congo  False  False
amu  yane1238  Amuesha  -10.5  -75.4166666667  South America  Western Arawakan  Arawakan  False  False
fua  adam1253  Fula (Cameroonian)  9.16666666667  13.5  Africa  Northern Atlantic  Niger-Congo  False  False
fma  pula1263  Fula (Mauritanian)  16.5  -13.75  Africa  Northern Atlantic  Niger-Congo  False  False
fbf  west2454  Fula (Burkina Faso)  14.0  0.0  Africa  Northern Atlantic  Niger-Congo  False  False
fgo  adam1253  Fulani (Gombe)  10.25  11.25  Africa  Northern Atlantic  Niger-Congo  False  False
fgu  pula1262  Fula (Guinean)  11.5  -12.5  Africa  Northern Atlantic  Niger-Congo  False  False
fum  maas1239  Fulfulde (Maasina)  15.0  -5.0  Africa  Northern Atlantic  Niger-Congo  False  False
fus  pula1263  Fula (Senegal)  15.0  -14.0  Africa  Northern Atlantic  Niger-Congo  False  False
fni  nige1253  Fula (Nigerian)  8.16666666667  10.5  Africa  Northern Atlantic  Niger-Congo  False  False
nnm  tuva1244  Nanumea  -5.66666666667  176.116666667  Papunesia  Oceanic  Austronesian  False  False
tvl  tuva1244  Tuvaluan  -8.5  179.166666667  Papunesia  Oceanic  Austronesian  False  False
wsk  wask1241  Waskia  -4.5  146.0  Papunesia  Madang  Trans-New Guinea  False  False
mel  cent2101  Melanau  2.5  111.5  Papunesia  North Borneo  Austronesian  False  False
doy  doya1240  Doyayo  8.66666666667  13.0833333333  Africa  Adamawa  Niger-Congo  False  False
ayw  ayiw1239  Ayiwo  -10.3333333333  166.25  Papunesia  Oceanic  Austronesian  False  False
ga  gaaa1244  Gã  5.66666666667  -0.166666666667  Africa  Kwa  Niger-Congo  False  False
irm  iris1253  Irish (Munster)  52.5  -9.0  Eurasia  Celtic  Indo-European  False  False
ird  iris1253  Irish (Donegal)  55.0  -8.0  Eurasia  Celtic  Indo-European  False  False
iri  iris1253  Irish  53.0  -8.0  Eurasia  Celtic  Indo-European  False  True
had  hadz1240  Hadza  -3.75  35.1666666667  Africa  Hadza  Hadza  False  False
jam  djam1255  Jaminjung  -15.0833333333  130.5  Australia  Jaminjungan  Australian  False  False
kod  koda1255  Kodava  12.1666666667  76.8333333333  Eurasia  Southern Dravidian  Dravidian  False  False
arr  east2379  Arrernte  -24.0  134.0  Australia  Pama-Nyungan  Australian  False  False
awe  west2441  Arrernte (Western)  -24.0  132.5  Australia  Pama-Nyungan  Australian  False  False
amp  east2379  Arrernte (Mparntwe)  -24.0  136.0  Australia  Pama-Nyungan  Australian  False  False
gwa  gbag1258  Gwari  9.5  7.0  Africa  Nupoid  Niger-Congo  False  False
tan  nucl1696  Tangale  9.75  11.3333333333  Africa  West Chadic  Afro-Asiatic  False  False
tur  nucl1301  Turkish  39.0  35.0  Eurasia  Turkic  Altaic  True  True
mrn  mara1404  Maranao  7.83333333333  124.25  Papunesia  Greater Central Philippine  Austronesian  False  False
goa  wayu1243  Goajiro  12.0  -72.0  South America  Northern Arawakan  Arawakan  False  False
mcd  mace1250  Macedonian  41.6666666667  21.75  Eurasia  Slavic  Indo-European  False  False
chr  chra1242  Chrau  10.75  107.5  Eurasia  Bahnaric  Austro-Asiatic  False  False
yur  yuro1248  Yurok  41.3333333333  -124.0  North America  Yurok  Algic  False  True
bya  byan1241  Byansi  30.1666666667  80.5  Eurasia  Bodic  Sino-Tibetan  False  False
ma  made1252  Ma  3.5  28.0  Africa  Ubangi  Niger-Congo  False  False
lrd  lard1243  Lardil  -16.5  139.333333333  Australia  Pama-Nyungan  Australian  False  False
kab  kaba1278  Kabardian  43.5  43.5  Eurasia  Northwest Caucasian  Northwest Caucasian  False  False
tak  taki1248  Takia  -4.66666666667  146.0  Papunesia  Oceanic  Austronesian  False  False
kad  katc1249  Kadugli  11.0  29.6666666667  Africa  Kadugli  Kadugli  False  False
cld  chal1275  Chaldean (Modern)  36.0  43.0  Eurasia  Semitic  Afro-Asiatic  False  False
chm  cham1309  Chamalal  42.55  46.05  Eurasia  Avar-Andic-Tsezic  Nakh-Daghestanian  False  False
uru  uruu1244  Uru  -16.75  -69.0  South America  Uru-Chipaya  Uru-Chipaya  False  False
msh  mars1254  Marshallese  7.11666666667  171.05  Papunesia  Oceanic  Austronesian  False  False
lag  lagw1237  Lagwan  11.5  14.8333333333  Africa  Biu-Mandara  Afro-Asiatic  False  False
bnj  band1339  Bandjalang  -28.75  153.0  Australia  Pama-Nyungan  Australian  False  False
gid  band1339  Gidabal  -28.4166666667  152.416666667  Australia  Pama-Nyungan  Australian  False  False
byu  band1339  Bandjalang (Yugumbir)  -27.9166666667  153.0  Australia  Pama-Nyungan  Australian  False  False
bca  band1339  Bandjalang (Casino)  -28.9166666667  153.0  Australia  Pama-Nyungan  Australian  False  False
bwa  band1339  Bandjalang (Waalubal)  -29.0833333333  152.583333333  Australia  Pama-Nyungan  Australian  False  False
nng  nyan1304  Nyanga  -1.25  28.1666666667  Africa  Bantoid  Niger-Congo  False  False
dhm  dhim1246  Dhimal  26.6666666667  87.75  Eurasia  Dhimalic  Sino-Tibetan  False  False
lha  laha1250  Laha  21.5833333333  103.916666667  Eurasia  Kadai  Tai-Kadai  False  False
ser  seri1257  Seri  29.0  -112.0  North America  Seri  Hokan  False  False
igb  nucl1417  Igbo  6.0  7.33333333333  Africa  Igboid  Niger-Congo  False  True
len  lena1238  Lenakel  -19.45  169.25  Papunesia  Oceanic  Austronesian  False  False
kmo  moun1252  Koiali (Mountain)  -9.0  147.5  Papunesia  Koiarian  Trans-New Guinea  False  False
boq  damu1236  Bokar  28.5  94.6666666667  Eurasia  Tani  Sino-Tibetan  False  False
boj  damu1236  Bori  28.3333333333  94.75  Eurasia  Tani  Sino-Tibetan  False  False
gal  damu1236  Galo  28.1666666667  94.6666666667  Eurasia  Tani  Sino-Tibetan  False  False
mil  damu1236  Milang  28.5  95.25  Eurasia  Tani  Sino-Tibetan  False  False
atc  urip1239  Atchin  -16.0  167.333333333  Papunesia  Oceanic  Austronesian  False  False
nit  noot1239  Nitinaht  48.6666666667  -124.75  North America  Southern Wakashan  Wakashan  False  False
kmr  kamo1255  Kamoro  -4.33333333333  136.0  Papunesia  Asmat-Kamoro  Trans-New Guinea  False  False
sug  assa1269  Sungor  13.75  21.5  Africa  Taman  Nilo-Saharan  False  False
mgo  mong1338  Mongo  0.0  21.0  Africa  Bantoid  Niger-Congo  False  False
lui  luis1253  Luiseño  33.3333333333  -117.166666667  North America  Takic  Uto-Aztecan  False  False
mgu  musg1254  Musgu  10.8333333333  14.9166666667  Africa  Biu-Mandara  Afro-Asiatic  False  False
mkl  makl1246  Maklew  -7.66666666667  139.416666667  Papunesia  Bulaka River  Bulaka River  False  False
tbe  tigr1270  Tigré (Beni Amer)  15.5  38.0  Africa  Semitic  Afro-Asiatic  False  False
tgr  tigr1270  Tigré  16.5  38.5  Africa  Semitic  Afro-Asiatic  False  False
err  siee1239  Erromangan  -18.8333333333  169.166666667  Papunesia  Oceanic  Austronesian  False  False
srr  serr1255  Serrano  34.5  -117.0  North America  Takic  Uto-Aztecan  False  False
kni  konn1242  Konni  10.25  -1.58333333333  Africa  Gur  Niger-Congo  False  False
chc  chec1245  Chechen  43.25  45.8333333333  Eurasia  Nakh  Nakh-Daghestanian  False  False
aze  sout2697  Azerbaijani  40.5  48.5  Eurasia  Turkic  Altaic  False  False
azi  sout2697  Azari (Iranian)  37.5  47.0  Eurasia  Turkic  Altaic  False  False
wat  waja1257  Watjarri  -26.0  117.5  Australia  Pama-Nyungan  Australian  False  False
grb  barc1235  Grebo  5.0  -8.0  Africa  Kru  Niger-Congo  True  True
eud  opat1246  Eudeve  29.1666666667  -109.666666667  North America  Cahita  Uto-Aztecan  False  False
kti  yong1280  Kati (in West Papua, Indonesia)  -5.75  140.916666667  Papunesia  Ok  Trans-New Guinea  False  False
pai  paiw1248  Paiwan  22.5  120.833333333  Papunesia  Paiwanic  Austronesian  True  True
mkr  arua1260  Mikarew  -4.41666666667  144.916666667  Papunesia  Mikarew  Lower Sepik-Ramu  False  False
brs  bara1380  Barasano  -0.166666666667  -70.6666666667  South America  Tucanoan  Tucanoan  True  True
bfd  biaf1240  Biafada  11.4166666667  -15.1666666667  Africa  Northern Atlantic  Niger-Congo  False  False
tst  tsat1238  Tsat  18.25  109.5  Eurasia  Malayo-Sumbawan  Austronesian  False  False
muu  mund1330  Mundurukú  -7.0  -58.0  South America  Munduruku  Tupian  False  False
ram  rama1270  Rama  11.75  -83.75  North America  Rama  Chibchan  True  True
wog  woga1249  Wogamusin  -4.25  142.333333333  Papunesia  Upper Sepik  Sepik  False  False
cwe  colu1241  Columbia-Wenatchi  47.5  -120.0  North America  Interior Salish  Salishan  False  False
nhh  huas1257  Nahuatl (Huasteca)  22.0  -99.0  North America  Aztecan  Uto-Aztecan  False  False
nhm  mich1245  Nahuatl (Michoacán)  18.5  -103.0  North America  Aztecan  Uto-Aztecan  False  False
nhn  nort2957  Nahuatl (North Puebla)  20.0  -98.25  North America  Aztecan  Uto-Aztecan  False  False
nht  tete1251  Nahuatl (Tetelcingo)  19.6666666667  -99.0  North America  Aztecan  Uto-Aztecan  False  True
nmp  None  Nahuatl (Milpa Alta)  19.25  -99.1666666667  None  Aztecan  Uto-Aztecan  False  False
nmi  isth1242  Nahuatl (Mecayapan Isthmus)  18.25  -94.8333333333  North America  Aztecan  Uto-Aztecan  False  False
nhu  None  Nahuatl (Huauchinango)  20.1666666667  -98.0833333333  None  Aztecan  Uto-Aztecan  False  False
npa  isth1241  Nahuatl (Pajapan)  18.25  -94.75  North America  Aztecan  Uto-Aztecan  False  False
nsz  high1278  Nahuatl (Sierra de Zacapoaxtla)  19.5833333333  -97.3333333333  North America  Aztecan  Uto-Aztecan  False  False
nhx  guer1241  Nahuatl (Xalitla)  18.0  -99.5  North America  Aztecan  Uto-Aztecan  False  False
nhp  poch1244  Nahuatl (Pochutla)  15.75  -96.5  North America  Aztecan  Uto-Aztecan  False  False
nhc  cent2132  Nahuatl (Central)  19.0  -98.25  North America  Aztecan  Uto-Aztecan  False  False
chl  uppe1439  Chehalis (Upper)  46.5833333333  -123.0  North America  Tsamosan  Salishan  False  False
mme  east2328  Mari (Meadow)  57.0  48.0  Eurasia  Mari  Uralic  False  False
mah  west2392  Mari (Hill)  57.0  58.0  Eurasia  Mari  Uralic  False  False
ing  ingu1240  Ingush  43.1666666667  45.0833333333  Eurasia  Nakh  Nakh-Daghestanian  False  True
man  mann1248  Mano  7.0  -9.0  Africa  Eastern Mande  Niger-Congo  False  False
gus  gusi1247  Gusii  -0.75  34.8333333333  Africa  Bantoid  Niger-Congo  False  False
toj  tojo1241  Tojolabal  16.3333333333  -91.5  North America  Mayan  Mayan  False  False
pia  piar1243  Piaroa  5.0  -67.0  South America  Piaroa  Sáliban  False  False
agr  agua1253  Aguaruna  -5.0  -78.0  South America  Jivaroan  Jivaroan  False  False
cch  choc1279  Chocho  17.6666666667  -97.4166666667  North America  Popolocan  Oto-Manguean  False  False
kat  kate1253  Kâte  -6.5  147.75  Papunesia  Finisterre-Huon  Trans-New Guinea  False  False
tnn  tune1241  Tunen  4.75  10.6666666667  Africa  Bantoid  Niger-Congo  False  False
iir  papu1250  Indonesian (Papuan)  -2.5  140.666666667  Papunesia  Malayo-Sumbawan  Austronesian  False  False
inj  indo1316  Indonesian (Jakarta)  -6.16666666667  106.75  Papunesia  Malayo-Sumbawan  Austronesian  False  False
ind  indo1316  Indonesian  0.0  106.0  Papunesia  Malayo-Sumbawan  Austronesian  True  True
gji  guri1247  Gurindji  -17.6666666667  130.666666667  Australia  Pama-Nyungan  Australian  False  False
yns  yans1239  Yansi  -3.83333333333  18.0  Africa  Bantoid  Niger-Congo  False  False
mao  maor1246  Maori  -40.0  176.0  Papunesia  Oceanic  Austronesian  False  True
nkn  nkon1245  Nkonya  7.16666666667  0.25  Africa  Kwa  Niger-Congo  False  False
ika  arhu1242  Ika  10.6666666667  -73.75  South America  Aruak  Chibchan  False  True
obg  ogbr1243  Ogbronuagum  4.75  6.86666666667  Africa  Cross River  Niger-Congo  False  False
tlf  tele1256  Telefol  -5.0  141.75  Papunesia  Ok  Trans-New Guinea  False  False
jlu  luwo1239  Jur Luwo  8.0  28.0  Africa  Nilotic  Nilo-Saharan  False  False
amz  guer1243  Amuzgo  16.8333333333  -98.0  North America  Amuzgoan  Oto-Manguean  False  False
fur  furr1244  Fur  13.5  25.0  Africa  Fur  Nilo-Saharan  False  True
gmb  guam1248  Guambiano  2.5  -76.6666666667  South America  Barbacoan  Barbacoan  False  False
haw  hawa1245  Hawaiian  19.5833333333  -155.5  Papunesia  Oceanic  Austronesian  False  False
tnk  tung1290  Tungak  -2.55  150.25  Papunesia  Oceanic  Austronesian  False  False
nha  nhan1238  Nhanda  -27.0  114.166666667  Australia  Pama-Nyungan  Australian  False  False
nze  zeme1240  Naga (Zeme)  25.1666666667  93.5  Eurasia  Kuki-Chin  Sino-Tibetan  False  False
crj  cari1279  Carijona  1.0  -73.0  South America  Cariban  Cariban  False  False
umu  cari1279  Umaua  1.0  -72.0  South America  Cariban  Cariban  False  False
kyo  kany1247  Kanyok  -7.33333333333  23.5833333333  Africa  Bantoid  Niger-Congo  False  False
yng  ying1247  Yingkarta  -25.1666666667  114.833333333  Australia  Pama-Nyungan  Australian  False  False
agm  anga1287  Angami  25.6666666667  94.5  Eurasia  Kuki-Chin  Sino-Tibetan  False  False
det  shua1254  Deti  -20.5  24.5  Africa  Central Khoisan  Khoisan  False  False
mko  muku1242  Mokilko  11.9166666667  18.0833333333  Africa  East Chadic  Afro-Asiatic  False  False
sra  sran1240  Sranan  5.83333333333  -55.3333333333  South America  Creoles and Pidgins  other  False  False
ale  aleu1260  Aleut  54.0  -166.0  North America  Aleut  Eskimo-Aleut  False  False
aea  aleu1260  Aleut (Eastern)  54.75  -164.0  North America  Aleut  Eskimo-Aleut  False  False
mot  siwa1245  Motuna  -6.61666666667  155.416666667  Papunesia  East Bougainville  East Bougainville  False  False
mrk  muri1260  Murik  -3.83333333333  144.25  Papunesia  Lower Sepik  Lower Sepik-Ramu  False  False
bar  bari1284  Bari  5.0  31.6666666667  Africa  Nilotic  Nilo-Saharan  False  False
kuk  bari1284  Kukú  5.83333333333  31.6666666667  Africa  Nilotic  Nilo-Saharan  False  False
bgr  furu1242  Bagiro  4.33333333333  20.5833333333  Africa  Bongo-Bagirmi  Nilo-Saharan  False  False
awy  awyi1241  Awyi  -2.91666666667  140.583333333  Papunesia  Border  Border  False  False
vep  veps1250  Veps  60.0  35.0  Eurasia  Finnic  Uralic  False  False
rut  rutu1240  Rutul  41.5  47.4166666667  Eurasia  Lezgic  Nakh-Daghestanian  False  False
one  molm1235  One  -3.25  141.916666667  Papunesia  West Wapei  Torricelli  False  False
wol  wole1240  Woleaian  7.33333333333  143.833333333  Papunesia  Oceanic  Austronesian  False  False
lmn  lamb1269  Lamani  17.0  77.0  Eurasia  Indic  Indo-European  False  False
eng  stan1293  English  52.0  0.0  Eurasia  Germanic  Indo-European  True  True
cyn  chey1247  Cheyenne  47.0  -95.0  North America  Algonquian  Algic  False  False
kyg  keny1279  Kenyang  5.66666666667  9.5  Africa  Bantoid  Niger-Congo  False  False
amh  amha1245  Amharic  10.0  38.0  Africa  Semitic  Afro-Asiatic  False  False
mhc  mohe1244  Mahican  42.6666666667  -73.5  North America  Algonquian  Algic  False  False
wam  wamb1258  Wambaya  -18.6666666667  135.75  Australia  West Barkly  Australian  False  True
rng  reng1252  Rengao  14.5833333333  107.833333333  Eurasia  Bahnaric  Austro-Asiatic  False  False
qay  ayac1239  Quechua (Ayacucho)  -14.0  -74.0  South America  Quechuan  Quechuan  False  False
mcs  cent2140  Miwok (Central Sierra)  38.0  -120.333333333  North America  Miwok  Penutian  False  False
bon  bong1291  Bongu  -5.5  145.916666667  Papunesia  Madang  Trans-New Guinea  False  False
wll  wall1257  Wallisian  -13.3  -176.2  Papunesia  Oceanic  Austronesian  False  False
cha  cham1312  Chamorro  13.45  144.75  Papunesia  Chamorro  Austronesian  True  True
fut  futu1245  Futuna-Aniwa  -19.5333333333  170.216666667  Papunesia  Oceanic  Austronesian  False  False
tbt  toba1266  Tobati  -2.58333333333  140.666666667  Papunesia  Oceanic  Austronesian  False  False
teo  teop1238  Teop  -5.66666666667  155.0  Papunesia  Oceanic  Austronesian  False  False
nne  neng1238  Nengone  -21.5  168.0  Papunesia  Oceanic  Austronesian  False  False
afr  afri1274  Afrikaans  -31.0  22.0  Africa  Germanic  Indo-European  False  False
fre  stan1290  French  48.0  2.0  Eurasia  Romance  Indo-European  True  True
xas  xaas1235  Xasonga  14.25  -10.5  Africa  Western Mande  Niger-Congo  False  False
mxa  atat1238  Mixtec (Atatlahuca)  17.0  -97.75  North America  Mixtecan  Oto-Manguean  False  False
mxc  sanm1295  Mixtec (Chalcatongo)  17.05  -97.5833333333  North America  Mixtecan  Oto-Manguean  True  True
mxj  pino1237  Mixtec (Jicaltepec)  16.3333333333  -98.0  North America  Mixtecan  Oto-Manguean  False  False
mxo  ocot1243  Mixtec (Ocotepec)  17.1666666667  -97.75  North America  Mixtecan  Oto-Manguean  False  False
mxp  peno1244  Mixtec (Peñoles)  17.0833333333  -96.9166666667  North America  Mixtecan  Oto-Manguean  False  False
mxy  yoso1239  Mixtec (Yosondúa)  16.9166666667  -97.5833333333  North America  Mixtecan  Oto-Manguean  False  False
mxt  ayut1236  Mixtec (Ayutla)  16.9166666667  -99.1666666667  North America  Mixtecan  Oto-Manguean  False  False
mxz  coat1241  Mixtec (Coatzospan)  18.0833333333  -96.5833333333  North America  Mixtecan  Oto-Manguean  False  False
mja  jami1235  Mixtec (Jamiltepec)  16.25  -97.8333333333  North America  Mixtecan  Oto-Manguean  False  False
mxm  sanm1295  Mixtec (Molinos)  17.0  -97.5833333333  North America  Mixtecan  Oto-Manguean  False  False
mxu  chay1249  Mixtec (Chayuco)  16.4166666667  -97.8333333333  North America  Mixtecan  Oto-Manguean  False  False
mjc  sanj1281  Mixtec (San Juan Colorado)  16.5  -98.0  North America  Mixtecan  Oto-Manguean  False  False
mxl  alac1244  Mixtec (Alacatlatzala)  17.25  -98.5833333333  North America  Mixtecan  Oto-Manguean  False  False
tuk  tuka1247  Tukang Besi  -5.5  123.5  Papunesia  Celebic  Austronesian  True  True
pwn  pawn1254  Pawnee  41.0  -98.6666666667  North America  Caddoan  Caddoan  False  False
anj  anei1239  Anejom  -20.2  169.8  Papunesia  Oceanic  Austronesian  False  False
kor  kore1280  Korean  37.5  128.0  Eurasia  Korean  Korean  True  True
lus  lush1252  Lushootseed  48.0  -122.0  North America  Central Salish  Salishan  False  False
apl  apal1257  Apalaí  0.0  -54.0  South America  Cariban  Cariban  False  False
dhb  baya1257  Dharumbal  -22.75  150.5  Australia  Pama-Nyungan  Australian  False  False
mkb  coas1301  Miwok (Bodega)  38.3333333333  -123.0  North America  Miwok  Penutian  False  False
hei  heil1246  Heiltsuk  52.0  -127.5  North America  Northern Wakashan  Wakashan  False  False
sue  suen1241  Suena  -7.75  147.55  Papunesia  Binanderean  Trans-New Guinea  False  True
krr  kair1263  Kairiru  -3.33333333333  143.583333333  Papunesia  Oceanic  Austronesian  False  False
bnm  binu1245  Binumarien  -6.28333333333  146.083333333  Papunesia  Eastern Highlands  Trans-New Guinea  False  False
tol  toll1241  Tol  14.6666666667  -87.0  North America  Tol  Tol  False  False
ukr  ukra1253  Ukrainian  49.0  33.0  Eurasia  Slavic  Indo-European  False  False
hwr  gura1251  Hawrami  35.75  45.5  Eurasia  Iranian  Indo-European  False  False
iwm  iwam1256  Iwam  -4.33333333333  142.0  Papunesia  Upper Sepik  Sepik  False  False
xho  xhos1239  Xhosa  -32.0  27.0  Africa  Bantoid  Niger-Congo  False  False
lil  lill1248  Lillooet  50.75  -122.0  North America  Interior Salish  Salishan  False  False
wrd  ward1246  Wardaman  -15.5  131.0  Australia  Yangmanic  Australian  False  True
cop  copt1239  Coptic  26.0  32.0  Africa  Egyptian-Coptic  Afro-Asiatic  False  False
big  yulu1243  Binga  8.0  25.0  Africa  Bongo-Bagirmi  Nilo-Saharan  False  False
yul  yulu1243  Yulu  8.5  25.25  Africa  Bongo-Bagirmi  Nilo-Saharan  False  False
brj  burj1242  Burji  5.5  37.8333333333  Africa  Eastern Cushitic  Afro-Asiatic  False  False
sva  svan1243  Svan  43.0  42.5  Eurasia  Kartvelian  Kartvelian  False  False
ndi  sout2784  Ngbandi  3.75  22.0  Africa  Ubangi  Niger-Congo  False  False
ygd  diii1241  Yag Dii  8.0  14.0  Africa  Adamawa  Niger-Congo  False  False
gnn  kwin1241  Gunin  -14.25  126.666666667  Australia  Wororan  Australian  False  False
cay  chac1249  Cayapa  0.666666666667  -79.0  South America  Barbacoan  Barbacoan  False  False
apk  apuc1241  A-Pucikwar  12.1666666667  92.8333333333  Eurasia  Great Andamanese  Great Andamanese  False  False
tmp  tamp1252  Tampulma  10.4166666667  -0.583333333333  Africa  Gur  Niger-Congo  False  False
wth  wath1238  Wathawurrung  -38.0  144.0  Australia  Pama-Nyungan  Australian  False  False
igs  gaam1241  Ingessana  11.5  34.0  Africa  Eastern Jebel  Nilo-Saharan  False  False
ao  aona1235  Ao  26.5833333333  94.6666666667  Eurasia  Kuki-Chin  Sino-Tibetan  False  False
cam  cams1241  Camsá  1.16666666667  -77.0  South America  Camsá  Camsá  False  False
hsl  hais1244  Haisla  54.0  -128.75  North America  Northern Wakashan  Wakashan  False  False
tnt  tont1239  Tontemboan  1.08333333333  124.5  Papunesia  Minahasan  Austronesian  False  False
zqc  copa1236  Zoque (Copainalá)  17.0  -93.25  North America  Mixe-Zoque  Mixe-Zoque  True  True
zqo  copa1236  Zoque (Ostuacan)  17.4166666667  -93.3  North America  Mixe-Zoque  Mixe-Zoque  False  False
zfl  fran1266  Zoque (Francisco León)  17.3333333333  -93.25  North America  Mixe-Zoque  Mixe-Zoque  False  False
zqr  rayo1235  Zoque (Rayon)  17.0833333333  -93.0  North America  Mixe-Zoque  Mixe-Zoque  False  False
zch  chim1300  Zoque (Chimalapa)  16.75  -94.75  North America  Mixe-Zoque  Mixe-Zoque  False  False
ama  amar1272  Amara  -5.66666666667  148.5  Papunesia  Oceanic  Austronesian  False  False
srl  lowe1385  Sorbian (Lower)  51.75  14.3333333333  Eurasia  Slavic  Indo-European  False  False
yaw  nucl1454  Yawa  -1.75  136.25  Papunesia  Yawa  Yawa  False  False
mhi  mara1378  Marathi  19.0  76.0  Eurasia  Indic  Indo-European  False  False
slb  sali1295  Saliba (in Papua New Guinea)  -10.5833333333  150.716666667  Papunesia  Oceanic  Austronesian  False  False
mar  mari1440  Maricopa  33.1666666667  -113.166666667  North America  Yuman  Hokan  True  True
shu  shus1248  Shuswap  52.0  -120.0  North America  Interior Salish  Salishan  False  False
mrr  mari1419  Maringarr  -14.25  130.0  Australia  Western Daly  Australian  False  False
oku  okuu1243  Oku  6.25  10.5  Africa  Bantoid  Niger-Congo  False  False
ahs  hass1238  Arabic (Bani-Hassan)  20.0  -10.0  Africa  Semitic  Afro-Asiatic  False  False
awi  aeky1238  Aekyom  -5.75  141.416666667  Papunesia  Awin-Pare  Awin-Pare  False  False
emc  embe1262  Embera Chami  5.0  -76.0  South America  Choco  Choco  False  False
mmz  mams1234  Mam (Southern)  14.8333333333  -91.6666666667  North America  Mayan  Mayan  False  False
mam  mamc1234  Mam  15.0  -91.8333333333  North America  Mayan  Mayan  False  False
tsh  pana1305  Tümpisa Shoshone  37.0  -117.0  North America  Numic  Uto-Aztecan  False  False
swr  shos1248  Shoshone (Wind River)  43.4166666667  -108.833333333  North America  Numic  Uto-Aztecan  False  False
sho  shos1248  Shoshone  41.0  -114.0  North America  Numic  Uto-Aztecan  False  False
tsz  dido1241  Tsez  42.25  45.75  Eurasia  Avar-Andic-Tsezic  Nakh-Daghestanian  False  False
bbf  sout2840  Bobo Madaré (Northern)  12.4166666667  -4.33333333333  Africa  Western Mande  Niger-Congo  False  False
tlp  acat1239  Tlapanec  17.0833333333  -99.0  North America  Subtiaba-Tlapanec  Oto-Manguean  False  False
thy  thay1249  Kuuk Thaayorre  -14.5833333333  141.833333333  Australia  Pama-Nyungan  Australian  False  False
shk  ship1254  Shipibo-Konibo  -7.5  -75.0  South America  Panoan  Panoan  False  True
sam  samo1305  Samoan  -13.9166666667  -171.833333333  Papunesia  Oceanic  Austronesian  False  False
moe  erzy1239  Mordvin (Erzya)  53.0  45.5  Eurasia  Mordvin  Uralic  False  False
luy  saam1283  Luyia  0.416666666667  34.5  Africa  Bantoid  Niger-Congo  False  False
ndu  ndum1239  Ndumu  -1.66666666667  13.5833333333  Africa  Bantoid  Niger-Congo  False  False
djp  dhuw1249  Djapu  -12.6666666667  136.0  Australia  Pama-Nyungan  Australian  False  False
gmt  guma1253  Gumatj  -12.5  135.5  Australia  Pama-Nyungan  Australian  False  False
dda  dhuw1249  Dhuwal (Dätiwuy)  -12.1666666667  136.25  Australia  Pama-Nyungan  Australian  False  False
hre  hree1244  Hre  14.6666666667  108.666666667  Eurasia  Bahnaric  Austro-Asiatic  False  False
sob  sobe1238  Sobei  -1.91666666667  138.75  Papunesia  Oceanic  Austronesian  False  False
ari  arib1241  Aribwatsa  -6.71666666667  147.0  Papunesia  Oceanic  Austronesian  False  False
rim  nyat1246  Rimi  -5.0  34.6666666667  Africa  Bantoid  Niger-Congo  False  False
ats  atsu1245  Atsugewi  40.75  -121.0  North America  Palaihnihan  Hokan  False  False
agw  alag1248  Alagwa  -5.5  35.75  Africa  Southern Cushitic  Afro-Asiatic  False  False
unm  unam1242  Unami  40.0  -75.1666666667  North America  Algonquian  Algic  False  False
mwl  lake1258  Miwok (Lake)  38.9166666667  -122.666666667  North America  Miwok  Penutian  False  False
mup  mwag1236  Mupun  9.5  8.83333333333  Africa  West Chadic  Afro-Asiatic  False  False
ntn  nate1242  Nateni  10.5  1.16666666667  Africa  Gur  Niger-Congo  False  False
dmk  doma1260  Dumaki  36.1666666667  74.0  Eurasia  Indic  Indo-European  False  False
lul  lule1238  Lule  -28.0  -64.0  South America  Lule  Lule  False  False
ckl  chin1286  Chinook (Lower)  46.25  -123.5  North America  Chinookan  Penutian  False  False
buw  bulu1251  Bulu  3.0  11.0  Africa  Bantoid  Niger-Congo  False  False
ppi  pitt1247  Pitta Pitta  -22.8333333333  140.0  Australia  Pama-Nyungan  Australian  False  False
msm  muso1238  Musom  -6.58333333333  147.0  Papunesia  Oceanic  Austronesian  False  False
ykm  yako1252  Yakoma  4.41666666667  18.4166666667  Africa  Ubangi  Niger-Congo  False  False
nin  ning1273  Ningil  -3.5  142.25  Papunesia  Wapei-Palei  Torricelli  False  False
ady  adyg1241  Adyghe (Abzakh)  45.2333333333  40.5833333333  Eurasia  Northwest Caucasian  Northwest Caucasian  False  False
adt  adyg1241  Adyghe (Temirgoy)  45.2166666667  39.7  Eurasia  Northwest Caucasian  Northwest Caucasian  False  False
ash  adyg1241  Adyghe (Shapsugh)  45.0  38.75  Eurasia  Northwest Caucasian  Northwest Caucasian  False  False
tin  tiri1258  Tinrin  -21.6666666667  165.75  Papunesia  Oceanic  Austronesian  False  False
jrw  jara1245  Jarawa (in Andamans)  12.0  92.5833333333  Eurasia  South Andamanese  South Andamanese  False  False
cuu  chuu1238  Chuukese  7.33333333333  151.75  Papunesia  Oceanic  Austronesian  False  False
uby  ubyk1235  Ubykh  43.6666666667  39.6666666667  Eurasia  Northwest Caucasian  Northwest Caucasian  False  False
nnt  nant1249  Nanticoke  38.0  -76.25  North America  Algonquian  Algic  False  False
bdk  budu1248  Budukh  41.1666666667  48.4166666667  Eurasia  Lezgic  Nakh-Daghestanian  False  False
kji  nort2641  Kurmanji  38.0  42.0  Eurasia  Iranian  Indo-European  False  False
kbl  kaby1243  Kabyle  36.5  5.0  Africa  Berber  Afro-Asiatic  False  False
ymd  yamd1240  Yamdena  -7.5  131.5  Papunesia  Central Malayo-Polynesian  Austronesian  False  False
mtk  matu1261  Matukar  -4.91666666667  145.75  Papunesia  Oceanic  Austronesian  False  False
wps  wapi1253  Wapishana  2.66666666667  -60.0  South America  Northern Arawakan  Arawakan  False  False
hun  hung1274  Hungarian  47.0  20.0  Eurasia  Ugric  Uralic  False  True
mse  muns1251  Munsee  41.5  -74.6666666667  North America  Algonquian  Algic  False  False
rao  raoo1244  Rao  -4.75  144.5  Papunesia  Annaberg  Lower Sepik-Ramu  False  False
sdh  sind1272  Sindhi  26.0  69.0  Eurasia  Indic  Indo-European  False  False
tar  tari1256  Tariana  1.0  -69.1666666667  South America  Northern Arawakan  Arawakan  False  False
dca  casi1235  Dumagat (Casiguran)  16.3333333333  122.0  Papunesia  Northern Luzon  Austronesian  False  False
tkm  turk1304  Turkmen  40.0  58.0  Eurasia  Turkic  Altaic  False  False
mdb  mudb1240  Mudburra  -17.3333333333  132.083333333  Australia  Pama-Nyungan  Australian  False  False
trt  tern1247  Ternate  0.833333333333  127.25  Papunesia  North Halmaheran  West Papuan  False  False
dha  daas1238  Dhaasanac  4.66666666667  36.3333333333  Africa  Eastern Cushitic  Afro-Asiatic  False  False
kyk  kyak1244  Kyaka  -5.55  144.083333333  Papunesia  Engan  Trans-New Guinea  False  False
ena  enga1252  Enga  -5.5  143.666666667  Papunesia  Engan  Trans-New Guinea  False  False
bdg  bada1257  Badaga  11.6666666667  76.75  Eurasia  Southern Dravidian  Dravidian  False  False
klv  kili1267  Kilivila  -8.5  151.083333333  Papunesia  Oceanic  Austronesian  False  True
kkb  konk1269  Konkomba  10.0  0.0833333333333  Africa  Gur  Niger-Congo  False  False
ark  arak1252  Araki  -15.6666666667  166.916666667  Papunesia  Oceanic  Austronesian  False  False
ktl  katl1237  Katla  11.8333333333  29.3333333333  Africa  Katla-Tima  Niger-Congo  False  False
sta  dong1285  Santa  31.5  107.5  Eurasia  Mongolic  Altaic  False  False
cso  west2644  Chatino (Sierra Occidental)  16.25  -97.3333333333  North America  Zapotecan  Oto-Manguean  False  False
cya  west2644  Chatino (Yaitepec)  16.25  -97.25  North America  Zapotecan  Oto-Manguean  False  False
ctt  tata1258  Chatino (Tataltepec)  16.1666666667  -97.5833333333  North America  Zapotecan  Oto-Manguean  False  False
cht  nopa1235  Chatino (Nopala)  16.0833333333  -97.1666666667  North America  Zapotecan  Oto-Manguean  False  False
map  mapu1245  Mapudungun  -38.0  -72.0  South America  Araucanian  Araucanian  True  True
mab  maba1277  Maba  13.75  20.8333333333  Africa  Maban  Nilo-Saharan  False  True
grj  huar1255  Guarijío  27.75  -108.666666667  North America  Tarahumaran  Uto-Aztecan  False  False
cup  cupe1243  Cupeño  33.1666666667  -116.5  North America  Takic  Uto-Aztecan  False  False
boi  boik1241  Boiken  -3.5  143.5  Papunesia  Middle Sepik  Sepik  False  False
nah  niha1238  Nahali  19.75  77.8333333333  Eurasia  Nahali  Nahali  False  False
kmu  khmu1256  Khmu'  21.0  102.0  Eurasia  Palaung-Khmuic  Austro-Asiatic  False  True
prs  west2369  Persian  32.0  54.0  Eurasia  Iranian  Indo-European  True  True
iau  iauu1242  Iau  -3.16666666667  137.5  Papunesia  Lakes Plain  Lakes Plain  False  False
kby  kabi1261  Kabiyé  9.66666666667  1.16666666667  Africa  Gur  Niger-Congo  False  False
rus  russ1263  Russian  56.0  38.0  Eurasia  Slavic  Indo-European  True  True
wnb  hoch1243  Winnebago  43.5  -88.5  North America  Siouan  Siouan  False  False
swa  swah1253  Swahili  -6.5  39.0  Africa  Bantoid  Niger-Congo  True  True
tht  tehi1237  Tehit  -1.5  132.0  Papunesia  West Bird's Head  West Papuan  False  False
tah  tahi1242  Tahitian  -17.6666666667  -149.583333333  Papunesia  Oceanic  Austronesian  False  False
ksr  kisa1266  Kisar  -8.08333333333  127.116666667  Papunesia  Central Malayo-Polynesian  Austronesian  False  False
bkr  bata1293  Batak (Karo)  3.25  98.25  Papunesia  Northwest Sumatra-Barrier Islands  Austronesian  False  True
snc  sene1264  Seneca  42.5  -77.5  North America  Northern Iroquoian  Iroquoian  False  False
bch  tach1249  Berber (Chaouia)  35.0  7.0  Africa  Berber  Afro-Asiatic  False  False
wrn  wand1263  Warndarang  -14.4166666667  135.583333333  Australia  Maran  Australian  False  False
cro  crow1244  Crow  47.0  -108.0  North America  Siouan  Siouan  False  False
aga  agar1252  Agarabi  -6.16666666667  146.0  Papunesia  Eastern Highlands  Trans-New Guinea  False  False
gds  gads1258  Gadsup  -6.25  146.0  Papunesia  Eastern Highlands  Trans-New Guinea  False  False
baf  bafu1246  Bafut  6.25  9.91666666667  Africa  Bantoid  Niger-Congo  False  False
kiq  kalm1243  Kalmyk (Issyk-Kul)  42.4166666667  78.3333333333  Eurasia  Mongolic  Altaic  False  False
kmk  kalm1243  Kalmyk  44.0  83.0  Eurasia  Mongolic  Altaic  False  False
mnc  manc1252  Manchu  49.5  127.5  Eurasia  Tungusic  Altaic  False  False
beg  idaa1241  Begak-Ida'an  5.25  118.833333333  Papunesia  North Borneo  Austronesian  False  False
sko  nucl1634  Skou  -2.66666666667  140.916666667  Papunesia  Western Skou  Skou  False  False
kwb  nucl1595  Kwerba  -2.25  138.5  Papunesia  Kwerba  Kwerba  False  False
mal  plat1254  Malagasy  -20.0  47.0  Africa  Barito  Austronesian  True  True
ldn  ladi1250  Ladin  46.5833333333  11.9166666667  Eurasia  Romance  Indo-European  False  False
plr  palo1243  Palor  14.8333333333  -16.75  Africa  Northern Atlantic  Niger-Congo  False  False
lho  lhom1239  Lhomi  27.6666666667  87.4166666667  Eurasia  Bodic  Sino-Tibetan  False  False
skk  sikk1242  Sikkimese  27.8333333333  88.5  Eurasia  Bodic  Sino-Tibetan  False  False
klm  klam1254  Klamath  42.5  -121.5  North America  Klamath-Modoc  Penutian  False  False
tns  sout2869  Tanna (Southwest)  -19.5666666667  169.333333333  Papunesia  Oceanic  Austronesian  False  False
wer  weri1253  Weri  -7.75  146.916666667  Papunesia  Goilalan  Trans-New Guinea  False  False
prc  pare1272  Parecis  -14.0  -57.0  South America  Central Arawakan  Arawakan  False  False
all  lala1268  Ala'ala  -8.91666666667  146.75  Papunesia  Oceanic  Austronesian  False  False
yaz  yazg1240  Yazgulyam  38.5  71.5  Eurasia  Iranian  Indo-European  False  False
ccm  coma1246  Chinantec (Comaltepec)  17.5833333333  -96.4166666667  North America  Chinantecan  Oto-Manguean  False  False
cle  leal1235  Chinantec (Lealao)  17.3333333333  -95.9166666667  North America  Chinantecan  Oto-Manguean  False  True
cpl  pala1351  Chinantec (Palantla)  18.8333333333  -96.75  North America  Chinantecan  Oto-Manguean  False  False
chq  quio1240  Chinantec (Quiotepec)  17.5833333333  -96.6666666667  North America  Chinantecan  Oto-Manguean  False  False
csc  soch1239  Chinantec (Sochiapan)  17.75  -96.6666666667  North America  Chinantecan  Oto-Manguean  False  False
cte  tepe1279  Chinantec (Tepetotutla)  17.8333333333  -96.5  North America  Chinantecan  Oto-Manguean  False  False
csf  usil1237  Chinantec (San Felipe Usila)  17.9166666667  -96.5  North America  Chinantecan  Oto-Manguean  False  False
ndt  ndut1239  Ndut  14.9166666667  -16.9166666667  Africa  Northern Atlantic  Niger-Congo  False  False
mpa  murr1258  Murrinh-Patha  -14.6666666667  129.666666667  Australia  Murrinh-Patha  Australian  False  False
awk  pong1250  Akwa  10.0833333333  6.33333333333  Africa  Kainji  Niger-Congo  False  False
kgi  wame1240  Konyagi  12.5  -13.25  Africa  Northern Atlantic  Niger-Congo  False  False
apw  west2615  Apache (Western)  33.75  -110.0  North America  Athapaskan  Na-Dene  False  False
bas  basa1284  Basaá  3.91666666667  10.5  Africa  Bantoid  Niger-Congo  False  False
jak  popt1235  Jakaltek  15.6666666667  -91.6666666667  North America  Mayan  Mayan  True  True
aym  nucl1667  Aymara  -17.0  -69.0  South America  Aymaran  Aymaran  False  True
twa  twan1247  Twana  47.6666666667  -122.75  North America  Central Salish  Salishan  False  False
wap  wapp1239  Wappo  38.5  -122.5  North America  Wappo  Wappo-Yukian  False  False
nmb  sout2994  Nambikuára  -13.0  -59.0  South America  Nambikuaran  Nambikuaran  False  False
eny  enya1247  Enya  -0.5  25.25  Africa  Bantoid  Niger-Congo  False  False
miy  miya1266  Miya  10.9166666667  9.66666666667  Africa  West Chadic  Afro-Asiatic  False  False
ish  sang1316  Ishkashmi  37.0  72.0  Eurasia  Iranian  Indo-European  False  False
fye  fyam1238  Fyem  9.58333333333  9.33333333333  Africa  Platoid  Niger-Congo  False  False
try  tiru1241  Tiruray  6.75  124.166666667  Papunesia  Bilic  Austronesian  False  False
bez  bezh1248  Bezhta  42.0833333333  46.1666666667  Eurasia  Avar-Andic-Tsezic  Nakh-Daghestanian  False  False
orl  orok1267  Orokolo  -7.83333333333  145.333333333  Papunesia  Eleman Proper  Eleman  False  False
rsu  roma1326  Romansch (Sursilvan)  46.6666666667  8.83333333333  Eurasia  Romance  Indo-European  False  False
rsm  roma1326  Romansch (Surmeiran)  46.5833333333  9.75  Eurasia  Romance  Indo-European  False  False
rsc  roma1326  Romansch (Scharans)  46.75  9.5  Eurasia  Romance  Indo-European  False  False
rmc  roma1326  Romansch  46.6666666667  9.16666666667  Eurasia  Romance  Indo-European  False  False
ngd  ngad1261  Ngad'a  -8.83333333333  121.0  Papunesia  Central Malayo-Polynesian  Austronesian  False  False
lkk  lakk1238  Lakkia  24.0833333333  110.166666667  Eurasia  Kadai  Tai-Kadai  False  False
bor  bora1263  Bora  -2.16666666667  -72.3333333333  South America  Boran  Huitotoan  False  False
naj  lish1245  Neo-Aramaic (Arbel Jewish)  31.75  35.0  Eurasia  Semitic  Afro-Asiatic  False  False
naa  chal1275  Neo-Aramaic (Amadiya)  37.0  43.0  Eurasia  Semitic  Afro-Asiatic  False  False
nap  lish1246  Neo-Aramaic (Persian Azerbaijan)  38.0  47.0  Eurasia  Semitic  Afro-Asiatic  False  False
dma  duma1253  Duma  -0.95  13.0  Africa  Bantoid  Niger-Congo  False  False
mem  mane1266  Manem  -3.0  140.833333333  Papunesia  Border  Border  False  False
brm  nucl1310  Burmese  21.0  96.0  Eurasia  Burmese-Lolo  Sino-Tibetan  True  True
yct  yuca1254  Yucatec  20.0  -89.0  North America  Mayan  Mayan  False  False
coe  coeu1236  Coeur d'Alene  47.25  -116.5  North America  Interior Salish  Salishan  False  False
tep  tlac1235  Tepehua (Tlachichilco)  20.5833333333  -98.25  North America  Totonacan  Totonacan  False  False
kkp  kara1467  Karakalpak  43.0  60.0  Eurasia  Turkic  Altaic  False  False
gyb  guay1257  Guayabero  2.83333333333  -72.0  South America  Guahiban  Guahiban  False  False
oss  osse1243  Ossetic  43.0  44.0  Eurasia  Iranian  Indo-European  False  False
bga  beng1282  Benga  1.16666666667  9.41666666667  Africa  Bantoid  Niger-Congo  False  False
tmr  temi1246  Temiar  5.0  101.5  Eurasia  Aslian  Austro-Asiatic  False  False
kyp  kaya1330  Kayapó  -9.0  -52.0  South America  Ge-Kaingang  Macro-Ge  False  False
tbr  taba1263  Tabaru  1.5  127.25  Papunesia  North Halmaheran  West Papuan  False  False
frw  west2354  Frisian (Western)  53.0  6.0  Eurasia  Germanic  Indo-European  False  False
fno  nort2626  Frisian (North)  54.5  9.0  Eurasia  Germanic  Indo-European  False  False
fea  east2288  Frisian (Eastern)  53.5833333333  7.5  Eurasia  Germanic  Indo-European  False  False
fri  east2288  Frisian  53.0  5.0  Eurasia  Germanic  Indo-European  False  False
bmr  buru1306  Burum  -6.5  147.333333333  Papunesia  Finisterre-Huon  Trans-New Guinea  False  False
yag  yagu1244  Yagua  -3.5  -72.0  South America  Peba-Yaguan  Peba-Yaguan  True  True
tmm  malo1243  Tamabo  -15.6666666667  167.166666667  Papunesia  Oceanic  Austronesian  False  False
gdk  pott1240  Gadaba (Kondekor)  18.75  83.5  Eurasia  Central Dravidian  Dravidian  False  False
kbw  bwek1238  Karen (Bwe)  19.5  97.0  Eurasia  Karen  Sino-Tibetan  False  False
kay  kaya1319  Kayardild  -17.05  139.5  Australia  Tangkic  Australian  True  True
ksm  kase1253  Kasem  11.25  -1.25  Africa  Gur  Niger-Congo  False  False
xoo  xooo1239  !Xóõ  -24.0  21.5  Africa  Southern Khoisan  Khoisan  False  False
her  here1253  Herero  -20.5833333333  19.0  Africa  Bantoid  Niger-Congo  False  False
zqs  high1276  Zoque (Soteapan)  18.3333333333  -95.1666666667  North America  Mixe-Zoque  Mixe-Zoque  False  False
chk  chuk1273  Chukchi  67.0  -173.0  Eurasia  Northern Chukotko-Kamchatkan  Chukotko-Kamchatkan  True  True
cme  east2563  Cham (Eastern)  11.3333333333  108.5  Eurasia  Malayo-Sumbawan  Austronesian  False  False
bal  bali1278  Balinese  -8.33333333333  115.25  Papunesia  Malayo-Sumbawan  Austronesian  False  False
knk  dera1248  Kanakuru  10.0  12.0  Africa  West Chadic  Afro-Asiatic  False  False
mds  mala1481  Manadonese  1.5  124.833333333  Papunesia  Malayo-Sumbawan  Austronesian  False  False
ktp  mala1479  Ketapang  -1.86666666667  110.0  Eurasia  Malayo-Sumbawan  Austronesian  False  False
myk  mala1479  Malay (Kuala Lumpur)  3.16666666667  101.7  Eurasia  Malayo-Sumbawan  Austronesian  False  False
kuy  teng1267  Kutai  -0.333333333333  116.666666667  Papunesia  Malayo-Sumbawan  Austronesian  False  False
mly  stan1306  Malay  3.0  102.0  Eurasia  Malayo-Sumbawan  Austronesian  False  False
hav  hava1248  Havasupai  35.75  -112.5  North America  Yuman  Hokan  False  False
kwn  kwan1273  Kwangali  -18.0  19.5  Africa  Bantoid  Niger-Congo  False  False
mbu  mana1298  Manambu  -4.25  142.833333333  Papunesia  Middle Sepik  Sepik  False  False
thw  thao1240  Thao  23.8833333333  120.916666667  Papunesia  Paiwanic  Austronesian  False  False
mri  moro1289  Moraori  -8.58333333333  140.666666667  Papunesia  Moraori  Moraori  False  False
bdc  berb1259  Berbice Dutch Creole  5.33333333333  -58.0  South America  Creoles and Pidgins  other  False  False
cnt  yuec1235  Cantonese  23.0  113.0  Eurasia  Chinese  Sino-Tibetan  False  False
khw  khow1242  Khowar  36.0  72.0  Eurasia  Indic  Indo-European  False  False
mnt  ment1249  Mentawai  -1.5  99.0  Papunesia  Northwest Sumatra-Barrier Islands  Austronesian  False  False
nde  nand1264  Nande  -0.0833333333333  29.1666666667  Africa  Bantoid  Niger-Congo  False  False
mos  mose1249  Mosetén  -14.75  -67.8333333333  South America  Mosetenan  Mosetenan  False  False
iso  isok1239  Isoko  5.5  6.25  Africa  Edoid  Niger-Congo  False  False
ndy  ndyu1242  Ndyuka  4.5  -54.5  South America  Creoles and Pidgins  other  False  True
tow  sout2797  Toussian (Win)  10.8333333333  -4.66666666667  Africa  Gur  Niger-Congo  False  False
tou  tusi1238  Toussian  11.0  -4.66666666667  Africa  Gur  Niger-Congo  False  False
hay  wayu1241  Hayu  27.25  86.0  Eurasia  Mahakiranti  Sino-Tibetan  False  False
rnd  rund1242  Rundi  -3.5  30.0  Africa  Bantoid  Niger-Congo  False  False
mlt  malt1254  Maltese  35.9166666667  14.4166666667  Eurasia  Semitic  Afro-Asiatic  False  False
dua  dual1243  Duala  4.0  9.41666666667  Africa  Bantoid  Niger-Congo  False  False
cad  cadd1256  Caddo  33.3333333333  -93.5  North America  Caddoan  Caddoan  False  False
izi  izie1238  Izi  6.33333333333  8.0  Africa  Igboid  Niger-Congo  False  False
noo  noon1242  Noon  14.8333333333  -16.8333333333  Africa  Northern Atlantic  Niger-Congo  False  False
blr  bela1254  Belorussian  54.0  28.0  Eurasia  Slavic  Indo-European  False  False
wak  wakh1245  Wakhi  36.5  72.0  Eurasia  Iranian  Indo-European  False  False
beo  beot1247  Beothuk  48.0  -57.0  North America  Beothuk  Beothuk  False  False
gur  guru1261  Gurung  28.3333333333  84.3333333333  Eurasia  Bodic  Sino-Tibetan  False  False
yrc  yura1255  Yuracare  -16.5833333333  -65.25  South America  Yuracare  Yuracare  False  False
osa  osag1243  Osage  37.0  -94.0  North America  Siouan  Siouan  False  False
amr  moro1292  Arabic (Moroccan)  34.0  -6.0  Africa  Semitic  Afro-Asiatic  False  False
atu  tuni1259  Arabic (Tunisian)  36.75  10.25  Africa  Semitic  Afro-Asiatic  False  False
ael  liby1240  Arabic (Eastern Libyan)  32.0  22.0  Africa  Semitic  Afro-Asiatic  False  False
abb  chad1249  Arabic (Abbéché Chad)  13.8333333333  20.8333333333  Africa  Semitic  Afro-Asiatic  False  False
arn  chad1249  Arabic (Borno Nigerian)  8.58333333333  12.4166666667  Africa  Semitic  Afro-Asiatic  False  False
pak  paka1251  Pakanha  -14.5  142.416666667  Australia  Pama-Nyungan  Australian  False  False
gdr  gida1247  Gidar  10.0  14.0  Africa  Biu-Mandara  Afro-Asiatic  False  False
chv  chuv1255  Chuvash  55.5  47.5  Eurasia  Turkic  Altaic  False  False
gbk  nort2775  Gbaya Kara  6.0  15.0  Africa  Gbaya-Manza-Ngbaka  Niger-Congo  False  False
gbb  gbay1287  Gbeya Bossangoa  6.66666666667  17.5  Africa  Gbaya-Manza-Ngbaka  Niger-Congo  False  False
mdo  gbay1281  Mbodomo  4.5  15.5  Africa  Gbaya-Manza-Ngbaka  Niger-Congo  False  False
neg  negi1245  Negidal  53.0  139.0  Eurasia  Tungusic  Altaic  False  False
tgw  west2538  Tarangan (West)  -6.5  134.166666667  Papunesia  Central Malayo-Polynesian  Austronesian  False  False
bka  baka1274  Baka (in Sudan)  4.83333333333  29.25  Africa  Bongo-Bagirmi  Nilo-Saharan  False  False
bak  baka1272  Baka (in Cameroon)  2.58333333333  13.5833333333  Africa  Ubangi  Niger-Congo  False  False
sol  even1259  Solon  48.0  120.0  Eurasia  Tungusic  Altaic  False  False
tub  tuba1279  Tubar  27.0  -108.0  North America  Tubar  Uto-Aztecan  False  False
kwz  kwaz1243  Kwazá  -12.5833333333  -60.6666666667  South America  Kwaza  Kwaza  False  False
bua  bura1267  Burarra  -12.25  134.583333333  Australia  Burarran  Australian  False  False
aul  aulu1238  Aulua  -16.3333333333  167.666666667  Papunesia  Oceanic  Austronesian  False  False
rot  rotu1241  Rotuman  -12.5  177.066666667  Papunesia  Oceanic  Austronesian  False  False
tmu  musl1236  Tat (Muslim)  41.25  48.75  Eurasia  Iranian  Indo-European  False  False
tbb  tuba1278  Tübatulabal  36.0  -118.333333333  North America  Tubatulabal  Uto-Aztecan  False  False
yba  yamb1251  Yamba  6.41666666667  11.0833333333  Africa  Bantoid  Niger-Congo  False  False
mno  mono1275  Mono (in United States)  38.0  -119.0  North America  Numic  Uto-Aztecan  False  False
moa  mono1273  Mono-Alu  -7.05  155.75  Papunesia  Oceanic  Austronesian  False  False
slr  sala1264  Salar  35.0  103.0  Eurasia  Turkic  Altaic  False  False
yid  yidi1250  Yidiny  -17.0  145.75  Australia  Pama-Nyungan  Australian  False  True
knu  rapo1238  Konua  -5.83333333333  154.833333333  Papunesia  West Bougainville  West Bougainville  False  False
shi  nina1238  Shiriana  3.5  -62.8333333333  South America  Yanomam  Yanomam  False  False
aml  east2443  Ambae (Lolovoli Northeast)  -15.4166666667  167.883333333  Papunesia  Oceanic  Austronesian  False  False
mcg  maca1259  Macaguán  6.5  -71.3333333333  South America  Guahiban  Guahiban  False  False
mdl  madn1237  Madngele  -13.8333333333  130.416666667  Australia  Eastern Daly  Australian  False  False
coi  chor1273  Chortí  14.8333333333  -89.25  North America  Mayan  Mayan  False  False
har  haru1245  Haruai  -5.08333333333  144.166666667  Papunesia  Piawi  Piawi  False  False
ren  rend1243  Rendille  2.0  37.5  Africa  Eastern Cushitic  Afro-Asiatic  False  False
cln  chol1284  Cholón  -8.0  -77.5  South America  Cholon  Cholon  False  False
bgl  bugl1243  Buglere  8.5  -81.25  North America  Guaymi  Chibchan  False  False
ayo  None  Ayomán  11.0  -69.0  None  Jirajaran  Jirajaran  False  False
kss  sout2778  Kisi (Southern)  8.5  -10.25  Africa  Southern Atlantic  Niger-Congo  False  False
kis  kiss1245  Kisi  8.83333333333  -10.1666666667  Africa  Southern Atlantic  Niger-Congo  False  False
hok  minn1241  Hokkien  25.0  118.0  Eurasia  Chinese  Sino-Tibetan  False  False
chz  minn1241  Chaozhou  23.6666666667  116.666666667  Eurasia  Chinese  Sino-Tibetan  False  False
gaa  gaga1251  Gaagudju  -12.5833333333  132.833333333  Australia  Gaagudju  Australian  False  False
mmw  mamb1296  Mambwe  -9.08333333333  31.1666666667  Africa  Bantoid  Niger-Congo  False  False
biq  sara1326  Bilaan  6.0  125.333333333  Papunesia  Bilic  Austronesian  False  False
bnr  ngar1235  Bilinara  -16.0  131.666666667  Australia  Pama-Nyungan  Australian  False  False
ngy  ngar1235  Ngarinyman  -16.5  130.5  Australia  Pama-Nyungan  Australian  False  False
toy  None  Tasmanian (Oyster Bay to Pitwater)  -42.5  147.75  None  Tasmanian  Tasmanian  False  False
tsm  None  Tasmanian  -42.1666666667  146.5  None  Tasmanian  Tasmanian  False  False
meh  mehr1241  Mehri  17.0  51.5  Eurasia  Semitic  Afro-Asiatic  False  False
hrs  hars1241  Harsusi  20.0  56.5  Eurasia  Semitic  Afro-Asiatic  False  False
bth  bath1244  Bathari  18.0  56.0  Eurasia  Semitic  Afro-Asiatic  False  False
jib  sheh1240  Jibbali  17.5  55.0  Eurasia  Semitic  Afro-Asiatic  False  False
soq  soqo1240  Soqotri  12.5  54.0  Africa  Semitic  Afro-Asiatic  False  False
may  maib1239  Maybrat  -1.33333333333  132.5  Papunesia  North-Central Bird's Head  West Papuan  True  True
zap  mitl1236  Zapotec (Mitla)  16.8  -96.25  North America  Zapotecan  Oto-Manguean  False  False
zsq  sanj1284  Zapotec (San Lucas Quiaviní)  16.9  -96.4666666667  North America  Zapotecan  Oto-Manguean  False  False
zai  isth1244  Zapotec (Isthmus)  16.416667  -95.0  North America  Zapotecan  Oto-Manguean  False  False
zya  yatz1235  Zapotec (Yatzachi)  17.2  -96.2  North America  Zapotecan  Oto-Manguean  False  False
zaq  sant1451  Zapotec (Quiegolani)  16.1666666667  -96.0833333333  North America  Zapotecan  Oto-Manguean  False  False
zzo  zoog1238  Zapotec (Zoogocho)  17.25  -96.25  North America  Zapotecan  Oto-Manguean  False  False
zaj  sier1250  Zapotec (Juárez)  17.5  -96.5833333333  North America  Zapotecan  Oto-Manguean  False  False
zam  mixt1426  Zapotec (Mixtepec)  16.3333333333  -96.3333333333  North America  Zapotecan  Oto-Manguean  False  False
zpi  sout3005  Zapotec (Ixtlan)  17.25  -96.5  North America  Zapotecan  Oto-Manguean  False  False
zte  texm1235  Zapotec (Texmelucan)  16.5  -97.1666666667  North America  Zapotecan  Oto-Manguean  False  False
muh  seba1251  Muher  8.16666666667  38.1666666667  Africa  Semitic  Afro-Asiatic  False  False
day  dayy1236  Day  8.75  17.8333333333  Africa  Adamawa  Niger-Congo  False  False
pal  pala1344  Palauan  7.5  134.583333333  Papunesia  Palauan  Austronesian  False  False
urn  urar1246  Urarina  -4.5  -75.5  South America  Urarina  Urarina  False  False
rum  rumu1243  Rumu  -7.16666666667  144.25  Papunesia  Turama-Kikorian  Turama-Kikorian  False  False
irq  iraq1241  Iraqw  -4.0  35.5  Africa  Southern Cushitic  Afro-Asiatic  False  True
toz  tong1318  Tonga (in Zambia)  -17.0  27.0  Africa  Bantoid  Niger-Congo  False  False
qui  quil1240  Quileute  47.9166666667  -124.25  North America  Chimakuan  Chimakuan  False  False
izh  ingr1248  Izhor  59.0  29.0  Eurasia  Finnic  Uralic  False  False
diz  dizi1235  Dizi  6.16666666667  36.5  Africa  North Omotic  Afro-Asiatic  False  False
tmo  tibe1272  Tibetan (Modern Literary)  29.8333333333  91.5  Eurasia  Bodic  Sino-Tibetan  False  False
tod  stod1241  Tod  32.4166666667  77.25  Eurasia  Bodic  Sino-Tibetan  False  False
tis  tibe1272  Tibetan (Shigatse)  29.0  89.0  Eurasia  Bodic  Sino-Tibetan  False  False
tib  tibe1272  Tibetan (Standard Spoken)  30.0  91.0  Eurasia  Bodic  Sino-Tibetan  False  False
tna  turk1308  Turkana  3.0  35.5  Africa  Nilotic  Nilo-Saharan  False  False
yaq  yaqu1251  Yaqui  27.5  -110.25  North America  Cahita  Uto-Aztecan  True  True
stl  sant1410  Santali  24.5  87.0  Eurasia  Munda  Austro-Asiatic  False  False
nar  nara1262  Nara (in Ethiopia)  15.0833333333  37.5833333333  Africa  Nara  Nilo-Saharan  False  False
mrd  nucl1622  Marind  -7.83333333333  140.166666667  Papunesia  Marind Proper  Marind  False  True
yor  yoru1245  Yoruba  8.0  4.33333333333  Africa  Defoid  Niger-Congo  True  True
sar  kapr1245  Sare  -4.5  143.166666667  Papunesia  Sepik Hill  Sepik  False  False
guq  cari1279  Guaque  1.0  -72.0833333333  South America  Cariban  Cariban  False  False
kdw  kadi1248  Kadiwéu  -20.0  -57.0  South America  Guaicuruan  Guaicuruan  False  False
nia  nias1242  Nias  1.0  97.75  Papunesia  Northwest Sumatra-Barrier Islands  Austronesian  False  False
orc  oroc1248  Oroch  50.3333333333  137.5  Eurasia  Tungusic  Altaic  False  False
bla  siks1238  Blackfoot  50.0  -112.666666667  North America  Algonquian  Algic  False  False
kms  kama1351  Kamass  52.0  92.0  Eurasia  Samoyedic  Uralic  False  False
tas  tach1250  Tashlhiyt  31.0  -5.0  Africa  Berber  Afro-Asiatic  False  False
eip  eipo1242  Eipo  -4.33333333333  140.083333333  Papunesia  Mek  Trans-New Guinea  False  False
dhw  thur1254  Dharawal  -34.5  150.5  Australia  Pama-Nyungan  Australian  False  False
bzi  bauz1241  Bauzi  -2.5  137.5  Papunesia  East Geelvink Bay  East Geelvink Bay  False  False
vag  vagl1239  Vagla  9.41666666667  -2.41666666667  Africa  Gur  Niger-Congo  False  False
bag  bagi1246  Bagirmi  11.6666666667  16.0  Africa  Bongo-Bagirmi  Nilo-Saharan  True  True
idn  idun1242  Iduna  -9.33333333333  150.25  Papunesia  Oceanic  Austronesian  False  False
heh  hehe1240  Hehe  -8.0  36.0  Africa  Bantoid  Niger-Congo  False  False
plk  pali1279  Palikur  3.0  -51.0  South America  Eastern Arawakan  Arawakan  False  False
pso  sout2982  Pomo (Southeastern)  39.0  -122.5  North America  Pomoan  Hokan  False  True
lgt  logo1259  Logoti  3.5  30.0  Africa  Moru-Ma'di  Nilo-Saharan  False  False
dri  dari1249  Dari  35.0  66.0  Eurasia  Iranian  Indo-European  False  False
bkd  binu1244  Binukid  8.25  124.833333333  Papunesia  Greater Central Philippine  Austronesian  False  False
acm  achu1247  Achumawi  41.5  -121.0  North America  Palaihnihan  Hokan  False  False
akl  akla1241  Aklanon  11.5833333333  122.333333333  Papunesia  Greater Central Philippine  Austronesian  False  False
kje  kore1283  Koreguaje  1.0  -75.5  South America  Tucanoan  Tucanoan  False  False
tgo  tsog1243  Tsogo  -1.5  11.3333333333  Africa  Bantoid  Niger-Congo  False  False
mwb  west2555  Manobo (Western Bukidnon)  7.66666666667  124.75  Papunesia  Greater Central Philippine  Austronesian  False  False
mga  ndun1249  Mondunga  2.25  21.5  Africa  Ubangi  Niger-Congo  False  False
lda  gand1255  Luganda  0.5  32.1666666667  Africa  Bantoid  Niger-Congo  False  False
mnv  mina1269  Minaveha  -9.6  150.466666667  Papunesia  Oceanic  Austronesian  False  False
nkr  nuku1260  Nukuoro  3.83333333333  154.916666667  Papunesia  Oceanic  Austronesian  False  False
pre  asut1235  Pare  -4.0  36.5  Africa  Bantoid  Niger-Congo  False  False
che  cher1273  Cherokee  35.5  -83.5  North America  Southern Iroquoian  Iroquoian  False  False
pdp  folo1238  Folopa  -7.0  144.5  Papunesia  Teberan  Teberan-Pawaian  False  False
wrs  wari1266  Waris  -3.16666666667  141.0  Papunesia  Border  Border  False  False
nak  naka1262  Nakanai  -5.58333333333  150.583333333  Papunesia  Oceanic  Austronesian  False  False
jpn  nucl1643  Japanese  37.0  140.0  Eurasia  Japanese  Japanese  True  True
lep  lepc1244  Lepcha  27.1666666667  88.5  Eurasia  Lepcha  Sino-Tibetan  False  True
drg  darg1241  Dargwa  42.25  47.4166666667  Eurasia  Lak-Dargwa  Nakh-Daghestanian  False  False
tzs  tzot1260  Tzotzil (San Andrés)  17.0  -92.8333333333  North America  Mayan  Mayan  False  False
tzz  tzot1264  Tzotzil (Zinacantán)  16.8333333333  -92.8333333333  North America  Mayan  Mayan  False  False
tzo  tzot1262  Tzotzil  16.5  -92.6666666667  North America  Mayan  Mayan  False  False
grt  goro1259  Gorontalo  0.5  122.0  Papunesia  Greater Central Philippine  Austronesian  False  False
onn  onon1246  Onondaga  42.75  -76.1666666667  North America  Northern Iroquoian  Iroquoian  False  False
cnm  kana1291  Canamarí  -6.5  -68.5  South America  Katukinan  Katukinan  False  False
kkw  kara1289  Karankawa  28.0  -97.0  North America  Karankawa  Karankawa  False  False
hln  hala1252  Halang  14.5  107.5  Eurasia  Bahnaric  Austro-Asiatic  False  False
mki  mika1239  Mikasuki  32.0  -85.0  North America  Muskogean  Muskogean  False  False
mtt  wamp1249  Massachusett  42.5  -71.0  North America  Algonquian  Algic  False  False
jad  tibe1272  Jad  30.8333333333  79.0  Eurasia  Bodic  Sino-Tibetan  False  False
pna  pamo1252  Pamona  -1.75  120.833333333  Papunesia  Celebic  Austronesian  False  False
wnt  want1252  Wantoat  -6.16666666667  146.5  Papunesia  Finisterre-Huon  Trans-New Guinea  False  False
akk  akak1252  Aka-Kede  12.75  92.75  Eurasia  Great Andamanese  Great Andamanese  False  False
atm  kunz1244  Atacameño  -23.0  -69.0  South America  Kunza  Kunza  False  False
ngl  ngal1293  Ngalakan  -14.25  134.0  Australia  Ngalakan  Australian  False  False
wob  weno1238  Wobe  7.41666666667  -7.33333333333  Africa  Kru  Niger-Congo  False  False
brr  boro1282  Bororo  -16.0  -57.0  South America  Bororo  Macro-Ge  False  False
krc  kara1465  Karachay-Balkar  43.5  42.0  Eurasia  Turkic  Altaic  False  False
els  else1239  Elseng  -3.0  140.5  Papunesia  Morwap  Morwap  False  False
amq  amba1265  Ambai  -1.83333333333  136.5  Papunesia  South Halmahera - West New Guinea  Austronesian  False  False
mud  mund1327  Mundani  5.66666666667  9.91666666667  Africa  Bantoid  Niger-Congo  False  False
nga  ngan1291  Nganasan  71.0  93.0  Eurasia  Samoyedic  Uralic  False  False
nbr  ngab1239  Ngäbere  8.66666666667  -82.0  North America  Guaymi  Chibchan  False  False
ora  emai1241  Emai  7.08333333333  5.91666666667  Africa  Edoid  Niger-Congo  False  False
dgi  indo1311  Dogri  33.0  75.0  Eurasia  Indic  Indo-European  False  False
cre  plai1258  Cree (Plains)  54.0  -110.0  North America  Algonquian  Algic  True  True
agu  agua1252  Aguacatec  15.4166666667  -91.3333333333  North America  Mayan  Mayan  False  False
oks  oksa1245  Oksapmin  -5.16666666667  142.166666667  Papunesia  Oksapmin  Oksapmin  False  False
ina  suab1238  Inanwatan  -2.08333333333  132.083333333  Papunesia  South Bird's Head  Marind  False  False
gku  puel1244  Gününa Küne  -41.0  -67.0  South America  Puelche  Chon  False  False
nma  maon1238  Naga (Mao)  25.5  94.3333333333  Eurasia  Kuki-Chin  Sino-Tibetan  False  False
rga  rong1268  Ronga  -26.0  32.5  Africa  Bantoid  Niger-Congo  False  False
pme  east2545  Pomo (Eastern)  39.0  -122.666666667  North America  Pomoan  Hokan  False  False
cut  cuit1236  Cuitlatec  17.5  -101.0  North America  Cuitlatec  Cuitlatec  False  False
hid  hida1246  Hidatsa  47.0  -102.5  North America  Siouan  Siouan  False  False
tzu  cakc1244  Tzutujil  14.6666666667  -91.3333333333  North America  Mayan  Mayan  False  False
yin  yind1247  Yindjibarndi  -21.75  117.916666667  Australia  Pama-Nyungan  Australian  False  False
cly  chul1246  Chulym  54.3333333333  89.6666666667  Eurasia  Turkic  Altaic  False  False
yan  yana1271  Yana  40.5  -122.0  North America  Yana  Hokan  False  False
juk  juku1254  Jukun  6.91666666667  10.4166666667  Africa  Platoid  Niger-Congo  False  False
nav  nava1243  Navajo  36.1666666667  -108.0  North America  Athapaskan  Na-Dene  False  True
nkt  nyah1250  Nyah Kur (Tha Pong)  15.6666666667  101.666666667  Eurasia  Monic  Austro-Asiatic  False  False
sed  seda1262  Sedang  14.8333333333  108.0  Eurasia  Bahnaric  Austro-Asiatic  False  False
krl  kare1335  Karelian  64.0  32.0  Eurasia  Finnic  Uralic  False  False
tse  uabm1237  Timorese  -9.66666666667  124.5  Papunesia  Central Malayo-Polynesian  Austronesian  False  False
jcr  jama1262  Jamaican Creole  18.1666666667  -77.25  North America  Creoles and Pidgins  other  False  False
nyl  nyal1254  Nyelâyu  -20.3333333333  164.333333333  Papunesia  Oceanic  Austronesian  False  False
shh  shar1245  Sharanahua  -11.0  -70.0  South America  Panoan  Panoan  False  False
obk  obok1239  Obokuitai  -3.0  138.0  Papunesia  Lakes Plain  Lakes Plain  False  False
wgl  waig1243  Waigali  35.0  71.25  Eurasia  Indic  Indo-European  False  False
ibi  ibib1240  Ibibio  5.25  7.83333333333  Africa  Cross River  Niger-Congo  False  False
bsi  siwi1239  Berber (Siwa)  29.1666666667  25.5  Africa  Berber  Afro-Asiatic  False  False
mua  makh1264  Makua  -15.0  38.6666666667  Africa  Bantoid  Niger-Congo  False  False
mkg  mand1436  Mandinka (Gambian)  13.4166666667  -16.0  Africa  Western Mande  Niger-Congo  False  False
mdk  mand1436  Mandinka  13.0  -15.6666666667  Africa  Western Mande  Niger-Congo  False  False
crp  cara1272  Carapana  0.833333333333  -70.75  South America  Tucanoan  Tucanoan  False  False
aci  quic1275  Achí  15.1666666667  -90.5  North America  Mayan  Mayan  False  False
bsq  basq1248  Basque  43.0  -3.0  Eurasia  Basque  Basque  True  True
bqb  basq1248  Basque (Bidasoa Valley)  43.0  -3.83333333333  Eurasia  Basque  Basque  False  False
bqg  basq1248  Basque (Gernica)  43.3333333333  -3.0  Eurasia  Basque  Basque  False  False
bqh  basq1248  Basque (Hondarribia)  42.5  -3.0  Eurasia  Basque  Basque  False  False
bql  basq1248  Basque (Lekeitio)  43.0  -2.5  Eurasia  Basque  Basque  False  False
bqn  basq1248  Basque (Northern High Navarrese)  43.3333333333  -2.5  Eurasia  Basque  Basque  False  False
bqo  basq1248  Basque (Oñati)  42.5  -3.5  Eurasia  Basque  Basque  False  False
bqr  basq1248  Basque (Roncalese)  43.0  -2.0  Eurasia  Basque  Basque  False  False
bqs  basq1248  Basque (Sakana)  42.5  -2.0  Eurasia  Basque  Basque  False  False
bso  basq1250  Basque (Souletin)  43.5  -1.5  Eurasia  Basque  Basque  False  False
bqz  basq1248  Basque (Zeberio)  42.0  -3.0  Eurasia  Basque  Basque  False  False
bqi  basq1248  Basque (Basaburua and Imoz)  43.0  -1.66666666667  Eurasia  Basque  Basque  False  False
gcy  mode1248  Greek (Cypriot)  34.75  33.0  Eurasia  Greek  Indo-European  False  False
grk  mode1248  Greek (Modern)  39.0  22.0  Eurasia  Greek  Indo-European  True  True
mer  meri1244  Meryam Mir  -9.91666666667  144.083333333  Papunesia  Western Fly  Western Fly  False  False
des  desa1247  Desano  0.833333333333  -69.8333333333  South America  Tucanoan  Tucanoan  False  False
kre  gbay1288  Kresh  8.5  24.5  Africa  Kresh  Nilo-Saharan  False  False
kte  kete1252  Kete  -7.0  22.8333333333  Africa  Bantoid  Niger-Congo  False  False
mtl  matt1238  Mattole  40.1666666667  -124.166666667  North America  Athapaskan  Na-Dene  False  False
ttu  bats1242  Tsova-Tush  42.5  45.5  Eurasia  Nakh  Nakh-Daghestanian  False  False
koo  kola1285  Kola  -5.5  134.5  Papunesia  Central Malayo-Polynesian  Austronesian  False  False
dja  dyaa1242  Djabugay  -16.75  145.583333333  Australia  Pama-Nyungan  Australian  False  False
taw  tawa1275  Tawala  -10.3333333333  150.666666667  Papunesia  Oceanic  Austronesian  False  False
mrw  muru1266  Muruwari  -28.75  147.0  Australia  Pama-Nyungan  Australian  False  False
ven  vend1245  Venda  -22.0  30.0  Africa  Bantoid  Niger-Congo  False  False
kai  kaia1245  Kaian  -4.08333333333  144.75  Papunesia  Lower Ramu  Lower Sepik-Ramu  False  False
tiw  tiwi1244  Tiwi  -11.5  131.0  Australia  Tiwian  Australian  True  True
cah  cahu1264  Cahuilla  33.5  -116.25  North America  Takic  Uto-Aztecan  False  True
ken  keng1240  Kenga  12.0  18.0  Africa  Bongo-Bagirmi  Nilo-Saharan  False  False
srm  sara1340  Saramaccan  4.5  -55.5  South America  Creoles and Pidgins  other  False  False
oma  omag1248  Omagua  -4.0  -73.5  South America  Tupi-Guaraní  Tupian  False  False
bnk  bank1256  Bankon  4.41666666667  9.58333333333  Africa  Bantoid  Niger-Congo  False  False
ber  bert1248  Berta  10.3333333333  34.6666666667  Africa  Berta  Nilo-Saharan  False  False
ret  tani1257  Retuarã  -0.5  -70.6666666667  South America  Tucanoan  Tucanoan  False  False
alu  alut1245  Alutor  61.0  165.0  Eurasia  Northern Chukotko-Kamchatkan  Chukotko-Kamchatkan  False  False
dgx  dege1248  Degexit'an  62.0  -160.0  North America  Athapaskan  Na-Dene  False  False
lnw  lonw1238  Lonwolwol  -16.2166666667  168.0  Papunesia  Oceanic  Austronesian  False  False
nkb  ngal1292  Ngalkbun  -13.5  134.833333333  Australia  Gunwinygic  Australian  False  False
olo  oloo1241  Olo  -3.41666666667  142.0  Papunesia  Wapei-Palei  Torricelli  False  False
stn  pedi1238  Sotho (Northern)  -24.0  29.0  Africa  Bantoid  Niger-Congo  False  False
knr  cent2050  Kanuri  12.0  13.0  Africa  Western Saharan  Nilo-Saharan  False  True
gar  garo1247  Garo  25.6666666667  90.5  Eurasia  Bodo-Garo  Sino-Tibetan  False  True
kse  koyr1242  Koyraboro Senni  16.0  0.0  Africa  Songhay  Nilo-Saharan  True  True
kch  koyr1240  Koyra Chiini  17.0  -3.0  Africa  Songhay  Nilo-Saharan  False  False
toq  toab1237  Toqabaqita  -8.41666666667  160.583333333  Papunesia  Oceanic  Austronesian  False  False
lez  lezg1247  Lezgian  41.6666666667  47.8333333333  Eurasia  Lezgic  Nakh-Daghestanian  True  True
qaf  afar1241  Qafar  12.0  42.0  Africa  Eastern Cushitic  Afro-Asiatic  False  False
alb  tosk1239  Albanian  41.0  20.0  Eurasia  Albanian  Indo-European  False  False
dim  dime1235  Dime  6.16666666667  36.25  Africa  South Omotic  Afro-Asiatic  False  False
url  urak1238  Urak Lawoi'  8.0  98.3333333333  Eurasia  Malayo-Sumbawan  Austronesian  False  False
mco  coat1238  Mixe (Coatlán)  16.9166666667  -95.6666666667  North America  Mixe-Zoque  Mixe-Zoque  False  False
mth  tlah1239  Mixe (Tlahuitoltepec)  17.0833333333  -96.1666666667  North America  Mixe-Zoque  Mixe-Zoque  False  False
mtp  toto1305  Mixe (Totontepec)  17.25  -96.0  North America  Mixe-Zoque  Mixe-Zoque  False  False
dhi  dhiv1236  Dhivehi  4.16666666667  73.5  Eurasia  Indic  Indo-European  False  False
paw  pawa1255  Pawaian  -7.0  145.083333333  Papunesia  Pawaian  Teberan-Pawaian  False  False
sal  sali1253  Salinan  36.0  -121.0  North America  Salinan  Salinan  False  False
krf  kora1294  Korafe  -9.05  149.083333333  Papunesia  Binanderean  Trans-New Guinea  False  False
nis  nisi1239  Nyishi  27.5  93.5  Eurasia  Tani  Sino-Tibetan  False  False
mle  male1284  Maale  6.0  36.9166666667  Africa  North Omotic  Afro-Asiatic  False  False
kpm  pamp1243  Kapampangan  15.3333333333  120.5  Papunesia  Central Luzon  Austronesian  False  False
mwe  mwer1248  Mwera  -9.0  39.0  Africa  Bantoid  Niger-Congo  False  False
kho  nama1264  Khoekhoe  -25.5  18.0  Africa  Central Khoisan  Khoisan  True  True
bkt  brok1247  Brokskat  35.3333333333  76.5  Eurasia  Indic  Indo-European  False  False
sav  savi1242  Savi  35.0  71.5  Eurasia  Indic  Indo-European  False  False
sna  shin1264  Shina  36.0  74.0  Eurasia  Indic  Indo-European  False  False
sht  shat1244  Shatt  10.8333333333  30.0  Africa  Daju  Nilo-Saharan  False  False
mng  mang1405  Manggarai  -8.5  120.333333333  Papunesia  Central Malayo-Polynesian  Austronesian  False  False
yta  noga1249  Yurt Tatar  46.3333333333  48.5  Eurasia  Turkic  Altaic  False  False
tlb  noga1249  Tatar-Noghay (Alabugat)  47.4166666667  45.6666666667  Eurasia  Turkic  Altaic  False  False
nok  noga1249  Noghay (Karagash)  47.5  47.25  Eurasia  Turkic  Altaic  False  False
nog  noga1249  Noghay  44.0  46.0  Eurasia  Turkic  Altaic  False  False
jah  jeha1242  Jahai  5.75  101.5  Eurasia  Aslian  Austro-Asiatic  False  False
rwe  wels1246  Romani (Welsh)  52.0  -4.0  Eurasia  Indic  Indo-European  False  False
rka  vlax1238  Romani (Kalderash)  45.0  21.0  Eurasia  Indic  Indo-European  False  False
rav  balk1252  Romani (Ajia Varvara)  38.0  23.5833333333  Eurasia  Indic  Indo-European  False  False
rnr  balt1257  Romani (North Russian)  60.0  38.0  Eurasia  Indic  Indo-European  False  False
rbu  balk1252  Romani (Bugurdzi)  42.6666666667  21.1666666667  Eurasia  Indic  Indo-European  False  False
rlo  vlax1238  Romani (Lovari)  47.0  21.5  Eurasia  Indic  Indo-European  False  False
rbg  sint1235  Romani (Burgenland)  47.5  16.5  Eurasia  Indic  Indo-European  False  False
rse  None  Romani (Sepecides)  38.25  27.0  None  Indic  Indo-European  False  False
cas  cash1251  Cashibo  -8.5  -75.5  South America  Panoan  Panoan  False  False
mit  mitu1240  Mituku  -1.66666666667  25.5  Africa  Bantoid  Niger-Congo  False  False
hwc  hawa1247  Hawaiian Creole  21.5  -158.0  North America  Creoles and Pidgins  other  False  False
gro  guro1248  Guro  7.0  -6.0  Africa  Eastern Mande  Niger-Congo  False  False
nro  naro1249  Nharo  -22.3333333333  20.5  Africa  Central Khoisan  Khoisan  False  False
anc  ngas1240  Angas  9.5  9.5  Africa  West Chadic  Afro-Asiatic  False  False
eya  eyak1241  Eyak  60.5  -145.0  North America  Eyak  Na-Dene  False  False
yes  yess1239  Yessan-Mayo  -4.16666666667  142.583333333  Papunesia  Tama Sepik  Sepik  False  False
tab  east2440  Taba  0.0  127.5  Papunesia  South Halmahera - West New Guinea  Austronesian  False  True
slp  sele1250  Selepet  -6.16666666667  147.166666667  Papunesia  Finisterre-Huon  Trans-New Guinea  False  False
ddf  darf1239  Daju (Dar Fur)  12.25  25.25  Africa  Daju  Nilo-Saharan  False  False
kil  luba1250  Kiluba  -8.0  26.0  Africa  Bantoid  Niger-Congo  False  False
gll  gale1259  Galela  2.41666666667  128.333333333  Papunesia  North Halmaheran  West Papuan  False  False
cze  czec1258  Czech  50.0  15.0  Eurasia  Slavic  Indo-European  False  False
pot  pota1247  Potawatomi  44.5  -85.0  North America  Algonquian  Algic  False  False
wya  wyan1247  Wyandot  44.3333333333  -77.5  North America  Northern Iroquoian  Iroquoian  False  False
psh  cent1973  Pashto  33.0  67.0  Eurasia  Iranian  Indo-European  False  False
kuv  kuvi1243  Kuvi  18.75  82.6666666667  Eurasia  South-Central Dravidian  Dravidian  False  False
raw  rawa1265  Rawang  27.5  97.5  Eurasia  Nungish  Sino-Tibetan  False  False
def  defa1248  Defaka  4.58333333333  7.5  Africa  Ijoid  Niger-Congo  False  False
mcv  moco1246  Mocoví  -28.0  -60.5  South America  Guaicuruan  Guaicuruan  False  False
kjr  koor1239  Koorete  5.83333333333  37.8333333333  Africa  North Omotic  Afro-Asiatic  False  False
ssa  west2465  Sisaala  10.8333333333  -2.66666666667  Africa  Gur  Niger-Congo  False  False
skw  shek1243  Shekhawati  28.0  75.5  Eurasia  Indic  Indo-European  False  False
srd  camp1261  Sardinian  40.0  9.0  Eurasia  Romance  Indo-European  False  False
koh  kohu1244  Kohumono  6.0  8.11666666667  Africa  Cross River  Niger-Congo  False  False
vai  vaii1241  Vai  6.91666666667  -11.25  Africa  Western Mande  Niger-Congo  False  False
nez  nezp1238  Nez Perce  46.0  -116.0  North America  Sahaptian  Penutian  False  True
dad  dadi1250  Dadibi  -6.55  144.583333333  Papunesia  Teberan  Teberan-Pawaian  False  False
hoa  hoav1238  Hoava  -8.08333333333  157.5  Papunesia  Oceanic  Austronesian  False  False
ckh  chek1238  Cheke Holo  -8.33333333333  159.666666667  Papunesia  Oceanic  Austronesian  False  False
kie  kire1240  Kire  -4.25  144.75  Papunesia  Mikarew  Lower Sepik-Ramu  False  False
nju  nyun1247  Nyungar  -33.75  122.0  Australia  Pama-Nyungan  Australian  False  False
awd  awad1243  Awadhi  27.5  81.5  Eurasia  Indic  Indo-European  False  False
kef  kafa1242  Kefa  7.25  36.25  Africa  South Omotic  Afro-Asiatic  False  False
kow  winy1241  Ko (Winye)  11.8666666667  -2.91666666667  Africa  Gur  Niger-Congo  False  False
omh  omah1247  Omaha  42.0  -97.25  North America  Siouan  Siouan  False  False
tob  toba1269  Toba  -26.5  -59.0  South America  Guaicuruan  Guaicuruan  False  False
shr  shor1247  Shor  53.0  88.0  Eurasia  Turkic  Altaic  False  False
krz  kryt1240  Kryz  41.0833333333  48.0  Eurasia  Lezgic  Nakh-Daghestanian  False  False
bol  boli1255  Bolia  -1.25  18.3333333333  Africa  Bantoid  Niger-Congo  False  False
nto  ntom1248  Ntomba  -2.0  18.3333333333  Africa  Bantoid  Niger-Congo  False  False
abn  arab1267  Arabana  -28.25  136.25  Australia  Pama-Nyungan  Australian  False  False
lok  loko1255  Loko  9.33333333333  -12.0833333333  Africa  Western Mande  Niger-Congo  False  False
mug  barg1252  Mugil  -4.88333333333  145.75  Papunesia  Madang  Trans-New Guinea  False  False
edo  edol1239  Edolo  -6.16666666667  142.666666667  Papunesia  Bosavi  Bosavi  False  False
tll  taul1251  Taulil  -4.41666666667  152.083333333  Papunesia  Taulil  Baining-Taulil  False  False
koe  kweg1241  Koegu  7.0  36.0833333333  Africa  Surmic  Nilo-Saharan  False  False
jab  yabe1254  Jabêm  -6.58333333333  147.783333333  Papunesia  Oceanic  Austronesian  False  False
ath  athp1241  Athpare  27.0  87.3333333333  Eurasia  Mahakiranti  Sino-Tibetan  False  False
kwe  west2635  Kanjobal (Western)  15.8333333333  -91.8333333333  North America  Mayan  Mayan  False  False
kea  qanj1241  Kanjobal (Eastern)  15.3333333333  -91.6666666667  North America  Mayan  Mayan  False  False
grw  kala1399  Greenlandic (West)  64.0  -51.0  Eurasia  Eskimo  Eskimo-Aleut  True  True
gre  kala1399  Greenlandic (East)  65.0  -40.0  Eurasia  Eskimo  Eskimo-Aleut  False  False
gso  kala1399  Greenlandic (South)  60.0  -44.0  Eurasia  Eskimo  Eskimo-Aleut  False  False
ylm  yelm1242  Yelmek  -7.66666666667  139.166666667  Papunesia  Bulaka River  Bulaka River  False  False
alk  arop1243  Arop-Lokep  -5.38333333333  147.05  Papunesia  Oceanic  Austronesian  False  False
pms  paam1238  Paamese  -16.5  168.25  Papunesia  Oceanic  Austronesian  False  True
gue  guer1240  Guere  6.66666666667  -7.75  Africa  Kru  Niger-Congo  False  False
mkd  mako1251  Makonde  -11.0  40.0  Africa  Bantoid  Niger-Congo  False  False
tig  tigr1271  Tigrinya  14.5  38.5  Africa  Semitic  Afro-Asiatic  False  False
eja  ejag1239  Ejagham  5.41666666667  8.66666666667  Africa  Bantoid  Niger-Congo  False  False
sre  koho1244  Sre  11.5  108.0  Eurasia  Bahnaric  Austro-Asiatic  False  False
noc  noct1238  Nocte  27.0  95.5  Eurasia  Northern Naga  Sino-Tibetan  False  False
mof  mofu1248  Mofu-Gudur  10.5  14.0  Africa  Biu-Mandara  Afro-Asiatic  False  False
adz  adze1240  Adzera  -6.25  146.25  Papunesia  Oceanic  Austronesian  False  False
bac  wadj1254  Bachamal  -13.1666666667  130.166666667  Australia  Anson Bay  Australian  False  False
trc  chic1273  Trique (Chicahuaxtla)  17.1666666667  -97.8333333333  North America  Mixtecan  Oto-Manguean  False  False
tri  copa1237  Trique (Copala)  17.1666666667  -97.9166666667  North America  Mixtecan  Oto-Manguean  False  False
spc  stan1288  Spanish (Canary Islands)  28.0  -15.5833333333  Eurasia  Romance  Indo-European  False  False
ast  astu1245  Asturian  43.25  -6.0  Eurasia  Romance  Indo-European  False  False
spa  stan1288  Spanish  40.0  -4.0  Eurasia  Romance  Indo-European  True  True
gag  gaga1249  Gagauz  46.3333333333  28.6666666667  Eurasia  Turkic  Altaic  False  False
kar  kara1482  Kara (in Central African Republic)  10.0  23.0  Africa  Bongo-Bagirmi  Nilo-Saharan  False  False
kra  kara1486  Kara (in Papua New Guinea)  -2.83333333333  151.116666667  Papunesia  Oceanic  Austronesian  False  False
kmn  kuma1280  Kuman  -5.91666666667  145.0  Papunesia  Chimbu  Trans-New Guinea  False  False
gln  goli1247  Golin  -6.33333333333  144.75  Papunesia  Chimbu  Trans-New Guinea  False  False
tba  sina1271  Tabare  -6.08333333333  145.0  Papunesia  Chimbu  Trans-New Guinea  False  False
zan  zand1248  Zande  4.0  26.0  Africa  Ubangi  Niger-Congo  False  False
bud  budu1265  Buduma  13.5  14.5  Africa  Biu-Mandara  Afro-Asiatic  False  False
shw  shaw1249  Shawnee  40.0  -83.0  North America  Algonquian  Algic  False  False
itw  itaw1240  Itawis  17.75  121.5  Papunesia  Northern Luzon  Austronesian  False  False
wwy  wara1300  Waray-Waray  12.0  125.0  Papunesia  Greater Central Philippine  Austronesian  False  False
mai  mait1250  Maithili  26.0  86.0  Eurasia  Indic  Indo-European  False  False
dym  djim1235  Dyimini  8.41666666667  -4.41666666667  Africa  Gur  Niger-Congo  False  False
sab  saba1265  Sa'ban  3.66666666667  115.666666667  Papunesia  North Borneo  Austronesian  False  False
tua  tuam1242  Tuamotuan  -17.0  -144.0  Papunesia  Oceanic  Austronesian  False  False
tem  temm1241  Tem  8.66666666667  0.5  Africa  Gur  Niger-Congo  False  False
hnd  hund1239  Hunde  -1.16666666667  28.8333333333  Africa  Bantoid  Niger-Congo  False  False
pur  pure1242  Purépecha  19.5  -101.666666667  North America  Tarascan  Tarascan  False  False
zaz  diml1238  Zazaki  39.0  41.0  Eurasia  Iranian  Indo-European  False  False
yrt  yuru1263  Yuruti  1.0  -70.4166666667  South America  Tucanoan  Tucanoan  False  False
mlm  mlab1235  Mlabri (Minor)  18.5  101.0  Eurasia  Palaung-Khmuic  Austro-Asiatic  False  False
drm  darm1243  Darma  30.0  79.75  Eurasia  Bodic  Sino-Tibetan  False  False
ene  enet1250  Enets  67.5  86.5  Eurasia  Samoyedic  Uralic  False  False
kos  kosr1238  Kosraean  5.3  163.0  Papunesia  Oceanic  Austronesian  False  False
kta  koit1244  Koita  -9.33333333333  147.083333333  Papunesia  Koiarian  Trans-New Guinea  False  False
nai  nana1257  Nanai  49.5  137.0  Eurasia  Tungusic  Altaic  False  False
mgi  mail1248  Magi  -10.3333333333  149.333333333  Papunesia  Mailuan  Trans-New Guinea  False  False
gpz  swis1247  German (Appenzell)  47.3333333333  9.33333333333  Eurasia  Germanic  Indo-European  False  False
gba  bava1246  German (Bavarian)  49.0  11.5  Eurasia  Germanic  Indo-European  False  False
gbl  stan1295  German (Berlin)  52.5  13.3333333333  Eurasia  Germanic  Indo-European  False  False
gbe  swis1247  German (Bern)  47.0  7.41666666667  Eurasia  Germanic  Indo-European  False  False
gha  stan1295  German (Hannover)  52.4166666667  9.66666666667  Eurasia  Germanic  Indo-European  False  False
gma  stan1295  German (Mansfeldisch)  51.5833333333  11.5  Eurasia  Germanic  Indo-European  False  False
gos  swis1247  German (Ostschweiz)  47.4166666667  9.25  Eurasia  Germanic  Indo-European  False  False
grp  kols1241  German (Ripuarian)  51.0  7.0  Eurasia  Germanic  Indo-European  False  False
gth  stan1295  German (Thuringian)  51.0  11.0  Eurasia  Germanic  Indo-European  False  False
gti  stan1295  German (Timisoara)  45.75  21.25  Eurasia  Germanic  Indo-European  False  False
gau  bava1246  German (Upper Austrian)  47.0  14.0  Eurasia  Germanic  Indo-European  False  False
gwe  west2356  German (Westphalian)  52.0  7.5  Eurasia  Germanic  Indo-European  False  False
gzu  swis1247  German (Zurich)  47.4166666667  8.5  Eurasia  Germanic  Indo-European  False  False
gvi  bava1246  German (Viennese)  48.1666666667  16.3333333333  Eurasia  Germanic  Indo-European  False  False
gtg  swis1247  German (Thurgau)  47.5833333333  9.16666666667  Eurasia  Germanic  Indo-European  False  False
ger  stan1295  German  52.0  10.0  Eurasia  Germanic  Indo-European  True  True
mee  meen1242  Me'en  5.0  37.0  Africa  Surmic  Nilo-Saharan  False  False
cvc  chav1241  Chavacano  7.0  122.083333333  Papunesia  Creoles and Pidgins  other  False  False
pui  puin1248  Puinave  4.0  -68.0  South America  Puinave  Puinave  False  False
leb  ngel1238  Lebeo  1.75  25.0  Africa  Bantoid  Niger-Congo  False  False
tun  tuni1252  Tunica  32.6666666667  -91.0  North America  Tunica  Tunica  False  True
ktn  kete1254  Ketengban  -4.5  140.5  Papunesia  Mek  Trans-New Guinea  False  False
knq  krio1252  Kriol (Ngukurr)  -14.8333333333  135.0  Australia  Creoles and Pidgins  other  False  False
sml  seme1247  Semelai  3.0  103.0  Eurasia  Aslian  Austro-Asiatic  False  True
nyi  amas1236  Nyimang  12.1666666667  29.3333333333  Africa  Nyimang  Nilo-Saharan  False  False
nag  yale1246  Nagatman  -3.75  141.5  Papunesia  Yale  Yale  False  False
deu  deor1238  Deuri  26.0  90.25  Eurasia  Bodo-Garo  Sino-Tibetan  False  False
per  pero1241  Pero  9.58333333333  11.0  Africa  West Chadic  Afro-Asiatic  False  False
mul  mula1253  Mulao  25.0  108.0  Eurasia  Kam-Tai  Tai-Kadai  False  False
kky  kank1243  Kankanay  16.75  120.583333333  Papunesia  Northern Luzon  Austronesian  False  False
mbo  nucl1458  Monumbo  -4.25  145.0  Papunesia  Monumbo  Monumbo  False  False
chu  niva1238  Chulupí  -23.5  -60.5  South America  Matacoan  Matacoan  False  False
myn  maan1238  Ma'anyan  -2.0  115.0  Papunesia  Barito  Austronesian  False  False
kna  kari1311  Karitiâna  -9.5  -64.0  South America  Arikem  Tupian  False  False
snd  ceba1235  Senadi  9.5  -6.25  Africa  Gur  Niger-Congo  False  False
liv  livv1244  Liv  56.8333333333  24.0  Eurasia  Finnic  Uralic  False  False
cak  kaqc1274  Cakchiquel  14.5  -91.0  North America  Mayan  Mayan  False  False
krj  kara1476  Karadjeri  -19.0  122.0  Australia  Pama-Nyungan  Australian  False  False
chs  siyi1240  Chin (Siyin)  23.8333333333  94.0  Eurasia  Kuki-Chin  Sino-Tibetan  False  False
rnn  renn1242  Rennellese  -11.6166666667  160.25  Papunesia  Oceanic  Austronesian  False  False
mii  tama1331  Miisiirii  13.5  22.0  Africa  Taman  Nilo-Saharan  False  False
tma  tama1331  Tama  14.5  22.0  Africa  Taman  Nilo-Saharan  False  False
ace  achi1257  Acehnese  5.5  95.5  Eurasia  Malayo-Sumbawan  Austronesian  False  False
ifm  teke1274  Ifumu  -3.66666666667  15.3333333333  Africa  Bantoid  Niger-Congo  False  False
akn  akan1250  Akan  6.5  -1.25  Africa  Kwa  Niger-Congo  False  False
wah  wahg1249  Wahgi  -5.83333333333  144.716666667  Papunesia  Chimbu  Trans-New Guinea  False  False
hmo  huam1250  Hmong Njua  28.0  105.0  Eurasia  Hmong-Mien  Hmong-Mien  True  True
hmd  hmon1333  Hmong Daw  26.0  105.0  Eurasia  Hmong-Mien  Hmong-Mien  False  False
gel  gela1263  Gela  -9.08333333333  160.25  Papunesia  Oceanic  Austronesian  False  False
mll  mola1238  Molala  44.5  -122.5  North America  Molala  Penutian  False  False
pap  papi1253  Papiamentu  12.25  -69.0  North America  Creoles and Pidgins  other  False  False
aro  aros1241  Arosi  -10.25  161.333333333  Papunesia  Oceanic  Austronesian  False  False
ham  hamt1247  Hamtai  -7.5  146.25  Papunesia  Angan  Trans-New Guinea  False  True
pla  play1240  Playero  7.0  -71.0  South America  Guahiban  Guahiban  False  False
nnc  cent1990  Nancowry  8.05  93.5  Eurasia  Nicobarese  Austro-Asiatic  False  False
nca  carn1240  Nicobarese (Car)  9.0  93.0  Eurasia  Nicobarese  Austro-Asiatic  False  False
nic  cent1990  Nicobarese  7.0  93.8333333333  Eurasia  Nicobarese  Austro-Asiatic  False  False
kol  kola1242  Kolami  20.0  78.5  Eurasia  Central Dravidian  Dravidian  False  False
ptp  patp1243  Patpatar  -3.76666666667  152.5  Papunesia  Oceanic  Austronesian  False  False
bry  baru1267  Baruya  -6.91666666667  145.916666667  Papunesia  Angan  Trans-New Guinea  False  False
rit  rita1239  Ritharngu  -12.8333333333  135.5  Australia  Pama-Nyungan  Australian  False  False
axv  akhv1239  Akhvakh  42.3333333333  46.3333333333  Eurasia  Avar-Andic-Tsezic  Nakh-Daghestanian  False  False
vie  viet1252  Vietnamese  10.5  106.5  Eurasia  Viet-Muong  Austro-Asiatic  True  True
kng  kain1272  Kaingang  -26.0  -52.0  South America  Ge-Kaingang  Macro-Ge  False  False
una  unaa1239  Una  -4.66666666667  140.0  Papunesia  Mek  Trans-New Guinea  False  True
mrl  murl1244  Murle  6.5  33.5  Africa  Surmic  Nilo-Saharan  False  True
pte  pait1244  Paite  24.0  93.1666666667  Eurasia  Kuki-Chin  Sino-Tibetan  False  False
nbb  bign1238  Nambas (Big)  -16.0833333333  167.2  Papunesia  Oceanic  Austronesian  False  False
ann  anin1240  Anindilyakwa  -14.0  136.5  Australia  Anindilyakwa  Australian  False  False
khm  cent1989  Khmer  12.5  105.0  Eurasia  Khmer  Austro-Asiatic  False  True
ytu  nort2745  Yukaghir (Tundra)  69.0  155.0  Eurasia  Yukaghir  Yukaghir  False  False
yko  sout2750  Yukaghir (Kolyma)  65.75  150.833333333  Eurasia  Yukaghir  Yukaghir  False  True
hve  sanm1287  Huave (San Mateo del Mar)  16.2166666667  -95.0  North America  Huavean  Huavean  False  False
mne  nort2952  Maidu (Northeast)  40.0  -120.666666667  North America  Maiduan  Penutian  False  False
was  wash1253  Washo  39.25  -120.0  North America  Washo  Washo  False  False
kul  gamo1244  Kullo  6.75  37.0833333333  Africa  North Omotic  Afro-Asiatic  False  False
gam  gamo1244  Gamo  6.66666666667  37.25  Africa  North Omotic  Afro-Asiatic  False  False
wly  wola1242  Wolaytta  6.83333333333  37.75  Africa  North Omotic  Afro-Asiatic  False  False
pkt  poko1263  Pokot  1.5  35.5  Africa  Nilotic  Nilo-Saharan  False  False
itn  neap1235  Italian (Napolitanian)  40.9166666667  14.25  Eurasia  Romance  Indo-European  False  False
itu  piem1238  Italian (Turinese)  45.0  7.66666666667  Eurasia  Romance  Indo-European  False  False
ifi  ital1282  Italian (Fiorentino)  43.75  11.25  Eurasia  Romance  Indo-European  False  False
itb  emil1242  Italian (Bologna)  44.5  11.3333333333  Eurasia  Romance  Indo-European  False  False
itg  ligu1248  Italian (Genoa)  44.4166666667  8.95  Eurasia  Romance  Indo-European  False  False
ita  ital1282  Italian  43.0  12.0  Eurasia  Romance  Indo-European  False  False
tno  tond1251  Tondano  1.25  125.0  Papunesia  Minahasan  Austronesian  False  False
lak  lakk1252  Lak  42.1666666667  47.1666666667  Eurasia  Lak-Dargwa  Nakh-Daghestanian  False  True
amc  amah1246  Amahuaca  -10.5  -72.5  South America  Panoan  Panoan  False  False
yyo  yort1237  Yorta Yorta  -36.0  146.0  Australia  Pama-Nyungan  Australian  False  False
rti  term1237  Roti  -10.6666666667  123.25  Papunesia  Central Malayo-Polynesian  Austronesian  False  False
tpc  tepe1278  Tepecano  21.75  -104.75  North America  Tepiman  Uto-Aztecan  False  False
cuc  timo1237  Cuica  9.0  -70.5  South America  Timote-Cuica  Timote-Cuica  False  False
gto  guat1253  Guató  -17.0  -58.0  South America  Guató  Macro-Ge  False  False
ket  kett1243  Ket  64.0  87.0  Eurasia  Yeniseian  Yeniseian  False  True
bgg  bang1368  Banggai  -1.41666666667  123.166666667  Papunesia  Celebic  Austronesian  False  False
dah  daha1245  Dahalo  -2.33333333333  40.5  Africa  Southern Cushitic  Afro-Asiatic  False  False
mbm  mbum1254  Mbum  7.75  13.1666666667  Africa  Adamawa  Niger-Congo  False  False
gfr  guia1246  Guianese French Creole  5.0  -53.0  South America  Creoles and Pidgins  other  False  False
sey  sese1246  Seychelles Creole  -4.75  55.5  Eurasia  Creoles and Pidgins  other  False  False
lcr  guad1242  Lesser Antillean French Creole  15.0  -61.1666666667  North America  Creoles and Pidgins  other  False  False
mqc  guad1242  Martinique Creole  14.6666666667  -61.0  North America  Creoles and Pidgins  other  False  False
urd  urdu1245  Urdu  25.0  67.0  Eurasia  Indic  Indo-European  False  False
nyk  tukp1239  Nyamkad  32.0  78.5  Eurasia  Bodic  Sino-Tibetan  False  False
bjs  sout2918  Bajau (Semporna)  4.5  118.5  Papunesia  Sama-Bajaw  Austronesian  False  False
orm  ormu1247  Ormuri  32.5  69.75  Eurasia  Iranian  Indo-European  False  False
ptt  patt1248  Pattani  32.75  76.75  Eurasia  Bodic  Sino-Tibetan  False  False
sle  samb1305  Samba Leko  8.5  12.5  Africa  Adamawa  Niger-Congo  False  False
mca  maca1260  Maca  -25.0  -57.5  South America  Matacoan  Matacoan  False  False
hem  hemb1242  Hemba  -6.25  27.1666666667  Africa  Bantoid  Niger-Congo  False  False
mjk  mand1419  Manjaku  12.0  -16.25  Africa  Northern Atlantic  Niger-Congo  False  False
chj  chuj1249  Chuj  15.9166666667  -91.5833333333  North America  Mayan  Mayan  False  False
fef  fefe1239  Fe'fe'  5.25  10.1666666667  Africa  Bantoid  Niger-Congo  False  False
wrp  waro1242  Waropen  -2.33333333333  136.583333333  Papunesia  South Halmahera - West New Guinea  Austronesian  False  False
abw  west2630  Abenaki (Western)  44.0  -72.25  North America  Algonquian  Algic  False  False
ldu  lend1245  Lendu  2.0  30.5  Africa  Lendu  Nilo-Saharan  False  False
nti  ngit1239  Ngiti  1.33333333333  30.25  Africa  Lendu  Nilo-Saharan  False  True
ido  idom1241  Idoma  6.91666666667  7.5  Africa  Idomoid  Niger-Congo  False  False
uli  ulit1238  Ulithian  9.91666666667  139.583333333  Papunesia  Oceanic  Austronesian  False  False
hba  hebr1245  Hebrew (Modern Ashkenazic)  31.75  35.1666666667  Eurasia  Semitic  Afro-Asiatic  False  False
heb  hebr1245  Hebrew (Modern)  31.5  34.8333333333  Eurasia  Semitic  Afro-Asiatic  True  True
mlk  mull1237  Malakmalak  -13.4166666667  130.416666667  Australia  Northern Daly  Australian  False  False
rad  rade1240  Rade  13.0  108.5  Eurasia  Malayo-Sumbawan  Austronesian  False  False
leg  lega1249  Lega  -2.83333333333  27.1666666667  Africa  Bantoid  Niger-Congo  False  False
kmh  gama1251  Kham  28.5  82.75  Eurasia  Mahakiranti  Sino-Tibetan  False  False
ixc  ixca1245  Ixcatec  17.8333333333  -97.1666666667  North America  Popolocan  Oto-Manguean  False  False
ykn  yaka1277  Yakan  6.5  122.0  Papunesia  Sama-Bajaw  Austronesian  False  False
ape  safe1240  Ampeeli  -6.75  146.083333333  Papunesia  Angan  Trans-New Guinea  False  False
pkn  darl1243  Paakantyi  -32.5  142.5  Australia  Pama-Nyungan  Australian  False  False
mdg  mund1325  Mundang  9.66666666667  14.5  Africa  Adamawa  Niger-Congo  False  False
klq  kala1397  Kalam  -5.25  144.583333333  Papunesia  Madang  Trans-New Guinea  False  False
srn  siri1273  Sirionó  -15.5833333333  -64.0  South America  Tupi-Guaraní  Tupian  False  False
thn  than1259  Thangmi  27.75  86.0  Eurasia  Mahakiranti  Sino-Tibetan  False  False
kwk  kwak1269  Kwakw'ala  51.0  -127.0  North America  Northern Wakashan  Wakashan  False  False
dbr  dutc1256  Dutch (Brabantic)  50.75  4.5  Eurasia  Germanic  Indo-European  False  False
dli  dutc1256  Dutch (Limburg)  51.0  5.5  Eurasia  Germanic  Indo-European  False  False
duz  zeeu1238  Dutch (Zeeuws)  51.5  3.75  Eurasia  Germanic  Indo-European  False  False
dut  dutc1256  Dutch  52.5  6.0  Eurasia  Germanic  Indo-European  False  False
cpa  ashe1273  Campa Pajonal Asheninca  -10.6666666667  -74.25  South America  Pre-Andine Arawakan  Arawakan  False  False
abd  abid1235  Abidji  5.66666666667  -4.58333333333  Africa  Kwa  Niger-Congo  False  False
vot  voti1245  Votic  59.5  30.0  Eurasia  Finnic  Uralic  False  False
beb  bena1264  Benabena  -6.16666666667  145.5  Papunesia  Eastern Highlands  Trans-New Guinea  False  False
men  meno1252  Menomini  45.5  -88.3333333333  North America  Algonquian  Algic  False  False
dre  dehu1237  Drehu  -21.0  167.25  Papunesia  Oceanic  Austronesian  False  True
mog  mogh1245  Moghol  35.0  62.0  Eurasia  Mongolic  Altaic  False  False
kuo  kuot1243  Kuot  -3.05  151.5  Papunesia  Kuot  Kuot  False  False
gad  gade1242  Gade  8.66666666667  7.41666666667  Africa  Nupoid  Niger-Congo  False  False
ese  esee1248  Ese Ejja  -11.0  -66.0  South America  Tacanan  Tacanan  False  False
iql  east2534  Inuktitut (Quebec-Labrador)  62.0  -73.0  North America  Eskimo  Eskimo-Aleut  False  False
ins  east2534  Inuktitut (Salluit)  62.0  -76.0  North America  Eskimo  Eskimo-Aleut  False  False
kpa  kpan1246  Kpan  7.58333333333  10.1666666667  Africa  Platoid  Niger-Congo  False  False
cml  caml1239  Camling  27.0  86.6666666667  Eurasia  Mahakiranti  Sino-Tibetan  False  False
mgk  mung1266  Mungaka  5.91666666667  10.0  Africa  Bantoid  Niger-Congo  False  False
mnu  kimm1245  Mun  19.0  110.0  Eurasia  Hmong-Mien  Hmong-Mien  False  False
mie  iumi1238  Mien  25.0  111.0  Eurasia  Hmong-Mien  Hmong-Mien  False  False
xav  xava1240  Xavánte  -15.0  -52.5  South America  Ge-Kaingang  Macro-Ge  False  False
nyu  nyul1247  Nyulnyul  -17.0  122.833333333  Australia  Nyulnyulan  Australian  False  False
kbr  bara1370  Kayan (Baram)  3.5  114.5  Papunesia  North Borneo  Austronesian  False  False
sap  sapu1248  Sapuan  15.1666666667  106.833333333  Eurasia  Bahnaric  Austro-Asiatic  False  False
yem  yemb1246  Yemba  5.41666666667  10.0833333333  Africa  Bantoid  Niger-Congo  False  False
cmk  chim1310  Chemakum  48.0833333333  -122.916666667  North America  Chimakuan  Chimakuan  False  False
klt  kela1258  Kelabit  3.66666666667  115.416666667  Papunesia  North Borneo  Austronesian  False  False
wlf  nucl1347  Wolof  15.25  -16.0  Africa  Northern Atlantic  Niger-Congo  False  False
gim  benc1235  Gimira  7.0  35.75  Africa  North Omotic  Afro-Asiatic  False  False
nom  noma1263  Nomatsiguenga  -11.6666666667  -74.5  South America  Pre-Andine Arawakan  Arawakan  False  False
ulc  ulch1241  Ulcha  52.25  140.333333333  Eurasia  Tungusic  Altaic  False  False
kin  kiny1244  Kinyarwanda  -2.0  30.0  Africa  Bantoid  Niger-Congo  False  False
ara  araw1276  Arawak  5.5  -55.1666666667  South America  Northern Arawakan  Arawakan  False  False
jiv  shua1257  Jivaro  -2.5  -78.0  South America  Jivaroan  Jivaroan  False  False
mui  muin1242  Muinane  -1.0  -72.5  South America  Boran  Huitotoan  False  False
orh  east2652  Oromo (Harar)  9.0  42.0  Africa  Eastern Cushitic  Afro-Asiatic  True  True
orw  waat1238  Oromo (Waata)  -3.33333333333  39.8333333333  Africa  Eastern Cushitic  Afro-Asiatic  False  False
orb  bora1271  Oromo (Boraana)  4.5  38.5  Africa  Eastern Cushitic  Afro-Asiatic  False  False
owc  west2721  Oromo (West-Central)  9.0  37.0  Africa  Eastern Cushitic  Afro-Asiatic  False  False
aeg  egyp1253  Arabic (Egyptian)  30.0  31.0  Africa  Semitic  Afro-Asiatic  True  True
arg  gulf1241  Arabic (Gulf)  26.0  49.0  Eurasia  Semitic  Afro-Asiatic  False  False
arq  meso1252  Arabic (Iraqi)  33.0  44.0  Eurasia  Semitic  Afro-Asiatic  False  False
arl  nort3139  Arabic (Lebanese)  34.0  36.0  Eurasia  Semitic  Afro-Asiatic  False  False
ako  cypr1248  Arabic (Kormakiti)  35.25  33.5  Eurasia  Semitic  Afro-Asiatic  False  False
ars  sana1295  Arabic (San'ani)  16.0  44.0  Eurasia  Semitic  Afro-Asiatic  False  False
abh  baha1259  Arabic (Bahrain)  26.0  50.5  Eurasia  Semitic  Afro-Asiatic  False  False
apa  sout3123  Arabic (Palestinian)  32.0  35.25  Eurasia  Semitic  Afro-Asiatic  False  False
arh  hija1235  Arabic (Hijazi)  26.0  38.0  Eurasia  Semitic  Afro-Asiatic  False  False
arv  sout3123  Arabic (Negev)  30.5  34.75  Eurasia  Semitic  Afro-Asiatic  False  False
asy  nort3139  Arabic (Syrian)  34.0  38.0  Eurasia  Semitic  Afro-Asiatic  False  False
abe  nort3139  Arabic (Beirut)  33.9166666667  35.5  Eurasia  Semitic  Afro-Asiatic  False  False
anl  nort3139  Arabic (North Levantine Spoken)  33.75  36.0  Eurasia  Semitic  Afro-Asiatic  False  False
blg  bala1310  Balangao  17.1666666667  121.166666667  Papunesia  Northern Luzon  Austronesian  False  False
ynm  yano1262  Yanomámi  2.33333333333  -63.0  South America  Yanomam  Yanomam  False  False
eka  ekar1243  Ekari  -3.83333333333  135.5  Papunesia  Wissel Lakes-Kemandoga  Trans-New Guinea  False  True
gho  ghot1243  Ghotuo  7.08333333333  5.75  Africa  Edoid  Niger-Congo  False  False
xun  kung1261  !Xun (Ekoka)  -19.6666666667  18.0  Africa  Northern Khoisan  Khoisan  False  False
bmn  bamu1253  Bamun  5.5  10.9166666667  Africa  Bantoid  Niger-Congo  False  False
iha  ihaa1241  Iha  -2.91666666667  132.25  Papunesia  West Bomberai  West Bomberai  False  False
eno  engg1245  Enggano  -5.41666666667  102.25  Papunesia  Enggano  Austronesian  False  False
lew  lewo1242  Lewo  -16.75  168.333333333  Papunesia  Oceanic  Austronesian  False  False
mch  mach1267  Machiguenga  -12.0  -72.6666666667  South America  Pre-Andine Arawakan  Arawakan  False  False
mbg  mbug1240  Mbugu  -4.33333333333  38.1666666667  Africa  Southern Cushitic  Afro-Asiatic  False  False
foe  foii1241  Foe  -6.5  143.5  Papunesia  Kutubuan  Trans-New Guinea  False  False
au  auuu1241  Au  -3.58333333333  142.083333333  Papunesia  Wapei-Palei  Torricelli  False  False
ala  alam1246  Alamblak  -4.66666666667  143.333333333  Papunesia  Sepik Hill  Sepik  True  True
dnw  dang1274  Dangaléat (Western)  12.1666666667  18.3333333333  Africa  East Chadic  Afro-Asiatic  False  False
tbo  tbol1240  Tboli  6.16666666667  124.5  Papunesia  Bilic  Austronesian  False  False
ydl  east2295  Yiddish (Lodz)  51.75  19.4166666667  Eurasia  Germanic  Indo-European  False  False
ydb  east2295  Yiddish (Bessarabian)  47.0  28.5  Eurasia  Germanic  Indo-European  False  False
ylt  east2295  Yiddish (Lithuanian)  55.0  25.0  Eurasia  Germanic  Indo-European  False  False
ydd  yidd1255  Yiddish  52.0  23.0  Eurasia  Germanic  Indo-European  False  False
lud  lund1271  Lun Dayeh  4.0  115.916666667  Papunesia  North Borneo  Austronesian  False  False
csh  cash1254  Cashinahua  -10.5  -71.8333333333  South America  Panoan  Panoan  False  False
gbc  uppe1455  Guinea Bissau Crioulo  12.0  -15.0  Africa  Creoles and Pidgins  other  False  False
kao  kara1487  Karao  16.5  120.833333333  Papunesia  Northern Luzon  Austronesian  False  False
mus  muss1246  Mussau  -1.45  149.616666667  Papunesia  Oceanic  Austronesian  False  False
lum  stra1244  Lummi  48.7  -122.666666667  North America  Central Salish  Salishan  False  False
sch  stra1244  Saanich  48.5833333333  -123.416666667  North America  Central Salish  Salishan  False  False
soo  stra1244  Sooke  48.3333333333  -123.75  North America  Central Salish  Salishan  False  False
sgs  stra1244  Songish  48.45  -123.333333333  North America  Central Salish  Salishan  False  False
sss  stra1244  Salish (Samish Straits)  48.5833333333  -122.583333333  North America  Central Salish  Salishan  False  False
sst  stra1244  Salish (Straits)  48.75  -123.25  North America  Central Salish  Salishan  False  False
pmc  cent2138  Pomo (Central)  39.0  -123.333333333  North America  Pomoan  Hokan  False  False
yao  yaoo1241  Yao (in Malawi)  -14.5  35.5  Africa  Bantoid  Niger-Congo  False  False
oto  iowa1245  Oto  40.5  -96.0  North America  Siouan  Siouan  False  False
crl  caro1242  Carolinian  15.2  145.75  Papunesia  Oceanic  Austronesian  False  False
pul  pulu1242  Puluwat  7.33333333333  149.333333333  Papunesia  Oceanic  Austronesian  False  False
bab  veng1238  Babungo  6.11666666667  10.4166666667  Africa  Bantoid  Niger-Congo  False  False
ibn  iban1267  Ibanag  17.5  121.666666667  Papunesia  Northern Luzon  Austronesian  False  False
kty  khan1273  Khanty  65.0  65.0  Eurasia  Ugric  Uralic  False  False
anu  anuf1239  Anufo  10.0833333333  0.25  Africa  Kwa  Niger-Congo  False  False
eve  even1259  Evenki  56.0  125.0  Eurasia  Tungusic  Altaic  False  True
bln  bili1260  Bilin  15.75  38.5  Africa  Central Cushitic  Afro-Asiatic  False  False
acg  acha1250  Achagua  4.41666666667  -72.25  South America  Northern Arawakan  Arawakan  False  False
kmi  kami1256  Kami  -6.75  38.0  Africa  Bantoid  Niger-Congo  False  False
ito  iton1250  Itonama  -12.8333333333  -64.3333333333  South America  Itonama  Itonama  False  False
mkz  maka1304  Makaa  3.41666666667  12.25  Africa  Bantoid  Niger-Congo  False  False
mey  meny1245  Menya  -7.25  146.0  Papunesia  Angan  Trans-New Guinea  False  False
dol  dolg1241  Dolgan  71.25  98.0  Eurasia  Turkic  Altaic  False  False
brb  baat1238  Bariba  10.0  2.5  Africa  Gur  Niger-Congo  False  False
bid  bidi1241  Bidiya  11.9166666667  18.75  Africa  East Chadic  Afro-Asiatic  False  False
cmn  coma1245  Comanche  33.5  -101.5  North America  Numic  Uto-Aztecan  False  True
ngm  ngam1268  Ngambay  8.66666666667  16.0  Africa  Bongo-Bagirmi  Nilo-Saharan  False  False
txj  xico1235  Totonac (Xicotepec de Juárez)  20.4166666667  -97.8333333333  North America  Totonacan  Totonacan  False  False
tpa  papa1238  Totonac (Papantla)  20.3333333333  -97.3333333333  North America  Totonacan  Totonacan  False  False
tot  yecu1235  Totonac (Misantla)  19.9166666667  -96.9166666667  North America  Totonacan  Totonacan  False  False
tos  high1243  Totonac (Sierra)  19.9166666667  -97.4166666667  North America  Totonacan  Totonacan  False  False
hzb  hunz1247  Hunzib  42.1666666667  46.25  Eurasia  Avar-Andic-Tsezic  Nakh-Daghestanian  False  True
kth  gwic1235  Kutchin  67.0  -146.0  North America  Athapaskan  Na-Dene  False  False
rap  rapa1244  Rapanui  -27.1166666667  -109.366666667  Papunesia  Oceanic  Austronesian  True  True
tok  taro1263  Tarok  9.0  10.0833333333  Africa  Platoid  Niger-Congo  False  False
wlo  woli1241  Wolio  -5.5  122.75  Papunesia  Celebic  Austronesian  False  False
lmp  lamp1243  Lampung  -5.0  105.0  Papunesia  Lampungic  Austronesian  False  False
bra  lave1249  Brao  14.1666666667  107.5  Eurasia  Bahnaric  Austro-Asiatic  False  False
ami  amis1246  Amis  23.3333333333  121.333333333  Papunesia  Paiwanic  Austronesian  False  False
ked  keda1252  Kedang  -8.25  123.75  Papunesia  Central Malayo-Polynesian  Austronesian  False  False
tut  nort2941  Tutchone (Northern)  63.0  -137.0  North America  Athapaskan  Na-Dene  False  False
glp  dhan1270  Gaalpu  -12.6666666667  136.75  Australia  Pama-Nyungan  Australian  False  False
tte  tute1247  Tutelo  37.6666666667  -78.75  North America  Siouan  Siouan  False  False
dgr  daur1238  Dagur  48.0  124.0  Eurasia  Mongolic  Altaic  False  False
mei  mani1292  Meithei  24.75  94.0  Eurasia  Kuki-Chin  Sino-Tibetan  True  True
dat  dato1239  Datooga  -4.33333333333  35.3333333333  Africa  Nilotic  Nilo-Saharan  False  False
meb  beta1252  Melayu Betawi  -6.5  107.0  Papunesia  Creoles and Pidgins  other  False  False
shy  east2337  Shira Yughur  38.0  99.0  Eurasia  Mongolic  Altaic  False  False
ldo  orok1266  Londo  5.0  9.16666666667  Africa  Bantoid  Niger-Congo  False  False
gjj  guaj1255  Guajajara  -5.0  -46.0  South America  Tupi-Guaraní  Tupian  False  False
coc  coca1259  Cocama  -5.0  -74.5  South America  Tupi-Guaraní  Tupian  False  False
kmj  kara1483  Karimojong  3.0  34.1666666667  Africa  Nilotic  Nilo-Saharan  False  False
gir  gula1265  Gula Iro  10.25  19.4166666667  Africa  Adamawa  Niger-Congo  False  False
msg  misi1242  Mising  28.5  94.8333333333  Eurasia  Tani  Sino-Tibetan  False  False
hhu  hang1263  Hanga Hundi  -3.83333333333  142.916666667  Papunesia  Middle Sepik  Sepik  False  False
uku  uppe1438  Upper Kuskokwim  63.0  -157.0  North America  Athapaskan  Na-Dene  False  False
tec  tekt1235  Teco  15.4166666667  -92.0833333333  North America  Mayan  Mayan  False  False
cga  moch1256  Chaga  -3.0  37.0  Africa  Bantoid  Niger-Congo  False  False
isa  kris1246  I'saka  -2.83333333333  141.283333333  Papunesia  Krisa  Skou  False  False
ite  itel1242  Itelmen  57.0  157.5  Eurasia  Southern Chukotko-Kamchatkan  Chukotko-Kamchatkan  False  False
mwn  nort2968  Miwok (Northern Sierra)  38.3333333333  -120.666666667  North America  Miwok  Penutian  False  False
mwp  plai1259  Miwok (Plains)  38.0  -121.0  North America  Miwok  Penutian  False  False
zay  zays1235  Zayse  5.91666666667  37.3333333333  Africa  North Omotic  Afro-Asiatic  False  False
psj  sanj1285  Popoloca (San Juan Atzingo)  18.1666666667  -96.4166666667  North America  Popolocan  Oto-Manguean  False  False
pop  mezo1235  Popoloca (Metzontla)  18.1666666667  -97.5  North America  Popolocan  Oto-Manguean  False  False
psv  coyo1236  Popoloca (San Vicente Coyotepec)  18.25  -97.8333333333  North America  Popolocan  Oto-Manguean  False  False
tug  taha1241  Tuareg (Ahaggar)  23.0  6.0  Africa  Berber  Afro-Asiatic  False  False
tai  taha1241  Tuareg (Air)  19.0  9.0  Africa  Berber  Afro-Asiatic  False  False
tny  west2466  Tenyer  10.6666666667  -4.5  Africa  Gur  Niger-Congo  False  False
tap  taia1239  Taiap  -4.08333333333  144.5  Papunesia  Gapun  Gapun  False  False
cqt  chiq1248  Chiquitano  -17.5  -60.0  South America  Chiquito  Chiquito  False  False
sng  sina1266  Sinaugoro  -9.83333333333  147.833333333  Papunesia  Oceanic  Austronesian  False  False
cum  chum1261  Chumburung  7.75  0.25  Africa  Kwa  Niger-Congo  False  False
kxo  kxoe1243  Kxoe  -17.5  22.5  Africa  Central Khoisan  Khoisan  False  False
pae  paez1247  Páez  2.66666666667  -76.0  South America  Páezan  Páezan  False  False
yli  angg1239  Yali  -4.0  139.333333333  Papunesia  Dani  Trans-New Guinea  False  False
bku  mokp1239  Bakueri  4.25  9.25  Africa  Bantoid  Niger-Congo  False  False
tmi  tata1255  Tatar (Mishar)  55.5  49.0  Eurasia  Turkic  Altaic  False  False
ttb  tata1255  Tatar (Baraba)  55.3333333333  78.3333333333  Eurasia  Turkic  Altaic  False  False
jem  jeme1245  Jemez  35.8333333333  -107.0  North America  Kiowa-Tanoan  Kiowa-Tanoan  False  False
new  newa1246  Newari (Kathmandu)  27.6666666667  85.5  Eurasia  Mahakiranti  Sino-Tibetan  False  False
nwd  newa1246  Newar (Dolakha)  27.3333333333  86.0  Eurasia  Mahakiranti  Sino-Tibetan  False  False
nyg  nyan1313  Nyangi  3.41666666667  33.5833333333  Africa  Kuliak  Nilo-Saharan  False  False
ssh  boro1277  Shinassha  10.4166666667  36.1666666667  Africa  North Omotic  Afro-Asiatic  False  False
fio  koon1244  Fiote  -5.5  14.0  Africa  Bantoid  Niger-Congo  False  False
yam  yami1256  Yaminahua  -8.0  -73.0  South America  Panoan  Panoan  False  False
ski  kild1236  Saami (Kildin)  67.0  37.0  Eurasia  Saami  Uralic  False  False
zhn  guib1245  Zhuang (Northern)  24.0  108.0  Eurasia  Kam-Tai  Tai-Kadai  False  False
fij  fiji1243  Fijian  -17.8333333333  178.0  Papunesia  Oceanic  Austronesian  True  True
aco  west2632  Acoma  34.9166666667  -107.583333333  North America  Keresan  Keresan  True  True
ykp  yukp1241  Yukpa  10.1666666667  -72.75  South America  Cariban  Cariban  False  False
cpw  chip1241  Chippewa (Red Lake and Pillager)  48.0  -95.0  North America  Algonquian  Algic  False  False
mda  mada1293  Mada (in Cameroon)  10.8333333333  14.1666666667  Africa  Biu-Mandara  Afro-Asiatic  False  False
krb  gilb1244  Kiribati  1.33333333333  173.0  Papunesia  Oceanic  Austronesian  False  True
mma  nucl1706  Mandaic (Modern)  31.0  48.5  Eurasia  Semitic  Afro-Asiatic  False  False
phl  pwon1235  Phlong  15.0  99.0  Eurasia  Karen  Sino-Tibetan  False  False
saw  sabu1255  Sawu  -11.5  121.916666667  Papunesia  Central Malayo-Polynesian  Austronesian  False  False
mgg  tuuu1240  Mangghuer  36.0  102.0  Eurasia  Mongolic  Altaic  False  False
grr  gara1261  Garrwa  -17.0833333333  137.166666667  Australia  Garrwan  Australian  False  False
juh  juho1239  Ju|'hoan  -19.0  21.0  Africa  Northern Khoisan  Khoisan  False  True
poa  fwai1237  Po-Ai  -20.6666666667  164.833333333  Papunesia  Oceanic  Austronesian  False  False
mut  sout2986  Mutsun  36.8333333333  -121.5  North America  Costanoan  Penutian  False  False
cof  cofa1242  Cofán  0.166666666667  -77.1666666667  South America  Cofán  Cofán  False  False
tps  sout2976  Tepehuan (Southeastern)  23.0  -104.5  North America  Tepiman  Uto-Aztecan  False  False
mlg  wand1278  Malgwa  11.5  13.75  Africa  Biu-Mandara  Afro-Asiatic  False  False
jun  juan1238  Juang  21.3333333333  86.0  Eurasia  Munda  Austro-Asiatic  False  False
yei  yeii1239  Yei  -7.91666666667  140.916666667  Papunesia  Morehead and Upper Maro Rivers  Morehead and Upper Maro Rivers  False  False
ses  sout2807  Sesotho  -28.0  27.0  Africa  Bantoid  Niger-Congo  False  False
mgd  mong1342  Mongondow  0.666666666667  124.0  Papunesia  Greater Central Philippine  Austronesian  False  False
nbd  kenu1236  Nubian (Dongolese)  18.25  30.75  Africa  Nubian  Nilo-Saharan  False  True
nku  kenu1236  Nubian (Kunuz)  23.0  33.0  Africa  Nubian  Nilo-Saharan  False  False
wch  wich1264  Wichí  -22.5  -62.5833333333  South America  Matacoan  Matacoan  True  True
die  kumi1248  Diegueño (Mesa Grande)  32.6666666667  -116.166666667  North America  Yuman  Hokan  False  False
tja  kumi1248  Tiipay (Jamul)  32.1666666667  -116.5  North America  Yuman  Hokan  False  False
sea  sout2859  Southeast Ambrym  -16.3  168.216666667  Papunesia  Oceanic  Austronesian  False  False
acu  achu1248  Achuar  -2.66667  -76.0  South America  Jivaroan  Jivaroan  False  False
sgb  mani1235  Sougb  -1.5  134.0  Papunesia  East Bird's Head  East Bird's Head  False  False
ill  miam1252  Illinois  40.0  -90.0  North America  Algonquian  Algic  False  False
maw  west2500  Maninka (Western)  13.0  -11.0  Africa  Western Mande  Niger-Congo  False  False
lga  onto1237  Luangiua  -5.33333333333  159.416666667  Papunesia  Oceanic  Austronesian  False  False
lux  luxe1241  Luxemburgeois  49.8333333333  6.16666666667  Eurasia  Germanic  Indo-European  False  False
jng  kach1280  Jingpho  25.4166666667  97.0  Eurasia  Jingpho  Sino-Tibetan  False  False
bnq  beng1286  Beng  7.83333333333  -4.25  Africa  Eastern Mande  Niger-Congo  False  False
nsg  nisg1240  Nisgha  55.0  -130.0  North America  Tsimshianic  Penutian  False  False
ano  nung1282  Anong  27.3333333333  98.75  Eurasia  Nungish  Sino-Tibetan  False  False
cax  asha1243  Campa (Axininca)  -12.0  -74.0  South America  Pre-Andine Arawakan  Arawakan  False  False
bmz  tumz1238  Berber (Mzab)  32.5  3.5  Africa  Berber  Afro-Asiatic  False  False
ifu  bata1298  Ifugao (Batad)  16.8333333333  121.083333333  Papunesia  Northern Luzon  Austronesian  False  False
cap  capa1241  Capanahua  -7.0  -74.0  South America  Panoan  Panoan  False  False
kkz  kukn1238  Kokni  20.75  73.5  Eurasia  Indic  Indo-European  False  False
cti  tedi1235  Chin (Tiddim)  23.3333333333  93.6666666667  Eurasia  Kuki-Chin  Sino-Tibetan  False  False
lu  luuu1242  Lü  22.0  100.666666667  Eurasia  Kam-Tai  Tai-Kadai  False  False
kgm  kago1247  Kagoma  9.25  8.16666666667  Africa  Platoid  Niger-Congo  False  False
gap  gapa1238  Gapapaiwa  -9.75  149.833333333  Papunesia  Oceanic  Austronesian  False  False
akw  akaw1239  Akawaio  6.0  -59.5  South America  Cariban  Cariban  False  False
nge  ngem1255  Ngemba  6.2  10.0  Africa  Bantoid  Niger-Congo  False  False
irr  irar1238  Irarutu  -3.0  133.5  Papunesia  South Halmahera - West New Guinea  Austronesian  False  False
ngo  ngon1269  Ngoni  -11.0  36.0  Africa  Bantoid  Niger-Congo  False  False
cub  cube1242  Cubeo  1.33333333333  -70.5  South America  Tucanoan  Tucanoan  False  False
gnd  gaan1243  Ga'anda  10.3333333333  12.5833333333  Africa  Biu-Mandara  Afro-Asiatic  False  False
yus  cent2128  Yupik (Siberian)  65.0  -173.0  Eurasia  Eskimo  Eskimo-Aleut  False  False
ysl  cent2128  Yupik (St. Lawrence Island)  63.5  -170.5  Eurasia  Eskimo  Eskimo-Aleut  False  False
tmn  nucl1339  Temein  11.9166666667  29.4166666667  Africa  Temein  Nilo-Saharan  False  False
lgi  lang1320  Langi  -4.5  36.0  Africa  Bantoid  Niger-Congo  False  False
tts  take1255  Tati (Southern)  36.0  49.6666666667  Eurasia  Iranian  Indo-European  False  False
bsh  bush1247  Bushoong  -4.5  21.5  Africa  Bantoid  Niger-Congo  False  False
kok  kokb1239  Kokborok  24.3333333333  92.5  Eurasia  Bodo-Garo  Sino-Tibetan  False  False
daa  daak1235  Da'a  -1.0  119.583333333  Papunesia  Celebic  Austronesian  False  False
tof  kara1462  Tofa  53.75  98.0  Eurasia  Turkic  Altaic  False  False
myi  mang1381  Mangarrayi  -14.6666666667  133.5  Australia  Mangarrayi  Australian  True  True
kha  halh1238  Khalkha  47.0  105.0  Eurasia  Mongolic  Altaic  True  True
sri  siri1274  Siriano  0.75  -70.1666666667  South America  Tucanoan  Tucanoan  False  False
wrb  warr1257  Warrnambool  -38.25  142.5  Australia  Pama-Nyungan  Australian  False  False
gun  nugu1242  Gunu  4.58333333333  11.25  Africa  Bantoid  Niger-Congo  False  False
bnw  bani1255  Baniwa  2.66666666667  -66.8333333333  South America  Northern Arawakan  Arawakan  False  False
kmt  kemt1242  Kemtuik  -2.66666666667  140.333333333  Papunesia  Nimboran  Nimboran  False  False
kaw  kaiw1246  Kaiwá  -23.0  -55.0  South America  Tupi-Guaraní  Tupian  False  False
htc  huas1256  Huastec  22.0833333333  -99.3333333333  North America  Mayan  Mayan  False  False
tks  teke1280  Teke (Southern)  -2.33333333333  14.5  Africa  Bantoid  Niger-Congo  False  False
yun  cent2127  Yup'ik (Norton Sound)  64.0  -161.0  North America  Eskimo  Eskimo-Aleut  False  False
mta  buka1257  Mentuh Tapuh  1.25  111.0  Papunesia  Land Dayak  Austronesian  False  False
yey  yeyi1239  Yeyi  -20.0  23.5  Africa  Bantoid  Niger-Congo  False  False
kik  kiku1240  Kikuyu  -0.75  36.75  Africa  Bantoid  Niger-Congo  False  False
ets  yekh1238  Etsako  7.25  6.5  Africa  Edoid  Niger-Congo  False  False
pun  wadj1254  Pungupungu  -13.5  130.416666667  Australia  Anson Bay  Australian  False  False
glc  gali1258  Galician  43.0  -8.0  Eurasia  Romance  Indo-European  False  False
dbw  dann1241  Dan (Blowo)  7.33333333333  -8.16666666667  Africa  Eastern Mande  Niger-Congo  False  False
ksp  kimm1246  Kosop  9.91666666667  15.9166666667  Africa  Adamawa  Niger-Congo  False  False
sis  baba1268  Sisiqa  -7.0  156.833333333  Papunesia  Oceanic  Austronesian  False  False
pny  pany1241  Panyjima  -22.8333333333  118.416666667  Australia  Pama-Nyungan  Australian  False  False
oca  ocai1244  Ocaina  -2.75  -71.75  South America  Huitoto  Huitotoan  False  False
ycn  yucu1253  Yucuna  -0.75  -71.0  South America  Northern Arawakan  Arawakan  False  False
son  sons1242  Sonsorol-Tobi  5.33333333333  132.25  Papunesia  Oceanic  Austronesian  False  False
ntj  ngaa1240  Ngaanyatjarra  -26.0  126.5  Australia  Pama-Nyungan  Australian  False  False
klp  kala1400  Kalapuya  44.5  -123.0  North America  Kalapuyan  Kalapuyan  False  False
zpr  zapa1253  Zaparo  -2.0  -76.3333333333  South America  Zaparoan  Zaparoan  False  False
bpa  bura1292  Bura-Pabir  10.5  12.25  Africa  Biu-Mandara  Afro-Asiatic  False  False
pok  rawo1244  Poko-Rawo  -2.83333333333  141.583333333  Papunesia  Serra Hills  Skou  False  False
bro  torr1261  Broken  -10.1666666667  143.0  Australia  Creoles and Pidgins  other  False  False
pad  pado1242  Padoe  -2.33333333333  121.333333333  Papunesia  Celebic  Austronesian  False  False
bfg  None  Berber (Figuig)  32.5  -1.5  None  Berber  Afro-Asiatic  False  False
qca  caja1238  Quechua (Cajamarca)  -7.0  -78.5  South America  Quechuan  Quechuan  False  False
xam  xamm1241  /Xam  -31.0  21.0  Africa  Southern Khoisan  Khoisan  False  False
pan  panj1256  Panjabi  31.0  74.0  Eurasia  Indic  Indo-European  False  False
bno  waim1255  Barasano (Northern)  0.333333333333  -70.25  South America  Tucanoan  Tucanoan  False  False
xer  xere1240  Xerénte  -10.0  -48.1666666667  South America  Ge-Kaingang  Macro-Ge  False  False
egn  enge1239  Engenni  5.16666666667  6.38333333333  Africa  Edoid  Niger-Congo  False  False
kap  kela1255  Kela (Apoze)  -7.41666666667  147.083333333  Papunesia  Oceanic  Austronesian  False  False
ndj  djee1236  Ndjébbana  -12.1666666667  134.116666667  Australia  Ndjébbana  Australian  False  False
brz  birr1240  Birri  5.5  25.1666666667  Africa  Bongo-Bagirmi  Nilo-Saharan  False  False
dga  sout2789  Dagaare  10.5  -2.66666666667  Africa  Gur  Niger-Congo  False  False
kyr  kark1258  Karkar-Yuri  -3.75  141.083333333  Papunesia  Karkar-Yuri  Karkar-Yuri  False  False
ktu  nucl1297  Katu  15.8333333333  107.583333333  Eurasia  Katuic  Austro-Asiatic  False  False
coo  coos1249  Coos (Hanis)  43.5  -124.166666667  North America  Coosan  Oregon Coast  False  True
mmu  nege1240  Malay (Ulu Muar)  2.66666666667  102.5  Eurasia  Malayo-Sumbawan  Austronesian  False  False
mau  maun1240  Maung  -11.9166666667  133.5  Australia  Iwaidjan  Australian  True  True
skr  sika1263  Sikaritai  -2.91666666667  138.25  Papunesia  Lakes Plain  Lakes Plain  False  False
mwa  mart1256  Martu Wangka  -21.5  126.0  Australia  Pama-Nyungan  Australian  False  False
cku  wasc1239  Chinook (Upper)  45.5  -122.5  North America  Chinookan  Penutian  False  False
kek  kekc1242  K'ekchí  16.0  -89.8333333333  North America  Mayan  Mayan  False  False
kma  kama1373  Kamaiurá  -12.0833333333  -52.5833333333  South America  Tupi-Guaraní  Tupian  False  False
nuu  noot1239  Nuuchahnulth  49.6666666667  -126.666666667  North America  Southern Wakashan  Wakashan  False  False
kyq  noot1239  Kyuquot  50.1666666667  -127.166666667  North America  Southern Wakashan  Wakashan  False  False
tgh  taha1241  Tuareg (Ghat)  25.0  10.1666666667  Africa  Berber  Afro-Asiatic  False  False
poh  pohn1238  Pohnpeian  6.88333333333  158.25  Papunesia  Oceanic  Austronesian  False  False
ijo  izon1238  Ijo (Kolokuma)  4.91666666667  5.66666666667  Africa  Ijoid  Niger-Congo  False  False
swv  swed1254  Swedish (Västerbotten)  64.25  19.75  Eurasia  Germanic  Indo-European  False  False
avt  avat1244  Avatime  6.83333333333  0.416666666667  Africa  Kwa  Niger-Congo  False  False
hum  muru1274  Huitoto (Murui)  -1.0  -73.5  South America  Huitoto  Huitotoan  False  False
wal  valm1241  Walman  -3.21666666667  142.5  Papunesia  Wapei-Palei  Torricelli  False  False
kaj  kaur1271  Kaure  -3.41666666667  140.083333333  Papunesia  Kaure  Kaure  False  False
tex  khor1269  Turkic (East-Central Xorasan)  37.0  59.0  Eurasia  Turkic  Altaic  False  False
twx  khor1269  Turkic (West Xorasan)  36.6666666667  56.0  Eurasia  Turkic  Altaic  False  False
teh  tehu1242  Tehuelche  -48.0  -68.0  South America  Chon Proper  Chon  False  False
irx  iran1263  Iranxe  -13.0  -58.0  South America  Iranxe  Iranxe  False  False
kae  kaki1249  Kaki Ae  -8.0  145.833333333  Papunesia  Tate  Eleman  False  False
uma  umaa1242  Uma  -1.83333333333  120.0  Papunesia  Celebic  Austronesian  False  False
bma  cent2194  Berber (Middle Atlas)  33.0  -5.0  Africa  Berber  Afro-Asiatic  True  True
bse  cent2194  Berber (Ayt Seghrouchen Middle Atlas)  33.3333333333  -4.66666666667  Africa  Berber  Afro-Asiatic  False  False
din  nort2815  Dinka  8.5  28.0  Africa  Nilotic  Nilo-Saharan  False  False
arb  arab1268  Arabela  -2.0  -75.1666666667  South America  Zaparoan  Zaparoan  False  False
llm  lele1264  Lelemi  7.33333333333  0.5  Africa  Kwa  Niger-Congo  False  False
lel  lele1276  Lele  9.08333333333  15.5833333333  Africa  East Chadic  Afro-Asiatic  False  False
bgv  bagv1239  Bagvalal  42.5833333333  46.1666666667  Eurasia  Avar-Andic-Tsezic  Nakh-Daghestanian  False  False
cbo  chac1251  Chácobo  -12.1666666667  -66.75  South America  Panoan  Panoan  False  False
kam  kamb1299  Kambera  -9.83333333333  120.166666667  Papunesia  Central Malayo-Polynesian  Austronesian  False  False
mhu  mbal1255  Mbalanhu  -17.5  15.0  Africa  Bantoid  Niger-Congo  False  False
hmi  mini1256  Huitoto (Minica)  -0.333333333333  -74.0  South America  Huitoto  Huitotoan  False  True
dum  vani1248  Dumo  -2.68333333333  141.3  Papunesia  Western Skou  Skou  False  False
olu  olut1240  Olutec  17.95  -95.0  North America  Mixe-Zoque  Mixe-Zoque  False  False
tke  toke1240  Tokelauan  -9.0  -172.0  Papunesia  Oceanic  Austronesian  False  False
pnu  youn1235  Punu  24.0  107.0  Eurasia  Hmong-Mien  Hmong-Mien  False  False
krd  nort2641  Kurdish (Central)  36.0  44.0  Eurasia  Iranian  Indo-European  False  False
snh  sinh1246  Sinhala  7.0  80.5  Eurasia  Indic  Indo-European  False  False
ypk  cent2127  Yup'ik (Central)  59.5  -160.0  North America  Eskimo  Eskimo-Aleut  False  True
dan  dann1241  Dan  7.5  -8.0  Africa  Eastern Mande  Niger-Congo  False  False
yuk  gang1267  Yukulta  -17.3333333333  138.833333333  Australia  Tangkic  Australian  False  False
niv  gily1242  Nivkh  53.3333333333  142.0  Eurasia  Nivkh  Nivkh  False  True
nvs  gily1242  Nivkh (South Sakhalin)  47.0  142.5  Eurasia  Nivkh  Nivkh  False  False
don  nort2735  Dong  27.0  109.0  Eurasia  Kam-Tai  Tai-Kadai  False  False
kzh  nort2735  Kam (Zhanglu)  26.0  108.5  Eurasia  Kam-Tai  Tai-Kadai  False  False
pba  pima1248  Pima Bajo  29.0  -111.0  North America  Tepiman  Uto-Aztecan  False  False
emb  nort2972  Emberá (Northern)  6.83333333333  -77.1666666667  South America  Choco  Choco  False  False
qim  imba1240  Quechua (Imbabura)  0.333333333333  -78.0  South America  Quechuan  Quechuan  True  True
wao  waor1240  Waorani  -1.0  -76.5  South America  Waorani  Waorani  False  False
gnb  kunb1251  Gunbalang  -12.0  134.0  Australia  Gunwinygic  Australian  False  False
mby  mbay1241  Mbay  8.25  17.5  Africa  Bongo-Bagirmi  Nilo-Saharan  False  False
ylb  mart1256  Yulparija  -21.0  124.0  Australia  Pama-Nyungan  Australian  False  False
nun  nung1283  Nung (in Vietnam)  21.9166666667  106.416666667  Eurasia  Kam-Tai  Tai-Kadai  False  False
brc  boru1252  Boruca  8.83333333333  -83.25  North America  Talamanca  Chibchan  False  False
tpn  nort2959  Tepehuan (Northern)  26.3333333333  -107.0  North America  Tepiman  Uto-Aztecan  False  False
gno  guan1269  Guanano  0.833333333333  -69.5  South America  Tucanoan  Tucanoan  False  False
prt  pira1254  Piratapuyo  0.333333333333  -69.5  South America  Tucanoan  Tucanoan  False  False
mrt  mart1255  Martuthunira  -20.8333333333  116.5  Australia  Pama-Nyungan  Australian  True  True
wur  waur1244  Waurá  -13.0  -53.0  South America  Central Arawakan  Arawakan  False  False
kgl  umbu1258  Umbu Ungu  -6.0  144.0  Papunesia  Chimbu  Trans-New Guinea  False  False
moc  shek1244  Moca  7.58333333333  35.5  Africa  North Omotic  Afro-Asiatic  False  False
sel  onaa1245  Selknam  -53.0  -70.0  South America  Chon Proper  Chon  False  True
epe  epen1239  Epena Pedee  3.0  -77.0  South America  Choco  Choco  False  True
jel  jeri1242  Jeli  9.5  -5.66666666667  Africa  Western Mande  Niger-Congo  False  False
hak  hakk1236  Hakka  25.0  116.0  Eurasia  Chinese  Sino-Tibetan  False  False
nnn  nort2784  Nuni (Northern)  12.1666666667  -3.0  Africa  Gur  Niger-Congo  False  False
prd  duru1236  Parji (Dravidian)  19.5  82.5  Eurasia  Central Dravidian  Dravidian  False  False
nel  kuma1276  Nelemwa  -20.25  164.083333333  Papunesia  Oceanic  Austronesian  False  False
wrw  warr1258  Warrwa  -17.5  123.5  Australia  Nyulnyulan  Australian  False  False
tal  tali1258  Talinga  0.416666666667  29.6666666667  Africa  Bantoid  Niger-Congo  False  False
yel  yele1255  Yelî Dnye  -11.3666666667  154.166666667  Papunesia  Yele  Yele  False  False
wet  luan1263  Wetan  -8.16666666667  128.0  Papunesia  Central Malayo-Polynesian  Austronesian  False  False
mzc  chiq1250  Mazatec (Chiquihuitlán)  17.75  -96.9166666667  North America  Popolocan  Oto-Manguean  False  False
mzh  huau1238  Mazatec (Huautla)  18.25  -96.8333333333  North America  Popolocan  Oto-Manguean  False  False
kto  kato1244  Kato  39.6666666667  -123.666666667  North America  Athapaskan  Na-Dene  False  False
lrk  lari1255  Larike  -3.75  127.916666667  Papunesia  Central Malayo-Polynesian  Austronesian  False  False
shm  sham1280  Shambala  -4.25  38.25  Africa  Bantoid  Niger-Congo  False  False
jug  tase1235  Jugli  27.5  96.3333333333  Eurasia  Northern Naga  Sino-Tibetan  False  False
lun  tase1235  Lungchang  27.5  96.4166666667  Eurasia  Northern Naga  Sino-Tibetan  False  False
kzy  komi1268  Komi-Zyrian  65.0  55.0  Eurasia  Permic  Uralic  False  False
yzv  komi1268  Yazva  65.0  55.0  Eurasia  Finnic  Uralic  False  False
ksi  puoc1238  Ksingmul  21.0833333333  104.0  Eurasia  Palaung-Khmuic  Austro-Asiatic  False  False
ivs  ivat1242  Ivatan (Southern)  20.3333333333  121.833333333  Papunesia  Batanic  Austronesian  False  False
qaw  qawa1238  Qawasqar  -49.0  -75.0  South America  Alacalufan  Alacalufan  False  True
wmu  wikm1247  Wik Munkan  -13.9166666667  141.75  Australia  Pama-Nyungan  Australian  False  False
aso  sout2694  Altai (Southern)  51.0  87.0  Eurasia  Turkic  Altaic  False  False
luc  luch1239  Lucazi  -14.0  20.0  Africa  Bantoid  Niger-Congo  False  False
mdm  None  Madimadi  -34.5  143.5  None  Pama-Nyungan  Australian  False  False
ess  esse1238  Esselen  36.25  -121.75  North America  Esselen  Esselen  False  False
mtb  matu1259  Matuumbi  -8.5  39.0  Africa  Bantoid  Niger-Congo  False  False
tmc  timu1245  Timucua  30.25  -82.5  North America  Timucua  Timucua  False  False
ojm  chip1241  Ojibwe (Minnesota)  47.6666666667  -92.5  North America  Algonquian  Algic  False  False
twe  lowl1265  Tarahumara (Western)  27.5  -108.0  North America  Tarahumaran  Uto-Aztecan  False  False
kun  bord1248  Kuna  8.0  -77.3333333333  South America  Kuna  Chibchan  False  False
cmr  mara1382  Chin (Mara)  23.0  93.1666666667  Eurasia  Kuki-Chin  Sino-Tibetan  False  False
tws  sout2961  Tiwa (Southern)  35.0  -106.333333333  North America  Kiowa-Tanoan  Kiowa-Tanoan  False  False
gae  scot1245  Gaelic (Scots)  57.0  -4.0  Eurasia  Celtic  Indo-European  False  False
tpt  tapi1253  Tapieté  -19.75  -61.6666666667  South America  Tupi-Guaraní  Tupian  False  False
bos  bosn1245  Bosnian  43.0  18.0  Eurasia  Slavic  Indo-European  False  False
siu  sius1254  Siuslaw  44.0  -124.0  North America  Siuslawan  Oregon Coast  False  False
mac  macu1259  Macushi  4.0  -60.0  South America  Cariban  Cariban  False  False
nsn  nise1244  Nisenan  39.0  -121.0  North America  Maiduan  Penutian  False  False
uyg  uigh1240  Uyghur  40.0  80.0  Eurasia  Turkic  Altaic  False  False
tuc  tuca1252  Tucano  0.5  -69.1666666667  South America  Tucanoan  Tucanoan  False  False
kwo  kwom1262  Kwoma  -4.16666666667  142.75  Papunesia  Middle Sepik  Sepik  False  False
way  waya1270  Wayampi  1.0  -52.0  South America  Tupi-Guaraní  Tupian  False  False
tuv  tuvi1240  Tuvan  52.0  95.0  Eurasia  Turkic  Altaic  False  False
bun  tere1278  Buin  -6.75  155.75  Papunesia  East Bougainville  East Bougainville  False  False
xia  minn1241  Xiamen  24.5  118.166666667  Eurasia  Chinese  Sino-Tibetan  False  False
taq  minn1241  Taiwanese  25.0  121.5  Eurasia  Chinese  Sino-Tibetan  False  False
fuz  mind1253  Fuzhou  26.0  119.5  Eurasia  Chinese  Sino-Tibetan  False  False
wuc  wuch1236  Wu (Changzhou)  31.6666666667  119.916666667  Eurasia  Chinese  Sino-Tibetan  False  False
kug  mand1415  Kunming  25.0  102.75  Eurasia  Chinese  Sino-Tibetan  False  False
mnd  mand1415  Mandarin  34.0  110.0  Eurasia  Chinese  Sino-Tibetan  True  True
ble  baou1238  Baule  7.0  -5.0  Africa  Kwa  Niger-Congo  False  False
kgz  kirg1245  Kirghiz  42.0  75.0  Eurasia  Turkic  Altaic  False  False
scr  sout1528  Serbian-Croatian  44.0  19.0  Eurasia  Slavic  Indo-European  False  False
chp  chip1261  Chipewyan  59.0  -106.0  North America  Athapaskan  Na-Dene  False  False
pis  asue1235  Pisa  -5.16666666667  139.166666667  Papunesia  Awju-Dumut  Trans-New Guinea  False  False
uhi  urad1239  Uradhi  -11.9166666667  142.416666667  Australia  Pama-Nyungan  Australian  False  False
smj  sema1266  Semai  4.33333333333  101.666666667  Eurasia  Aslian  Austro-Asiatic  False  False
qec  chim1302  Quechua (Ecuadorean)  -1.0  -79.0  South America  Quechuan  Quechuan  False  False
tbw  taab1238  Tabwa  -8.0  29.5  Africa  Bantoid  Niger-Congo  False  False
ayn  ainu1251  Aynu  39.5  76.0  Eurasia  Turkic  Altaic  False  False
clc  cola1237  Colac  -38.3333333333  143.5  Australia  Pama-Nyungan  Australian  False  False
agl  aghu1253  Aghul  41.75  47.6666666667  Eurasia  Lezgic  Nakh-Daghestanian  False  False
krg  shon1251  Karanga  -20.0  31.0  Africa  Bantoid  Niger-Congo  False  False
mge  east2333  Mnong (Eastern)  12.6666666667  108.5  Eurasia  Bahnaric  Austro-Asiatic  False  False
baj  indo1317  Bajau (Sama)  -4.33333333333  123.0  Papunesia  Sama-Bajaw  Austronesian  False  False
awt  awtu1239  Awtuw  -3.58333333333  142.0  Papunesia  Ram  Sepik  False  False
twn  nort1550  Tiwa (Northern)  36.5  -105.5  North America  Kiowa-Tanoan  Kiowa-Tanoan  False  False
dji  djin1251  Djingili  -17.75  134.0  Australia  West Barkly  Australian  False  False
abz  abaz1241  Abaza  44.0  42.0  Eurasia  Northwest Caucasian  Northwest Caucasian  False  False
cba  barb1263  Chumash (Barbareño)  34.5  -120.25  North America  Chumash  Chumash  False  False
see  taro1264  Seediq  24.1666666667  121.416666667  Papunesia  Atayalic  Austronesian  False  False
bgn  bugu1246  Bugun  27.5  92.5833333333  Eurasia  Western Arunachal  Sino-Tibetan  False  False
pkm  poco1241  Pokomchí  15.4166666667  -90.5  North America  Mayan  Mayan  False  False
tce  cent2131  Tarahumara (Central)  27.5  -107.5  North America  Tarahumaran  Uto-Aztecan  False  False
yqy  yaqa1246  Yaqay  -6.58333333333  139.25  Papunesia  Marind Proper  Marind  False  False
any  anua1242  Anywa  8.0  33.5  Africa  Nilotic  Nilo-Saharan  False  False
so  sooo1256  So  2.58333333333  34.75  Africa  Kuliak  Nilo-Saharan  False  False
tho  thom1243  Thompson  49.75  -121.75  North America  Interior Salish  Salishan  False  False
cic  nyan1308  Chichewa  -14.0  34.0  Africa  Bantoid  Niger-Congo  False  False
ynk  yank1247  Yankuntjatjara  -27.0  132.0  Australia  Pama-Nyungan  Australian  False  False
lob  lobi1245  Lobi  10.5  -3.25  Africa  Gur  Niger-Congo  False  False
btk  cent2083  Bontok  17.0833333333  120.916666667  Papunesia  Northern Luzon  Austronesian  False  False
lge  nort2627  Low German  53.0  10.0  Eurasia  Germanic  Indo-European  False  False
ati  atik1240  Atikamekw  48.0  -74.0  North America  Algonquian  Algic  False  False
kda  kond1295  Konda  19.5  83.0  Eurasia  South-Central Dravidian  Dravidian  False  False
tes  teso1249  Teso  1.83333333333  33.8333333333  Africa  Nilotic  Nilo-Saharan  False  False
kgt  west2618  Kangiryuarmiut  68.3333333333  -133.75  North America  Eskimo  Eskimo-Aleut  False  False
mrs  nucl1594  Mairasi  -3.5  134.0  Papunesia  Mairasi-Tanahmerah  Trans-New Guinea  False  False
geo  nucl1302  Georgian  42.0  44.0  Eurasia  Kartvelian  Kartvelian  True  True
sno  nort2671  Saami (Northern)  69.0  24.0  Eurasia  Saami  Uralic  False  False
ych  cent2127  Yup'ik (Chevak)  61.5  -165.75  North America  Eskimo  Eskimo-Aleut  False  False
skp  selk1253  Selkup  65.0  82.0  Eurasia  Samoyedic  Uralic  False  False
aba  abau1245  Abau  -4.0  141.25  Papunesia  Upper Sepik  Sepik  False  False
bae  bare1276  Baré  1.0  -67.0  South America  Northern Arawakan  Arawakan  False  False
put  utes1238  Paiute (Southern)  37.8333333333  -113.333333333  North America  Numic  Uto-Aztecan  False  False
bee  beem1239  Beembe  -3.91666666667  14.0833333333  Africa  Bantoid  Niger-Congo  False  False
evn  even1260  Even  68.0  130.0  Eurasia  Tungusic  Altaic  False  False
ruk  ruka1240  Rukai (Tanan)  22.8333333333  120.833333333  Papunesia  Rukai  Austronesian  False  False
rom  roma1327  Romanian  46.0  25.0  Eurasia  Romance  Indo-European  False  False
ksh  kash1280  Kashaya  38.6666666667  -123.333333333  North America  Pomoan  Hokan  False  False
ctl  stan1289  Catalan  41.75  2.0  Eurasia  Romance  Indo-European  False  False
mum  nucl1240  Mumuye  9.0  11.6666666667  Africa  Adamawa  Niger-Congo  False  False
kri  kari1255  Kipea  -10.0  -37.0  South America  Kariri  Kariri  False  False
msy  west2418  Magar (Syangja)  28.0833333333  83.8333333333  Eurasia  Mahakiranti  Sino-Tibetan  False  False
syg  west2402  Saryg Yughur  38.75  99.75  Eurasia  Turkic  Altaic  False  False
koy  koya1251  Koya  17.5  81.3333333333  Eurasia  South-Central Dravidian  Dravidian  False  False
pam  cent2145  Pame  22.0  -99.5  North America  Pamean  Oto-Manguean  False  False
lav  lavu1241  Lavukaleve  -9.08333333333  159.2  Papunesia  Lavukaleve  Solomons East Papuan  True  True
wlw  warl1256  Warluwara  -22.0  138.5  Australia  Pama-Nyungan  Australian  False  False
nan  nand1266  Nandi  0.25  35.0  Africa  Nilotic  Nilo-Saharan  False  False
ood  toho1245  O'odham  32.0  -112.0  North America  Tepiman  Uto-Aztecan  False  False
pir  yine1238  Piro  -11.0  -73.5  South America  Purus  Arawakan  False  False
nrm  naro1251  Narom  4.41666666667  114.0  Papunesia  North Borneo  Austronesian  False  False
cri  crim1257  Crimean Tatar  45.0  34.0833333333  Eurasia  Turkic  Altaic  False  False
apu  apur1254  Apurinã  -9.0  -67.0  South America  Purus  Arawakan  True  True
cnl  cane1242  Canela  -7.0  -45.0  South America  Ge-Kaingang  Macro-Ge  False  False
ccp  coco1261  Cocopa  32.3333333333  -115.0  North America  Yuman  Hokan  False  False
mcr  mori1278  Mauritian Creole  -20.3333333333  57.5  Africa  Creoles and Pidgins  other  False  False
ngr  narr1259  Ngarinyeri  -36.0  140.0  Australia  Pama-Nyungan  Australian  False  False
les  lese1243  Lese  2.0  29.0  Africa  Mangbutu-Efe  Nilo-Saharan  False  False
gdf  gudu1252  Guduf  11.2333333333  13.8  Africa  Biu-Mandara  Afro-Asiatic  False  False
dgb  dagb1246  Dagbani  9.58333333333  -0.5  Africa  Gur  Niger-Congo  False  False
lno  ladi1251  Ladino  40.0  33.0  Eurasia  Romance  Indo-European  False  False
khi  khin1240  Khinalug  41.1666666667  48.0833333333  Eurasia  Lezgic  Nakh-Daghestanian  False  False
tvo  tata1255  Tatar  56.0  49.5  Eurasia  Turkic  Altaic  False  False
cjo  chic1272  Chichimeca-Jonaz  21.6666666667  -100.5  North America  Chichimec  Oto-Manguean  False  False
kfy  kirg1245  Kirghiz (Fu-Yu)  47.75  124.416666667  Eurasia  Turkic  Altaic  False  False
bsk  bash1264  Bashkir  53.0  58.0  Eurasia  Turkic  Altaic  False  False
lse  span1263  Lengua de Señas Española  40.0  -3.0  Eurasia  Sign Languages  other  False  False
mxs  sila1250  Mixtec (Silacayoapan)  17.5  -98.1666666667  North America  Mixtecan  Oto-Manguean  False  False
mid  mido1240  Midob  15.0833333333  26.25  Africa  Nubian  Nilo-Saharan  False  False
yok  yoku1256  Yokuts (Yaudanchi)  36.0833333333  -119.083333333  North America  Yokuts  Penutian  False  False
psm  male1292  Passamaquoddy-Maliseet  45.0  -67.0  North America  Algonquian  Algic  False  True
akc  akac1240  Aka-Cari  13.5  93.0  Eurasia  Great Andamanese  Great Andamanese  False  False
gan  apuc1241  Great Andamanese  12.0  92.6666666667  Eurasia  Great Andamanese  Great Andamanese  False  False
akb  akab1249  Aka-Biada  11.6666666667  92.5  Eurasia  Great Andamanese  Great Andamanese  False  False
bbl  dibo1245  Babole  1.08333333333  17.25  Africa  Bantoid  Niger-Congo  False  False
dio  jola1263  Diola-Fogny  13.0  -16.25  Africa  Northern Atlantic  Niger-Congo  False  True
rny  nyan1307  Runyankore  -0.5  30.5  Africa  Bantoid  Niger-Congo  False  False
aht  ahte1237  Ahtna  62.0  -145.0  North America  Athapaskan  Na-Dene  False  False
mni  moni1261  Moni  -3.66666666667  137.0  Papunesia  Wissel Lakes-Kemandoga  Trans-New Guinea  False  False
mij  miju1243  Miju  29.0  96.0  Eurasia  Tani  Sino-Tibetan  False  False
war  wari1268  Wari'  -11.3333333333  -65.0  South America  Chapacura-Wanham  Chapacura-Wanham  True  True
maa  masa1300  Maasai  -3.0  36.0  Africa  Nilotic  Nilo-Saharan  False  False
tni  tina1246  Tinani  32.3333333333  77.1666666667  Eurasia  Bodic  Sino-Tibetan  False  False
abu  abun1252  Abun  -0.5  132.5  Papunesia  North-Central Bird's Head  West Papuan  False  False
inu  nort2943  Iñupiaq  67.0  -161.0  North America  Eskimo  Eskimo-Aleut  False  False
nbo  nyam1277  Nyambo  -1.0  31.3333333333  Africa  Bantoid  Niger-Congo  False  False
cil  luba1249  CiLuba  -6.0  22.0  Africa  Bantoid  Niger-Congo  False  False
dhu  dhur1239  Dhurga  -35.6666666667  150.0  Australia  Pama-Nyungan  Australian  False  False
wdo  None  Western Desert (Ooldea)  -30.5  132.0  None  Pama-Nyungan  Australian  False  False
kop  komi1269  Komi-Permyak  59.5  54.5  Eurasia  Permic  Uralic  False  False
crq  carr1249  Carrier  53.75  -123.5  North America  Athapaskan  Na-Dene  False  False
bnl  bang1339  Banggarla  -32.0  137.0  Australia  Pama-Nyungan  Australian  False  False
pow  powh1243  Powhatan  37.3333333333  -76.5  North America  Algonquian  Algic  False  False
jmo  jurm1239  Jur Mödö  6.0  30.0  Africa  Bongo-Bagirmi  Nilo-Saharan  False  False
kbu  kane1243  Kanembu  14.0  15.0  Africa  Western Saharan  Nilo-Saharan  False  False
bur  buru1296  Burushaski  36.5  74.5  Eurasia  Burushaski  Burushaski  True  True
bob  bang1354  Bobangi  -1.33333333333  17.3333333333  Africa  Bantoid  Niger-Congo  False  False
wik  yoku1256  Wikchamni  36.4166666667  -119.083333333  North America  Yokuts  Penutian  False  False
bto  bata1289  Batak (Toba)  2.5  99.0  Papunesia  Northwest Sumatra-Barrier Islands  Austronesian  False  False
moo  moss1236  Mooré  12.8333333333  -1.25  Africa  Gur  Niger-Congo  False  False
iwa  iwai1244  Iwaidja  -11.5  132.666666667  Australia  Iwaidjan  Australian  False  False
asl  amer1248  American Sign Language  39.0  -78.0  North America  Sign Languages  other  False  False
kus  kusu1250  Kusunda  28.0  84.6666666667  Eurasia  Kusunda  Kusunda  False  False
kem  qima1242  Kemant  12.6666666667  37.4166666667  Africa  Central Cushitic  Afro-Asiatic  False  False
kfc  None  Kriol (Fitzroy Crossing)  -18.1666666667  125.583333333  None  Creoles and Pidgins  other  False  False
dom  doma1258  Domari  32.0  35.0  Eurasia  Indic  Indo-European  False  False
htt  mini1256  Huitoto  -1.0  -74.0  South America  Huitoto  Huitotoan  False  False
knd  nucl1305  Kannada  14.0  76.0  Eurasia  Southern Dravidian  Dravidian  True  True
kro  kron1241  Krongo  10.5  30.0  Africa  Kadugli  Kadugli  True  True
yna  nauk1242  Yupik (Naukan)  66.0  -172.0  Eurasia  Eskimo  Eskimo-Aleut  False  False
ain  ainu1240  Ainu  43.0  143.0  Eurasia  Ainu  Ainu  False  True
kyl  east2342  Kayah Li (Eastern)  19.0  97.5  Eurasia  Karen  Sino-Tibetan  False  True
dts  toro1252  Toro So  14.4166666667  -3.25  Africa  Dogon  Niger-Congo  False  False
lje  lauj1238  Lauje  -0.5  120.0  Papunesia  Celebic  Austronesian  False  False
wrg  warr1255  Warrgamay  -18.5833333333  146.083333333  Australia  Pama-Nyungan  Australian  False  False
kkv  kali1298  Kaliai-Kove  -5.58333333333  149.666666667  Papunesia  Oceanic  Austronesian  False  False
brw  west2397  Bru (Western)  16.75  104.75  Eurasia  Katuic  Austro-Asiatic  False  False
hrr  hara1271  Harari  9.25  42.1666666667  Africa  Semitic  Afro-Asiatic  False  False
kim  kima1246  Kimaghama  -8.0  138.5  Papunesia  Kolopom  Kolopom  False  False
ngu  nort2836  Nguna  -16.9166666667  168.5  Papunesia  Oceanic  Austronesian  False  False
nko  chig1238  Nkore-Kiga  -0.916666666667  29.8333333333  Africa  Bantoid  Niger-Congo  False  True
bus  busa1253  Busa  9.66666666667  4.0  Africa  Eastern Mande  Niger-Congo  False  False
mxg  sanm1295  Mixtec (San Miguel el Grande)  17.05  -97.5666666667  North America  Mixtecan  Oto-Manguean  False  False
tsn  tson1249  Tsonga  -24.0  32.0  Africa  Bantoid  Niger-Congo  False  False
amb  ambu1247  Ambulas  -3.83333333333  143.0  Papunesia  Middle Sepik  Sepik  False  False
klz  kala1384  Kalanga  -20.5  27.5  Africa  Bantoid  Niger-Congo  False  False
hlu  halk1245  Halkomelem (Upriver)  49.25  -121.916666667  North America  Central Salish  Salishan  False  False
tic  ticu1245  Ticuna  -4.0  -70.5  South America  Ticuna  Ticuna  False  False
brd  bard1255  Bardi  -16.5833333333  122.916666667  Australia  Nyulnyulan  Australian  False  False
tnb  ango1257  Tunebo  6.75  -72.25  South America  Chibchan Proper  Chibchan  False  False
tet  tete1250  Tetela  -4.0  24.0  Africa  Bantoid  Niger-Congo  False  False
bej  beja1238  Beja  18.0  36.0  Africa  Beja  Afro-Asiatic  False  True
sim  sime1241  Simeulue  2.5  96.25  Papunesia  Northwest Sumatra-Barrier Islands  Austronesian  False  False
agt  leni1238  Anguthimri  -12.3333333333  141.833333333  Australia  Pama-Nyungan  Australian  False  False
pen  peng1244  Pengo  19.8333333333  83.8333333333  Eurasia  South-Central Dravidian  Dravidian  False  False
lai  haka1240  Lai  22.6666666667  93.6666666667  Eurasia  Kuki-Chin  Sino-Tibetan  False  False
sak  saka1289  Sakao  -15.1666666667  167.083333333  Papunesia  Oceanic  Austronesian  False  False
hmu  nupo1240  Huitoto (Muinane)  -2.41666666667  -71.0  South America  Huitoto  Huitotoan  False  False
qco  sout2991  Quechua (Cochabamba)  -17.5  -66.0  South America  Quechuan  Quechuan  False  False
kut  kute1249  Kutenai  49.5  -116.0  North America  Kutenai  Kutenai  True  True
bsm  bisl1239  Bislama  -16.0  168.0  Papunesia  Creoles and Pidgins  other  False  False
ksa  east1472  Keresan (Santa Ana)  35.4166666667  -106.666666667  North America  Keresan  Keresan  False  False
cin  ines1240  Chumash (Ineseño)  34.6666666667  -120.25  North America  Chumash  Chumash  False  False
ygr  yaga1260  Yagaria  -6.33333333333  145.416666667  Papunesia  Eastern Highlands  Trans-New Guinea  False  False
kyn  koyu1237  Koyukon  65.0  -155.0  North America  Athapaskan  Na-Dene  False  False
bkn  orok1266  Bakundu  4.83333333333  9.33333333333  Africa  Bantoid  Niger-Congo  False  False
kpe  libe1247  Kpelle  7.0  -10.0  Africa  Western Mande  Niger-Congo  False  False
miz  lush1249  Mizo  23.1666666667  92.8333333333  Eurasia  Kuki-Chin  Sino-Tibetan  False  False
ksg  sgaw1245  Karen (Sgaw)  18.0  97.0  Eurasia  Karen  Sino-Tibetan  False  False
kll  kalu1248  Kaluli  -6.5  142.75  Papunesia  Bosavi  Bosavi  False  False
bug  bugi1244  Bugis  -4.0  120.0  Papunesia  South Sulawesi  Austronesian  False  False
grf  gari1256  Garífuna  15.6666666667  -88.0  North America  Northern Arawakan  Arawakan  False  False
dul  drun1238  Dulong  28.0  98.3333333333  Eurasia  Nungish  Sino-Tibetan  False  False
asm  tamn1235  Asmat  -5.5  138.5  Papunesia  Asmat-Kamoro  Trans-New Guinea  True  True
bem  bemb1258  Bemba  -10.0  28.25  Africa  Bantoid  Niger-Congo  False  False
par  pari1256  Päri  5.0  32.5  Africa  Nilotic  Nilo-Saharan  False  False
kfe  koro1298  Koromfe  14.25  -0.916666666667  Africa  Gur  Niger-Congo  False  True
nob  nobi1240  Nobiin  21.0  31.0  Africa  Nubian  Nilo-Saharan  False  False
mea  meya1236  Meyah  -1.16666666667  133.5  Papunesia  East Bird's Head  East Bird's Head  False  False
nse  nsen1242  Nsenga  -14.5  30.8333333333  Africa  Bantoid  Niger-Congo  False  False
nor  norw1259  Norwegian  61.0  8.0  Eurasia  Germanic  Indo-European  False  False
jur  jurc1239  Jurchen  47.0  130.0  Eurasia  Tungusic  Altaic  False  False
ahu  aghu1255  Aghu  -6.16666666667  140.166666667  Papunesia  Awju-Dumut  Trans-New Guinea  False  False
mka  maho1249  Mauka  8.33333333333  -7.5  Africa  Western Mande  Niger-Congo  False  False
yug  yugh1239  Yugh  61.0  90.0  Eurasia  Yeniseian  Yeniseian  False  False
gdl  guad1242  Guadeloupe Creole  16.25  -61.5  North America  Creoles and Pidgins  other  False  False
bkl  cent2087  Bikol  13.3333333333  123.5  Papunesia  Greater Central Philippine  Austronesian  False  False
laf  lafo1243  Lafofa  10.25  31.25  Africa  Tegem  Niger-Congo  False  False
mkn  mank1251  Mankanya  12.0833333333  -15.9166666667  Africa  Northern Atlantic  Niger-Congo  False  False
sly  sela1260  Selayar  -6.0  120.5  Papunesia  South Sulawesi  Austronesian  False  False
did  didi1258  Didinga  4.5  33.5  Africa  Surmic  Nilo-Saharan  False  False
win  wint1259  Wintu  41.0  -122.5  North America  Wintuan  Penutian  False  False
tne  timn1235  Temne  8.66666666667  -13.0833333333  Africa  Southern Atlantic  Niger-Congo  False  False
tay  tayo1238  Tayo  -22.0  166.333333333  Papunesia  Creoles and Pidgins  other  False  False
bik  biak1248  Biak  -1.0  136.0  Papunesia  South Halmahera - West New Guinea  Austronesian  False  False
nym  nyam1276  Nyamwezi  -5.0  33.0  Africa  Bantoid  Niger-Congo  False  False
run  rung1258  Runga  10.3333333333  21.0  Africa  Maban  Nilo-Saharan  False  False
bgo  bong1285  Bongo  7.5  28.5  Africa  Bongo-Bagirmi  Nilo-Saharan  False  False
kaz  kaza1248  Kazakh  50.0  70.0  Eurasia  Turkic  Altaic  False  False
tam  east2347  Tamang (Eastern)  27.5  85.6666666667  Eurasia  Bodic  Sino-Tibetan  False  False
ckr  krah1246  Canela-Krahô  -6.0  -46.0  South America  Ge-Kaingang  Macro-Ge  True  True
ams  stan1318  Arabic (Modern Standard)  25.0  42.0  Eurasia  Semitic  Afro-Asiatic  False  False
yyg  yayg1236  Yaygir  -29.6666666667  153.0  Australia  Pama-Nyungan  Australian  False  False
baw  bawm1236  Bawm  22.5  92.25  Eurasia  Kuki-Chin  Sino-Tibetan  False  True
umb  umbu1257  UMbundu  -12.5  15.0  Africa  Bantoid  Niger-Congo  False  False
tew  tewa1260  Tewa (Arizona)  35.8333333333  -110.416666667  North America  Kiowa-Tanoan  Kiowa-Tanoan  False  False
gmz  gumu1244  Gumuz  12.5  35.8333333333  Africa  Gumuz  Nilo-Saharan  False  False
mag  east2352  Magar  28.0  83.0  Eurasia  Mahakiranti  Sino-Tibetan  False  False
mkh  None  Mongol (Khamnigan)  49.0  117.0  None  Mongolic  Altaic  False  False
dds  donn1238  Donno So  14.3333333333  -3.58333333333  Africa  Dogon  Niger-Congo  False  False
sha  shan1277  Shan  22.0  98.0  Eurasia  Kam-Tai  Tai-Kadai  False  False
itz  itza1241  Itzaj  17.0  -89.8333333333  North America  Mayan  Mayan  False  False
zar  zarm1239  Zarma  13.8333333333  2.16666666667  Africa  Songhay  Nilo-Saharan  False  False
yi  sich1238  Yi  24.0  104.0  Eurasia  Burmese-Lolo  Sino-Tibetan  False  False
ful  fuln1247  Fulniô  -8.0  -37.5  South America  Yatê  Macro-Ge  False  False
kiw  nort2930  Kiwai  -8.0  143.5  Papunesia  Kiwaian  Kiwaian  False  False
lkt  lako1247  Lakhota  43.8333333333  -101.833333333  North America  Siouan  Siouan  True  True
wma  west2600  West Makian  0.5  127.583333333  Papunesia  North Halmaheran  West Papuan  False  False
arx  area1240  'Are'are  -9.25  161.166666667  Papunesia  Oceanic  Austronesian  False  False
she  sher1255  Sherpa  27.75  86.8333333333  Eurasia  Bodic  Sino-Tibetan  False  False
nep  nepa1252  Nepali  28.0  85.0  Eurasia  Indic  Indo-European  False  False
ots  east2556  Otomí (Sierra)  20.6666666667  -98.8333333333  North America  Otomian  Oto-Manguean  False  False
mlc  mala1533  Malacca Creole  2.2  102.25  Eurasia  Creoles and Pidgins  other  False  False
goo  goon1238  Gooniyandi  -18.3333333333  126.333333333  Australia  Bunuban  Australian  True  True
sin  sion1247  Siona  0.333333333333  -76.25  South America  Tucanoan  Tucanoan  False  False
keo  keoo1238  Ke'o  -8.83333333333  121.25  Papunesia  Central Malayo-Polynesian  Austronesian  False  False
kal  kala1373  Kalami  35.5  72.5  Eurasia  Indic  Indo-European  False  False
omi  omie1241  Ömie  -9.05  148.083333333  Papunesia  Koiarian  Trans-New Guinea  False  False
ten  tenn1246  Tennet  4.41666666667  32.5  Africa  Surmic  Nilo-Saharan  False  False
hdi  hdii1240  Hdi  11.8666666667  13.7166666667  Africa  Biu-Mandara  Afro-Asiatic  False  False
aji  ajie1238  Ajië  -21.3333333333  165.5  Papunesia  Oceanic  Austronesian  False  False
sou  uppe1395  Sorbian (Upper)  51.8333333333  14.5  Eurasia  Slavic  Indo-European  False  False
lug  lugb1240  Lugbara  3.08333333333  30.9166666667  Africa  Moru-Ma'di  Nilo-Saharan  False  False
nuk  nuka1242  Nukak  2.5  -71.5  South America  Cacua-Nukak  Cacua-Nukak  False  False
kmw  kamu1258  Kamu  -13.5833333333  130.833333333  Australia  Eastern Daly  Australian  False  False
cat  embe1260  Catio  7.16666666667  -76.3333333333  South America  Choco  Choco  False  False
ghr  gahr1239  Gahri  32.5  77.0  Eurasia  Bodic  Sino-Tibetan  False  False
dak  dako1258  Dakota  45.0  -93.5  North America  Siouan  Siouan  False  False
mns  mans1258  Mansi  62.0  62.0  Eurasia  Ugric  Uralic  False  False
nax  naxi1245  Naxi  27.5  100.0  Eurasia  Naxi  Sino-Tibetan  False  False
npi  nige1257  Nigerian Pidgin  6.5  3.33333333333  Africa  Creoles and Pidgins  other  False  False
bum  tean1237  Buma  -11.6333333333  166.833333333  Papunesia  Oceanic  Austronesian  False  False
dng  ding1239  Ding  -4.33333333333  19.5  Africa  Bantoid  Niger-Congo  False  False
msl  nucl1440  Masalit  13.3333333333  22.0  Africa  Maban  Nilo-Saharan  False  False
kli  ledo1238  Kaili  -1.16666666667  120.0  Papunesia  Celebic  Austronesian  False  False
sla  slav1253  Slave  67.0  -125.0  North America  Athapaskan  Na-Dene  True  True
thp  thay1248  Thaypan  -14.8333333333  143.166666667  Australia  Pama-Nyungan  Australian  False  False
kwa  kwai1243  Kwaio  -8.95  161.0  Papunesia  Oceanic  Austronesian  False  False
tgk  tiga1245  Tigak  -2.71666666667  150.8  Papunesia  Oceanic  Austronesian  False  False
toa  toar1246  Toaripi  -8.33333333333  146.25  Papunesia  Eleman Proper  Eleman  False  False
bim  bima1247  Bima  -8.5  118.5  Papunesia  Central Malayo-Polynesian  Austronesian  False  False
brf  tari1263  Berber (Rif)  34.5  -4.0  Africa  Berber  Afro-Asiatic  False  False
xok  xokl1240  Xokleng  -24.5  -50.0  South America  Ge-Kaingang  Macro-Ge  False  False
kba  kamb1297  Kamba  -1.5  38.0  Africa  Bantoid  Niger-Congo  False  False
wrk  guar1293  Warekena  1.5  -67.5  South America  Northern Arawakan  Arawakan  False  False
ayi  anyi1245  Anyi  7.0  -3.5  Africa  Kwa  Niger-Congo  False  False
tso  tsou1248  Tsou  23.5  120.75  Papunesia  Tsouic  Austronesian  False  False
cck  chic1270  Chickasaw  34.0  -88.0  North America  Muskogean  Muskogean  False  False
ipi  indi1237  Indo-Pakistani Sign Language (Indian dialects)  24.0  80.0  Eurasia  Sign Languages  other  False  False
gdi  godi1239  Godié  5.41666666667  -5.83333333333  Africa  Kru  Niger-Congo  False  False
sgu  sang1333  Sangu  -1.5  11.8333333333  Africa  Bantoid  Niger-Congo  False  False
mur  murs1242  Mursi  5.58333333333  36.0833333333  Africa  Surmic  Nilo-Saharan  False  False
jin  jino1236  Jino  22.0  101.0  Eurasia  Burmese-Lolo  Sino-Tibetan  False  False
mti  bari1297  Motilón (Chibchan)  9.0  -73.0  South America  Motilon  Chibchan  False  False
pum  pumi1242  Pumi  28.0  101.0  Eurasia  Qiangic  Sino-Tibetan  False  False
kdg  kari1317  Karipuna do Guapore  -10.0  -65.0  South America  Panoan  Panoan  False  False
syu  salt1242  Salt-Yui  -6.28333333333  145.033333333  Papunesia  Chimbu  Trans-New Guinea  False  False
jbt  djeo1235  Jabutí  -12.25  -62.25  South America  Jabutí  Jabutí  False  False
ign  igna1246  Ignaciano  -15.1666666667  -65.4166666667  South America  Bolivia-Parana  Arawakan  False  False
mgl  ming1252  Mingrelian  42.5  42.0  Eurasia  Kartvelian  Kartvelian  False  False
amd  amdo1237  Amdo  35.0  100.0  Eurasia  Bodic  Sino-Tibetan  False  False
jia  jiar1239  Jiarong  31.5  102.0  Eurasia  rGyalrong  Sino-Tibetan  False  False
yak  yaka1269  Yaka  -7.0  17.5  Africa  Bantoid  Niger-Congo  False  False
oka  okan1243  Okanagan  49.5  -118.5  North America  Interior Salish  Salishan  False  False
sgr  sang1336  Sangir  3.5  125.5  Papunesia  Sangiric  Austronesian  False  False
yny  yany1243  Yanyuwa  -16.4166666667  137.166666667  Australia  Pama-Nyungan  Australian  False  False
brk  beri1254  Berik  -2.25  138.833333333  Papunesia  Tor  Tor-Orya  False  False
wem  None  Wembawemba  -35.3333333333  144.0  None  Pama-Nyungan  Australian  False  False
adn  adny1235  Adynyamathanha  -30.5  139.5  Australia  Pama-Nyungan  Australian  False  False
wrl  warl1254  Warlpiri  -20.0  132.333333333  Australia  Pama-Nyungan  Australian  False  False
fue  east2447  Futuna (East)  -14.3333333333  -178.166666667  Papunesia  Oceanic  Austronesian  False  False
apc  mesc1238  Apache (Chiricahua)  33.25  -108.0  North America  Athapaskan  Na-Dene  False  False
trd  tora1261  Toraja  -3.0  119.75  Papunesia  South Sulawesi  Austronesian  False  False
ngj  ngad1258  Ngadjumaja  -32.3333333333  123.833333333  Australia  Pama-Nyungan  Australian  False  False
msk  ngil1242  Masakin  10.6666666667  30.0  Africa  Talodi Proper  Niger-Congo  False  False
mun  mund1320  Mundari  23.0  84.6666666667  Eurasia  Munda  Austro-Asiatic  False  True
krt  kara1474  Karata  42.5833333333  46.3333333333  Eurasia  Avar-Andic-Tsezic  Nakh-Daghestanian  False  False
grg  gura1252  Gurr-goni  -12.25  134.416666667  Australia  Burarran  Australian  False  False
squ  squa1248  Squamish  49.6666666667  -123.166666667  North America  Central Salish  Salishan  False  True
usa  usan1239  Usan  -4.83333333333  145.166666667  Papunesia  Madang  Trans-New Guinea  False  True
puk  para1301  Parauk  23.25  99.5  Eurasia  Palaung-Khmuic  Austro-Asiatic  False  False
krh  krah1246  Krahô  -8.0  -48.0  South America  Ge-Kaingang  Macro-Ge  False  False
dhl  dhal1245  Dhalandji  -22.08  115.0  Australia  Pama-Nyungan  Australian  False  False
vka  kari1304  Kariera  -20.5  118.5  Australia  Pama-Nyungan  Australian  False  False
lnj  leni1238  Linngithig  -12.5  142.83  Australia  Pama-Nyungan  Australian  False  False
nlr  ngar1286  Ngarla  -20.0  119.0  Australia  Pama-Nyungan  Australian  False  False
nly  nyam1271  Nyamal  -21.0  119.0  Australia  Pama-Nyungan  Australian  False  False
ump  umpi1239  Umpila  -13.5  143.5  Australia  Pama-Nyungan  Australian  False  False
wbt  wanm1242  Wanman  -22.0  123.0  Australia  Pama-Nyungan  Australian  False  False
ylr  yala1262  Yalarnnga  -22.0  140.0  Australia  Pama-Nyungan  Australian  False  False
huc  huaa1248  =|Hoan  -25.5  25.0  Africa  =|Hoan  Khoisan  False  False
tia  tima1241  Tima  11.6666666667  29.25  Africa  Katla-Tima  Niger-Congo  False  False
ney  neyo1238  Neyo  5.0  -6.0  Africa  Kru  Niger-Congo  False  False
nrg  nane1238  Nanerge  11.75  -5.0  Africa  Gur  Niger-Congo  False  False
wwa  waam1244  Waama  10.5833333333  1.66666666667  Africa  Gur  Niger-Congo  False  False
xsm  kase1253  Kàsim  11.0  -1.33333333333  Africa  Gur  Niger-Congo  False  False
mmi  mamb1294  Mambai  9.66666666667  14.0  Africa  Adamawa  Niger-Congo  False  False
myg  mayo1261  Mayogo  3.0  29.0  Africa  Ubangi  Niger-Congo  False  False
ajg  ajab1235  Ajagbe  7.0  1.75  Africa  Kwa  Niger-Congo  False  False
guw  gunn1250  Gungbe  6.5  2.5  Africa  Kwa  Niger-Congo  False  False
avk  avik1243  Avikam  5.16666666667  -5.5  Africa  Kwa  Niger-Congo  False  False
mkq  ngem1255  Mankon  6.0  10.1666666667  Africa  Bantoid  Niger-Congo  False  False
mdw  mbos1242  Mbosi  -1.25  15.5  Africa  Bantoid  Niger-Congo  False  False
kwy  sans1272  Iwoyo  -5.5  12.25  Africa  Bantoid  Niger-Congo  False  False
zag  zagh1240  Beria  16.0  23.0  Africa  Eastern Saharan  Nilo-Saharan  False  False
mgq  mang1398  Mango  8.75  17.0  Africa  Bongo-Bagirmi  Nilo-Saharan  False  False
sid  sida1246  Sidaama  6.66666666667  38.5  Africa  Eastern Cushitic  Afro-Asiatic  False  False
arj  gulf1241  Arabic (Kuwaiti)  29.5  47.5  Eurasia  Semitic  Afro-Asiatic  False  False
bkb  bett1235  Betta Kurumba  11.5  76.75  Eurasia  Southern Dravidian  Dravidian  False  False
rji  raji1240  Raji  28.0  82.75  Eurasia  Bodic  Sino-Tibetan  False  False
ksn  suoy1242  Kasong  12.75  102.116666667  Eurasia  Pearic  Austro-Asiatic  False  False
tbx  seke1240  Tangbe  28.9166666667  83.75  Eurasia  Bodic  Sino-Tibetan  False  False
tdi  tibe1272  Tibetan (Dingri)  28.5  86.5  Eurasia  Bodic  Sino-Tibetan  False  False
tdr  tibe1272  Tibetan (Drokpa)  32.25  81.25  Eurasia  Bodic  Sino-Tibetan  False  False
amt  amdo1237  Amdo (Themchen)  38.0  98.0  Eurasia  Bodic  Sino-Tibetan  False  False
shg  tibe1272  Shigatse  29.0  89.0  Eurasia  Bodic  Sino-Tibetan  False  False
rpa  tibe1272  Rang Pas  30.3333333333  79.3333333333  Eurasia  Bodic  Sino-Tibetan  False  False
wme  wamb1257  Wambule  29.25  85.9166666667  Eurasia  Mahakiranti  Sino-Tibetan  False  False
ybi  yamp1242  Yamphu  27.5833333333  87.3333333333  Eurasia  Mahakiranti  Sino-Tibetan  False  False
gyc  jiar1239  Gyarong (Cogtse)  31.5  102.0  Eurasia  rGyalrong  Sino-Tibetan  False  False
rgc  jiar1239  rGyalrong (Caodeng)  31.6666666667  101.75  Eurasia  rGyalrong  Sino-Tibetan  False  False
tvt  tuts1235  Tutsa  27.5  96.5  Eurasia  Northern Naga  Sino-Tibetan  False  False
ral  ralt1242  Ralte  23.75  92.75  Eurasia  Kuki-Chin  Sino-Tibetan  False  False
mhl  misi1242  Miri (Hill):  27.9166666667  93.8333333333  Eurasia  Tani  Sino-Tibetan  False  False
khn  khun1259  Khün  21.0  100.0  Eurasia  Kam-Tai  Tai-Kadai  False  False
smp  shom1245  Shompen  7.0  93.75  Eurasia  Shompen  Shompen  False  False
ttd  tetu1245  Tetun Dili  -8.58333333333  125.583333333  Papunesia  Central Malayo-Polynesian  Austronesian  False  False
lab  labu1248  Labu  -6.75  146.916666667  Papunesia  Oceanic  Austronesian  False  False
vnm  vinm1237  Vinmavis  -16.1666666667  167.416666667  Papunesia  Oceanic  Austronesian  False  False
erk  sout2856  Efate (South)  -17.75  168.416666667  Papunesia  Oceanic  Austronesian  False  False
ndr  fiji1243  Nadroga  -18.0833333333  177.416666667  Papunesia  Oceanic  Austronesian  False  False
mpt  mian1256  Mian  -4.75  141.5  Papunesia  Ok  Trans-New Guinea  False  False
mkj  maka1316  Makasae  -8.66666666667  126.5  Papunesia  Makasae-Fataluku-Oirata  Timor-Alor-Pantar  False  False
adg  adan1251  Adang  -8.2  124.0  Papunesia  Greater Alor  Timor-Alor-Pantar  False  False
bdw  baha1258  Baham  -3.16666666667  132.666666667  Papunesia  West Bomberai  West Bomberai  False  False
dlm  dera1245  Dla (Menggwa)  -3.55  141.033333333  Papunesia  Senagi  Senagi  False  False
brp  wara1302  Barupu  -3.08333333333  142.083333333  Papunesia  Warapu  Skou  False  False
kwt  nucl1593  Kwomtari  -3.5  141.5  Papunesia  Kwomtari  Kwomtari-Baibai  False  False
amm  amap1240  Ama  -4.21666666667  141.616666667  Papunesia  Left May  Left May  False  False
urt  urat1244  Urat  -3.66666666667  142.833333333  Papunesia  Wapei-Palei  Torricelli  False  False
aoj  mufi1238  Mufian  -3.5  143.0  Papunesia  Kombio-Arapesh  Torricelli  False  False
kmz  kama1367  Kamasau  -3.91666666667  143.666666667  Papunesia  Marienberg  Torricelli  False  False
tee  hueh1236  Tepehua (Huehuetla)  20.5  -98.0  North America  Totonacan  Totonacan  False  False
mxx  None  Mixe (Ayutla)  17.0833333333  -96.0833333333  None  Mixe-Zoque  Mixe-Zoque  False  False
lec  leco1242  Leko  -15.0  -67.9166666667  South America  Leko  Leko  False  False
kyz  kaya1329  Kayabí  -11.0  -55.5  South America  Tupi-Guaraní  Tupian  False  False
kno  kano1245  Kanoê  -13.25  -61.0  South America  Kapixana  Kapixana  False  False
cpy  chip1262  Chipaya  -18.75  -67.8333333333  South America  Uru-Chipaya  Uru-Chipaya  False  False
kqq  kren1239  Krenak  -15.5  -41.0  South America  Botocudo  Macro-Ge  False  False
tsl  tanz1238  Tanzania Sign Language  -6.0  35.0  Africa  Sign Languages  other  False  False
buj  kwas1243  Bujeba  3.0  10.1666666667  Africa  Bantoid  Niger-Congo  False  False
qia  qian1264  Qiang  32.0  102.666666667  Eurasia  Qiangic  Sino-Tibetan  False  False
tsr  taus1253  Taushiro  -3.25  -75.5  South America  Taushiro  Taushiro  False  False
kbi  inpu1234  Kabui  24.8333333333  94.0  Eurasia  Kuki-Chin  Sino-Tibetan  False  False
bnt  bant1286  Bantik  1.41666666667  124.75  Papunesia  Sangiric  Austronesian  False  False
sud  sude1239  Sudest  -11.5  153.45  Papunesia  Oceanic  Austronesian  False  False
pnr  enap1235  Panare  6.5  -66.0  South America  Cariban  Cariban  False  False
alg  algo1255  Algonquin  46.0  -77.0  North America  Algonquian  Algic  False  False
shs  shas1239  Shasta  41.8333333333  -122.666666667  North America  Shasta  Hokan  False  False
aik  aika1237  Aikaná  -12.6666666667  -60.6666666667  South America  Aikaná  Aikaná  False  False
sor  sora1254  Sora  20.0  84.3333333333  Eurasia  Munda  Austro-Asiatic  False  False
kkl  beng1239  Kata Kolok  -8.25  115.166666667  Papunesia  Sign Languages  other  False  False
lii  ital1275  Lingua Italiana dei Segni  42.0  13.0  Eurasia  Sign Languages  other  False  False
cac  cacu1241  Cacua  1.08333333333  -70.0  South America  Cacua-Nukak  Cacua-Nukak  False  False
lgp  port1277  Língua Gestual Portuguesa  40.0  -8.0  Eurasia  Sign Languages  other  False  False
ori  tega1236  Orig  12.1666666667  30.8333333333  Africa  Rashad  Niger-Congo  False  False
plp  ngaj1237  Pulopetak  1.41666666667  109.833333333  Papunesia  Barito  Austronesian  False  False
bir  bero1242  Birom  9.66666666667  8.83333333333  Africa  Platoid  Niger-Congo  False  False
npn  naga1394  Naga Pidgin  25.6666666667  94.0  Eurasia  Creoles and Pidgins  other  False  False
qbo  boli1262  Quechua (Bolivian)  -20.0  -66.0  South America  Quechuan  Quechuan  False  False
kko  kura1250  Koranko  9.33333333333  -11.25  Africa  Western Mande  Niger-Congo  False  False
lua  niel1243  Lua  9.75  17.75  Africa  Adamawa  Niger-Congo  False  False
mli  mali1284  Mali  -4.83333333333  152.25  Papunesia  Baining  Baining-Taulil  False  False
cos  nort2969  Costanoan  37.0  -122.0  North America  Costanoan  Penutian  False  False
ics  icel1236  Icelandic Sign Language  65.0  -18.0  Eurasia  Sign Languages  other  False  False
ptw  wint1259  Patwin  39.0  -122.333333333  North America  Wintuan  Penutian  False  False
kak  kama1370  Kamano-Kafe  -6.25  145.666666667  Papunesia  Eastern Highlands  Trans-New Guinea  False  False
occ  occi1239  Occitan  44.0  2.0  Eurasia  Romance  Indo-European  False  False
arp  buki1249  Arapesh (Mountain)  -3.46666666667  143.166666667  Papunesia  Kombio-Arapesh  Torricelli  True  True
lao  laoo1244  Lao  18.0  103.0  Eurasia  Kam-Tai  Tai-Kadai  False  False
jaq  jaqa1244  Jaqaru  -13.0  -76.0  South America  Aymaran  Aymaran  False  False
tng  tong1325  Tongan  -21.1666666667  -175.166666667  Papunesia  Oceanic  Austronesian  False  False
ths  thai1240  Thai Sign Language  15.0  101.0  Eurasia  Sign Languages  other  False  False
chb  cham1313  Chambri  -4.16666666667  143.083333333  Papunesia  Lower Sepik  Lower Sepik-Ramu  False  False
awa  awap1236  Awa  -6.66666666667  145.75  Papunesia  Eastern Highlands  Trans-New Guinea  False  False
tsp  tami1289  Tamil (Spoken)  11.0  78.0  Eurasia  Southern Dravidian  Dravidian  False  False
niu  niue1239  Niuean  -19.05  -170.116666667  Papunesia  Oceanic  Austronesian  False  False
kpn  kapi1249  Kapingamarangi  1.05  154.75  Papunesia  Oceanic  Austronesian  False  False
sub  subi1246  Subiya  -17.75  24.9166666667  Africa  Bantoid  Niger-Congo  False  False
bel  belh1239  Belhare  26.9666666667  87.3  Eurasia  Mahakiranti  Sino-Tibetan  False  False
mov  movi1243  Movima  -13.8333333333  -65.6666666667  South America  Movima  Movima  False  False
bul  bulg1262  Bulgarian  42.5  25.0  Eurasia  Slavic  Indo-European  False  False
thk  thak1245  Thakali  29.0  83.75  Eurasia  Bodic  Sino-Tibetan  False  False
cul  culi1244  Culina  -6.0  -70.5  South America  Arauan  Arauan  False  False
krm  kara1464  Karaim  54.6666666667  24.9166666667  Eurasia  Turkic  Altaic  False  False
lon  loni1238  Loniu  -2.06666666667  147.333333333  Papunesia  Oceanic  Austronesian  False  False
iba  iban1264  Iban  2.0  112.0  Papunesia  Malayo-Sumbawan  Austronesian  False  False
mas  masa1322  Masa  10.5  15.5  Africa  Masa  Afro-Asiatic  False  False
npu  napu1241  Napu  -1.33333333333  120.416666667  Papunesia  Celebic  Austronesian  False  False
daw  daww1239  Dâw  -0.25  -67.0833333333  South America  Nadahup  Nadahup  False  False
wir  wira1260  Wirangu  -32.0  134.0  Australia  Pama-Nyungan  Australian  False  False
pat  pate1247  Patep  -6.91666666667  146.583333333  Papunesia  Oceanic  Austronesian  False  False
lim  limb1266  Limbu  27.1666666667  87.75  Eurasia  Mahakiranti  Sino-Tibetan  False  False
ndo  ndon1254  Ndonga  -18.0  17.0  Africa  Bantoid  Niger-Congo  False  False
kkn  konk1267  Konkani  15.25  74.0  Eurasia  Indic  Indo-European  False  False
coa  coah1252  Coahuilteco  28.0  -100.0  North America  Coahuiltecan  Coahuiltecan  False  False
klr  shah1254  Koluri  37.0  48.0  Eurasia  Iranian  Indo-European  False  False
bui  buli1255  Buli (in Indonesia)  1.0  128.5  Papunesia  South Halmahera - West New Guinea  Austronesian  False  False
tsg  taus1251  Tausug  6.0  121.0  Papunesia  Greater Central Philippine  Austronesian  False  False
baq  baur1253  Baure  -13.0833333333  -64.1666666667  South America  Bolivia-Parana  Arawakan  False  False
hmr  hame1242  Hamer  5.0  36.5  Africa  South Omotic  Afro-Asiatic  False  False
yim  yima1243  Yimas  -4.66666666667  143.55  Papunesia  Lower Sepik  Lower Sepik-Ramu  False  True
klg  kulu1253  Kulung  27.5  87.0  Eurasia  Mahakiranti  Sino-Tibetan  False  False
hol  holo1240  Holoholo  -5.16666666667  29.9166666667  Africa  Bantoid  Niger-Congo  False  False
mmv  mamv1243  Mamvu  3.25  29.0  Africa  Mangbutu-Efe  Nilo-Saharan  False  False
slv  sout2959  Slavey  60.0  -120.0  North America  Athapaskan  Na-Dene  False  False
rik  rikb1245  Rikbaktsa  -11.8333333333  -57.5  South America  Rikbaktsa  Macro-Ge  False  False
ria  rian1263  Riantana  -7.5  138.5  Papunesia  Kolopom  Kolopom  False  False
pit  pitj1243  Pitjantjatjara  -26.0  130.0  Australia  Pama-Nyungan  Australian  False  True
kur  kuru1302  Kurukh  22.8333333333  85.5  Eurasia  Northern Dravidian  Dravidian  False  False
tag  taga1270  Tagalog  15.0  121.0  Papunesia  Greater Central Philippine  Austronesian  True  True
emm  amii1238  Emmi  -13.5  130.0  Australia  Western Daly  Australian  False  False
gdb  bodo1267  Gutob  19.0  83.6666666667  Eurasia  Munda  Austro-Asiatic  False  False
tmg  tama1336  Tamagario  -6.41666666667  139.25  Papunesia  Kayagar  Kayagar  False  False
snt  nucl1632  Sentani  -2.58333333333  140.583333333  Papunesia  Sentani  Sentani  False  True
giz  maro1246  Giziga  10.3333333333  14.1666666667  Africa  Biu-Mandara  Afro-Asiatic  False  False
mbr  mbar1260  Mbara  11.0  15.4166666667  Africa  Biu-Mandara  Afro-Asiatic  False  False
ixi  ixil1250  Ixil  15.5  -91.0  North America  Mayan  Mayan  False  False
sil  dars1235  Sila  12.3333333333  21.75  Africa  Daju  Nilo-Saharan  False  False
khu  khum1248  Khumi  21.9166666667  92.4166666667  Eurasia  Kuki-Chin  Sino-Tibetan  False  False
trb  teri1250  Teribe  9.33333333333  -82.6666666667  North America  Talamanca  Chibchan  False  False
fsl  finn1310  Finnish Sign Language  62.0  26.0  Eurasia  Sign Languages  other  False  False
lsf  fren1243  Langue des Signes Française  47.0  3.0  Eurasia  Sign Languages  other  False  False
oi  oyyy1238  Oi  14.8333333333  107.166666667  Eurasia  Bahnaric  Austro-Asiatic  False  False
klb  huba1236  Kilba  10.3333333333  13.1666666667  Africa  Biu-Mandara  Afro-Asiatic  False  False
gwo  tyap1238  Gworok  9.91666666667  8.16666666667  Africa  Platoid  Niger-Congo  False  False
nyh  nyih1240  Nyiha  -10.0  33.0  Africa  Bantoid  Niger-Congo  False  False
qhu  huam1248  Quechua (Huallaga)  -9.5  -75.5  South America  Quechuan  Quechuan  False  False
zha  jang1254  Zhang-Zhung  31.5833333333  78.4166666667  Eurasia  Bodic  Sino-Tibetan  False  False
cla  clal1241  Clallam  48.0833333333  -123.75  North America  Central Salish  Salishan  False  False
plh  paul1238  Paulohi  -3.25  128.75  Papunesia  Central Malayo-Polynesian  Austronesian  False  False
svk  slov1269  Slovak  49.0  20.0  Eurasia  Slavic  Indo-European  False  False
lur  nort2645  Luri  33.5  48.5  Eurasia  Iranian  Indo-European  False  False
ik  ikkk1242  Ik  3.75  34.1666666667  Africa  Kuliak  Nilo-Saharan  False  False
sia  sian1257  Siane  -6.08333333333  145.2  Papunesia  Eastern Highlands  Trans-New Guinea  False  False
hat  hata1243  Hatam  -1.0  134.0  Papunesia  Hatam  West Papuan  False  False
tac  taca1256  Tacana  -13.5  -68.0  South America  Tacanan  Tacanan  False  False
khv  khva1239  Khvarshi  42.25  46.1666666667  Eurasia  Avar-Andic-Tsezic  Nakh-Daghestanian  False  False
blj  kaci1244  Baale  6.5  34.5  Africa  Surmic  Nilo-Saharan  False  False
shb  shab1252  Shabo  7.58333333333  35.4166666667  Africa  Shabo  Nilo-Saharan  False  False
oir  kalm1243  Oirat  37.5  93.0  Eurasia  Mongolic  Altaic  False  False
dni  lowe1415  Dani (Lower Grand Valley)  -4.33333333333  138.833333333  Papunesia  Dani  Trans-New Guinea  True  True
mna  muna1247  Muna  -5.0  122.5  Papunesia  Celebic  Austronesian  False  False
baa  bara1377  Barai  -9.33333333333  148.083333333  Papunesia  Koiarian  Trans-New Guinea  False  False
eml  emba1238  Embaloh  1.16666666667  112.333333333  Papunesia  South Sulawesi  Austronesian  False  False
lsa  arge1236  Lengua de Señas Argentina  -34.0  -63.0  South America  Sign Languages  other  False  False
yuw  gami1243  Yuwaalaraay  -29.5  148.0  Australia  Pama-Nyungan  Australian  False  False
mdn  mand1446  Mandan  46.5  -102.5  North America  Siouan  Siouan  False  False
nsk  nask1242  Naskapi  56.0  -70.0  North America  Algonquian  Algic  False  False
yms  yems1235  Yemsa  7.83333333333  37.3333333333  Africa  North Omotic  Afro-Asiatic  False  False
laa  laal1242  Laal  10.0  17.6666666667  Africa  Laal  Laal  False  False
brn  buru1320  Burunge  -5.33333333333  36.0  Africa  Southern Cushitic  Afro-Asiatic  False  False
kws  kawa1283  Kawaiisu  36.0  -117.5  North America  Numic  Uto-Aztecan  False  False
dam  mala1522  Damana  11.0  -73.5  South America  Aruak  Chibchan  False  False
bho  bhoj1244  Bhojpuri  26.0  84.0  Eurasia  Indic  Indo-European  False  False
lit  lith1251  Lithuanian  55.0  24.0  Eurasia  Baltic  Indo-European  False  False
kbt  kaba1276  Kabatei  36.75  49.4166666667  Eurasia  Iranian  Indo-European  False  False
pac  paco1243  Pacoh  16.4166666667  107.083333333  Eurasia  Katuic  Austro-Asiatic  False  False
fiw  west2519  Fijian (Wayan)  -17.0  177.3  Papunesia  Oceanic  Austronesian  False  False
luv  luva1239  Luvale  -12.0  22.0  Africa  Bantoid  Niger-Congo  True  True
tim  timu1262  Timugon  5.0  116.0  Papunesia  North Borneo  Austronesian  False  False
cea  swam1239  Cree (Swampy)  56.0  -90.0  North America  Algonquian  Algic  False  False
ach  ache1246  Aché  -25.25  -55.1666666667  South America  Tupi-Guaraní  Tupian  False  False
kir  cerm1238  Kirma  10.25  -4.83333333333  Africa  Gur  Niger-Congo  False  False
san  sang1328  Sango  5.0  18.0  Africa  Ubangi  Niger-Congo  True  True
res  resi1247  Resígaro  -2.41666666667  -71.5  South America  Northern Arawakan  Arawakan  False  False
rwa  rawa1267  Rawa  -5.83333333333  146.0  Papunesia  Finisterre-Huon  Trans-New Guinea  False  False
nlu  ngar1287  Ngarluma  -20.8333333333  117.5  Australia  Pama-Nyungan  Australian  False  False
kio  kiow1266  Kiowa  37.0  -99.0  North America  Kiowa-Tanoan  Kiowa-Tanoan  True  True
sun  sund1252  Sundanese  -7.0  107.0  Papunesia  Malayo-Sumbawan  Austronesian  False  False
lau  lauu1247  Lau  -9.58333333333  161.5  Papunesia  Oceanic  Austronesian  False  False
ork  orok1265  Orok  49.5  143.5  Eurasia  Tungusic  Altaic  False  False
lsq  queb1245  Langue des Signes Québecoise  48.0  -75.0  North America  Sign Languages  other  False  False
tda  toda1252  Toda  11.4166666667  76.75  Eurasia  Southern Dravidian  Dravidian  False  False
mtu  motu1246  Motu  -9.33333333333  147.0  Papunesia  Oceanic  Austronesian  False  False
kpw  east2341  Karen (Pwo)  13.0  99.1666666667  Eurasia  Karen  Sino-Tibetan  False  False
tum  tuml1238  Tumleo  -3.08333333333  142.416666667  Papunesia  Oceanic  Austronesian  False  False
lal  xish1235  Lalo  25.0  100.25  Eurasia  Burmese-Lolo  Sino-Tibetan  False  False
uzb  uzbe1247  Uzbek  39.0  66.0  Eurasia  Turkic  Altaic  False  False
bod  bodo1269  Bodo  26.8333333333  92.0  Eurasia  Bodo-Garo  Sino-Tibetan  False  False
rem  bond1245  Remo  18.0  82.0  Eurasia  Munda  Austro-Asiatic  False  False
bok  boko1266  Boko  10.5  3.5  Africa  Eastern Mande  Niger-Congo  False  False
ong  onge1236  Onge  10.75  92.4166666667  Eurasia  South Andamanese  South Andamanese  False  False
ore  orej1242  Orejón  -2.83333333333  -72.5  South America  Tucanoan  Tucanoan  False  False
irs  iris1235  Irish Sign Language  53.5  -7.5  Eurasia  Sign Languages  other  False  False
mmn  mama1275  Mamanwa  9.41666666667  125.5  Papunesia  Greater Central Philippine  Austronesian  False  False
grs  garu1246  Garus  -4.95  145.666666667  Papunesia  Madang  Trans-New Guinea  False  False
cyg  cayu1261  Cayuga  42.75  -76.75  North America  Northern Iroquoian  Iroquoian  False  False
rtk  roto1249  Rotokas  -6.0  155.166666667  Papunesia  West Bougainville  West Bougainville  False  False
ngz  ngiz1242  Ngizim  12.0833333333  10.9166666667  Africa  West Chadic  Afro-Asiatic  False  False
knm  kuna1268  Kunama  14.5  37.0  Africa  Kunama  Nilo-Saharan  False  True
atq  paci1278  Alutiiq  57.0  -157.0  North America  Eskimo  Eskimo-Aleut  False  False
but  mong1330  Buriat  52.0  108.0  Eurasia  Mongolic  Altaic  False  False
sro  siro1249  Siroi  -5.5  146.0  Papunesia  Madang  Trans-New Guinea  False  False
duk  huns1239  Duka  11.1666666667  5.08333333333  Africa  Kainji  Niger-Congo  False  False
oko  adiv1239  Oriya (Kotia)  18.3333333333  83.0  Eurasia  Indic  Indo-European  False  False
svs  savo1255  Savosavo  -9.13333333333  159.8  Papunesia  Savosavo  Solomons East Papuan  False  False
sgl  seng1278  Sengele  -1.83333333333  17.3333333333  Africa  Bantoid  Niger-Congo  False  False
lch  lach1248  Lachi  22.6666666667  104.833333333  Eurasia  Kadai  Tai-Kadai  False  False
tnl  lowe1425  Tanana (Lower)  65.0  -150.0  North America  Athapaskan  Na-Dene  False  False
kou  komc1235  Kom  6.25  10.3333333333  Africa  Bantoid  Niger-Congo  False  False
lmb  lamb1271  Lamba  -13.0  28.0  Africa  Bantoid  Niger-Congo  False  False
bet  dalo1238  Bété  6.25  -6.25  Africa  Kru  Niger-Congo  False  False
scs  sout2674  Saami (Central-South)  64.6666666667  16.75  Eurasia  Saami  Uralic  False  False
moh  moha1258  Mohawk  43.5  -74.25  North America  Northern Iroquoian  Iroquoian  False  False
kau  kaul1240  Kaulong  -6.16666666667  149.666666667  Papunesia  Oceanic  Austronesian  False  False
ndg  ndog1248  Ndogo  7.75  27.0  Africa  Ubangi  Niger-Congo  False  False
trr  nort2920  Tairora  -6.5  146.0  Papunesia  Eastern Highlands  Trans-New Guinea  False  False
tnc  tana1290  Tanacross  63.5  -143.5  North America  Athapaskan  Na-Dene  False  False
tmk  tuma1260  Tumak  9.5  17.3333333333  Africa  East Chadic  Afro-Asiatic  False  False
mad  madi1260  Ma'di  3.25  31.5  Africa  Moru-Ma'di  Nilo-Saharan  False  False
kga  nucl1379  Kinga  -9.0  34.0  Africa  Bantoid  Niger-Congo  False  False
mom  nucl1452  Mombum  -8.25  138.75  Papunesia  Mombum  Mombum  False  False
ktk  afad1236  Kotoko  11.3333333333  15.3333333333  Africa  Biu-Mandara  Afro-Asiatic  False  False
dag  daga1275  Daga  -10.0  149.333333333  Papunesia  Dagan  Dagan  True  True
ras  tega1236  Rashad  11.8333333333  31.05  Africa  Rashad  Niger-Congo  False  False
dug  gaww1239  Dullay (Gollango)  5.5  37.25  Africa  Eastern Cushitic  Afro-Asiatic  False  False
kag  kome1238  Kayu Agung  -3.16666666667  104.916666667  Papunesia  Lampungic  Austronesian  False  False
ame  amel1241  Amele  -5.25  145.583333333  Papunesia  Madang  Trans-New Guinea  True  True
anx  andi1255  Andi  42.75  46.25  Eurasia  Avar-Andic-Tsezic  Nakh-Daghestanian  False  False
god  ghod1238  Godoberi  42.6666666667  46.0833333333  Eurasia  Avar-Andic-Tsezic  Nakh-Daghestanian  False  False
lns  lamn1239  Lamnso'  6.16666666667  10.75  Africa  Bantoid  Niger-Congo  False  False
thu  thul1246  Thulung  27.4166666667  86.5  Eurasia  Mahakiranti  Sino-Tibetan  False  False
tus  tusc1257  Tuscarora  36.0  -77.5  North America  Northern Iroquoian  Iroquoian  False  False
mrq  nort2845  Marquesan  -8.91666666667  -140.083333333  Papunesia  Oceanic  Austronesian  False  False
pro  occi1239  Provençal  44.0  6.0  Eurasia  Romance  Indo-European  False  False
qan  chiq1249  Quechua (Ancash)  -8.5  -77.5  South America  Quechuan  Quechuan  False  False
let  leti1246  Leti  -8.2  127.666666667  Papunesia  Central Malayo-Polynesian  Austronesian  False  False
rsl  russ1255  Russian Sign Language  56.0  44.0  Eurasia  Sign Languages  other  False  False
hnk  hinu1240  Hinukh  42.1666666667  46.0  Eurasia  Avar-Andic-Tsezic  Nakh-Daghestanian  False  False
bvi  bali1280  Bali-Vitu  -4.9  149.116666667  Papunesia  Oceanic  Austronesian  False  False
mto  kuma1274  Malto  25.0  87.3333333333  Eurasia  Northern Dravidian  Dravidian  False  False
mbi  bamb1266  Mbili  6.11666666667  10.2  Africa  Bantoid  Niger-Congo  False  False
dhr  dhar1247  Dhargari  -23.75  114.916666667  Australia  Pama-Nyungan  Australian  False  False
kum  kuma1273  Kumauni  30.0  80.0  Eurasia  Indic  Indo-European  False  False
mrh  mari1424  Marrithiyel  -13.8333333333  130.0  Australia  Western Daly  Australian  False  False
xar  xara1244  Xârâcùù  -21.6666666667  166.0  Papunesia  Oceanic  Austronesian  False  False
ktz  kati1270  Kati (in Afghanistan)  35.5  70.0  Eurasia  Indic  Indo-European  False  False
alt  swis1247  Alsatian  48.5  7.5  Eurasia  Germanic  Indo-European  False  False
ceb  cebu1242  Cebuano  10.0  124.0  Papunesia  Greater Central Philippine  Austronesian  False  False
sec  seco1241  Secoya  -0.333333333333  -76.0  South America  Tucanoan  Tucanoan  False  False
jum  juma1249  Júma  -7.5  -64.0  South America  Tupi-Guaraní  Tupian  False  False
mnr  mand1442  Mandar  -3.41666666667  119.083333333  Papunesia  South Sulawesi  Austronesian  False  False
ute  utes1238  Ute  39.0  -109.0  North America  Numic  Uto-Aztecan  False  False
ewa  ewee1241  Ewe (Anglo)  6.0  1.0  Africa  Kwa  Niger-Congo  False  False
acn  acha1249  Achang  25.0  98.5  Eurasia  Burmese-Lolo  Sino-Tibetan  False  False
bbm  bamb1270  Bambam  -3.08333333333  119.083333333  Papunesia  South Sulawesi  Austronesian  False  False
snn  soni1259  Soninke  15.0  -10.5  Africa  Western Mande  Niger-Congo  False  False
tir  trio1238  Tiriyo  3.25  -55.75  South America  Cariban  Cariban  False  False
mce  beli1260  Mískito Coast English Creole  16.25  -88.8333333333  North America  Creoles and Pidgins  other  False  False
sul  sulk1246  Sulka  -5.08333333333  151.916666667  Papunesia  Sulka  Sulka  False  False
mks  maka1311  Makassar  -5.41666666667  119.583333333  Papunesia  South Sulawesi  Austronesian  False  False
blz  bala1300  Balanta  12.25  -15.3333333333  Africa  Northern Atlantic  Niger-Congo  False  False
mav  mari1435  Maring  -5.5  144.666666667  Papunesia  Chimbu  Trans-New Guinea  False  False
tui  turk1288  Türk Isaret Dili  39.0  34.0  Eurasia  Sign Languages  other  False  False
lmg  lama1288  Lamang  11.25  13.5833333333  Africa  Biu-Mandara  Afro-Asiatic  False  False
agh  aghe1239  Aghem  6.66666666667  10.0  Africa  Bantoid  Niger-Congo  False  False
akm  marm1234  Arakanese (Marma)  21.5  92.5  Eurasia  Burmese-Lolo  Sino-Tibetan  False  False
chw  west2650  Cham (Western)  12.0  105.5  Eurasia  Malayo-Sumbawan  Austronesian  False  False
tla  kuan1248  Tolai  -4.25  152.083333333  Papunesia  Oceanic  Austronesian  False  False
mnk  east2426  Maninka  10.5  -9.5  Africa  Western Mande  Niger-Congo  False  False
lad  lada1244  Ladakhi  34.0  78.0  Eurasia  Bodic  Sino-Tibetan  False  True
arc  arch1244  Archi  42.0  46.8333333333  Eurasia  Lezgic  Nakh-Daghestanian  False  False
avo  avok1242  Avokaya  4.66666666667  30.0  Africa  Moru-Ma'di  Nilo-Saharan  False  False
lam  peve1243  Lamé  9.0  14.5  Africa  Masa  Afro-Asiatic  False  False
nbh  ghul1238  Ghulfan  12.0  31.0  Africa  Nubian  Nilo-Saharan  False  False
lot  loth1237  Lotha  26.5  94.25  Eurasia  Kuki-Chin  Sino-Tibetan  False  False
krq  kere1280  Kerek  62.25  175.0  Eurasia  Northern Chukotko-Kamchatkan  Chukotko-Kamchatkan  False  False
hal  hali1244  Halia  -5.25  154.666666667  Papunesia  Oceanic  Austronesian  False  False
nus  nusu1239  Nusu  26.75  99.0  Eurasia  Burmese-Lolo  Sino-Tibetan  False  False
nbk  natu1249  Natügu  -10.7833333333  165.866666667  Papunesia  Oceanic  Austronesian  False  False
knw  nort2951  Konkow  39.5  -121.5  North America  Maiduan  Penutian  False  False
dbd  tait1250  Dabida  -4.0  38.6666666667  Africa  Bantoid  Niger-Congo  False  False
aar  aari1239  Aari  6.0  36.5833333333  Africa  South Omotic  Afro-Asiatic  False  False
iqu  iqui1243  Iquito  -3.25  -74.0  South America  Zaparoan  Zaparoan  False  False
wau  woun1238  Waunana  4.0  -77.0  South America  Choco  Choco  False  False
djn  djin1253  Djinang  -12.3333333333  134.833333333  Australia  Pama-Nyungan  Australian  False  False
pip  pipi1250  Pipil  13.8333333333  -89.5833333333  North America  Aztecan  Uto-Aztecan  False  False
guj  guja1252  Gujarati  23.0  72.0  Eurasia  Indic  Indo-European  False  False
tru  trum1247  Trumai  -11.9166666667  -53.5833333333  South America  Trumai  Trumai  False  True
snm  sanu1240  Sanuma  4.5  -64.6666666667  South America  Yanomam  Yanomam  True  True
hin  hind1269  Hindi  25.0  77.0  Eurasia  Indic  Indo-European  True  True
mir  miri1266  Miriwung  -15.6666666667  129.0  Australia  Djeragan  Australian  False  False
zim  zima1244  Zimakani  -7.43333333333  141.433333333  Papunesia  Marind Proper  Marind  False  False
ono  onoo1246  Ono  -6.16666666667  147.583333333  Papunesia  Finisterre-Huon  Trans-New Guinea  False  False
maz  maza1293  Mazahua  19.4166666667  -99.9166666667  North America  Otomian  Oto-Manguean  False  False
kkt  koko1269  Kokota  -8.0  159.133333333  Papunesia  Oceanic  Austronesian  False  False
mcn  macu1260  Macuna  -0.333333333333  -70.1666666667  South America  Tucanoan  Tucanoan  False  False
wtm  wata1253  Watam  -3.91666666667  144.5  Papunesia  Lower Ramu  Lower Sepik-Ramu  False  False
ywr  yawu1244  Yawuru  -18.0  122.5  Australia  Nyulnyulan  Australian  False  False
apj  jica1244  Apache (Jicarilla)  36.5833333333  -104.0  North America  Athapaskan  Na-Dene  False  False
knn  kinn1249  Kinnauri  31.5  78.0  Eurasia  Bodic  Sino-Tibetan  False  False
lar  lara1258  Laragia  -12.6666666667  130.833333333  Australia  Laragiyan  Australian  False  False
mik  karb1241  Mikir  26.3333333333  93.5  Eurasia  Kuki-Chin  Sino-Tibetan  False  False
qta  nort2980  Quechua (Tarma)  -11.4166666667  -75.75  South America  Quechuan  Quechuan  False  False
urh  urho1239  Urhobo  5.58333333333  6.0  Africa  Edoid  Niger-Congo  False  False
ngw  ngaw1240  Ngawun  -19.0  141.5  Australia  Pama-Nyungan  Australian  False  False
gml  gami1243  Gamilaraay  -29.8333333333  149.5  Australia  Pama-Nyungan  Australian  False  False
abo  arbo1245  Arbore  5.0  36.75  Africa  Eastern Cushitic  Afro-Asiatic  False  False
bit  biat1246  Biatah  1.25  110.0  Papunesia  Land Dayak  Austronesian  False  False
crn  corn1251  Cornish  50.3333333333  -5.0  Eurasia  Celtic  Indo-European  False  False
mym  mala1464  Malayalam  10.0  76.5  Eurasia  Southern Dravidian  Dravidian  False  False
krk  karo1304  Karok  41.6666666667  -123.0  North America  Karok  Karok  True  True
wmn  weme1239  Wéménugbé  6.66666666667  2.5  Africa  Kwa  Niger-Congo  False  False
spi  tibe1272  Spitian  32.25  78.0  Eurasia  Bodic  Sino-Tibetan  False  False
msc  chib1270  Muisca  5.0  -74.0  South America  Chibchan Proper  Chibchan  False  False
chn  chan1310  Chantyal  28.5833333333  83.4166666667  Eurasia  Bodic  Sino-Tibetan  False  False
wlm  walm1241  Walmatjari  -19.5  125.75  Australia  Pama-Nyungan  Australian  False  False
kry  kory1246  Koryak  61.0  167.0  Eurasia  Northern Chukotko-Kamchatkan  Chukotko-Kamchatkan  False  False
abk  abkh1244  Abkhaz  43.0833333333  41.0  Eurasia  Northwest Caucasian  Northwest Caucasian  True  True
por  port1283  Portuguese  39.0  -8.0  Eurasia  Romance  Indo-European  False  False
yap  yape1248  Yapese  9.58333333333  138.166666667  Papunesia  Yapese  Austronesian  False  False
spo  spok1245  Spokane  47.6666666667  -117.75  North America  Interior Salish  Salishan  False  False
smn  cree1270  Seminole  33.0  -84.0  North America  Muskogean  Muskogean  False  False
nyn  nyig1240  Nyigina  -18.0  124.333333333  Australia  Nyulnyulan  Australian  False  False
bki  baka1277  Bakairí  -14.0  -55.0  South America  Cariban  Cariban  False  False
vaf  vafs1240  Vafsi  34.6666666667  49.9166666667  Eurasia  Iranian  Indo-European  False  False
aho  arap1274  Arapaho  40.0  -103.0  North America  Algonquian  Algic  False  False
gug  koka1244  Gugada  -30.0  134.0  Australia  Pama-Nyungan  Australian  False  False
abm  alab1237  Alabama  32.3333333333  -87.4166666667  North America  Muskogean  Muskogean  False  False
taf  sapo1253  Taiof  -5.53333333333  154.633333333  Papunesia  Oceanic  Austronesian  False  False
prk  puri1258  Purki  34.6666666667  76.0  Eurasia  Bodic  Sino-Tibetan  False  False
mon  monn1252  Mon  14.8333333333  100.5  Eurasia  Monic  Austro-Asiatic  False  False
car  gali1262  Carib  5.5  -56.0  South America  Cariban  Cariban  False  True
gna  guan1268  Guana  -22.0  -58.0  South America  Mascoian  Mascoian  False  False
pri  prin1242  Príncipense  1.61666666667  7.36666666667  Africa  Creoles and Pidgins  other  False  False
rov  rovi1238  Roviana  -8.25  157.333333333  Papunesia  Oceanic  Austronesian  False  False
crh  chru1239  Chru  11.5  108.5  Eurasia  Malayo-Sumbawan  Austronesian  False  False
lma  loma1260  Loma  8.0  -9.5  Africa  Western Mande  Niger-Congo  False  False
fox  mesk1242  Fox  43.0  -83.0  North America  Algonquian  Algic  False  False
cui  cuib1242  Cuiba  6.5  -70.0  South America  Guahiban  Guahiban  False  False
tpi  tokp1240  Tok Pisin  -9.5  147.166666667  Papunesia  Creoles and Pidgins  other  False  False
say  sayu1241  Sayultec  17.8333333333  -95.0  North America  Mixe-Zoque  Mixe-Zoque  False  False
bng  qaqe1238  Baining  -4.58333333333  152.0  Papunesia  Baining  Baining-Taulil  False  False
bub  bube1242  Bubi  3.5  8.66666666667  Africa  Bantoid  Niger-Congo  False  False
fon  fonn1241  Fongbe  6.41666666667  2.16666666667  Africa  Kwa  Niger-Congo  False  False
wyn  waya1269  Wayana  3.25  -54.1666666667  South America  Cariban  Cariban  False  False
mmo  moks1248  Mordvin (Moksha)  54.0  44.0  Eurasia  Mordvin  Uralic  False  False
ewe  ewee1241  Ewe  6.33333333333  0.416666666667  Africa  Kwa  Niger-Congo  False  True
hcr  hait1244  Haitian Creole  19.0  -72.5  North America  Creoles and Pidgins  other  False  False
bpb  bahn1262  Bahnar (Plei Bong-Mang Yang)  13.8333333333  108.333333333  Eurasia  Bahnaric  Austro-Asiatic  False  False
biu  bisu1246  Bisu  19.75  100.0  Eurasia  Burmese-Lolo  Sino-Tibetan  False  False
lye  lyel1241  Lyele  12.5  -2.66666666667  Africa  Gur  Niger-Congo  False  False
non  noon1243  Noni  6.41666666667  10.5833333333  Africa  Bantoid  Niger-Congo  False  False
cmh  utes1238  Chemehuevi  34.3333333333  -115.166666667  North America  Numic  Uto-Aztecan  False  False
deg  dege1246  Degema  4.75  6.75  Africa  Edoid  Niger-Congo  False  False
ned  dutc1253  Nederlandse Gebarentaal  52.25  5.5  Eurasia  Sign Languages  other  False  False
acl  acol1236  Acholi  3.0  32.6666666667  Africa  Nilotic  Nilo-Saharan  False  False
hua  yaga1260  Hua  -6.33333333333  145.333333333  Papunesia  Eastern Highlands  Trans-New Guinea  False  False
swe  swed1254  Swedish  60.0  15.0  Eurasia  Germanic  Indo-European  False  False
blc  east2304  Baluchi  28.0  62.0  Eurasia  Iranian  Indo-European  False  False
ter  tera1251  Tera  11.0  11.8333333333  Africa  Biu-Mandara  Afro-Asiatic  False  False
ocu  atzi1235  Ocuilteco  18.9166666667  -99.6666666667  North America  Otomian  Oto-Manguean  False  False
yay  bouy1240  Yay  22.4166666667  104.75  Eurasia  Kam-Tai  Tai-Kadai  False  False
udm  udmu1245  Udmurt  57.5  52.5  Eurasia  Permic  Uralic  False  False
nam  nami1256  Namia  -3.83333333333  141.75  Papunesia  Yellow River  Sepik  False  False
nug  nung1290  Nunggubuyu  -13.75  135.666666667  Australia  Nunggubuyu  Australian  False  True
shl  shil1265  Shilluk  9.66666666667  31.75  Africa  Nilotic  Nilo-Saharan  False  False
cct  choc1276  Choctaw  32.25  -88.5  North America  Muskogean  Muskogean  False  False
gny  guny1241  Gunya  -26.5  146.5  Australia  Pama-Nyungan  Australian  False  False
mdr  nucl1460  Madurese  -7.0  113.5  Papunesia  Malayo-Sumbawan  Austronesian  False  False
aja  ajas1235  Aja  7.33333333333  25.6666666667  Africa  Kresh  Nilo-Saharan  False  False
gol  gola1255  Gola  7.25  -10.8333333333  Africa  Southern Atlantic  Niger-Congo  False  False
mwc  mawc1242  Mawchi  21.3333333333  73.6666666667  Eurasia  Indic  Indo-European  False  False
mms  mama1276  Mamasa  -3.08333333333  119.666666667  Papunesia  South Sulawesi  Austronesian  False  False
jmm  jama1261  Jamamadi  -7.5  -67.0  South America  Arauan  Arauan  False  False
chi  chim1301  Chimariko  41.0  -123.0  North America  Chimariko  Hokan  False  False
iss  isra1236  Israeli Sign Language  32.0  34.8333333333  Eurasia  Sign Languages  other  False  False
sur  surs1246  Sursurunga  -4.0  152.766666667  Papunesia  Oceanic  Austronesian  False  False
shd  sher1257  Sherdukpen  27.0  92.5  Eurasia  Western Arunachal  Sino-Tibetan  False  False
mla  nige1255  Mambila  6.75  11.5  Africa  Bantoid  Niger-Congo  False  False
brl  lowa1242  Baragaunle  28.8333333333  83.8333333333  Eurasia  Bodic  Sino-Tibetan  False  False
crk  cree1270  Creek  34.0  -85.0  North America  Muskogean  Muskogean  False  False
wor  woro1255  Worora  -15.6666666667  124.666666667  Australia  Wororan  Australian  False  False
kjo  coas1295  Konjo  -5.46666666667  120.333333333  Papunesia  South Sulawesi  Austronesian  False  False
pem  pemo1248  Pemon  5.33333333333  -62.0  South America  Cariban  Cariban  False  False
jpr  japr1238  Japreria  10.5  -73.0  South America  Cariban  Cariban  False  False
tli  tlin1245  Tlingit  59.0  -135.0  North America  Tlingit  Na-Dene  False  True
olm  ngaj1237  Oloh Mangtangai  -0.833333333333  113.0  Papunesia  Barito  Austronesian  False  False
taj  taji1245  Tajik  38.6666666667  70.0  Eurasia  Iranian  Indo-European  False  False
jwr  jama1261  Jarawara  -7.5  -65.5  South America  Arauan  Arauan  False  False
wed  weda1241  Wedau  -10.1666666667  150.166666667  Papunesia  Oceanic  Austronesian  False  False
dge  germ1281  Deutsche Gebärdensprache  52.0  11.0  Eurasia  Sign Languages  other  False  False
lgu  long1395  Longgu  -9.75  160.666666667  Papunesia  Oceanic  Austronesian  False  False
koi  gras1249  Koiari  -9.5  147.333333333  Papunesia  Koiarian  Trans-New Guinea  False  False
udi  udii1243  Udi  41.0  48.0  Eurasia  Lezgic  Nakh-Daghestanian  False  False
tga  tang1348  Tangga  -3.46666666667  153.2  Papunesia  Oceanic  Austronesian  False  False
diy  dier1241  Diyari  -28.0  139.0  Australia  Pama-Nyungan  Australian  False  False
sen  nucl1396  Sena  -18.0  35.25  Africa  Bantoid  Niger-Congo  False  False
tul  tulu1258  Tulu  12.75  75.3333333333  Eurasia  Southern Dravidian  Dravidian  False  False
tnj  tana1289  Tanaina  62.0  -150.0  North America  Athapaskan  Na-Dene  False  False
iat  iatm1242  Iatmul  -4.25  143.25  Papunesia  Middle Sepik  Sepik  False  False
tml  tami1289  Tamil  11.0  78.5  Eurasia  Southern Dravidian  Dravidian  False  False
knc  kuku1280  Kugu Nganhcara  -14.4166666667  142.0  Australia  Pama-Nyungan  Australian  False  False
uri  urim1252  Urim  -3.58333333333  142.666666667  Papunesia  Urim  Torricelli  False  False
bai  cent2004  Bai  26.0  100.0  Eurasia  Bai  Sino-Tibetan  False  False
frd  ford1242  Fordata  -6.75  131.5  Papunesia  Central Malayo-Polynesian  Austronesian  False  False
ndb  sout2808  Ndebele (in South Africa)  -25.3333333333  29.0  Africa  Bantoid  Niger-Congo  False  False
mcf  mich1243  Michif  52.0  -100.166666667  North America  Algonquian  Algic  False  False
krn  kora1292  Korana  -29.5  20.5  Africa  Central Khoisan  Khoisan  False  False
kew  kewa1250  Kewa  -6.5  143.833333333  Papunesia  Engan  Trans-New Guinea  True  True
mnj  mart1256  Mantjiltjara  -22.6666666667  125.083333333  Australia  Pama-Nyungan  Australian  False  False
ngn  ngan1295  Ngandi  -13.8333333333  135.0  Australia  Ngandi  Australian  False  False
khs  khas1269  Khasi  25.5  92.0  Eurasia  Khasian  Austro-Asiatic  False  True
klk  kuoo1238  Koh (Lakka)  8.0  15.5  Africa  Adamawa  Niger-Congo  False  False
wel  wels1247  Welsh  52.0  -3.0  Eurasia  Celtic  Indo-European  False  False
oya  nucl1284  Oriya  21.0  85.0  Eurasia  Indic  Indo-European  False  False
sme  siam1242  Seme  11.0  -4.91666666667  Africa  Kru  Niger-Congo  False  False
sae  saek1240  Saek  17.4166666667  104.75  Eurasia  Kam-Tai  Tai-Kadai  False  False
mgh  maga1260  Magahi  23.5  85.5  Eurasia  Indic  Indo-European  False  False
tty  tatu1247  Tatuyo  0.416666666667  -70.5  South America  Tucanoan  Tucanoan  False  False
hli  halk1245  Halkomelem (Island)  49.2  -123.0  North America  Central Salish  Salishan  False  False
guf  gupa1247  Gupapuyngu  -12.0  136.0  Australia  Pama-Nyungan  Australian  False  False
kyt  kayt1238  Kaytej  -21.0  134.0  Australia  Pama-Nyungan  Australian  False  False
wru  waru1265  Warumungu  -19.5  134.5  Australia  Pama-Nyungan  Australian  False  False
wec  wels1247  Welsh (Colloquial)  52.75  -3.5833  Eurasia  Celtic  Indo-European  False  False
wna  wann1242  Wan  7.83333333333  -5.86666666667  Africa  Eastern Mande  Niger-Congo  False  False
ddj  godi1239  Dadjriwalé  5.25  -5.66666666667  Africa  Kru  Niger-Congo  False  False
jms  jams1239  Jamsay  14.4166666667  -2.5  Africa  Dogon  Niger-Congo  False  False
mnz  monz1249  Munzombo  3.0  18.4166666667  Africa  Ubangi  Niger-Congo  False  False
sku  suku1259  Suku  -6.0  17.6666666667  Africa  Bantoid  Niger-Congo  False  False
bgm  bang1363  Bangime  14.9166666667  -3.83333333333  Africa  Bangime  Bangime  False  False
tsk  tama1365  Tamashek  20.0  -2.0  Africa  Berber  Afro-Asiatic  False  False
ryu  cent2126  Shuri  26.5  127.5  Eurasia  Japanese  Japanese  False  False
kgy  kyer1238  Kyirong  28.4166666667  85.3333333333  Eurasia  Bodic  Sino-Tibetan  False  False
lic  hlai1239  Hlai (Baoding)  19.0  109.5  Eurasia  Hlai  Tai-Kadai  False  False
bgz  bong1289  Banggi  7.25  117.166666667  Papunesia  Barito  Austronesian  False  False
fqs  fass1245  Momu  -3.0  141.583333333  Papunesia  Fas  Kwomtari-Baibai  False  False
bio  naii1241  Nai  -3.71666666667  141.266666667  Papunesia  Kwomtari  Kwomtari-Baibai  False  False
owi  owin1240  Owininga  -4.5  141.75  Papunesia  Left May  Left May  False  False
inn  yand1253  Innamincka  -27.75  140.75  Australia  Pama-Nyungan  Australian  False  False
msq  halk1245  Musqueam  49.1666666667  -123.0  North America  Central Salish  Salishan  False  False
qum  sipa1247  Sipakapense  15.25  -91.75  North America  Mayan  Mayan  False  False
eme  emer1243  Émérillon  3.16666666667  -52.4166666667  South America  Tupi-Guaraní  Tupian  False  False
kkq  kuik1246  Kuikúro  -12.4166666667  -53.0833333333  South America  Cariban  Cariban  False  False
ige  iged1239  Igede  7.0  8.16666666667  Africa  Idomoid  Niger-Congo  False  False
gil  gila1241  Gilaki  37.3333333333  50.0  Eurasia  Iranian  Indo-European  False  False
ord  peri1253  Ordos  39.0  109.0  Eurasia  Mongolic  Altaic  False  False
kom  komo1258  Komo  8.75  33.75  Africa  Koman  Nilo-Saharan  False  False
mae  maee1241  Mae  -16.0  167.25  Papunesia  Oceanic  Austronesian  False  False
bin  bina1277  Binandere  -8.25  148.0  Papunesia  Binanderean  Trans-New Guinea  False  False
ega  egaa1242  Ega  5.5  -5.5  Africa  Kwa  Niger-Congo  False  False
gud  gude1246  Gude  10.4166666667  13.4166666667  Africa  Biu-Mandara  Afro-Asiatic  False  False
pta  dumb1241  Paita  -22.0833333333  166.5  Papunesia  Oceanic  Austronesian  False  False
aiz  apro1235  Aizi  5.25  -4.5  Africa  Kru  Niger-Congo  False  False
vat  lako1244  Vata  5.83333333333  -5.41666666667  Africa  Kru  Niger-Congo  False  False
nim  nucl1633  Nimboran  -2.5  140.166666667  Papunesia  Nimboran  Nimboran  False  False
bil  bilu1245  Bilua  -7.75  156.666666667  Papunesia  Bilua  Solomons East Papuan  False  False
hno  nort2938  Haida (Northern)  54.0  -132.5  North America  Haida  Haida  False  False
guh  guhu1244  Guhu-Samane  -8.0  147.333333333  Papunesia  Binanderean  Trans-New Guinea  False  False
kwm  kwaa1269  Kwami  10.4166666667  11.0  Africa  West Chadic  Afro-Asiatic  False  False
iga  inga1252  Inga  1.0  -77.0  South America  Quechuan  Quechuan  False  False
sir  siar1238  Siar  -4.66666666667  152.916666667  Papunesia  Oceanic  Austronesian  False  False
mru  maru1249  Maru  23.5  98.5  Eurasia  Burmese-Lolo  Sino-Tibetan  False  False
ctw  cata1286  Catawba  35.5  -80.5  North America  Siouan  Siouan  False  False
wrm  ware1253  Warembori  -1.66666666667  137.583333333  Papunesia  South Halmahera - West New Guinea  Austronesian  False  False
gon  sout2711  Gondi  19.0  81.0  Eurasia  South-Central Dravidian  Dravidian  False  False
png  pang1287  Pangwa  -10.0  34.75  Africa  Bantoid  Niger-Congo  False  False
dmi  dumi1241  Dumi  27.25  86.6666666667  Eurasia  Mahakiranti  Sino-Tibetan  False  False
pga  pila1245  Pilagá  -25.0  -60.0  South America  Guaicuruan  Guaicuruan  False  False
djr  jaru1254  Djaru  -18.75  128.0  Australia  Pama-Nyungan  Australian  False  False
ygn  yagn1238  Yaghnobi  39.0  69.0  Eurasia  Iranian  Indo-European  False  False
kgu  kalk1246  Kalkatungu  -21.0  139.5  Australia  Pama-Nyungan  Australian  False  False
goj  guja1253  Gojri  32.75  76.25  Eurasia  Indic  Indo-European  False  False
amn  aman1265  Amanab  -3.58333333333  141.25  Papunesia  Border  Border  False  False
bri  brib1243  Bribri  9.41666666667  -83.0  North America  Talamanca  Chibchan  False  True
sti  stie1250  Stieng  11.8333333333  106.75  Eurasia  Bahnaric  Austro-Asiatic  False  False
boa  kuni1265  Boazi  -7.0  141.333333333  Papunesia  Marind Proper  Marind  False  False
dyu  dyul1238  Dyula  9.83333333333  -4.66666666667  Africa  Western Mande  Niger-Congo  False  False
nnk  nank1250  Nankina  -5.78333333333  146.45  Papunesia  Finisterre-Huon  Trans-New Guinea  False  False
trm  suri1267  Tirmaga  5.75  35.25  Africa  Surmic  Nilo-Saharan  False  False
fli  west2454  Ful (Liptako)  13.5  0.5  Africa  Northern Atlantic  Niger-Congo  False  False
nev  toho1245  Nevome  31.0  -112.5  North America  Tepiman  Uto-Aztecan  False  False
ada  adam1238  Adamorobe Sign Language  5.83333333333  -0.166666666667  Africa  Sign Languages  other  False  False
cur  curr1243  Curripaco  2.5  -68.5  South America  Northern Arawakan  Arawakan  False  False
kmb  ndei1235  Kombai  -5.58333333333  140.0  Papunesia  Awju-Dumut  Trans-New Guinea  False  False
bnb  buna1275  Bunuba  -17.75  125.75  Australia  Bunuban  Australian  False  True
bnd  band1352  Bandi  8.08333333333  -10.25  Africa  Western Mande  Niger-Congo  False  False
alx  bata1292  Alas  3.66666666667  97.8333333333  Papunesia  Northwest Sumatra-Barrier Islands  Austronesian  False  False
ssl  kore1273  South Korean Sign Language  37.0  128.0  Eurasia  Sign Languages  other  False  False
pol  poli1260  Polish  52.0  20.0  Eurasia  Slavic  Indo-European  False  False
obo  obol1243  Obolo  4.58333333333  7.83333333333  Africa  Cross River  Niger-Congo  False  False
gut  gour1243  Gurma (Togo)  10.75  0.666666666667  Africa  Gur  Niger-Congo  False  False
mnx  manx1243  Manx  54.1666666667  -4.5  Eurasia  Celtic  Indo-European  False  False
jrn  juru1256  Juruna  -5.0  -54.5  South America  Tupi-Guaraní  Tupian  False  False
ago  ango1258  Angolar  0.25  6.5  Africa  Creoles and Pidgins  other  False  False
cab  cabe1245  Cabécar  9.75  -83.4166666667  North America  Talamanca  Chibchan  False  False
shn  shon1251  Shona  -18.0  31.0  Africa  Bantoid  Niger-Congo  False  False
als  alse1251  Alsea  44.6666666667  -123.916666667  North America  Alsea  Oregon Coast  False  False
vla  vlaa1235  Vlaamse Gebarentaal  51.0  4.0  Eurasia  Sign Languages  other  False  False
mro  moro1285  Moro  11.0  30.1666666667  Africa  Heiban  Niger-Congo  False  False
ory  orya1242  Orya  -2.75  139.833333333  Papunesia  Orya  Tor-Orya  False  False
lah  lahu1253  Lahu  20.0  98.1666666667  Eurasia  Burmese-Lolo  Sino-Tibetan  False  False
bis  biss1248  Bisa  11.5  -0.5  Africa  Eastern Mande  Niger-Congo  False  False
que  quec1382  Quechan  32.8333333333  -114.333333333  North America  Yuman  Hokan  False  False
dgo  dong1290  Dongo  3.0  30.0  Africa  Ubangi  Niger-Congo  False  False
aln  alun1238  Alune  -3.0  128.333333333  Papunesia  Central Malayo-Polynesian  Austronesian  False  False
akr  arik1262  Arikara  45.5  -100.5  North America  Caddoan  Caddoan  False  False
khg  khal1275  Khaling  27.5  86.6666666667  Eurasia  Mahakiranti  Sino-Tibetan  False  False
khk  khak1248  Khakas  53.0  90.0  Eurasia  Turkic  Altaic  False  False
hau  haus1257  Hausa  12.0  7.0  Africa  West Chadic  Afro-Asiatic  True  True
chg  chan1313  Chang  26.3333333333  94.75  Eurasia  Northern Naga  Sino-Tibetan  False  False
bat  bata1301  Batak  10.25  119.083333333  Papunesia  Greater Central Philippine  Austronesian  False  False
crt  chor1274  Chorote  -22.5  -62.5  South America  Matacoan  Matacoan  False  False
uld  wuzl1236  Uldeme  10.95  14.1166666667  Africa  Biu-Mandara  Afro-Asiatic  False  False
tgb  tagb1258  Tagbanwa (Aborlan)  9.5  118.5  Papunesia  Greater Central Philippine  Austronesian  False  False
pgl  ping1243  Pingilapese  6.21666666667  160.7  Papunesia  Oceanic  Austronesian  False  False
akh  akha1245  Akha  21.8333333333  99.8333333333  Eurasia  Burmese-Lolo  Sino-Tibetan  False  False
yrr  pume1238  Yaruro  7.0  -68.0  South America  Yaruro  Yaruro  False  False
srb  sorb1249  Sorbian  51.5  14.0  Eurasia  Slavic  Indo-European  False  False
wn  wikn1245  Wik Ngathana  -13.9166666667  141.5  Australia  Pama-Nyungan  Australian  False  False
tgn  tugu1245  Tugun  -7.71666666667  126.75  Papunesia  Central Malayo-Polynesian  Austronesian  False  False
krw  koro1312  Korowai  -5.25  140.0  Papunesia  Awju-Dumut  Trans-New Guinea  False  False
ise  isek1239  Isekiri  5.66666666667  5.5  Africa  Defoid  Niger-Congo  False  False
cma  chim1309  Chimila  10.0  -74.0  South America  Chimila  Chibchan  False  False
nph  narp1239  Nar-Phu  28.6666666667  84.25  Eurasia  Bodic  Sino-Tibetan  False  False
plg  nucl1291  Palaung  22.6666666667  96.6666666667  Eurasia  Palaung-Khmuic  Austro-Asiatic  False  False
brh  brah1256  Brahui  28.5  67.0  Eurasia  Northern Dravidian  Dravidian  False  True
laz  lazz1240  Laz  41.5  41.5  Eurasia  Kartvelian  Kartvelian  False  False
mop  mopa1243  Mopan  16.5833333333  -88.6666666667  North America  Mayan  Mayan  False  False
urm  urum1249  Urum  47.1166666667  37.55  Eurasia  Turkic  Altaic  False  False
lsb  braz1236  Língua de Sinais Brasileira  -15.0  -48.0  South America  Sign Languages  other  False  False
tid  tido1248  Tidore  0.75  127.5  Papunesia  North Halmaheran  West Papuan  False  False
oji  east2542  Ojibwa (Eastern)  46.0  -80.0  North America  Algonquian  Algic  False  False
bfi  bafi1243  Bafia  5.0  11.1666666667  Africa  Bantoid  Niger-Congo  False  False
tiv  tivv1240  Tiv  7.5  9.0  Africa  Bantoid  Niger-Congo  False  False
ktb  kitu1246  Kituba  -5.0  17.5  Africa  Creoles and Pidgins  other  False  False
psl  plai1235  Plains-Indians Sign Language  40.0  -100.0  North America  Sign Languages  other  False  False
tsi  nucl1649  Tsimshian (Coast)  52.5  -129.0  North America  Tsimshianic  Penutian  False  True
ywl  yoku1256  Yawelmani  35.4166666667  -119.0  North America  Yokuts  Penutian  False  False
bsl  brit1235  British Sign Language  52.0  -1.0  Eurasia  Sign Languages  other  False  False
abi  abip1241  Abipón  -29.0  -61.0  South America  Guaicuruan  Guaicuruan  False  True
naf  nafa1258  Nafaanra  8.0  -2.58333333333  Africa  Gur  Niger-Congo  False  False
hnn  hanu1241  Hanunóo  12.3333333333  121.25  Papunesia  Greater Central Philippine  Austronesian  False  False
bad  bade1248  Bade  12.8333333333  10.5  Africa  West Chadic  Afro-Asiatic  False  False
grm  gour1243  Gurma  12.25  1.0  Africa  Gur  Niger-Congo  False  False
tor  rata1244  Toratán  1.08333333333  124.833333333  Papunesia  Sangiric  Austronesian  False  False
auy  awiy1238  Auyana  -6.5  145.75  Papunesia  Eastern Highlands  Trans-New Guinea  False  False
yar  yare1248  Yareba  -9.5  148.5  Papunesia  Yareban  Yareban  False  False
sum  sumo1243  Sumu  13.0  -84.5  North America  Misumalpan  Misumalpan  False  False
ron  ronn1241  Ron  9.0  8.75  Africa  West Chadic  Afro-Asiatic  False  False
mts  mati1255  Matis  -4.41666666667  -70.25  South America  Panoan  Panoan  False  False
iaa  iaai1238  Iaai  -20.4166666667  166.583333333  Papunesia  Oceanic  Austronesian  False  False
isi  isir1237  Isirawa  -1.83333333333  138.5  Papunesia  Kwerba  Kwerba  False  False
ksu  kash1274  Kashubian  54.0  18.0  Eurasia  Slavic  Indo-European  False  False
for  fore1270  Fore  -6.75  145.5  Papunesia  Eastern Highlands  Trans-New Guinea  False  False
rru  nyor1246  Runyoro-Rutooro  1.5  31.3333333333  Africa  Bantoid  Niger-Congo  False  False
adi  adio1239  Adioukrou  5.41666666667  -4.58333333333  Africa  Kwa  Niger-Congo  False  False
nua  nuau1240  Nuaulu  -3.25  129.166666667  Papunesia  Central Malayo-Polynesian  Austronesian  False  False
moj  moha1256  Mojave  34.6666666667  -114.583333333  North America  Yuman  Hokan  False  False
sru  sela1259  Selaru  -8.2  131.0  Papunesia  Central Malayo-Polynesian  Austronesian  False  False
swi  sawa1247  Sawai  0.5  128.0  Papunesia  South Halmahera - West New Guinea  Austronesian  False  False
nas  naas1242  Nasioi  -6.33333333333  155.583333333  Papunesia  East Bougainville  East Bougainville  False  False
com  maor1244  Comorian  -12.0  44.0  Africa  Bantoid  Niger-Congo  False  False
kac  kach1279  Kachari  26.5  91.0  Eurasia  Bodo-Garo  Sino-Tibetan  False  False
jar  jara1263  Jarawa (in Nigeria)  9.5  10.5  Africa  Bantoid  Niger-Congo  False  False
urk  urub1250  Urubú-Kaapor  -2.33333333333  -46.5  South America  Tupi-Guaraní  Tupian  False  True
cai  suri1267  Chai  5.33333333333  35.3333333333  Africa  Surmic  Nilo-Saharan  False  False
pin  pint1250  Pintupi  -23.0  129.0  Australia  Pama-Nyungan  Australian  False  False
apt  apat1240  Apatani  27.5  93.75  Eurasia  Tani  Sino-Tibetan  False  False
som  soma1255  Somali  3.0  45.0  Africa  Eastern Cushitic  Afro-Asiatic  False  False
nzs  newz1236  New Zealand Sign Language  -43.0  172.0  Papunesia  Sign Languages  other  False  False
ngb  ngba1285  Ngbaka (Minagende)  3.5  20.0  Africa  Gbaya-Manza-Ngbaka  Niger-Congo  False  False
hai  haid1248  Haida  53.0  -132.0  North America  Haida  Haida  False  True
ojs  seve1240  Ojibwa (Severn)  53.0  -90.0  North America  Algonquian  Algic  False  False
mic  mikm1235  Micmac  45.0  -63.0  North America  Algonquian  Algic  False  False
cpn  chep1245  Chepang  27.6666666667  84.75  Eurasia  Mahakiranti  Sino-Tibetan  False  False
dar  dara1250  Darai  24.0  84.0  Eurasia  Indic  Indo-European  False  False
qcu  cusc1236  Quechua (Cuzco)  -14.5  -71.0  South America  Quechuan  Quechuan  False  False
wic  wich1260  Wichita  33.3333333333  -97.3333333333  North America  Caddoan  Caddoan  True  True
pod  park1239  Podoko  11.0  14.0833333333  Africa  Biu-Mandara  Afro-Asiatic  False  False
svc  kash1274  Slovincian  54.0  16.0  Eurasia  Slavic  Indo-European  False  False
kan  khan1278  Kana  4.75  7.41666666667  Africa  Cross River  Niger-Congo  False  False
tha  thai1261  Thai  16.0  101.0  Eurasia  Kam-Tai  Tai-Kadai  True  True
kon  koon1244  Kongo  -5.0  15.0  Africa  Bantoid  Niger-Congo  False  True
mol  roma1327  Moldavian  47.0  29.0  Eurasia  Romance  Indo-European  False  False
ngi  wang1291  Ngiyambaa  -31.75  145.5  Australia  Pama-Nyungan  Australian  True  True
sui  suii1243  Sui  26.0  107.5  Eurasia  Kam-Tai  Tai-Kadai  False  False
lng  leng1262  Lengua  -22.5  -59.0  South America  Mascoian  Mascoian  False  False
tki  tuki1240  Tuki  4.58333333333  11.5  Africa  Bantoid  Niger-Congo  False  False
tif  tifa1245  Tifal  -5.0  141.333333333  Papunesia  Ok  Trans-New Guinea  False  False
col  chol1281  Chol  17.75  -92.5  North America  Mayan  Mayan  False  False
ppc  piap1246  Piapoco  4.0  -69.5  South America  Northern Arawakan  Arawakan  False  False
trn  tere1279  Terêna  -20.0  -56.0  South America  Bolivia-Parana  Arawakan  False  False
hui  huic1243  Huichol  22.0  -104.0  North America  Corachol  Uto-Aztecan  False  False
kly  kala1377  Kala Lagaw Ya  -10.1166666667  142.116666667  Papunesia  Pama-Nyungan  Australian  False  False
ond  onei1249  Oneida  43.0  -75.6666666667  North America  Northern Iroquoian  Iroquoian  True  True
vas  vasa1239  Vasavi  24.5  71.5  Eurasia  Indic  Indo-European  False  False
dun  duna1248  Duna  -5.5  142.5  Papunesia  Duna  Trans-New Guinea  False  False
nkk  naka1260  Nakkara  -12.1166666667  134.416666667  Australia  Nakkara  Australian  False  False
nat  natc1249  Natchez  31.75  -91.3333333333  North America  Natchez  Natchez  False  False
mrc  rong1264  Marchha  30.25  79.5833333333  Eurasia  Bodic  Sino-Tibetan  False  False
tye  tyar1236  Tyeraity  -13.0  130.333333333  Australia  Northern Daly  Australian  False  False
ata  atay1247  Atayal  24.5  121.333333333  Papunesia  Atayalic  Austronesian  False  False
kas  kash1277  Kashmiri  34.0  76.0  Eurasia  Indic  Indo-European  False  False
ebi  ebir1243  Ebira  8.16666666667  7.0  Africa  Nupoid  Niger-Congo  False  False
kob  kobo1249  Kobon  -5.16666666667  144.333333333  Papunesia  Madang  Trans-New Guinea  False  True
kel  kele1258  Kele  -2.08333333333  147.083333333  Papunesia  Oceanic  Austronesian  False  False
wgu  waru1264  Warrungu  -18.0  145.0  Australia  Pama-Nyungan  Australian  False  False
sik  sika1262  Sika  -8.7  122.25  Papunesia  Central Malayo-Polynesian  Austronesian  False  False
slo  slov1268  Slovene  46.0  15.0  Eurasia  Slavic  Indo-European  False  False
atb  aral1243  Aralle-Tabulahan  -2.75  119.25  Papunesia  South Sulawesi  Austronesian  False  False
muo  muon1246  Muong  20.5  105.083333333  Eurasia  Viet-Muong  Austro-Asiatic  False  True
lac  laca1243  Lacandón  17.0  -91.5  North America  Mayan  Mayan  False  False
min  mina1268  Minangkabau  -1.0  101.0  Papunesia  Malayo-Sumbawan  Austronesian  False  False
wai  waiw1244  Wai Wai  1.0  -59.0  South America  Cariban  Cariban  False  False
hlb  halb1244  Halbi  21.0  81.0  Eurasia  Indic  Indo-European  False  False
loz  lozi1239  Lozi  -17.8333333333  26.0  Africa  Bantoid  Niger-Congo  False  False
mgn  magu1243  Magindanao  6.83333333333  124.5  Papunesia  Greater Central Philippine  Austronesian  False  False
buy  buli1254  Buli (in Ghana)  10.5  -1.25  Africa  Gur  Niger-Congo  False  False
kaa  karo1305  Karó (Arára)  -10.3333333333  -62.0  South America  Ramarama  Tupian  False  False
lan  lang1324  Lango  2.16666666667  33.0  Africa  Nilotic  Nilo-Saharan  True  True
kuq  kumy1244  Kumyk  43.0  47.3333333333  Eurasia  Turkic  Altaic  False  False
bmb  bimo1239  Bimoba  10.5  0.0  Africa  Gur  Niger-Congo  False  False
yir  yiry1245  Yir Yiront  -14.8333333333  141.833333333  Australia  Pama-Nyungan  Australian  False  False
suk  suki1245  Suki  -8.0  141.75  Papunesia  Suki  Gogodala-Suki  False  False
kbo  apma1241  Kambot  -4.25  144.133333333  Papunesia  Botin  Lower Sepik-Ramu  False  False
nte  norw1255  Norsk Tegnspråk  61.0  9.0  Eurasia  Sign Languages  other  False  False
lml  nucl1327  Limilngan  -12.5  131.916666667  Australia  Limilngan  Australian  False  False
lis  lisu1250  Lisu  26.0  98.0  Eurasia  Burmese-Lolo  Sino-Tibetan  False  False
blt  balt1258  Balti  35.0  76.0  Eurasia  Bodic  Sino-Tibetan  False  False
dyi  dyir1250  Dyirbal  -17.8333333333  145.583333333  Australia  Pama-Nyungan  Australian  False  False
ila  ilaa1246  Ila  -15.5833333333  26.5  Africa  Bantoid  Niger-Congo  False  False
sto  ston1242  Stoney  53.75  -116.5  North America  Siouan  Siouan  False  False
ved  vedd1240  Vedda  7.0  81.0  Eurasia  Indic  Indo-European  False  False
amo  amoo1242  Amo  10.3333333333  8.66666666667  Africa  Kainji  Niger-Congo  False  False
git  gitx1241  Gitksan  55.3333333333  -127.75  North America  Tsimshianic  Penutian  False  False
chh  seba1251  Chaha  8.112935  37.93267  Africa  Semitic  Afro-Asiatic  False  False
eko  koti1238  Ekoti  -16.5  39.5  Africa  Bantoid  Niger-Congo  False  False
sge  song1303  Songe  -6.83333333333  22.0  Africa  Bantoid  Niger-Congo  False  False
gav  gavi1246  Gavião  -10.6666666667  -62.0  South America  Monde  Tupian  False  False
buu  buru1303  Buru  -3.5  126.5  Papunesia  Central Malayo-Polynesian  Austronesian  False  False
jav  java1254  Javanese  -7.0  111.0  Papunesia  Javanese  Austronesian  False  False
ane  anem1249  Anêm  -5.58333333333  149.083333333  Papunesia  Anêm  Anêm  False  False
bgi  bagr1243  Bagri  29.5833333333  74.3333333333  Eurasia  Indic  Indo-European  False  False
tik  tika1246  Tikar  5.83333333333  11.6666666667  Africa  Bantoid  Niger-Congo  False  False
fas  fasu1242  Fasu  -6.58333333333  143.333333333  Papunesia  Fasu  Trans-New Guinea  False  False
yki  yuki1243  Yuki  39.6666666667  -123.5  North America  Yukian  Wappo-Yukian  False  False
trw  torw1241  Torwali  34.25  72.0  Eurasia  Indic  Indo-European  False  False
cmc  come1251  Comecrudo  25.8333333333  -99.0  North America  Comecrudan  Comecrudan  False  False
bsr  bass1258  Basari  12.6666666667  -13.0  Africa  Northern Atlantic  Niger-Congo  False  False
tsw  tswa1253  Tswana  -24.0  26.0  Africa  Bantoid  Niger-Congo  False  False
bxj  bayu1240  Bayungu  -23.0  114.0  Australia  Pama-Nyungan  Australian  False  False
ggd  guga1239  Gugadj  -18.5  140.5  Australia  Pama-Nyungan  Australian  False  False
mrj  ngad1258  Mirniny  -31.0  129.0  Australia  Pama-Nyungan  Australian  False  False
wkw  waka1274  Wagawaga  -26.5  152.5  Australia  Pama-Nyungan  Australian  False  False
agb  legb1242  Leggbó  6.0  8.0  Africa  Cross River  Niger-Congo  False  False
ncm  ntch1242  Ncàm  9.33333333333  0.666666666667  Africa  Gur  Niger-Congo  False  False
knz  kham1282  Kham (Tibetan) (Nangchen)  32.5  96.5  Eurasia  Bodic  Sino-Tibetan  False  False
khd  kham1282  Kham (Dege)  31.8333333333  98.5833333333  Eurasia  Bodic  Sino-Tibetan  False  False
xns  kana1283  Kanashi  32.0833333333  77.25  Eurasia  Bodic  Sino-Tibetan  False  False
agd  dupa1235  Agta (Dupaningan)  18.0  122.083333333  Papunesia  Greater Central Philippine  Austronesian  False  False
bwc  west2560  Bajau (West Coast)  6.33333333333  116.333333333  Papunesia  Sama-Bajaw  Austronesian  False  False
psw  port1285  Port Sandwich  -16.5  167.75  Papunesia  Oceanic  Austronesian  False  False
lmu  lame1260  Lamen  -16.5833333333  168.166666667  Papunesia  Oceanic  Austronesian  False  False
bhu  mund1320  Bhumij  21.3333333333  86.5  Eurasia  Munda  Austro-Asiatic  False  False
sah  sahu1245  Sahu  1.16666666667  127.5  Papunesia  North Halmaheran  West Papuan  False  False
khr  khar1287  Kharia  22.5  84.3333333333  Eurasia  Munda  Austro-Asiatic  False  False
yal  kosa1249  Yale (Kosarek)  -4.08333333333  139.5  Papunesia  Mek  Trans-New Guinea  False  False
ktc  katc1249  Katcha  10.8333333333  29.6666666667  Africa  Kadugli  Kadugli  False  False
nmd  samo1303  Nomad  -6.16666666667  142.25  Papunesia  East Strickland  East Strickland  False  False
gla  gela1261  Gelao  22.9166666667  105.5  Eurasia  Kadai  Tai-Kadai  False  False
kuz  mati1250  Kulamanen  7.75  125.0  Papunesia  Greater Central Philippine  Austronesian  False  False
swt  swat1243  Swati  -26.5  31.0  Africa  Bantoid  Niger-Congo  False  False
den  deni1241  Dení  -6.0  -67.0  South America  Arauan  Arauan  False  False
kit  kits1249  Kitsai  31.8333333333  -96.5  North America  Caddoan  Caddoan  False  False
blq  nucl1695  Bole  11.3333333333  11.25  Africa  West Chadic  Afro-Asiatic  False  False
mhk  mehe1243  Mehek  -3.75  142.5  Papunesia  Tama Sepik  Sepik  False  False
mmp  mamp1244  Mampruli  10.3333333333  -0.666666666667  Africa  Gur  Niger-Congo  False  False
mpy  mapo1246  Mapoyo  6.0  -67.0  South America  Cariban  Cariban  False  False
wiy  wiyo1248  Wiyot  40.8333333333  -124.166666667  North America  Wiyot  Algic  False  False
nke  nkem1242  Nkem  6.58333333333  8.58333333333  Africa  Bantoid  Niger-Congo  False  False
tnd  tind1238  Tindi  42.3666666667  46.25  Eurasia  Avar-Andic-Tsezic  Nakh-Daghestanian  False  False
hop  hopi1249  Hopi  36.0  -110.0  North America  Hopi  Uto-Aztecan  False  False
yav  hava1248  Yavapai  34.0  -113.333333333  North America  Yuman  Hokan  False  False
bia  bila1255  Bira  1.0  28.75  Africa  Bantoid  Niger-Congo  False  False
ald  alla1248  Alladian  5.16666666667  -4.33333333333  Africa  Kwa  Niger-Congo  False  False
kym  nort2690  Krymchak  45.0  34.25  Eurasia  Turkic  Altaic  False  False
usl  urub1243  Urubú Sign Language  -2.33333333333  -46.0  South America  Sign Languages  other  False  False
nza  nzak1247  Nzakara  5.0  23.0  Africa  Ubangi  Niger-Congo  False  False
kls  kali1308  Kalispel  48.0  -117.0  North America  Interior Salish  Salishan  False  False
ana  arao1248  Araona  -12.3333333333  -67.75  South America  Tacanan  Tacanan  False  True
bru  east2332  Bru (Eastern)  17.3333333333  106.0  Eurasia  Katuic  Austro-Asiatic  False  False
aus  aust1271  Auslan  -30.0  145.0  Australia  Sign Languages  other  False  False
lmh  lama1277  Lamaholot  -8.25  122.916666667  Papunesia  Central Malayo-Polynesian  Austronesian  False  False
seb  kups1238  Sebei  1.33333333333  34.5833333333  Africa  Nilotic  Nilo-Saharan  False  False
cor  elna1235  Cora  22.1666666667  -104.833333333  North America  Corachol  Uto-Aztecan  False  False
plb  pola1255  Polabian  51.0  12.8333333333  Eurasia  Slavic  Indo-European  False  False
mhm  besi1244  Mah Meri  2.83333333333  101.5  Eurasia  Aslian  Austro-Asiatic  False  False
kot  kota1263  Kota  11.5  77.1666666667  Eurasia  Southern Dravidian  Dravidian  False  False
hup  hupa1239  Hupa  41.0833333333  -123.666666667  North America  Athapaskan  Na-Dene  False  False
gul  gula1269  Gula (in Central African Republic)  9.5  22.5  Africa  Bongo-Bagirmi  Nilo-Saharan  False  False
myo  mayo1264  Mayo  26.0  -108.0  North America  Cahita  Uto-Aztecan  False  False
ror  waim1251  Roro  -8.75  146.583333333  Papunesia  Oceanic  Austronesian  False  False
thd  thad1238  Thadou  24.4166666667  93.9166666667  Eurasia  Kuki-Chin  Sino-Tibetan  False  False
mbt  mang1394  Mangbetu  2.5  26.5  Africa  Mangbetu  Nilo-Saharan  False  False
iva  ivat1242  Ivatan  20.5  122.0  Papunesia  Batanic  Austronesian  False  False
rsh  shug1248  Rushan  38.1666666667  71.5  Eurasia  Iranian  Indo-European  False  False
smd  sema1269  Semandang  -0.75  110.5  Papunesia  Land Dayak  Austronesian  False  False
kjn  kunj1245  Kunjen  -16.5  142.5  Australia  Pama-Nyungan  Australian  False  False
mku  mara1386  Maranungku  -13.6666666667  130.0  Australia  Western Daly  Australian  False  True
ymi  yami1254  Yami  22.0  121.5  Papunesia  Batanic  Austronesian  False  False
usr  usar1243  Usarufa  -6.41666666667  145.583333333  Papunesia  Eastern Highlands  Trans-New Guinea  False  False
pau  paum1247  Paumarí  -6.0  -64.0  South America  Arauan  Arauan  False  True
mek  saki1248  Mekens  -12.5  -61.5  South America  Tupari  Tupian  False  False
csl  chin1283  Chinese Sign Language  35.0  115.0  Eurasia  Sign Languages  other  False  False
lin  ling1263  Lingala  2.0  18.5  Africa  Bantoid  Niger-Congo  False  False
ugs  ugan1238  Ugandan Sign Language  1.0  32.5  Africa  Sign Languages  other  False  False
inr  west2618  Inuktitut (Rankin Inlet)  63.0  -92.0  North America  Eskimo  Eskimo-Aleut  False  False
sbg  bala1311  Sama (Balangingi)  6.16666666667  121.833333333  Papunesia  Sama-Bajaw  Austronesian  False  False
src  sars1236  Sarcee  52.5  -116.0  North America  Athapaskan  Na-Dene  False  False
yil  yill1241  Yil  -3.53333333333  142.15  Papunesia  Wapei-Palei  Torricelli  False  False
jom  talo1250  Jomang  10.5833333333  30.5  Africa  Talodi Proper  Niger-Congo  False  False
jva  kara1500  Javaé  -10.0  -50.3333333333  South America  Karajá  Macro-Ge  False  False
kpo  ikpo1238  Kposo  7.5  0.833333333333  Africa  Kwa  Niger-Congo  False  False
tgp  sawi1256  Tanglapui  -8.28333333333  125.083333333  Papunesia  Kolana-Tanglapui  Timor-Alor-Pantar  False  False
max  maxa1247  Maxakalí  -18.0  -40.0  South America  Maxakalí  Macro-Ge  False  False
nnd  nend1239  Nend  -5.0  144.916666667  Papunesia  Madang  Trans-New Guinea  False  False
tsa  tsak1249  Tsakhur  41.6666666667  47.1666666667  Eurasia  Lezgic  Nakh-Daghestanian  False  False
mde  mend1266  Mende  7.83333333333  -11.5  Africa  Western Mande  Niger-Congo  False  False
isn  isna1241  Isnag  18.25  121.0  Papunesia  Northern Luzon  Austronesian  False  False
mke  meke1243  Mekeo  -8.33333333333  146.5  Papunesia  Oceanic  Austronesian  False  False
sod  kist1241  Soddo  8.5  38.5  Africa  Semitic  Afro-Asiatic  False  False
svt  swed1236  Svenska Teckenspråket  59.0  15.0  Eurasia  Sign Languages  other  False  False
gor  goro1270  Gorowa  -4.5  36.5  Africa  Southern Cushitic  Afro-Asiatic  False  False
can  cand1248  Candoshi  -4.16666666667  -77.0  South America  Candoshi  Candoshi  False  False
tuy  tuyu1244  Tuyuca  0.5  -70.0833333333  South America  Tucanoan  Tucanoan  False  False
uzn  nort2690  Uzbek (Northern)  40.6666666667  66.5  Eurasia  Turkic  Altaic  False  False
poc  poqo1257  Pocomam Oriental  14.75  -89.75  North America  Mayan  Mayan  False  False
pog  pogo1243  Pogoro  -8.75  36.5  Africa  Bantoid  Niger-Congo  False  False
mak  maka1318  Makah  48.3333333333  -124.666666667  North America  Southern Wakashan  Wakashan  True  True
ban  bana1305  Bana  10.4166666667  13.5833333333  Africa  Biu-Mandara  Afro-Asiatic  False  False
ava  avar1256  Avar  42.5  46.5  Eurasia  Avar-Andic-Tsezic  Nakh-Daghestanian  False  False
gok  goka1239  Gokana  4.58333333333  7.33333333333  Africa  Cross River  Niger-Congo  False  False
asu  toca1235  Asuriní  -3.5  -49.5  South America  Tupi-Guaraní  Tupian  False  False
chd  chau1259  Chaudangsi  30.0  80.25  Eurasia  Bodic  Sino-Tibetan  False  False
bco  bell1243  Bella Coola  52.5  -126.666666667  North America  Bella Coola  Salishan  False  False
mok  moki1238  Mokilese  6.66666666667  159.75  Papunesia  Oceanic  Austronesian  False  False
ksl  keny1241  Kenyan Sign Language  0.0  38.0  Africa  Sign Languages  other  False  False
wag  wage1238  Wagiman  -14.0  131.25  Australia  Wagiman  Australian  False  False
rmb  remb1249  Rembarnga  -12.8333333333  134.583333333  Australia  Rembarnga  Australian  False  False
bly  nija1241  Balyku  -22.0  120.0  Australia  Pama-Nyungan  Australian  False  False
bdu  budu1250  Budu  2.0  28.0  Africa  Bantoid  Niger-Congo  False  False
hna  mina1276  Mina  10.3333333333  13.8333333333  Africa  Biu-Mandara  Afro-Asiatic  False  False
mxe  mele1250  Ifira-Mele  -17.75  168.25  Papunesia  Oceanic  Austronesian  False  False
abv  abui1241  Abui  -8.25  124.666666667  Papunesia  Greater Alor  Timor-Alor-Pantar  False  False
nbm  ngba1284  Ngbaka (Ma'bo)  3.56  18.36  Africa  Ubangi  Niger-Congo  False  False
mpr  maip1246  Maipure  5.5  -67.5  South America  Northern Arawakan  Arawakan  False  False
esm  atac1235  Esmeraldeño  0.333333333333  -79.8333333333  South America  Tacame  Tacame  False  False
hks  hong1241  Hong Kong Sign Language  22.5  114.0  Eurasia  Sign Languages  other  False  False
puq  puqu1242  Puquina  -16.5  -68.5  South America  Puquina  Puquina  False  False
isl  inte1259  International Sign  40.0  -170.0  North America  Sign Languages  other  False  False
mkw  maku1246  Máku  0.416666666667  -69.8333333333  South America  Máku  Máku  False  False
ktt  kott1239  Kott  57.0  94.0  Eurasia  Yeniseian  Yeniseian  False  False
kaq  kaur1267  Kaurna  -34.25  138.5  Australia  Pama-Nyungan  Australian  False  False
cav  cavi1250  Cavineña  -13.3333333333  -66.5  South America  Tacanan  Tacanan  False  False
mra  mara1385  Mara  -15.0  135.166666667  Australia  Maran  Australian  False  False
nya  nyaw1247  Nyawaygi  -19.0  146.166666667  Australia  Pama-Nyungan  Australian  False  False
gum  kumb1268  Gumbaynggir  -30.1666666667  152.5  Australia  Pama-Nyungan  Australian  False  False
cec  chic1271  Chicomuceltec  15.5  -92.25  North America  Mayan  Mayan  False  False
tlo  tobe1252  Tobelo  1.5  128.5  Papunesia  North Halmaheran  West Papuan  False  False
til  till1254  Tillamook  45.3333333333  -123.75  North America  Tillamook  Salishan  False  False
tsf  colo1256  Tsafiki  -1.0  -79.3333333333  South America  Barbacoan  Barbacoan  False  False
tao  tara1313  Tarao  24.25  94.1666666667  Eurasia  Kuki-Chin  Sino-Tibetan  False  False
blk  bala1315  Balantak  -0.833333333333  123.25  Papunesia  Celebic  Austronesian  False  False
ant  anga1290  Angaatiha  -7.21666666667  146.25  Papunesia  Angan  Trans-New Guinea  False  False
muy  muyu1244  Muyuw  -9.08333333333  152.75  Papunesia  Oceanic  Austronesian  False  False
pcm  poqo1253  Pocomam  14.6666666667  -90.5  North America  Mayan  Mayan  False  False
blu  luba1249  Bena-Lulua  -6.0  21.0  Africa  Bantoid  Niger-Congo  False  False
bys  bais1246  Bayso  6.25  37.75  Africa  Eastern Cushitic  Afro-Asiatic  False  False
mcc  moch1259  Mochica  -7.5  -79.3333333333  South America  Chimúan  Chimúan  False  False
ice  icel1247  Icelandic  65.0  -17.0  Eurasia  Germanic  Indo-European  False  False
taz  taly1247  Talysh (Azerbaijan)  38.75  48.6666666667  Eurasia  Iranian  Indo-European  False  False
tls  taly1247  Talysh (Southern)  37.0  49.0  Eurasia  Iranian  Indo-European  False  False
mdu  mund1326  Mündü  4.5  30.0  Africa  Ubangi  Niger-Congo  False  False
kln  wers1238  Kolana  -8.25  125.116666667  Papunesia  Kolana-Tanglapui  Timor-Alor-Pantar  False  False
nal  nali1244  Nalik  -2.95  151.333333333  Papunesia  Oceanic  Austronesian  False  False
tup  None  Tupi  -6.0  -36.0  None  Tupi-Guaraní  Tupian  False  False
hya  haya1250  Haya  -2.0  31.5  Africa  Bantoid  Niger-Congo  False  False
ttn  tetu1245  Tetun  -9.0  126.0  Papunesia  Central Malayo-Polynesian  Austronesian  False  False
wra  wara1303  Warao  9.33333333333  -61.6666666667  South America  Warao  Warao  True  True
gmw  guma1254  Gumawana  -9.25  150.833333333  Papunesia  Oceanic  Austronesian  False  False
lou  louu1245  Lou  -2.38333333333  147.316666667  Papunesia  Oceanic  Austronesian  False  False
kei  keii1239  Kei  -5.83333333333  132.916666667  Papunesia  Central Malayo-Polynesian  Austronesian  False  False
bii  biri1256  Biri  -20.5  146.5  Australia  Pama-Nyungan  Australian  False  False
bam  bamb1269  Bambara  12.5  -7.5  Africa  Western Mande  Niger-Congo  False  True
mdz  mada1282  Mada (in Nigeria)  8.75  8.25  Africa  Platoid  Niger-Congo  False  False
kwr  kwam1252  Kwamera  -19.5833333333  169.416666667  Papunesia  Oceanic  Austronesian  False  False
pag  pagu1249  Pagu  1.25  127.75  Papunesia  North Halmaheran  West Papuan  False  False
udh  udih1248  Udihe  47.6666666667  136.25  Eurasia  Tungusic  Altaic  False  False
han  hani1248  Hani  23.0  103.0  Eurasia  Burmese-Lolo  Sino-Tibetan  False  False
pra  pras1239  Prasuni  35.5  71.0  Eurasia  Indic  Indo-European  False  False
hma  hmar1241  Hmar  24.1666666667  93.0  Eurasia  Kuki-Chin  Sino-Tibetan  False  False
api  apin1244  Apinayé  -5.5  -48.0  South America  Ge-Kaingang  Macro-Ge  False  False
ayr  ayor1240  Ayoreo  -20.25  -59.25  South America  Zamucoan  Zamucoan  False  False
nue  nuer1246  Nuer  8.33333333333  32.0  Africa  Nilotic  Nilo-Saharan  False  False
nad  nade1244  Nadëb  -1.0  -66.5  South America  Nadahup  Nadahup  False  False
tau  tauy1241  Tauya  -5.75  145.333333333  Papunesia  Madang  Trans-New Guinea  False  False
est  esto1258  Estonian  59.0  26.0  Eurasia  Finnic  Uralic  False  False
otr  otor1240  Otoro  11.1666666667  30.5  Africa  Heiban  Niger-Congo  False  False
mrg  marg1265  Margi  11.0  13.0  Africa  Biu-Mandara  Afro-Asiatic  False  False
zun  zuni1245  Zuni  35.0833333333  -108.833333333  North America  Zuni  Zuni  False  False
trg  tewa1260  Tewa (Rio Grande)  36.25  -106.166666667  North America  Kiowa-Tanoan  Kiowa-Tanoan  False  False
tsj  tewa1260  Tewa (San Juan Pueblo)  36.0833333333  -106.083333333  North America  Kiowa-Tanoan  Kiowa-Tanoan  False  False
ton  tonk1249  Tonkawa  30.25  -96.75  North America  Tonkawa  Tonkawa  False  False
wbn  wamb1259  Wambon  -5.5  140.416666667  Papunesia  Awju-Dumut  Trans-New Guinea  False  False
bgs  baga1272  Baga Sitemu  10.5  -14.5  Africa  Southern Atlantic  Niger-Congo  False  False
gog  gogo1265  Gogodala  -8.08333333333  142.833333333  Papunesia  Gogodala  Gogodala-Suki  False  False
oro  orok1269  Orokaiva  -8.83333333333  148.25  Papunesia  Binanderean  Trans-New Guinea  False  False
blx  bilo1248  Biloxi  30.5  -88.6666666667  North America  Siouan  Siouan  False  False
boz  tiey1235  Bozo (Tigemaxo)  15.0  -4.0  Africa  Western Mande  Niger-Congo  False  False
bau  bauu1244  Bau  -5.25  145.616666667  Papunesia  Madang  Trans-New Guinea  False  False
bou  taga1278  Berber (Wargla)  31.9166666667  5.33333333333  Africa  Berber  Afro-Asiatic  False  False
ker  kera1255  Kera  9.83333333333  15.0833333333  Africa  East Chadic  Afro-Asiatic  False  True
maj  maja1242  Majang  6.75  35.0  Africa  Surmic  Nilo-Saharan  False  False
alc  alle1238  Allentiac  -31.0  -68.0  South America  Huarpe  Huarpe  False  False
tel  telu1262  Telugu  16.0  79.0  Eurasia  South-Central Dravidian  Dravidian  False  False
rej  reja1240  Rejang  -3.41666666667  102.5  Papunesia  Rejang  Austronesian  False  False
wwr  woiw1237  Woiwurrung  -37.5  145.5  Australia  Pama-Nyungan  Australian  False  False
adk  ando1256  Andoke  -0.666666666667  -72.0  South America  Andoke  Andoke  False  False
sdw  sand1273  Sandawe  -5.0  35.0  Africa  Sandawe  Khoisan  False  False
mbb  mbab1239  Mbabaram  -17.1666666667  145.0  Australia  Pama-Nyungan  Australian  False  False
sus  susu1250  Susu  10.0  -13.0  Africa  Western Mande  Niger-Congo  False  False
kuu  kuuk1238  Kuuku Ya'u  -12.5833333333  143.083333333  Australia  Pama-Nyungan  Australian  False  False
bdm  badi1246  Badimaya  -27.6666666667  118.0  Australia  Pama-Nyungan  Australian  False  False
djm  djam1256  Djambarrpuyngu  -12.1666666667  135.5  Australia  Pama-Nyungan  Australian  False  False
nih  japa1238  Nihon Shuwa (Japanese Sign Language)  36.0  139.0  Eurasia  Sign Languages  other  False  False
skl  siku1242  Sikule  2.66666666667  96.0  Papunesia  Northwest Sumatra-Barrier Islands  Austronesian  False  False
vif  vili1238  Vili  -5.5  14.0  Africa  Bantoid  Niger-Congo  False  False
nmm  mana1288  Manange  28.5833333333  84.0  Eurasia  Bodic  Sino-Tibetan  False  False
xbi  komb1272  Kombio  -3.5  142.75  Papunesia  Kombio-Arapesh  Torricelli  False  False
pnx  pana1307  Panará  -10.0  -55.0  South America  Ge-Kaingang  Macro-Ge  False  False
nub  nubi1253  Nubi  0.666666666667  32.0833333333  Africa  Creoles and Pidgins  other  False  False
slg  sulu1241  Sulung  28.3333333333  93.25  Eurasia  Sulung  Sulung  False  False
kdz  coas1294  Kadazan  5.91666666667  117.166666667  Papunesia  North Borneo  Austronesian  False  False
mtg  mont1268  Montagnais  52.0  -65.0  North America  Algonquian  Algic  False  False
imo  imon1245  Imonda  -3.33333333333  141.166666667  Papunesia  Border  Border  True  True
sem  sumi1235  Sema  26.0  94.5  Eurasia  Kuki-Chin  Sino-Tibetan  False  False
kic  kick1244  Kickapoo  42.25  -84.0  North America  Algonquian  Algic  False  False
gsl  gree1271  Greek Sign Language  38.5  22.0  Eurasia  Sign Languages  other  False  False
ipk  paki1242  Indo-Pakistani Sign Language (Karachi dialect)  28.0  68.0  Eurasia  Sign Languages  other  False  False
sps  sout2965  Salish (Southern Puget Sound)  47.25  -122.5  North America  Central Salish  Salishan  False  False
tzi  taiw1241  Taiwanese Sign Language (Ziran Shouyu)  24.0  121.0  Papunesia  Sign Languages  other  False  False
aka  yaka1272  Aka  2.66666666667  16.25  Africa  Bantoid  Niger-Congo  False  False
buk  buku1249  Bukusu  0.75  34.6666666667  Africa  Bantoid  Niger-Congo  False  False
ani  anii1246  //Ani  -18.9166666667  21.9166666667  Africa  Central Khoisan  Khoisan  False  False
kkr  kiri1256  Kirikiri  -3.0  137.166666667  Papunesia  Lakes Plain  Lakes Plain  False  False
wgg  wang1290  Wangkangurru  -27.0  137.0  Australia  Pama-Nyungan  Australian  False  False
mqf  momu1241  Momuna  -4.83333333333  139.25  Papunesia  Momuna  Trans-New Guinea  False  False
csk  jola1262  Diola-Kasa  12.5  -16.75  Africa  Northern Atlantic  Niger-Congo  False  False
bnu  bula1255  Bularnu  -21.0  138.0  Australia  Pama-Nyungan  Australian  False  False
wom  womo1238  Womo  -2.91666666667  141.833333333  Papunesia  Serra Hills  Skou  False  False
myy  mayk1239  Mayi-Yapi  -20.0  141.0  Australia  Pama-Nyungan  Australian  False  False
cco  tutu1242  Chasta Costa  42.6666666667  -124.0  North America  Athapaskan  Na-Dene  False  False
aab  None  Arapesh (Abu)  -3.45  142.95  None  Kombio-Arapesh  Torricelli  False  False
bah  None  Bahuana  -0.5  -62.5  None  Northern Arawakan  Arawakan  False  False
tms  None  Tommo So  15.0  -3.0  None  Dogon  Niger-Congo  False  False
kua  None  Kualan  -0.416666666667  110.416666667  None  Land Dayak  Austronesian  False  False
lgh  None  Lughat al-Isharat al-Lubnaniya  34.0  35.8333333333  None  Sign Languages  other  False  False
rcp  None  Russian-Chinese Pidgin (Birobidjan)  48.8  132.95  None  Creoles and Pidgins  other  False  False
jua  None  Juat  -31.0  115.5  None  Pama-Nyungan  Australian  False  False
keu  None  Kenyah (Uma' Lung)  3.0  115.833333333  None  North Borneo  Austronesian  False  False
joh  None  Johari  30.6666666667  80.0  None  Bodic  Sino-Tibetan  False  False"""

WALS = {}
for line in wals_tsv.split('\n'):
  lang = line.split()[0]
  for key, value in zip(headerline.split()[1:], line.split()[1:]):
    WALS.setdefault(lang, {})[key] = value
    
lang2family = defaultdict(list)
for lang in WALS:
  lang2family[WALS[lang]['genus']].append(lang)
  
langs_in_same_cluster = defaultdict(list)
for lang in WALS:
  langs_in_same_cluster[lang] = lang2family[WALS[lang]['genus']]
  
