# -*- coding: utf-8 -*-

import codecs, re
from collections import defaultdict

# from http://www-01.sil.org/iso639-3/iso-639-3_Name_Index.tab
iso6963 = """Id  Print_Name  Inverted_Name
aaa  Ghotuo  Ghotuo
aab  Alumu-Tesu  Alumu-Tesu
aac  Ari  Ari
aad  Amal  Amal
aae  Arbëreshë Albanian  Albanian, Arbëreshë
aaf  Aranadan  Aranadan
aag  Ambrak  Ambrak
aah  Abu' Arapesh  Arapesh, Abu'
aai  Arifama-Miniafia  Arifama-Miniafia
aak  Ankave  Ankave
aal  Afade  Afade
aam  Aramanik  Aramanik
aan  Anambé  Anambé
aao  Algerian Saharan Arabic  Arabic, Algerian Saharan
aap  Pará Arára  Arára, Pará
aaq  Eastern Abnaki  Abnaki, Eastern
aar  Afar  Afar
aas  Aasáx  Aasáx
aat  Arvanitika Albanian  Albanian, Arvanitika
aau  Abau  Abau
aaw  Solong  Solong
aax  Mandobo Atas  Mandobo Atas
aaz  Amarasi  Amarasi
aba  Abé  Abé
abb  Bankon  Bankon
abc  Ambala Ayta  Ayta, Ambala
abd  Manide  Manide
abe  Western Abnaki  Abnaki, Western
abf  Abai Sungai  Abai Sungai
abg  Abaga  Abaga
abh  Tajiki Arabic  Arabic, Tajiki
abi  Abidji  Abidji
abj  Aka-Bea  Aka-Bea
abk  Abkhazian  Abkhazian
abl  Lampung Nyo  Lampung Nyo
abm  Abanyom  Abanyom
abn  Abua  Abua
abo  Abon  Abon
abp  Abellen Ayta  Ayta, Abellen
abq  Abaza  Abaza
abr  Abron  Abron
abs  Ambonese Malay  Malay, Ambonese
abt  Ambulas  Ambulas
abu  Abure  Abure
abv  Baharna Arabic  Arabic, Baharna
abw  Pal  Pal
abx  Inabaknon  Inabaknon
aby  Aneme Wake  Aneme Wake
abz  Abui  Abui
aca  Achagua  Achagua
acb  Áncá  Áncá
acd  Gikyode  Gikyode
ace  Achinese  Achinese
acf  Saint Lucian Creole French  Creole French, Saint Lucian
ach  Acoli  Acoli
aci  Aka-Cari  Aka-Cari
ack  Aka-Kora  Aka-Kora
acl  Akar-Bale  Akar-Bale
acm  Mesopotamian Arabic  Arabic, Mesopotamian
acn  Achang  Achang
acp  Eastern Acipa  Acipa, Eastern
acq  Ta'izzi-Adeni Arabic  Arabic, Ta'izzi-Adeni
acr  Achi  Achi
acs  Acroá  Acroá
act  Achterhoeks  Achterhoeks
acu  Achuar-Shiwiar  Achuar-Shiwiar
acv  Achumawi  Achumawi
acw  Hijazi Arabic  Arabic, Hijazi
acx  Omani Arabic  Arabic, Omani
acy  Cypriot Arabic  Arabic, Cypriot
acz  Acheron  Acheron
ada  Adangme  Adangme
adb  Adabe  Adabe
add  Dzodinka  Dzodinka
ade  Adele  Adele
adf  Dhofari Arabic  Arabic, Dhofari
adg  Andegerebinha  Andegerebinha
adh  Adhola  Adhola
adi  Adi  Adi
adj  Adioukrou  Adioukrou
adl  Galo  Galo
adn  Adang  Adang
ado  Abu  Abu
adp  Adap  Adap
adq  Adangbe  Adangbe
adr  Adonara  Adonara
ads  Adamorobe Sign Language  Adamorobe Sign Language
adt  Adnyamathanha  Adnyamathanha
adu  Aduge  Aduge
adw  Amundava  Amundava
adx  Amdo Tibetan  Tibetan, Amdo
ady  Adygei  Adygei
ady  Adyghe  Adyghe
adz  Adzera  Adzera
aea  Areba  Areba
aeb  Tunisian Arabic  Arabic, Tunisian
aec  Saidi Arabic  Arabic, Saidi
aed  Argentine Sign Language  Argentine Sign Language
aee  Northeast Pashayi  Pashayi, Northeast
aek  Haeke  Haeke
ael  Ambele  Ambele
aem  Arem  Arem
aen  Armenian Sign Language  Armenian Sign Language
aeq  Aer  Aer
aer  Eastern Arrernte  Arrernte, Eastern
aes  Alsea  Alsea
aeu  Akeu  Akeu
aew  Ambakich  Ambakich
aey  Amele  Amele
aez  Aeka  Aeka
afb  Gulf Arabic  Arabic, Gulf
afd  Andai  Andai
afe  Putukwam  Putukwam
afg  Afghan Sign Language  Afghan Sign Language
afh  Afrihili  Afrihili
afi  Akrukay  Akrukay
afk  Nanubae  Nanubae
afn  Defaka  Defaka
afo  Eloyi  Eloyi
afp  Tapei  Tapei
afr  Afrikaans  Afrikaans
afs  Afro-Seminole Creole  Creole, Afro-Seminole
aft  Afitti  Afitti
afu  Awutu  Awutu
afz  Obokuitai  Obokuitai
aga  Aguano  Aguano
agb  Legbo  Legbo
agc  Agatu  Agatu
agd  Agarabi  Agarabi
age  Angal  Angal
agf  Arguni  Arguni
agg  Angor  Angor
agh  Ngelima  Ngelima
agi  Agariya  Agariya
agj  Argobba  Argobba
agk  Isarog Agta  Agta, Isarog
agl  Fembe  Fembe
agm  Angaataha  Angaataha
agn  Agutaynen  Agutaynen
ago  Tainae  Tainae
agq  Aghem  Aghem
agr  Aguaruna  Aguaruna
ags  Esimbi  Esimbi
agt  Central Cagayan Agta  Agta, Central Cagayan
agu  Aguacateco  Aguacateco
agv  Remontado Dumagat  Dumagat, Remontado
agw  Kahua  Kahua
agx  Aghul  Aghul
agy  Southern Alta  Alta, Southern
agz  Mt. Iriga Agta  Agta, Mt. Iriga
aha  Ahanta  Ahanta
ahb  Axamb  Axamb
ahg  Qimant  Qimant
ahh  Aghu  Aghu
ahi  Tiagbamrin Aizi  Aizi, Tiagbamrin
ahk  Akha  Akha
ahl  Igo  Igo
ahm  Mobumrin Aizi  Aizi, Mobumrin
ahn  Àhàn  Àhàn
aho  Ahom  Ahom
ahp  Aproumu Aizi  Aizi, Aproumu
ahr  Ahirani  Ahirani
ahs  Ashe  Ashe
aht  Ahtena  Ahtena
aia  Arosi  Arosi
aib  Ainu (China)  Ainu (China)
aic  Ainbai  Ainbai
aid  Alngith  Alngith
aie  Amara  Amara
aif  Agi  Agi
aig  Antigua and Barbuda Creole English  Creole English, Antigua and Barbuda
aih  Ai-Cham  Ai-Cham
aii  Assyrian Neo-Aramaic  Neo-Aramaic, Assyrian
aij  Lishanid Noshan  Lishanid Noshan
aik  Ake  Ake
ail  Aimele  Aimele
aim  Aimol  Aimol
ain  Ainu (Japan)  Ainu (Japan)
aio  Aiton  Aiton
aip  Burumakok  Burumakok
aiq  Aimaq  Aimaq
air  Airoran  Airoran
ais  Nataoran Amis  Amis, Nataoran
ait  Arikem  Arikem
aiw  Aari  Aari
aix  Aighon  Aighon
aiy  Ali  Ali
aja  Aja (Sudan)  Aja (Sudan)
ajg  Aja (Benin)  Aja (Benin)
aji  Ajië  Ajië
ajn  Andajin  Andajin
ajp  South Levantine Arabic  Arabic, South Levantine
ajt  Judeo-Tunisian Arabic  Arabic, Judeo-Tunisian
aju  Judeo-Moroccan Arabic  Arabic, Judeo-Moroccan
ajw  Ajawa  Ajawa
ajz  Amri Karbi  Karbi, Amri
aka  Akan  Akan
akb  Batak Angkola  Batak Angkola
akc  Mpur  Mpur
akd  Ukpet-Ehom  Ukpet-Ehom
ake  Akawaio  Akawaio
akf  Akpa  Akpa
akg  Anakalangu  Anakalangu
akh  Angal Heneng  Angal Heneng
aki  Aiome  Aiome
akj  Aka-Jeru  Aka-Jeru
akk  Akkadian  Akkadian
akl  Aklanon  Aklanon
akm  Aka-Bo  Aka-Bo
ako  Akurio  Akurio
akp  Siwu  Siwu
akq  Ak  Ak
akr  Araki  Araki
aks  Akaselem  Akaselem
akt  Akolet  Akolet
aku  Akum  Akum
akv  Akhvakh  Akhvakh
akw  Akwa  Akwa
akx  Aka-Kede  Aka-Kede
aky  Aka-Kol  Aka-Kol
akz  Alabama  Alabama
ala  Alago  Alago
alc  Qawasqar  Qawasqar
ald  Alladian  Alladian
ale  Aleut  Aleut
alf  Alege  Alege
alh  Alawa  Alawa
ali  Amaimon  Amaimon
alj  Alangan  Alangan
alk  Alak  Alak
all  Allar  Allar
alm  Amblong  Amblong
aln  Gheg Albanian  Albanian, Gheg
alo  Larike-Wakasihu  Larike-Wakasihu
alp  Alune  Alune
alq  Algonquin  Algonquin
alr  Alutor  Alutor
als  Tosk Albanian  Albanian, Tosk
alt  Southern Altai  Altai, Southern
alu  'Are'are  'Are'are
alw  Alaba-K’abeena  Alaba-K’abeena
alw  Wanbasana  Wanbasana
alx  Amol  Amol
aly  Alyawarr  Alyawarr
alz  Alur  Alur
ama  Amanayé  Amanayé
amb  Ambo  Ambo
amc  Amahuaca  Amahuaca
ame  Yanesha'  Yanesha'
amf  Hamer-Banna  Hamer-Banna
amg  Amurdak  Amurdak
amh  Amharic  Amharic
ami  Amis  Amis
amj  Amdang  Amdang
amk  Ambai  Ambai
aml  War-Jaintia  War-Jaintia
amm  Ama (Papua New Guinea)  Ama (Papua New Guinea)
amn  Amanab  Amanab
amo  Amo  Amo
amp  Alamblak  Alamblak
amq  Amahai  Amahai
amr  Amarakaeri  Amarakaeri
ams  Southern Amami-Oshima  Amami-Oshima, Southern
amt  Amto  Amto
amu  Guerrero Amuzgo  Amuzgo, Guerrero
amv  Ambelau  Ambelau
amw  Western Neo-Aramaic  Neo-Aramaic, Western
amx  Anmatyerre  Anmatyerre
amy  Ami  Ami
amz  Atampaya  Atampaya
ana  Andaqui  Andaqui
anb  Andoa  Andoa
anc  Ngas  Ngas
and  Ansus  Ansus
ane  Xârâcùù  Xârâcùù
anf  Animere  Animere
ang  Old English (ca. 450-1100)  English, Old (ca. 450-1100)
anh  Nend  Nend
ani  Andi  Andi
anj  Anor  Anor
ank  Goemai  Goemai
anl  Anu-Hkongso Chin  Chin, Anu-Hkongso
anm  Anal  Anal
ann  Obolo  Obolo
ano  Andoque  Andoque
anp  Angika  Angika
anq  Jarawa (India)  Jarawa (India)
anr  Andh  Andh
ans  Anserma  Anserma
ant  Antakarinya  Antakarinya
anu  Anuak  Anuak
anv  Denya  Denya
anw  Anaang  Anaang
anx  Andra-Hus  Andra-Hus
any  Anyin  Anyin
anz  Anem  Anem
aoa  Angolar  Angolar
aob  Abom  Abom
aoc  Pemon  Pemon
aod  Andarum  Andarum
aoe  Angal Enen  Angal Enen
aof  Bragat  Bragat
aog  Angoram  Angoram
aoh  Arma  Arma
aoi  Anindilyakwa  Anindilyakwa
aoj  Mufian  Mufian
aok  Arhö  Arhö
aol  Alor  Alor
aom  Ömie  Ömie
aon  Bumbita Arapesh  Arapesh, Bumbita
aor  Aore  Aore
aos  Taikat  Taikat
aot  A'tong  A'tong
aou  A'ou  A'ou
aox  Atorada  Atorada
aoz  Uab Meto  Uab Meto
apb  Sa'a  Sa'a
apc  North Levantine Arabic  Arabic, North Levantine
apd  Sudanese Arabic  Arabic, Sudanese
ape  Bukiyip  Bukiyip
apf  Pahanan Agta  Agta, Pahanan
apg  Ampanang  Ampanang
aph  Athpariya  Athpariya
api  Apiaká  Apiaká
apj  Jicarilla Apache  Apache, Jicarilla
apk  Kiowa Apache  Apache, Kiowa
apl  Lipan Apache  Apache, Lipan
apm  Mescalero-Chiricahua Apache  Apache, Mescalero-Chiricahua
apn  Apinayé  Apinayé
apo  Ambul  Ambul
app  Apma  Apma
apq  A-Pucikwar  A-Pucikwar
apr  Arop-Lokep  Arop-Lokep
aps  Arop-Sissano  Arop-Sissano
apt  Apatani  Apatani
apu  Apurinã  Apurinã
apv  Alapmunte  Alapmunte
apw  Western Apache  Apache, Western
apx  Aputai  Aputai
apy  Apalaí  Apalaí
apz  Safeyoka  Safeyoka
aqc  Archi  Archi
aqd  Ampari Dogon  Dogon, Ampari
aqg  Arigidi  Arigidi
aqm  Atohwaim  Atohwaim
aqn  Northern Alta  Alta, Northern
aqp  Atakapa  Atakapa
aqr  Arhâ  Arhâ
aqz  Akuntsu  Akuntsu
ara  Arabic  Arabic
arb  Standard Arabic  Arabic, Standard
arc  Imperial Aramaic (700-300 BCE)  Aramaic, Imperial (700-300 BCE)
arc  Official Aramaic (700-300 BCE)  Aramaic, Official (700-300 BCE)
ard  Arabana  Arabana
are  Western Arrarnta  Arrarnta, Western
arg  Aragonese  Aragonese
arh  Arhuaco  Arhuaco
ari  Arikara  Arikara
arj  Arapaso  Arapaso
ark  Arikapú  Arikapú
arl  Arabela  Arabela
arn  Mapuche  Mapuche
arn  Mapudungun  Mapudungun
aro  Araona  Araona
arp  Arapaho  Arapaho
arq  Algerian Arabic  Arabic, Algerian
arr  Karo (Brazil)  Karo (Brazil)
ars  Najdi Arabic  Arabic, Najdi
aru  Arawá  Arawá
aru  Aruá (Amazonas State)  Aruá (Amazonas State)
arv  Arbore  Arbore
arw  Arawak  Arawak
arx  Aruá (Rodonia State)  Aruá (Rodonia State)
ary  Moroccan Arabic  Arabic, Moroccan
arz  Egyptian Arabic  Arabic, Egyptian
asa  Asu (Tanzania)  Asu (Tanzania)
asb  Assiniboine  Assiniboine
asc  Casuarina Coast Asmat  Asmat, Casuarina Coast
asd  Asas  Asas
ase  American Sign Language  American Sign Language
asf  Australian Sign Language  Australian Sign Language
asg  Cishingini  Cishingini
ash  Abishira  Abishira
asi  Buruwai  Buruwai
asj  Sari  Sari
ask  Ashkun  Ashkun
asl  Asilulu  Asilulu
asm  Assamese  Assamese
asn  Xingú Asuriní  Asuriní, Xingú
aso  Dano  Dano
asp  Algerian Sign Language  Algerian Sign Language
asq  Austrian Sign Language  Austrian Sign Language
asr  Asuri  Asuri
ass  Ipulo  Ipulo
ast  Asturian  Asturian
ast  Asturleonese  Asturleonese
ast  Bable  Bable
ast  Leonese  Leonese
asu  Tocantins Asurini  Asurini, Tocantins
asv  Asoa  Asoa
asw  Australian Aborigines Sign Language  Australian Aborigines Sign Language
asx  Muratayak  Muratayak
asy  Yaosakor Asmat  Asmat, Yaosakor
asz  As  As
ata  Pele-Ata  Pele-Ata
atb  Zaiwa  Zaiwa
atc  Atsahuaca  Atsahuaca
atd  Ata Manobo  Manobo, Ata
ate  Atemble  Atemble
atg  Ivbie North-Okpela-Arhe  Ivbie North-Okpela-Arhe
ati  Attié  Attié
atj  Atikamekw  Atikamekw
atk  Ati  Ati
atl  Mt. Iraya Agta  Agta, Mt. Iraya
atm  Ata  Ata
atn  Ashtiani  Ashtiani
ato  Atong  Atong
atp  Pudtol Atta  Atta, Pudtol
atq  Aralle-Tabulahan  Aralle-Tabulahan
atr  Waimiri-Atroari  Waimiri-Atroari
ats  Gros Ventre  Gros Ventre
att  Pamplona Atta  Atta, Pamplona
atu  Reel  Reel
atv  Northern Altai  Altai, Northern
atw  Atsugewi  Atsugewi
atx  Arutani  Arutani
aty  Aneityum  Aneityum
atz  Arta  Arta
aua  Asumboa  Asumboa
aub  Alugu  Alugu
auc  Waorani  Waorani
aud  Anuta  Anuta
aue  =/Kx'au//'ein  =/Kx'au//'ein
aug  Aguna  Aguna
auh  Aushi  Aushi
aui  Anuki  Anuki
auj  Awjilah  Awjilah
auk  Heyo  Heyo
aul  Aulua  Aulua
aum  Asu (Nigeria)  Asu (Nigeria)
aun  Molmo One  One, Molmo
auo  Auyokawa  Auyokawa
aup  Makayam  Makayam
auq  Anus  Anus
auq  Korur  Korur
aur  Aruek  Aruek
aut  Austral  Austral
auu  Auye  Auye
auw  Awyi  Awyi
aux  Aurá  Aurá
auy  Awiyaana  Awiyaana
auz  Uzbeki Arabic  Arabic, Uzbeki
ava  Avaric  Avaric
avb  Avau  Avau
avd  Alviri-Vidari  Alviri-Vidari
ave  Avestan  Avestan
avi  Avikam  Avikam
avk  Kotava  Kotava
avl  Eastern Egyptian Bedawi Arabic  Arabic, Eastern Egyptian Bedawi
avm  Angkamuthi  Angkamuthi
avn  Avatime  Avatime
avo  Agavotaguerra  Agavotaguerra
avs  Aushiri  Aushiri
avt  Au  Au
avu  Avokaya  Avokaya
avv  Avá-Canoeiro  Avá-Canoeiro
awa  Awadhi  Awadhi
awb  Awa (Papua New Guinea)  Awa (Papua New Guinea)
awc  Cicipu  Cicipu
awe  Awetí  Awetí
awg  Anguthimri  Anguthimri
awh  Awbono  Awbono
awi  Aekyom  Aekyom
awk  Awabakal  Awabakal
awm  Arawum  Arawum
awn  Awngi  Awngi
awo  Awak  Awak
awr  Awera  Awera
aws  South Awyu  Awyu, South
awt  Araweté  Araweté
awu  Central Awyu  Awyu, Central
awv  Jair Awyu  Awyu, Jair
aww  Awun  Awun
awx  Awara  Awara
awy  Edera Awyu  Awyu, Edera
axb  Abipon  Abipon
axe  Ayerrerenge  Ayerrerenge
axg  Mato Grosso Arára  Arára, Mato Grosso
axk  Yaka (Central African Republic)  Yaka (Central African Republic)
axl  Lower Southern Aranda  Aranda, Lower Southern
axm  Middle Armenian  Armenian, Middle
axx  Xârâgurè  Xârâgurè
aya  Awar  Awar
ayb  Ayizo Gbe  Gbe, Ayizo
ayc  Southern Aymara  Aymara, Southern
ayd  Ayabadhu  Ayabadhu
aye  Ayere  Ayere
ayg  Ginyanga  Ginyanga
ayh  Hadrami Arabic  Arabic, Hadrami
ayi  Leyigha  Leyigha
ayk  Akuku  Akuku
ayl  Libyan Arabic  Arabic, Libyan
aym  Aymara  Aymara
ayn  Sanaani Arabic  Arabic, Sanaani
ayo  Ayoreo  Ayoreo
ayp  North Mesopotamian Arabic  Arabic, North Mesopotamian
ayq  Ayi (Papua New Guinea)  Ayi (Papua New Guinea)
ayr  Central Aymara  Aymara, Central
ays  Sorsogon Ayta  Ayta, Sorsogon
ayt  Magbukun Ayta  Ayta, Magbukun
ayu  Ayu  Ayu
ayy  Tayabas Ayta  Ayta, Tayabas
ayz  Mai Brat  Mai Brat
aza  Azha  Azha
azb  South Azerbaijani  Azerbaijani, South
azd  Eastern Durango Nahuatl  Nahuatl, Eastern Durango
aze  Azerbaijani  Azerbaijani
azg  San Pedro Amuzgos Amuzgo  Amuzgo, San Pedro Amuzgos
azj  North Azerbaijani  Azerbaijani, North
azm  Ipalapa Amuzgo  Amuzgo, Ipalapa
azn  Western Durango Nahuatl  Nahuatl, Western Durango
azo  Awing  Awing
azt  Faire Atta  Atta, Faire
azz  Highland Puebla Nahuatl  Nahuatl, Highland Puebla
baa  Babatana  Babatana
bab  Bainouk-Gunyuño  Bainouk-Gunyuño
bac  Badui  Badui
bae  Baré  Baré
baf  Nubaca  Nubaca
bag  Tuki  Tuki
bah  Bahamas Creole English  Creole English, Bahamas
baj  Barakai  Barakai
bak  Bashkir  Bashkir
bal  Baluchi  Baluchi
bam  Bambara  Bambara
ban  Balinese  Balinese
bao  Waimaha  Waimaha
bap  Bantawa  Bantawa
bar  Bavarian  Bavarian
bas  Basa (Cameroon)  Basa (Cameroon)
bau  Bada (Nigeria)  Bada (Nigeria)
bav  Vengo  Vengo
baw  Bambili-Bambui  Bambili-Bambui
bax  Bamun  Bamun
bay  Batuley  Batuley
bba  Baatonum  Baatonum
bbb  Barai  Barai
bbc  Batak Toba  Batak Toba
bbd  Bau  Bau
bbe  Bangba  Bangba
bbf  Baibai  Baibai
bbg  Barama  Barama
bbh  Bugan  Bugan
bbi  Barombi  Barombi
bbj  Ghomálá'  Ghomálá'
bbk  Babanki  Babanki
bbl  Bats  Bats
bbm  Babango  Babango
bbn  Uneapa  Uneapa
bbo  Konabéré  Konabéré
bbo  Northern Bobo Madaré  Bobo Madaré, Northern
bbp  West Central Banda  Banda, West Central
bbq  Bamali  Bamali
bbr  Girawa  Girawa
bbs  Bakpinka  Bakpinka
bbt  Mburku  Mburku
bbu  Kulung (Nigeria)  Kulung (Nigeria)
bbv  Karnai  Karnai
bbw  Baba  Baba
bbx  Bubia  Bubia
bby  Befang  Befang
bbz  Babalia Creole Arabic  Creole Arabic, Babalia
bca  Central Bai  Bai, Central
bcb  Bainouk-Samik  Bainouk-Samik
bcc  Southern Balochi  Balochi, Southern
bcd  North Babar  Babar, North
bce  Bamenyam  Bamenyam
bcf  Bamu  Bamu
bcg  Baga Binari  Baga Binari
bch  Bariai  Bariai
bci  Baoulé  Baoulé
bcj  Bardi  Bardi
bck  Bunaba  Bunaba
bcl  Central Bikol  Bikol, Central
bcm  Bannoni  Bannoni
bcn  Bali (Nigeria)  Bali (Nigeria)
bco  Kaluli  Kaluli
bcp  Bali (Democratic Republic of Congo)  Bali (Democratic Republic of Congo)
bcq  Bench  Bench
bcr  Babine  Babine
bcs  Kohumono  Kohumono
bct  Bendi  Bendi
bcu  Awad Bing  Awad Bing
bcv  Shoo-Minda-Nye  Shoo-Minda-Nye
bcw  Bana  Bana
bcy  Bacama  Bacama
bcz  Bainouk-Gunyaamolo  Bainouk-Gunyaamolo
bda  Bayot  Bayot
bdb  Basap  Basap
bdc  Emberá-Baudó  Emberá-Baudó
bdd  Bunama  Bunama
bde  Bade  Bade
bdf  Biage  Biage
bdg  Bonggi  Bonggi
bdh  Baka (Sudan)  Baka (Sudan)
bdi  Burun  Burun
bdj  Bai  Bai
bdk  Budukh  Budukh
bdl  Indonesian Bajau  Bajau, Indonesian
bdm  Buduma  Buduma
bdn  Baldemu  Baldemu
bdo  Morom  Morom
bdp  Bende  Bende
bdq  Bahnar  Bahnar
bdr  West Coast Bajau  Bajau, West Coast
bds  Burunge  Burunge
bdt  Bokoto  Bokoto
bdu  Oroko  Oroko
bdv  Bodo Parja  Bodo Parja
bdw  Baham  Baham
bdx  Budong-Budong  Budong-Budong
bdy  Bandjalang  Bandjalang
bdz  Badeshi  Badeshi
bea  Beaver  Beaver
beb  Bebele  Bebele
bec  Iceve-Maci  Iceve-Maci
bed  Bedoanas  Bedoanas
bee  Byangsi  Byangsi
bef  Benabena  Benabena
beg  Belait  Belait
beh  Biali  Biali
bei  Bekati'  Bekati'
bej  Bedawiyet  Bedawiyet
bej  Beja  Beja
bek  Bebeli  Bebeli
bel  Belarusian  Belarusian
bem  Bemba (Zambia)  Bemba (Zambia)
ben  Bengali  Bengali
beo  Beami  Beami
bep  Besoa  Besoa
beq  Beembe  Beembe
bes  Besme  Besme
bet  Guiberoua Béte  Béte, Guiberoua
beu  Blagar  Blagar
bev  Daloa Bété  Bété, Daloa
bew  Betawi  Betawi
bex  Jur Modo  Jur Modo
bey  Beli (Papua New Guinea)  Beli (Papua New Guinea)
bez  Bena (Tanzania)  Bena (Tanzania)
bfa  Bari  Bari
bfb  Pauri Bareli  Bareli, Pauri
bfc  Northern Bai  Bai, Northern
bfd  Bafut  Bafut
bfe  Betaf  Betaf
bfe  Tena  Tena
bff  Bofi  Bofi
bfg  Busang Kayan  Kayan, Busang
bfh  Blafe  Blafe
bfi  British Sign Language  British Sign Language
bfj  Bafanji  Bafanji
bfk  Ban Khor Sign Language  Ban Khor Sign Language
bfl  Banda-Ndélé  Banda-Ndélé
bfm  Mmen  Mmen
bfn  Bunak  Bunak
bfo  Malba Birifor  Birifor, Malba
bfp  Beba  Beba
bfq  Badaga  Badaga
bfr  Bazigar  Bazigar
bfs  Southern Bai  Bai, Southern
bft  Balti  Balti
bfu  Gahri  Gahri
bfw  Bondo  Bondo
bfx  Bantayanon  Bantayanon
bfy  Bagheli  Bagheli
bfz  Mahasu Pahari  Pahari, Mahasu
bga  Gwamhi-Wuri  Gwamhi-Wuri
bgb  Bobongko  Bobongko
bgc  Haryanvi  Haryanvi
bgd  Rathwi Bareli  Bareli, Rathwi
bge  Bauria  Bauria
bgf  Bangandu  Bangandu
bgg  Bugun  Bugun
bgi  Giangan  Giangan
bgj  Bangolan  Bangolan
bgk  Bit  Bit
bgk  Buxinhua  Buxinhua
bgl  Bo (Laos)  Bo (Laos)
bgm  Baga Mboteni  Baga Mboteni
bgn  Western Balochi  Balochi, Western
bgo  Baga Koga  Baga Koga
bgp  Eastern Balochi  Balochi, Eastern
bgq  Bagri  Bagri
bgr  Bawm Chin  Chin, Bawm
bgs  Tagabawa  Tagabawa
bgt  Bughotu  Bughotu
bgu  Mbongno  Mbongno
bgv  Warkay-Bipim  Warkay-Bipim
bgw  Bhatri  Bhatri
bgx  Balkan Gagauz Turkish  Turkish, Balkan Gagauz
bgy  Benggoi  Benggoi
bgz  Banggai  Banggai
bha  Bharia  Bharia
bhb  Bhili  Bhili
bhc  Biga  Biga
bhd  Bhadrawahi  Bhadrawahi
bhe  Bhaya  Bhaya
bhf  Odiai  Odiai
bhg  Binandere  Binandere
bhh  Bukharic  Bukharic
bhi  Bhilali  Bhilali
bhj  Bahing  Bahing
bhl  Bimin  Bimin
bhm  Bathari  Bathari
bhn  Bohtan Neo-Aramaic  Neo-Aramaic, Bohtan
bho  Bhojpuri  Bhojpuri
bhp  Bima  Bima
bhq  Tukang Besi South  Tukang Besi South
bhr  Bara Malagasy  Malagasy, Bara
bhs  Buwal  Buwal
bht  Bhattiyali  Bhattiyali
bhu  Bhunjia  Bhunjia
bhv  Bahau  Bahau
bhw  Biak  Biak
bhx  Bhalay  Bhalay
bhy  Bhele  Bhele
bhz  Bada (Indonesia)  Bada (Indonesia)
bia  Badimaya  Badimaya
bib  Bisa  Bisa
bib  Bissa  Bissa
bic  Bikaru  Bikaru
bid  Bidiyo  Bidiyo
bie  Bepour  Bepour
bif  Biafada  Biafada
big  Biangai  Biangai
bij  Vaghat-Ya-Bijim-Legeri  Vaghat-Ya-Bijim-Legeri
bik  Bikol  Bikol
bil  Bile  Bile
bim  Bimoba  Bimoba
bin  Bini  Bini
bin  Edo  Edo
bio  Nai  Nai
bip  Bila  Bila
biq  Bipi  Bipi
bir  Bisorio  Bisorio
bis  Bislama  Bislama
bit  Berinomo  Berinomo
biu  Biete  Biete
biv  Southern Birifor  Birifor, Southern
biw  Kol (Cameroon)  Kol (Cameroon)
bix  Bijori  Bijori
biy  Birhor  Birhor
biz  Baloi  Baloi
bja  Budza  Budza
bjb  Banggarla  Banggarla
bjc  Bariji  Bariji
bje  Biao-Jiao Mien  Mien, Biao-Jiao
bjf  Barzani Jewish Neo-Aramaic  Neo-Aramaic, Barzani Jewish
bjg  Bidyogo  Bidyogo
bjh  Bahinemo  Bahinemo
bji  Burji  Burji
bjj  Kanauji  Kanauji
bjk  Barok  Barok
bjl  Bulu (Papua New Guinea)  Bulu (Papua New Guinea)
bjm  Bajelani  Bajelani
bjn  Banjar  Banjar
bjo  Mid-Southern Banda  Banda, Mid-Southern
bjp  Fanamaket  Fanamaket
bjr  Binumarien  Binumarien
bjs  Bajan  Bajan
bjt  Balanta-Ganja  Balanta-Ganja
bju  Busuu  Busuu
bjv  Bedjond  Bedjond
bjw  Bakwé  Bakwé
bjx  Banao Itneg  Itneg, Banao
bjy  Bayali  Bayali
bjz  Baruga  Baruga
bka  Kyak  Kyak
bkc  Baka (Cameroon)  Baka (Cameroon)
bkd  Binukid  Binukid
bkd  Talaandig  Talaandig
bkf  Beeke  Beeke
bkg  Buraka  Buraka
bkh  Bakoko  Bakoko
bki  Baki  Baki
bkj  Pande  Pande
bkk  Brokskat  Brokskat
bkl  Berik  Berik
bkm  Kom (Cameroon)  Kom (Cameroon)
bkn  Bukitan  Bukitan
bko  Kwa'  Kwa'
bkp  Boko (Democratic Republic of Congo)  Boko (Democratic Republic of Congo)
bkq  Bakairí  Bakairí
bkr  Bakumpai  Bakumpai
bks  Northern Sorsoganon  Sorsoganon, Northern
bkt  Boloki  Boloki
bku  Buhid  Buhid
bkv  Bekwarra  Bekwarra
bkw  Bekwel  Bekwel
bkx  Baikeno  Baikeno
bky  Bokyi  Bokyi
bkz  Bungku  Bungku
bla  Siksika  Siksika
blb  Bilua  Bilua
blc  Bella Coola  Bella Coola
bld  Bolango  Bolango
ble  Balanta-Kentohe  Balanta-Kentohe
blf  Buol  Buol
blg  Balau  Balau
blh  Kuwaa  Kuwaa
bli  Bolia  Bolia
blj  Bolongan  Bolongan
blk  Pa'O  Pa'O
blk  Pa'o Karen  Karen, Pa'o
bll  Biloxi  Biloxi
blm  Beli (Sudan)  Beli (Sudan)
bln  Southern Catanduanes Bikol  Bikol, Southern Catanduanes
blo  Anii  Anii
blp  Blablanga  Blablanga
blq  Baluan-Pam  Baluan-Pam
blr  Blang  Blang
bls  Balaesang  Balaesang
blt  Tai Dam  Tai Dam
blv  Bolo  Bolo
blw  Balangao  Balangao
blx  Mag-Indi Ayta  Ayta, Mag-Indi
bly  Notre  Notre
blz  Balantak  Balantak
bma  Lame  Lame
bmb  Bembe  Bembe
bmc  Biem  Biem
bmd  Baga Manduri  Manduri, Baga
bme  Limassa  Limassa
bmf  Bom  Bom
bmg  Bamwe  Bamwe
bmh  Kein  Kein
bmi  Bagirmi  Bagirmi
bmj  Bote-Majhi  Bote-Majhi
bmk  Ghayavi  Ghayavi
bml  Bomboli  Bomboli
bmm  Northern Betsimisaraka Malagasy  Malagasy, Northern Betsimisaraka
bmn  Bina (Papua New Guinea)  Bina (Papua New Guinea)
bmo  Bambalang  Bambalang
bmp  Bulgebi  Bulgebi
bmq  Bomu  Bomu
bmr  Muinane  Muinane
bms  Bilma Kanuri  Kanuri, Bilma
bmt  Biao Mon  Biao Mon
bmu  Somba-Siawari  Somba-Siawari
bmv  Bum  Bum
bmw  Bomwali  Bomwali
bmx  Baimak  Baimak
bmy  Bemba (Democratic Republic of Congo)  Bemba (Democratic Republic of Congo)
bmz  Baramu  Baramu
bna  Bonerate  Bonerate
bnb  Bookan  Bookan
bnc  Bontok  Bontok
bnd  Banda (Indonesia)  Banda (Indonesia)
bne  Bintauna  Bintauna
bnf  Masiwang  Masiwang
bng  Benga  Benga
bni  Bangi  Bangi
bnj  Eastern Tawbuid  Tawbuid, Eastern
bnk  Bierebo  Bierebo
bnl  Boon  Boon
bnm  Batanga  Batanga
bnn  Bunun  Bunun
bno  Bantoanon  Bantoanon
bnp  Bola  Bola
bnq  Bantik  Bantik
bnr  Butmas-Tur  Butmas-Tur
bns  Bundeli  Bundeli
bnu  Bentong  Bentong
bnv  Beneraf  Beneraf
bnv  Bonerif  Bonerif
bnv  Edwas  Edwas
bnw  Bisis  Bisis
bnx  Bangubangu  Bangubangu
bny  Bintulu  Bintulu
bnz  Beezen  Beezen
boa  Bora  Bora
bob  Aweer  Aweer
bod  Tibetan  Tibetan
boe  Mundabli  Mundabli
bof  Bolon  Bolon
bog  Bamako Sign Language  Bamako Sign Language
boh  Boma  Boma
boi  Barbareño  Barbareño
boj  Anjam  Anjam
bok  Bonjo  Bonjo
bol  Bole  Bole
bom  Berom  Berom
bon  Bine  Bine
boo  Tiemacèwè Bozo  Bozo, Tiemacèwè
bop  Bonkiman  Bonkiman
boq  Bogaya  Bogaya
bor  Borôro  Borôro
bos  Bosnian  Bosnian
bot  Bongo  Bongo
bou  Bondei  Bondei
bov  Tuwuli  Tuwuli
bow  Rema  Rema
box  Buamu  Buamu
boy  Bodo (Central African Republic)  Bodo (Central African Republic)
boz  Tiéyaxo Bozo  Bozo, Tiéyaxo
bpa  Daakaka  Daakaka
bpb  Barbacoas  Barbacoas
bpd  Banda-Banda  Banda-Banda
bpg  Bonggo  Bonggo
bph  Botlikh  Botlikh
bpi  Bagupi  Bagupi
bpj  Binji  Binji
bpk  'Ôrôê  'Ôrôê
bpk  Orowe  Orowe
bpl  Broome Pearling Lugger Pidgin  Broome Pearling Lugger Pidgin
bpm  Biyom  Biyom
bpn  Dzao Min  Dzao Min
bpo  Anasi  Anasi
bpp  Kaure  Kaure
bpq  Banda Malay  Malay, Banda
bpr  Koronadal Blaan  Blaan, Koronadal
bps  Sarangani Blaan  Blaan, Sarangani
bpt  Barrow Point  Barrow Point
bpu  Bongu  Bongu
bpv  Bian Marind  Marind, Bian
bpw  Bo (Papua New Guinea)  Bo (Papua New Guinea)
bpx  Palya Bareli  Bareli, Palya
bpy  Bishnupriya  Bishnupriya
bpz  Bilba  Bilba
bqa  Tchumbuli  Tchumbuli
bqb  Bagusa  Bagusa
bqc  Boko (Benin)  Boko (Benin)
bqc  Boo  Boo
bqd  Bung  Bung
bqf  Baga Kaloum  Baga Kaloum
bqg  Bago-Kusuntu  Bago-Kusuntu
bqh  Baima  Baima
bqi  Bakhtiari  Bakhtiari
bqj  Bandial  Bandial
bqk  Banda-Mbrès  Banda-Mbrès
bql  Bilakura  Bilakura
bqm  Wumboko  Wumboko
bqn  Bulgarian Sign Language  Bulgarian Sign Language
bqo  Balo  Balo
bqp  Busa  Busa
bqq  Biritai  Biritai
bqr  Burusu  Burusu
bqs  Bosngun  Bosngun
bqt  Bamukumbit  Bamukumbit
bqu  Boguru  Boguru
bqv  Begbere-Ejar  Begbere-Ejar
bqv  Koro Wachi  Koro Wachi
bqw  Buru (Nigeria)  Buru (Nigeria)
bqx  Baangi  Baangi
bqy  Bengkala Sign Language  Bengkala Sign Language
bqz  Bakaka  Bakaka
bra  Braj  Braj
brb  Lave  Lave
brc  Berbice Creole Dutch  Creole Dutch, Berbice
brd  Baraamu  Baraamu
bre  Breton  Breton
brf  Bera  Bera
brg  Baure  Baure
brh  Brahui  Brahui
bri  Mokpwe  Mokpwe
brj  Bieria  Bieria
brk  Birked  Birked
brl  Birwa  Birwa
brm  Barambu  Barambu
brn  Boruca  Boruca
bro  Brokkat  Brokkat
brp  Barapasi  Barapasi
brq  Breri  Breri
brr  Birao  Birao
brs  Baras  Baras
brt  Bitare  Bitare
bru  Eastern Bru  Bru, Eastern
brv  Western Bru  Bru, Western
brw  Bellari  Bellari
brx  Bodo (India)  Bodo (India)
bry  Burui  Burui
brz  Bilbil  Bilbil
bsa  Abinomn  Abinomn
bsb  Brunei Bisaya  Bisaya, Brunei
bsc  Bassari  Bassari
bsc  Oniyan  Oniyan
bse  Wushi  Wushi
bsf  Bauchi  Bauchi
bsg  Bashkardi  Bashkardi
bsh  Kati  Kati
bsi  Bassossi  Bassossi
bsj  Bangwinji  Bangwinji
bsk  Burushaski  Burushaski
bsl  Basa-Gumna  Basa-Gumna
bsm  Busami  Busami
bsn  Barasana-Eduria  Barasana-Eduria
bso  Buso  Buso
bsp  Baga Sitemu  Baga Sitemu
bsq  Bassa  Bassa
bsr  Bassa-Kontagora  Bassa-Kontagora
bss  Akoose  Akoose
bst  Basketo  Basketo
bsu  Bahonsuai  Bahonsuai
bsv  Baga Sobané  Baga Sobané
bsw  Baiso  Baiso
bsx  Yangkam  Yangkam
bsy  Sabah Bisaya  Bisaya, Sabah
bta  Bata  Bata
btc  Bati (Cameroon)  Bati (Cameroon)
btd  Batak Dairi  Batak Dairi
bte  Gamo-Ningi  Gamo-Ningi
btf  Birgit  Birgit
btg  Gagnoa Bété  Bété, Gagnoa
bth  Biatah Bidayuh  Bidayuh, Biatah
bti  Burate  Burate
btj  Bacanese Malay  Malay, Bacanese
btl  Bhatola  Bhatola
btm  Batak Mandailing  Batak Mandailing
btn  Ratagnon  Ratagnon
bto  Rinconada Bikol  Bikol, Rinconada
btp  Budibud  Budibud
btq  Batek  Batek
btr  Baetora  Baetora
bts  Batak Simalungun  Batak Simalungun
btt  Bete-Bendi  Bete-Bendi
btu  Batu  Batu
btv  Bateri  Bateri
btw  Butuanon  Butuanon
btx  Batak Karo  Batak Karo
bty  Bobot  Bobot
btz  Batak Alas-Kluet  Batak Alas-Kluet
bua  Buriat  Buriat
bub  Bua  Bua
buc  Bushi  Bushi
bud  Ntcham  Ntcham
bue  Beothuk  Beothuk
buf  Bushoong  Bushoong
bug  Buginese  Buginese
buh  Younuo Bunu  Bunu, Younuo
bui  Bongili  Bongili
buj  Basa-Gurmana  Basa-Gurmana
buk  Bugawac  Bugawac
bul  Bulgarian  Bulgarian
bum  Bulu (Cameroon)  Bulu (Cameroon)
bun  Sherbro  Sherbro
buo  Terei  Terei
bup  Busoa  Busoa
buq  Brem  Brem
bus  Bokobaru  Bokobaru
but  Bungain  Bungain
buu  Budu  Budu
buv  Bun  Bun
buw  Bubi  Bubi
bux  Boghom  Boghom
buy  Bullom So  Bullom So
buz  Bukwen  Bukwen
bva  Barein  Barein
bvb  Bube  Bube
bvc  Baelelea  Baelelea
bvd  Baeggu  Baeggu
bve  Berau Malay  Malay, Berau
bvf  Boor  Boor
bvg  Bonkeng  Bonkeng
bvh  Bure  Bure
bvi  Belanda Viri  Belanda Viri
bvj  Baan  Baan
bvk  Bukat  Bukat
bvl  Bolivian Sign Language  Bolivian Sign Language
bvm  Bamunka  Bamunka
bvn  Buna  Buna
bvo  Bolgo  Bolgo
bvp  Bumang  Bumang
bvq  Birri  Birri
bvr  Burarra  Burarra
bvt  Bati (Indonesia)  Bati (Indonesia)
bvu  Bukit Malay  Malay, Bukit
bvv  Baniva  Baniva
bvw  Boga  Boga
bvx  Dibole  Dibole
bvy  Baybayanon  Baybayanon
bvz  Bauzi  Bauzi
bwa  Bwatoo  Bwatoo
bwb  Namosi-Naitasiri-Serua  Namosi-Naitasiri-Serua
bwc  Bwile  Bwile
bwd  Bwaidoka  Bwaidoka
bwe  Bwe Karen  Karen, Bwe
bwf  Boselewa  Boselewa
bwg  Barwe  Barwe
bwh  Bishuo  Bishuo
bwi  Baniwa  Baniwa
bwj  Láá Láá Bwamu  Bwamu, Láá Láá
bwk  Bauwaki  Bauwaki
bwl  Bwela  Bwela
bwm  Biwat  Biwat
bwn  Wunai Bunu  Bunu, Wunai
bwo  Borna (Ethiopia)  Borna (Ethiopia)
bwo  Boro (Ethiopia)  Boro (Ethiopia)
bwp  Mandobo Bawah  Mandobo Bawah
bwq  Southern Bobo Madaré  Bobo Madaré, Southern
bwr  Bura-Pabir  Bura-Pabir
bws  Bomboma  Bomboma
bwt  Bafaw-Balong  Bafaw-Balong
bwu  Buli (Ghana)  Buli (Ghana)
bww  Bwa  Bwa
bwx  Bu-Nao Bunu  Bunu, Bu-Nao
bwy  Cwi Bwamu  Bwamu, Cwi
bwz  Bwisi  Bwisi
bxa  Tairaha  Tairaha
bxb  Belanda Bor  Bor, Belanda
bxc  Molengue  Molengue
bxd  Pela  Pela
bxe  Birale  Birale
bxf  Bilur  Bilur
bxf  Minigir  Minigir
bxg  Bangala  Bangala
bxh  Buhutu  Buhutu
bxi  Pirlatapa  Pirlatapa
bxj  Bayungu  Bayungu
bxk  Bukusu  Bukusu
bxk  Lubukusu  Lubukusu
bxl  Jalkunan  Jalkunan
bxm  Mongolia Buriat  Buriat, Mongolia
bxn  Burduna  Burduna
bxo  Barikanchi  Barikanchi
bxp  Bebil  Bebil
bxq  Beele  Beele
bxr  Russia Buriat  Buriat, Russia
bxs  Busam  Busam
bxu  China Buriat  Buriat, China
bxv  Berakou  Berakou
bxw  Bankagooma  Bankagooma
bxx  Borna (Democratic Republic of Congo)  Borna (Democratic Republic of Congo)
bxz  Binahari  Binahari
bya  Batak  Batak
byb  Bikya  Bikya
byc  Ubaghara  Ubaghara
byd  Benyadu'  Benyadu'
bye  Pouye  Pouye
byf  Bete  Bete
byg  Baygo  Baygo
byh  Bhujel  Bhujel
byi  Buyu  Buyu
byj  Bina (Nigeria)  Bina (Nigeria)
byk  Biao  Biao
byl  Bayono  Bayono
bym  Bidyara  Bidyara
byn  Bilin  Bilin
byn  Blin  Blin
byo  Biyo  Biyo
byp  Bumaji  Bumaji
byq  Basay  Basay
byr  Baruya  Baruya
byr  Yipma  Yipma
bys  Burak  Burak
byt  Berti  Berti
byv  Medumba  Medumba
byw  Belhariya  Belhariya
byx  Qaqet  Qaqet
byy  Buya  Buya
byz  Banaro  Banaro
bza  Bandi  Bandi
bzb  Andio  Andio
bzc  Southern Betsimisaraka Malagasy  Malagasy, Southern Betsimisaraka
bzd  Bribri  Bribri
bze  Jenaama Bozo  Bozo, Jenaama
bzf  Boikin  Boikin
bzg  Babuza  Babuza
bzh  Mapos Buang  Buang, Mapos
bzi  Bisu  Bisu
bzj  Belize Kriol English  Kriol English, Belize
bzk  Nicaragua Creole English  Creole English, Nicaragua
bzl  Boano (Sulawesi)  Boano (Sulawesi)
bzm  Bolondo  Bolondo
bzn  Boano (Maluku)  Boano (Maluku)
bzo  Bozaba  Bozaba
bzp  Kemberano  Kemberano
bzq  Buli (Indonesia)  Buli (Indonesia)
bzr  Biri  Biri
bzs  Brazilian Sign Language  Brazilian Sign Language
bzt  Brithenig  Brithenig
bzu  Burmeso  Burmeso
bzv  Naami  Naami
bzw  Basa (Nigeria)  Basa (Nigeria)
bzx  Kɛlɛngaxo Bozo  Bozo, Kɛlɛngaxo
bzy  Obanliku  Obanliku
bzz  Evant  Evant
caa  Chortí  Chortí
cab  Garifuna  Garifuna
cac  Chuj  Chuj
cad  Caddo  Caddo
cae  Laalaa  Laalaa
cae  Lehar  Lehar
caf  Southern Carrier  Carrier, Southern
cag  Nivaclé  Nivaclé
cah  Cahuarano  Cahuarano
caj  Chané  Chané
cak  Cakchiquel  Cakchiquel
cak  Kaqchikel  Kaqchikel
cal  Carolinian  Carolinian
cam  Cemuhî  Cemuhî
can  Chambri  Chambri
cao  Chácobo  Chácobo
cap  Chipaya  Chipaya
caq  Car Nicobarese  Nicobarese, Car
car  Galibi Carib  Carib, Galibi
cas  Tsimané  Tsimané
cat  Catalan  Catalan
cat  Valencian  Valencian
cav  Cavineña  Cavineña
caw  Callawalla  Callawalla
cax  Chiquitano  Chiquitano
cay  Cayuga  Cayuga
caz  Canichana  Canichana
cbb  Cabiyarí  Cabiyarí
cbc  Carapana  Carapana
cbd  Carijona  Carijona
cbe  Chipiajes  Chipiajes
cbg  Chimila  Chimila
cbh  Cagua  Cagua
cbi  Chachi  Chachi
cbj  Ede Cabe  Ede Cabe
cbk  Chavacano  Chavacano
cbl  Bualkhaw Chin  Chin, Bualkhaw
cbn  Nyahkur  Nyahkur
cbo  Izora  Izora
cbr  Cashibo-Cacataibo  Cashibo-Cacataibo
cbs  Cashinahua  Cashinahua
cbt  Chayahuita  Chayahuita
cbu  Candoshi-Shapra  Candoshi-Shapra
cbv  Cacua  Cacua
cbw  Kinabalian  Kinabalian
cby  Carabayo  Carabayo
cca  Cauca  Cauca
ccc  Chamicuro  Chamicuro
ccd  Cafundo Creole  Creole, Cafundo
cce  Chopi  Chopi
ccg  Samba Daka  Daka, Samba
cch  Atsam  Atsam
ccj  Kasanga  Kasanga
ccl  Cutchi-Swahili  Cutchi-Swahili
ccm  Malaccan Creole Malay  Creole Malay, Malaccan
cco  Comaltepec Chinantec  Chinantec, Comaltepec
ccp  Chakma  Chakma
ccr  Cacaopera  Cacaopera
cda  Choni  Choni
cde  Chenchu  Chenchu
cdf  Chiru  Chiru
cdg  Chamari  Chamari
cdh  Chambeali  Chambeali
cdi  Chodri  Chodri
cdj  Churahi  Churahi
cdm  Chepang  Chepang
cdn  Chaudangsi  Chaudangsi
cdo  Min Dong Chinese  Chinese, Min Dong
cdr  Cinda-Regi-Tiyal  Cinda-Regi-Tiyal
cds  Chadian Sign Language  Chadian Sign Language
cdy  Chadong  Chadong
cdz  Koda  Koda
cea  Lower Chehalis  Chehalis, Lower
ceb  Cebuano  Cebuano
ceg  Chamacoco  Chamacoco
cek  Eastern Khumi Chin  Chin, Eastern Khumi
cen  Cen  Cen
ces  Czech  Czech
cet  Centúúm  Centúúm
cfa  Dijim-Bwilim  Dijim-Bwilim
cfd  Cara  Cara
cfg  Como Karim  Como Karim
cfm  Falam Chin  Chin, Falam
cga  Changriwa  Changriwa
cgc  Kagayanen  Kagayanen
cgg  Chiga  Chiga
cgk  Chocangacakha  Chocangacakha
cha  Chamorro  Chamorro
chb  Chibcha  Chibcha
chc  Catawba  Catawba
chd  Highland Oaxaca Chontal  Chontal, Highland Oaxaca
che  Chechen  Chechen
chf  Tabasco Chontal  Chontal, Tabasco
chg  Chagatai  Chagatai
chh  Chinook  Chinook
chj  Ojitlán Chinantec  Chinantec, Ojitlán
chk  Chuukese  Chuukese
chl  Cahuilla  Cahuilla
chm  Mari (Russia)  Mari (Russia)
chn  Chinook jargon  Chinook jargon
cho  Choctaw  Choctaw
chp  Chipewyan  Chipewyan
chp  Dene Suline  Dene Suline
chq  Quiotepec Chinantec  Chinantec, Quiotepec
chr  Cherokee  Cherokee
cht  Cholón  Cholón
chu  Church Slavic  Slavic, Church
chu  Church Slavonic  Slavonic, Church
chu  Old Bulgarian  Bulgarian, Old
chu  Old Church Slavonic  Slavonic, Old Church
chu  Old Slavonic  Slavonic, Old
chv  Chuvash  Chuvash
chw  Chuwabu  Chuwabu
chx  Chantyal  Chantyal
chy  Cheyenne  Cheyenne
chz  Ozumacín Chinantec  Chinantec, Ozumacín
cia  Cia-Cia  Cia-Cia
cib  Ci Gbe  Gbe, Ci
cic  Chickasaw  Chickasaw
cid  Chimariko  Chimariko
cie  Cineni  Cineni
cih  Chinali  Chinali
cik  Chitkuli Kinnauri  Kinnauri, Chitkuli
cim  Cimbrian  Cimbrian
cin  Cinta Larga  Cinta Larga
cip  Chiapanec  Chiapanec
cir  Haméa  Haméa
cir  Méa  Méa
cir  Tiri  Tiri
ciw  Chippewa  Chippewa
ciy  Chaima  Chaima
cja  Western Cham  Cham, Western
cje  Chru  Chru
cjh  Upper Chehalis  Chehalis, Upper
cji  Chamalal  Chamalal
cjk  Chokwe  Chokwe
cjm  Eastern Cham  Cham, Eastern
cjn  Chenapian  Chenapian
cjo  Ashéninka Pajonal  Ashéninka Pajonal
cjp  Cabécar  Cabécar
cjs  Shor  Shor
cjv  Chuave  Chuave
cjy  Jinyu Chinese  Chinese, Jinyu
ckb  Central Kurdish  Kurdish, Central
ckh  Chak  Chak
ckl  Cibak  Cibak
ckn  Kaang Chin  Chin, Kaang
cko  Anufo  Anufo
ckq  Kajakse  Kajakse
ckr  Kairak  Kairak
cks  Tayo  Tayo
ckt  Chukot  Chukot
cku  Koasati  Koasati
ckv  Kavalan  Kavalan
ckx  Caka  Caka
cky  Cakfem-Mushere  Cakfem-Mushere
ckz  Cakchiquel-Quiché Mixed Language  Cakchiquel-Quiché Mixed Language
cla  Ron  Ron
clc  Chilcotin  Chilcotin
cld  Chaldean Neo-Aramaic  Neo-Aramaic, Chaldean
cle  Lealao Chinantec  Chinantec, Lealao
clh  Chilisso  Chilisso
cli  Chakali  Chakali
clj  Laitu Chin  Chin, Laitu
clk  Idu-Mishmi  Idu-Mishmi
cll  Chala  Chala
clm  Clallam  Clallam
clo  Lowland Oaxaca Chontal  Chontal, Lowland Oaxaca
clt  Lautu Chin  Chin, Lautu
clu  Caluyanun  Caluyanun
clw  Chulym  Chulym
cly  Eastern Highland Chatino  Chatino, Eastern Highland
cma  Maa  Maa
cme  Cerma  Cerma
cmg  Classical Mongolian  Mongolian, Classical
cmi  Emberá-Chamí  Emberá-Chamí
cml  Campalagian  Campalagian
cmm  Michigamea  Michigamea
cmn  Mandarin Chinese  Chinese, Mandarin
cmo  Central Mnong  Mnong, Central
cmr  Mro-Khimi Chin  Chin, Mro-Khimi
cms  Messapic  Messapic
cmt  Camtho  Camtho
cna  Changthang  Changthang
cnb  Chinbon Chin  Chin, Chinbon
cnc  Côông  Côông
cng  Northern Qiang  Qiang, Northern
cnh  Haka Chin  Chin, Haka
cni  Asháninka  Asháninka
cnk  Khumi Chin  Chin, Khumi
cnl  Lalana Chinantec  Chinantec, Lalana
cno  Con  Con
cns  Central Asmat  Asmat, Central
cnt  Tepetotutla Chinantec  Chinantec, Tepetotutla
cnu  Chenoua  Chenoua
cnw  Ngawn Chin  Chin, Ngawn
cnx  Middle Cornish  Cornish, Middle
coa  Cocos Islands Malay  Malay, Cocos Islands
cob  Chicomuceltec  Chicomuceltec
coc  Cocopa  Cocopa
cod  Cocama-Cocamilla  Cocama-Cocamilla
coe  Koreguaje  Koreguaje
cof  Colorado  Colorado
cog  Chong  Chong
coh  Chichonyi-Chidzihana-Chikauma  Chichonyi-Chidzihana-Chikauma
coh  Chonyi-Dzihana-Kauma  Chonyi-Dzihana-Kauma
coj  Cochimi  Cochimi
cok  Santa Teresa Cora  Cora, Santa Teresa
col  Columbia-Wenatchi  Columbia-Wenatchi
com  Comanche  Comanche
con  Cofán  Cofán
coo  Comox  Comox
cop  Coptic  Coptic
coq  Coquille  Coquille
cor  Cornish  Cornish
cos  Corsican  Corsican
cot  Caquinte  Caquinte
cou  Wamey  Wamey
cov  Cao Miao  Cao Miao
cow  Cowlitz  Cowlitz
cox  Nanti  Nanti
coy  Coyaima  Coyaima
coz  Chochotec  Chochotec
cpa  Palantla Chinantec  Chinantec, Palantla
cpb  Ucayali-Yurúa Ashéninka  Ashéninka, Ucayali-Yurúa
cpc  Ajyíninka Apurucayali  Ajyíninka Apurucayali
cpg  Cappadocian Greek  Greek, Cappadocian
cpi  Chinese Pidgin English  Pidgin English, Chinese
cpn  Cherepon  Cherepon
cpo  Kpeego  Kpeego
cps  Capiznon  Capiznon
cpu  Pichis Ashéninka  Ashéninka, Pichis
cpx  Pu-Xian Chinese  Chinese, Pu-Xian
cpy  South Ucayali Ashéninka  Ashéninka, South Ucayali
cqd  Chuanqiandian Cluster Miao  Miao, Chuanqiandian Cluster
cqu  Chilean Quechua  Quechua, Chilean
cra  Chara  Chara
crb  Island Carib  Carib, Island
crc  Lonwolwol  Lonwolwol
crd  Coeur d'Alene  Coeur d'Alene
cre  Cree  Cree
crf  Caramanta  Caramanta
crg  Michif  Michif
crh  Crimean Tatar  Tatar, Crimean
crh  Crimean Turkish  Turkish, Crimean
cri  Sãotomense  Sãotomense
crj  Southern East Cree  Cree, Southern East
crk  Plains Cree  Cree, Plains
crl  Northern East Cree  Cree, Northern East
crm  Moose Cree  Cree, Moose
crn  El Nayar Cora  Cora, El Nayar
cro  Crow  Crow
crq  Iyo'wujwa Chorote  Chorote, Iyo'wujwa
crr  Carolina Algonquian  Algonquian, Carolina
crs  Seselwa Creole French  Creole French, Seselwa
crt  Iyojwa'ja Chorote  Chorote, Iyojwa'ja
crv  Chaura  Chaura
crw  Chrau  Chrau
crx  Carrier  Carrier
cry  Cori  Cori
crz  Cruzeño  Cruzeño
csa  Chiltepec Chinantec  Chinantec, Chiltepec
csb  Kashubian  Kashubian
csc  Catalan Sign Language  Catalan Sign Language
csc  Lengua de señas catalana  Lengua de señas catalana
csc  Llengua de Signes Catalana  Llengua de Signes Catalana
csd  Chiangmai Sign Language  Chiangmai Sign Language
cse  Czech Sign Language  Czech Sign Language
csf  Cuba Sign Language  Cuba Sign Language
csg  Chilean Sign Language  Chilean Sign Language
csh  Asho Chin  Chin, Asho
csi  Coast Miwok  Miwok, Coast
csj  Songlai Chin  Chin, Songlai
csk  Jola-Kasa  Jola-Kasa
csl  Chinese Sign Language  Chinese Sign Language
csm  Central Sierra Miwok  Miwok, Central Sierra
csn  Colombian Sign Language  Colombian Sign Language
cso  Sochiapam Chinantec  Chinantec, Sochiapam
cso  Sochiapan Chinantec  Chinantec, Sochiapan
csq  Croatia Sign Language  Croatia Sign Language
csr  Costa Rican Sign Language  Costa Rican Sign Language
css  Southern Ohlone  Ohlone, Southern
cst  Northern Ohlone  Ohlone, Northern
csv  Sumtu Chin  Chin, Sumtu
csw  Swampy Cree  Cree, Swampy
csy  Siyin Chin  Chin, Siyin
csz  Coos  Coos
cta  Tataltepec Chatino  Chatino, Tataltepec
ctc  Chetco  Chetco
ctd  Tedim Chin  Chin, Tedim
cte  Tepinapa Chinantec  Chinantec, Tepinapa
ctg  Chittagonian  Chittagonian
cth  Thaiphum Chin  Chin, Thaiphum
ctl  Tlacoatzintepec Chinantec  Chinantec, Tlacoatzintepec
ctm  Chitimacha  Chitimacha
ctn  Chhintange  Chhintange
cto  Emberá-Catío  Emberá-Catío
ctp  Western Highland Chatino  Chatino, Western Highland
cts  Northern Catanduanes Bikol  Bikol, Northern Catanduanes
ctt  Wayanad Chetti  Chetti, Wayanad
ctu  Chol  Chol
ctz  Zacatepec Chatino  Chatino, Zacatepec
cua  Cua  Cua
cub  Cubeo  Cubeo
cuc  Usila Chinantec  Chinantec, Usila
cug  Cung  Cung
cuh  Chuka  Chuka
cuh  Gichuka  Gichuka
cui  Cuiba  Cuiba
cuj  Mashco Piro  Mashco Piro
cuk  San Blas Kuna  Kuna, San Blas
cul  Culina  Culina
cul  Kulina  Kulina
cum  Cumeral  Cumeral
cuo  Cumanagoto  Cumanagoto
cup  Cupeño  Cupeño
cuq  Cun  Cun
cur  Chhulung  Chhulung
cut  Teutila Cuicatec  Cuicatec, Teutila
cuu  Tai Ya  Tai Ya
cuv  Cuvok  Cuvok
cuw  Chukwa  Chukwa
cux  Tepeuxila Cuicatec  Cuicatec, Tepeuxila
cvg  Chug  Chug
cvn  Valle Nacional Chinantec  Chinantec, Valle Nacional
cwa  Kabwa  Kabwa
cwb  Maindo  Maindo
cwd  Woods Cree  Cree, Woods
cwe  Kwere  Kwere
cwg  Cheq Wong  Cheq Wong
cwg  Chewong  Chewong
cwt  Kuwaataay  Kuwaataay
cya  Nopala Chatino  Chatino, Nopala
cyb  Cayubaba  Cayubaba
cym  Welsh  Welsh
cyo  Cuyonon  Cuyonon
czh  Huizhou Chinese  Chinese, Huizhou
czk  Knaanic  Knaanic
czn  Zenzontepec Chatino  Chatino, Zenzontepec
czo  Min Zhong Chinese  Chinese, Min Zhong
czt  Zotung Chin  Chin, Zotung
daa  Dangaléat  Dangaléat
dac  Dambi  Dambi
dad  Marik  Marik
dae  Duupa  Duupa
dag  Dagbani  Dagbani
dah  Gwahatike  Gwahatike
dai  Day  Day
daj  Dar Fur Daju  Daju, Dar Fur
dak  Dakota  Dakota
dal  Dahalo  Dahalo
dam  Damakawa  Damakawa
dan  Danish  Danish
dao  Daai Chin  Chin, Daai
daq  Dandami Maria  Maria, Dandami
dar  Dargwa  Dargwa
das  Daho-Doo  Daho-Doo
dau  Dar Sila Daju  Daju, Dar Sila
dav  Dawida  Dawida
dav  Taita  Taita
daw  Davawenyo  Davawenyo
dax  Dayi  Dayi
daz  Dao  Dao
dba  Bangime  Bangime
dbb  Deno  Deno
dbd  Dadiya  Dadiya
dbe  Dabe  Dabe
dbf  Edopi  Edopi
dbg  Dogul Dom Dogon  Dogon, Dogul Dom
dbi  Doka  Doka
dbj  Ida'an  Ida'an
dbl  Dyirbal  Dyirbal
dbm  Duguri  Duguri
dbn  Duriankere  Duriankere
dbo  Dulbu  Dulbu
dbp  Duwai  Duwai
dbq  Daba  Daba
dbr  Dabarre  Dabarre
dbt  Ben Tey Dogon  Dogon, Ben Tey
dbu  Bondum Dom Dogon  Dogon, Bondum Dom
dbv  Dungu  Dungu
dbw  Bankan Tey Dogon  Dogon, Bankan Tey
dby  Dibiyaso  Dibiyaso
dcc  Deccan  Deccan
dcr  Negerhollands  Negerhollands
dda  Dadi Dadi  Dadi Dadi
ddd  Dongotono  Dongotono
dde  Doondo  Doondo
ddg  Fataluku  Fataluku
ddi  West Goodenough  Goodenough, West
ddj  Jaru  Jaru
ddn  Dendi (Benin)  Dendi (Benin)
ddo  Dido  Dido
ddr  Dhudhuroa  Dhudhuroa
dds  Donno So Dogon  Dogon, Donno So
ddw  Dawera-Daweloor  Dawera-Daweloor
dec  Dagik  Dagik
ded  Dedua  Dedua
dee  Dewoin  Dewoin
def  Dezfuli  Dezfuli
deg  Degema  Degema
deh  Dehwari  Dehwari
dei  Demisa  Demisa
dek  Dek  Dek
del  Delaware  Delaware
dem  Dem  Dem
den  Slave (Athapascan)  Slave (Athapascan)
dep  Pidgin Delaware  Delaware, Pidgin
deq  Dendi (Central African Republic)  Dendi (Central African Republic)
der  Deori  Deori
des  Desano  Desano
deu  German  German
dev  Domung  Domung
dez  Dengese  Dengese
dga  Southern Dagaare  Dagaare, Southern
dgb  Bunoge Dogon  Dogon, Bunoge
dgc  Casiguran Dumagat Agta  Agta, Casiguran Dumagat
dgd  Dagaari Dioula  Dagaari Dioula
dge  Degenan  Degenan
dgg  Doga  Doga
dgh  Dghwede  Dghwede
dgi  Northern Dagara  Dagara, Northern
dgk  Dagba  Dagba
dgl  Andaandi  Andaandi
dgl  Dongolawi  Dongolawi
dgn  Dagoman  Dagoman
dgo  Dogri (individual language)  Dogri (individual language)
dgr  Dogrib  Dogrib
dgs  Dogoso  Dogoso
dgt  Ndra'ngith  Ndra'ngith
dgu  Degaru  Degaru
dgw  Daungwurrung  Daungwurrung
dgx  Doghoro  Doghoro
dgz  Daga  Daga
dhd  Dhundari  Dhundari
dhg  Dhangu  Dhangu
dhg  Djangu  Djangu
dhi  Dhimal  Dhimal
dhl  Dhalandji  Dhalandji
dhm  Zemba  Zemba
dhn  Dhanki  Dhanki
dho  Dhodia  Dhodia
dhr  Dhargari  Dhargari
dhs  Dhaiso  Dhaiso
dhu  Dhurga  Dhurga
dhv  Dehu  Dehu
dhv  Drehu  Drehu
dhw  Dhanwar (Nepal)  Dhanwar (Nepal)
dhx  Dhungaloo  Dhungaloo
dia  Dia  Dia
dib  South Central Dinka  Dinka, South Central
dic  Lakota Dida  Dida, Lakota
did  Didinga  Didinga
dif  Dieri  Dieri
dig  Chidigo  Chidigo
dig  Digo  Digo
dih  Kumiai  Kumiai
dii  Dimbong  Dimbong
dij  Dai  Dai
dik  Southwestern Dinka  Dinka, Southwestern
dil  Dilling  Dilling
dim  Dime  Dime
din  Dinka  Dinka
dio  Dibo  Dibo
dip  Northeastern Dinka  Dinka, Northeastern
diq  Dimli (individual language)  Dimli (individual language)
dir  Dirim  Dirim
dis  Dimasa  Dimasa
dit  Dirari  Dirari
diu  Diriku  Diriku
div  Dhivehi  Dhivehi
div  Divehi  Divehi
div  Maldivian  Maldivian
diw  Northwestern Dinka  Dinka, Northwestern
dix  Dixon Reef  Dixon Reef
diy  Diuwe  Diuwe
diz  Ding  Ding
dja  Djadjawurrung  Djadjawurrung
djb  Djinba  Djinba
djc  Dar Daju Daju  Daju, Dar Daju
djd  Djamindjung  Djamindjung
dje  Zarma  Zarma
djf  Djangun  Djangun
dji  Djinang  Djinang
djj  Djeebbana  Djeebbana
djk  Businenge Tongo  Businenge Tongo
djk  Eastern Maroon Creole  Eastern Maroon Creole
djk  Nenge  Nenge
djm  Jamsay Dogon  Dogon, Jamsay
djn  Djauan  Djauan
djo  Jangkang  Jangkang
djr  Djambarrpuyngu  Djambarrpuyngu
dju  Kapriman  Kapriman
djw  Djawi  Djawi
dka  Dakpakha  Dakpakha
dkk  Dakka  Dakka
dkr  Kuijau  Kuijau
dks  Southeastern Dinka  Dinka, Southeastern
dkx  Mazagway  Mazagway
dlg  Dolgan  Dolgan
dlk  Dahalik  Dahalik
dlm  Dalmatian  Dalmatian
dln  Darlong  Darlong
dma  Duma  Duma
dmb  Mombo Dogon  Dogon, Mombo
dmc  Gavak  Gavak
dmd  Madhi Madhi  Madhi Madhi
dme  Dugwor  Dugwor
dmg  Upper Kinabatangan  Kinabatangan, Upper
dmk  Domaaki  Domaaki
dml  Dameli  Dameli
dmm  Dama  Dama
dmo  Kemedzung  Kemedzung
dmr  East Damar  Damar, East
dms  Dampelas  Dampelas
dmu  Dubu  Dubu
dmu  Tebi  Tebi
dmv  Dumpas  Dumpas
dmw  Mudburra  Mudburra
dmx  Dema  Dema
dmy  Demta  Demta
dmy  Sowari  Sowari
dna  Upper Grand Valley Dani  Dani, Upper Grand Valley
dnd  Daonda  Daonda
dne  Ndendeule  Ndendeule
dng  Dungan  Dungan
dni  Lower Grand Valley Dani  Dani, Lower Grand Valley
dnj  Dan  Dan
dnk  Dengka  Dengka
dnn  Dzùùngoo  Dzùùngoo
dnr  Danaru  Danaru
dnt  Mid Grand Valley Dani  Dani, Mid Grand Valley
dnu  Danau  Danau
dnv  Danu  Danu
dnw  Western Dani  Dani, Western
dny  Dení  Dení
doa  Dom  Dom
dob  Dobu  Dobu
doc  Northern Dong  Dong, Northern
doe  Doe  Doe
dof  Domu  Domu
doh  Dong  Dong
doi  Dogri (macrolanguage)  Dogri (macrolanguage)
dok  Dondo  Dondo
dol  Doso  Doso
don  Toura (Papua New Guinea)  Toura (Papua New Guinea)
doo  Dongo  Dongo
dop  Lukpa  Lukpa
doq  Dominican Sign Language  Dominican Sign Language
dor  Dori'o  Dori'o
dos  Dogosé  Dogosé
dot  Dass  Dass
dov  Dombe  Dombe
dow  Doyayo  Doyayo
dox  Bussa  Bussa
doy  Dompo  Dompo
doz  Dorze  Dorze
dpp  Papar  Papar
drb  Dair  Dair
drc  Minderico  Minderico
drd  Darmiya  Darmiya
dre  Dolpo  Dolpo
drg  Rungus  Rungus
dri  C'lela  C'lela
drl  Paakantyi  Paakantyi
drn  West Damar  Damar, West
dro  Daro-Matu Melanau  Melanau, Daro-Matu
drq  Dura  Dura
drr  Dororo  Dororo
drs  Gedeo  Gedeo
drt  Drents  Drents
dru  Rukai  Rukai
dry  Darai  Darai
dsb  Lower Sorbian  Sorbian, Lower
dse  Dutch Sign Language  Dutch Sign Language
dsh  Daasanach  Daasanach
dsi  Disa  Disa
dsl  Danish Sign Language  Danish Sign Language
dsn  Dusner  Dusner
dso  Desiya  Desiya
dsq  Tadaksahak  Tadaksahak
dta  Daur  Daur
dtb  Labuk-Kinabatangan Kadazan  Kadazan, Labuk-Kinabatangan
dtd  Ditidaht  Ditidaht
dth  Adithinngithigh  Adithinngithigh
dti  Ana Tinga Dogon  Dogon, Ana Tinga
dtk  Tene Kan Dogon  Dogon, Tene Kan
dtm  Tomo Kan Dogon  Dogon, Tomo Kan
dto  Tommo So Dogon  Dogon, Tommo So
dtp  Central Dusun  Dusun, Central
dtr  Lotud  Lotud
dts  Toro So Dogon  Dogon, Toro So
dtt  Toro Tegu Dogon  Dogon, Toro Tegu
dtu  Tebul Ure Dogon  Dogon, Tebul Ure
dty  Dotyali  Dotyali
dua  Duala  Duala
dub  Dubli  Dubli
duc  Duna  Duna
dud  Hun-Saare  Hun-Saare
due  Umiray Dumaget Agta  Agta, Umiray Dumaget
duf  Drubea  Drubea
duf  Dumbea  Dumbea
dug  Chiduruma  Chiduruma
dug  Duruma  Duruma
duh  Dungra Bhil  Dungra Bhil
dui  Dumun  Dumun
duj  Dhuwal  Dhuwal
duk  Uyajitaya  Uyajitaya
dul  Alabat Island Agta  Agta, Alabat Island
dum  Middle Dutch (ca. 1050-1350)  Dutch, Middle (ca. 1050-1350)
dun  Dusun Deyah  Dusun Deyah
duo  Dupaninan Agta  Agta, Dupaninan
dup  Duano  Duano
duq  Dusun Malang  Dusun Malang
dur  Dii  Dii
dus  Dumi  Dumi
duu  Drung  Drung
duv  Duvle  Duvle
duw  Dusun Witu  Dusun Witu
dux  Duungooma  Duungooma
duy  Dicamay Agta  Agta, Dicamay
duz  Duli  Duli
dva  Duau  Duau
dwa  Diri  Diri
dwr  Dawro  Dawro
dws  Dutton World Speedwords  Dutton World Speedwords
dww  Dawawa  Dawawa
dya  Dyan  Dyan
dyb  Dyaberdyaber  Dyaberdyaber
dyd  Dyugun  Dyugun
dyg  Villa Viciosa Agta  Agta, Villa Viciosa
dyi  Djimini Senoufo  Senoufo, Djimini
dym  Yanda Dom Dogon  Dogon, Yanda Dom
dyn  Dyangadi  Dyangadi
dyo  Jola-Fonyi  Jola-Fonyi
dyu  Dyula  Dyula
dyy  Dyaabugay  Dyaabugay
dza  Tunzu  Tunzu
dzd  Daza  Daza
dze  Djiwarli  Djiwarli
dzg  Dazaga  Dazaga
dzl  Dzalakha  Dzalakha
dzn  Dzando  Dzando
dzo  Dzongkha  Dzongkha
eaa  Karenggapa  Karenggapa
ebg  Ebughu  Ebughu
ebk  Eastern Bontok  Bontok, Eastern
ebo  Teke-Ebo  Teke-Ebo
ebr  Ebrié  Ebrié
ebu  Embu  Embu
ebu  Kiembu  Kiembu
ecr  Eteocretan  Eteocretan
ecs  Ecuadorian Sign Language  Ecuadorian Sign Language
ecy  Eteocypriot  Eteocypriot
eee  E  E
efa  Efai  Efai
efe  Efe  Efe
efi  Efik  Efik
ega  Ega  Ega
egl  Emilian  Emilian
ego  Eggon  Eggon
egy  Egyptian (Ancient)  Egyptian (Ancient)
ehu  Ehueun  Ehueun
eip  Eipomek  Eipomek
eit  Eitiep  Eitiep
eiv  Askopan  Askopan
eja  Ejamat  Ejamat
eka  Ekajuk  Ekajuk
ekc  Eastern Karnic  Karnic, Eastern
eke  Ekit  Ekit
ekg  Ekari  Ekari
eki  Eki  Eki
ekk  Standard Estonian  Estonian, Standard
ekl  Kol  Kol
ekl  Kol (Bangladesh)  Kol (Bangladesh)
ekm  Elip  Elip
eko  Koti  Koti
ekp  Ekpeye  Ekpeye
ekr  Yace  Yace
eky  Eastern Kayah  Kayah, Eastern
ele  Elepi  Elepi
elh  El Hugeirat  El Hugeirat
eli  Nding  Nding
elk  Elkei  Elkei
ell  Modern Greek (1453-)  Greek, Modern (1453-)
elm  Eleme  Eleme
elo  El Molo  El Molo
elu  Elu  Elu
elx  Elamite  Elamite
ema  Emai-Iuleha-Ora  Emai-Iuleha-Ora
emb  Embaloh  Embaloh
eme  Emerillon  Emerillon
emg  Eastern Meohang  Meohang, Eastern
emi  Mussau-Emira  Mussau-Emira
emk  Eastern Maninkakan  Maninkakan, Eastern
emm  Mamulique  Mamulique
emn  Eman  Eman
emo  Emok  Emok
emp  Northern Emberá  Emberá, Northern
ems  Pacific Gulf Yupik  Yupik, Pacific Gulf
emu  Eastern Muria  Muria, Eastern
emw  Emplawas  Emplawas
emx  Erromintxela  Erromintxela
emy  Epigraphic Mayan  Mayan, Epigraphic
ena  Apali  Apali
enb  Markweeta  Markweeta
enc  En  En
end  Ende  Ende
enf  Forest Enets  Enets, Forest
eng  English  English
enh  Tundra Enets  Enets, Tundra
enm  Middle English (1100-1500)  English, Middle (1100-1500)
enn  Engenni  Engenni
eno  Enggano  Enggano
enq  Enga  Enga
enr  Emem  Emem
enr  Emumu  Emumu
enu  Enu  Enu
env  Enwan (Edu State)  Enwan (Edu State)
enw  Enwan (Akwa Ibom State)  Enwan (Akwa Ibom State)
eot  Beti (Côte d'Ivoire)  Beti (Côte d'Ivoire)
epi  Epie  Epie
epo  Esperanto  Esperanto
era  Eravallan  Eravallan
erg  Sie  Sie
erh  Eruwa  Eruwa
eri  Ogea  Ogea
erk  South Efate  Efate, South
ero  Horpa  Horpa
err  Erre  Erre
ers  Ersu  Ersu
ert  Eritai  Eritai
erw  Erokwanas  Erokwanas
ese  Ese Ejja  Ese Ejja
esh  Eshtehardi  Eshtehardi
esi  North Alaskan Inupiatun  Inupiatun, North Alaskan
esk  Northwest Alaska Inupiatun  Inupiatun, Northwest Alaska
esl  Egypt Sign Language  Egypt Sign Language
esm  Esuma  Esuma
esn  Salvadoran Sign Language  Salvadoran Sign Language
eso  Estonian Sign Language  Estonian Sign Language
esq  Esselen  Esselen
ess  Central Siberian Yupik  Yupik, Central Siberian
est  Estonian  Estonian
esu  Central Yupik  Yupik, Central
etb  Etebi  Etebi
etc  Etchemin  Etchemin
eth  Ethiopian Sign Language  Ethiopian Sign Language
etn  Eton (Vanuatu)  Eton (Vanuatu)
eto  Eton (Cameroon)  Eton (Cameroon)
etr  Edolo  Edolo
ets  Yekhee  Yekhee
ett  Etruscan  Etruscan
etu  Ejagham  Ejagham
etx  Eten  Eten
etz  Semimi  Semimi
eus  Basque  Basque
eve  Even  Even
evh  Uvbie  Uvbie
evn  Evenki  Evenki
ewe  Ewe  Ewe
ewo  Ewondo  Ewondo
ext  Extremaduran  Extremaduran
eya  Eyak  Eyak
eyo  Keiyo  Keiyo
eza  Ezaa  Ezaa
eze  Uzekwe  Uzekwe
faa  Fasu  Fasu
fab  Fa d'Ambu  Fa d'Ambu
fad  Wagi  Wagi
faf  Fagani  Fagani
fag  Finongan  Finongan
fah  Baissa Fali  Fali, Baissa
fai  Faiwol  Faiwol
faj  Faita  Faita
fak  Fang (Cameroon)  Fang (Cameroon)
fal  South Fali  Fali, South
fam  Fam  Fam
fan  Fang (Equatorial Guinea)  Fang (Equatorial Guinea)
fao  Faroese  Faroese
fap  Palor  Palor
far  Fataleka  Fataleka
fas  Persian  Persian
fat  Fanti  Fanti
fau  Fayu  Fayu
fax  Fala  Fala
fay  Southwestern Fars  Fars, Southwestern
faz  Northwestern Fars  Fars, Northwestern
fbl  West Albay Bikol  Bikol, West Albay
fcs  Quebec Sign Language  Quebec Sign Language
fer  Feroge  Feroge
ffi  Foia Foia  Foia Foia
ffm  Maasina Fulfulde  Fulfulde, Maasina
fgr  Fongoro  Fongoro
fia  Nobiin  Nobiin
fie  Fyer  Fyer
fij  Fijian  Fijian
fil  Filipino  Filipino
fil  Pilipino  Pilipino
fin  Finnish  Finnish
fip  Fipa  Fipa
fir  Firan  Firan
fit  Tornedalen Finnish  Finnish, Tornedalen
fiw  Fiwaga  Fiwaga
fkk  Kirya-Konzəl  Kirya-Konzəl
fkv  Kven Finnish  Finnish, Kven
fla  Kalispel-Pend d'Oreille  Kalispel-Pend d'Oreille
flh  Foau  Foau
fli  Fali  Fali
fll  North Fali  Fali, North
fln  Flinders Island  Flinders Island
flr  Fuliiru  Fuliiru
fly  Tsotsitaal  Tsotsitaal
fmp  Fe'fe'  Fe'fe'
fmu  Far Western Muria  Muria, Far Western
fng  Fanagalo  Fanagalo
fni  Fania  Fania
fod  Foodo  Foodo
foi  Foi  Foi
fom  Foma  Foma
fon  Fon  Fon
for  Fore  Fore
fos  Siraya  Siraya
fpe  Fernando Po Creole English  Creole English, Fernando Po
fqs  Fas  Fas
fra  French  French
frc  Cajun French  French, Cajun
frd  Fordata  Fordata
frk  Frankish  Frankish
frm  Middle French (ca. 1400-1600)  French, Middle (ca. 1400-1600)
fro  Old French (842-ca. 1400)  French, Old (842-ca. 1400)
frp  Arpitan  Arpitan
frp  Francoprovençal  Francoprovençal
frq  Forak  Forak
frr  Northern Frisian  Frisian, Northern
frs  Eastern Frisian  Frisian, Eastern
frt  Fortsenal  Fortsenal
fry  Western Frisian  Frisian, Western
fse  Finnish Sign Language  Finnish Sign Language
fsl  French Sign Language  French Sign Language
fss  finlandssvenskt teckenspråk  finlandssvenskt teckenspråk
fss  Finland-Swedish Sign Language  Finland-Swedish Sign Language
fss  suomenruotsalainen viittomakieli  suomenruotsalainen viittomakieli
fub  Adamawa Fulfulde  Fulfulde, Adamawa
fuc  Pulaar  Pulaar
fud  East Futuna  Futuna, East
fue  Borgu Fulfulde  Fulfulde, Borgu
fuf  Pular  Pular
fuh  Western Niger Fulfulde  Fulfulde, Western Niger
fui  Bagirmi Fulfulde  Fulfulde, Bagirmi
fuj  Ko  Ko
ful  Fulah  Fulah
fum  Fum  Fum
fun  Fulniô  Fulniô
fuq  Central-Eastern Niger Fulfulde  Fulfulde, Central-Eastern Niger
fur  Friulian  Friulian
fut  Futuna-Aniwa  Futuna-Aniwa
fuu  Furu  Furu
fuv  Nigerian Fulfulde  Fulfulde, Nigerian
fuy  Fuyug  Fuyug
fvr  Fur  Fur
fwa  Fwâi  Fwâi
fwe  Fwe  Fwe
gaa  Ga  Ga
gab  Gabri  Gabri
gac  Mixed Great Andamanese  Great Andamanese, Mixed
gad  Gaddang  Gaddang
gae  Guarequena  Guarequena
gaf  Gende  Gende
gag  Gagauz  Gagauz
gah  Alekano  Alekano
gai  Borei  Borei
gaj  Gadsup  Gadsup
gak  Gamkonora  Gamkonora
gal  Galolen  Galolen
gam  Kandawo  Kandawo
gan  Gan Chinese  Chinese, Gan
gao  Gants  Gants
gap  Gal  Gal
gaq  Gata'  Gata'
gar  Galeya  Galeya
gas  Adiwasi Garasia  Garasia, Adiwasi
gat  Kenati  Kenati
gau  Mudhili Gadaba  Gadaba, Mudhili
gaw  Nobonob  Nobonob
gax  Borana-Arsi-Guji Oromo  Oromo, Borana-Arsi-Guji
gay  Gayo  Gayo
gaz  West Central Oromo  Oromo, West Central
gba  Gbaya (Central African Republic)  Gbaya (Central African Republic)
gbb  Kaytetye  Kaytetye
gbd  Karadjeri  Karadjeri
gbe  Niksek  Niksek
gbf  Gaikundi  Gaikundi
gbg  Gbanziri  Gbanziri
gbh  Defi Gbe  Gbe, Defi
gbi  Galela  Galela
gbj  Bodo Gadaba  Gadaba, Bodo
gbk  Gaddi  Gaddi
gbl  Gamit  Gamit
gbm  Garhwali  Garhwali
gbn  Mo'da  Mo'da
gbo  Northern Grebo  Grebo, Northern
gbp  Gbaya-Bossangoa  Gbaya-Bossangoa
gbq  Gbaya-Bozoum  Gbaya-Bozoum
gbr  Gbagyi  Gbagyi
gbs  Gbesi Gbe  Gbe, Gbesi
gbu  Gagadu  Gagadu
gbv  Gbanu  Gbanu
gbw  Gabi-Gabi  Gabi-Gabi
gbx  Eastern Xwla Gbe  Gbe, Eastern Xwla
gby  Gbari  Gbari
gbz  Zoroastrian Dari  Dari, Zoroastrian
gcc  Mali  Mali
gcd  Ganggalida  Ganggalida
gce  Galice  Galice
gcf  Guadeloupean Creole French  Creole French, Guadeloupean
gcl  Grenadian Creole English  Creole English, Grenadian
gcn  Gaina  Gaina
gcr  Guianese Creole French  Creole French, Guianese
gct  Colonia Tovar German  German, Colonia Tovar
gda  Gade Lohar  Lohar, Gade
gdb  Pottangi Ollar Gadaba  Gadaba, Pottangi Ollar
gdc  Gugu Badhun  Gugu Badhun
gdd  Gedaged  Gedaged
gde  Gude  Gude
gdf  Guduf-Gava  Guduf-Gava
gdg  Ga'dang  Ga'dang
gdh  Gadjerawang  Gadjerawang
gdi  Gundi  Gundi
gdj  Gurdjar  Gurdjar
gdk  Gadang  Gadang
gdl  Dirasha  Dirasha
gdm  Laal  Laal
gdn  Umanakaina  Umanakaina
gdo  Ghodoberi  Ghodoberi
gdq  Mehri  Mehri
gdr  Wipi  Wipi
gds  Ghandruk Sign Language  Ghandruk Sign Language
gdt  Kungardutyi  Kungardutyi
gdu  Gudu  Gudu
gdx  Godwari  Godwari
gea  Geruma  Geruma
geb  Kire  Kire
gec  Gboloo Grebo  Grebo, Gboloo
ged  Gade  Gade
geg  Gengle  Gengle
geh  Hutterisch  Hutterisch
geh  Hutterite German  German, Hutterite
gei  Gebe  Gebe
gej  Gen  Gen
gek  Yiwom  Yiwom
gel  ut-Ma'in  ut-Ma'in
geq  Geme  Geme
ges  Geser-Gorom  Geser-Gorom
gew  Gera  Gera
gex  Garre  Garre
gey  Enya  Enya
gez  Geez  Geez
gfk  Patpatar  Patpatar
gft  Gafat  Gafat
gfx  Mangetti Dune !Xung  !Xung, Mangetti Dune
gga  Gao  Gao
ggb  Gbii  Gbii
ggd  Gugadj  Gugadj
gge  Guragone  Guragone
ggg  Gurgula  Gurgula
ggk  Kungarakany  Kungarakany
ggl  Ganglau  Ganglau
ggm  Gugu Mini  Gugu Mini
ggn  Eastern Gurung  Gurung, Eastern
ggo  Southern Gondi  Gondi, Southern
ggt  Gitua  Gitua
ggu  Gagu  Gagu
ggu  Gban  Gban
ggw  Gogodala  Gogodala
gha  Ghadamès  Ghadamès
ghc  Hiberno-Scottish Gaelic  Gaelic, Hiberno-Scottish
ghe  Southern Ghale  Ghale, Southern
ghh  Northern Ghale  Ghale, Northern
ghk  Geko Karen  Karen, Geko
ghl  Ghulfan  Ghulfan
ghn  Ghanongga  Ghanongga
gho  Ghomara  Ghomara
ghr  Ghera  Ghera
ghs  Guhu-Samane  Guhu-Samane
ght  Kuke  Kuke
ght  Kutang Ghale  Ghale, Kutang
gia  Kitja  Kitja
gib  Gibanawa  Gibanawa
gic  Gail  Gail
gid  Gidar  Gidar
gig  Goaria  Goaria
gih  Githabul  Githabul
gil  Gilbertese  Gilbertese
gim  Gimi (Eastern Highlands)  Gimi (Eastern Highlands)
gin  Hinukh  Hinukh
gip  Gimi (West New Britain)  Gimi (West New Britain)
giq  Green Gelao  Gelao, Green
gir  Red Gelao  Gelao, Red
gis  North Giziga  Giziga, North
git  Gitxsan  Gitxsan
giu  Mulao  Mulao
giw  White Gelao  Gelao, White
gix  Gilima  Gilima
giy  Giyug  Giyug
giz  South Giziga  Giziga, South
gji  Geji  Geji
gjk  Kachi Koli  Koli, Kachi
gjm  Gunditjmara  Gunditjmara
gjn  Gonja  Gonja
gju  Gujari  Gujari
gka  Guya  Guya
gke  Ndai  Ndai
gkn  Gokana  Gokana
gko  Kok-Nar  Kok-Nar
gkp  Guinea Kpelle  Kpelle, Guinea
gla  Gaelic  Gaelic
gla  Scottish Gaelic  Gaelic, Scottish
glc  Bon Gula  Bon Gula
gld  Nanai  Nanai
gle  Irish  Irish
glg  Galician  Galician
glh  Northwest Pashayi  Pashayi, Northwest
gli  Guliguli  Guliguli
glj  Gula Iro  Gula Iro
glk  Gilaki  Gilaki
gll  Garlali  Garlali
glo  Galambu  Galambu
glr  Glaro-Twabo  Glaro-Twabo
glu  Gula (Chad)  Gula (Chad)
glv  Manx  Manx
glw  Glavda  Glavda
gly  Gule  Gule
gma  Gambera  Gambera
gmb  Gula'alaa  Gula'alaa
gmd  Mághdì  Mághdì
gmh  Middle High German (ca. 1050-1500)  German, Middle High (ca. 1050-1500)
gml  Middle Low German  German, Middle Low
gmm  Gbaya-Mbodomo  Gbaya-Mbodomo
gmn  Gimnime  Gimnime
gmu  Gumalu  Gumalu
gmv  Gamo  Gamo
gmx  Magoma  Magoma
gmy  Mycenaean Greek  Greek, Mycenaean
gmz  Mgbolizhia  Mgbolizhia
gna  Kaansa  Kaansa
gnb  Gangte  Gangte
gnc  Guanche  Guanche
gnd  Zulgo-Gemzek  Zulgo-Gemzek
gne  Ganang  Ganang
gng  Ngangam  Ngangam
gnh  Lere  Lere
gni  Gooniyandi  Gooniyandi
gnk  //Gana  //Gana
gnl  Gangulu  Gangulu
gnm  Ginuman  Ginuman
gnn  Gumatj  Gumatj
gno  Northern Gondi  Gondi, Northern
gnq  Gana  Gana
gnr  Gureng Gureng  Gureng Gureng
gnt  Guntai  Guntai
gnu  Gnau  Gnau
gnw  Western Bolivian Guaraní  Guaraní, Western Bolivian
gnz  Ganzi  Ganzi
goa  Guro  Guro
gob  Playero  Playero
goc  Gorakor  Gorakor
god  Godié  Godié
goe  Gongduk  Gongduk
gof  Gofa  Gofa
gog  Gogo  Gogo
goh  Old High German (ca. 750-1050)  German, Old High (ca. 750-1050)
goi  Gobasi  Gobasi
goj  Gowlan  Gowlan
gok  Gowli  Gowli
gol  Gola  Gola
gom  Goan Konkani  Konkani, Goan
gon  Gondi  Gondi
goo  Gone Dau  Gone Dau
gop  Yeretuar  Yeretuar
goq  Gorap  Gorap
gor  Gorontalo  Gorontalo
gos  Gronings  Gronings
got  Gothic  Gothic
gou  Gavar  Gavar
gow  Gorowa  Gorowa
gox  Gobu  Gobu
goy  Goundo  Goundo
goz  Gozarkhani  Gozarkhani
gpa  Gupa-Abawa  Gupa-Abawa
gpe  Ghanaian Pidgin English  Pidgin English, Ghanaian
gpn  Taiap  Taiap
gqa  Ga'anda  Ga'anda
gqi  Guiqiong  Guiqiong
gqn  Guana (Brazil)  Guana (Brazil)
gqr  Gor  Gor
gqu  Qau  Qau
gra  Rajput Garasia  Garasia, Rajput
grb  Grebo  Grebo
grc  Ancient Greek (to 1453)  Greek, Ancient (to 1453)
grd  Guruntum-Mbaaru  Guruntum-Mbaaru
grg  Madi  Madi
grh  Gbiri-Niragu  Gbiri-Niragu
gri  Ghari  Ghari
grj  Southern Grebo  Grebo, Southern
grm  Kota Marudu Talantang  Kota Marudu Talantang
grn  Guarani  Guarani
gro  Groma  Groma
grq  Gorovu  Gorovu
grr  Taznatit  Taznatit
grs  Gresi  Gresi
grt  Garo  Garo
gru  Kistane  Kistane
grv  Central Grebo  Grebo, Central
grw  Gweda  Gweda
grx  Guriaso  Guriaso
gry  Barclayville Grebo  Grebo, Barclayville
grz  Guramalum  Guramalum
gse  Ghanaian Sign Language  Ghanaian Sign Language
gsg  German Sign Language  German Sign Language
gsl  Gusilay  Gusilay
gsm  Guatemalan Sign Language  Guatemalan Sign Language
gsn  Gusan  Gusan
gso  Southwest Gbaya  Gbaya, Southwest
gsp  Wasembo  Wasembo
gss  Greek Sign Language  Greek Sign Language
gsw  Alemannic  Alemannic
gsw  Alsatian  Alsatian
gsw  Swiss German  German, Swiss
gta  Guató  Guató
gti  Gbati-ri  Gbati-ri
gtu  Aghu-Tharnggala  Aghu-Tharnggala
gua  Shiki  Shiki
gub  Guajajára  Guajajára
guc  Wayuu  Wayuu
gud  Yocoboué Dida  Dida, Yocoboué
gue  Gurinji  Gurinji
guf  Gupapuyngu  Gupapuyngu
gug  Paraguayan Guaraní  Guaraní, Paraguayan
guh  Guahibo  Guahibo
gui  Eastern Bolivian Guaraní  Guaraní, Eastern Bolivian
guj  Gujarati  Gujarati
guk  Gumuz  Gumuz
gul  Sea Island Creole English  Creole English, Sea Island
gum  Guambiano  Guambiano
gun  Mbyá Guaraní  Guaraní, Mbyá
guo  Guayabero  Guayabero
gup  Gunwinggu  Gunwinggu
guq  Aché  Aché
gur  Farefare  Farefare
gus  Guinean Sign Language  Guinean Sign Language
gut  Maléku Jaíka  Maléku Jaíka
guu  Yanomamö  Yanomamö
guv  Gey  Gey
guw  Gun  Gun
gux  Gourmanchéma  Gourmanchéma
guz  Ekegusii  Ekegusii
guz  Gusii  Gusii
gva  Guana (Paraguay)  Guana (Paraguay)
gvc  Guanano  Guanano
gve  Duwet  Duwet
gvf  Golin  Golin
gvj  Guajá  Guajá
gvl  Gulay  Gulay
gvm  Gurmana  Gurmana
gvn  Kuku-Yalanji  Kuku-Yalanji
gvo  Gavião Do Jiparaná  Gavião Do Jiparaná
gvp  Pará Gavião  Gavião, Pará
gvr  Western Gurung  Gurung, Western
gvs  Gumawana  Gumawana
gvy  Guyani  Guyani
gwa  Mbato  Mbato
gwb  Gwa  Gwa
gwc  Kalami  Kalami
gwd  Gawwada  Gawwada
gwe  Gweno  Gweno
gwf  Gowro  Gowro
gwg  Moo  Moo
gwi  Gwichʼin  Gwichʼin
gwj  /Gwi  /Gwi
gwm  Awngthim  Awngthim
gwn  Gwandara  Gwandara
gwr  Gwere  Gwere
gwt  Gawar-Bati  Gawar-Bati
gwu  Guwamu  Guwamu
gww  Kwini  Kwini
gwx  Gua  Gua
gxx  Wè Southern  Wè Southern
gya  Northwest Gbaya  Gbaya, Northwest
gyb  Garus  Garus
gyd  Kayardild  Kayardild
gye  Gyem  Gyem
gyf  Gungabula  Gungabula
gyg  Gbayi  Gbayi
gyi  Gyele  Gyele
gyl  Gayil  Gayil
gym  Ngäbere  Ngäbere
gyn  Guyanese Creole English  Creole English, Guyanese
gyr  Guarayu  Guarayu
gyy  Gunya  Gunya
gza  Ganza  Ganza
gzi  Gazi  Gazi
gzn  Gane  Gane
haa  Han  Han
hab  Hanoi Sign Language  Hanoi Sign Language
hac  Gurani  Gurani
had  Hatam  Hatam
hae  Eastern Oromo  Oromo, Eastern
haf  Haiphong Sign Language  Haiphong Sign Language
hag  Hanga  Hanga
hah  Hahon  Hahon
hai  Haida  Haida
haj  Hajong  Hajong
hak  Hakka Chinese  Chinese, Hakka
hal  Halang  Halang
ham  Hewa  Hewa
han  Hangaza  Hangaza
hao  Hakö  Hakö
hap  Hupla  Hupla
haq  Ha  Ha
har  Harari  Harari
has  Haisla  Haisla
hat  Haitian  Haitian
hat  Haitian Creole  Creole, Haitian
hau  Hausa  Hausa
hav  Havu  Havu
haw  Hawaiian  Hawaiian
hax  Southern Haida  Haida, Southern
hay  Haya  Haya
haz  Hazaragi  Hazaragi
hba  Hamba  Hamba
hbb  Huba  Huba
hbn  Heiban  Heiban
hbo  Ancient Hebrew  Hebrew, Ancient
hbs  Serbo-Croatian  Serbo-Croatian
hbu  Habu  Habu
hca  Andaman Creole Hindi  Creole Hindi, Andaman
hch  Huichol  Huichol
hdn  Northern Haida  Haida, Northern
hds  Honduras Sign Language  Honduras Sign Language
hdy  Hadiyya  Hadiyya
hea  Northern Qiandong Miao  Miao, Northern Qiandong
heb  Hebrew  Hebrew
hed  Herdé  Herdé
heg  Helong  Helong
heh  Hehe  Hehe
hei  Heiltsuk  Heiltsuk
hem  Hemba  Hemba
her  Herero  Herero
hgm  Hai//om  Hai//om
hgw  Haigwai  Haigwai
hhi  Hoia Hoia  Hoia Hoia
hhr  Kerak  Kerak
hhy  Hoyahoya  Hoyahoya
hia  Lamang  Lamang
hib  Hibito  Hibito
hid  Hidatsa  Hidatsa
hif  Fiji Hindi  Hindi, Fiji
hig  Kamwe  Kamwe
hih  Pamosu  Pamosu
hii  Hinduri  Hinduri
hij  Hijuk  Hijuk
hik  Seit-Kaitetu  Seit-Kaitetu
hil  Hiligaynon  Hiligaynon
hin  Hindi  Hindi
hio  Tsoa  Tsoa
hir  Himarimã  Himarimã
hit  Hittite  Hittite
hiw  Hiw  Hiw
hix  Hixkaryána  Hixkaryána
hji  Haji  Haji
hka  Kahe  Kahe
hke  Hunde  Hunde
hkk  Hunjara-Kaina Ke  Hunjara-Kaina Ke
hks  Heung Kong Sau Yue  Heung Kong Sau Yue
hks  Hong Kong Sign Language  Hong Kong Sign Language
hla  Halia  Halia
hlb  Halbi  Halbi
hld  Halang Doan  Halang Doan
hle  Hlersu  Hlersu
hlt  Matu Chin  Chin, Matu
hlu  Hieroglyphic Luwian  Luwian, Hieroglyphic
hma  Southern Mashan Hmong  Hmong, Southern Mashan
hma  Southern Mashan Miao  Miao, Southern Mashan
hmb  Humburi Senni Songhay  Songhay, Humburi Senni
hmc  Central Huishui Hmong  Hmong, Central Huishui
hmc  Central Huishui Miao  Miao, Central Huishui
hmd  A-hmaos  A-hmaos
hmd  Da-Hua Miao  Miao, Da-Hua
hmd  Large Flowery Miao  Miao, Large Flowery
hme  Eastern Huishui Hmong  Hmong, Eastern Huishui
hme  Eastern Huishui Miao  Miao, Eastern Huishui
hmf  Hmong Don  Hmong Don
hmg  Southwestern Guiyang Hmong  Hmong, Southwestern Guiyang
hmh  Southwestern Huishui Hmong  Hmong, Southwestern Huishui
hmh  Southwestern Huishui Miao  Miao, Southwestern Huishui
hmi  Northern Huishui Hmong  Hmong, Northern Huishui
hmi  Northern Huishui Miao  Miao, Northern Huishui
hmj  Ge  Ge
hmj  Gejia  Gejia
hmk  Maek  Maek
hml  Luopohe Hmong  Hmong, Luopohe
hml  Luopohe Miao  Miao, Luopohe
hmm  Central Mashan Hmong  Hmong, Central Mashan
hmm  Central Mashan Miao  Miao, Central Mashan
hmn  Hmong  Hmong
hmn  Mong  Mong
hmo  Hiri Motu  Hiri Motu
hmp  Northern Mashan Hmong  Hmong, Northern Mashan
hmp  Northern Mashan Miao  Miao, Northern Mashan
hmq  Eastern Qiandong Miao  Miao, Eastern Qiandong
hmr  Hmar  Hmar
hms  Southern Qiandong Miao  Miao, Southern Qiandong
hmt  Hamtai  Hamtai
hmu  Hamap  Hamap
hmv  Hmong Dô  Hmong Dô
hmw  Western Mashan Hmong  Hmong, Western Mashan
hmw  Western Mashan Miao  Miao, Western Mashan
hmy  Southern Guiyang Hmong  Hmong, Southern Guiyang
hmy  Southern Guiyang Miao  Miao, Southern Guiyang
hmz  Hmong Shua  Hmong Shua
hmz  Sinicized Miao  Miao, Sinicized
hna  Mina (Cameroon)  Mina (Cameroon)
hnd  Southern Hindko  Hindko, Southern
hne  Chhattisgarhi  Chhattisgarhi
hnh  //Ani  //Ani
hni  Hani  Hani
hnj  Hmong Njua  Hmong Njua
hnj  Mong Leng  Mong Leng
hnj  Mong Njua  Mong Njua
hnn  Hanunoo  Hanunoo
hno  Northern Hindko  Hindko, Northern
hns  Caribbean Hindustani  Hindustani, Caribbean
hnu  Hung  Hung
hoa  Hoava  Hoava
hob  Mari (Madang Province)  Mari (Madang Province)
hoc  Ho  Ho
hod  Holma  Holma
hoe  Horom  Horom
hoh  Hobyót  Hobyót
hoi  Holikachuk  Holikachuk
hoj  Hadothi  Hadothi
hoj  Haroti  Haroti
hol  Holu  Holu
hom  Homa  Homa
hoo  Holoholo  Holoholo
hop  Hopi  Hopi
hor  Horo  Horo
hos  Ho Chi Minh City Sign Language  Ho Chi Minh City Sign Language
hot  Hote  Hote
hot  Malê  Malê
hov  Hovongan  Hovongan
how  Honi  Honi
hoy  Holiya  Holiya
hoz  Hozo  Hozo
hpo  Hpon  Hpon
hps  Hawai'i Pidgin Sign Language  Hawai'i Pidgin Sign Language
hra  Hrangkhol  Hrangkhol
hrc  Niwer Mil  Niwer Mil
hre  Hre  Hre
hrk  Haruku  Haruku
hrm  Horned Miao  Miao, Horned
hro  Haroi  Haroi
hrp  Nhirrpi  Nhirrpi
hrt  Hértevin  Hértevin
hru  Hruso  Hruso
hrv  Croatian  Croatian
hrw  Warwar Feni  Warwar Feni
hrx  Hunsrik  Hunsrik
hrz  Harzani  Harzani
hsb  Upper Sorbian  Sorbian, Upper
hsh  Hungarian Sign Language  Hungarian Sign Language
hsl  Hausa Sign Language  Hausa Sign Language
hsn  Xiang Chinese  Chinese, Xiang
hss  Harsusi  Harsusi
hti  Hoti  Hoti
hto  Minica Huitoto  Huitoto, Minica
hts  Hadza  Hadza
htu  Hitu  Hitu
htx  Middle Hittite  Hittite, Middle
hub  Huambisa  Huambisa
huc  =/Hua  =/Hua
hud  Huaulu  Huaulu
hue  San Francisco Del Mar Huave  Huave, San Francisco Del Mar
huf  Humene  Humene
hug  Huachipaeri  Huachipaeri
huh  Huilliche  Huilliche
hui  Huli  Huli
huj  Northern Guiyang Hmong  Hmong, Northern Guiyang
huj  Northern Guiyang Miao  Miao, Northern Guiyang
huk  Hulung  Hulung
hul  Hula  Hula
hum  Hungana  Hungana
hun  Hungarian  Hungarian
huo  Hu  Hu
hup  Hupa  Hupa
huq  Tsat  Tsat
hur  Halkomelem  Halkomelem
hus  Huastec  Huastec
hut  Humla  Humla
huu  Murui Huitoto  Huitoto, Murui
huv  San Mateo Del Mar Huave  Huave, San Mateo Del Mar
huw  Hukumina  Hukumina
hux  Nüpode Huitoto  Huitoto, Nüpode
huy  Hulaulá  Hulaulá
huz  Hunzib  Hunzib
hvc  Haitian Vodoun Culture Language  Haitian Vodoun Culture Language
hve  San Dionisio Del Mar Huave  Huave, San Dionisio Del Mar
hvk  Haveke  Haveke
hvn  Sabu  Sabu
hvv  Santa María Del Mar Huave  Huave, Santa María Del Mar
hwa  Wané  Wané
hwc  Hawai'i Creole English  Creole English, Hawai'i
hwc  Hawai'i Pidgin  Hawai'i Pidgin
hwo  Hwana  Hwana
hya  Hya  Hya
hye  Armenian  Armenian
iai  Iaai  Iaai
ian  Iatmul  Iatmul
iap  Iapama  Iapama
iar  Purari  Purari
iba  Iban  Iban
ibb  Ibibio  Ibibio
ibd  Iwaidja  Iwaidja
ibe  Akpes  Akpes
ibg  Ibanag  Ibanag
ibl  Ibaloi  Ibaloi
ibm  Agoi  Agoi
ibn  Ibino  Ibino
ibo  Igbo  Igbo
ibr  Ibuoro  Ibuoro
ibu  Ibu  Ibu
iby  Ibani  Ibani
ica  Ede Ica  Ede Ica
ich  Etkywan  Etkywan
icl  Icelandic Sign Language  Icelandic Sign Language
icr  Islander Creole English  Creole English, Islander
ida  Idakho-Isukha-Tiriki  Idakho-Isukha-Tiriki
ida  Luidakho-Luisukha-Lutirichi  Luidakho-Luisukha-Lutirichi
idb  Indo-Portuguese  Indo-Portuguese
idc  Ajiya  Ajiya
idc  Idon  Idon
idd  Ede Idaca  Ede Idaca
ide  Idere  Idere
idi  Idi  Idi
ido  Ido  Ido
idr  Indri  Indri
ids  Idesa  Idesa
idt  Idaté  Idaté
idu  Idoma  Idoma
ifa  Amganad Ifugao  Ifugao, Amganad
ifb  Ayangan Ifugao  Ifugao, Ayangan
ifb  Batad Ifugao  Ifugao, Batad
ife  Ifè  Ifè
iff  Ifo  Ifo
ifk  Tuwali Ifugao  Ifugao, Tuwali
ifm  Teke-Fuumu  Teke-Fuumu
ifu  Mayoyao Ifugao  Ifugao, Mayoyao
ify  Keley-I Kallahan  Kallahan, Keley-I
igb  Ebira  Ebira
ige  Igede  Igede
igg  Igana  Igana
igl  Igala  Igala
igm  Kanggape  Kanggape
ign  Ignaciano  Ignaciano
igo  Isebe  Isebe
igs  Interglossa  Interglossa
igw  Igwe  Igwe
ihb  Iha Based Pidgin  Iha Based Pidgin
ihi  Ihievbe  Ihievbe
ihp  Iha  Iha
ihw  Bidhawal  Bidhawal
iii  Nuosu  Nuosu
iii  Sichuan Yi  Yi, Sichuan
iin  Thiin  Thiin
ijc  Izon  Izon
ije  Biseni  Biseni
ijj  Ede Ije  Ede Ije
ijn  Kalabari  Kalabari
ijs  Southeast Ijo  Ijo, Southeast
ike  Eastern Canadian Inuktitut  Inuktitut, Eastern Canadian
iki  Iko  Iko
ikk  Ika  Ika
ikl  Ikulu  Ikulu
iko  Olulumo-Ikom  Olulumo-Ikom
ikp  Ikpeshi  Ikpeshi
ikr  Ikaranggal  Ikaranggal
ikt  Inuinnaqtun  Inuinnaqtun
ikt  Western Canadian Inuktitut  Inuktitut, Western Canadian
iku  Inuktitut  Inuktitut
ikv  Iku-Gora-Ankwa  Iku-Gora-Ankwa
ikw  Ikwere  Ikwere
ikx  Ik  Ik
ikz  Ikizu  Ikizu
ila  Ile Ape  Ile Ape
ilb  Ila  Ila
ile  Interlingue  Interlingue
ile  Occidental  Occidental
ilg  Garig-Ilgar  Garig-Ilgar
ili  Ili Turki  Ili Turki
ilk  Ilongot  Ilongot
ill  Iranun  Iranun
ilo  Iloko  Iloko
ils  International Sign  International Sign
ilu  Ili'uun  Ili'uun
ilv  Ilue  Ilue
ima  Mala Malasar  Malasar, Mala
ime  Imeraguen  Imeraguen
imi  Anamgura  Anamgura
iml  Miluk  Miluk
imn  Imonda  Imonda
imo  Imbongu  Imbongu
imr  Imroing  Imroing
ims  Marsian  Marsian
imy  Milyan  Milyan
ina  Interlingua (International Auxiliary Language Association)  Interlingua (International Auxiliary Language Association)
inb  Inga  Inga
ind  Indonesian  Indonesian
ing  Degexit'an  Degexit'an
inh  Ingush  Ingush
inj  Jungle Inga  Inga, Jungle
inl  Indonesian Sign Language  Indonesian Sign Language
inm  Minaean  Minaean
inn  Isinai  Isinai
ino  Inoke-Yate  Inoke-Yate
inp  Iñapari  Iñapari
ins  Indian Sign Language  Indian Sign Language
int  Intha  Intha
inz  Ineseño  Ineseño
ior  Inor  Inor
iou  Tuma-Irumu  Tuma-Irumu
iow  Iowa-Oto  Iowa-Oto
ipi  Ipili  Ipili
ipk  Inupiaq  Inupiaq
ipo  Ipiko  Ipiko
iqu  Iquito  Iquito
iqw  Ikwo  Ikwo
ire  Iresim  Iresim
irh  Irarutu  Irarutu
iri  Irigwe  Irigwe
irk  Iraqw  Iraqw
irn  Irántxe  Irántxe
irr  Ir  Ir
iru  Irula  Irula
irx  Kamberau  Kamberau
iry  Iraya  Iraya
isa  Isabi  Isabi
isc  Isconahua  Isconahua
isd  Isnag  Isnag
ise  Italian Sign Language  Italian Sign Language
isg  Irish Sign Language  Irish Sign Language
ish  Esan  Esan
isi  Nkem-Nkum  Nkem-Nkum
isk  Ishkashimi  Ishkashimi
isl  Icelandic  Icelandic
ism  Masimasi  Masimasi
isn  Isanzu  Isanzu
iso  Isoko  Isoko
isr  Israeli Sign Language  Israeli Sign Language
ist  Istriot  Istriot
isu  Isu (Menchum Division)  Isu (Menchum Division)
ita  Italian  Italian
itb  Binongan Itneg  Itneg, Binongan
ite  Itene  Itene
iti  Inlaod Itneg  Itneg, Inlaod
itk  Judeo-Italian  Judeo-Italian
itl  Itelmen  Itelmen
itm  Itu Mbon Uzo  Itu Mbon Uzo
ito  Itonama  Itonama
itr  Iteri  Iteri
its  Isekiri  Isekiri
itt  Maeng Itneg  Itneg, Maeng
itv  Itawit  Itawit
itw  Ito  Ito
itx  Itik  Itik
ity  Moyadan Itneg  Itneg, Moyadan
itz  Itzá  Itzá
ium  Iu Mien  Mien, Iu
ivb  Ibatan  Ibatan
ivv  Ivatan  Ivatan
iwk  I-Wak  I-Wak
iwm  Iwam  Iwam
iwo  Iwur  Iwur
iws  Sepik Iwam  Iwam, Sepik
ixc  Ixcatec  Ixcatec
ixl  Ixil  Ixil
iya  Iyayu  Iyayu
iyo  Mesaka  Mesaka
iyx  Yaka (Congo)  Yaka (Congo)
izh  Ingrian  Ingrian
izr  Izere  Izere
izz  Izii  Izii
jaa  Jamamadí  Jamamadí
jab  Hyam  Hyam
jac  Jakalteko  Jakalteko
jac  Popti'  Popti'
jad  Jahanka  Jahanka
jae  Yabem  Yabem
jaf  Jara  Jara
jah  Jah Hut  Jah Hut
jaj  Zazao  Zazao
jak  Jakun  Jakun
jal  Yalahatan  Yalahatan
jam  Jamaican Creole English  Creole English, Jamaican
jan  Jandai  Jandai
jao  Yanyuwa  Yanyuwa
jaq  Yaqay  Yaqay
jas  New Caledonian Javanese  Javanese, New Caledonian
jat  Jakati  Jakati
jau  Yaur  Yaur
jav  Javanese  Javanese
jax  Jambi Malay  Malay, Jambi
jay  Yan-nhangu  Yan-nhangu
jaz  Jawe  Jawe
jbe  Judeo-Berber  Judeo-Berber
jbi  Badjiri  Badjiri
jbj  Arandai  Arandai
jbk  Barikewa  Barikewa
jbn  Nafusi  Nafusi
jbo  Lojban  Lojban
jbr  Jofotek-Bromnya  Jofotek-Bromnya
jbt  Jabutí  Jabutí
jbu  Jukun Takum  Jukun Takum
jbw  Yawijibaya  Yawijibaya
jcs  Jamaican Country Sign Language  Jamaican Country Sign Language
jct  Krymchak  Krymchak
jda  Jad  Jad
jdg  Jadgali  Jadgali
jdt  Judeo-Tat  Judeo-Tat
jeb  Jebero  Jebero
jee  Jerung  Jerung
jeg  Jeng  Jeng
jeh  Jeh  Jeh
jei  Yei  Yei
jek  Jeri Kuo  Jeri Kuo
jel  Yelmek  Yelmek
jen  Dza  Dza
jer  Jere  Jere
jet  Manem  Manem
jeu  Jonkor Bourmataguil  Jonkor Bourmataguil
jgb  Ngbee  Ngbee
jge  Judeo-Georgian  Judeo-Georgian
jgk  Gwak  Gwak
jgo  Ngomba  Ngomba
jhi  Jehai  Jehai
jhs  Jhankot Sign Language  Jhankot Sign Language
jia  Jina  Jina
jib  Jibu  Jibu
jic  Tol  Tol
jid  Bu  Bu
jie  Jilbe  Jilbe
jig  Djingili  Djingili
jih  Shangzhai  Shangzhai
jih  sTodsde  sTodsde
jii  Jiiddu  Jiiddu
jil  Jilim  Jilim
jim  Jimi (Cameroon)  Jimi (Cameroon)
jio  Jiamao  Jiamao
jiq  Guanyinqiao  Guanyinqiao
jiq  Lavrung  Lavrung
jit  Jita  Jita
jiu  Youle Jinuo  Jinuo, Youle
jiv  Shuar  Shuar
jiy  Buyuan Jinuo  Jinuo, Buyuan
jjr  Bankal  Bankal
jkm  Mobwa Karen  Karen, Mobwa
jko  Kubo  Kubo
jkp  Paku Karen  Karen, Paku
jkr  Koro (India)  Koro (India)
jku  Labir  Labir
jle  Ngile  Ngile
jls  Jamaican Sign Language  Jamaican Sign Language
jma  Dima  Dima
jmb  Zumbun  Zumbun
jmc  Machame  Machame
jmd  Yamdena  Yamdena
jmi  Jimi (Nigeria)  Jimi (Nigeria)
jml  Jumli  Jumli
jmn  Makuri Naga  Naga, Makuri
jmr  Kamara  Kamara
jms  Mashi (Nigeria)  Mashi (Nigeria)
jmw  Mouwase  Mouwase
jmx  Western Juxtlahuaca Mixtec  Mixtec, Western Juxtlahuaca
jna  Jangshung  Jangshung
jnd  Jandavra  Jandavra
jng  Yangman  Yangman
jni  Janji  Janji
jnj  Yemsa  Yemsa
jnl  Rawat  Rawat
jns  Jaunsari  Jaunsari
job  Joba  Joba
jod  Wojenaka  Wojenaka
jor  Jorá  Jorá
jos  Jordanian Sign Language  Jordanian Sign Language
jow  Jowulu  Jowulu
jpa  Jewish Palestinian Aramaic  Aramaic, Jewish Palestinian
jpn  Japanese  Japanese
jpr  Judeo-Persian  Judeo-Persian
jqr  Jaqaru  Jaqaru
jra  Jarai  Jarai
jrb  Judeo-Arabic  Judeo-Arabic
jrr  Jiru  Jiru
jrt  Jorto  Jorto
jru  Japrería  Japrería
jsl  Japanese Sign Language  Japanese Sign Language
jua  Júma  Júma
jub  Wannu  Wannu
juc  Jurchen  Jurchen
jud  Worodougou  Worodougou
juh  Hõne  Hõne
jui  Ngadjuri  Ngadjuri
juk  Wapan  Wapan
jul  Jirel  Jirel
jum  Jumjum  Jumjum
jun  Juang  Juang
juo  Jiba  Jiba
jup  Hupdë  Hupdë
jur  Jurúna  Jurúna
jus  Jumla Sign Language  Jumla Sign Language
jut  Jutish  Jutish
juu  Ju  Ju
juw  Wãpha  Wãpha
juy  Juray  Juray
jvd  Javindo  Javindo
jvn  Caribbean Javanese  Javanese, Caribbean
jwi  Jwira-Pepesa  Jwira-Pepesa
jya  Jiarong  Jiarong
jye  Judeo-Yemeni Arabic  Arabic, Judeo-Yemeni
jyy  Jaya  Jaya
kaa  Kara-Kalpak  Kara-Kalpak
kab  Kabyle  Kabyle
kac  Jingpho  Jingpho
kac  Kachin  Kachin
kad  Adara  Adara
kae  Ketangalan  Ketangalan
kaf  Katso  Katso
kag  Kajaman  Kajaman
kah  Kara (Central African Republic)  Kara (Central African Republic)
kai  Karekare  Karekare
kaj  Jju  Jju
kak  Kayapa Kallahan  Kallahan, Kayapa
kal  Greenlandic  Greenlandic
kal  Kalaallisut  Kalaallisut
kam  Kamba (Kenya)  Kamba (Kenya)
kan  Kannada  Kannada
kao  Xaasongaxango  Xaasongaxango
kap  Bezhta  Bezhta
kaq  Capanahua  Capanahua
kas  Kashmiri  Kashmiri
kat  Georgian  Georgian
kau  Kanuri  Kanuri
kav  Katukína  Katukína
kaw  Kawi  Kawi
kax  Kao  Kao
kay  Kamayurá  Kamayurá
kaz  Kazakh  Kazakh
kba  Kalarko  Kalarko
kbb  Kaxuiâna  Kaxuiâna
kbc  Kadiwéu  Kadiwéu
kbd  Kabardian  Kabardian
kbe  Kanju  Kanju
kbf  Kakauhua  Kakauhua
kbg  Khamba  Khamba
kbh  Camsá  Camsá
kbi  Kaptiau  Kaptiau
kbj  Kari  Kari
kbk  Grass Koiari  Koiari, Grass
kbl  Kanembu  Kanembu
kbm  Iwal  Iwal
kbn  Kare (Central African Republic)  Kare (Central African Republic)
kbo  Keliko  Keliko
kbp  Kabiyè  Kabiyè
kbq  Kamano  Kamano
kbr  Kafa  Kafa
kbs  Kande  Kande
kbt  Abadi  Abadi
kbu  Kabutra  Kabutra
kbv  Dera (Indonesia)  Dera (Indonesia)
kbw  Kaiep  Kaiep
kbx  Ap Ma  Ap Ma
kby  Manga Kanuri  Kanuri, Manga
kbz  Duhwa  Duhwa
kca  Khanty  Khanty
kcb  Kawacha  Kawacha
kcc  Lubila  Lubila
kcd  Ngkâlmpw Kanum  Kanum, Ngkâlmpw
kce  Kaivi  Kaivi
kcf  Ukaan  Ukaan
kcg  Tyap  Tyap
kch  Vono  Vono
kci  Kamantan  Kamantan
kcj  Kobiana  Kobiana
kck  Kalanga  Kalanga
kcl  Kala  Kala
kcl  Kela (Papua New Guinea)  Kela (Papua New Guinea)
kcm  Gula (Central African Republic)  Gula (Central African Republic)
kcn  Nubi  Nubi
kco  Kinalakna  Kinalakna
kcp  Kanga  Kanga
kcq  Kamo  Kamo
kcr  Katla  Katla
kcs  Koenoem  Koenoem
kct  Kaian  Kaian
kcu  Kami (Tanzania)  Kami (Tanzania)
kcv  Kete  Kete
kcw  Kabwari  Kabwari
kcx  Kachama-Ganjule  Kachama-Ganjule
kcy  Korandje  Korandje
kcz  Konongo  Konongo
kda  Worimi  Worimi
kdc  Kutu  Kutu
kdd  Yankunytjatjara  Yankunytjatjara
kde  Makonde  Makonde
kdf  Mamusi  Mamusi
kdg  Seba  Seba
kdh  Tem  Tem
kdi  Kumam  Kumam
kdj  Karamojong  Karamojong
kdk  Kwényi  Kwényi
kdk  Numèè  Numèè
kdl  Tsikimba  Tsikimba
kdm  Kagoma  Kagoma
kdn  Kunda  Kunda
kdp  Kaningdon-Nindem  Kaningdon-Nindem
kdq  Koch  Koch
kdr  Karaim  Karaim
kdt  Kuy  Kuy
kdu  Kadaru  Kadaru
kdw  Koneraw  Koneraw
kdx  Kam  Kam
kdy  Keder  Keder
kdy  Keijar  Keijar
kdz  Kwaja  Kwaja
kea  Kabuverdianu  Kabuverdianu
keb  Kélé  Kélé
kec  Keiga  Keiga
ked  Kerewe  Kerewe
kee  Eastern Keres  Keres, Eastern
kef  Kpessi  Kpessi
keg  Tese  Tese
keh  Keak  Keak
kei  Kei  Kei
kej  Kadar  Kadar
kek  Kekchí  Kekchí
kel  Kela (Democratic Republic of Congo)  Kela (Democratic Republic of Congo)
kem  Kemak  Kemak
ken  Kenyang  Kenyang
keo  Kakwa  Kakwa
kep  Kaikadi  Kaikadi
keq  Kamar  Kamar
ker  Kera  Kera
kes  Kugbo  Kugbo
ket  Ket  Ket
keu  Akebu  Akebu
kev  Kanikkaran  Kanikkaran
kew  West Kewa  Kewa, West
kex  Kukna  Kukna
key  Kupia  Kupia
kez  Kukele  Kukele
kfa  Kodava  Kodava
kfb  Northwestern Kolami  Kolami, Northwestern
kfc  Konda-Dora  Konda-Dora
kfd  Korra Koraga  Koraga, Korra
kfe  Kota (India)  Kota (India)
kff  Koya  Koya
kfg  Kudiya  Kudiya
kfh  Kurichiya  Kurichiya
kfi  Kannada Kurumba  Kurumba, Kannada
kfj  Kemiehua  Kemiehua
kfk  Kinnauri  Kinnauri
kfl  Kung  Kung
kfm  Khunsari  Khunsari
kfn  Kuk  Kuk
kfo  Koro (Côte d'Ivoire)  Koro (Côte d'Ivoire)
kfp  Korwa  Korwa
kfq  Korku  Korku
kfr  Kachchi  Kachchi
kfs  Bilaspuri  Bilaspuri
kft  Kanjari  Kanjari
kfu  Katkari  Katkari
kfv  Kurmukar  Kurmukar
kfw  Kharam Naga  Naga, Kharam
kfx  Kullu Pahari  Pahari, Kullu
kfy  Kumaoni  Kumaoni
kfz  Koromfé  Koromfé
kga  Koyaga  Koyaga
kgb  Kawe  Kawe
kgc  Kasseng  Kasseng
kgd  Kataang  Kataang
kge  Komering  Komering
kgf  Kube  Kube
kgg  Kusunda  Kusunda
kgi  Selangor Sign Language  Selangor Sign Language
kgj  Gamale Kham  Kham, Gamale
kgk  Kaiwá  Kaiwá
kgl  Kunggari  Kunggari
kgm  Karipúna  Karipúna
kgn  Karingani  Karingani
kgo  Krongo  Krongo
kgp  Kaingang  Kaingang
kgq  Kamoro  Kamoro
kgr  Abun  Abun
kgs  Kumbainggar  Kumbainggar
kgt  Somyev  Somyev
kgu  Kobol  Kobol
kgv  Karas  Karas
kgw  Karon Dori  Karon Dori
kgx  Kamaru  Kamaru
kgy  Kyerung  Kyerung
kha  Khasi  Khasi
khb  Lü  Lü
khc  Tukang Besi North  Tukang Besi North
khd  Bädi Kanum  Kanum, Bädi
khe  Korowai  Korowai
khf  Khuen  Khuen
khg  Khams Tibetan  Tibetan, Khams
khh  Kehu  Kehu
khj  Kuturmi  Kuturmi
khk  Halh Mongolian  Mongolian, Halh
khl  Lusi  Lusi
khm  Central Khmer  Khmer, Central
khn  Khandesi  Khandesi
kho  Khotanese  Khotanese
kho  Sakan  Sakan
khp  Kapauri  Kapauri
khp  Kapori  Kapori
khq  Koyra Chiini Songhay  Songhay, Koyra Chiini
khr  Kharia  Kharia
khs  Kasua  Kasua
kht  Khamti  Khamti
khu  Nkhumbi  Nkhumbi
khv  Khvarshi  Khvarshi
khw  Khowar  Khowar
khx  Kanu  Kanu
khy  Kele (Democratic Republic of Congo)  Kele (Democratic Republic of Congo)
khz  Keapara  Keapara
kia  Kim  Kim
kib  Koalib  Koalib
kic  Kickapoo  Kickapoo
kid  Koshin  Koshin
kie  Kibet  Kibet
kif  Eastern Parbate Kham  Kham, Eastern Parbate
kig  Kimaama  Kimaama
kig  Kimaghima  Kimaghima
kih  Kilmeri  Kilmeri
kii  Kitsai  Kitsai
kij  Kilivila  Kilivila
kik  Gikuyu  Gikuyu
kik  Kikuyu  Kikuyu
kil  Kariya  Kariya
kim  Karagas  Karagas
kin  Kinyarwanda  Kinyarwanda
kio  Kiowa  Kiowa
kip  Sheshi Kham  Kham, Sheshi
kiq  Kosadle  Kosadle
kiq  Kosare  Kosare
kir  Kirghiz  Kirghiz
kir  Kyrgyz  Kyrgyz
kis  Kis  Kis
kit  Agob  Agob
kiu  Kirmanjki (individual language)  Kirmanjki (individual language)
kiv  Kimbu  Kimbu
kiw  Northeast Kiwai  Kiwai, Northeast
kix  Khiamniungan Naga  Naga, Khiamniungan
kiy  Kirikiri  Kirikiri
kiz  Kisi  Kisi
kja  Mlap  Mlap
kjb  Kanjobal  Kanjobal
kjb  Q'anjob'al  Q'anjob'al
kjc  Coastal Konjo  Konjo, Coastal
kjd  Southern Kiwai  Kiwai, Southern
kje  Kisar  Kisar
kjf  Khalaj  Khalaj
kjg  Khmu  Khmu
kjh  Khakas  Khakas
kji  Zabana  Zabana
kjj  Khinalugh  Khinalugh
kjk  Highland Konjo  Konjo, Highland
kjl  Western Parbate Kham  Kham, Western Parbate
kjm  Kháng  Kháng
kjn  Kunjen  Kunjen
kjo  Harijan Kinnauri  Kinnauri, Harijan
kjp  Pwo Eastern Karen  Karen, Pwo Eastern
kjq  Western Keres  Keres, Western
kjr  Kurudu  Kurudu
kjs  East Kewa  Kewa, East
kjt  Phrae Pwo Karen  Karen, Phrae Pwo
kju  Kashaya  Kashaya
kjx  Ramopa  Ramopa
kjy  Erave  Erave
kjz  Bumthangkha  Bumthangkha
kka  Kakanda  Kakanda
kkb  Kwerisa  Kwerisa
kkc  Odoodee  Odoodee
kkd  Kinuku  Kinuku
kke  Kakabe  Kakabe
kkf  Kalaktang Monpa  Monpa, Kalaktang
kkg  Mabaka Valley Kalinga  Kalinga, Mabaka Valley
kkh  Khün  Khün
kki  Kagulu  Kagulu
kkj  Kako  Kako
kkk  Kokota  Kokota
kkl  Kosarek Yale  Yale, Kosarek
kkm  Kiong  Kiong
kkn  Kon Keu  Kon Keu
kko  Karko  Karko
kkp  Gugubera  Gugubera
kkq  Kaiku  Kaiku
kkr  Kir-Balar  Kir-Balar
kks  Giiwo  Giiwo
kkt  Koi  Koi
kku  Tumi  Tumi
kkv  Kangean  Kangean
kkw  Teke-Kukuya  Teke-Kukuya
kkx  Kohin  Kohin
kky  Guguyimidjir  Guguyimidjir
kkz  Kaska  Kaska
kla  Klamath-Modoc  Klamath-Modoc
klb  Kiliwa  Kiliwa
klc  Kolbila  Kolbila
kld  Gamilaraay  Gamilaraay
kle  Kulung (Nepal)  Kulung (Nepal)
klf  Kendeje  Kendeje
klg  Tagakaulo  Tagakaulo
klh  Weliki  Weliki
kli  Kalumpang  Kalumpang
klj  Turkic Khalaj  Khalaj, Turkic
klk  Kono (Nigeria)  Kono (Nigeria)
kll  Kagan Kalagan  Kalagan, Kagan
klm  Migum  Migum
kln  Kalenjin  Kalenjin
klo  Kapya  Kapya
klp  Kamasa  Kamasa
klq  Rumu  Rumu
klr  Khaling  Khaling
kls  Kalasha  Kalasha
klt  Nukna  Nukna
klu  Klao  Klao
klv  Maskelynes  Maskelynes
klw  Lindu  Lindu
klx  Koluwawa  Koluwawa
kly  Kalao  Kalao
klz  Kabola  Kabola
kma  Konni  Konni
kmb  Kimbundu  Kimbundu
kmc  Southern Dong  Dong, Southern
kmd  Majukayang Kalinga  Kalinga, Majukayang
kme  Bakole  Bakole
kmf  Kare (Papua New Guinea)  Kare (Papua New Guinea)
kmg  Kâte  Kâte
kmh  Kalam  Kalam
kmi  Kami (Nigeria)  Kami (Nigeria)
kmj  Kumarbhag Paharia  Kumarbhag Paharia
kmk  Limos Kalinga  Kalinga, Limos
kml  Tanudan Kalinga  Kalinga, Tanudan
kmm  Kom (India)  Kom (India)
kmn  Awtuw  Awtuw
kmo  Kwoma  Kwoma
kmp  Gimme  Gimme
kmq  Kwama  Kwama
kmr  Northern Kurdish  Kurdish, Northern
kms  Kamasau  Kamasau
kmt  Kemtuik  Kemtuik
kmu  Kanite  Kanite
kmv  Karipúna Creole French  Creole French, Karipúna
kmw  Komo (Democratic Republic of Congo)  Komo (Democratic Republic of Congo)
kmx  Waboda  Waboda
kmy  Koma  Koma
kmz  Khorasani Turkish  Khorasani Turkish
kna  Dera (Nigeria)  Dera (Nigeria)
knb  Lubuagan Kalinga  Kalinga, Lubuagan
knc  Central Kanuri  Kanuri, Central
knd  Konda  Konda
kne  Kankanaey  Kankanaey
knf  Mankanya  Mankanya
kng  Koongo  Koongo
kni  Kanufi  Kanufi
knj  Western Kanjobal  Kanjobal, Western
knk  Kuranko  Kuranko
knl  Keninjal  Keninjal
knm  Kanamarí  Kanamarí
knn  Konkani (individual language)  Konkani (individual language)
kno  Kono (Sierra Leone)  Kono (Sierra Leone)
knp  Kwanja  Kwanja
knq  Kintaq  Kintaq
knr  Kaningra  Kaningra
kns  Kensiu  Kensiu
knt  Panoan Katukína  Katukína, Panoan
knu  Kono (Guinea)  Kono (Guinea)
knv  Tabo  Tabo
knw  Kung-Ekoka  Kung-Ekoka
knx  Kendayan  Kendayan
knx  Salako  Salako
kny  Kanyok  Kanyok
knz  Kalamsé  Kalamsé
koa  Konomala  Konomala
koc  Kpati  Kpati
kod  Kodi  Kodi
koe  Kacipo-Balesi  Kacipo-Balesi
kof  Kubi  Kubi
kog  Cogui  Cogui
kog  Kogi  Kogi
koh  Koyo  Koyo
koi  Komi-Permyak  Komi-Permyak
koj  Sara Dunjo  Sara Dunjo
kok  Konkani (macrolanguage)  Konkani (macrolanguage)
kol  Kol (Papua New Guinea)  Kol (Papua New Guinea)
kom  Komi  Komi
kon  Kongo  Kongo
koo  Konzo  Konzo
kop  Waube  Waube
koq  Kota (Gabon)  Kota (Gabon)
kor  Korean  Korean
kos  Kosraean  Kosraean
kot  Lagwan  Lagwan
kou  Koke  Koke
kov  Kudu-Camo  Kudu-Camo
kow  Kugama  Kugama
kox  Coxima  Coxima
koy  Koyukon  Koyukon
koz  Korak  Korak
kpa  Kutto  Kutto
kpb  Mullu Kurumba  Kurumba, Mullu
kpc  Curripaco  Curripaco
kpd  Koba  Koba
kpe  Kpelle  Kpelle
kpf  Komba  Komba
kpg  Kapingamarangi  Kapingamarangi
kph  Kplang  Kplang
kpi  Kofei  Kofei
kpj  Karajá  Karajá
kpk  Kpan  Kpan
kpl  Kpala  Kpala
kpm  Koho  Koho
kpn  Kepkiriwát  Kepkiriwát
kpo  Ikposo  Ikposo
kpq  Korupun-Sela  Korupun-Sela
kpr  Korafe-Yegha  Korafe-Yegha
kps  Tehit  Tehit
kpt  Karata  Karata
kpu  Kafoa  Kafoa
kpv  Komi-Zyrian  Komi-Zyrian
kpw  Kobon  Kobon
kpx  Mountain Koiali  Koiali, Mountain
kpy  Koryak  Koryak
kpz  Kupsabiny  Kupsabiny
kqa  Mum  Mum
kqb  Kovai  Kovai
kqc  Doromu-Koki  Doromu-Koki
kqd  Koy Sanjaq Surat  Koy Sanjaq Surat
kqe  Kalagan  Kalagan
kqf  Kakabai  Kakabai
kqg  Khe  Khe
kqh  Kisankasa  Kisankasa
kqi  Koitabu  Koitabu
kqj  Koromira  Koromira
kqk  Kotafon Gbe  Gbe, Kotafon
kql  Kyenele  Kyenele
kqm  Khisa  Khisa
kqn  Kaonde  Kaonde
kqo  Eastern Krahn  Krahn, Eastern
kqp  Kimré  Kimré
kqq  Krenak  Krenak
kqr  Kimaragang  Kimaragang
kqs  Northern Kissi  Kissi, Northern
kqt  Klias River Kadazan  Kadazan, Klias River
kqu  Seroa  Seroa
kqv  Okolod  Okolod
kqw  Kandas  Kandas
kqx  Mser  Mser
kqy  Koorete  Koorete
kqz  Korana  Korana
kra  Kumhali  Kumhali
krb  Karkin  Karkin
krc  Karachay-Balkar  Karachay-Balkar
krd  Kairui-Midiki  Kairui-Midiki
kre  Panará  Panará
krf  Koro (Vanuatu)  Koro (Vanuatu)
krh  Kurama  Kurama
kri  Krio  Krio
krj  Kinaray-A  Kinaray-A
krk  Kerek  Kerek
krl  Karelian  Karelian
krm  Krim  Krim
krn  Sapo  Sapo
krp  Korop  Korop
krr  Kru'ng 2  Kru'ng 2
krs  Gbaya (Sudan)  Gbaya (Sudan)
krt  Tumari Kanuri  Kanuri, Tumari
kru  Kurukh  Kurukh
krv  Kavet  Kavet
krw  Western Krahn  Krahn, Western
krx  Karon  Karon
kry  Kryts  Kryts
krz  Sota Kanum  Kanum, Sota
ksa  Shuwa-Zamani  Shuwa-Zamani
ksb  Shambala  Shambala
ksc  Southern Kalinga  Kalinga, Southern
ksd  Kuanua  Kuanua
kse  Kuni  Kuni
ksf  Bafia  Bafia
ksg  Kusaghe  Kusaghe
ksh  Kölsch  Kölsch
ksi  I'saka  I'saka
ksi  Krisa  Krisa
ksj  Uare  Uare
ksk  Kansa  Kansa
ksl  Kumalu  Kumalu
ksm  Kumba  Kumba
ksn  Kasiguranin  Kasiguranin
kso  Kofa  Kofa
ksp  Kaba  Kaba
ksq  Kwaami  Kwaami
ksr  Borong  Borong
kss  Southern Kisi  Kisi, Southern
kst  Winyé  Winyé
ksu  Khamyang  Khamyang
ksv  Kusu  Kusu
ksw  S'gaw Karen  Karen, S'gaw
ksx  Kedang  Kedang
ksy  Kharia Thar  Kharia Thar
ksz  Kodaku  Kodaku
kta  Katua  Katua
ktb  Kambaata  Kambaata
ktc  Kholok  Kholok
ktd  Kokata  Kokata
kte  Nubri  Nubri
ktf  Kwami  Kwami
ktg  Kalkutung  Kalkutung
kth  Karanga  Karanga
kti  North Muyu  Muyu, North
ktj  Plapo Krumen  Krumen, Plapo
ktk  Kaniet  Kaniet
ktl  Koroshi  Koroshi
ktm  Kurti  Kurti
ktn  Karitiâna  Karitiâna
kto  Kuot  Kuot
ktp  Kaduo  Kaduo
ktq  Katabaga  Katabaga
ktr  Kota Marudu Tinagas  Kota Marudu Tinagas
kts  South Muyu  Muyu, South
ktt  Ketum  Ketum
ktu  Kituba (Democratic Republic of Congo)  Kituba (Democratic Republic of Congo)
ktv  Eastern Katu  Katu, Eastern
ktw  Kato  Kato
ktx  Kaxararí  Kaxararí
kty  Kango (Bas-Uélé District)  Kango (Bas-Uélé District)
ktz  Ju/'hoan  Ju/'hoan
kua  Kuanyama  Kuanyama
kua  Kwanyama  Kwanyama
kub  Kutep  Kutep
kuc  Kwinsu  Kwinsu
kud  'Auhelawa  'Auhelawa
kue  Kuman  Kuman
kuf  Western Katu  Katu, Western
kug  Kupa  Kupa
kuh  Kushi  Kushi
kui  Kuikúro-Kalapálo  Kuikúro-Kalapálo
kuj  Kuria  Kuria
kuk  Kepo'  Kepo'
kul  Kulere  Kulere
kum  Kumyk  Kumyk
kun  Kunama  Kunama
kuo  Kumukio  Kumukio
kup  Kunimaipa  Kunimaipa
kuq  Karipuna  Karipuna
kur  Kurdish  Kurdish
kus  Kusaal  Kusaal
kut  Kutenai  Kutenai
kuu  Upper Kuskokwim  Kuskokwim, Upper
kuv  Kur  Kur
kuw  Kpagua  Kpagua
kux  Kukatja  Kukatja
kuy  Kuuku-Ya'u  Kuuku-Ya'u
kuz  Kunza  Kunza
kva  Bagvalal  Bagvalal
kvb  Kubu  Kubu
kvc  Kove  Kove
kvd  Kui (Indonesia)  Kui (Indonesia)
kve  Kalabakan  Kalabakan
kvf  Kabalai  Kabalai
kvg  Kuni-Boazi  Kuni-Boazi
kvh  Komodo  Komodo
kvi  Kwang  Kwang
kvj  Psikye  Psikye
kvk  Korean Sign Language  Korean Sign Language
kvl  Kayaw  Kayaw
kvm  Kendem  Kendem
kvn  Border Kuna  Kuna, Border
kvo  Dobel  Dobel
kvp  Kompane  Kompane
kvq  Geba Karen  Karen, Geba
kvr  Kerinci  Kerinci
kvs  Kunggara  Kunggara
kvt  Lahta  Lahta
kvt  Lahta Karen  Karen, Lahta
kvu  Yinbaw Karen  Karen, Yinbaw
kvv  Kola  Kola
kvw  Wersing  Wersing
kvx  Parkari Koli  Koli, Parkari
kvy  Yintale  Yintale
kvy  Yintale Karen  Karen, Yintale
kvz  Tsakwambo  Tsakwambo
kvz  Tsaukambo  Tsaukambo
kwa  Dâw  Dâw
kwb  Kwa  Kwa
kwc  Likwala  Likwala
kwd  Kwaio  Kwaio
kwe  Kwerba  Kwerba
kwf  Kwara'ae  Kwara'ae
kwg  Sara Kaba Deme  Sara Kaba Deme
kwh  Kowiai  Kowiai
kwi  Awa-Cuaiquer  Awa-Cuaiquer
kwj  Kwanga  Kwanga
kwk  Kwakiutl  Kwakiutl
kwl  Kofyar  Kofyar
kwm  Kwambi  Kwambi
kwn  Kwangali  Kwangali
kwo  Kwomtari  Kwomtari
kwp  Kodia  Kodia
kwq  Kwak  Kwak
kwr  Kwer  Kwer
kws  Kwese  Kwese
kwt  Kwesten  Kwesten
kwu  Kwakum  Kwakum
kwv  Sara Kaba Náà  Sara Kaba Náà
kww  Kwinti  Kwinti
kwx  Khirwar  Khirwar
kwy  San Salvador Kongo  Kongo, San Salvador
kwz  Kwadi  Kwadi
kxa  Kairiru  Kairiru
kxb  Krobu  Krobu
kxc  Khonso  Khonso
kxc  Konso  Konso
kxd  Brunei  Brunei
kxe  Kakihum  Kakihum
kxf  Manumanaw  Manumanaw
kxf  Manumanaw Karen  Karen, Manumanaw
kxh  Karo (Ethiopia)  Karo (Ethiopia)
kxi  Keningau Murut  Murut, Keningau
kxj  Kulfa  Kulfa
kxk  Zayein Karen  Karen, Zayein
kxl  Nepali Kurux  Kurux, Nepali
kxm  Northern Khmer  Khmer, Northern
kxn  Kanowit-Tanjong Melanau  Melanau, Kanowit-Tanjong
kxo  Kanoé  Kanoé
kxp  Wadiyara Koli  Koli, Wadiyara
kxq  Smärky Kanum  Kanum, Smärky
kxr  Koro (Papua New Guinea)  Koro (Papua New Guinea)
kxs  Kangjia  Kangjia
kxt  Koiwat  Koiwat
kxu  Kui (India)  Kui (India)
kxv  Kuvi  Kuvi
kxw  Konai  Konai
kxx  Likuba  Likuba
kxy  Kayong  Kayong
kxz  Kerewo  Kerewo
kya  Kwaya  Kwaya
kyb  Butbut Kalinga  Kalinga, Butbut
kyc  Kyaka  Kyaka
kyd  Karey  Karey
kye  Krache  Krache
kyf  Kouya  Kouya
kyg  Keyagana  Keyagana
kyh  Karok  Karok
kyi  Kiput  Kiput
kyj  Karao  Karao
kyk  Kamayo  Kamayo
kyl  Kalapuya  Kalapuya
kym  Kpatili  Kpatili
kyn  Northern Binukidnon  Binukidnon, Northern
kyo  Kelon  Kelon
kyp  Kang  Kang
kyq  Kenga  Kenga
kyr  Kuruáya  Kuruáya
kys  Baram Kayan  Kayan, Baram
kyt  Kayagar  Kayagar
kyu  Western Kayah  Kayah, Western
kyv  Kayort  Kayort
kyw  Kudmali  Kudmali
kyx  Rapoisi  Rapoisi
kyy  Kambaira  Kambaira
kyz  Kayabí  Kayabí
kza  Western Karaboro  Karaboro, Western
kzb  Kaibobo  Kaibobo
kzc  Bondoukou Kulango  Kulango, Bondoukou
kzd  Kadai  Kadai
kze  Kosena  Kosena
kzf  Da'a Kaili  Kaili, Da'a
kzg  Kikai  Kikai
kzi  Kelabit  Kelabit
kzj  Coastal Kadazan  Kadazan, Coastal
kzk  Kazukuru  Kazukuru
kzl  Kayeli  Kayeli
kzm  Kais  Kais
kzn  Kokola  Kokola
kzo  Kaningi  Kaningi
kzp  Kaidipang  Kaidipang
kzq  Kaike  Kaike
kzr  Karang  Karang
kzs  Sugut Dusun  Dusun, Sugut
kzt  Tambunan Dusun  Dusun, Tambunan
kzu  Kayupulau  Kayupulau
kzv  Komyandaret  Komyandaret
kzw  Karirí-Xocó  Karirí-Xocó
kzx  Kamarian  Kamarian
kzy  Kango (Tshopo District)  Kango (Tshopo District)
kzz  Kalabra  Kalabra
laa  Southern Subanen  Subanen, Southern
lab  Linear A  Linear A
lac  Lacandon  Lacandon
lad  Ladino  Ladino
lae  Pattani  Pattani
laf  Lafofa  Lafofa
lag  Langi  Langi
lah  Lahnda  Lahnda
lai  Lambya  Lambya
laj  Lango (Uganda)  Lango (Uganda)
lak  Laka (Nigeria)  Laka (Nigeria)
lal  Lalia  Lalia
lam  Lamba  Lamba
lan  Laru  Laru
lao  Lao  Lao
lap  Laka (Chad)  Laka (Chad)
laq  Qabiao  Qabiao
lar  Larteh  Larteh
las  Lama (Togo)  Lama (Togo)
lat  Latin  Latin
lau  Laba  Laba
lav  Latvian  Latvian
law  Lauje  Lauje
lax  Tiwa  Tiwa
lay  Lama (Myanmar)  Lama (Myanmar)
laz  Aribwatsa  Aribwatsa
lba  Lui  Lui
lbb  Label  Label
lbc  Lakkia  Lakkia
lbe  Lak  Lak
lbf  Tinani  Tinani
lbg  Laopang  Laopang
lbi  La'bi  La'bi
lbj  Ladakhi  Ladakhi
lbk  Central Bontok  Bontok, Central
lbl  Libon Bikol  Bikol, Libon
lbm  Lodhi  Lodhi
lbn  Lamet  Lamet
lbo  Laven  Laven
lbq  Wampar  Wampar
lbr  Lohorung  Lohorung
lbs  Libyan Sign Language  Libyan Sign Language
lbt  Lachi  Lachi
lbu  Labu  Labu
lbv  Lavatbura-Lamusong  Lavatbura-Lamusong
lbw  Tolaki  Tolaki
lbx  Lawangan  Lawangan
lby  Lamu-Lamu  Lamu-Lamu
lbz  Lardil  Lardil
lcc  Legenyem  Legenyem
lcd  Lola  Lola
lce  Loncong  Loncong
lcf  Lubu  Lubu
lch  Luchazi  Luchazi
lcl  Lisela  Lisela
lcm  Tungag  Tungag
lcp  Western Lawa  Lawa, Western
lcq  Luhu  Luhu
lcs  Lisabata-Nuniali  Lisabata-Nuniali
lda  Kla-Dan  Kla-Dan
ldb  Dũya  Dũya
ldd  Luri  Luri
ldg  Lenyima  Lenyima
ldh  Lamja-Dengsa-Tola  Lamja-Dengsa-Tola
ldi  Laari  Laari
ldj  Lemoro  Lemoro
ldk  Leelau  Leelau
ldl  Kaan  Kaan
ldm  Landoma  Landoma
ldn  Láadan  Láadan
ldo  Loo  Loo
ldp  Tso  Tso
ldq  Lufu  Lufu
lea  Lega-Shabunda  Lega-Shabunda
leb  Lala-Bisa  Lala-Bisa
lec  Leco  Leco
led  Lendu  Lendu
lee  Lyélé  Lyélé
lef  Lelemi  Lelemi
leg  Lengua  Lengua
leh  Lenje  Lenje
lei  Lemio  Lemio
lej  Lengola  Lengola
lek  Leipon  Leipon
lel  Lele (Democratic Republic of Congo)  Lele (Democratic Republic of Congo)
lem  Nomaande  Nomaande
len  Lenca  Lenca
leo  Leti (Cameroon)  Leti (Cameroon)
lep  Lepcha  Lepcha
leq  Lembena  Lembena
ler  Lenkau  Lenkau
les  Lese  Lese
let  Amio-Gelimi  Amio-Gelimi
let  Lesing-Gelimi  Lesing-Gelimi
leu  Kara (Papua New Guinea)  Kara (Papua New Guinea)
lev  Lamma  Lamma
lew  Ledo Kaili  Kaili, Ledo
lex  Luang  Luang
ley  Lemolang  Lemolang
lez  Lezghian  Lezghian
lfa  Lefa  Lefa
lfn  Lingua Franca Nova  Lingua Franca Nova
lga  Lungga  Lungga
lgb  Laghu  Laghu
lgg  Lugbara  Lugbara
lgh  Laghuu  Laghuu
lgi  Lengilu  Lengilu
lgk  Lingarak  Lingarak
lgk  Neverver  Neverver
lgl  Wala  Wala
lgm  Lega-Mwenga  Lega-Mwenga
lgn  Opuuo  Opuuo
lgq  Logba  Logba
lgr  Lengo  Lengo
lgt  Pahi  Pahi
lgu  Longgu  Longgu
lgz  Ligenza  Ligenza
lha  Laha (Viet Nam)  Laha (Viet Nam)
lhh  Laha (Indonesia)  Laha (Indonesia)
lhi  Lahu Shi  Lahu Shi
lhl  Lahul Lohar  Lohar, Lahul
lhm  Lhomi  Lhomi
lhn  Lahanan  Lahanan
lhp  Lhokpu  Lhokpu
lhs  Mlahsö  Mlahsö
lht  Lo-Toga  Lo-Toga
lhu  Lahu  Lahu
lia  West-Central Limba  Limba, West-Central
lib  Likum  Likum
lic  Hlai  Hlai
lid  Nyindrou  Nyindrou
lie  Likila  Likila
lif  Limbu  Limbu
lig  Ligbi  Ligbi
lih  Lihir  Lihir
lii  Lingkhim  Lingkhim
lij  Ligurian  Ligurian
lik  Lika  Lika
lil  Lillooet  Lillooet
lim  Limburgan  Limburgan
lim  Limburger  Limburger
lim  Limburgish  Limburgish
lin  Lingala  Lingala
lio  Liki  Liki
lip  Sekpele  Sekpele
liq  Libido  Libido
lir  Liberian English  English, Liberian
lis  Lisu  Lisu
lit  Lithuanian  Lithuanian
liu  Logorik  Logorik
liv  Liv  Liv
liw  Col  Col
lix  Liabuku  Liabuku
liy  Banda-Bambari  Banda-Bambari
liz  Libinza  Libinza
lja  Golpa  Golpa
lje  Rampi  Rampi
lji  Laiyolo  Laiyolo
ljl  Li'o  Li'o
ljp  Lampung Api  Lampung Api
ljw  Yirandali  Yirandali
ljx  Yuru  Yuru
lka  Lakalei  Lakalei
lkb  Kabras  Kabras
lkb  Lukabaras  Lukabaras
lkc  Kucong  Kucong
lkd  Lakondê  Lakondê
lke  Kenyi  Kenyi
lkh  Lakha  Lakha
lki  Laki  Laki
lkj  Remun  Remun
lkl  Laeko-Libuat  Laeko-Libuat
lkm  Kalaamaya  Kalaamaya
lkn  Lakon  Lakon
lkn  Vure  Vure
lko  Khayo  Khayo
lko  Olukhayo  Olukhayo
lkr  Päri  Päri
lks  Kisa  Kisa
lks  Olushisa  Olushisa
lkt  Lakota  Lakota
lku  Kungkari  Kungkari
lky  Lokoya  Lokoya
lla  Lala-Roba  Lala-Roba
llb  Lolo  Lolo
llc  Lele (Guinea)  Lele (Guinea)
lld  Ladin  Ladin
lle  Lele (Papua New Guinea)  Lele (Papua New Guinea)
llf  Hermit  Hermit
llg  Lole  Lole
llh  Lamu  Lamu
lli  Teke-Laali  Teke-Laali
llj  Ladji Ladji  Ladji Ladji
llk  Lelak  Lelak
lll  Lilau  Lilau
llm  Lasalimu  Lasalimu
lln  Lele (Chad)  Lele (Chad)
llo  Khlor  Khlor
llp  North Efate  Efate, North
llq  Lolak  Lolak
lls  Lithuanian Sign Language  Lithuanian Sign Language
llu  Lau  Lau
llx  Lauan  Lauan
lma  East Limba  Limba, East
lmb  Merei  Merei
lmc  Limilngan  Limilngan
lmd  Lumun  Lumun
lme  Pévé  Pévé
lmf  South Lembata  Lembata, South
lmg  Lamogai  Lamogai
lmh  Lambichhong  Lambichhong
lmi  Lombi  Lombi
lmj  West Lembata  Lembata, West
lmk  Lamkang  Lamkang
lml  Hano  Hano
lmm  Lamam  Lamam
lmn  Lambadi  Lambadi
lmo  Lombard  Lombard
lmp  Limbum  Limbum
lmq  Lamatuka  Lamatuka
lmr  Lamalera  Lamalera
lmu  Lamenu  Lamenu
lmv  Lomaiviti  Lomaiviti
lmw  Lake Miwok  Miwok, Lake
lmx  Laimbue  Laimbue
lmy  Lamboya  Lamboya
lmz  Lumbee  Lumbee
lna  Langbashe  Langbashe
lnb  Mbalanhu  Mbalanhu
lnd  Lun Bawang  Lun Bawang
lnd  Lundayeh  Lundayeh
lng  Langobardic  Langobardic
lnh  Lanoh  Lanoh
lni  Daantanai'  Daantanai'
lnj  Leningitij  Leningitij
lnl  South Central Banda  Banda, South Central
lnm  Langam  Langam
lnn  Lorediakarkar  Lorediakarkar
lno  Lango (Sudan)  Lango (Sudan)
lns  Lamnso'  Lamnso'
lnu  Longuda  Longuda
lnw  Lanima  Lanima
lnz  Lonzo  Lonzo
loa  Loloda  Loloda
lob  Lobi  Lobi
loc  Inonhan  Inonhan
loe  Saluan  Saluan
lof  Logol  Logol
log  Logo  Logo
loh  Narim  Narim
loi  Loma (Côte d'Ivoire)  Loma (Côte d'Ivoire)
loj  Lou  Lou
lok  Loko  Loko
lol  Mongo  Mongo
lom  Loma (Liberia)  Loma (Liberia)
lon  Malawi Lomwe  Lomwe, Malawi
loo  Lombo  Lombo
lop  Lopa  Lopa
loq  Lobala  Lobala
lor  Téén  Téén
los  Loniu  Loniu
lot  Otuho  Otuho
lou  Louisiana Creole French  Creole French, Louisiana
lov  Lopi  Lopi
low  Tampias Lobu  Lobu, Tampias
lox  Loun  Loun
loy  Loke  Loke
loz  Lozi  Lozi
lpa  Lelepa  Lelepa
lpe  Lepki  Lepki
lpn  Long Phuri Naga  Naga, Long Phuri
lpo  Lipo  Lipo
lpx  Lopit  Lopit
lra  Rara Bakati'  Rara Bakati'
lrc  Northern Luri  Luri, Northern
lre  Laurentian  Laurentian
lrg  Laragia  Laragia
lri  Marachi  Marachi
lri  Olumarachi  Olumarachi
lrk  Loarki  Loarki
lrl  Lari  Lari
lrm  Marama  Marama
lrm  Olumarama  Olumarama
lrn  Lorang  Lorang
lro  Laro  Laro
lrr  Southern Yamphu  Yamphu, Southern
lrt  Larantuka Malay  Malay, Larantuka
lrv  Larevat  Larevat
lrz  Lemerig  Lemerig
lsa  Lasgerdi  Lasgerdi
lsd  Lishana Deni  Lishana Deni
lse  Lusengo  Lusengo
lsg  Lyons Sign Language  Lyons Sign Language
lsh  Lish  Lish
lsi  Lashi  Lashi
lsl  Latvian Sign Language  Latvian Sign Language
lsm  Olusamia  Olusamia
lsm  Saamia  Saamia
lso  Laos Sign Language  Laos Sign Language
lsp  Lengua de Señas Panameñas  Lengua de Señas Panameñas
lsp  Panamanian Sign Language  Panamanian Sign Language
lsr  Aruop  Aruop
lss  Lasi  Lasi
lst  Trinidad and Tobago Sign Language  Trinidad and Tobago Sign Language
lsy  Mauritian Sign Language  Mauritian Sign Language
ltc  Late Middle Chinese  Chinese, Late Middle
ltg  Latgalian  Latgalian
lti  Leti (Indonesia)  Leti (Indonesia)
ltn  Latundê  Latundê
lto  Olutsotso  Olutsotso
lto  Tsotso  Tsotso
lts  Lutachoni  Lutachoni
lts  Tachoni  Tachoni
ltu  Latu  Latu
ltz  Letzeburgesch  Letzeburgesch
ltz  Luxembourgish  Luxembourgish
lua  Luba-Lulua  Luba-Lulua
lub  Luba-Katanga  Luba-Katanga
luc  Aringa  Aringa
lud  Ludian  Ludian
lue  Luvale  Luvale
luf  Laua  Laua
lug  Ganda  Ganda
lui  Luiseno  Luiseno
luj  Luna  Luna
luk  Lunanakha  Lunanakha
lul  Olu'bo  Olu'bo
lum  Luimbi  Luimbi
lun  Lunda  Lunda
luo  Dholuo  Dholuo
luo  Luo (Kenya and Tanzania)  Luo (Kenya and Tanzania)
lup  Lumbu  Lumbu
luq  Lucumi  Lucumi
lur  Laura  Laura
lus  Lushai  Lushai
lut  Lushootseed  Lushootseed
luu  Lumba-Yakkha  Lumba-Yakkha
luv  Luwati  Luwati
luw  Luo (Cameroon)  Luo (Cameroon)
luy  Luyia  Luyia
luy  Oluluyia  Oluluyia
luz  Southern Luri  Luri, Southern
lva  Maku'a  Maku'a
lvk  Lavukaleve  Lavukaleve
lvs  Standard Latvian  Latvian, Standard
lvu  Levuka  Levuka
lwa  Lwalu  Lwalu
lwe  Lewo Eleng  Lewo Eleng
lwg  Oluwanga  Oluwanga
lwg  Wanga  Wanga
lwh  White Lachi  Lachi, White
lwl  Eastern Lawa  Lawa, Eastern
lwm  Laomian  Laomian
lwo  Luwo  Luwo
lwt  Lewotobi  Lewotobi
lwu  Lawu  Lawu
lww  Lewo  Lewo
lya  Layakha  Layakha
lyg  Lyngngam  Lyngngam
lyn  Luyana  Luyana
lzh  Literary Chinese  Chinese, Literary
lzl  Litzlitz  Litzlitz
lzn  Leinong Naga  Naga, Leinong
lzz  Laz  Laz
maa  San Jerónimo Tecóatl Mazatec  Mazatec, San Jerónimo Tecóatl
mab  Yutanduchi Mixtec  Mixtec, Yutanduchi
mad  Madurese  Madurese
mae  Bo-Rukul  Bo-Rukul
maf  Mafa  Mafa
mag  Magahi  Magahi
mah  Marshallese  Marshallese
mai  Maithili  Maithili
maj  Jalapa De Díaz Mazatec  Mazatec, Jalapa De Díaz
mak  Makasar  Makasar
mal  Malayalam  Malayalam
mam  Mam  Mam
man  Manding  Manding
man  Mandingo  Mandingo
maq  Chiquihuitlán Mazatec  Mazatec, Chiquihuitlán
mar  Marathi  Marathi
mas  Masai  Masai
mat  San Francisco Matlatzinca  Matlatzinca, San Francisco
mau  Huautla Mazatec  Mazatec, Huautla
mav  Sateré-Mawé  Sateré-Mawé
maw  Mampruli  Mampruli
max  North Moluccan Malay  Malay, North Moluccan
maz  Central Mazahua  Mazahua, Central
mba  Higaonon  Higaonon
mbb  Western Bukidnon Manobo  Manobo, Western Bukidnon
mbc  Macushi  Macushi
mbd  Dibabawon Manobo  Manobo, Dibabawon
mbe  Molale  Molale
mbf  Baba Malay  Malay, Baba
mbh  Mangseng  Mangseng
mbi  Ilianen Manobo  Manobo, Ilianen
mbj  Nadëb  Nadëb
mbk  Malol  Malol
mbl  Maxakalí  Maxakalí
mbm  Ombamba  Ombamba
mbn  Macaguán  Macaguán
mbo  Mbo (Cameroon)  Mbo (Cameroon)
mbp  Malayo  Malayo
mbq  Maisin  Maisin
mbr  Nukak Makú  Nukak Makú
mbs  Sarangani Manobo  Manobo, Sarangani
mbt  Matigsalug Manobo  Manobo, Matigsalug
mbu  Mbula-Bwazza  Mbula-Bwazza
mbv  Mbulungish  Mbulungish
mbw  Maring  Maring
mbx  Mari (East Sepik Province)  Mari (East Sepik Province)
mby  Memoni  Memoni
mbz  Amoltepec Mixtec  Mixtec, Amoltepec
mca  Maca  Maca
mcb  Machiguenga  Machiguenga
mcc  Bitur  Bitur
mcd  Sharanahua  Sharanahua
mce  Itundujia Mixtec  Mixtec, Itundujia
mcf  Matsés  Matsés
mcg  Mapoyo  Mapoyo
mch  Maquiritari  Maquiritari
mci  Mese  Mese
mcj  Mvanip  Mvanip
mck  Mbunda  Mbunda
mcl  Macaguaje  Macaguaje
mcm  Malaccan Creole Portuguese  Creole Portuguese, Malaccan
mcn  Masana  Masana
mco  Coatlán Mixe  Mixe, Coatlán
mcp  Makaa  Makaa
mcq  Ese  Ese
mcr  Menya  Menya
mcs  Mambai  Mambai
mct  Mengisa  Mengisa
mcu  Cameroon Mambila  Mambila, Cameroon
mcv  Minanibai  Minanibai
mcw  Mawa (Chad)  Mawa (Chad)
mcx  Mpiemo  Mpiemo
mcy  South Watut  Watut, South
mcz  Mawan  Mawan
mda  Mada (Nigeria)  Mada (Nigeria)
mdb  Morigi  Morigi
mdc  Male (Papua New Guinea)  Male (Papua New Guinea)
mdd  Mbum  Mbum
mde  Maba (Chad)  Maba (Chad)
mdf  Moksha  Moksha
mdg  Massalat  Massalat
mdh  Maguindanaon  Maguindanaon
mdi  Mamvu  Mamvu
mdj  Mangbetu  Mangbetu
mdk  Mangbutu  Mangbutu
mdl  Maltese Sign Language  Maltese Sign Language
mdm  Mayogo  Mayogo
mdn  Mbati  Mbati
mdp  Mbala  Mbala
mdq  Mbole  Mbole
mdr  Mandar  Mandar
mds  Maria (Papua New Guinea)  Maria (Papua New Guinea)
mdt  Mbere  Mbere
mdu  Mboko  Mboko
mdv  Santa Lucía Monteverde Mixtec  Mixtec, Santa Lucía Monteverde
mdw  Mbosi  Mbosi
mdx  Dizin  Dizin
mdy  Male (Ethiopia)  Male (Ethiopia)
mdz  Suruí Do Pará  Suruí Do Pará
mea  Menka  Menka
meb  Ikobi  Ikobi
mec  Mara  Mara
med  Melpa  Melpa
mee  Mengen  Mengen
mef  Megam  Megam
meh  Southwestern Tlaxiaco Mixtec  Mixtec, Southwestern Tlaxiaco
mei  Midob  Midob
mej  Meyah  Meyah
mek  Mekeo  Mekeo
mel  Central Melanau  Melanau, Central
mem  Mangala  Mangala
men  Mende (Sierra Leone)  Mende (Sierra Leone)
meo  Kedah Malay  Malay, Kedah
mep  Miriwung  Miriwung
meq  Merey  Merey
mer  Meru  Meru
mes  Masmaje  Masmaje
met  Mato  Mato
meu  Motu  Motu
mev  Mano  Mano
mew  Maaka  Maaka
mey  Hassaniyya  Hassaniyya
mez  Menominee  Menominee
mfa  Pattani Malay  Malay, Pattani
mfb  Bangka  Bangka
mfc  Mba  Mba
mfd  Mendankwe-Nkwen  Mendankwe-Nkwen
mfe  Morisyen  Morisyen
mff  Naki  Naki
mfg  Mogofin  Mogofin
mfh  Matal  Matal
mfi  Wandala  Wandala
mfj  Mefele  Mefele
mfk  North Mofu  Mofu, North
mfl  Putai  Putai
mfm  Marghi South  Marghi South
mfn  Cross River Mbembe  Mbembe, Cross River
mfo  Mbe  Mbe
mfp  Makassar Malay  Malay, Makassar
mfq  Moba  Moba
mfr  Marithiel  Marithiel
mfs  Mexican Sign Language  Mexican Sign Language
mft  Mokerang  Mokerang
mfu  Mbwela  Mbwela
mfv  Mandjak  Mandjak
mfw  Mulaha  Mulaha
mfx  Melo  Melo
mfy  Mayo  Mayo
mfz  Mabaan  Mabaan
mga  Middle Irish (900-1200)  Irish, Middle (900-1200)
mgb  Mararit  Mararit
mgc  Morokodo  Morokodo
mgd  Moru  Moru
mge  Mango  Mango
mgf  Maklew  Maklew
mgg  Mpumpong  Mpumpong
mgh  Makhuwa-Meetto  Makhuwa-Meetto
mgi  Lijili  Lijili
mgj  Abureni  Abureni
mgk  Mawes  Mawes
mgl  Maleu-Kilenge  Maleu-Kilenge
mgm  Mambae  Mambae
mgn  Mbangi  Mbangi
mgo  Meta'  Meta'
mgp  Eastern Magar  Magar, Eastern
mgq  Malila  Malila
mgr  Mambwe-Lungu  Mambwe-Lungu
mgs  Manda (Tanzania)  Manda (Tanzania)
mgt  Mongol  Mongol
mgu  Mailu  Mailu
mgv  Matengo  Matengo
mgw  Matumbi  Matumbi
mgy  Mbunga  Mbunga
mgz  Mbugwe  Mbugwe
mha  Manda (India)  Manda (India)
mhb  Mahongwe  Mahongwe
mhc  Mocho  Mocho
mhd  Mbugu  Mbugu
mhe  Besisi  Besisi
mhe  Mah Meri  Mah Meri
mhf  Mamaa  Mamaa
mhg  Margu  Margu
mhh  Maskoy Pidgin  Maskoy Pidgin
mhi  Ma'di  Ma'di
mhj  Mogholi  Mogholi
mhk  Mungaka  Mungaka
mhl  Mauwake  Mauwake
mhm  Makhuwa-Moniga  Makhuwa-Moniga
mhn  Mócheno  Mócheno
mho  Mashi (Zambia)  Mashi (Zambia)
mhp  Balinese Malay  Malay, Balinese
mhq  Mandan  Mandan
mhr  Eastern Mari  Mari, Eastern
mhs  Buru (Indonesia)  Buru (Indonesia)
mht  Mandahuaca  Mandahuaca
mhu  Darang Deng  Deng, Darang
mhu  Digaro-Mishmi  Digaro-Mishmi
mhw  Mbukushu  Mbukushu
mhx  Lhaovo  Lhaovo
mhx  Maru  Maru
mhy  Ma'anyan  Ma'anyan
mhz  Mor (Mor Islands)  Mor (Mor Islands)
mia  Miami  Miami
mib  Atatláhuca Mixtec  Mixtec, Atatláhuca
mic  Micmac  Micmac
mic  Mi'kmaq  Mi'kmaq
mid  Mandaic  Mandaic
mie  Ocotepec Mixtec  Mixtec, Ocotepec
mif  Mofu-Gudur  Mofu-Gudur
mig  San Miguel El Grande Mixtec  Mixtec, San Miguel El Grande
mih  Chayuco Mixtec  Mixtec, Chayuco
mii  Chigmecatitlán Mixtec  Mixtec, Chigmecatitlán
mij  Abar  Abar
mij  Mungbam  Mungbam
mik  Mikasuki  Mikasuki
mil  Peñoles Mixtec  Mixtec, Peñoles
mim  Alacatlatzala Mixtec  Mixtec, Alacatlatzala
min  Minangkabau  Minangkabau
mio  Pinotepa Nacional Mixtec  Mixtec, Pinotepa Nacional
mip  Apasco-Apoala Mixtec  Mixtec, Apasco-Apoala
miq  Mískito  Mískito
mir  Isthmus Mixe  Mixe, Isthmus
mis  Uncoded languages  Uncoded languages
mit  Southern Puebla Mixtec  Mixtec, Southern Puebla
miu  Cacaloxtepec Mixtec  Mixtec, Cacaloxtepec
miw  Akoye  Akoye
mix  Mixtepec Mixtec  Mixtec, Mixtepec
miy  Ayutla Mixtec  Mixtec, Ayutla
miz  Coatzospan Mixtec  Mixtec, Coatzospan
mjc  San Juan Colorado Mixtec  Mixtec, San Juan Colorado
mjd  Northwest Maidu  Maidu, Northwest
mje  Muskum  Muskum
mjg  Tu  Tu
mjh  Mwera (Nyasa)  Mwera (Nyasa)
mji  Kim Mun  Kim Mun
mjj  Mawak  Mawak
mjk  Matukar  Matukar
mjl  Mandeali  Mandeali
mjm  Medebur  Medebur
mjn  Ma (Papua New Guinea)  Ma (Papua New Guinea)
mjo  Malankuravan  Malankuravan
mjp  Malapandaram  Malapandaram
mjq  Malaryan  Malaryan
mjr  Malavedan  Malavedan
mjs  Miship  Miship
mjt  Sauria Paharia  Sauria Paharia
mju  Manna-Dora  Manna-Dora
mjv  Mannan  Mannan
mjw  Karbi  Karbi
mjx  Mahali  Mahali
mjy  Mahican  Mahican
mjz  Majhi  Majhi
mka  Mbre  Mbre
mkb  Mal Paharia  Mal Paharia
mkc  Siliput  Siliput
mkd  Macedonian  Macedonian
mke  Mawchi  Mawchi
mkf  Miya  Miya
mkg  Mak (China)  Mak (China)
mki  Dhatki  Dhatki
mkj  Mokilese  Mokilese
mkk  Byep  Byep
mkl  Mokole  Mokole
mkm  Moklen  Moklen
mkn  Kupang Malay  Malay, Kupang
mko  Mingang Doso  Mingang Doso
mkp  Moikodi  Moikodi
mkq  Bay Miwok  Miwok, Bay
mkr  Malas  Malas
mks  Silacayoapan Mixtec  Mixtec, Silacayoapan
mkt  Vamale  Vamale
mku  Konyanka Maninka  Maninka, Konyanka
mkv  Mafea  Mafea
mkw  Kituba (Congo)  Kituba (Congo)
mkx  Kinamiging Manobo  Manobo, Kinamiging
mky  East Makian  Makian, East
mkz  Makasae  Makasae
mla  Malo  Malo
mlb  Mbule  Mbule
mlc  Cao Lan  Cao Lan
mle  Manambu  Manambu
mlf  Mal  Mal
mlg  Malagasy  Malagasy
mlh  Mape  Mape
mli  Malimpung  Malimpung
mlj  Miltu  Miltu
mlk  Ilwana  Ilwana
mlk  Kiwilwana  Kiwilwana
mll  Malua Bay  Malua Bay
mlm  Mulam  Mulam
mln  Malango  Malango
mlo  Mlomp  Mlomp
mlp  Bargam  Bargam
mlq  Western Maninkakan  Maninkakan, Western
mlr  Vame  Vame
mls  Masalit  Masalit
mlt  Maltese  Maltese
mlu  To'abaita  To'abaita
mlv  Motlav  Motlav
mlv  Mwotlap  Mwotlap
mlw  Moloko  Moloko
mlx  Malfaxal  Malfaxal
mlx  Naha'ai  Naha'ai
mlz  Malaynon  Malaynon
mma  Mama  Mama
mmb  Momina  Momina
mmc  Michoacán Mazahua  Mazahua, Michoacán
mmd  Maonan  Maonan
mme  Mae  Mae
mmf  Mundat  Mundat
mmg  North Ambrym  Ambrym, North
mmh  Mehináku  Mehináku
mmi  Musar  Musar
mmj  Majhwar  Majhwar
mmk  Mukha-Dora  Mukha-Dora
mml  Man Met  Man Met
mmm  Maii  Maii
mmn  Mamanwa  Mamanwa
mmo  Mangga Buang  Buang, Mangga
mmp  Siawi  Siawi
mmq  Musak  Musak
mmr  Western Xiangxi Miao  Miao, Western Xiangxi
mmt  Malalamai  Malalamai
mmu  Mmaala  Mmaala
mmv  Miriti  Miriti
mmw  Emae  Emae
mmx  Madak  Madak
mmy  Migaama  Migaama
mmz  Mabaale  Mabaale
mna  Mbula  Mbula
mnb  Muna  Muna
mnc  Manchu  Manchu
mnd  Mondé  Mondé
mne  Naba  Naba
mnf  Mundani  Mundani
mng  Eastern Mnong  Mnong, Eastern
mnh  Mono (Democratic Republic of Congo)  Mono (Democratic Republic of Congo)
mni  Manipuri  Manipuri
mnj  Munji  Munji
mnk  Mandinka  Mandinka
mnl  Tiale  Tiale
mnm  Mapena  Mapena
mnn  Southern Mnong  Mnong, Southern
mnp  Min Bei Chinese  Chinese, Min Bei
mnq  Minriq  Minriq
mnr  Mono (USA)  Mono (USA)
mns  Mansi  Mansi
mnu  Mer  Mer
mnv  Rennell-Bellona  Rennell-Bellona
mnw  Mon  Mon
mnx  Manikion  Manikion
mny  Manyawa  Manyawa
mnz  Moni  Moni
moa  Mwan  Mwan
moc  Mocoví  Mocoví
mod  Mobilian  Mobilian
moe  Montagnais  Montagnais
mog  Mongondow  Mongondow
moh  Mohawk  Mohawk
moi  Mboi  Mboi
moj  Monzombo  Monzombo
mok  Morori  Morori
mom  Mangue  Mangue
mon  Mongolian  Mongolian
moo  Monom  Monom
mop  Mopán Maya  Mopán Maya
moq  Mor (Bomberai Peninsula)  Mor (Bomberai Peninsula)
mor  Moro  Moro
mos  Mossi  Mossi
mot  Barí  Barí
mou  Mogum  Mogum
mov  Mohave  Mohave
mow  Moi (Congo)  Moi (Congo)
mox  Molima  Molima
moy  Shekkacho  Shekkacho
moz  Gergiko  Gergiko
moz  Mukulu  Mukulu
mpa  Mpoto  Mpoto
mpb  Mullukmulluk  Mullukmulluk
mpc  Mangarayi  Mangarayi
mpd  Machinere  Machinere
mpe  Majang  Majang
mpg  Marba  Marba
mph  Maung  Maung
mpi  Mpade  Mpade
mpj  Martu Wangka  Martu Wangka
mpk  Mbara (Chad)  Mbara (Chad)
mpl  Middle Watut  Watut, Middle
mpm  Yosondúa Mixtec  Mixtec, Yosondúa
mpn  Mindiri  Mindiri
mpo  Miu  Miu
mpp  Migabac  Migabac
mpq  Matís  Matís
mpr  Vangunu  Vangunu
mps  Dadibi  Dadibi
mpt  Mian  Mian
mpu  Makuráp  Makuráp
mpv  Mungkip  Mungkip
mpw  Mapidian  Mapidian
mpx  Misima-Panaeati  Misima-Panaeati
mpy  Mapia  Mapia
mpz  Mpi  Mpi
mqa  Maba (Indonesia)  Maba (Indonesia)
mqb  Mbuko  Mbuko
mqc  Mangole  Mangole
mqe  Matepi  Matepi
mqf  Momuna  Momuna
mqg  Kota Bangun Kutai Malay  Malay, Kota Bangun Kutai
mqh  Tlazoyaltepec Mixtec  Mixtec, Tlazoyaltepec
mqi  Mariri  Mariri
mqj  Mamasa  Mamasa
mqk  Rajah Kabunsuwan Manobo  Manobo, Rajah Kabunsuwan
mql  Mbelime  Mbelime
mqm  South Marquesan  Marquesan, South
mqn  Moronene  Moronene
mqo  Modole  Modole
mqp  Manipa  Manipa
mqq  Minokok  Minokok
mqr  Mander  Mander
mqs  West Makian  Makian, West
mqt  Mok  Mok
mqu  Mandari  Mandari
mqv  Mosimo  Mosimo
mqw  Murupi  Murupi
mqx  Mamuju  Mamuju
mqy  Manggarai  Manggarai
mqz  Pano  Pano
mra  Mlabri  Mlabri
mrb  Marino  Marino
mrc  Maricopa  Maricopa
mrd  Western Magar  Magar, Western
mre  Martha's Vineyard Sign Language  Martha's Vineyard Sign Language
mrf  Elseng  Elseng
mrg  Mising  Mising
mrh  Mara Chin  Chin, Mara
mri  Maori  Maori
mrj  Western Mari  Mari, Western
mrk  Hmwaveke  Hmwaveke
mrl  Mortlockese  Mortlockese
mrm  Merlav  Merlav
mrm  Mwerlap  Mwerlap
mrn  Cheke Holo  Cheke Holo
mro  Mru  Mru
mrp  Morouas  Morouas
mrq  North Marquesan  Marquesan, North
mrr  Maria (India)  Maria (India)
mrs  Maragus  Maragus
mrt  Marghi Central  Marghi Central
mru  Mono (Cameroon)  Mono (Cameroon)
mrv  Mangareva  Mangareva
mrw  Maranao  Maranao
mrx  Dineor  Dineor
mrx  Maremgi  Maremgi
mry  Mandaya  Mandaya
mrz  Marind  Marind
msa  Malay (macrolanguage)  Malay (macrolanguage)
msb  Masbatenyo  Masbatenyo
msc  Sankaran Maninka  Maninka, Sankaran
msd  Yucatec Maya Sign Language  Yucatec Maya Sign Language
mse  Musey  Musey
msf  Mekwei  Mekwei
msg  Moraid  Moraid
msh  Masikoro Malagasy  Malagasy, Masikoro
msi  Sabah Malay  Malay, Sabah
msj  Ma (Democratic Republic of Congo)  Ma (Democratic Republic of Congo)
msk  Mansaka  Mansaka
msl  Molof  Molof
msl  Poule  Poule
msm  Agusan Manobo  Manobo, Agusan
msn  Vurës  Vurës
mso  Mombum  Mombum
msp  Maritsauá  Maritsauá
msq  Caac  Caac
msr  Mongolian Sign Language  Mongolian Sign Language
mss  West Masela  Masela, West
msu  Musom  Musom
msv  Maslam  Maslam
msw  Mansoanka  Mansoanka
msx  Moresada  Moresada
msy  Aruamu  Aruamu
msz  Momare  Momare
mta  Cotabato Manobo  Manobo, Cotabato
mtb  Anyin Morofo  Anyin Morofo
mtc  Munit  Munit
mtd  Mualang  Mualang
mte  Mono (Solomon Islands)  Mono (Solomon Islands)
mtf  Murik (Papua New Guinea)  Murik (Papua New Guinea)
mtg  Una  Una
mth  Munggui  Munggui
mti  Maiwa (Papua New Guinea)  Maiwa (Papua New Guinea)
mtj  Moskona  Moskona
mtk  Mbe'  Mbe'
mtl  Montol  Montol
mtm  Mator  Mator
mtn  Matagalpa  Matagalpa
mto  Totontepec Mixe  Mixe, Totontepec
mtp  Wichí Lhamtés Nocten  Wichí Lhamtés Nocten
mtq  Muong  Muong
mtr  Mewari  Mewari
mts  Yora  Yora
mtt  Mota  Mota
mtu  Tututepec Mixtec  Mixtec, Tututepec
mtv  Asaro'o  Asaro'o
mtw  Southern Binukidnon  Binukidnon, Southern
mtx  Tidaá Mixtec  Mixtec, Tidaá
mty  Nabi  Nabi
mua  Mundang  Mundang
mub  Mubi  Mubi
muc  Ajumbu  Ajumbu
mud  Mednyj Aleut  Aleut, Mednyj
mue  Media Lengua  Media Lengua
mug  Musgu  Musgu
muh  Mündü  Mündü
mui  Musi  Musi
muj  Mabire  Mabire
muk  Mugom  Mugom
mul  Multiple languages  Multiple languages
mum  Maiwala  Maiwala
muo  Nyong  Nyong
mup  Malvi  Malvi
muq  Eastern Xiangxi Miao  Miao, Eastern Xiangxi
mur  Murle  Murle
mus  Creek  Creek
mut  Western Muria  Muria, Western
muu  Yaaku  Yaaku
muv  Muthuvan  Muthuvan
mux  Bo-Ung  Bo-Ung
muy  Muyang  Muyang
muz  Mursi  Mursi
mva  Manam  Manam
mvb  Mattole  Mattole
mvd  Mamboru  Mamboru
mve  Marwari (Pakistan)  Marwari (Pakistan)
mvf  Peripheral Mongolian  Mongolian, Peripheral
mvg  Yucuañe Mixtec  Mixtec, Yucuañe
mvh  Mulgi  Mulgi
mvi  Miyako  Miyako
mvk  Mekmek  Mekmek
mvl  Mbara (Australia)  Mbara (Australia)
mvm  Muya  Muya
mvn  Minaveha  Minaveha
mvo  Marovo  Marovo
mvp  Duri  Duri
mvq  Moere  Moere
mvr  Marau  Marau
mvs  Massep  Massep
mvt  Mpotovoro  Mpotovoro
mvu  Marfa  Marfa
mvv  Tagal Murut  Murut, Tagal
mvw  Machinga  Machinga
mvx  Meoswar  Meoswar
mvy  Indus Kohistani  Kohistani, Indus
mvz  Mesqan  Mesqan
mwa  Mwatebu  Mwatebu
mwb  Juwal  Juwal
mwc  Are  Are
mwe  Mwera (Chimwera)  Mwera (Chimwera)
mwf  Murrinh-Patha  Murrinh-Patha
mwg  Aiklep  Aiklep
mwh  Mouk-Aria  Mouk-Aria
mwi  Labo  Labo
mwi  Ninde  Ninde
mwj  Maligo  Maligo
mwk  Kita Maninkakan  Maninkakan, Kita
mwl  Mirandese  Mirandese
mwm  Sar  Sar
mwn  Nyamwanga  Nyamwanga
mwo  Central Maewo  Maewo, Central
mwp  Kala Lagaw Ya  Kala Lagaw Ya
mwq  Mün Chin  Chin, Mün
mwr  Marwari  Marwari
mws  Mwimbi-Muthambi  Mwimbi-Muthambi
mwt  Moken  Moken
mwu  Mittu  Mittu
mwv  Mentawai  Mentawai
mww  Hmong Daw  Hmong Daw
mwx  Mediak  Mediak
mwy  Mosiro  Mosiro
mwz  Moingi  Moingi
mxa  Northwest Oaxaca Mixtec  Mixtec, Northwest Oaxaca
mxb  Tezoatlán Mixtec  Mixtec, Tezoatlán
mxc  Manyika  Manyika
mxd  Modang  Modang
mxe  Mele-Fila  Mele-Fila
mxf  Malgbe  Malgbe
mxg  Mbangala  Mbangala
mxh  Mvuba  Mvuba
mxi  Mozarabic  Mozarabic
mxj  Geman Deng  Deng, Geman
mxj  Miju-Mishmi  Miju-Mishmi
mxk  Monumbo  Monumbo
mxl  Maxi Gbe  Gbe, Maxi
mxm  Meramera  Meramera
mxn  Moi (Indonesia)  Moi (Indonesia)
mxo  Mbowe  Mbowe
mxp  Tlahuitoltepec Mixe  Mixe, Tlahuitoltepec
mxq  Juquila Mixe  Mixe, Juquila
mxr  Murik (Malaysia)  Murik (Malaysia)
mxs  Huitepec Mixtec  Mixtec, Huitepec
mxt  Jamiltepec Mixtec  Mixtec, Jamiltepec
mxu  Mada (Cameroon)  Mada (Cameroon)
mxv  Metlatónoc Mixtec  Mixtec, Metlatónoc
mxw  Namo  Namo
mxx  Mahou  Mahou
mxx  Mawukakan  Mawukakan
mxy  Southeastern Nochixtlán Mixtec  Mixtec, Southeastern Nochixtlán
mxz  Central Masela  Masela, Central
mya  Burmese  Burmese
myb  Mbay  Mbay
myc  Mayeka  Mayeka
myd  Maramba  Maramba
mye  Myene  Myene
myf  Bambassi  Bambassi
myg  Manta  Manta
myh  Makah  Makah
myi  Mina (India)  Mina (India)
myj  Mangayat  Mangayat
myk  Mamara Senoufo  Senoufo, Mamara
myl  Moma  Moma
mym  Me'en  Me'en
myo  Anfillo  Anfillo
myp  Pirahã  Pirahã
myr  Muniche  Muniche
mys  Mesmes  Mesmes
myu  Mundurukú  Mundurukú
myv  Erzya  Erzya
myw  Muyuw  Muyuw
myx  Masaaba  Masaaba
myy  Macuna  Macuna
myz  Classical Mandaic  Mandaic, Classical
mza  Santa María Zacatepec Mixtec  Mixtec, Santa María Zacatepec
mzb  Tumzabt  Tumzabt
mzc  Madagascar Sign Language  Madagascar Sign Language
mzd  Malimba  Malimba
mze  Morawa  Morawa
mzg  Monastic Sign Language  Monastic Sign Language
mzh  Wichí Lhamtés Güisnay  Wichí Lhamtés Güisnay
mzi  Ixcatlán Mazatec  Mazatec, Ixcatlán
mzj  Manya  Manya
mzk  Nigeria Mambila  Mambila, Nigeria
mzl  Mazatlán Mixe  Mixe, Mazatlán
mzm  Mumuye  Mumuye
mzn  Mazanderani  Mazanderani
mzo  Matipuhy  Matipuhy
mzp  Movima  Movima
mzq  Mori Atas  Mori Atas
mzr  Marúbo  Marúbo
mzs  Macanese  Macanese
mzt  Mintil  Mintil
mzu  Inapang  Inapang
mzv  Manza  Manza
mzw  Deg  Deg
mzx  Mawayana  Mawayana
mzy  Mozambican Sign Language  Mozambican Sign Language
mzz  Maiadomu  Maiadomu
naa  Namla  Namla
nab  Southern Nambikuára  Nambikuára, Southern
nac  Narak  Narak
nad  Nijadali  Nijadali
nae  Naka'ela  Naka'ela
naf  Nabak  Nabak
nag  Naga Pidgin  Naga Pidgin
naj  Nalu  Nalu
nak  Nakanai  Nakanai
nal  Nalik  Nalik
nam  Ngan'gityemerri  Ngan'gityemerri
nan  Min Nan Chinese  Chinese, Min Nan
nao  Naaba  Naaba
nap  Neapolitan  Neapolitan
naq  Nama (Namibia)  Nama (Namibia)
nar  Iguta  Iguta
nas  Naasioi  Naasioi
nat  Hungworo  Hungworo
nau  Nauru  Nauru
nav  Navaho  Navaho
nav  Navajo  Navajo
naw  Nawuri  Nawuri
nax  Nakwi  Nakwi
nay  Narrinyeri  Narrinyeri
naz  Coatepec Nahuatl  Nahuatl, Coatepec
nba  Nyemba  Nyemba
nbb  Ndoe  Ndoe
nbc  Chang Naga  Naga, Chang
nbd  Ngbinda  Ngbinda
nbe  Konyak Naga  Naga, Konyak
nbg  Nagarchal  Nagarchal
nbh  Ngamo  Ngamo
nbi  Mao Naga  Naga, Mao
nbj  Ngarinman  Ngarinman
nbk  Nake  Nake
nbl  South Ndebele  Ndebele, South
nbm  Ngbaka Ma'bo  Ngbaka Ma'bo
nbn  Kuri  Kuri
nbo  Nkukoli  Nkukoli
nbp  Nnam  Nnam
nbq  Nggem  Nggem
nbr  Numana-Nunku-Gbantu-Numbu  Numana-Nunku-Gbantu-Numbu
nbs  Namibian Sign Language  Namibian Sign Language
nbt  Na  Na
nbu  Rongmei Naga  Naga, Rongmei
nbv  Ngamambo  Ngamambo
nbw  Southern Ngbandi  Ngbandi, Southern
nby  Ningera  Ningera
nca  Iyo  Iyo
ncb  Central Nicobarese  Nicobarese, Central
ncc  Ponam  Ponam
ncd  Nachering  Nachering
nce  Yale  Yale
ncf  Notsi  Notsi
ncg  Nisga'a  Nisga'a
nch  Central Huasteca Nahuatl  Nahuatl, Central Huasteca
nci  Classical Nahuatl  Nahuatl, Classical
ncj  Northern Puebla Nahuatl  Nahuatl, Northern Puebla
nck  Nakara  Nakara
ncl  Michoacán Nahuatl  Nahuatl, Michoacán
ncm  Nambo  Nambo
ncn  Nauna  Nauna
nco  Sibe  Sibe
ncp  Ndaktup  Ndaktup
ncr  Ncane  Ncane
ncs  Nicaraguan Sign Language  Nicaraguan Sign Language
nct  Chothe Naga  Naga, Chothe
ncu  Chumburung  Chumburung
ncx  Central Puebla Nahuatl  Nahuatl, Central Puebla
ncz  Natchez  Natchez
nda  Ndasa  Ndasa
ndb  Kenswei Nsei  Kenswei Nsei
ndc  Ndau  Ndau
ndd  Nde-Nsele-Nta  Nde-Nsele-Nta
nde  North Ndebele  Ndebele, North
ndf  Nadruvian  Nadruvian
ndg  Ndengereko  Ndengereko
ndh  Ndali  Ndali
ndi  Samba Leko  Samba Leko
ndj  Ndamba  Ndamba
ndk  Ndaka  Ndaka
ndl  Ndolo  Ndolo
ndm  Ndam  Ndam
ndn  Ngundi  Ngundi
ndo  Ndonga  Ndonga
ndp  Ndo  Ndo
ndq  Ndombe  Ndombe
ndr  Ndoola  Ndoola
nds  Low German  German, Low
nds  Low Saxon  Saxon, Low
ndt  Ndunga  Ndunga
ndu  Dugun  Dugun
ndv  Ndut  Ndut
ndw  Ndobo  Ndobo
ndx  Nduga  Nduga
ndy  Lutos  Lutos
ndz  Ndogo  Ndogo
nea  Eastern Ngad'a  Ngad'a, Eastern
neb  Toura (Côte d'Ivoire)  Toura (Côte d'Ivoire)
nec  Nedebang  Nedebang
ned  Nde-Gbite  Nde-Gbite
nee  Nêlêmwa-Nixumwak  Nêlêmwa-Nixumwak
nef  Nefamese  Nefamese
neg  Negidal  Negidal
neh  Nyenkha  Nyenkha
nei  Neo-Hittite  Hittite, Neo-
nej  Neko  Neko
nek  Neku  Neku
nem  Nemi  Nemi
nen  Nengone  Nengone
neo  Ná-Meo  Ná-Meo
nep  Nepali (macrolanguage)  Nepali (macrolanguage)
neq  North Central Mixe  Mixe, North Central
ner  Yahadian  Yahadian
nes  Bhoti Kinnauri  Kinnauri, Bhoti
net  Nete  Nete
neu  Neo  Neo
nev  Nyaheun  Nyaheun
new  Nepal Bhasa  Bhasa, Nepal
new  Newari  Newari
nex  Neme  Neme
ney  Neyo  Neyo
nez  Nez Perce  Nez Perce
nfa  Dhao  Dhao
nfd  Ahwai  Ahwai
nfl  Äiwoo  Äiwoo
nfl  Ayiwo  Ayiwo
nfr  Nafaanra  Nafaanra
nfu  Mfumte  Mfumte
nga  Ngbaka  Ngbaka
ngb  Northern Ngbandi  Ngbandi, Northern
ngc  Ngombe (Democratic Republic of Congo)  Ngombe (Democratic Republic of Congo)
ngd  Ngando (Central African Republic)  Ngando (Central African Republic)
nge  Ngemba  Ngemba
ngg  Ngbaka Manza  Ngbaka Manza
ngh  N/u  N/u
ngi  Ngizim  Ngizim
ngj  Ngie  Ngie
ngk  Dalabon  Dalabon
ngl  Lomwe  Lomwe
ngm  Ngatik Men's Creole  Ngatik Men's Creole
ngn  Ngwo  Ngwo
ngo  Ngoni  Ngoni
ngp  Ngulu  Ngulu
ngq  Ngoreme  Ngoreme
ngq  Ngurimi  Ngurimi
ngr  Engdewu  Engdewu
ngs  Gvoko  Gvoko
ngt  Ngeq  Ngeq
ngu  Guerrero Nahuatl  Nahuatl, Guerrero
ngv  Nagumi  Nagumi
ngw  Ngwaba  Ngwaba
ngx  Nggwahyi  Nggwahyi
ngy  Tibea  Tibea
ngz  Ngungwel  Ngungwel
nha  Nhanda  Nhanda
nhb  Beng  Beng
nhc  Tabasco Nahuatl  Nahuatl, Tabasco
nhd  Ava Guaraní  Guaraní, Ava
nhd  Chiripá  Chiripá
nhe  Eastern Huasteca Nahuatl  Nahuatl, Eastern Huasteca
nhf  Nhuwala  Nhuwala
nhg  Tetelcingo Nahuatl  Nahuatl, Tetelcingo
nhh  Nahari  Nahari
nhi  Zacatlán-Ahuacatlán-Tepetzintla Nahuatl  Nahuatl, Zacatlán-Ahuacatlán-Tepetzintla
nhk  Isthmus-Cosoleacaque Nahuatl  Nahuatl, Isthmus-Cosoleacaque
nhm  Morelos Nahuatl  Nahuatl, Morelos
nhn  Central Nahuatl  Nahuatl, Central
nho  Takuu  Takuu
nhp  Isthmus-Pajapan Nahuatl  Nahuatl, Isthmus-Pajapan
nhq  Huaxcaleca Nahuatl  Nahuatl, Huaxcaleca
nhr  Naro  Naro
nht  Ometepec Nahuatl  Nahuatl, Ometepec
nhu  Noone  Noone
nhv  Temascaltepec Nahuatl  Nahuatl, Temascaltepec
nhw  Western Huasteca Nahuatl  Nahuatl, Western Huasteca
nhx  Isthmus-Mecayapan Nahuatl  Nahuatl, Isthmus-Mecayapan
nhy  Northern Oaxaca Nahuatl  Nahuatl, Northern Oaxaca
nhz  Santa María La Alta Nahuatl  Nahuatl, Santa María La Alta
nia  Nias  Nias
nib  Nakame  Nakame
nid  Ngandi  Ngandi
nie  Niellim  Niellim
nif  Nek  Nek
nig  Ngalakan  Ngalakan
nih  Nyiha (Tanzania)  Nyiha (Tanzania)
nii  Nii  Nii
nij  Ngaju  Ngaju
nik  Southern Nicobarese  Nicobarese, Southern
nil  Nila  Nila
nim  Nilamba  Nilamba
nin  Ninzo  Ninzo
nio  Nganasan  Nganasan
niq  Nandi  Nandi
nir  Nimboran  Nimboran
nis  Nimi  Nimi
nit  Southeastern Kolami  Kolami, Southeastern
niu  Niuean  Niuean
niv  Gilyak  Gilyak
niw  Nimo  Nimo
nix  Hema  Hema
niy  Ngiti  Ngiti
niz  Ningil  Ningil
nja  Nzanyi  Nzanyi
njb  Nocte Naga  Naga, Nocte
njd  Ndonde Hamba  Ndonde Hamba
njh  Lotha Naga  Naga, Lotha
nji  Gudanji  Gudanji
njj  Njen  Njen
njl  Njalgulgule  Njalgulgule
njm  Angami Naga  Naga, Angami
njn  Liangmai Naga  Naga, Liangmai
njo  Ao Naga  Naga, Ao
njr  Njerep  Njerep
njs  Nisa  Nisa
njt  Ndyuka-Trio Pidgin  Ndyuka-Trio Pidgin
nju  Ngadjunmaya  Ngadjunmaya
njx  Kunyi  Kunyi
njy  Njyem  Njyem
njz  Nyishi  Nyishi
nka  Nkoya  Nkoya
nkb  Khoibu Naga  Naga, Khoibu
nkc  Nkongho  Nkongho
nkd  Koireng  Koireng
nke  Duke  Duke
nkf  Inpui Naga  Naga, Inpui
nkg  Nekgini  Nekgini
nkh  Khezha Naga  Naga, Khezha
nki  Thangal Naga  Naga, Thangal
nkj  Nakai  Nakai
nkk  Nokuku  Nokuku
nkm  Namat  Namat
nkn  Nkangala  Nkangala
nko  Nkonya  Nkonya
nkp  Niuatoputapu  Niuatoputapu
nkq  Nkami  Nkami
nkr  Nukuoro  Nukuoro
nks  North Asmat  Asmat, North
nkt  Nyika (Tanzania)  Nyika (Tanzania)
nku  Bouna Kulango  Kulango, Bouna
nkv  Nyika (Malawi and Zambia)  Nyika (Malawi and Zambia)
nkw  Nkutu  Nkutu
nkx  Nkoroo  Nkoroo
nkz  Nkari  Nkari
nla  Ngombale  Ngombale
nlc  Nalca  Nalca
nld  Dutch  Dutch
nld  Flemish  Flemish
nle  East Nyala  Nyala, East
nlg  Gela  Gela
nli  Grangali  Grangali
nlj  Nyali  Nyali
nlk  Ninia Yali  Yali, Ninia
nll  Nihali  Nihali
nlo  Ngul  Ngul
nlq  Lao Naga  Naga, Lao
nlu  Nchumbulu  Nchumbulu
nlv  Orizaba Nahuatl  Nahuatl, Orizaba
nlw  Walangama  Walangama
nlx  Nahali  Nahali
nly  Nyamal  Nyamal
nlz  Nalögo  Nalögo
nma  Maram Naga  Naga, Maram
nmb  Big Nambas  Nambas, Big
nmb  V'ënen Taut  V'ënen Taut
nmc  Ngam  Ngam
nmd  Ndumu  Ndumu
nme  Mzieme Naga  Naga, Mzieme
nmf  Tangkhul Naga (India)  Naga, Tangkhul (India)
nmg  Kwasio  Kwasio
nmh  Monsang Naga  Naga, Monsang
nmi  Nyam  Nyam
nmj  Ngombe (Central African Republic)  Ngombe (Central African Republic)
nmk  Namakura  Namakura
nml  Ndemli  Ndemli
nmm  Manangba  Manangba
nmn  !Xóõ  !Xóõ
nmo  Moyon Naga  Naga, Moyon
nmp  Nimanbur  Nimanbur
nmq  Nambya  Nambya
nmr  Nimbari  Nimbari
nms  Letemboi  Letemboi
nmt  Namonuito  Namonuito
nmu  Northeast Maidu  Maidu, Northeast
nmv  Ngamini  Ngamini
nmw  Nimoa  Nimoa
nmx  Nama (Papua New Guinea)  Nama (Papua New Guinea)
nmy  Namuyi  Namuyi
nmz  Nawdm  Nawdm
nna  Nyangumarta  Nyangumarta
nnb  Nande  Nande
nnc  Nancere  Nancere
nnd  West Ambae  Ambae, West
nne  Ngandyera  Ngandyera
nnf  Ngaing  Ngaing
nng  Maring Naga  Naga, Maring
nnh  Ngiemboon  Ngiemboon
nni  North Nuaulu  Nuaulu, North
nnj  Nyangatom  Nyangatom
nnk  Nankina  Nankina
nnl  Northern Rengma Naga  Naga, Northern Rengma
nnm  Namia  Namia
nnn  Ngete  Ngete
nno  Norwegian Nynorsk  Norwegian Nynorsk
nnp  Wancho Naga  Naga, Wancho
nnq  Ngindo  Ngindo
nnr  Narungga  Narungga
nns  Ningye  Ningye
nnt  Nanticoke  Nanticoke
nnu  Dwang  Dwang
nnv  Nugunu (Australia)  Nugunu (Australia)
nnw  Southern Nuni  Nuni, Southern
nnx  Ngong  Ngong
nny  Nyangga  Nyangga
nnz  Nda'nda'  Nda'nda'
noa  Woun Meu  Woun Meu
nob  Norwegian Bokmål  Norwegian Bokmål
noc  Nuk  Nuk
nod  Northern Thai  Thai, Northern
noe  Nimadi  Nimadi
nof  Nomane  Nomane
nog  Nogai  Nogai
noh  Nomu  Nomu
noi  Noiri  Noiri
noj  Nonuya  Nonuya
nok  Nooksack  Nooksack
nol  Nomlaki  Nomlaki
nom  Nocamán  Nocamán
non  Old Norse  Norse, Old
nop  Numanggang  Numanggang
noq  Ngongo  Ngongo
nor  Norwegian  Norwegian
nos  Eastern Nisu  Nisu, Eastern
not  Nomatsiguenga  Nomatsiguenga
nou  Ewage-Notu  Ewage-Notu
nov  Novial  Novial
now  Nyambo  Nyambo
noy  Noy  Noy
noz  Nayi  Nayi
npa  Nar Phu  Nar Phu
npb  Nupbikha  Nupbikha
npg  Ponyo-Gongwang Naga  Naga, Ponyo-Gongwang
nph  Phom Naga  Naga, Phom
npi  Nepali (individual language)  Nepali (individual language)
npl  Southeastern Puebla Nahuatl  Nahuatl, Southeastern Puebla
npn  Mondropolon  Mondropolon
npo  Pochuri Naga  Naga, Pochuri
nps  Nipsan  Nipsan
npu  Puimei Naga  Naga, Puimei
npy  Napu  Napu
nqg  Southern Nago  Nago, Southern
nqk  Kura Ede Nago  Ede Nago, Kura
nqm  Ndom  Ndom
nqn  Nen  Nen
nqo  N'Ko  N'Ko
nqq  Kyan-Karyaw Naga  Naga, Kyan-Karyaw
nqy  Akyaung Ari Naga  Naga, Akyaung Ari
nra  Ngom  Ngom
nrb  Nara  Nara
nrc  Noric  Noric
nre  Southern Rengma Naga  Naga, Southern Rengma
nrg  Narango  Narango
nri  Chokri Naga  Naga, Chokri
nrk  Ngarla  Ngarla
nrl  Ngarluma  Ngarluma
nrm  Narom  Narom
nrn  Norn  Norn
nrp  North Picene  Picene, North
nrr  Nora  Nora
nrr  Norra  Norra
nrt  Northern Kalapuya  Kalapuya, Northern
nru  Narua  Narua
nrx  Ngurmbur  Ngurmbur
nrz  Lala  Lala
nsa  Sangtam Naga  Naga, Sangtam
nsc  Nshi  Nshi
nsd  Southern Nisu  Nisu, Southern
nse  Nsenga  Nsenga
nsf  Northwestern Nisu  Nisu, Northwestern
nsg  Ngasa  Ngasa
nsh  Ngoshie  Ngoshie
nsi  Nigerian Sign Language  Nigerian Sign Language
nsk  Naskapi  Naskapi
nsl  Norwegian Sign Language  Norwegian Sign Language
nsm  Sumi Naga  Naga, Sumi
nsn  Nehan  Nehan
nso  Northern Sotho  Sotho, Northern
nso  Pedi  Pedi
nso  Sepedi  Sepedi
nsp  Nepalese Sign Language  Nepalese Sign Language
nsq  Northern Sierra Miwok  Miwok, Northern Sierra
nsr  Maritime Sign Language  Maritime Sign Language
nss  Nali  Nali
nst  Tase Naga  Naga, Tase
nsu  Sierra Negra Nahuatl  Nahuatl, Sierra Negra
nsv  Southwestern Nisu  Nisu, Southwestern
nsw  Navut  Navut
nsx  Nsongo  Nsongo
nsy  Nasal  Nasal
nsz  Nisenan  Nisenan
nte  Nathembo  Nathembo
ntg  Ngantangarra  Ngantangarra
nti  Natioro  Natioro
ntj  Ngaanyatjarra  Ngaanyatjarra
ntk  Ikoma-Nata-Isenye  Ikoma-Nata-Isenye
ntm  Nateni  Nateni
nto  Ntomba  Ntomba
ntp  Northern Tepehuan  Tepehuan, Northern
ntr  Delo  Delo
nts  Natagaimas  Natagaimas
ntu  Natügu  Natügu
ntw  Nottoway  Nottoway
ntx  Tangkhul Naga (Myanmar)  Naga, Tangkhul (Myanmar)
nty  Mantsi  Mantsi
ntz  Natanzi  Natanzi
nua  Yuanga  Yuanga
nuc  Nukuini  Nukuini
nud  Ngala  Ngala
nue  Ngundu  Ngundu
nuf  Nusu  Nusu
nug  Nungali  Nungali
nuh  Ndunda  Ndunda
nui  Ngumbi  Ngumbi
nuj  Nyole  Nyole
nuk  Nuuchahnulth  Nuuchahnulth
nuk  Nuu-chah-nulth  Nuu-chah-nulth
nul  Nusa Laut  Nusa Laut
num  Niuafo'ou  Niuafo'ou
nun  Anong  Anong
nuo  Nguôn  Nguôn
nup  Nupe-Nupe-Tako  Nupe-Nupe-Tako
nuq  Nukumanu  Nukumanu
nur  Nukuria  Nukuria
nus  Nuer  Nuer
nut  Nung (Viet Nam)  Nung (Viet Nam)
nuu  Ngbundu  Ngbundu
nuv  Northern Nuni  Nuni, Northern
nuw  Nguluwan  Nguluwan
nux  Mehek  Mehek
nuy  Nunggubuyu  Nunggubuyu
nuz  Tlamacazapa Nahuatl  Nahuatl, Tlamacazapa
nvh  Nasarian  Nasarian
nvm  Namiae  Namiae
nvo  Nyokon  Nyokon
nwa  Nawathinehena  Nawathinehena
nwb  Nyabwa  Nyabwa
nwc  Classical Nepal Bhasa  Nepal Bhasa, Classical
nwc  Classical Newari  Newari, Classical
nwc  Old Newari  Newari, Old
nwe  Ngwe  Ngwe
nwg  Ngayawung  Ngayawung
nwi  Southwest Tanna  Tanna, Southwest
nwm  Nyamusa-Molo  Nyamusa-Molo
nwo  Nauo  Nauo
nwr  Nawaru  Nawaru
nwx  Middle Newar  Newar, Middle
nwy  Nottoway-Meherrin  Nottoway-Meherrin
nxa  Nauete  Nauete
nxd  Ngando (Democratic Republic of Congo)  Ngando (Democratic Republic of Congo)
nxe  Nage  Nage
nxg  Ngad'a  Ngad'a
nxi  Nindi  Nindi
nxk  Koki Naga  Naga, Koki
nxl  South Nuaulu  Nuaulu, South
nxm  Numidian  Numidian
nxn  Ngawun  Ngawun
nxq  Naxi  Naxi
nxr  Ninggerum  Ninggerum
nxu  Narau  Narau
nxx  Nafri  Nafri
nya  Chewa  Chewa
nya  Chichewa  Chichewa
nya  Nyanja  Nyanja
nyb  Nyangbo  Nyangbo
nyc  Nyanga-li  Nyanga-li
nyd  Nyore  Nyore
nyd  Olunyole  Olunyole
nye  Nyengo  Nyengo
nyf  Giryama  Giryama
nyf  Kigiryama  Kigiryama
nyg  Nyindu  Nyindu
nyh  Nyigina  Nyigina
nyi  Ama (Sudan)  Ama (Sudan)
nyj  Nyanga  Nyanga
nyk  Nyaneka  Nyaneka
nyl  Nyeu  Nyeu
nym  Nyamwezi  Nyamwezi
nyn  Nyankole  Nyankole
nyo  Nyoro  Nyoro
nyp  Nyang'i  Nyang'i
nyq  Nayini  Nayini
nyr  Nyiha (Malawi)  Nyiha (Malawi)
nys  Nyunga  Nyunga
nyt  Nyawaygi  Nyawaygi
nyu  Nyungwe  Nyungwe
nyv  Nyulnyul  Nyulnyul
nyw  Nyaw  Nyaw
nyx  Nganyaywana  Nganyaywana
nyy  Nyakyusa-Ngonde  Nyakyusa-Ngonde
nza  Tigon Mbembe  Mbembe, Tigon
nzb  Njebi  Njebi
nzi  Nzima  Nzima
nzk  Nzakara  Nzakara
nzm  Zeme Naga  Naga, Zeme
nzs  New Zealand Sign Language  New Zealand Sign Language
nzu  Teke-Nzikou  Teke-Nzikou
nzy  Nzakambay  Nzakambay
nzz  Nanga Dama Dogon  Dogon, Nanga Dama
oaa  Orok  Orok
oac  Oroch  Oroch
oar  Ancient Aramaic (up to 700 BCE)  Aramaic, Ancient (up to 700 BCE)
oar  Old Aramaic (up to 700 BCE)  Aramaic, Old (up to 700 BCE)
oav  Old Avar  Avar, Old
obi  Obispeño  Obispeño
obk  Southern Bontok  Bontok, Southern
obl  Oblo  Oblo
obm  Moabite  Moabite
obo  Obo Manobo  Manobo, Obo
obr  Old Burmese  Burmese, Old
obt  Old Breton  Breton, Old
obu  Obulom  Obulom
oca  Ocaina  Ocaina
och  Old Chinese  Chinese, Old
oci  Occitan (post 1500)  Occitan (post 1500)
oco  Old Cornish  Cornish, Old
ocu  Atzingo Matlatzinca  Matlatzinca, Atzingo
oda  Odut  Odut
odk  Od  Od
odt  Old Dutch  Dutch, Old
odu  Odual  Odual
ofo  Ofo  Ofo
ofs  Old Frisian  Frisian, Old
ofu  Efutop  Efutop
ogb  Ogbia  Ogbia
ogc  Ogbah  Ogbah
oge  Old Georgian  Georgian, Old
ogg  Ogbogolo  Ogbogolo
ogo  Khana  Khana
ogu  Ogbronuagum  Ogbronuagum
oht  Old Hittite  Hittite, Old
ohu  Old Hungarian  Hungarian, Old
oia  Oirata  Oirata
oin  Inebu One  One, Inebu
ojb  Northwestern Ojibwa  Ojibwa, Northwestern
ojc  Central Ojibwa  Ojibwa, Central
ojg  Eastern Ojibwa  Ojibwa, Eastern
oji  Ojibwa  Ojibwa
ojp  Old Japanese  Japanese, Old
ojs  Severn Ojibwa  Ojibwa, Severn
ojv  Ontong Java  Ontong Java
ojw  Western Ojibwa  Ojibwa, Western
oka  Okanagan  Okanagan
okb  Okobo  Okobo
okd  Okodia  Okodia
oke  Okpe (Southwestern Edo)  Okpe (Southwestern Edo)
okg  Koko Babangk  Koko Babangk
okh  Koresh-e Rostam  Koresh-e Rostam
oki  Okiek  Okiek
okj  Oko-Juwoi  Oko-Juwoi
okk  Kwamtim One  One, Kwamtim
okl  Old Kentish Sign Language  Kentish Sign Language, Old
okm  Middle Korean (10th-16th cent.)  Korean, Middle (10th-16th cent.)
okn  Oki-No-Erabu  Oki-No-Erabu
oko  Old Korean (3rd-9th cent.)  Korean, Old (3rd-9th cent.)
okr  Kirike  Kirike
oks  Oko-Eni-Osayen  Oko-Eni-Osayen
oku  Oku  Oku
okv  Orokaiva  Orokaiva
okx  Okpe (Northwestern Edo)  Okpe (Northwestern Edo)
ola  Walungge  Walungge
old  Mochi  Mochi
ole  Olekha  Olekha
olk  Olkol  Olkol
olm  Oloma  Oloma
olo  Livvi  Livvi
olr  Olrat  Olrat
oma  Omaha-Ponca  Omaha-Ponca
omb  East Ambae  Ambae, East
omc  Mochica  Mochica
ome  Omejes  Omejes
omg  Omagua  Omagua
omi  Omi  Omi
omk  Omok  Omok
oml  Ombo  Ombo
omn  Minoan  Minoan
omo  Utarmbung  Utarmbung
omp  Old Manipuri  Manipuri, Old
omr  Old Marathi  Marathi, Old
omt  Omotik  Omotik
omu  Omurano  Omurano
omw  South Tairora  Tairora, South
omx  Old Mon  Mon, Old
ona  Ona  Ona
onb  Lingao  Lingao
one  Oneida  Oneida
ong  Olo  Olo
oni  Onin  Onin
onj  Onjob  Onjob
onk  Kabore One  One, Kabore
onn  Onobasulu  Onobasulu
ono  Onondaga  Onondaga
onp  Sartang  Sartang
onr  Northern One  One, Northern
ons  Ono  Ono
ont  Ontenu  Ontenu
onu  Unua  Unua
onw  Old Nubian  Nubian, Old
onx  Onin Based Pidgin  Onin Based Pidgin
ood  Tohono O'odham  Tohono O'odham
oog  Ong  Ong
oon  Önge  Önge
oor  Oorlams  Oorlams
oos  Old Ossetic  Ossetic, Old
opa  Okpamheri  Okpamheri
opk  Kopkaka  Kopkaka
opm  Oksapmin  Oksapmin
opo  Opao  Opao
opt  Opata  Opata
opy  Ofayé  Ofayé
ora  Oroha  Oroha
orc  Orma  Orma
ore  Orejón  Orejón
org  Oring  Oring
orh  Oroqen  Oroqen
ori  Oriya (macrolanguage)  Oriya (macrolanguage)
orm  Oromo  Oromo
orn  Orang Kanaq  Orang Kanaq
oro  Orokolo  Orokolo
orr  Oruma  Oruma
ors  Orang Seletar  Orang Seletar
ort  Adivasi Oriya  Oriya, Adivasi
oru  Ormuri  Ormuri
orv  Old Russian  Russian, Old
orw  Oro Win  Oro Win
orx  Oro  Oro
ory  Oriya (individual language)  Oriya (individual language)
orz  Ormu  Ormu
osa  Osage  Osage
osc  Oscan  Oscan
osi  Osing  Osing
oso  Ososo  Ososo
osp  Old Spanish  Spanish, Old
oss  Ossetian  Ossetian
oss  Ossetic  Ossetic
ost  Osatu  Osatu
osu  Southern One  One, Southern
osx  Old Saxon  Saxon, Old
ota  Ottoman Turkish (1500-1928)  Turkish, Ottoman (1500-1928)
otb  Old Tibetan  Tibetan, Old
otd  Ot Danum  Ot Danum
ote  Mezquital Otomi  Otomi, Mezquital
oti  Oti  Oti
otk  Old Turkish  Turkish, Old
otl  Tilapa Otomi  Otomi, Tilapa
otm  Eastern Highland Otomi  Otomi, Eastern Highland
otn  Tenango Otomi  Otomi, Tenango
otq  Querétaro Otomi  Otomi, Querétaro
otr  Otoro  Otoro
ots  Estado de México Otomi  Otomi, Estado de México
ott  Temoaya Otomi  Otomi, Temoaya
otu  Otuke  Otuke
otw  Ottawa  Ottawa
otx  Texcatepec Otomi  Otomi, Texcatepec
oty  Old Tamil  Tamil, Old
otz  Ixtenco Otomi  Otomi, Ixtenco
oua  Tagargrent  Tagargrent
oub  Glio-Oubi  Glio-Oubi
oue  Oune  Oune
oui  Old Uighur  Uighur, Old
oum  Ouma  Ouma
oun  !O!ung  !O!ung
owi  Owiniga  Owiniga
owl  Old Welsh  Welsh, Old
oyb  Oy  Oy
oyd  Oyda  Oyda
oym  Wayampi  Wayampi
oyy  Oya'oya  Oya'oya
ozm  Koonzime  Koonzime
pab  Parecís  Parecís
pac  Pacoh  Pacoh
pad  Paumarí  Paumarí
pae  Pagibete  Pagibete
paf  Paranawát  Paranawát
pag  Pangasinan  Pangasinan
pah  Tenharim  Tenharim
pai  Pe  Pe
pak  Parakanã  Parakanã
pal  Pahlavi  Pahlavi
pam  Kapampangan  Kapampangan
pam  Pampanga  Pampanga
pan  Panjabi  Panjabi
pan  Punjabi  Punjabi
pao  Northern Paiute  Paiute, Northern
pap  Papiamento  Papiamento
paq  Parya  Parya
par  Panamint  Panamint
par  Timbisha  Timbisha
pas  Papasena  Papasena
pat  Papitalai  Papitalai
pau  Palauan  Palauan
pav  Pakaásnovos  Pakaásnovos
paw  Pawnee  Pawnee
pax  Pankararé  Pankararé
pay  Pech  Pech
paz  Pankararú  Pankararú
pbb  Páez  Páez
pbc  Patamona  Patamona
pbe  Mezontla Popoloca  Popoloca, Mezontla
pbf  Coyotepec Popoloca  Popoloca, Coyotepec
pbg  Paraujano  Paraujano
pbh  E'ñapa Woromaipu  E'ñapa Woromaipu
pbi  Parkwa  Parkwa
pbl  Mak (Nigeria)  Mak (Nigeria)
pbn  Kpasam  Kpasam
pbo  Papel  Papel
pbp  Badyara  Badyara
pbr  Pangwa  Pangwa
pbs  Central Pame  Pame, Central
pbt  Southern Pashto  Pashto, Southern
pbu  Northern Pashto  Pashto, Northern
pbv  Pnar  Pnar
pby  Pyu  Pyu
pca  Santa Inés Ahuatempan Popoloca  Popoloca, Santa Inés Ahuatempan
pcb  Pear  Pear
pcc  Bouyei  Bouyei
pcd  Picard  Picard
pce  Ruching Palaung  Palaung, Ruching
pcf  Paliyan  Paliyan
pcg  Paniya  Paniya
pch  Pardhan  Pardhan
pci  Duruwa  Duruwa
pcj  Parenga  Parenga
pck  Paite Chin  Chin, Paite
pcl  Pardhi  Pardhi
pcm  Nigerian Pidgin  Pidgin, Nigerian
pcn  Piti  Piti
pcp  Pacahuara  Pacahuara
pcw  Pyapun  Pyapun
pda  Anam  Anam
pdc  Pennsylvania German  German, Pennsylvania
pdi  Pa Di  Pa Di
pdn  Fedan  Fedan
pdn  Podena  Podena
pdo  Padoe  Padoe
pdt  Plautdietsch  Plautdietsch
pdu  Kayan  Kayan
pea  Peranakan Indonesian  Indonesian, Peranakan
peb  Eastern Pomo  Pomo, Eastern
ped  Mala (Papua New Guinea)  Mala (Papua New Guinea)
pee  Taje  Taje
pef  Northeastern Pomo  Pomo, Northeastern
peg  Pengo  Pengo
peh  Bonan  Bonan
pei  Chichimeca-Jonaz  Chichimeca-Jonaz
pej  Northern Pomo  Pomo, Northern
pek  Penchal  Penchal
pel  Pekal  Pekal
pem  Phende  Phende
peo  Old Persian (ca. 600-400 B.C.)  Persian, Old (ca. 600-400 B.C.)
pep  Kunja  Kunja
peq  Southern Pomo  Pomo, Southern
pes  Iranian Persian  Persian, Iranian
pev  Pémono  Pémono
pex  Petats  Petats
pey  Petjo  Petjo
pez  Eastern Penan  Penan, Eastern
pfa  Pááfang  Pááfang
pfe  Peere  Peere
pfl  Pfaelzisch  Pfaelzisch
pga  Sudanese Creole Arabic  Creole Arabic, Sudanese
pgg  Pangwali  Pangwali
pgi  Pagi  Pagi
pgk  Rerep  Rerep
pgl  Primitive Irish  Irish, Primitive
pgn  Paelignian  Paelignian
pgs  Pangseng  Pangseng
pgu  Pagu  Pagu
pha  Pa-Hng  Pa-Hng
phd  Phudagi  Phudagi
phg  Phuong  Phuong
phh  Phukha  Phukha
phk  Phake  Phake
phl  Palula  Palula
phl  Phalura  Phalura
phm  Phimbi  Phimbi
phn  Phoenician  Phoenician
pho  Phunoi  Phunoi
phq  Phana'  Phana'
phr  Pahari-Potwari  Pahari-Potwari
pht  Phu Thai  Phu Thai
phu  Phuan  Phuan
phv  Pahlavani  Pahlavani
phw  Phangduwali  Phangduwali
pia  Pima Bajo  Pima Bajo
pib  Yine  Yine
pic  Pinji  Pinji
pid  Piaroa  Piaroa
pie  Piro  Piro
pif  Pingelapese  Pingelapese
pig  Pisabo  Pisabo
pih  Pitcairn-Norfolk  Pitcairn-Norfolk
pii  Pini  Pini
pij  Pijao  Pijao
pil  Yom  Yom
pim  Powhatan  Powhatan
pin  Piame  Piame
pio  Piapoco  Piapoco
pip  Pero  Pero
pir  Piratapuyo  Piratapuyo
pis  Pijin  Pijin
pit  Pitta Pitta  Pitta Pitta
piu  Pintupi-Luritja  Pintupi-Luritja
piv  Pileni  Pileni
piv  Vaeakau-Taumako  Vaeakau-Taumako
piw  Pimbwe  Pimbwe
pix  Piu  Piu
piy  Piya-Kwonci  Piya-Kwonci
piz  Pije  Pije
pjt  Pitjantjatjara  Pitjantjatjara
pka  Ardhamāgadhī Prākrit  Prākrit, Ardhamāgadhī
pkb  Kipfokomo  Kipfokomo
pkb  Pokomo  Pokomo
pkc  Paekche  Paekche
pkg  Pak-Tong  Pak-Tong
pkh  Pankhu  Pankhu
pkn  Pakanha  Pakanha
pko  Pökoot  Pökoot
pkp  Pukapuka  Pukapuka
pkr  Attapady Kurumba  Kurumba, Attapady
pks  Pakistan Sign Language  Pakistan Sign Language
pkt  Maleng  Maleng
pku  Paku  Paku
pla  Miani  Miani
plb  Polonombauk  Polonombauk
plc  Central Palawano  Palawano, Central
pld  Polari  Polari
ple  Palu'e  Palu'e
plg  Pilagá  Pilagá
plh  Paulohi  Paulohi
pli  Pali  Pali
plj  Polci  Polci
plk  Kohistani Shina  Shina, Kohistani
pll  Shwe Palaung  Palaung, Shwe
pln  Palenquero  Palenquero
plo  Oluta Popoluca  Popoluca, Oluta
plp  Palpa  Palpa
plq  Palaic  Palaic
plr  Palaka Senoufo  Senoufo, Palaka
pls  San Marcos Tlalcoyalco Popoloca  Popoloca, San Marcos Tlalcoyalco
plt  Plateau Malagasy  Malagasy, Plateau
plu  Palikúr  Palikúr
plv  Southwest Palawano  Palawano, Southwest
plw  Brooke's Point Palawano  Palawano, Brooke's Point
ply  Bolyu  Bolyu
plz  Paluan  Paluan
pma  Paama  Paama
pmb  Pambia  Pambia
pmc  Palumata  Palumata
pmd  Pallanganmiddang  Pallanganmiddang
pme  Pwaamei  Pwaamei
pmf  Pamona  Pamona
pmh  Māhārāṣṭri Prākrit  Prākrit, Māhārāṣṭri
pmi  Northern Pumi  Pumi, Northern
pmj  Southern Pumi  Pumi, Southern
pmk  Pamlico  Pamlico
pml  Lingua Franca  Lingua Franca
pmm  Pomo  Pomo
pmn  Pam  Pam
pmo  Pom  Pom
pmq  Northern Pame  Pame, Northern
pmr  Paynamar  Paynamar
pms  Piemontese  Piemontese
pmt  Tuamotuan  Tuamotuan
pmu  Mirpur Panjabi  Panjabi, Mirpur
pmw  Plains Miwok  Miwok, Plains
pmx  Poumei Naga  Naga, Poumei
pmy  Papuan Malay  Malay, Papuan
pmz  Southern Pame  Pame, Southern
pna  Punan Bah-Biau  Punan Bah-Biau
pnb  Western Panjabi  Panjabi, Western
pnc  Pannei  Pannei
pne  Western Penan  Penan, Western
png  Pongu  Pongu
pnh  Penrhyn  Penrhyn
pni  Aoheng  Aoheng
pnj  Pinjarup  Pinjarup
pnk  Paunaka  Paunaka
pnl  Paleni  Paleni
pnm  Punan Batu 1  Punan Batu 1
pnn  Pinai-Hagahai  Pinai-Hagahai
pno  Panobo  Panobo
pnp  Pancana  Pancana
pnq  Pana (Burkina Faso)  Pana (Burkina Faso)
pnr  Panim  Panim
pns  Ponosakan  Ponosakan
pnt  Pontic  Pontic
pnu  Jiongnai Bunu  Bunu, Jiongnai
pnv  Pinigura  Pinigura
pnw  Panytyima  Panytyima
pnx  Phong-Kniang  Phong-Kniang
pny  Pinyin  Pinyin
pnz  Pana (Central African Republic)  Pana (Central African Republic)
poc  Poqomam  Poqomam
pod  Ponares  Ponares
poe  San Juan Atzingo Popoloca  Popoloca, San Juan Atzingo
pof  Poke  Poke
pog  Potiguára  Potiguára
poh  Poqomchi'  Poqomchi'
poi  Highland Popoluca  Popoluca, Highland
pok  Pokangá  Pokangá
pol  Polish  Polish
pom  Southeastern Pomo  Pomo, Southeastern
pon  Pohnpeian  Pohnpeian
poo  Central Pomo  Pomo, Central
pop  Pwapwâ  Pwapwâ
poq  Texistepec Popoluca  Popoluca, Texistepec
por  Portuguese  Portuguese
pos  Sayula Popoluca  Popoluca, Sayula
pot  Potawatomi  Potawatomi
pov  Upper Guinea Crioulo  Crioulo, Upper Guinea
pow  San Felipe Otlaltepec Popoloca  Popoloca, San Felipe Otlaltepec
pox  Polabian  Polabian
poy  Pogolo  Pogolo
ppa  Pao  Pao
ppe  Papi  Papi
ppi  Paipai  Paipai
ppk  Uma  Uma
ppl  Nicarao  Nicarao
ppl  Pipil  Pipil
ppm  Papuma  Papuma
ppn  Papapana  Papapana
ppo  Folopa  Folopa
ppp  Pelende  Pelende
ppq  Pei  Pei
pps  San Luís Temalacayuca Popoloca  Popoloca, San Luís Temalacayuca
ppt  Pare  Pare
ppu  Papora  Papora
pqa  Pa'a  Pa'a
pqm  Malecite-Passamaquoddy  Malecite-Passamaquoddy
prb  Lua'  Lua'
prc  Parachi  Parachi
prd  Parsi-Dari  Parsi-Dari
pre  Principense  Principense
prf  Paranan  Paranan
prg  Prussian  Prussian
prh  Porohanon  Porohanon
pri  Paicî  Paicî
prk  Parauk  Parauk
prl  Peruvian Sign Language  Peruvian Sign Language
prm  Kibiri  Kibiri
prn  Prasuni  Prasuni
pro  Old Occitan (to 1500)  Occitan, Old (to 1500)
pro  Old Provençal (to 1500)  Provençal, Old (to 1500)
prp  Parsi  Parsi
prq  Ashéninka Perené  Ashéninka Perené
prr  Puri  Puri
prs  Afghan Persian  Persian, Afghan
prs  Dari  Dari
prt  Phai  Phai
pru  Puragi  Puragi
prw  Parawen  Parawen
prx  Purik  Purik
pry  Pray 3  Pray 3
prz  Providencia Sign Language  Providencia Sign Language
psa  Asue Awyu  Awyu, Asue
psc  Persian Sign Language  Persian Sign Language
psd  Plains Indian Sign Language  Plains Indian Sign Language
pse  Central Malay  Malay, Central
psg  Penang Sign Language  Penang Sign Language
psh  Southwest Pashayi  Pashayi, Southwest
psi  Southeast Pashayi  Pashayi, Southeast
psl  Puerto Rican Sign Language  Puerto Rican Sign Language
psm  Pauserna  Pauserna
psn  Panasuan  Panasuan
pso  Polish Sign Language  Polish Sign Language
psp  Philippine Sign Language  Philippine Sign Language
psq  Pasi  Pasi
psr  Portuguese Sign Language  Portuguese Sign Language
pss  Kaulong  Kaulong
pst  Central Pashto  Pashto, Central
psu  Sauraseni Prākrit  Prākrit, Sauraseni
psw  Port Sandwich  Port Sandwich
psy  Piscataway  Piscataway
pta  Pai Tavytera  Pai Tavytera
pth  Pataxó Hã-Ha-Hãe  Pataxó Hã-Ha-Hãe
pti  Pintiini  Pintiini
ptn  Patani  Patani
pto  Zo'é  Zo'é
ptp  Patep  Patep
ptr  Piamatsina  Piamatsina
ptt  Enrekang  Enrekang
ptu  Bambam  Bambam
ptv  Port Vato  Port Vato
ptw  Pentlatch  Pentlatch
pty  Pathiya  Pathiya
pua  Western Highland Purepecha  Purepecha, Western Highland
pub  Purum  Purum
puc  Punan Merap  Punan Merap
pud  Punan Aput  Punan Aput
pue  Puelche  Puelche
puf  Punan Merah  Punan Merah
pug  Phuie  Phuie
pui  Puinave  Puinave
puj  Punan Tubu  Punan Tubu
puk  Pu Ko  Pu Ko
pum  Puma  Puma
puo  Puoc  Puoc
pup  Pulabu  Pulabu
puq  Puquina  Puquina
pur  Puruborá  Puruborá
pus  Pashto  Pashto
pus  Pushto  Pushto
put  Putoh  Putoh
puu  Punu  Punu
puw  Puluwatese  Puluwatese
pux  Puare  Puare
puy  Purisimeño  Purisimeño
puz  Purum Naga  Naga, Purum
pwa  Pawaia  Pawaia
pwb  Panawa  Panawa
pwg  Gapapaiwa  Gapapaiwa
pwi  Patwin  Patwin
pwm  Molbog  Molbog
pwn  Paiwan  Paiwan
pwo  Pwo Western Karen  Karen, Pwo Western
pwr  Powari  Powari
pww  Pwo Northern Karen  Karen, Pwo Northern
pxm  Quetzaltepec Mixe  Mixe, Quetzaltepec
pye  Pye Krumen  Krumen, Pye
pym  Fyam  Fyam
pyn  Poyanáwa  Poyanáwa
pys  Lengua de Señas del Paraguay  Lengua de Señas del Paraguay
pys  Paraguayan Sign Language  Paraguayan Sign Language
pyu  Puyuma  Puyuma
pyx  Pyu (Myanmar)  Pyu (Myanmar)
pyy  Pyen  Pyen
pzn  Para Naga  Naga, Para
qua  Quapaw  Quapaw
qub  Huallaga Huánuco Quechua  Quechua, Huallaga Huánuco
quc  K'iche'  K'iche'
quc  Quiché  Quiché
qud  Calderón Highland Quichua  Quichua, Calderón Highland
que  Quechua  Quechua
quf  Lambayeque Quechua  Quechua, Lambayeque
qug  Chimborazo Highland Quichua  Quichua, Chimborazo Highland
quh  South Bolivian Quechua  Quechua, South Bolivian
qui  Quileute  Quileute
quk  Chachapoyas Quechua  Quechua, Chachapoyas
qul  North Bolivian Quechua  Quechua, North Bolivian
qum  Sipacapense  Sipacapense
qun  Quinault  Quinault
qup  Southern Pastaza Quechua  Quechua, Southern Pastaza
quq  Quinqui  Quinqui
qur  Yanahuanca Pasco Quechua  Quechua, Yanahuanca Pasco
qus  Santiago del Estero Quichua  Quichua, Santiago del Estero
quv  Sacapulteco  Sacapulteco
quw  Tena Lowland Quichua  Quichua, Tena Lowland
qux  Yauyos Quechua  Quechua, Yauyos
quy  Ayacucho Quechua  Quechua, Ayacucho
quz  Cusco Quechua  Quechua, Cusco
qva  Ambo-Pasco Quechua  Quechua, Ambo-Pasco
qvc  Cajamarca Quechua  Quechua, Cajamarca
qve  Eastern Apurímac Quechua  Quechua, Eastern Apurímac
qvh  Huamalíes-Dos de Mayo Huánuco Quechua  Quechua, Huamalíes-Dos de Mayo Huánuco
qvi  Imbabura Highland Quichua  Quichua, Imbabura Highland
qvj  Loja Highland Quichua  Quichua, Loja Highland
qvl  Cajatambo North Lima Quechua  Quechua, Cajatambo North Lima
qvm  Margos-Yarowilca-Lauricocha Quechua  Quechua, Margos-Yarowilca-Lauricocha
qvn  North Junín Quechua  Quechua, North Junín
qvo  Napo Lowland Quechua  Quechua, Napo Lowland
qvp  Pacaraos Quechua  Quechua, Pacaraos
qvs  San Martín Quechua  Quechua, San Martín
qvw  Huaylla Wanca Quechua  Quechua, Huaylla Wanca
qvy  Queyu  Queyu
qvz  Northern Pastaza Quichua  Quichua, Northern Pastaza
qwa  Corongo Ancash Quechua  Quechua, Corongo Ancash
qwc  Classical Quechua  Quechua, Classical
qwh  Huaylas Ancash Quechua  Quechua, Huaylas Ancash
qwm  Kuman (Russia)  Kuman (Russia)
qws  Sihuas Ancash Quechua  Quechua, Sihuas Ancash
qwt  Kwalhioqua-Tlatskanai  Kwalhioqua-Tlatskanai
qxa  Chiquián Ancash Quechua  Quechua, Chiquián Ancash
qxc  Chincha Quechua  Quechua, Chincha
qxh  Panao Huánuco Quechua  Quechua, Panao Huánuco
qxl  Salasaca Highland Quichua  Quichua, Salasaca Highland
qxn  Northern Conchucos Ancash Quechua  Quechua, Northern Conchucos Ancash
qxo  Southern Conchucos Ancash Quechua  Quechua, Southern Conchucos Ancash
qxp  Puno Quechua  Quechua, Puno
qxq  Qashqa'i  Qashqa'i
qxr  Cañar Highland Quichua  Quichua, Cañar Highland
qxs  Southern Qiang  Qiang, Southern
qxt  Santa Ana de Tusi Pasco Quechua  Quechua, Santa Ana de Tusi Pasco
qxu  Arequipa-La Unión Quechua  Quechua, Arequipa-La Unión
qxw  Jauja Wanca Quechua  Quechua, Jauja Wanca
qya  Quenya  Quenya
qyp  Quiripi  Quiripi
raa  Dungmali  Dungmali
rab  Camling  Camling
rac  Rasawa  Rasawa
rad  Rade  Rade
raf  Western Meohang  Meohang, Western
rag  Logooli  Logooli
rag  Lulogooli  Lulogooli
rah  Rabha  Rabha
rai  Ramoaaina  Ramoaaina
raj  Rajasthani  Rajasthani
rak  Tulu-Bohuai  Tulu-Bohuai
ral  Ralte  Ralte
ram  Canela  Canela
ran  Riantana  Riantana
rao  Rao  Rao
rap  Rapanui  Rapanui
raq  Saam  Saam
rar  Cook Islands Maori  Maori, Cook Islands
rar  Rarotongan  Rarotongan
ras  Tegali  Tegali
rat  Razajerdi  Razajerdi
rau  Raute  Raute
rav  Sampang  Sampang
raw  Rawang  Rawang
rax  Rang  Rang
ray  Rapa  Rapa
raz  Rahambuu  Rahambuu
rbb  Rumai Palaung  Palaung, Rumai
rbk  Northern Bontok  Bontok, Northern
rbl  Miraya Bikol  Bikol, Miraya
rbp  Barababaraba  Barababaraba
rcf  Réunion Creole French  Creole French, Réunion
rdb  Rudbari  Rudbari
rea  Rerau  Rerau
reb  Rembong  Rembong
ree  Rejang Kayan  Kayan, Rejang
reg  Kara (Tanzania)  Kara (Tanzania)
rei  Reli  Reli
rej  Rejang  Rejang
rel  Rendille  Rendille
rem  Remo  Remo
ren  Rengao  Rengao
rer  Rer Bare  Rer Bare
res  Reshe  Reshe
ret  Retta  Retta
rey  Reyesano  Reyesano
rga  Roria  Roria
rge  Romano-Greek  Romano-Greek
rgk  Rangkas  Rangkas
rgn  Romagnol  Romagnol
rgr  Resígaro  Resígaro
rgs  Southern Roglai  Roglai, Southern
rgu  Ringgou  Ringgou
rhg  Rohingya  Rohingya
rhp  Yahang  Yahang
ria  Riang (India)  Riang (India)
rie  Rien  Rien
rif  Tarifit  Tarifit
ril  Riang (Myanmar)  Riang (Myanmar)
rim  Nyaturu  Nyaturu
rin  Nungu  Nungu
rir  Ribun  Ribun
rit  Ritarungo  Ritarungo
riu  Riung  Riung
rjg  Rajong  Rajong
rji  Raji  Raji
rjs  Rajbanshi  Rajbanshi
rka  Kraol  Kraol
rkb  Rikbaktsa  Rikbaktsa
rkh  Rakahanga-Manihiki  Rakahanga-Manihiki
rki  Rakhine  Rakhine
rkm  Marka  Marka
rkt  Kamta  Kamta
rkt  Rangpuri  Rangpuri
rkw  Arakwal  Arakwal
rma  Rama  Rama
rmb  Rembarunga  Rembarunga
rmc  Carpathian Romani  Romani, Carpathian
rmd  Traveller Danish  Danish, Traveller
rme  Angloromani  Angloromani
rmf  Kalo Finnish Romani  Romani, Kalo Finnish
rmg  Traveller Norwegian  Norwegian, Traveller
rmh  Murkim  Murkim
rmi  Lomavren  Lomavren
rmk  Romkun  Romkun
rml  Baltic Romani  Romani, Baltic
rmm  Roma  Roma
rmn  Balkan Romani  Romani, Balkan
rmo  Sinte Romani  Romani, Sinte
rmp  Rempi  Rempi
rmq  Caló  Caló
rms  Romanian Sign Language  Romanian Sign Language
rmt  Domari  Domari
rmu  Tavringer Romani  Romani, Tavringer
rmv  Romanova  Romanova
rmw  Welsh Romani  Romani, Welsh
rmx  Romam  Romam
rmy  Vlax Romani  Romani, Vlax
rmz  Marma  Marma
rna  Runa  Runa
rnd  Ruund  Ruund
rng  Ronga  Ronga
rnl  Ranglong  Ranglong
rnn  Roon  Roon
rnp  Rongpo  Rongpo
rnr  Nari Nari  Nari Nari
rnw  Rungwa  Rungwa
rob  Tae'  Tae'
roc  Cacgia Roglai  Roglai, Cacgia
rod  Rogo  Rogo
roe  Ronji  Ronji
rof  Rombo  Rombo
rog  Northern Roglai  Roglai, Northern
roh  Romansh  Romansh
rol  Romblomanon  Romblomanon
rom  Romany  Romany
ron  Moldavian  Moldavian
ron  Moldovan  Moldovan
ron  Romanian  Romanian
roo  Rotokas  Rotokas
rop  Kriol  Kriol
ror  Rongga  Rongga
rou  Runga  Runga
row  Dela-Oenale  Dela-Oenale
rpn  Repanbitip  Repanbitip
rpt  Rapting  Rapting
rri  Ririo  Ririo
rro  Waima  Waima
rrt  Arritinngithigh  Arritinngithigh
rsb  Romano-Serbian  Romano-Serbian
rsi  Rennellese Sign Language  Rennellese Sign Language
rsl  Russian Sign Language  Russian Sign Language
rtc  Rungtu Chin  Chin, Rungtu
rth  Ratahan  Ratahan
rtm  Rotuman  Rotuman
rtw  Rathawi  Rathawi
rub  Gungu  Gungu
ruc  Ruuli  Ruuli
rue  Rusyn  Rusyn
ruf  Luguru  Luguru
rug  Roviana  Roviana
ruh  Ruga  Ruga
rui  Rufiji  Rufiji
ruk  Che  Che
run  Rundi  Rundi
ruo  Istro Romanian  Romanian, Istro
rup  Aromanian  Aromanian
rup  Arumanian  Arumanian
rup  Macedo-Romanian  Romanian, Macedo-
ruq  Megleno Romanian  Romanian, Megleno
rus  Russian  Russian
rut  Rutul  Rutul
ruu  Lanas Lobu  Lobu, Lanas
ruy  Mala (Nigeria)  Mala (Nigeria)
ruz  Ruma  Ruma
rwa  Rawo  Rawo
rwk  Rwa  Rwa
rwm  Amba (Uganda)  Amba (Uganda)
rwo  Rawa  Rawa
rwr  Marwari (India)  Marwari (India)
rxd  Ngardi  Ngardi
rxw  Karuwali  Karuwali
ryn  Northern Amami-Oshima  Amami-Oshima, Northern
rys  Yaeyama  Yaeyama
ryu  Central Okinawan  Okinawan, Central
saa  Saba  Saba
sab  Buglere  Buglere
sac  Meskwaki  Meskwaki
sad  Sandawe  Sandawe
sae  Sabanê  Sabanê
saf  Safaliba  Safaliba
sag  Sango  Sango
sah  Yakut  Yakut
saj  Sahu  Sahu
sak  Sake  Sake
sam  Samaritan Aramaic  Aramaic, Samaritan
san  Sanskrit  Sanskrit
sao  Sause  Sause
sap  Sanapaná  Sanapaná
saq  Samburu  Samburu
sar  Saraveca  Saraveca
sas  Sasak  Sasak
sat  Santali  Santali
sau  Saleman  Saleman
sav  Saafi-Saafi  Saafi-Saafi
saw  Sawi  Sawi
sax  Sa  Sa
say  Saya  Saya
saz  Saurashtra  Saurashtra
sba  Ngambay  Ngambay
sbb  Simbo  Simbo
sbc  Kele (Papua New Guinea)  Kele (Papua New Guinea)
sbd  Southern Samo  Samo, Southern
sbe  Saliba  Saliba
sbf  Shabo  Shabo
sbg  Seget  Seget
sbh  Sori-Harengan  Sori-Harengan
sbi  Seti  Seti
sbj  Surbakhal  Surbakhal
sbk  Safwa  Safwa
sbl  Botolan Sambal  Sambal, Botolan
sbm  Sagala  Sagala
sbn  Sindhi Bhil  Bhil, Sindhi
sbo  Sabüm  Sabüm
sbp  Sangu (Tanzania)  Sangu (Tanzania)
sbq  Sileibi  Sileibi
sbr  Sembakung Murut  Sembakung Murut
sbs  Subiya  Subiya
sbt  Kimki  Kimki
sbu  Stod Bhoti  Bhoti, Stod
sbv  Sabine  Sabine
sbw  Simba  Simba
sbx  Seberuang  Seberuang
sby  Soli  Soli
sbz  Sara Kaba  Sara Kaba
scb  Chut  Chut
sce  Dongxiang  Dongxiang
scf  San Miguel Creole French  Creole French, San Miguel
scg  Sanggau  Sanggau
sch  Sakachep  Sakachep
sci  Sri Lankan Creole Malay  Creole Malay, Sri Lankan
sck  Sadri  Sadri
scl  Shina  Shina
scn  Sicilian  Sicilian
sco  Scots  Scots
scp  Helambu Sherpa  Helambu Sherpa
scq  Sa'och  Sa'och
scs  North Slavey  Slavey, North
scu  Shumcho  Shumcho
scv  Sheni  Sheni
scw  Sha  Sha
scx  Sicel  Sicel
sda  Toraja-Sa'dan  Toraja-Sa'dan
sdb  Shabak  Shabak
sdc  Sassarese Sardinian  Sardinian, Sassarese
sde  Surubu  Surubu
sdf  Sarli  Sarli
sdg  Savi  Savi
sdh  Southern Kurdish  Kurdish, Southern
sdj  Suundi  Suundi
sdk  Sos Kundi  Sos Kundi
sdl  Saudi Arabian Sign Language  Saudi Arabian Sign Language
sdm  Semandang  Semandang
sdn  Gallurese Sardinian  Sardinian, Gallurese
sdo  Bukar-Sadung Bidayuh  Bidayuh, Bukar-Sadung
sdp  Sherdukpen  Sherdukpen
sdr  Oraon Sadri  Sadri, Oraon
sds  Sened  Sened
sdt  Shuadit  Shuadit
sdu  Sarudu  Sarudu
sdx  Sibu Melanau  Melanau, Sibu
sdz  Sallands  Sallands
sea  Semai  Semai
seb  Shempire Senoufo  Senoufo, Shempire
sec  Sechelt  Sechelt
sed  Sedang  Sedang
see  Seneca  Seneca
sef  Cebaara Senoufo  Senoufo, Cebaara
seg  Segeju  Segeju
seh  Sena  Sena
sei  Seri  Seri
sej  Sene  Sene
sek  Sekani  Sekani
sel  Selkup  Selkup
sen  Nanerigé Sénoufo  Sénoufo, Nanerigé
seo  Suarmin  Suarmin
sep  Sìcìté Sénoufo  Sénoufo, Sìcìté
seq  Senara Sénoufo  Sénoufo, Senara
ser  Serrano  Serrano
ses  Koyraboro Senni Songhai  Songhai, Koyraboro Senni
set  Sentani  Sentani
seu  Serui-Laut  Serui-Laut
sev  Nyarafolo Senoufo  Senoufo, Nyarafolo
sew  Sewa Bay  Sewa Bay
sey  Secoya  Secoya
sez  Senthang Chin  Chin, Senthang
sfb  French Belgian Sign Language  French Belgian Sign Language
sfb  Langue des signes de Belgique Francophone  Langue des signes de Belgique Francophone
sfe  Eastern Subanen  Subanen, Eastern
sfm  Small Flowery Miao  Miao, Small Flowery
sfs  South African Sign Language  South African Sign Language
sfw  Sehwi  Sehwi
sga  Old Irish (to 900)  Irish, Old (to 900)
sgb  Mag-antsi Ayta  Ayta, Mag-antsi
sgc  Kipsigis  Kipsigis
sgd  Surigaonon  Surigaonon
sge  Segai  Segai
sgg  Swiss-German Sign Language  Swiss-German Sign Language
sgh  Shughni  Shughni
sgi  Suga  Suga
sgj  Surgujia  Surgujia
sgk  Sangkong  Sangkong
sgm  Singa  Singa
sgo  Songa  Songa
sgp  Singpho  Singpho
sgr  Sangisari  Sangisari
sgs  Samogitian  Samogitian
sgt  Brokpake  Brokpake
sgu  Salas  Salas
sgw  Sebat Bet Gurage  Sebat Bet Gurage
sgx  Sierra Leone Sign Language  Sierra Leone Sign Language
sgy  Sanglechi  Sanglechi
sgz  Sursurunga  Sursurunga
sha  Shall-Zwall  Shall-Zwall
shb  Ninam  Ninam
shc  Sonde  Sonde
shd  Kundal Shahi  Kundal Shahi
she  Sheko  Sheko
shg  Shua  Shua
shh  Shoshoni  Shoshoni
shi  Tachelhit  Tachelhit
shj  Shatt  Shatt
shk  Shilluk  Shilluk
shl  Shendu  Shendu
shm  Shahrudi  Shahrudi
shn  Shan  Shan
sho  Shanga  Shanga
shp  Shipibo-Conibo  Shipibo-Conibo
shq  Sala  Sala
shr  Shi  Shi
shs  Shuswap  Shuswap
sht  Shasta  Shasta
shu  Chadian Arabic  Arabic, Chadian
shv  Shehri  Shehri
shw  Shwai  Shwai
shx  She  She
shy  Tachawit  Tachawit
shz  Syenara Senoufo  Senoufo, Syenara
sia  Akkala Sami  Sami, Akkala
sib  Sebop  Sebop
sid  Sidamo  Sidamo
sie  Simaa  Simaa
sif  Siamou  Siamou
sig  Paasaal  Paasaal
sih  Sîshëë  Sîshëë
sih  Zire  Zire
sii  Shom Peng  Shom Peng
sij  Numbami  Numbami
sik  Sikiana  Sikiana
sil  Tumulung Sisaala  Sisaala, Tumulung
sim  Mende (Papua New Guinea)  Mende (Papua New Guinea)
sin  Sinhala  Sinhala
sin  Sinhalese  Sinhalese
sip  Sikkimese  Sikkimese
siq  Sonia  Sonia
sir  Siri  Siri
sis  Siuslaw  Siuslaw
siu  Sinagen  Sinagen
siv  Sumariup  Sumariup
siw  Siwai  Siwai
six  Sumau  Sumau
siy  Sivandi  Sivandi
siz  Siwi  Siwi
sja  Epena  Epena
sjb  Sajau Basap  Sajau Basap
sjd  Kildin Sami  Sami, Kildin
sje  Pite Sami  Sami, Pite
sjg  Assangori  Assangori
sjk  Kemi Sami  Sami, Kemi
sjl  Miji  Miji
sjl  Sajalong  Sajalong
sjm  Mapun  Mapun
sjn  Sindarin  Sindarin
sjo  Xibe  Xibe
sjp  Surjapuri  Surjapuri
sjr  Siar-Lak  Siar-Lak
sjs  Senhaja De Srair  Senhaja De Srair
sjt  Ter Sami  Sami, Ter
sju  Ume Sami  Sami, Ume
sjw  Shawnee  Shawnee
ska  Skagit  Skagit
skb  Saek  Saek
skc  Ma Manda  Ma Manda
skd  Southern Sierra Miwok  Miwok, Southern Sierra
ske  Seke (Vanuatu)  Seke (Vanuatu)
skf  Sakirabiá  Sakirabiá
skg  Sakalava Malagasy  Malagasy, Sakalava
skh  Sikule  Sikule
ski  Sika  Sika
skj  Seke (Nepal)  Seke (Nepal)
skk  Sok  Sok
skm  Kutong  Kutong
skn  Kolibugan Subanon  Subanon, Kolibugan
sko  Seko Tengah  Seko Tengah
skp  Sekapan  Sekapan
skq  Sininkere  Sininkere
skr  Seraiki  Seraiki
sks  Maia  Maia
skt  Sakata  Sakata
sku  Sakao  Sakao
skv  Skou  Skou
skw  Skepi Creole Dutch  Creole Dutch, Skepi
skx  Seko Padang  Seko Padang
sky  Sikaiana  Sikaiana
skz  Sekar  Sekar
slc  Sáliba  Sáliba
sld  Sissala  Sissala
sle  Sholaga  Sholaga
slf  Swiss-Italian Sign Language  Swiss-Italian Sign Language
slg  Selungai Murut  Selungai Murut
slh  Southern Puget Sound Salish  Salish, Southern Puget Sound
sli  Lower Silesian  Silesian, Lower
slj  Salumá  Salumá
slk  Slovak  Slovak
sll  Salt-Yui  Salt-Yui
slm  Pangutaran Sama  Sama, Pangutaran
sln  Salinan  Salinan
slp  Lamaholot  Lamaholot
slq  Salchuq  Salchuq
slr  Salar  Salar
sls  Singapore Sign Language  Singapore Sign Language
slt  Sila  Sila
slu  Selaru  Selaru
slv  Slovenian  Slovenian
slw  Sialum  Sialum
slx  Salampasu  Salampasu
sly  Selayar  Selayar
slz  Ma'ya  Ma'ya
sma  Southern Sami  Sami, Southern
smb  Simbari  Simbari
smc  Som  Som
smd  Sama  Sama
sme  Northern Sami  Sami, Northern
smf  Auwe  Auwe
smg  Simbali  Simbali
smh  Samei  Samei
smj  Lule Sami  Lule Sami
smk  Bolinao  Bolinao
sml  Central Sama  Sama, Central
smm  Musasa  Musasa
smn  Inari Sami  Sami, Inari
smo  Samoan  Samoan
smp  Samaritan  Samaritan
smq  Samo  Samo
smr  Simeulue  Simeulue
sms  Skolt Sami  Sami, Skolt
smt  Simte  Simte
smu  Somray  Somray
smv  Samvedi  Samvedi
smw  Sumbawa  Sumbawa
smx  Samba  Samba
smy  Semnani  Semnani
smz  Simeku  Simeku
sna  Shona  Shona
snb  Sebuyau  Sebuyau
snc  Sinaugoro  Sinaugoro
snd  Sindhi  Sindhi
sne  Bau Bidayuh  Bidayuh, Bau
snf  Noon  Noon
sng  Sanga (Democratic Republic of Congo)  Sanga (Democratic Republic of Congo)
snh  Shinabo  Shinabo
sni  Sensi  Sensi
snj  Riverain Sango  Sango, Riverain
snk  Soninke  Soninke
snl  Sangil  Sangil
snm  Southern Ma'di  Ma'di, Southern
snn  Siona  Siona
sno  Snohomish  Snohomish
snp  Siane  Siane
snq  Sangu (Gabon)  Sangu (Gabon)
snr  Sihan  Sihan
sns  Nahavaq  Nahavaq
sns  South West Bay  South West Bay
snu  Senggi  Senggi
snu  Viid  Viid
snv  Sa'ban  Sa'ban
snw  Selee  Selee
snx  Sam  Sam
sny  Saniyo-Hiyewe  Saniyo-Hiyewe
snz  Sinsauru  Sinsauru
soa  Thai Song  Thai Song
sob  Sobei  Sobei
soc  So (Democratic Republic of Congo)  So (Democratic Republic of Congo)
sod  Songoora  Songoora
soe  Songomeno  Songomeno
sog  Sogdian  Sogdian
soh  Aka  Aka
soi  Sonha  Sonha
soj  Soi  Soi
sok  Sokoro  Sokoro
sol  Solos  Solos
som  Somali  Somali
soo  Songo  Songo
sop  Songe  Songe
soq  Kanasi  Kanasi
sor  Somrai  Somrai
sos  Seeku  Seeku
sot  Southern Sotho  Sotho, Southern
sou  Southern Thai  Thai, Southern
sov  Sonsorol  Sonsorol
sow  Sowanda  Sowanda
sox  Swo  Swo
soy  Miyobe  Miyobe
soz  Temi  Temi
spa  Castilian  Castilian
spa  Spanish  Spanish
spb  Sepa (Indonesia)  Sepa (Indonesia)
spc  Sapé  Sapé
spd  Saep  Saep
spe  Sepa (Papua New Guinea)  Sepa (Papua New Guinea)
spg  Sian  Sian
spi  Saponi  Saponi
spk  Sengo  Sengo
spl  Selepet  Selepet
spm  Akukem  Akukem
spo  Spokane  Spokane
spp  Supyire Senoufo  Senoufo, Supyire
spq  Loreto-Ucayali Spanish  Spanish, Loreto-Ucayali
spr  Saparua  Saparua
sps  Saposa  Saposa
spt  Spiti Bhoti  Bhoti, Spiti
spu  Sapuan  Sapuan
spv  Kosli  Kosli
spv  Sambalpuri  Sambalpuri
spx  South Picene  Picene, South
spy  Sabaot  Sabaot
sqa  Shama-Sambuga  Shama-Sambuga
sqh  Shau  Shau
sqi  Albanian  Albanian
sqk  Albanian Sign Language  Albanian Sign Language
sqm  Suma  Suma
sqn  Susquehannock  Susquehannock
sqo  Sorkhei  Sorkhei
sqq  Sou  Sou
sqr  Siculo Arabic  Arabic, Siculo
sqs  Sri Lankan Sign Language  Sri Lankan Sign Language
sqt  Soqotri  Soqotri
squ  Squamish  Squamish
sra  Saruga  Saruga
srb  Sora  Sora
src  Logudorese Sardinian  Sardinian, Logudorese
srd  Sardinian  Sardinian
sre  Sara  Sara
srf  Nafi  Nafi
srg  Sulod  Sulod
srh  Sarikoli  Sarikoli
sri  Siriano  Siriano
srk  Serudung Murut  Serudung Murut
srl  Isirawa  Isirawa
srm  Saramaccan  Saramaccan
srn  Sranan Tongo  Sranan Tongo
sro  Campidanese Sardinian  Sardinian, Campidanese
srp  Serbian  Serbian
srq  Sirionó  Sirionó
srr  Serer  Serer
srs  Sarsi  Sarsi
srt  Sauri  Sauri
sru  Suruí  Suruí
srv  Southern Sorsoganon  Sorsoganon, Southern
srw  Serua  Serua
srx  Sirmauri  Sirmauri
sry  Sera  Sera
srz  Shahmirzadi  Shahmirzadi
ssb  Southern Sama  Sama, Southern
ssc  Suba-Simbiti  Suba-Simbiti
ssd  Siroi  Siroi
sse  Balangingi  Balangingi
sse  Bangingih Sama  Sama, Bangingih
ssf  Thao  Thao
ssg  Seimat  Seimat
ssh  Shihhi Arabic  Arabic, Shihhi
ssi  Sansi  Sansi
ssj  Sausi  Sausi
ssk  Sunam  Sunam
ssl  Western Sisaala  Sisaala, Western
ssm  Semnam  Semnam
ssn  Waata  Waata
sso  Sissano  Sissano
ssp  Spanish Sign Language  Spanish Sign Language
ssq  So'a  So'a
ssr  Swiss-French Sign Language  Swiss-French Sign Language
sss  Sô  Sô
sst  Sinasina  Sinasina
ssu  Susuami  Susuami
ssv  Shark Bay  Shark Bay
ssw  Swati  Swati
ssx  Samberigi  Samberigi
ssy  Saho  Saho
ssz  Sengseng  Sengseng
sta  Settla  Settla
stb  Northern Subanen  Subanen, Northern
std  Sentinel  Sentinel
ste  Liana-Seti  Liana-Seti
stf  Seta  Seta
stg  Trieng  Trieng
sth  Shelta  Shelta
sti  Bulo Stieng  Stieng, Bulo
stj  Matya Samo  Samo, Matya
stk  Arammba  Arammba
stl  Stellingwerfs  Stellingwerfs
stm  Setaman  Setaman
stn  Owa  Owa
sto  Stoney  Stoney
stp  Southeastern Tepehuan  Tepehuan, Southeastern
stq  Saterfriesisch  Saterfriesisch
str  Straits Salish  Salish, Straits
sts  Shumashti  Shumashti
stt  Budeh Stieng  Stieng, Budeh
stu  Samtao  Samtao
stv  Silt'e  Silt'e
stw  Satawalese  Satawalese
sty  Siberian Tatar  Tatar, Siberian
sua  Sulka  Sulka
sub  Suku  Suku
suc  Western Subanon  Subanon, Western
sue  Suena  Suena
sug  Suganga  Suganga
sui  Suki  Suki
suj  Shubi  Shubi
suk  Sukuma  Sukuma
sun  Sundanese  Sundanese
suq  Suri  Suri
sur  Mwaghavul  Mwaghavul
sus  Susu  Susu
sut  Subtiaba  Subtiaba
suv  Puroik  Puroik
suw  Sumbwa  Sumbwa
sux  Sumerian  Sumerian
suy  Suyá  Suyá
suz  Sunwar  Sunwar
sva  Svan  Svan
svb  Ulau-Suain  Ulau-Suain
svc  Vincentian Creole English  Creole English, Vincentian
sve  Serili  Serili
svk  Slovakian Sign Language  Slovakian Sign Language
svm  Slavomolisano  Slavomolisano
svr  Savara  Savara
svs  Savosavo  Savosavo
svx  Skalvian  Skalvian
swa  Swahili (macrolanguage)  Swahili (macrolanguage)
swb  Maore Comorian  Comorian, Maore
swc  Congo Swahili  Swahili, Congo
swe  Swedish  Swedish
swf  Sere  Sere
swg  Swabian  Swabian
swh  Kiswahili  Kiswahili
swh  Swahili (individual language)  Swahili (individual language)
swi  Sui  Sui
swj  Sira  Sira
swk  Malawi Sena  Sena, Malawi
swl  Swedish Sign Language  Swedish Sign Language
swm  Samosa  Samosa
swn  Sawknah  Sawknah
swo  Shanenawa  Shanenawa
swp  Suau  Suau
swq  Sharwa  Sharwa
swr  Saweru  Saweru
sws  Seluwasan  Seluwasan
swt  Sawila  Sawila
swu  Suwawa  Suwawa
swv  Shekhawati  Shekhawati
sww  Sowa  Sowa
swx  Suruahá  Suruahá
swy  Sarua  Sarua
sxb  Suba  Suba
sxc  Sicanian  Sicanian
sxe  Sighu  Sighu
sxg  Shixing  Shixing
sxk  Southern Kalapuya  Kalapuya, Southern
sxl  Selian  Selian
sxm  Samre  Samre
sxn  Sangir  Sangir
sxo  Sorothaptic  Sorothaptic
sxr  Saaroa  Saaroa
sxs  Sasaru  Sasaru
sxu  Upper Saxon  Saxon, Upper
sxw  Saxwe Gbe  Gbe, Saxwe
sya  Siang  Siang
syb  Central Subanen  Subanen, Central
syc  Classical Syriac  Syriac, Classical
syi  Seki  Seki
syk  Sukur  Sukur
syl  Sylheti  Sylheti
sym  Maya Samo  Samo, Maya
syn  Senaya  Senaya
syo  Suoy  Suoy
syr  Syriac  Syriac
sys  Sinyar  Sinyar
syw  Kagate  Kagate
syy  Al-Sayyid Bedouin Sign Language  Al-Sayyid Bedouin Sign Language
sza  Semelai  Semelai
szb  Ngalum  Ngalum
szc  Semaq Beri  Semaq Beri
szd  Seru  Seru
sze  Seze  Seze
szg  Sengele  Sengele
szl  Silesian  Silesian
szn  Sula  Sula
szp  Suabo  Suabo
szv  Isu (Fako Division)  Isu (Fako Division)
szw  Sawai  Sawai
taa  Lower Tanana  Tanana, Lower
tab  Tabassaran  Tabassaran
tac  Lowland Tarahumara  Tarahumara, Lowland
tad  Tause  Tause
tae  Tariana  Tariana
taf  Tapirapé  Tapirapé
tag  Tagoi  Tagoi
tah  Tahitian  Tahitian
taj  Eastern Tamang  Tamang, Eastern
tak  Tala  Tala
tal  Tal  Tal
tam  Tamil  Tamil
tan  Tangale  Tangale
tao  Yami  Yami
tap  Taabwa  Taabwa
taq  Tamasheq  Tamasheq
tar  Central Tarahumara  Tarahumara, Central
tas  Tay Boi  Tay Boi
tat  Tatar  Tatar
tau  Upper Tanana  Tanana, Upper
tav  Tatuyo  Tatuyo
taw  Tai  Tai
tax  Tamki  Tamki
tay  Atayal  Atayal
taz  Tocho  Tocho
tba  Aikanã  Aikanã
tbb  Tapeba  Tapeba
tbc  Takia  Takia
tbd  Kaki Ae  Kaki Ae
tbe  Tanimbili  Tanimbili
tbf  Mandara  Mandara
tbg  North Tairora  Tairora, North
tbh  Thurawal  Thurawal
tbi  Gaam  Gaam
tbj  Tiang  Tiang
tbk  Calamian Tagbanwa  Tagbanwa, Calamian
tbl  Tboli  Tboli
tbm  Tagbu  Tagbu
tbn  Barro Negro Tunebo  Tunebo, Barro Negro
tbo  Tawala  Tawala
tbp  Diebroud  Diebroud
tbp  Taworta  Taworta
tbr  Tumtum  Tumtum
tbs  Tanguat  Tanguat
tbt  Tembo (Kitembo)  Tembo (Kitembo)
tbu  Tubar  Tubar
tbv  Tobo  Tobo
tbw  Tagbanwa  Tagbanwa
tbx  Kapin  Kapin
tby  Tabaru  Tabaru
tbz  Ditammari  Ditammari
tca  Ticuna  Ticuna
tcb  Tanacross  Tanacross
tcc  Datooga  Datooga
tcd  Tafi  Tafi
tce  Southern Tutchone  Tutchone, Southern
tcf  Malinaltepec Me'phaa  Me'phaa, Malinaltepec
tcf  Malinaltepec Tlapanec  Tlapanec, Malinaltepec
tcg  Tamagario  Tamagario
tch  Turks And Caicos Creole English  Creole English, Turks And Caicos
tci  Wára  Wára
tck  Tchitchege  Tchitchege
tcl  Taman (Myanmar)  Taman (Myanmar)
tcm  Tanahmerah  Tanahmerah
tcn  Tichurong  Tichurong
tco  Taungyo  Taungyo
tcp  Tawr Chin  Chin, Tawr
tcq  Kaiy  Kaiy
tcs  Torres Strait Creole  Creole, Torres Strait
tct  T'en  T'en
tcu  Southeastern Tarahumara  Tarahumara, Southeastern
tcw  Tecpatlán Totonac  Totonac, Tecpatlán
tcx  Toda  Toda
tcy  Tulu  Tulu
tcz  Thado Chin  Chin, Thado
tda  Tagdal  Tagdal
tdb  Panchpargania  Panchpargania
tdc  Emberá-Tadó  Emberá-Tadó
tdd  Tai Nüa  Tai Nüa
tde  Tiranige Diga Dogon  Dogon, Tiranige Diga
tdf  Talieng  Talieng
tdg  Western Tamang  Tamang, Western
tdh  Thulung  Thulung
tdi  Tomadino  Tomadino
tdj  Tajio  Tajio
tdk  Tambas  Tambas
tdl  Sur  Sur
tdn  Tondano  Tondano
tdo  Teme  Teme
tdq  Tita  Tita
tdr  Todrah  Todrah
tds  Doutai  Doutai
tdt  Tetun Dili  Tetun Dili
tdu  Tempasuk Dusun  Dusun, Tempasuk
tdv  Toro  Toro
tdx  Tandroy-Mahafaly Malagasy  Malagasy, Tandroy-Mahafaly
tdy  Tadyawan  Tadyawan
tea  Temiar  Temiar
teb  Tetete  Tetete
tec  Terik  Terik
ted  Tepo Krumen  Krumen, Tepo
tee  Huehuetla Tepehua  Tepehua, Huehuetla
tef  Teressa  Teressa
teg  Teke-Tege  Teke-Tege
teh  Tehuelche  Tehuelche
tei  Torricelli  Torricelli
tek  Ibali Teke  Teke, Ibali
tel  Telugu  Telugu
tem  Timne  Timne
ten  Tama (Colombia)  Tama (Colombia)
teo  Teso  Teso
tep  Tepecano  Tepecano
teq  Temein  Temein
ter  Tereno  Tereno
tes  Tengger  Tengger
tet  Tetum  Tetum
teu  Soo  Soo
tev  Teor  Teor
tew  Tewa (USA)  Tewa (USA)
tex  Tennet  Tennet
tey  Tulishi  Tulishi
tfi  Tofin Gbe  Gbe, Tofin
tfn  Tanaina  Tanaina
tfo  Tefaro  Tefaro
tfr  Teribe  Teribe
tft  Ternate  Ternate
tga  Sagalla  Sagalla
tgb  Tobilung  Tobilung
tgc  Tigak  Tigak
tgd  Ciwogai  Ciwogai
tge  Eastern Gorkha Tamang  Tamang, Eastern Gorkha
tgf  Chalikha  Chalikha
tgh  Tobagonian Creole English  Creole English, Tobagonian
tgi  Lawunuia  Lawunuia
tgj  Tagin  Tagin
tgk  Tajik  Tajik
tgl  Tagalog  Tagalog
tgn  Tandaganon  Tandaganon
tgo  Sudest  Sudest
tgp  Tangoa  Tangoa
tgq  Tring  Tring
tgr  Tareng  Tareng
tgs  Nume  Nume
tgt  Central Tagbanwa  Tagbanwa, Central
tgu  Tanggu  Tanggu
tgv  Tingui-Boto  Tingui-Boto
tgw  Tagwana Senoufo  Senoufo, Tagwana
tgx  Tagish  Tagish
tgy  Togoyo  Togoyo
tgz  Tagalaka  Tagalaka
tha  Thai  Thai
thc  Tai Hang Tong  Tai Hang Tong
thd  Thayore  Thayore
the  Chitwania Tharu  Tharu, Chitwania
thf  Thangmi  Thangmi
thh  Northern Tarahumara  Tarahumara, Northern
thi  Tai Long  Tai Long
thk  Kitharaka  Kitharaka
thk  Tharaka  Tharaka
thl  Dangaura Tharu  Tharu, Dangaura
thm  Aheu  Aheu
thn  Thachanadan  Thachanadan
thp  Thompson  Thompson
thq  Kochila Tharu  Tharu, Kochila
thr  Rana Tharu  Tharu, Rana
ths  Thakali  Thakali
tht  Tahltan  Tahltan
thu  Thuri  Thuri
thv  Tahaggart Tamahaq  Tamahaq, Tahaggart
thw  Thudam  Thudam
thx  The  The
thy  Tha  Tha
thz  Tayart Tamajeq  Tamajeq, Tayart
tia  Tidikelt Tamazight  Tamazight, Tidikelt
tic  Tira  Tira
tid  Tidong  Tidong
tif  Tifal  Tifal
tig  Tigre  Tigre
tih  Timugon Murut  Murut, Timugon
tii  Tiene  Tiene
tij  Tilung  Tilung
tik  Tikar  Tikar
til  Tillamook  Tillamook
tim  Timbe  Timbe
tin  Tindi  Tindi
tio  Teop  Teop
tip  Trimuris  Trimuris
tiq  Tiéfo  Tiéfo
tir  Tigrinya  Tigrinya
tis  Masadiit Itneg  Itneg, Masadiit
tit  Tinigua  Tinigua
tiu  Adasen  Adasen
tiv  Tiv  Tiv
tiw  Tiwi  Tiwi
tix  Southern Tiwa  Tiwa, Southern
tiy  Tiruray  Tiruray
tiz  Tai Hongjin  Tai Hongjin
tja  Tajuasohn  Tajuasohn
tjg  Tunjung  Tunjung
tji  Northern Tujia  Tujia, Northern
tjl  Tai Laing  Tai Laing
tjm  Timucua  Timucua
tjn  Tonjon  Tonjon
tjo  Temacine Tamazight  Tamazight, Temacine
tjs  Southern Tujia  Tujia, Southern
tju  Tjurruru  Tjurruru
tjw  Djabwurrung  Djabwurrung
tka  Truká  Truká
tkb  Buksa  Buksa
tkd  Tukudede  Tukudede
tke  Takwane  Takwane
tkf  Tukumanféd  Tukumanféd
tkg  Tesaka Malagasy  Malagasy, Tesaka
tkl  Tokelau  Tokelau
tkm  Takelma  Takelma
tkn  Toku-No-Shima  Toku-No-Shima
tkp  Tikopia  Tikopia
tkq  Tee  Tee
tkr  Tsakhur  Tsakhur
tks  Takestani  Takestani
tkt  Kathoriya Tharu  Tharu, Kathoriya
tku  Upper Necaxa Totonac  Totonac, Upper Necaxa
tkw  Teanu  Teanu
tkx  Tangko  Tangko
tkz  Takua  Takua
tla  Southwestern Tepehuan  Tepehuan, Southwestern
tlb  Tobelo  Tobelo
tlc  Yecuatla Totonac  Totonac, Yecuatla
tld  Talaud  Talaud
tlf  Telefol  Telefol
tlg  Tofanma  Tofanma
tlh  Klingon  Klingon
tlh  tlhIngan-Hol  tlhIngan-Hol
tli  Tlingit  Tlingit
tlj  Talinga-Bwisi  Talinga-Bwisi
tlk  Taloki  Taloki
tll  Tetela  Tetela
tlm  Tolomako  Tolomako
tln  Talondo'  Talondo'
tlo  Talodi  Talodi
tlp  Filomena Mata-Coahuitlán Totonac  Totonac, Filomena Mata-Coahuitlán
tlq  Tai Loi  Tai Loi
tlr  Talise  Talise
tls  Tambotalo  Tambotalo
tlt  Teluti  Teluti
tlu  Tulehu  Tulehu
tlv  Taliabu  Taliabu
tlx  Khehek  Khehek
tly  Talysh  Talysh
tma  Tama (Chad)  Tama (Chad)
tmb  Avava  Avava
tmb  Katbol  Katbol
tmc  Tumak  Tumak
tmd  Haruai  Haruai
tme  Tremembé  Tremembé
tmf  Toba-Maskoy  Toba-Maskoy
tmg  Ternateño  Ternateño
tmh  Tamashek  Tamashek
tmi  Tutuba  Tutuba
tmj  Samarokena  Samarokena
tmk  Northwestern Tamang  Tamang, Northwestern
tml  Tamnim Citak  Citak, Tamnim
tmm  Tai Thanh  Tai Thanh
tmn  Taman (Indonesia)  Taman (Indonesia)
tmo  Temoq  Temoq
tmp  Tai Mène  Tai Mène
tmq  Tumleo  Tumleo
tmr  Jewish Babylonian Aramaic (ca. 200-1200 CE)  Aramaic, Jewish Babylonian (ca. 200-1200 CE)
tms  Tima  Tima
tmt  Tasmate  Tasmate
tmu  Iau  Iau
tmv  Tembo (Motembo)  Tembo (Motembo)
tmw  Temuan  Temuan
tmy  Tami  Tami
tmz  Tamanaku  Tamanaku
tna  Tacana  Tacana
tnb  Western Tunebo  Tunebo, Western
tnc  Tanimuca-Retuarã  Tanimuca-Retuarã
tnd  Angosturas Tunebo  Tunebo, Angosturas
tne  Tinoc Kallahan  Kallahan, Tinoc
tng  Tobanga  Tobanga
tnh  Maiani  Maiani
tni  Tandia  Tandia
tnk  Kwamera  Kwamera
tnl  Lenakel  Lenakel
tnm  Tabla  Tabla
tnn  North Tanna  Tanna, North
tno  Toromono  Toromono
tnp  Whitesands  Whitesands
tnq  Taino  Taino
tnr  Ménik  Ménik
tns  Tenis  Tenis
tnt  Tontemboan  Tontemboan
tnu  Tay Khang  Tay Khang
tnv  Tangchangya  Tangchangya
tnw  Tonsawang  Tonsawang
tnx  Tanema  Tanema
tny  Tongwe  Tongwe
tnz  Tonga (Thailand)  Tonga (Thailand)
tob  Toba  Toba
toc  Coyutla Totonac  Totonac, Coyutla
tod  Toma  Toma
toe  Tomedes  Tomedes
tof  Gizrra  Gizrra
tog  Tonga (Nyasa)  Tonga (Nyasa)
toh  Gitonga  Gitonga
toi  Tonga (Zambia)  Tonga (Zambia)
toj  Tojolabal  Tojolabal
tol  Tolowa  Tolowa
tom  Tombulu  Tombulu
ton  Tonga (Tonga Islands)  Tonga (Tonga Islands)
too  Xicotepec De Juárez Totonac  Totonac, Xicotepec De Juárez
top  Papantla Totonac  Totonac, Papantla
toq  Toposa  Toposa
tor  Togbo-Vara Banda  Banda, Togbo-Vara
tos  Highland Totonac  Totonac, Highland
tou  Tho  Tho
tov  Upper Taromi  Taromi, Upper
tow  Jemez  Jemez
tox  Tobian  Tobian
toy  Topoiyo  Topoiyo
toz  To  To
tpa  Taupota  Taupota
tpc  Azoyú Me'phaa  Me'phaa, Azoyú
tpc  Azoyú Tlapanec  Tlapanec, Azoyú
tpe  Tippera  Tippera
tpf  Tarpia  Tarpia
tpg  Kula  Kula
tpi  Tok Pisin  Tok Pisin
tpj  Tapieté  Tapieté
tpk  Tupinikin  Tupinikin
tpl  Tlacoapa Me'phaa  Me'phaa, Tlacoapa
tpl  Tlacoapa Tlapanec  Tlapanec, Tlacoapa
tpm  Tampulma  Tampulma
tpn  Tupinambá  Tupinambá
tpo  Tai Pao  Tai Pao
tpp  Pisaflores Tepehua  Tepehua, Pisaflores
tpq  Tukpa  Tukpa
tpr  Tuparí  Tuparí
tpt  Tlachichilco Tepehua  Tepehua, Tlachichilco
tpu  Tampuan  Tampuan
tpv  Tanapag  Tanapag
tpw  Tupí  Tupí
tpx  Acatepec Me'phaa  Me'phaa, Acatepec
tpx  Acatepec Tlapanec  Tlapanec, Acatepec
tpy  Trumai  Trumai
tpz  Tinputz  Tinputz
tqb  Tembé  Tembé
tql  Lehali  Lehali
tqm  Turumsa  Turumsa
tqn  Tenino  Tenino
tqo  Toaripi  Toaripi
tqp  Tomoip  Tomoip
tqq  Tunni  Tunni
tqr  Torona  Torona
tqt  Western Totonac  Totonac, Western
tqu  Touo  Touo
tqw  Tonkawa  Tonkawa
tra  Tirahi  Tirahi
trb  Terebu  Terebu
trc  Copala Triqui  Triqui, Copala
trd  Turi  Turi
tre  East Tarangan  Tarangan, East
trf  Trinidadian Creole English  Creole English, Trinidadian
trg  Lishán Didán  Lishán Didán
trh  Turaka  Turaka
tri  Trió  Trió
trj  Toram  Toram
trl  Traveller Scottish  Scottish, Traveller
trm  Tregami  Tregami
trn  Trinitario  Trinitario
tro  Tarao Naga  Naga, Tarao
trp  Kok Borok  Kok Borok
trq  San Martín Itunyoso Triqui  Triqui, San Martín Itunyoso
trr  Taushiro  Taushiro
trs  Chicahuaxtla Triqui  Triqui, Chicahuaxtla
trt  Tunggare  Tunggare
tru  Surayt  Surayt
tru  Turoyo  Turoyo
trv  Taroko  Taroko
trw  Torwali  Torwali
trx  Tringgus-Sembaan Bidayuh  Bidayuh, Tringgus-Sembaan
try  Turung  Turung
trz  Torá  Torá
tsa  Tsaangi  Tsaangi
tsb  Tsamai  Tsamai
tsc  Tswa  Tswa
tsd  Tsakonian  Tsakonian
tse  Tunisian Sign Language  Tunisian Sign Language
tsf  Southwestern Tamang  Tamang, Southwestern
tsg  Tausug  Tausug
tsh  Tsuvan  Tsuvan
tsi  Tsimshian  Tsimshian
tsj  Tshangla  Tshangla
tsk  Tseku  Tseku
tsl  Ts'ün-Lao  Ts'ün-Lao
tsm  Türk İşaret Dili  Türk İşaret Dili
tsm  Turkish Sign Language  Turkish Sign Language
tsn  Tswana  Tswana
tso  Tsonga  Tsonga
tsp  Northern Toussian  Toussian, Northern
tsq  Thai Sign Language  Thai Sign Language
tsr  Akei  Akei
tss  Taiwan Sign Language  Taiwan Sign Language
tst  Tondi Songway Kiini  Songway Kiini, Tondi
tsu  Tsou  Tsou
tsv  Tsogo  Tsogo
tsw  Tsishingini  Tsishingini
tsx  Mubami  Mubami
tsy  Tebul Sign Language  Tebul Sign Language
tsz  Purepecha  Purepecha
tta  Tutelo  Tutelo
ttb  Gaa  Gaa
ttc  Tektiteko  Tektiteko
ttd  Tauade  Tauade
tte  Bwanabwana  Bwanabwana
ttf  Tuotomb  Tuotomb
ttg  Tutong  Tutong
tth  Upper Ta'oih  Ta'oih, Upper
tti  Tobati  Tobati
ttj  Tooro  Tooro
ttk  Totoro  Totoro
ttl  Totela  Totela
ttm  Northern Tutchone  Tutchone, Northern
ttn  Towei  Towei
tto  Lower Ta'oih  Ta'oih, Lower
ttp  Tombelala  Tombelala
ttq  Tawallammat Tamajaq  Tamajaq, Tawallammat
ttr  Tera  Tera
tts  Northeastern Thai  Thai, Northeastern
ttt  Muslim Tat  Tat, Muslim
ttu  Torau  Torau
ttv  Titan  Titan
ttw  Long Wat  Long Wat
tty  Sikaritai  Sikaritai
ttz  Tsum  Tsum
tua  Wiarumus  Wiarumus
tub  Tübatulabal  Tübatulabal
tuc  Mutu  Mutu
tud  Tuxá  Tuxá
tue  Tuyuca  Tuyuca
tuf  Central Tunebo  Tunebo, Central
tug  Tunia  Tunia
tuh  Taulil  Taulil
tui  Tupuri  Tupuri
tuj  Tugutil  Tugutil
tuk  Turkmen  Turkmen
tul  Tula  Tula
tum  Tumbuka  Tumbuka
tun  Tunica  Tunica
tuo  Tucano  Tucano
tuq  Tedaga  Tedaga
tur  Turkish  Turkish
tus  Tuscarora  Tuscarora
tuu  Tututni  Tututni
tuv  Turkana  Turkana
tux  Tuxináwa  Tuxináwa
tuy  Tugen  Tugen
tuz  Turka  Turka
tva  Vaghua  Vaghua
tvd  Tsuvadi  Tsuvadi
tve  Te'un  Te'un
tvk  Southeast Ambrym  Ambrym, Southeast
tvl  Tuvalu  Tuvalu
tvm  Tela-Masbuar  Tela-Masbuar
tvn  Tavoyan  Tavoyan
tvo  Tidore  Tidore
tvs  Taveta  Taveta
tvt  Tutsa Naga  Naga, Tutsa
tvu  Tunen  Tunen
tvw  Sedoa  Sedoa
tvy  Timor Pidgin  Pidgin, Timor
twa  Twana  Twana
twb  Western Tawbuid  Tawbuid, Western
twc  Teshenawa  Teshenawa
twd  Twents  Twents
twe  Tewa (Indonesia)  Tewa (Indonesia)
twf  Northern Tiwa  Tiwa, Northern
twg  Tereweng  Tereweng
twh  Tai Dón  Tai Dón
twi  Twi  Twi
twl  Tawara  Tawara
twm  Tawang Monpa  Monpa, Tawang
twn  Twendi  Twendi
two  Tswapong  Tswapong
twp  Ere  Ere
twq  Tasawaq  Tasawaq
twr  Southwestern Tarahumara  Tarahumara, Southwestern
twt  Turiwára  Turiwára
twu  Termanu  Termanu
tww  Tuwari  Tuwari
twx  Tewe  Tewe
twy  Tawoyan  Tawoyan
txa  Tombonuo  Tombonuo
txb  Tokharian B  Tokharian B
txc  Tsetsaut  Tsetsaut
txe  Totoli  Totoli
txg  Tangut  Tangut
txh  Thracian  Thracian
txi  Ikpeng  Ikpeng
txm  Tomini  Tomini
txn  West Tarangan  Tarangan, West
txo  Toto  Toto
txq  Tii  Tii
txr  Tartessian  Tartessian
txs  Tonsea  Tonsea
txt  Citak  Citak
txu  Kayapó  Kayapó
txx  Tatana  Tatana
txy  Tanosy Malagasy  Malagasy, Tanosy
tya  Tauya  Tauya
tye  Kyanga  Kyanga
tyh  O'du  O'du
tyi  Teke-Tsaayi  Teke-Tsaayi
tyj  Tai Do  Tai Do
tyl  Thu Lao  Thu Lao
tyn  Kombai  Kombai
typ  Thaypan  Thaypan
tyr  Tai Daeng  Tai Daeng
tys  Tày Sa Pa  Tày Sa Pa
tyt  Tày Tac  Tày Tac
tyu  Kua  Kua
tyv  Tuvinian  Tuvinian
tyx  Teke-Tyee  Teke-Tyee
tyz  Tày  Tày
tza  Tanzanian Sign Language  Tanzanian Sign Language
tzh  Tzeltal  Tzeltal
tzj  Tz'utujil  Tz'utujil
tzl  Talossan  Talossan
tzm  Central Atlas Tamazight  Tamazight, Central Atlas
tzn  Tugun  Tugun
tzo  Tzotzil  Tzotzil
tzx  Tabriak  Tabriak
uam  Uamué  Uamué
uan  Kuan  Kuan
uar  Tairuma  Tairuma
uba  Ubang  Ubang
ubi  Ubi  Ubi
ubl  Buhi'non Bikol  Bikol, Buhi'non
ubr  Ubir  Ubir
ubu  Umbu-Ungu  Umbu-Ungu
uby  Ubykh  Ubykh
uda  Uda  Uda
ude  Udihe  Udihe
udg  Muduga  Muduga
udi  Udi  Udi
udj  Ujir  Ujir
udl  Wuzlam  Wuzlam
udm  Udmurt  Udmurt
udu  Uduk  Uduk
ues  Kioko  Kioko
ufi  Ufim  Ufim
uga  Ugaritic  Ugaritic
ugb  Kuku-Ugbanh  Kuku-Ugbanh
uge  Ughele  Ughele
ugn  Ugandan Sign Language  Ugandan Sign Language
ugo  Ugong  Ugong
ugy  Uruguayan Sign Language  Uruguayan Sign Language
uha  Uhami  Uhami
uhn  Damal  Damal
uig  Uighur  Uighur
uig  Uyghur  Uyghur
uis  Uisai  Uisai
uiv  Iyive  Iyive
uji  Tanjijili  Tanjijili
uka  Kaburi  Kaburi
ukg  Ukuriguma  Ukuriguma
ukh  Ukhwejo  Ukhwejo
ukl  Ukrainian Sign Language  Ukrainian Sign Language
ukp  Ukpe-Bayobiri  Ukpe-Bayobiri
ukq  Ukwa  Ukwa
ukr  Ukrainian  Ukrainian
uks  Kaapor Sign Language  Kaapor Sign Language
uks  Urubú-Kaapor Sign Language  Urubú-Kaapor Sign Language
uku  Ukue  Ukue
ukw  Ukwuani-Aboh-Ndoni  Ukwuani-Aboh-Ndoni
uky  Kuuk-Yak  Kuuk-Yak
ula  Fungwa  Fungwa
ulb  Ulukwumi  Ulukwumi
ulc  Ulch  Ulch
ule  Lule  Lule
ulf  Afra  Afra
ulf  Usku  Usku
uli  Ulithian  Ulithian
ulk  Meriam  Meriam
ull  Ullatan  Ullatan
ulm  Ulumanda'  Ulumanda'
uln  Unserdeutsch  Unserdeutsch
ulu  Uma' Lung  Uma' Lung
ulw  Ulwa  Ulwa
uma  Umatilla  Umatilla
umb  Umbundu  Umbundu
umc  Marrucinian  Marrucinian
umd  Umbindhamu  Umbindhamu
umg  Umbuygamu  Umbuygamu
umi  Ukit  Ukit
umm  Umon  Umon
umn  Makyan Naga  Naga, Makyan
umo  Umotína  Umotína
ump  Umpila  Umpila
umr  Umbugarla  Umbugarla
ums  Pendau  Pendau
umu  Munsee  Munsee
una  North Watut  Watut, North
und  Undetermined  Undetermined
une  Uneme  Uneme
ung  Ngarinyin  Ngarinyin
unk  Enawené-Nawé  Enawené-Nawé
unm  Unami  Unami
unn  Kurnai  Kurnai
unr  Mundari  Mundari
unu  Unubahe  Unubahe
unx  Munda  Munda
unz  Unde Kaili  Kaili, Unde
uok  Uokha  Uokha
upi  Umeda  Umeda
upv  Uripiv-Wala-Rano-Atchin  Uripiv-Wala-Rano-Atchin
ura  Urarina  Urarina
urb  Kaapor  Kaapor
urb  Urubú-Kaapor  Urubú-Kaapor
urc  Urningangg  Urningangg
urd  Urdu  Urdu
ure  Uru  Uru
urf  Uradhi  Uradhi
urg  Urigina  Urigina
urh  Urhobo  Urhobo
uri  Urim  Urim
urk  Urak Lawoi'  Urak Lawoi'
url  Urali  Urali
urm  Urapmin  Urapmin
urn  Uruangnirin  Uruangnirin
uro  Ura (Papua New Guinea)  Ura (Papua New Guinea)
urp  Uru-Pa-In  Uru-Pa-In
urr  Lehalurup  Lehalurup
urr  Löyöp  Löyöp
urt  Urat  Urat
uru  Urumi  Urumi
urv  Uruava  Uruava
urw  Sop  Sop
urx  Urimo  Urimo
ury  Orya  Orya
urz  Uru-Eu-Wau-Wau  Uru-Eu-Wau-Wau
usa  Usarufa  Usarufa
ush  Ushojo  Ushojo
usi  Usui  Usui
usk  Usaghade  Usaghade
usp  Uspanteco  Uspanteco
usu  Uya  Uya
uta  Otank  Otank
ute  Ute-Southern Paiute  Ute-Southern Paiute
utp  Amba (Solomon Islands)  Amba (Solomon Islands)
utr  Etulo  Etulo
utu  Utu  Utu
uum  Urum  Urum
uun  Kulon-Pazeh  Kulon-Pazeh
uur  Ura (Vanuatu)  Ura (Vanuatu)
uuu  U  U
uve  Fagauvea  Fagauvea
uve  West Uvean  Uvean, West
uvh  Uri  Uri
uvl  Lote  Lote
uwa  Kuku-Uwanh  Kuku-Uwanh
uya  Doko-Uyanga  Doko-Uyanga
uzb  Uzbek  Uzbek
uzn  Northern Uzbek  Uzbek, Northern
uzs  Southern Uzbek  Uzbek, Southern
vaa  Vaagri Booli  Vaagri Booli
vae  Vale  Vale
vaf  Vafsi  Vafsi
vag  Vagla  Vagla
vah  Varhadi-Nagpuri  Varhadi-Nagpuri
vai  Vai  Vai
vaj  Vasekela Bushman  Vasekela Bushman
val  Vehes  Vehes
vam  Vanimo  Vanimo
van  Valman  Valman
vao  Vao  Vao
vap  Vaiphei  Vaiphei
var  Huarijio  Huarijio
vas  Vasavi  Vasavi
vau  Vanuma  Vanuma
vav  Varli  Varli
vay  Wayu  Wayu
vbb  Southeast Babar  Babar, Southeast
vbk  Southwestern Bontok  Bontok, Southwestern
vec  Venetian  Venetian
ved  Veddah  Veddah
vel  Veluws  Veluws
vem  Vemgo-Mabas  Vemgo-Mabas
ven  Venda  Venda
veo  Ventureño  Ventureño
vep  Veps  Veps
ver  Mom Jango  Mom Jango
vgr  Vaghri  Vaghri
vgt  Flemish Sign Language  Flemish Sign Language
vgt  Vlaamse Gebarentaal  Vlaamse Gebarentaal
vic  Virgin Islands Creole English  Creole English, Virgin Islands
vid  Vidunda  Vidunda
vie  Vietnamese  Vietnamese
vif  Vili  Vili
vig  Viemo  Viemo
vil  Vilela  Vilela
vin  Vinza  Vinza
vis  Vishavan  Vishavan
vit  Viti  Viti
viv  Iduna  Iduna
vka  Kariyarra  Kariyarra
vki  Ija-Zuba  Ija-Zuba
vkj  Kujarge  Kujarge
vkk  Kaur  Kaur
vkl  Kulisusu  Kulisusu
vkm  Kamakan  Kamakan
vko  Kodeoha  Kodeoha
vkp  Korlai Creole Portuguese  Creole Portuguese, Korlai
vkt  Tenggarong Kutai Malay  Malay, Tenggarong Kutai
vku  Kurrama  Kurrama
vlp  Valpei  Valpei
vls  Vlaams  Vlaams
vma  Martuyhunira  Martuyhunira
vmb  Barbaram  Barbaram
vmc  Juxtlahuaca Mixtec  Mixtec, Juxtlahuaca
vmd  Mudu Koraga  Koraga, Mudu
vme  East Masela  Masela, East
vmf  Mainfränkisch  Mainfränkisch
vmg  Lungalunga  Lungalunga
vmh  Maraghei  Maraghei
vmi  Miwa  Miwa
vmj  Ixtayutla Mixtec  Mixtec, Ixtayutla
vmk  Makhuwa-Shirima  Makhuwa-Shirima
vml  Malgana  Malgana
vmm  Mitlatongo Mixtec  Mixtec, Mitlatongo
vmp  Soyaltepec Mazatec  Mazatec, Soyaltepec
vmq  Soyaltepec Mixtec  Mixtec, Soyaltepec
vmr  Marenje  Marenje
vms  Moksela  Moksela
vmu  Muluridyi  Muluridyi
vmv  Valley Maidu  Maidu, Valley
vmw  Makhuwa  Makhuwa
vmx  Tamazola Mixtec  Mixtec, Tamazola
vmy  Ayautla Mazatec  Mazatec, Ayautla
vmz  Mazatlán Mazatec  Mazatec, Mazatlán
vnk  Lovono  Lovono
vnk  Vano  Vano
vnm  Neve'ei  Neve'ei
vnm  Vinmavis  Vinmavis
vnp  Vunapu  Vunapu
vol  Volapük  Volapük
vor  Voro  Voro
vot  Votic  Votic
vra  Vera'a  Vera'a
vro  Võro  Võro
vrs  Varisi  Varisi
vrt  Banam Bay  Banam Bay
vrt  Burmbar  Burmbar
vsi  Moldova Sign Language  Moldova Sign Language
vsl  Venezuelan Sign Language  Venezuelan Sign Language
vsv  Llengua de signes valenciana  Llengua de signes valenciana
vsv  Valencian Sign Language  Valencian Sign Language
vto  Vitou  Vitou
vum  Vumbu  Vumbu
vun  Vunjo  Vunjo
vut  Vute  Vute
vwa  Awa (China)  Awa (China)
waa  Walla Walla  Walla Walla
wab  Wab  Wab
wac  Wasco-Wishram  Wasco-Wishram
wad  Wandamen  Wandamen
wae  Walser  Walser
waf  Wakoná  Wakoná
wag  Wa'ema  Wa'ema
wah  Watubela  Watubela
wai  Wares  Wares
waj  Waffa  Waffa
wal  Wolaitta  Wolaitta
wal  Wolaytta  Wolaytta
wam  Wampanoag  Wampanoag
wan  Wan  Wan
wao  Wappo  Wappo
wap  Wapishana  Wapishana
waq  Wageman  Wageman
war  Waray (Philippines)  Waray (Philippines)
was  Washo  Washo
wat  Kaninuwa  Kaninuwa
wau  Waurá  Waurá
wav  Waka  Waka
waw  Waiwai  Waiwai
wax  Marangis  Marangis
wax  Watam  Watam
way  Wayana  Wayana
waz  Wampur  Wampur
wba  Warao  Warao
wbb  Wabo  Wabo
wbe  Waritai  Waritai
wbf  Wara  Wara
wbh  Wanda  Wanda
wbi  Vwanji  Vwanji
wbj  Alagwa  Alagwa
wbk  Waigali  Waigali
wbl  Wakhi  Wakhi
wbm  Wa  Wa
wbp  Warlpiri  Warlpiri
wbq  Waddar  Waddar
wbr  Wagdi  Wagdi
wbt  Wanman  Wanman
wbv  Wajarri  Wajarri
wbw  Woi  Woi
wca  Yanomámi  Yanomámi
wci  Waci Gbe  Gbe, Waci
wdd  Wandji  Wandji
wdg  Wadaginam  Wadaginam
wdj  Wadjiginy  Wadjiginy
wdk  Wadikali  Wadikali
wdu  Wadjigu  Wadjigu
wdy  Wadjabangayi  Wadjabangayi
wea  Wewaw  Wewaw
wec  Wè Western  Wè Western
wed  Wedau  Wedau
weg  Wergaia  Wergaia
weh  Weh  Weh
wei  Kiunum  Kiunum
wem  Weme Gbe  Gbe, Weme
weo  Wemale  Wemale
wep  Westphalien  Westphalien
wer  Weri  Weri
wes  Cameroon Pidgin  Pidgin, Cameroon
wet  Perai  Perai
weu  Rawngtu Chin  Chin, Rawngtu
wew  Wejewa  Wejewa
wfg  Yafi  Yafi
wfg  Zorop  Zorop
wga  Wagaya  Wagaya
wgb  Wagawaga  Wagawaga
wgg  Wangganguru  Wangganguru
wgi  Wahgi  Wahgi
wgo  Waigeo  Waigeo
wgu  Wirangu  Wirangu
wgy  Warrgamay  Warrgamay
wha  Manusela  Manusela
whg  North Wahgi  Wahgi, North
whk  Wahau Kenyah  Kenyah, Wahau
whu  Wahau Kayan  Kayan, Wahau
wib  Southern Toussian  Toussian, Southern
wic  Wichita  Wichita
wie  Wik-Epa  Wik-Epa
wif  Wik-Keyangan  Wik-Keyangan
wig  Wik-Ngathana  Wik-Ngathana
wih  Wik-Me'anha  Wik-Me'anha
wii  Minidien  Minidien
wij  Wik-Iiyanh  Wik-Iiyanh
wik  Wikalkan  Wikalkan
wil  Wilawila  Wilawila
wim  Wik-Mungkan  Wik-Mungkan
win  Ho-Chunk  Ho-Chunk
wir  Wiraféd  Wiraféd
wiu  Wiru  Wiru
wiv  Vitu  Vitu
wiy  Wiyot  Wiyot
wja  Waja  Waja
wji  Warji  Warji
wka  Kw'adza  Kw'adza
wkb  Kumbaran  Kumbaran
wkd  Mo  Mo
wkd  Wakde  Wakde
wkl  Kalanadi  Kalanadi
wku  Kunduvadi  Kunduvadi
wkw  Wakawaka  Wakawaka
wky  Wangkayutyuru  Wangkayutyuru
wla  Walio  Walio
wlc  Mwali Comorian  Comorian, Mwali
wle  Wolane  Wolane
wlg  Kunbarlang  Kunbarlang
wli  Waioli  Waioli
wlk  Wailaki  Wailaki
wll  Wali (Sudan)  Wali (Sudan)
wlm  Middle Welsh  Welsh, Middle
wln  Walloon  Walloon
wlo  Wolio  Wolio
wlr  Wailapa  Wailapa
wls  Wallisian  Wallisian
wlu  Wuliwuli  Wuliwuli
wlv  Wichí Lhamtés Vejoz  Wichí Lhamtés Vejoz
wlw  Walak  Walak
wlx  Wali (Ghana)  Wali (Ghana)
wly  Waling  Waling
wma  Mawa (Nigeria)  Mawa (Nigeria)
wmb  Wambaya  Wambaya
wmc  Wamas  Wamas
wmd  Mamaindé  Mamaindé
wme  Wambule  Wambule
wmh  Waima'a  Waima'a
wmi  Wamin  Wamin
wmm  Maiwa (Indonesia)  Maiwa (Indonesia)
wmn  Waamwang  Waamwang
wmo  Wom (Papua New Guinea)  Wom (Papua New Guinea)
wms  Wambon  Wambon
wmt  Walmajarri  Walmajarri
wmw  Mwani  Mwani
wmx  Womo  Womo
wnb  Wanambre  Wanambre
wnc  Wantoat  Wantoat
wnd  Wandarang  Wandarang
wne  Waneci  Waneci
wng  Wanggom  Wanggom
wni  Ndzwani Comorian  Comorian, Ndzwani
wnk  Wanukaka  Wanukaka
wnm  Wanggamala  Wanggamala
wnn  Wunumara  Wunumara
wno  Wano  Wano
wnp  Wanap  Wanap
wnu  Usan  Usan
wnw  Wintu  Wintu
wny  Wanyi  Wanyi
woa  Tyaraity  Tyaraity
wob  Wè Northern  Wè Northern
woc  Wogeo  Wogeo
wod  Wolani  Wolani
woe  Woleaian  Woleaian
wof  Gambian Wolof  Wolof, Gambian
wog  Wogamusin  Wogamusin
woi  Kamang  Kamang
wok  Longto  Longto
wol  Wolof  Wolof
wom  Wom (Nigeria)  Wom (Nigeria)
won  Wongo  Wongo
woo  Manombai  Manombai
wor  Woria  Woria
wos  Hanga Hundi  Hanga Hundi
wow  Wawonii  Wawonii
woy  Weyto  Weyto
wpc  Maco  Maco
wra  Warapu  Warapu
wrb  Warluwara  Warluwara
wrd  Warduji  Warduji
wrg  Warungu  Warungu
wrh  Wiradhuri  Wiradhuri
wri  Wariyangga  Wariyangga
wrk  Garrwa  Garrwa
wrl  Warlmanpa  Warlmanpa
wrm  Warumungu  Warumungu
wrn  Warnang  Warnang
wro  Worrorra  Worrorra
wrp  Waropen  Waropen
wrr  Wardaman  Wardaman
wrs  Waris  Waris
wru  Waru  Waru
wrv  Waruna  Waruna
wrw  Gugu Warra  Gugu Warra
wrx  Wae Rana  Wae Rana
wry  Merwari  Merwari
wrz  Waray (Australia)  Waray (Australia)
wsa  Warembori  Warembori
wsi  Wusi  Wusi
wsk  Waskia  Waskia
wsr  Owenia  Owenia
wss  Wasa  Wasa
wsu  Wasu  Wasu
wsv  Wotapuri-Katarqalai  Wotapuri-Katarqalai
wtf  Watiwa  Watiwa
wth  Wathawurrung  Wathawurrung
wti  Berta  Berta
wtk  Watakataui  Watakataui
wtm  Mewati  Mewati
wtw  Wotu  Wotu
wua  Wikngenchera  Wikngenchera
wub  Wunambal  Wunambal
wud  Wudu  Wudu
wuh  Wutunhua  Wutunhua
wul  Silimo  Silimo
wum  Wumbvu  Wumbvu
wun  Bungu  Bungu
wur  Wurrugu  Wurrugu
wut  Wutung  Wutung
wuu  Wu Chinese  Chinese, Wu
wuv  Wuvulu-Aua  Wuvulu-Aua
wux  Wulna  Wulna
wuy  Wauyai  Wauyai
wwa  Waama  Waama
wwb  Wakabunga  Wakabunga
wwo  Dorig  Dorig
wwo  Wetamut  Wetamut
wwr  Warrwa  Warrwa
www  Wawa  Wawa
wxa  Waxianghua  Waxianghua
wxw  Wardandi  Wardandi
wya  Wyandot  Wyandot
wyb  Wangaaybuwan-Ngiyambaa  Wangaaybuwan-Ngiyambaa
wyi  Woiwurrung  Woiwurrung
wym  Wymysorys  Wymysorys
wyr  Wayoró  Wayoró
wyy  Western Fijian  Fijian, Western
xaa  Andalusian Arabic  Arabic, Andalusian
xab  Sambe  Sambe
xac  Kachari  Kachari
xad  Adai  Adai
xae  Aequian  Aequian
xag  Aghwan  Aghwan
xai  Kaimbé  Kaimbé
xal  Kalmyk  Kalmyk
xal  Oirat  Oirat
xam  /Xam  /Xam
xan  Xamtanga  Xamtanga
xao  Khao  Khao
xap  Apalachee  Apalachee
xaq  Aquitanian  Aquitanian
xar  Karami  Karami
xas  Kamas  Kamas
xat  Katawixi  Katawixi
xau  Kauwera  Kauwera
xav  Xavánte  Xavánte
xaw  Kawaiisu  Kawaiisu
xay  Kayan Mahakam  Kayan Mahakam
xba  Kamba (Brazil)  Kamba (Brazil)
xbb  Lower Burdekin  Burdekin, Lower
xbc  Bactrian  Bactrian
xbd  Bindal  Bindal
xbe  Bigambal  Bigambal
xbg  Bunganditj  Bunganditj
xbi  Kombio  Kombio
xbj  Birrpayi  Birrpayi
xbm  Middle Breton  Breton, Middle
xbn  Kenaboi  Kenaboi
xbo  Bolgarian  Bolgarian
xbp  Bibbulman  Bibbulman
xbr  Kambera  Kambera
xbw  Kambiwá  Kambiwá
xbx  Kabixí  Kabixí
xby  Batyala  Batyala
xcb  Cumbric  Cumbric
xcc  Camunic  Camunic
xce  Celtiberian  Celtiberian
xcg  Cisalpine Gaulish  Gaulish, Cisalpine
xch  Chemakum  Chemakum
xch  Chimakum  Chimakum
xcl  Classical Armenian  Armenian, Classical
xcm  Comecrudo  Comecrudo
xcn  Cotoname  Cotoname
xco  Chorasmian  Chorasmian
xcr  Carian  Carian
xct  Classical Tibetan  Tibetan, Classical
xcu  Curonian  Curonian
xcv  Chuvantsy  Chuvantsy
xcw  Coahuilteco  Coahuilteco
xcy  Cayuse  Cayuse
xda  Darkinyung  Darkinyung
xdc  Dacian  Dacian
xdk  Dharuk  Dharuk
xdm  Edomite  Edomite
xdy  Malayic Dayak  Dayak, Malayic
xeb  Eblan  Eblan
xed  Hdi  Hdi
xeg  //Xegwi  //Xegwi
xel  Kelo  Kelo
xem  Kembayan  Kembayan
xep  Epi-Olmec  Epi-Olmec
xer  Xerénte  Xerénte
xes  Kesawai  Kesawai
xet  Xetá  Xetá
xeu  Keoru-Ahia  Keoru-Ahia
xfa  Faliscan  Faliscan
xga  Galatian  Galatian
xgb  Gbin  Gbin
xgd  Gudang  Gudang
xgf  Gabrielino-Fernandeño  Gabrielino-Fernandeño
xgg  Goreng  Goreng
xgi  Garingbal  Garingbal
xgl  Galindan  Galindan
xgm  Guwinmal  Guwinmal
xgr  Garza  Garza
xgu  Unggumi  Unggumi
xgw  Guwa  Guwa
xha  Harami  Harami
xhc  Hunnic  Hunnic
xhd  Hadrami  Hadrami
xhe  Khetrani  Khetrani
xho  Xhosa  Xhosa
xhr  Hernican  Hernican
xht  Hattic  Hattic
xhu  Hurrian  Hurrian
xhv  Khua  Khua
xib  Iberian  Iberian
xii  Xiri  Xiri
xil  Illyrian  Illyrian
xin  Xinca  Xinca
xip  Xipináwa  Xipináwa
xir  Xiriâna  Xiriâna
xiv  Indus Valley Language  Indus Valley Language
xiy  Xipaya  Xipaya
xjb  Minjungbal  Minjungbal
xjt  Jaitmatang  Jaitmatang
xka  Kalkoti  Kalkoti
xkb  Northern Nago  Nago, Northern
xkc  Kho'ini  Kho'ini
xkd  Mendalam Kayan  Kayan, Mendalam
xke  Kereho  Kereho
xkf  Khengkha  Khengkha
xkg  Kagoro  Kagoro
xkh  Karahawyana  Karahawyana
xki  Kenyan Sign Language  Kenyan Sign Language
xkj  Kajali  Kajali
xkk  Kaco'  Kaco'
xkl  Mainstream Kenyah  Mainstream Kenyah
xkn  Kayan River Kayan  Kayan, Kayan River
xko  Kiorr  Kiorr
xkp  Kabatei  Kabatei
xkq  Koroni  Koroni
xkr  Xakriabá  Xakriabá
xks  Kumbewaha  Kumbewaha
xkt  Kantosi  Kantosi
xku  Kaamba  Kaamba
xkv  Kgalagadi  Kgalagadi
xkw  Kembra  Kembra
xkx  Karore  Karore
xky  Uma' Lasan  Uma' Lasan
xkz  Kurtokha  Kurtokha
xla  Kamula  Kamula
xlb  Loup B  Loup B
xlc  Lycian  Lycian
xld  Lydian  Lydian
xle  Lemnian  Lemnian
xlg  Ligurian (Ancient)  Ligurian (Ancient)
xli  Liburnian  Liburnian
xln  Alanic  Alanic
xlo  Loup A  Loup A
xlp  Lepontic  Lepontic
xls  Lusitanian  Lusitanian
xlu  Cuneiform Luwian  Luwian, Cuneiform
xly  Elymian  Elymian
xma  Mushungulu  Mushungulu
xmb  Mbonga  Mbonga
xmc  Makhuwa-Marrevone  Makhuwa-Marrevone
xmd  Mbudum  Mbudum
xme  Median  Median
xmf  Mingrelian  Mingrelian
xmg  Mengaka  Mengaka
xmh  Kuku-Muminh  Kuku-Muminh
xmj  Majera  Majera
xmk  Ancient Macedonian  Macedonian, Ancient
xml  Malaysian Sign Language  Malaysian Sign Language
xmm  Manado Malay  Malay, Manado
xmn  Manichaean Middle Persian  Persian, Manichaean Middle
xmo  Morerebi  Morerebi
xmp  Kuku-Mu'inh  Kuku-Mu'inh
xmq  Kuku-Mangk  Kuku-Mangk
xmr  Meroitic  Meroitic
xms  Moroccan Sign Language  Moroccan Sign Language
xmt  Matbat  Matbat
xmu  Kamu  Kamu
xmv  Antankarana Malagasy  Malagasy, Antankarana
xmv  Tankarana Malagasy  Malagasy, Tankarana
xmw  Tsimihety Malagasy  Malagasy, Tsimihety
xmx  Maden  Maden
xmy  Mayaguduna  Mayaguduna
xmz  Mori Bawah  Mori Bawah
xna  Ancient North Arabian  North Arabian, Ancient
xnb  Kanakanabu  Kanakanabu
xng  Middle Mongolian  Mongolian, Middle
xnh  Kuanhua  Kuanhua
xni  Ngarigu  Ngarigu
xnk  Nganakarti  Nganakarti
xnn  Northern Kankanay  Kankanay, Northern
xno  Anglo-Norman  Anglo-Norman
xnr  Kangri  Kangri
xns  Kanashi  Kanashi
xnt  Narragansett  Narragansett
xnu  Nukunul  Nukunul
xny  Nyiyaparli  Nyiyaparli
xnz  Kenzi  Kenzi
xnz  Mattoki  Mattoki
xoc  O'chi'chi'  O'chi'chi'
xod  Kokoda  Kokoda
xog  Soga  Soga
xoi  Kominimung  Kominimung
xok  Xokleng  Xokleng
xom  Komo (Sudan)  Komo (Sudan)
xon  Konkomba  Konkomba
xoo  Xukurú  Xukurú
xop  Kopar  Kopar
xor  Korubo  Korubo
xow  Kowaki  Kowaki
xpa  Pirriya  Pirriya
xpc  Pecheneg  Pecheneg
xpe  Liberia Kpelle  Kpelle, Liberia
xpg  Phrygian  Phrygian
xpi  Pictish  Pictish
xpj  Mpalitjanh  Mpalitjanh
xpk  Kulina Pano  Pano, Kulina
xpm  Pumpokol  Pumpokol
xpn  Kapinawá  Kapinawá
xpo  Pochutec  Pochutec
xpp  Puyo-Paekche  Puyo-Paekche
xpq  Mohegan-Pequot  Mohegan-Pequot
xpr  Parthian  Parthian
xps  Pisidian  Pisidian
xpt  Punthamara  Punthamara
xpu  Punic  Punic
xpy  Puyo  Puyo
xqa  Karakhanid  Karakhanid
xqt  Qatabanian  Qatabanian
xra  Krahô  Krahô
xrb  Eastern Karaboro  Karaboro, Eastern
xrd  Gundungurra  Gundungurra
xre  Kreye  Kreye
xrg  Minang  Minang
xri  Krikati-Timbira  Krikati-Timbira
xrm  Armazic  Armazic
xrn  Arin  Arin
xrq  Karranga  Karranga
xrr  Raetic  Raetic
xrt  Aranama-Tamique  Aranama-Tamique
xru  Marriammu  Marriammu
xrw  Karawa  Karawa
xsa  Sabaean  Sabaean
xsb  Sambal  Sambal
xsc  Scythian  Scythian
xsd  Sidetic  Sidetic
xse  Sempan  Sempan
xsh  Shamang  Shamang
xsi  Sio  Sio
xsj  Subi  Subi
xsl  South Slavey  Slavey, South
xsm  Kasem  Kasem
xsn  Sanga (Nigeria)  Sanga (Nigeria)
xso  Solano  Solano
xsp  Silopi  Silopi
xsq  Makhuwa-Saka  Makhuwa-Saka
xsr  Sherpa  Sherpa
xss  Assan  Assan
xsu  Sanumá  Sanumá
xsv  Sudovian  Sudovian
xsy  Saisiyat  Saisiyat
xta  Alcozauca Mixtec  Mixtec, Alcozauca
xtb  Chazumba Mixtec  Mixtec, Chazumba
xtc  Katcha-Kadugli-Miri  Katcha-Kadugli-Miri
xtd  Diuxi-Tilantongo Mixtec  Mixtec, Diuxi-Tilantongo
xte  Ketengban  Ketengban
xtg  Transalpine Gaulish  Gaulish, Transalpine
xth  Yitha Yitha  Yitha Yitha
xti  Sinicahua Mixtec  Mixtec, Sinicahua
xtj  San Juan Teita Mixtec  Mixtec, San Juan Teita
xtl  Tijaltepec Mixtec  Mixtec, Tijaltepec
xtm  Magdalena Peñasco Mixtec  Mixtec, Magdalena Peñasco
xtn  Northern Tlaxiaco Mixtec  Mixtec, Northern Tlaxiaco
xto  Tokharian A  Tokharian A
xtp  San Miguel Piedras Mixtec  Mixtec, San Miguel Piedras
xtq  Tumshuqese  Tumshuqese
xtr  Early Tripuri  Tripuri, Early
xts  Sindihui Mixtec  Mixtec, Sindihui
xtt  Tacahua Mixtec  Mixtec, Tacahua
xtu  Cuyamecalco Mixtec  Mixtec, Cuyamecalco
xtv  Thawa  Thawa
xtw  Tawandê  Tawandê
xty  Yoloxochitl Mixtec  Mixtec, Yoloxochitl
xtz  Tasmanian  Tasmanian
xua  Alu Kurumba  Kurumba, Alu
xub  Betta Kurumba  Kurumba, Betta
xud  Umiida  Umiida
xug  Kunigami  Kunigami
xuj  Jennu Kurumba  Kurumba, Jennu
xul  Ngunawal  Ngunawal
xum  Umbrian  Umbrian
xun  Unggaranggu  Unggaranggu
xuo  Kuo  Kuo
xup  Upper Umpqua  Umpqua, Upper
xur  Urartian  Urartian
xut  Kuthant  Kuthant
xuu  Kxoe  Kxoe
xve  Venetic  Venetic
xvi  Kamviri  Kamviri
xvn  Vandalic  Vandalic
xvo  Volscian  Volscian
xvs  Vestinian  Vestinian
xwa  Kwaza  Kwaza
xwc  Woccon  Woccon
xwd  Wadi Wadi  Wadi Wadi
xwe  Xwela Gbe  Gbe, Xwela
xwg  Kwegu  Kwegu
xwj  Wajuk  Wajuk
xwk  Wangkumara  Wangkumara
xwl  Western Xwla Gbe  Gbe, Western Xwla
xwo  Written Oirat  Oirat, Written
xwr  Kwerba Mamberamo  Kwerba Mamberamo
xwt  Wotjobaluk  Wotjobaluk
xww  Wemba Wemba  Wemba Wemba
xxb  Boro (Ghana)  Boro (Ghana)
xxk  Ke'o  Ke'o
xxm  Minkin  Minkin
xxr  Koropó  Koropó
xxt  Tambora  Tambora
xya  Yaygir  Yaygir
xyb  Yandjibara  Yandjibara
xyj  Mayi-Yapi  Mayi-Yapi
xyk  Mayi-Kulan  Mayi-Kulan
xyl  Yalakalore  Yalakalore
xyt  Mayi-Thakurti  Mayi-Thakurti
xyy  Yorta Yorta  Yorta Yorta
xzh  Zhang-Zhung  Zhang-Zhung
xzm  Zemgalian  Zemgalian
xzp  Ancient Zapotec  Zapotec, Ancient
yaa  Yaminahua  Yaminahua
yab  Yuhup  Yuhup
yac  Pass Valley Yali  Yali, Pass Valley
yad  Yagua  Yagua
yae  Pumé  Pumé
yaf  Yaka (Democratic Republic of Congo)  Yaka (Democratic Republic of Congo)
yag  Yámana  Yámana
yah  Yazgulyam  Yazgulyam
yai  Yagnobi  Yagnobi
yaj  Banda-Yangere  Banda-Yangere
yak  Yakama  Yakama
yal  Yalunka  Yalunka
yam  Yamba  Yamba
yan  Mayangna  Mayangna
yao  Yao  Yao
yap  Yapese  Yapese
yaq  Yaqui  Yaqui
yar  Yabarana  Yabarana
yas  Nugunu (Cameroon)  Nugunu (Cameroon)
yat  Yambeta  Yambeta
yau  Yuwana  Yuwana
yav  Yangben  Yangben
yaw  Yawalapití  Yawalapití
yax  Yauma  Yauma
yay  Agwagwune  Agwagwune
yaz  Lokaa  Lokaa
yba  Yala  Yala
ybb  Yemba  Yemba
ybe  West Yugur  Yugur, West
ybh  Yakha  Yakha
ybi  Yamphu  Yamphu
ybj  Hasha  Hasha
ybk  Bokha  Bokha
ybl  Yukuben  Yukuben
ybm  Yaben  Yaben
ybn  Yabaâna  Yabaâna
ybo  Yabong  Yabong
ybx  Yawiyo  Yawiyo
yby  Yaweyuha  Yaweyuha
ych  Chesu  Chesu
ycl  Lolopo  Lolopo
ycn  Yucuna  Yucuna
ycp  Chepya  Chepya
yda  Yanda  Yanda
ydd  Eastern Yiddish  Yiddish, Eastern
yde  Yangum Dey  Yangum Dey
ydg  Yidgha  Yidgha
ydk  Yoidik  Yoidik
yds  Yiddish Sign Language  Yiddish Sign Language
yea  Ravula  Ravula
yec  Yeniche  Yeniche
yee  Yimas  Yimas
yei  Yeni  Yeni
yej  Yevanic  Yevanic
yel  Yela  Yela
yer  Tarok  Tarok
yes  Nyankpa  Nyankpa
yet  Yetfa  Yetfa
yeu  Yerukula  Yerukula
yev  Yapunda  Yapunda
yey  Yeyi  Yeyi
yga  Malyangapa  Malyangapa
ygi  Yiningayi  Yiningayi
ygl  Yangum Gel  Yangum Gel
ygm  Yagomi  Yagomi
ygp  Gepo  Gepo
ygr  Yagaria  Yagaria
ygu  Yugul  Yugul
ygw  Yagwoia  Yagwoia
yha  Baha Buyang  Buyang, Baha
yhd  Judeo-Iraqi Arabic  Arabic, Judeo-Iraqi
yhl  Hlepho Phowa  Phowa, Hlepho
yia  Yinggarda  Yinggarda
yid  Yiddish  Yiddish
yif  Ache  Ache
yig  Wusa Nasu  Nasu, Wusa
yih  Western Yiddish  Yiddish, Western
yii  Yidiny  Yidiny
yij  Yindjibarndi  Yindjibarndi
yik  Dongshanba Lalo  Lalo, Dongshanba
yil  Yindjilandji  Yindjilandji
yim  Yimchungru Naga  Naga, Yimchungru
yin  Yinchia  Yinchia
yip  Pholo  Pholo
yiq  Miqie  Miqie
yir  North Awyu  Awyu, North
yis  Yis  Yis
yit  Eastern Lalu  Lalu, Eastern
yiu  Awu  Awu
yiv  Northern Nisu  Nisu, Northern
yix  Axi Yi  Yi, Axi
yiz  Azhe  Azhe
yka  Yakan  Yakan
ykg  Northern Yukaghir  Yukaghir, Northern
yki  Yoke  Yoke
ykk  Yakaikeke  Yakaikeke
ykl  Khlula  Khlula
ykm  Kap  Kap
ykn  Kua-nsi  Kua-nsi
yko  Yasa  Yasa
ykr  Yekora  Yekora
ykt  Kathu  Kathu
yku  Kuamasi  Kuamasi
yky  Yakoma  Yakoma
yla  Yaul  Yaul
ylb  Yaleba  Yaleba
yle  Yele  Yele
ylg  Yelogu  Yelogu
yli  Angguruk Yali  Yali, Angguruk
yll  Yil  Yil
ylm  Limi  Limi
yln  Langnian Buyang  Buyang, Langnian
ylo  Naluo Yi  Yi, Naluo
ylr  Yalarnnga  Yalarnnga
ylu  Aribwaung  Aribwaung
yly  Nyâlayu  Nyâlayu
yly  Nyelâyu  Nyelâyu
ymb  Yambes  Yambes
ymc  Southern Muji  Muji, Southern
ymd  Muda  Muda
yme  Yameo  Yameo
ymg  Yamongeri  Yamongeri
ymh  Mili  Mili
ymi  Moji  Moji
ymk  Makwe  Makwe
yml  Iamalele  Iamalele
ymm  Maay  Maay
ymn  Sunum  Sunum
ymn  Yamna  Yamna
ymo  Yangum Mon  Yangum Mon
ymp  Yamap  Yamap
ymq  Qila Muji  Muji, Qila
ymr  Malasar  Malasar
yms  Mysian  Mysian
ymt  Mator-Taygi-Karagas  Mator-Taygi-Karagas
ymx  Northern Muji  Muji, Northern
ymz  Muzi  Muzi
yna  Aluo  Aluo
ynd  Yandruwandha  Yandruwandha
yne  Lang'e  Lang'e
yng  Yango  Yango
ynh  Yangho  Yangho
ynk  Naukan Yupik  Yupik, Naukan
ynl  Yangulam  Yangulam
ynn  Yana  Yana
yno  Yong  Yong
ynq  Yendang  Yendang
yns  Yansi  Yansi
ynu  Yahuna  Yahuna
yob  Yoba  Yoba
yog  Yogad  Yogad
yoi  Yonaguni  Yonaguni
yok  Yokuts  Yokuts
yol  Yola  Yola
yom  Yombe  Yombe
yon  Yongkom  Yongkom
yor  Yoruba  Yoruba
yot  Yotti  Yotti
yox  Yoron  Yoron
yoy  Yoy  Yoy
ypa  Phala  Phala
ypb  Labo Phowa  Phowa, Labo
ypg  Phola  Phola
yph  Phupha  Phupha
ypm  Phuma  Phuma
ypn  Ani Phowa  Phowa, Ani
ypo  Alo Phola  Phola, Alo
ypp  Phupa  Phupa
ypz  Phuza  Phuza
yra  Yerakai  Yerakai
yrb  Yareba  Yareba
yre  Yaouré  Yaouré
yri  Yarí  Yarí
yrk  Nenets  Nenets
yrl  Nhengatu  Nhengatu
yrm  Yirrk-Mel  Yirrk-Mel
yrn  Yerong  Yerong
yrs  Yarsun  Yarsun
yrw  Yarawata  Yarawata
yry  Yarluyandi  Yarluyandi
ysc  Yassic  Yassic
ysd  Samatao  Samatao
ysg  Sonaga  Sonaga
ysl  Yugoslavian Sign Language  Yugoslavian Sign Language
ysn  Sani  Sani
yso  Nisi (China)  Nisi (China)
ysp  Southern Lolopo  Lolopo, Southern
ysr  Sirenik Yupik  Yupik, Sirenik
yss  Yessan-Mayo  Yessan-Mayo
ysy  Sanie  Sanie
yta  Talu  Talu
ytl  Tanglang  Tanglang
ytp  Thopho  Thopho
ytw  Yout Wam  Yout Wam
yty  Yatay  Yatay
yua  Yucatec Maya  Maya, Yucatec
yua  Yucateco  Yucateco
yub  Yugambal  Yugambal
yuc  Yuchi  Yuchi
yud  Judeo-Tripolitanian Arabic  Arabic, Judeo-Tripolitanian
yue  Yue Chinese  Chinese, Yue
yuf  Havasupai-Walapai-Yavapai  Havasupai-Walapai-Yavapai
yug  Yug  Yug
yui  Yurutí  Yurutí
yuj  Karkar-Yuri  Karkar-Yuri
yuk  Yuki  Yuki
yul  Yulu  Yulu
yum  Quechan  Quechan
yun  Bena (Nigeria)  Bena (Nigeria)
yup  Yukpa  Yukpa
yuq  Yuqui  Yuqui
yur  Yurok  Yurok
yut  Yopno  Yopno
yuu  Yugh  Yugh
yuw  Yau (Morobe Province)  Yau (Morobe Province)
yux  Southern Yukaghir  Yukaghir, Southern
yuy  East Yugur  Yugur, East
yuz  Yuracare  Yuracare
yva  Yawa  Yawa
yvt  Yavitero  Yavitero
ywa  Kalou  Kalou
ywg  Yinhawangka  Yinhawangka
ywl  Western Lalu  Lalu, Western
ywn  Yawanawa  Yawanawa
ywq  Wuding-Luquan Yi  Yi, Wuding-Luquan
ywr  Yawuru  Yawuru
ywt  Central Lalo  Lalo, Central
ywt  Xishanba Lalo  Lalo, Xishanba
ywu  Wumeng Nasu  Nasu, Wumeng
yww  Yawarawarga  Yawarawarga
yxa  Mayawali  Mayawali
yxg  Yagara  Yagara
yxl  Yardliyawarra  Yardliyawarra
yxm  Yinwum  Yinwum
yxu  Yuyu  Yuyu
yxy  Yabula Yabula  Yabula Yabula
yyr  Yir Yoront  Yir Yoront
yyu  Yau (Sandaun Province)  Yau (Sandaun Province)
yyz  Ayizi  Ayizi
yzg  E'ma Buyang  Buyang, E'ma
yzk  Zokhuo  Zokhuo
zaa  Sierra de Juárez Zapotec  Zapotec, Sierra de Juárez
zab  San Juan Guelavía Zapotec  Zapotec, San Juan Guelavía
zac  Ocotlán Zapotec  Zapotec, Ocotlán
zad  Cajonos Zapotec  Zapotec, Cajonos
zae  Yareni Zapotec  Zapotec, Yareni
zaf  Ayoquesco Zapotec  Zapotec, Ayoquesco
zag  Zaghawa  Zaghawa
zah  Zangwal  Zangwal
zai  Isthmus Zapotec  Zapotec, Isthmus
zaj  Zaramo  Zaramo
zak  Zanaki  Zanaki
zal  Zauzou  Zauzou
zam  Miahuatlán Zapotec  Zapotec, Miahuatlán
zao  Ozolotepec Zapotec  Zapotec, Ozolotepec
zap  Zapotec  Zapotec
zaq  Aloápam Zapotec  Zapotec, Aloápam
zar  Rincón Zapotec  Zapotec, Rincón
zas  Santo Domingo Albarradas Zapotec  Zapotec, Santo Domingo Albarradas
zat  Tabaa Zapotec  Zapotec, Tabaa
zau  Zangskari  Zangskari
zav  Yatzachi Zapotec  Zapotec, Yatzachi
zaw  Mitla Zapotec  Zapotec, Mitla
zax  Xadani Zapotec  Zapotec, Xadani
zay  Zaysete  Zaysete
zay  Zayse-Zergulla  Zayse-Zergulla
zaz  Zari  Zari
zbc  Central Berawan  Berawan, Central
zbe  East Berawan  Berawan, East
zbl  Bliss  Bliss
zbl  Blissymbolics  Blissymbolics
zbl  Blissymbols  Blissymbols
zbt  Batui  Batui
zbw  West Berawan  Berawan, West
zca  Coatecas Altas Zapotec  Zapotec, Coatecas Altas
zch  Central Hongshuihe Zhuang  Zhuang, Central Hongshuihe
zdj  Ngazidja Comorian  Comorian, Ngazidja
zea  Zeeuws  Zeeuws
zeg  Zenag  Zenag
zeh  Eastern Hongshuihe Zhuang  Zhuang, Eastern Hongshuihe
zen  Zenaga  Zenaga
zga  Kinga  Kinga
zgb  Guibei Zhuang  Zhuang, Guibei
zgh  Standard Moroccan Tamazight  Tamazight, Standard Moroccan
zgm  Minz Zhuang  Zhuang, Minz
zgn  Guibian Zhuang  Zhuang, Guibian
zgr  Magori  Magori
zha  Chuang  Chuang
zha  Zhuang  Zhuang
zhb  Zhaba  Zhaba
zhd  Dai Zhuang  Zhuang, Dai
zhi  Zhire  Zhire
zhn  Nong Zhuang  Zhuang, Nong
zho  Chinese  Chinese
zhw  Zhoa  Zhoa
zia  Zia  Zia
zib  Zimbabwe Sign Language  Zimbabwe Sign Language
zik  Zimakani  Zimakani
zil  Zialo  Zialo
zim  Mesme  Mesme
zin  Zinza  Zinza
zir  Ziriya  Ziriya
ziw  Zigula  Zigula
ziz  Zizilivakan  Zizilivakan
zka  Kaimbulawa  Kaimbulawa
zkb  Koibal  Koibal
zkd  Kadu  Kadu
zkg  Koguryo  Koguryo
zkh  Khorezmian  Khorezmian
zkk  Karankawa  Karankawa
zkn  Kanan  Kanan
zko  Kott  Kott
zkp  São Paulo Kaingáng  Kaingáng, São Paulo
zkr  Zakhring  Zakhring
zkt  Kitan  Kitan
zku  Kaurna  Kaurna
zkv  Krevinian  Krevinian
zkz  Khazar  Khazar
zlj  Liujiang Zhuang  Zhuang, Liujiang
zlm  Malay (individual language)  Malay (individual language)
zln  Lianshan Zhuang  Zhuang, Lianshan
zlq  Liuqian Zhuang  Zhuang, Liuqian
zma  Manda (Australia)  Manda (Australia)
zmb  Zimba  Zimba
zmc  Margany  Margany
zmd  Maridan  Maridan
zme  Mangerr  Mangerr
zmf  Mfinu  Mfinu
zmg  Marti Ke  Marti Ke
zmh  Makolkol  Makolkol
zmi  Negeri Sembilan Malay  Negeri Sembilan Malay
zmj  Maridjabin  Maridjabin
zmk  Mandandanyi  Mandandanyi
zml  Madngele  Madngele
zmm  Marimanindji  Marimanindji
zmn  Mbangwe  Mbangwe
zmo  Molo  Molo
zmp  Mpuono  Mpuono
zmq  Mituku  Mituku
zmr  Maranunggu  Maranunggu
zms  Mbesa  Mbesa
zmt  Maringarr  Maringarr
zmu  Muruwari  Muruwari
zmv  Mbariman-Gudhinma  Mbariman-Gudhinma
zmw  Mbo (Democratic Republic of Congo)  Mbo (Democratic Republic of Congo)
zmx  Bomitaba  Bomitaba
zmy  Mariyedi  Mariyedi
zmz  Mbandja  Mbandja
zna  Zan Gula  Zan Gula
zne  Zande (individual language)  Zande (individual language)
zng  Mang  Mang
znk  Manangkari  Manangkari
zns  Mangas  Mangas
zoc  Copainalá Zoque  Zoque, Copainalá
zoh  Chimalapa Zoque  Zoque, Chimalapa
zom  Zou  Zou
zoo  Asunción Mixtepec Zapotec  Zapotec, Asunción Mixtepec
zoq  Tabasco Zoque  Zoque, Tabasco
zor  Rayón Zoque  Zoque, Rayón
zos  Francisco León Zoque  Zoque, Francisco León
zpa  Lachiguiri Zapotec  Zapotec, Lachiguiri
zpb  Yautepec Zapotec  Zapotec, Yautepec
zpc  Choapan Zapotec  Zapotec, Choapan
zpd  Southeastern Ixtlán Zapotec  Zapotec, Southeastern Ixtlán
zpe  Petapa Zapotec  Zapotec, Petapa
zpf  San Pedro Quiatoni Zapotec  Zapotec, San Pedro Quiatoni
zpg  Guevea De Humboldt Zapotec  Zapotec, Guevea De Humboldt
zph  Totomachapan Zapotec  Zapotec, Totomachapan
zpi  Santa María Quiegolani Zapotec  Zapotec, Santa María Quiegolani
zpj  Quiavicuzas Zapotec  Zapotec, Quiavicuzas
zpk  Tlacolulita Zapotec  Zapotec, Tlacolulita
zpl  Lachixío Zapotec  Zapotec, Lachixío
zpm  Mixtepec Zapotec  Zapotec, Mixtepec
zpn  Santa Inés Yatzechi Zapotec  Zapotec, Santa Inés Yatzechi
zpo  Amatlán Zapotec  Zapotec, Amatlán
zpp  El Alto Zapotec  Zapotec, El Alto
zpq  Zoogocho Zapotec  Zapotec, Zoogocho
zpr  Santiago Xanica Zapotec  Zapotec, Santiago Xanica
zps  Coatlán Zapotec  Zapotec, Coatlán
zpt  San Vicente Coatlán Zapotec  Zapotec, San Vicente Coatlán
zpu  Yalálag Zapotec  Zapotec, Yalálag
zpv  Chichicapan Zapotec  Zapotec, Chichicapan
zpw  Zaniza Zapotec  Zapotec, Zaniza
zpx  San Baltazar Loxicha Zapotec  Zapotec, San Baltazar Loxicha
zpy  Mazaltepec Zapotec  Zapotec, Mazaltepec
zpz  Texmelucan Zapotec  Zapotec, Texmelucan
zqe  Qiubei Zhuang  Zhuang, Qiubei
zra  Kara (Korea)  Kara (Korea)
zrg  Mirgan  Mirgan
zrn  Zerenkel  Zerenkel
zro  Záparo  Záparo
zrp  Zarphatic  Zarphatic
zrs  Mairasi  Mairasi
zsa  Sarasira  Sarasira
zsk  Kaskean  Kaskean
zsl  Zambian Sign Language  Zambian Sign Language
zsm  Standard Malay  Malay, Standard
zsr  Southern Rincon Zapotec  Zapotec, Southern Rincon
zsu  Sukurum  Sukurum
zte  Elotepec Zapotec  Zapotec, Elotepec
ztg  Xanaguía Zapotec  Zapotec, Xanaguía
ztl  Lapaguía-Guivini Zapotec  Zapotec, Lapaguía-Guivini
ztm  San Agustín Mixtepec Zapotec  Zapotec, San Agustín Mixtepec
ztn  Santa Catarina Albarradas Zapotec  Zapotec, Santa Catarina Albarradas
ztp  Loxicha Zapotec  Zapotec, Loxicha
ztq  Quioquitani-Quierí Zapotec  Zapotec, Quioquitani-Quierí
zts  Tilquiapan Zapotec  Zapotec, Tilquiapan
ztt  Tejalapan Zapotec  Zapotec, Tejalapan
ztu  Güilá Zapotec  Zapotec, Güilá
ztx  Zaachila Zapotec  Zapotec, Zaachila
zty  Yatee Zapotec  Zapotec, Yatee
zua  Zeem  Zeem
zuh  Tokano  Tokano
zul  Zulu  Zulu
zum  Kumzari  Kumzari
zun  Zuni  Zuni
zuy  Zumaya  Zumaya
zwa  Zay  Zay
zxx  No linguistic content  No linguistic content
zxx  Not applicable  Not applicable
zyb  Yongbei Zhuang  Zhuang, Yongbei
zyg  Yang Zhuang  Zhuang, Yang
zyj  Youjiang Zhuang  Zhuang, Youjiang
zyn  Yongnan Zhuang  Zhuang, Yongnan
zyp  Zyphe Chin  Chin, Zyphe
zza  Dimili  Dimili
zza  Dimli (macrolanguage)  Dimli (macrolanguage)
zza  Kirdki  Kirdki
zza  Kirmanjki (macrolanguage)  Kirmanjki (macrolanguage)
zza  Zaza  Zaza
zza  Zazaki  Zazaki
zzj  Zuojiang Zhuang  Zhuang, Zuojiang"""

# from http://www-01.sil.org/iso639-3/iso-639-3_Retirements.tab
retired_iso6393 = """Id  Ref_Name  Ret_Reason  Change_To  Ret_Remedy  Effective
fri  Western Frisian  C  fry    2007-02-01
auv  Auvergnat  M  oci    2007-03-14
gsc  Gascon  M  oci    2007-03-14
lms  Limousin  M  oci    2007-03-14
lnc  Languedocien  M  oci    2007-03-14
prv  Provençal  M  oci    2007-03-14
amd  Amapá Creole  N      2007-07-18
bgh  Bogan  D  bbh    2007-07-18
bnh  Banawá  M  jaa    2007-07-18
bvs  Belgian Sign Language  S    Split into Langue des signes de Belgique Francophone [sfb], and Vlaamse Gebarentaal [vgt]  2007-07-18
ccy  Southern Zhuang  S    Split into five languages: Nong Zhuang [zhn];  Yang Zhuang [zyg]; Yongnan Zhuang [zyn]; Zuojiang Zhuang [zzj]; Dai Zhuang [zhd].  2007-07-18
cit  Chittagonian  S    Split into Rohingya [rhg], and Chittagonian (new identifier [ctg])  2007-07-18
flm  Falam Chin  S    Split into Ranglong [rnl], and Falam Chin (new identifier [cfm]).  2007-07-18
jap  Jaruára  M  jaa    2007-07-18
kob  Kohoroxitari  M  xsu    2007-07-18
mob  Moinba  S    Split into five languages: Chug [cvg]; Lish [lsh];  Kalaktang Monpa [kkf]; Tawang Monpa [twm]; Sartang [onp]  2007-07-18
mzf  Aiku  S    Split into four languages: Ambrak [aag]; Yangum Dey [yde]; Yangum Gel [ygl]; Yangum Mon [ymo]  2007-07-18
nhj  Tlalitzlipa Nahuatl  M  nhi    2007-07-18
nhs  Southeastern Puebla Nahuatl  S    Split into Sierra Negra Nahuatl [nsu] and Southeastern Puebla Nahuatl [npl]  2007-07-18
occ  Occidental  D  ile    2007-07-18
tmx  Tomyang  M  ybi    2007-07-18
tot  Patla-Chicontla Totonac  S    Split into Upper Necaxa Totonac [tku] and Tecpatlán Totonac [tcw]  2007-07-18
xmi  Miarrã  N      2007-07-18
yib  Yinglish  M  eng    2007-07-18
ztc  Lachirioag Zapotec  M  zty    2007-07-18
atf  Atuence  N      2007-08-10
bqe  Navarro-Labourdin Basque  M  eus    2007-08-10
bsz  Souletin Basque  M  eus    2007-08-10
aex  Amerax  M  eng    2008-01-14
ahe  Ahe  M  knx    2008-01-14
aiz  Aari  S    Split into Aari [aiw] (new identifier) and Gayil [gyl]  2008-01-14
akn  Amikoana  N      2008-01-14
arf  Arafundi  S    Split into three languages: Andai [afd]; Nanubae [afk]; Tapei [afp]  2008-01-14
azr  Adzera  S    Split into three languages: Adzera [adz] (new identifier), Sukurum [zsu] and Sarasira [zsa]  2008-01-14
bcx  Pamona  S    Split into Pamona [pmf] (new identifier) and Batui [zbt]  2008-01-14
bii  Bisu  S    Split into Bisu [bzi] (new identifier) and Laomian [lwm]  2008-01-14
bke  Bengkulu  M  pse    2008-01-14
blu  Hmong Njua  S    Split into four languages: Hmong Njua [hnj] (new identifier); Chuanqiandian Cluster Miao [cqd]; Horned Miao [hrm]; Small Flowery Miao [sfm]  2008-01-14
boc  Bakung Kenyah  M  xkl    2008-01-14
bsd  Sarawak Bisaya  M  bsb    2008-01-14
bwv  Bahau River Kenyah  N      2008-01-14
bxt  Buxinhua  D  bgk    2008-01-14
byu  Buyang  S    Split into three languages: E'ma Buyang [yzg]; Langnian Buyang [yln]; Baha Buyang [yha]  2008-01-14
ccx  Northern Zhuang  S    Split into ten languages: Guibian Zh [zgn]; Liujiang Zh [zlj]; Qiubei Zh [zqe]; Guibei Zh [zgb]; Youjiang Zh [zyj]; Central Hongshuihe Zh [zch]; Eastern Hongshuihe Zh [zeh]; Liuqian Zh [zlq]; Yongbei Zh [zyb]; Lianshan Zh [zln].  2008-01-14
cru  Carútana  M  bwi    2008-01-14
dat  Darang Deng  D  mhu    2008-01-14
dyk  Land Dayak  N      2008-01-14
eni  Enim  M  pse    2008-01-14
fiz  Izere  S    Split into Ganang [gne] and Izere [izr] (new identifier)  2008-01-14
gen  Geman Deng  D  mxj    2008-01-14
ggh  Garreh-Ajuran  S    Split between Borana [gax] and Somali [som]  2008-01-14
itu  Itutang  M  mzu    2008-01-14
kds  Lahu Shi  S    Split into Kucong [lkc] and Lahu Shi [lhi] (new identifier)  2008-01-14
knh  Kayan River Kenyah  N      2008-01-14
krg  North Korowai  M  khe    2008-01-14
krq  Krui  M  ljp    2008-01-14
kxg  Katingan  M  nij    2008-01-14
lmt  Lematang  M  mui    2008-01-14
lnt  Lintang  M  pse    2008-01-14
lod  Berawan  S    Split into three languages: West Berawan [zbw], Central Berawan [zbc], and East Berawan [zbe]  2008-01-14
mbg  Northern Nambikuára  S    Split into six languages: Alapmunte [apv]; Lakondê [lkd]; Latundê [ltn]; Mamaindé [wmd]; Tawandê [xtw]; Yalakalore [xyl]  2008-01-14
mdo  Southwest Gbaya  S    Split into Southwest Gbaya [gso] (new identifier) and Gbaya-Mbodomo [gmm]  2008-01-14
mhv  Arakanese  S    Split into Marma [rmz] and Rakhine [rki]  2008-01-14
miv  Mimi  M  amj    2008-01-14
mqd  Madang  M  xkl    2008-01-14
nky  Khiamniungan Naga  S    Split into three languages: Khiamniungan Naga [kix] (new identifier); Para Naga [pzn]; Makuri Naga [jmn]  2008-01-14
nxj  Nyadu  M  byd    2008-01-14
ogn  Ogan  M  pse    2008-01-14
ork  Orokaiva  S    Split into Orokaiva [okv] (new identifier), Aeka [aez] and Hunjara-Kaina Ke [hkk]  2008-01-14
paj  Ipeka-Tapuia  M  kpc    2008-01-14
pec  Southern Pesisir  M  ljp    2008-01-14
pen  Penesak  M  mui    2008-01-14
plm  Palembang  M  mui    2008-01-14
poj  Lower Pokomo  M  pkb    2008-01-14
pun  Pubian  M  ljp    2008-01-14
rae  Ranau  M  ljp    2008-01-14
rjb  Rajbanshi  S    Split into Kamta (India) / Rangpuri (Bangladesh) [rkt] and Rajbanshi (Nepal) [rjs]  2008-01-14
rws  Rawas  M  mui    2008-01-14
sdd  Semendo  M  pse    2008-01-14
sdi  Sindang Kelingi  M  liw    2008-01-14
skl  Selako  M  knx    2008-01-14
slb  Kahumamahon Saluan  M  loe    2008-01-14
srj  Serawai  M  pse    2008-01-14
suf  Tarpia  S    Split into Tarpia [tpf] (new identifier) and Kaptiau [kbi]  2008-01-14
suh  Suba  S    Split into Suba [sxb] (Kenya) and Suba-Simbita [ssc] (Tanzania)  2008-01-14
suu  Sungkai  M  ljp    2008-01-14
szk  Sizaki  M  ikz    2008-01-14
tle  Southern Marakwet  M  enb    2008-01-14
tnj  Tanjong  M  kxn    2008-01-14
ttx  Tutong 1  M  bsb    2008-01-14
ubm  Upper Baram Kenyah  N      2008-01-14
vky  Kayu Agung  M  kge    2008-01-14
vmo  Muko-Muko  M  min    2008-01-14
wre  Ware  N      2008-01-14
xah  Kahayan  M  nij    2008-01-14
xkm  Mahakam Kenyah  N      2008-01-14
xuf  Kunfal  M  awn    2008-01-14
yio  Dayao Yi  M  lpo    2008-01-14
ymj  Muji Yi  S    Split into five languages: Muji, Southern [ymc], Mojii [ymi], Qila Muji [ymq], Northern Muji [ymx], and Muzi [ymz]  2008-01-14
ypl  Pula Yi  S    Split into three languages: Phola [ypg], Phala [ypa] and Alo Phola [ypo]  2008-01-14
ypw  Puwa Yi  S    Split into three languages: Hlepho Phowa [yhl], Labo Phowa [ypb], and Ani Phowa [ypn]  2008-01-14
ywm  Wumeng Yi  M  ywu    2008-01-14
yym  Yuanjiang-Mojiang Yi  S    Split into Southern Nisu [nsd] and Southwestern Nisu [nsv]  2008-01-14
mly  Malay (individual language)  S    Split into four languages: Standard Malay [zsm], Haji [hji], Papuan Malay [pmy] and Malay (individual language) [zlm]  2008-02-18
muw  Mundari  S    Split into Munda [unx] and Mundari [unr] (new identifier)  2008-02-18
xst  Silt'e  S    Split into Wolane [wle] and Silt'e [stv] (new identifier)  2008-02-28
ope  Old Persian  D  peo    2008-04-18
scc  Serbian  D  srp    2008-06-28
scr  Croatian  D  hrv    2008-06-28
xsk  Sakan  D  kho    2008-10-23
mol  Moldavian  M  ron    2008-11-03
aay  Aariya  N      2009-01-16
acc  Cubulco Achí  M  acr    2009-01-16
cbm  Yepocapa Southwestern Cakchiquel  M  cak    2009-01-16
chs  Chumash  S    Chumash is actually a family name, not a language name. Language family members already have code elements: Barbareño [boi], Cruzeño [crz], Ineseño [inz], Obispeño [obi], Purisimeño [puy], and Ventureño [veo]  2009-01-16
ckc  Northern Cakchiquel  M  cak    2009-01-16
ckd  South Central Cakchiquel  M  cak    2009-01-16
cke  Eastern Cakchiquel  M  cak    2009-01-16
ckf  Southern Cakchiquel  M  cak    2009-01-16
cki  Santa María De Jesús Cakchiquel  M  cak    2009-01-16
ckj  Santo Domingo Xenacoj Cakchiquel  M  cak    2009-01-16
ckk  Acatenango Southwestern Cakchiquel  M  cak    2009-01-16
ckw  Western Cakchiquel  M  cak    2009-01-16
cnm  Ixtatán Chuj  M  cac    2009-01-16
cti  Tila Chol  M  ctu    2009-01-16
cun  Cunén Quiché  M  quc    2009-01-16
eml  Emiliano-Romagnolo  S    Split into Emilian [egl] and Romagnol [rgn]  2009-01-16
eur  Europanto  N      2009-01-16
gmo  Gamo-Gofa-Dawro  S    Split into three languages: Gamo [gmv], Gofa [gof], and Dawro [dwr]  2009-01-16
hsf  Southeastern Huastec  M  hus    2009-01-16
hva  San Luís Potosí Huastec  M  hus    2009-01-16
ixi  Nebaj Ixil  M  ixl    2009-01-16
ixj  Chajul Ixil  M  ixl    2009-01-16
jai  Western Jacalteco  M  jac    2009-01-16
mms  Southern Mam  M  mam    2009-01-16
mpf  Tajumulco Mam  M  mam    2009-01-16
mtz  Tacanec  M  mam    2009-01-16
mvc  Central Mam  M  mam    2009-01-16
mvj  Todos Santos Cuchumatán Mam  M  mam    2009-01-16
poa  Eastern Pokomam  M  poc    2009-01-16
pob  Western Pokomchí  M  poh    2009-01-16
pou  Southern Pokomam  M  poc    2009-01-16
ppv  Papavô  N      2009-01-16
quj  Joyabaj Quiché  M  quc    2009-01-16
qut  West Central Quiché  M  quc    2009-01-16
quu  Eastern Quiché  M  quc    2009-01-16
qxi  San Andrés Quiché  M  quc    2009-01-16
sic  Malinguat  S    Split into Keak [keh] and Sos Kundi [sdk]  2009-01-16
stc  Santa Cruz  S    Split into Natügu [ntu] and Nalögo [nlz]  2009-01-16
tlz  Toala'  M  rob    2009-01-16
tzb  Bachajón Tzeltal  M  tzh    2009-01-16
tzc  Chamula Tzotzil  M  tzo    2009-01-16
tze  Chenalhó Tzotzil  M  tzo    2009-01-16
tzs  San Andrés Larrainzar Tzotzil  M  tzo    2009-01-16
tzt  Western Tzutujil  M  tzj    2009-01-16
tzu  Huixtán Tzotzil  M  tzo    2009-01-16
tzz  Zinacantán Tzotzil  M  tzo    2009-01-16
vlr  Vatrata  S    Split into Vera'a [vra] and Lemerig [lrz]  2009-01-16
yus  Chan Santa Cruz Maya  M  yua    2009-01-16
nfg  Nyeng  M  nfd    2009-01-26
nfk  Shakara  M  nfd    2009-01-26
agp  Paranan  S    Split into Pahanan Agta [apf] and Paranan [prf] (new identifier)  2010-01-18
bhk  Albay Bicolano  S    Split into Buhi'non Bikol [ubl]; Libon Bikol [lbl]; Miraya Bikol [rbl]; West Albay Bikol [fbl]  2010-01-18
bkb  Finallig  S    Split into Eastern Bontok [ebk] and Southern Bontok [obk]  2010-01-18
btb  Beti (Cameroon)  S    Beti is a group name, not an individual language name. Member languages are Bebele [beb], Bebil [bxp], Bulu [bum], Eton [eto], Ewondo [ewo], Fang [fan], and Mengisa [mct], all of which already have their own code elements.  2010-01-18
cjr  Chorotega  M  mom    2010-01-18
cmk  Chimakum  D  xch    2010-01-18
drh  Darkhat  M  khk    2010-01-18
drw  Darwazi  M  prs    2010-01-18
gav  Gabutamon  M  dev    2010-01-18
mof  Mohegan-Montauk-Narragansett  S    split into Mohegan-Pequot [xpq] and Narragansett [xnt]  2010-01-18
mst  Cataelano Mandaya  M  mry    2010-01-18
myt  Sangab Mandaya  M  mry    2010-01-18
rmr  Caló  S    split into Caló [rmq] and Erromintxela [emx]  2010-01-18
sgl  Sanglechi-Ishkashimi  S    split into Sanglechi [sgy] and Ishkashimi [isk]  2010-01-18
sul  Surigaonon  S    Split into Tandaganon [tgn] and Surigaonon [sgd] (new identifier)  2010-01-18
sum  Sumo-Mayangna  S    Split into Mayangna [yan] and Ulwa [ulw]  2010-01-18
tnf  Tangshewi  M  prs    2010-01-18
wgw  Wagawaga  S    Split into Yaleba [ylb] and Wagawaga [wgb] (new identifier)  2010-01-18
ayx  Ayi (China)  D  nun    2011-05-18
bjq  Southern Betsimisaraka Malagasy  S    split into Southern Betsimisaraka [bzc] and Tesaka Malagasy [tkg]  2011-05-18
dha  Dhanwar (India)  N      2011-05-18
dkl  Kolum So Dogon  S    split into Ampari Dogon [aqd] and Mombo Dogon [dmb]  2011-05-18
mja  Mahei  N      2011-05-18
nbf  Naxi  S    split into Naxi [nxq] and Narua [nru]  2011-05-18
noo  Nootka  S    Split into [dtd] Ditidaht and [nuk] Nuu-chah-nulth  2011-05-18
tie  Tingal  M  ras    2011-05-18
tkk  Takpa  D  twm    2011-05-18
baz  Tunen  S    Split Tunen [baz]  into Tunen [tvu] and Nyokon [nvo]  2012-02-03
bjd  Bandjigali  M  drl    2012-02-03
ccq  Chaungtha  M  rki    2012-02-03
cka  Khumi Awa Chin  M  cmr    2012-02-03
dap  Nisi (India)  S    Split into Nyishi [njz] and Tagin [tgj]  2012-02-03
dwl  Walo Kumbe Dogon  S    Split into Dogon, Bankan Tey (Walo) [dbw]  and Dogon, Ben Tey (Beni) [dbt]  2012-02-03
elp  Elpaputih  N      2012-02-03
gbc  Garawa  S    Split into Garrwa [wrk] and Wanyi [wny]  2012-02-03
gio  Gelao  S    split into Qau [gqu] and A'ou [aou] with some going to Green Gelao [gig], some to Red Gelao [gir], and some to White Gelao [giw]  2012-02-03
hrr  Horuru  M  jal    2012-02-03
ibi  Ibilo  M  opa    2012-02-03
jar  Jarawa (Nigeria)  S    split into Gwak [jgk] and Bankal [jjr]  2012-02-03
kdv  Kado  S    split into Kadu [zkd] and Kanan [zkn]  2012-02-03
kgh  Upper Tanudan Kalinga  M  kml    2012-02-03
kpp  Paku Karen  S    Split into Paku Karen [jkp] and Mobwa Karen [jkm]  2012-02-03
kzh  Kenuzi-Dongola  S    Split into Andaandi (Dongolawi) [dgl] and Kenzi (Mattoki) [xnz]  2012-02-03
lcq  Luhu  M  ppr    2012-02-03
mgx  Omati  S    Split into Barikewa [jbk] and Mouwase [jmw]  2012-02-03
nln  Durango Nahuatl  S    Split into Eastern Durango Nahuatl [azd] and Western Durango Nahuatl [azn]  2012-02-03
pbz  Palu  N      2012-02-03
pgy  Pongyong  N      2012-02-03
sca  Sansu  M  sca    2012-02-03
tlw  South Wemale  M  weo    2012-02-03
unp  Worora  S    Split into Worrorra [wro] and Unggumi [xgu].  2012-02-03
wiw  Wirangu  S    Split into Wirangu [wgu] and Nauo [nwo]  2012-02-03
ybd  Yangbye  M  rki    2012-02-03
yen  Yendang  S    Split into Yendang [ynq] and Yotti [yot]  2012-02-03
yma  Yamphe  M  lrr    2012-02-03
daf  Dan  S    Split into Dan [dnj] and Kla-Dan [lda]  2013-01-23
djl  Djiwarli  S    Split into Djiwarli [dze] and Thiin [iin]  2013-01-23
ggr  Aghu Tharnggalu  S    Split into Aghu-Tharnggala [gtu], Gugu-Mini [ggm], and Ikarranggal [ikr]  2013-01-23
ilw  Talur  M  gal    2013-01-23
izi  Izi-Ezaa-Ikwo-Mgbo  S    Split into Izii [izz], Ezaa [eza], Ikwo [iqw], Mgbolizhia [gmz]  2013-01-23
meg  Mea  M  cir    2013-01-23
mld  Malakhel  N      2013-01-23
mnt  Maykulan  S    Split into Mayi-Kulan [xyk], Mayi-Thakurti [xyt], Mayi-Yapi [xyj], and Wunumara [wnn]  2013-01-23
mwd  Mudbura  S    Split into Karranga [xrq] and Mudburra [dmw]  2013-01-23
myq  Forest Maninka  N      2013-01-23
nbx  Ngura  S    Split into Eastern Karnic [ekc], Garlali [gll], Punthamara [xpt], Wangkumara [xwk], and Badjiri [jbi]  2013-01-23
nlr  Ngarla  S    Split into Ngarla [nrk] and Yinhawangka [ywg]  2013-01-23
pcr  Panang  M  adx    2013-01-23
ppr  Piru        2013-01-23
tgg  Tangga  S    Split into Fanamaket [bjp], Niwer Mil [hrc], and Warwar Feni [hrw]  2013-01-23
wit  Wintu  S    Split into Wintu [wnw], Nomlaki [nol], and Patwin [pwi]  2013-01-23
xia  Xiandao  M  acn    2013-01-23
yiy  Yir Yoront  S    Split into Yir Yoront [yyr] and Yirrk-Mel [yrm]  2013-01-23
yos  Yos  M  zom    2013-01-23"""


# from http://www-01.sil.org/iso639-3/codes.asp?order=639_3&letter=%25
#639-1 	639-2/639-5 	639-3	Language Name 	Scope 	Type
isomapping = """aa 	aar 	aar 	Afar 	Individual 	Living 	more ...
ab 	abk 	abk 	Abkhazian 	Individual 	Living 	more ...
ae 	ave 	ave 	Avestan 	Individual 	Ancient 	more ...
af 	afr 	afr 	Afrikaans 	Individual 	Living 	more ...
ak 	aka 	aka 	Akan 	Macrolanguage 	Living 	more ...
am 	amh 	amh 	Amharic 	Individual 	Living 	more ...
an 	arg 	arg 	Aragonese 	Individual 	Living 	more ...
ar 	ara 	ara 	Arabic 	Macrolanguage 	Living 	more ...
as 	asm 	asm 	Assamese 	Individual 	Living 	more ...
av 	ava 	ava 	Avaric 	Individual 	Living 	more ...
ay 	aym 	aym 	Aymara 	Macrolanguage 	Living 	more ...
az 	aze 	aze 	Azerbaijani 	Macrolanguage 	Living 	more ...
ba 	bak 	bak 	Bashkir 	Individual 	Living 	more ...
be 	bel 	bel 	Belarusian 	Individual 	Living 	more ...
bg 	bul 	bul 	Bulgarian 	Individual 	Living 	more ...
bh 	bih 	- 	Bihari languages 	Collective 		more ...
bi 	bis 	bis 	Bislama 	Individual 	Living 	more ...
bm 	bam 	bam 	Bambara 	Individual 	Living 	more ...
bn 	ben 	ben 	Bengali 	Individual 	Living 	more ...
bo 	bod / tib*  	bod 	Tibetan 	Individual 	Living 	more ...
br 	bre 	bre 	Breton 	Individual 	Living 	more ...
bs 	bos 	bos 	Bosnian 	Individual 	Living 	more ...
ca 	cat 	cat 	Catalan 	Individual 	Living 	more ...
ce 	che 	che 	Chechen 	Individual 	Living 	more ...
ch 	cha 	cha 	Chamorro 	Individual 	Living 	more ...
co 	cos 	cos 	Corsican 	Individual 	Living 	more ...
cr 	cre 	cre 	Cree 	Macrolanguage 	Living 	more ...
cs 	ces / cze*  	ces 	Czech 	Individual 	Living 	more ...
cu 	chu 	chu 	Church Slavic 	Individual 	Ancient 	more ...
cv 	chv 	chv 	Chuvash 	Individual 	Living 	more ...
cy 	cym / wel*  	cym 	Welsh 	Individual 	Living 	more ...
da 	dan 	dan 	Danish 	Individual 	Living 	more ...
de 	deu / ger*  	deu 	German 	Individual 	Living 	more ...
dv 	div 	div 	Dhivehi 	Individual 	Living 	more ...
dz 	dzo 	dzo 	Dzongkha 	Individual 	Living 	more ...
ee 	ewe 	ewe 	Ewe 	Individual 	Living 	more ...
el 	ell / gre*  	ell 	Modern Greek (1453-) 	Individual 	Living 	more ...
en 	eng 	eng 	English 	Individual 	Living 	more ...
eo 	epo 	epo 	Esperanto 	Individual 	Constructed 	more ...
es 	spa 	spa 	Spanish 	Individual 	Living 	more ...
et 	est 	est 	Estonian 	Macrolanguage 	Living 	more ...
eu 	eus / baq*  	eus 	Basque 	Individual 	Living 	more ...
fa 	fas / per*  	fas 	Persian 	Macrolanguage 	Living 	more ...
ff 	ful 	ful 	Fulah 	Macrolanguage 	Living 	more ...
fi 	fin 	fin 	Finnish 	Individual 	Living 	more ...
fj 	fij 	fij 	Fijian 	Individual 	Living 	more ...
fo 	fao 	fao 	Faroese 	Individual 	Living 	more ...
fr 	fra / fre*  	fra 	French 	Individual 	Living 	more ...
fy 	fry 	fry 	Western Frisian 	Individual 	Living 	more ...
ga 	gle 	gle 	Irish 	Individual 	Living 	more ...
gd 	gla 	gla 	Scottish Gaelic 	Individual 	Living 	more ...
gl 	glg 	glg 	Galician 	Individual 	Living 	more ...
gn 	grn 	grn 	Guarani 	Macrolanguage 	Living 	more ...
gu 	guj 	guj 	Gujarati 	Individual 	Living 	more ...
gv 	glv 	glv 	Manx 	Individual 	Living 	more ...
ha 	hau 	hau 	Hausa 	Individual 	Living 	more ...
he 	heb 	heb 	Hebrew 	Individual 	Living 	more ...
hi 	hin 	hin 	Hindi 	Individual 	Living 	more ...
ho 	hmo 	hmo 	Hiri Motu 	Individual 	Living 	more ...
hr 	hrv 	hrv 	Croatian 	Individual 	Living 	more ...
ht 	hat 	hat 	Haitian 	Individual 	Living 	more ...
hu 	hun 	hun 	Hungarian 	Individual 	Living 	more ...
hy 	hye / arm*  	hye 	Armenian 	Individual 	Living 	more ...
hz 	her 	her 	Herero 	Individual 	Living 	more ...
ia 	ina 	ina 	Interlingua (International Auxiliary Language Association) 	Individual 	Constructed 	more ...
id 	ind 	ind 	Indonesian 	Individual 	Living 	more ...
ie 	ile 	ile 	Interlingue 	Individual 	Constructed 	more ...
ig 	ibo 	ibo 	Igbo 	Individual 	Living 	more ...
ii 	iii 	iii 	Sichuan Yi 	Individual 	Living 	more ...
ik 	ipk 	ipk 	Inupiaq 	Macrolanguage 	Living 	more ...
io 	ido 	ido 	Ido 	Individual 	Constructed 	more ...
is 	isl / ice*  	isl 	Icelandic 	Individual 	Living 	more ...
it 	ita 	ita 	Italian 	Individual 	Living 	more ...
iu 	iku 	iku 	Inuktitut 	Macrolanguage 	Living 	more ...
ja 	jpn 	jpn 	Japanese 	Individual 	Living 	more ...
jv 	jav 	jav 	Javanese 	Individual 	Living 	more ...
ka 	kat / geo*  	kat 	Georgian 	Individual 	Living 	more ...
kg 	kon 	kon 	Kongo 	Macrolanguage 	Living 	more ...
ki 	kik 	kik 	Kikuyu 	Individual 	Living 	more ...
kj 	kua 	kua 	Kuanyama 	Individual 	Living 	more ...
kk 	kaz 	kaz 	Kazakh 	Individual 	Living 	more ...
kl 	kal 	kal 	Kalaallisut 	Individual 	Living 	more ...
km 	khm 	khm 	Central Khmer 	Individual 	Living 	more ...
kn 	kan 	kan 	Kannada 	Individual 	Living 	more ...
ko 	kor 	kor 	Korean 	Individual 	Living 	more ...
kr 	kau 	kau 	Kanuri 	Macrolanguage 	Living 	more ...
ks 	kas 	kas 	Kashmiri 	Individual 	Living 	more ...
ku 	kur 	kur 	Kurdish 	Macrolanguage 	Living 	more ...
kv 	kom 	kom 	Komi 	Macrolanguage 	Living 	more ...
kw 	cor 	cor 	Cornish 	Individual 	Living 	more ...
ky 	kir 	kir 	Kirghiz 	Individual 	Living 	more ...
la 	lat 	lat 	Latin 	Individual 	Ancient 	more ...
lb 	ltz 	ltz 	Luxembourgish 	Individual 	Living 	more ...
lg 	lug 	lug 	Ganda 	Individual 	Living 	more ...
li 	lim 	lim 	Limburgan 	Individual 	Living 	more ...
ln 	lin 	lin 	Lingala 	Individual 	Living 	more ...
lo 	lao 	lao 	Lao 	Individual 	Living 	more ...
lt 	lit 	lit 	Lithuanian 	Individual 	Living 	more ...
lu 	lub 	lub 	Luba-Katanga 	Individual 	Living 	more ...
lv 	lav 	lav 	Latvian 	Macrolanguage 	Living 	more ...
mg 	mlg 	mlg 	Malagasy 	Macrolanguage 	Living 	more ...
mh 	mah 	mah 	Marshallese 	Individual 	Living 	more ...
mi 	mri / mao*  	mri 	Maori 	Individual 	Living 	more ...
mk 	mkd / mac*  	mkd 	Macedonian 	Individual 	Living 	more ...
ml 	mal 	mal 	Malayalam 	Individual 	Living 	more ...
mn 	mon 	mon 	Mongolian 	Macrolanguage 	Living 	more ...
mr 	mar 	mar 	Marathi 	Individual 	Living 	more ...
ms 	msa / may*  	msa 	Malay (macrolanguage) 	Macrolanguage 	Living 	more ...
mt 	mlt 	mlt 	Maltese 	Individual 	Living 	more ...
my 	mya / bur*  	mya 	Burmese 	Individual 	Living 	more ...
na 	nau 	nau 	Nauru 	Individual 	Living 	more ...
nb 	nob 	nob 	Norwegian Bokmål 	Individual 	Living 	more ...
nd 	nde 	nde 	North Ndebele 	Individual 	Living 	more ...
ne 	nep 	nep 	Nepali (macrolanguage) 	Macrolanguage 	Living 	more ...
ng 	ndo 	ndo 	Ndonga 	Individual 	Living 	more ...
nl 	nld / dut*  	nld 	Dutch 	Individual 	Living 	more ...
nn 	nno 	nno 	Norwegian Nynorsk 	Individual 	Living 	more ...
no 	nor 	nor 	Norwegian 	Macrolanguage 	Living 	more ...
nr 	nbl 	nbl 	South Ndebele 	Individual 	Living 	more ...
nv 	nav 	nav 	Navajo 	Individual 	Living 	more ...
ny 	nya 	nya 	Nyanja 	Individual 	Living 	more ...
oc 	oci 	oci 	Occitan (post 1500) 	Individual 	Living 	more ...
oj 	oji 	oji 	Ojibwa 	Macrolanguage 	Living 	more ...
om 	orm 	orm 	Oromo 	Macrolanguage 	Living 	more ...
or 	ori 	ori 	Oriya (macrolanguage) 	Macrolanguage 	Living 	more ...
os 	oss 	oss 	Ossetian 	Individual 	Living 	more ...
pa 	pan 	pan 	Panjabi 	Individual 	Living 	more ...
pi 	pli 	pli 	Pali 	Individual 	Ancient 	more ...
pl 	pol 	pol 	Polish 	Individual 	Living 	more ...
ps 	pus 	pus 	Pushto 	Macrolanguage 	Living 	more ...
pt 	por 	por 	Portuguese 	Individual 	Living 	more ...
qu 	que 	que 	Quechua 	Macrolanguage 	Living 	more ...
rm 	roh 	roh 	Romansh 	Individual 	Living 	more ...
rn 	run 	run 	Rundi 	Individual 	Living 	more ...
ro 	ron / rum*  	ron 	Romanian 	Individual 	Living 	more ...
ru 	rus 	rus 	Russian 	Individual 	Living 	more ...
rw 	kin 	kin 	Kinyarwanda 	Individual 	Living 	more ...
sa 	san 	san 	Sanskrit 	Individual 	Ancient 	more ...
sc 	srd 	srd 	Sardinian 	Macrolanguage 	Living 	more ...
sd 	snd 	snd 	Sindhi 	Individual 	Living 	more ...
se 	sme 	sme 	Northern Sami 	Individual 	Living 	more ...
sg 	sag 	sag 	Sango 	Individual 	Living 	more ...
sh (deprecated) 	- 	hbs 	Serbo-Croatian 	Macrolanguage 	Living 	more ...
si 	sin 	sin 	Sinhala 	Individual 	Living 	more ...
sk 	slk / slo*  	slk 	Slovak 	Individual 	Living 	more ...
sl 	slv 	slv 	Slovenian 	Individual 	Living 	more ...
sm 	smo 	smo 	Samoan 	Individual 	Living 	more ...
sn 	sna 	sna 	Shona 	Individual 	Living 	more ...
so 	som 	som 	Somali 	Individual 	Living 	more ...
sq 	sqi / alb*  	sqi 	Albanian 	Macrolanguage 	Living 	more ...
sr 	srp 	srp 	Serbian 	Individual 	Living 	more ...
ss 	ssw 	ssw 	Swati 	Individual 	Living 	more ...
st 	sot 	sot 	Southern Sotho 	Individual 	Living 	more ...
su 	sun 	sun 	Sundanese 	Individual 	Living 	more ...
sv 	swe 	swe 	Swedish 	Individual 	Living 	more ...
sw 	swa 	swa 	Swahili (macrolanguage) 	Macrolanguage 	Living 	more ...
ta 	tam 	tam 	Tamil 	Individual 	Living 	more ...
te 	tel 	tel 	Telugu 	Individual 	Living 	more ...
tg 	tgk 	tgk 	Tajik 	Individual 	Living 	more ...
th 	tha 	tha 	Thai 	Individual 	Living 	more ...
ti 	tir 	tir 	Tigrinya 	Individual 	Living 	more ...
tk 	tuk 	tuk 	Turkmen 	Individual 	Living 	more ...
tl 	tgl 	tgl 	Tagalog 	Individual 	Living 	more ...
tn 	tsn 	tsn 	Tswana 	Individual 	Living 	more ...
to 	ton 	ton 	Tonga (Tonga Islands) 	Individual 	Living 	more ...
tr 	tur 	tur 	Turkish 	Individual 	Living 	more ...
ts 	tso 	tso 	Tsonga 	Individual 	Living 	more ...
tt 	tat 	tat 	Tatar 	Individual 	Living 	more ...
tw 	twi 	twi 	Twi 	Individual 	Living 	more ...
ty 	tah 	tah 	Tahitian 	Individual 	Living 	more ...
ug 	uig 	uig 	Uighur 	Individual 	Living 	more ...
uk 	ukr 	ukr 	Ukrainian 	Individual 	Living 	more ...
ur 	urd 	urd 	Urdu 	Individual 	Living 	more ...
uz 	uzb 	uzb 	Uzbek 	Macrolanguage 	Living 	more ...
ve 	ven 	ven 	Venda 	Individual 	Living 	more ...
vi 	vie 	vie 	Vietnamese 	Individual 	Living 	more ...
vo 	vol 	vol 	Volapük 	Individual 	Constructed 	more ...
wa 	wln 	wln 	Walloon 	Individual 	Living 	more ...
wo 	wol 	wol 	Wolof 	Individual 	Living 	more ...
xh 	xho 	xho 	Xhosa 	Individual 	Living 	more ...
yi 	yid 	yid 	Yiddish 	Macrolanguage 	Living 	more ...
yo 	yor 	yor 	Yoruba 	Individual 	Living 	more ...
za 	zha 	zha 	Zhuang 	Macrolanguage 	Living 	more ...
zh 	zho / chi*  	zho 	Chinese 	Macrolanguage 	Living 	more ...
zu 	zul 	zul 	Zulu 	Individual 	Living 	more ..."""

# http://meta.wikimedia.org/wiki/Special_language_codes
wikispecialcodes = """als gsw
bat-smg sgs
cbk-zam cbk
fiu-vro vro
roa-rup rup
map-bms jv
sh hbs
zh-classical lzh
zh-min-nan nan
zh-yue yue
mo ron""" #simple en

iso6395 = """aka  Akan  fat  Fanti
   twi  Twi
ara  Arabic  aao  Algerian Saharan Arabic
   abh  Tajiki Arabic
   abv  Baharna Arabic
   acm  Mesopotamian Arabic
   acq  Ta'izzi-Adeni Arabic
   acw  Hijazi Arabic
   acx  Omani Arabic
   acy  Cypriot Arabic
   adf  Dhofari Arabic
   aeb  Tunisian Arabic
   aec  Saidi Arabic
   afb  Gulf Arabic
   ajp  South Levantine Arabic
   apc  North Levantine Arabic
   apd  Sudanese Arabic
   arb  Standard Arabic
   arq  Algerian Arabic
   ars  Najdi Arabic
   ary  Moroccan Arabic
   arz  Egyptian Arabic
   auz  Uzbeki Arabic
   avl  Eastern Egyptian Bedawi Arabic
   ayh  Hadrami Arabic
   ayl  Libyan Arabic
   ayn  Sanaani Arabic
   ayp  North Mesopotamian Arabic
   bbz  Babalia Creole Arabic
   pga  Sudanese Creole Arabic
   shu  Chadian Arabic
   ssh  Shihhi Arabic
aym  Aymara  ayc  Southern Aymara
   ayr  Central Aymara
aze  Azerbaijani  azb  South Azerbaijani
   azj  North Azerbaijani
bal  Baluchi  bcc  Southern Balochi
   bgn  Western Balochi
   bgp  Eastern Balochi
bik  Bikol  bcl  Central Bikol
   bhk  Albay Bicolano  (Retired 1/15/2010)
   bln  Southern Catanduanes Bikol
   bto  Rinconada Bikol
   cts  Northern Catanduanes Bikol
   fbl  West Albay Bikol
   lbl  Libon Bikol
   rbl  Miraya Bikol
   ubl  Buhi'non Bikol
bnc  Bontok  ebk  Eastern Bontok
   lbk  Central Bontok
   obk  Southern Bontok
   rbk  Northern Bontok
   vbk  Southwestern Bontok
bua  Buriat  bxm  Mongolia Buriat
   bxr  Russia Buriat
   bxu  China Buriat
chm  Mari (Russia)  mhr  Eastern Mari
   mrj  Western Mari
cre  Cree  crj  Southern East Cree
   crk  Plains Cree
   crl  Northern East Cree
   crm  Moose Cree
   csw  Swampy Cree
   cwd  Woods Cree
del  Delaware  umu  Munsee
   unm  Unami
den  Slave (Athapascan)  scs  North Slavey
   xsl  South Slavey
din  Dinka  dib  South Central Dinka
   dik  Southwestern Dinka
   dip  Northeastern Dinka
   diw  Northwestern Dinka
   dks  Southeastern Dinka
doi  Dogri (macrolanguage)  dgo  Dogri (individual language)
   xnr  Kangri
est  Estonian  ekk  Standard Estonian
   vro  Võro
fas  Persian  pes  Iranian Persian
   prs  Dari
ful  Fulah  ffm  Maasina Fulfulde
   fub  Adamawa Fulfulde
   fuc  Pulaar
   fue  Borgu Fulfulde
   fuf  Pular
   fuh  Western Niger Fulfulde
   fui  Bagirmi Fulfulde
   fuq  Central-Eastern Niger Fulfulde
   fuv  Nigerian Fulfulde
gba  Gbaya (Central African Republic)  bdt  Bokoto
   gbp  Gbaya-Bossangoa
   gbq  Gbaya-Bozoum
   gmm  Gbaya-Mbodomo
   gso  Southwest Gbaya
   gya  Northwest Gbaya
   mdo  Southwest Gbaya  (Retired 1/14/2008)
gon  Gondi  ggo  Southern Gondi
   gno  Northern Gondi
grb  Grebo  gbo  Northern Grebo
   gec  Gboloo Grebo
   grj  Southern Grebo
   grv  Central Grebo
   gry  Barclayville Grebo
grn  Guarani  gnw  Western Bolivian Guaraní
   gug  Paraguayan Guaraní
   gui  Eastern Bolivian Guaraní
   gun  Mbyá Guaraní
   nhd  Chiripá
hai  Haida  hax  Southern Haida
   hdn  Northern Haida
hbs  Serbo-Croatian  bos  Bosnian
   hrv  Croatian
   srp  Serbian
hmn  Hmong  blu  Hmong Njua  (Retired 1/14/2008)
   cqd  Chuanqiandian Cluster Miao
   hea  Northern Qiandong Miao
   hma  Southern Mashan Hmong
   hmc  Central Huishui Hmong
   hmd  Large Flowery Miao
   hme  Eastern Huishui Hmong
   hmg  Southwestern Guiyang Hmong
   hmh  Southwestern Huishui Hmong
   hmi  Northern Huishui Hmong
   hmj  Ge
   hml  Luopohe Hmong
   hmm  Central Mashan Hmong
   hmp  Northern Mashan Hmong
   hmq  Eastern Qiandong Miao
   hms  Southern Qiandong Miao
   hmw  Western Mashan Hmong
   hmy  Southern Guiyang Hmong
   hmz  Hmong Shua
   hnj  Hmong Njua
   hrm  Horned Miao
   huj  Northern Guiyang Hmong
   mmr  Western Xiangxi Miao
   muq  Eastern Xiangxi Miao
   mww  Hmong Daw
   sfm  Small Flowery Miao
iku  Inuktitut  ike  Eastern Canadian Inuktitut
   ikt  Inuinnaqtun
ipk  Inupiaq  esi  North Alaskan Inupiatun
   esk  Northwest Alaska Inupiatun
jrb  Judeo-Arabic  ajt  Judeo-Tunisian Arabic
   aju  Judeo-Moroccan Arabic
   jye  Judeo-Yemeni Arabic
   yhd  Judeo-Iraqi Arabic
   yud  Judeo-Tripolitanian Arabic
kau  Kanuri  kby  Manga Kanuri
   knc  Central Kanuri
   krt  Tumari Kanuri
kln  Kalenjin  enb  Markweeta
   eyo  Keiyo
   niq  Nandi
   oki  Okiek
   pko  Pökoot
   sgc  Kipsigis
   spy  Sabaot
   tec  Terik
   tuy  Tugen
kok  Konkani (macrolanguage)  gom  Goan Konkani
   knn  Konkani (individual language)
kom  Komi  koi  Komi-Permyak
   kpv  Komi-Zyrian
kon  Kongo  kng  Koongo
   kwy  San Salvador Kongo
   ldi  Laari
kpe  Kpelle  gkp  Guinea Kpelle
   xpe  Liberia Kpelle
kur  Kurdish  ckb  Central Kurdish
   kmr  Northern Kurdish
   sdh  Southern Kurdish
lah  Lahnda  hnd  Southern Hindko
   hno  Northern Hindko
   jat  Jakati
   phr  Pahari-Potwari
   pmu  Mirpur Panjabi
   pnb  Western Panjabi
   skr  Seraiki
   xhe  Khetrani
lav  Latvian  ltg  Latgalian
   lvs  Standard Latvian
luy  Luyia  bxk  Bukusu
   ida  Idakho-Isukha-Tiriki
   lkb  Kabras
   lko  Khayo
   lks  Kisa
   lri  Marachi
   lrm  Marama
   lsm  Saamia
   lto  Tsotso
   lts  Tachoni
   lwg  Wanga
   nle  East Nyala
   nyd  Nyore
   rag  Logooli
man  Mandingo  emk  Eastern Maninkakan
   mku  Konyanka Maninka
   mlq  Western Maninkakan
   mnk  Mandinka
   msc  Sankaran Maninka
   mwk  Kita Maninkakan
   myq  Forest Maninka  (Retired )
mlg  Malagasy  bhr  Bara Malagasy
   bjq  Southern Betsimisaraka Malagasy  (Retired )
   bmm  Northern Betsimisaraka Malagasy
   bzc  Southern Betsimisaraka Malagasy
   msh  Masikoro Malagasy
   plt  Plateau Malagasy
   skg  Sakalava Malagasy
   tdx  Tandroy-Mahafaly Malagasy
   tkg  Tesaka Malagasy
   txy  Tanosy Malagasy
   xmv  Antankarana Malagasy
   xmw  Tsimihety Malagasy
mon  Mongolian  khk  Halh Mongolian
   mvf  Peripheral Mongolian
msa  Malay (macrolanguage)  bjn  Banjar
   btj  Bacanese Malay
   bve  Berau Malay
   bvu  Bukit Malay
   coa  Cocos Islands Malay
   dup  Duano
   hji  Haji
   ind  Indonesian
   jak  Jakun
   jax  Jambi Malay
   kvb  Kubu
   kvr  Kerinci
   kxd  Brunei
   lce  Loncong
   lcf  Lubu
   liw  Col
   max  North Moluccan Malay
   meo  Kedah Malay
   mfa  Pattani Malay
   mfb  Bangka
   min  Minangkabau
   mly  Malay (individual language)  (Retired 2/18/2008)
   mqg  Kota Bangun Kutai Malay
   msi  Sabah Malay
   mui  Musi
   orn  Orang Kanaq
   ors  Orang Seletar
   pel  Pekal
   pse  Central Malay
   tmw  Temuan
   urk  Urak Lawoi'
   vkk  Kaur
   vkt  Tenggarong Kutai Malay
   xmm  Manado Malay
   zlm  Malay (individual language)
   zmi  Negeri Sembilan Malay
   zsm  Standard Malay
mwr  Marwari  dhd  Dhundari
   mtr  Mewari
   mve  Marwari (Pakistan)
   rwr  Marwari (India)
   swv  Shekhawati
   wry  Merwari
nep  Nepali (macrolanguage)  dty  Dotyali
   npi  Nepali (individual language)
nor  Norwegian  nno  Norwegian Nynorsk
   nob  Norwegian Bokmål
oji  Ojibwa  ciw  Chippewa
   ojb  Northwestern Ojibwa
   ojc  Central Ojibwa
   ojg  Eastern Ojibwa
   ojs  Severn Ojibwa
   ojw  Western Ojibwa
   otw  Ottawa
ori  Oriya (macrolanguage)  ory  Oriya (individual language)
   spv  Sambalpuri
orm  Oromo  gax  Borana-Arsi-Guji Oromo
   gaz  West Central Oromo
   hae  Eastern Oromo
   orc  Orma
pus  Pushto  pbt  Southern Pashto
   pbu  Northern Pashto
   pst  Central Pashto
que  Quechua  cqu  Chilean Quechua
   qub  Huallaga Huánuco Quechua
   qud  Calderón Highland Quichua
   quf  Lambayeque Quechua
   qug  Chimborazo Highland Quichua
   quh  South Bolivian Quechua
   quk  Chachapoyas Quechua
   qul  North Bolivian Quechua
   qup  Southern Pastaza Quechua
   qur  Yanahuanca Pasco Quechua
   qus  Santiago del Estero Quichua
   quw  Tena Lowland Quichua
   qux  Yauyos Quechua
   quy  Ayacucho Quechua
   quz  Cusco Quechua
   qva  Ambo-Pasco Quechua
   qvc  Cajamarca Quechua
   qve  Eastern Apurímac Quechua
   qvh  Huamalíes-Dos de Mayo Huánuco Quechua
   qvi  Imbabura Highland Quichua
   qvj  Loja Highland Quichua
   qvl  Cajatambo North Lima Quechua
   qvm  Margos-Yarowilca-Lauricocha Quechua
   qvn  North Junín Quechua
   qvo  Napo Lowland Quechua
   qvp  Pacaraos Quechua
   qvs  San Martín Quechua
   qvw  Huaylla Wanca Quechua
   qvz  Northern Pastaza Quichua
   qwa  Corongo Ancash Quechua
   qwc  Classical Quechua
   qwh  Huaylas Ancash Quechua
   qws  Sihuas Ancash Quechua
   qxa  Chiquián Ancash Quechua
   qxc  Chincha Quechua
   qxh  Panao Huánuco Quechua
   qxl  Salasaca Highland Quichua
   qxn  Northern Conchucos Ancash Quechua
   qxo  Southern Conchucos Ancash Quechua
   qxp  Puno Quechua
   qxr  Cañar Highland Quichua
   qxt  Santa Ana de Tusi Pasco Quechua
   qxu  Arequipa-La Unión Quechua
   qxw  Jauja Wanca Quechua
raj  Rajasthani  bgq  Bagri
   gda  Gade Lohar
   gju  Gujari
   hoj  Hadothi
   mup  Malvi
   wbr  Wagdi
rom  Romany  rmc  Carpathian Romani
   rmf  Kalo Finnish Romani
   rml  Baltic Romani
   rmn  Balkan Romani
   rmo  Sinte Romani
   rmw  Welsh Romani
   rmy  Vlax Romani
sqi  Albanian  aae  Arbëreshë Albanian
   aat  Arvanitika Albanian
   aln  Gheg Albanian
   als  Tosk Albanian
srd  Sardinian  sdc  Sassarese Sardinian
   sdn  Gallurese Sardinian
   src  Logudorese Sardinian
   sro  Campidanese Sardinian
swa  Swahili (macrolanguage)  swc  Congo Swahili
   swh  Swahili (individual language)
syr  Syriac  aii  Assyrian Neo-Aramaic
   cld  Chaldean Neo-Aramaic
tmh  Tamashek  taq  Tamasheq
   thv  Tahaggart Tamahaq
   thz  Tayart Tamajeq
   ttq  Tawallammat Tamajaq
uzb  Uzbek  uzn  Northern Uzbek
   uzs  Southern Uzbek
yid  Yiddish  ydd  Eastern Yiddish
   yih  Western Yiddish
zap  Zapotec  zaa  Sierra de Juárez Zapotec
   zab  San Juan Guelavía Zapotec
   zac  Ocotlán Zapotec
   zad  Cajonos Zapotec
   zae  Yareni Zapotec
   zaf  Ayoquesco Zapotec
   zai  Isthmus Zapotec
   zam  Miahuatlán Zapotec
   zao  Ozolotepec Zapotec
   zaq  Aloápam Zapotec
   zar  Rincón Zapotec
   zas  Santo Domingo Albarradas Zapotec
   zat  Tabaa Zapotec
   zav  Yatzachi Zapotec
   zaw  Mitla Zapotec
   zax  Xadani Zapotec
   zca  Coatecas Altas Zapotec
   zoo  Asunción Mixtepec Zapotec
   zpa  Lachiguiri Zapotec
   zpb  Yautepec Zapotec
   zpc  Choapan Zapotec
   zpd  Southeastern Ixtlán Zapotec
   zpe  Petapa Zapotec
   zpf  San Pedro Quiatoni Zapotec
   zpg  Guevea De Humboldt Zapotec
   zph  Totomachapan Zapotec
   zpi  Santa María Quiegolani Zapotec
   zpj  Quiavicuzas Zapotec
   zpk  Tlacolulita Zapotec
   zpl  Lachixío Zapotec
   zpm  Mixtepec Zapotec
   zpn  Santa Inés Yatzechi Zapotec
   zpo  Amatlán Zapotec
   zpp  El Alto Zapotec
   zpq  Zoogocho Zapotec
   zpr  Santiago Xanica Zapotec
   zps  Coatlán Zapotec
   zpt  San Vicente Coatlán Zapotec
   zpu  Yalálag Zapotec
   zpv  Chichicapan Zapotec
   zpw  Zaniza Zapotec
   zpx  San Baltazar Loxicha Zapotec
   zpy  Mazaltepec Zapotec
   zpz  Texmelucan Zapotec
   zsr  Southern Rincon Zapotec
   ztc  Lachirioag Zapotec  (Retired 7/18/2007)
   zte  Elotepec Zapotec
   ztg  Xanaguía Zapotec
   ztl  Lapaguía-Guivini Zapotec
   ztm  San Agustín Mixtepec Zapotec
   ztn  Santa Catarina Albarradas Zapotec
   ztp  Loxicha Zapotec
   ztq  Quioquitani-Quierí Zapotec
   zts  Tilquiapan Zapotec
   ztt  Tejalapan Zapotec
   ztu  Güilá Zapotec
   ztx  Zaachila Zapotec
   zty  Yatee Zapotec
zha  Zhuang  ccx  Northern Zhuang  (Retired 1/14/2008)
   ccy  Southern Zhuang  (Retired 7/18/2007)
   zch  Central Hongshuihe Zhuang
   zeh  Eastern Hongshuihe Zhuang
   zgb  Guibei Zhuang
   zgm  Minz Zhuang
   zgn  Guibian Zhuang
   zhd  Dai Zhuang
   zhn  Nong Zhuang
   zlj  Liujiang Zhuang
   zln  Lianshan Zhuang
   zlq  Liuqian Zhuang
   zqe  Qiubei Zhuang
   zyb  Yongbei Zhuang
   zyg  Yang Zhuang
   zyj  Youjiang Zhuang
   zyn  Yongnan Zhuang
   zzj  Zuojiang Zhuang
zho  Chinese  cdo  Min Dong Chinese
   cjy  Jinyu Chinese
   cmn  Mandarin Chinese
   cpx  Pu-Xian Chinese
   czh  Huizhou Chinese
   czo  Min Zhong Chinese
   gan  Gan Chinese
   hak  Hakka Chinese
   hsn  Xiang Chinese
   lzh  Literary Chinese
   mnp  Min Bei Chinese
   nan  Min Nan Chinese
   wuu  Wu Chinese
   yue  Yue Chinese
zza  Zaza  diq  Dimli (individual language)
   kiu  Kirmanjki (individual language)""" 

# listofwikis is incomplete!
listofwikis = """English Wikipedia  English  English  en  6
German Wikipedia  German  Latn  de  6
French Wikipedia  French  Latn  fr  6
Dutch Wikipedia  Dutch  Latn  nl  6
Italian Wikipedia  Italian  Latn  it  6
Spanish Wikipedia  Spanish  Latn  es  6
Russian Wikipedia  Russian  Cyrl  ru  6
Swedish Wikipedia  Swedish  Latn  sv  6
Polish Wikipedia  Polish  Latn  pl  6
Japanese Wikipedia  Japanese  Jpan  ja  5
Portuguese Wikipedia  Portuguese  English  pt  6
Arabic Wikipedia  Arabic  Arab  ar  6
Chinese Wikipedia  Chinese  Hans/Hant  zh  6
Ukrainian Wikipedia  Ukrainian  Cyrl  uk  5
Catalan Wikipedia  Catalan  Latn  ca  5
Bokmål/Riksmål Wikipedia  Norwegian (Bokmål)  Latn  no  5
Finnish Wikipedia  Finnish  Latn  fi  5
Czech Wikipedia  Czech  Latn  cs  5
Hungarian Wikipedia  Hungarian  Latn  hu  5
Turkish Wikipedia  Turkish  Latn  tr  5
Romanian Wikipedia  Romanian  Latn  ro  5
Swahili Wikipedia  Swahili  English  sw  5
Korean Wikipedia  Korean  Hang  ko  5
Kazakh Wikipedia  Kazakh  Cyrl / Latin / Arab  kk  5
Vietnamese Wikipedia  Vietnamese  Latn  vi  5
Danish Wikipedia  Danish  Latn  da  5
Esperanto Wikipedia  Esperanto  Latn  eo  5
Serbian Wikipedia  Serbian  Cyrl/Latn  sr  5
Indonesian Wikipedia  Indonesian  Latn  id  5
Lithuanian Wikipedia  Lithuanian  Latn  lt  5
Volapük Wikipedia  Volapük  Latn  vo  5
Slovak Wikipedia  Slovak  Latn  sk  5
Hebrew Wikipedia  Hebrew  Hebr  he  5
Persian Wikipedia  Persian  Perso  fa  5
Bulgarian Wikipedia  Bulgarian  Cyrl  bg  5
Slovene Wikipedia  Slovene  Latn  sl  5
Basque Wikipedia  Basque  Latn  eu  5
Waray-Waray Wikipedia  Waray-Waray  Latn  war  5
Lombard Wikipedia  Lombard  Latn  lmo  4
Estonian Wikipedia  Estonian  Latn  et  5
Croatian Wikipedia  Croatian  Latn  hr  5
Newar Wikipedia  Newar / Nepal Bhasa  Deva  new  4
Telugu Wikipedia  Telugu  Telu  te  4
Nynorsk Wikipedia  Norwegian (Nynorsk)  Latn  nn  4
Thai Wikipedia  Thai  Thai  th  4
Galician Wikipedia  Galician  Latn  gl  4
Greek Wikipedia  Greek  Grek  el  4
Cebuano Wikipedia  Cebuano  Latn  ceb  4
Simple English Wikipedia  Simple English  Latn  simple  4
Malay Wikipedia  Malay  Latn  ms  5
Haitian Creole Wikipedia  Haitian  Latn  ht  4
Bosnian Wikipedia  Bosnian  Latn  bs  4
Bishnupriya Manipuri Wikipedia  Bishnupriya Manipuri  Beng  bpy  4
Luxembourgish Wikipedia  Luxembourgish  Latn  lb  4
Georgian Wikipedia  Georgian  Geor  ka  4
Icelandic Wikipedia  Icelandic  Latn  is  4
Albanian Wikipedia  Albanian  Latn  sq  4
Latin Wikipedia  Latin  Latn  la  4
Breton Wikipedia  Breton  Latn  br  4
Hindi Wikipedia  Hindi  Deva  hi  5
Azerbaijani Wikipedia  Azerbaijani  Latn/Arab  az  4
Bengali Wikipedia  Bengali  Beng  bn  4
Macedonian Wikipedia  Macedonian  Cyrl  mk  4
Marathi Wikipedia  Marathi  Deva  mr  4
Serbo-Croatian Wikipedia  Serbo-Croatian  Latn/Cyrl  sh  4
Tagalog Wikipedia  Tagalog  Latn  tl  4
Welsh Wikipedia  Welsh  Latn  cy  4
Ido Wikipedia  Ido  Latn  io  4
Piedmontese Wikipedia  Piedmontese  Latn  pms  4
Latvian Wikipedia  Latvian  Latn  lv  4
Tamil Wikipedia  Tamil  Taml  ta  4
Sundanese Wikipedia  Sundanese  Latn  su  4
Occitan Wikipedia  Occitan  Latn  oc  4
Javanese Wikipedia  Javanese  Latn  jv  4
Neapolitan Wikipedia  Neapolitan  Latn  nap  4
Low Saxon Wikipedia  Low Saxon  Latn  nds  4
Sicilian Wikipedia  Sicilian  Latn  scn  4
Belarusian Wikipedia  Belarusian  Cyrl  be  4
Asturian Wikipedia  Asturian  Latn  ast  4
Kurdish Wikipedia  Kurdish  Latn/Arab  ku  4
Walloon Wikipedia  Walloon  Latn  wa  4
Afrikaans Wikipedia  Afrikaans  Latn  af  4
Belarusian (Taraškievica) Wikipedia  Belarusian (Taraškievica)  Cyrl  be-x-old  4
Aragonese Wikipedia  Aragonese  Latn  an  4
Ripuarian Wikipedia  Ripuarian  Latn  ksh  3
Silesian Wikipedia  Silesian  Latn  szl  3
West Frisian Wikipedia  West Frisian  Latn  fy  4
North Frisian Wikipedia  North Frisian  Latn  frr  3
Cantonese Wikipedia  Cantonese  Hant  yue  4
Urdu Wikipedia  Urdu  Arab  ur  4
Interlingua Wikipedia  Interlingua  Latn/Arab  ia  4
Irish Wikipedia  Irish  Latn  ga  4
Yiddish Wikipedia  Yiddish  Hebr  yi  3
Alemannic Wikipedia  Alemannic  Latn  als  4
Armenian Wikipedia  Armenian  Armn  hy  4
Amharic Wikipedia  Amharic  Geez  am  4
Aromanian Wikipedia  Aromanian  Latn  roa-rup  4
Banyumasan Wikipedia  Banyumasan  Latn  map-bms  3
Bihari Wikipedia  Bihari  Deva  bh  3
Corsican Wikipedia  Corsican  Latn  co  3
Chuvash Wikipedia  Chuvash  Latn  cv  4
Divehi Wikipedia  Divehi  Thaa  dv  3
Dutch Low Saxon Wikipedia  Dutch Low Saxon  Latn  nds-nl  3
Faroese Wikipedia  Faroese  Latn  fo  3
Friulian Wikipedia  Friulian  Latn  fur  3
Gilaki Wikipedia  Gilaki  Perso  glk  3
Gujarati Wikipedia  Gujarati  Gujr  gu  4
Ilokano Wikipedia  Ilokano  Latn  ilo  3
Kannada Wikipedia  Kannada  Knda  kn  4
Kapampangan Wikipedia  Kapampangan  Latn  pam  3
Kashubian Wikipedia  Kashubian  Latn  csb  3
Khmer Wikipedia  Khmer  Khmr  km  3
Ligurian Wikipedia  Ligurian  Latn  lij  3
Limburgish Wikipedia  Limburgish  Latn  li  3
Malayalam Wikipedia  Malayalam  Mlym  ml  4
Manx Wikipedia  Manx  Latn  gv  3
Māori Wikipedia  Māori  Latn  mi  3
Maltese Wikipedia  Maltese  Latn  mt  3
Nāhuatl Wikipedia  Nāhuatl  Latn  nah  3
Nepali Wikipedia  Nepali  Deva  ne  4
Norman Wikipedia  Norman  Latn  nrm  3
Northern Sami Wikipedia  Northern Sami  Latn  se  3
Novial Wikipedia  Novial  Latn  nov  3
Quechua Wikipedia  Quechua  Latn  qu  4
Ossetian Wikipedia  Ossetian  Cyrl  os  3
Pali Wikipedia  Pali  Deva  pi  3
Pangasinan Wikipedia  Pangasinan  Latn  pag  3
Pashto Wikipedia  Pashto  Arab  ps  3
Pennsylvania German Wikipedia  Pennsylvania German  Latn  pdc  3
Romansh Wikipedia[c]  Romansh  Latn  rm  3
Samogitian Wikipedia  Samogitian  Latn  bat-smg  4
Sanskrit Wikipedia  Sanskrit  Deva  sa  3
Scottish Gaelic Wikipedia  Scottish Gaelic  Latn  gd  3
Scots Wikipedia  Scots  Latn  sco  3
Sardinian Wikipedia  Sardinian  Latn  sc  3
Sinhalese Wikipedia  Sinhalese  Sinh  si  3
Tajik Wikipedia  Tajik  Cyrl  tg  3
Tarantino Wikipedia  Tarantino  Latn  roa-tara  3
Tatar Wikipedia  Tatar  Cyrl/Latn  tt  4
Tongan Wikipedia  Tongan  Latn  to  3
Turkmen Wikipedia  Turkmen  Latn  tk  3
Upper Sorbian Wikipedia  Upper Sorbian  Latn  hsb  3
Uzbek Wikipedia  Uzbek  Latn/Cyrl  uz  3
Venetian Wikipedia  Venetian  Latn  vec  3
Voro Wikipedia  Võro  Latn  fiu-vro  3
Wu Wikipedia  Wu  Hans  wuu  3
West Flemish Wikipedia  West Flemish  Latn  vls  3
Yoruba Wikipedia  Yoruba  Latn  yo  4
Zazaki Wikipedia  Zazaki  Latn  diq  4
Min Nan Wikipedia  Min Nan  Latn  zh-min-nan  3
Classical Chinese Wikipedia  Classical Chinese  Hant  zh-classical  3
Franco-Provençal Wikipedia  Franco-Provençal/Arpitan  Latn  frp  3
Ladino Wikipedia  Ladino  Latn  lad  3
Bavarian Wikipedia  Bavarian  Latn  bar  3
Central Bicolano Wikipedia  Central_Bicolano  Latn  bcl  3
Cornish Wikipedia  Cornish  Latn  kw  3
Mongolian Wikipedia  Mongolian  Cyrl  mn  3
Hawaiian Wikipedia  Hawaiian  Latn  haw  3
Anglo-Saxon Wikipedia  Anglo-Saxon  Latn  ang  3
Lingala Wikipedia  Lingala  Latn  ln  3
Interlingue Wikipedia  Interlingue  Latn  ie  3
Wolof Wikipedia  Wolof  Latn  wo  3
Tok Pisin Wikipedia  Tok Pisin  Latn  tpi  3
Tahitian Wikipedia  Tahitian  Latn  ty  2
Crimean Tatar Wikipedia  Crimean Tatar  Latn  crh  3
Lojban Wikipedia  Lojban  Latn  jbo  3
Aymara Wikipedia  Aymara  Latn  ay  3
Zealandic Wikipedia  Zealandic  Latn  zea  3
Emilian-Romagnol Wikipedia  Emilian-Romagnol  Latn  eml  3
Kyrgyz Wikipedia  Kyrgyz  Cyrl  ky  3
Igbo Wikipedia  Igbo  Latn  ig  2
Oriya Wikipedia  Oriya  Orya  or  3
Malagasy Wikipedia  Malagasy  Latn  mg  4
Zamboanga Chavacano Wikipedia  Zamboanga Chavacano  Latn  cbk-zam  3
Kongo Wikipedia  Kongo  Latn  kg  2
Syriac Wikipedia  Syriac  Syrc  arc  3
Vlax Romani Wikipedia  Vlax Romani  Latn/Deva  rmy  2
Guarani Wikipedia  Guarani  Latn  gn  3
Moldovan Wikipedia  Moldovan  Cyrl  mo (closed)  2
Somali Wikipedia  Somali  Latn  so  3
Kabyle Wikipedia  Kabyle  Latn  kab  2
Kashmiri Wikipedia  Kashmiri  Arab/Deva  ks  2
Saterland Frisian Wikipedia  Saterland Frisian  Latn  stq  3
Chechen Wikipedia  Chechen  Cyrl  ce  3
Udmurt Wikipedia  Udmurt  Cyrl  udm  3
Mazandarani Wikipedia  Mazandarani  Perso  mzn  3
Papiamentu Wikipedia  Papiamentu  Latn  pap  3
Old Church Slavonic Wikipedia  Old Church Slavonic  Cyrs  cu  2
Sakha Wikipedia  Sakha  Cyrl  sah  3
Tetum Wikipedia  Tetum  Latn  tet  2
Sindhi Wikipedia  Sindhi  Arab  sd  2
Lao Wikipedia  Lao  Laoo  lo  2
Bashkir Wikipedia  Bashkir  Cyrl  ba  3
Western Punjabi Wikipedia  Punjabi  Shahmukhi  pnb  4
Iniktitut Wikipedia  Inuktitut  Cans/Latn  iu  2
Nauruan Wikipedia  Nauruan  Latn  na  2
Gothic Wikipedia  Gothic  Goth  got  2
Tibetan Wikipedia  Tibetan  Tibt  bo  3
Lower Sorbian Wikipedia  Lower Sorbian  Latn  dsb  2
Cherokee Wikipedia  Cherokee  Cher  chr  2
Min Dong Wikipedia  Min Dong  Latn  cdo  2
Hakka Wikipedia  Hakka  Latn  hak  3
Oromo Wikipedia  Oromo  Latn  om  2
Burmese Wikipedia  Burmese  Mymr  my  4
Samoan Wikipedia  Samoan  Latn  sm  2
Ewe Wikipedia  Ewe  Latn  ee  2
Picard Wikipedia  Picard  Latn  pcd  3
Uyghur Wikipedia  Uyghur  Latn/Arab  ug  3
Assamese Wikipedia  Assamese  Beng  as  2
Tigrinya Wikipedia  Tigrinya  Ethi  ti  2
Avar Wikipedia  Avar  Cyrl  av  3
Bambara Wikipedia  Bambara  Latn  bm  2
Zulu Wikipedia  Zulu  Latn  zu  2
Pontic Wikipedia  Pontic  Grek  pnt  2
Navajo Wikipedia  Navajo  Latn  nv  3
Cree Wikipedia  Cree  Cans/Latn  cr  2
Norfolk Wikipedia  Norfolk  Latn  pih  2
Swati Wikipedia  Swati  Latn  ss  2
Venda Wikipedia  Venda  Latn  ve  2
Bislama Wikipedia  Bislama  Latn  bi  2
Kinyarwanda Wikipedia  Kinyarwanda  Latn  rw  3
Chamorro Wikipedia  Chamorro  Latn  ch  2
Egyptian Arabic Wikipedia  Egyptian Arabic  Arab/Latn  arz  3
Xhosa Wikipedia  Xhosa  Latn  xh  2
Greenlandic Wikipedia  Greenlandic  Latn  kl  3
Inupiak Wikipedia  Inupiak  Latn  ik  2
Buginese Wikipedia  Buginese  Bugi  bug  4
Dzongkha Wikipedia  Dzongkha  Tibt  dz  2
Tsonga Wikipedia  Tsonga  Latn  ts  2
Tswana Wikipedia  Tswana  Latn  tn  2
Komi Wikipedia  Komi  Cyrl  kv  3
Tumbuku Wikipedia  Tumbuka  Latn  tum  2
Kalmyk Wikipedia  Kalmyk  Cyrl  xal  3
Sesotho Wikipedia  Sesotho  Latn  st  2
Twi Wikipedia  Twi  Latn  tw  2
Buryat (Russia) Wikipedia  Buryat (Russia)  Cyrl  bxr  2
Akan Wikipedia  Akan  Latn  ak  2
Abkhazian Wikipedia  Abkhazian  Cyrl  ab  2
Chichewa Wikipedia  Chichewa  Latn  ny  2
Fijian Wikipedia  Fijian  Latn  fj  2
Lak Wikipedia  Lak  Cyrl  lbe  3
Kikuyu Wikipedia  Kikuyu  Latn  ki  2
Zhuang Wikipedia  Zhuang  Latn  za  2
Fula Wikipedia  Fula  Latn  ff  2
Luganda Wikipedia  Luganda  Latn  lg  2
Shona Wikipedia  Shona  Latn  sn  2
Hausa Wikipedia  Hausa  Latn  ha  2
Sango Wikipedia  Sango  Latn  sg  2
Sichuan Yi Wikipedia  Sichuan Yi  Yiii  ii  1
Choctaw Wikipedia  Choctaw  Latn  cho  1
Kirundi Wikipedia  Kirundi  Latn  rn  2
Marshallese Wikipedia  Marshallese  Latn  mh  1
Cheyenne Wikipedia  Cheyenne  Latn  chy  2
Ndonga Wikipedia  Ndonga  Latn  ng  1
Kuanyama Wikipedia  Kuanyama  Latn  kj  0
Hiri Motu Wikipedia  Hiri Motu  Latn  ho  0
Muscogee Wikipedia  Muscogee  Latn  mus  0
Kanuri Wikipedia  Kanuri  Latn  kr  0
Herero Wikipedia  Herero  Latn  hz  0
Moloko Wikipedia  Moloko  Latn  mwl  2
Punjabi Wikipedia  Punjabi  Guru  pa  3
Mingrelian Wikipedia  Mingrelian  Geor  xmf  3
Lezgi Wikipedia  Lezgian  Cyrl  lez  2
Champenois Wikipedia  Champenoisian  Latn  chm  2"""

# from http://borel.slu.edu/crubadan/stadas.html
crubadantable = """Code  Name (English)  Name (Native)  ISO 639-3  Country  Docs  Words  Characters  SIL  WT  WP  UDHR  Close to  Polluters  FLOSS SplChk  Contact(s)  Updated  Alternate names  Classification
aa  Afar  Qafár af  aar  Ethiopia  20  53904  366504  AFR  -  aa  -  so om  en  no  -  Mon Dec 2 10:23:06 CST 2013  AFARAF, 'DANAKIL', 'DENKEL', AFAR AF, ADAL  Afro-Asiatic, Cushitic, East, Saho-Afar.
aae  Arbëreshë Albanian  -  aae  Italy  0  0  0  AAE  -  -  -  als  en  no  -  -  ARBËRESHË  Indo-European, Albanian, Tosk.
aaf  Aranadan  Aranatan  aaf  India  2  165  1274  AAF  -  -  -  dwr gof wal so  en  no  -  Mon Sep 23 10:59:44 CDT 2013  ERANADANS  Dravidian, Southern, Tamil-Kannada, Tamil-Kodagu, Tamil-Malayalam, Malayalam.
aai  Arifama-Miniafia  -  aai  Papua New Guinea  290  258829  1673286  AAI  -  -  -  mpx ubr bik  en  no  -  Fri Dec 28 21:45:17 CST 2012  MINIAFIA-ARIFAMA  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Nuclear, North Papuan Mainland-D'Entrecasteaux, Are-Taupota, Are.
aak  Ankave  -  aak  Papua New Guinea  288  350667  2823796  AAK  -  -  -  aoj ttg byr-x-waga cok byr ake  en  no  -  Tue Jun 12 20:28:41 CDT 2012  ANGAVE  Trans-New Guinea, Main Section, Central and Western, Angan, Angan Proper.
aat  Arvanitika Albanian  -  aat  Greece  1  162  887  AAT  -  -  -  als aae aln zac  en  no  -  Sat Feb 16 09:46:23 CST 2013  ARVANITIKA, ARVANITIC, ARBERICHTE  Indo-European, Albanian, Tosk.
aau  Abau  -  aau  Papua New Guinea  280  445768  2527506  AAU  -  -  -  chk ach awi ibl pon  en  no  -  Tue Jun 12 20:40:40 CDT 2012  GREEN RIVER  Sepik-Ramu, Sepik, Upper Sepik, Abau.
ab  Abkhaz  Аҧсуа  abk  Georgia  1289  319734  2752660  ABK  abk*  ab  abk  ce  en ru  no  -  Sat Sep 7 04:55:23 CDT 2013  ABXAZO, ABKHAZIAN  North Caucasian, Northwest, Abkhaz-Abazin.
abe  Western Abnaki  -  abe  Canada  1  176  1404  ABE  -  -  -  ify vmw mpx dag cr-Latn swh  en  no  -  Thu Jan 31 13:38:42 CST 2013  ABENAKI, ABENAQUI, ST. FRANCIS  Algic, Algonquian, Eastern.
abn  Abua  Abuan  abn  Nigeria  2  3057  18024  ABN  au  -  -  ify vmw yap dag yo lgg  en  no  -  Mon Oct 1 17:10:49 CDT 2012  ABUAN  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Cross River, Delta Cross, Central Delta, Abua-Odual.
abt  Ambulas  -  abt  Papua New Guinea  575  821688  5191595  ABT  -  -  -  wos sw wmw swh pkb swc kki tum ian dgz gog swb lu  en  no  -  Sun Dec 30 12:17:34 CST 2012  ABULAS, ABELAM  Sepik-Ramu, Sepik, Middle Sepik, Ndu.
abt-x-maprik  Ambulas Maprik  -  abt  Papua New Guinea  286  358612  2158555  ABT  -  -  -  swh swc wmw  en  no  -  Sun Dec 30 11:15:49 CST 2012  ABULAS, ABELAM  Sepik-Ramu, Sepik, Middle Sepik, Ndu.
abt-x-wosera  Ambulas Wosera Kamu  -  abt  Papua New Guinea  287  333978  2226682  ABT  -  -  -  abt-x-maprik swh swc wmw  en  no  -  Sun Dec 30 11:28:17 CST 2012  ABULAS, ABELAM  Sepik-Ramu, Sepik, Middle Sepik, Ndu.
abx  Inabaknon  -  abx  Philippines  4  43898  283607  ABX  -  -  -  war hil  en  no  -  Mon Jan 7 20:52:51 CST 2013  ABAKNON, INBAKNON, INABAKNON, CAPUL, CAPULEÑO, KAPUL  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Sama-Bajaw, Abaknon.
aby  Aneme Wake  -  aby  Papua New Guinea  287  280468  1721323  ABY  -  -  -  wmw  en  no  -  Sun Dec 30 12:30:55 CST 2012  ABIE, ABIA  Trans-New Guinea, Main Section, Eastern, Central and Southeastern, Yareban.
acc  Cubulco Achi’  -  acc  Guatemala  2  417267  1980126  ACC  -  -  -  quj pob poh ckk cbm tzj-x-eastern usp qut tzt cki quc ckw acr tzj chf  en es  no  -  Mon Oct 1 17:40:23 CDT 2012  -  Mayan, Quichean-Mamean, Greater Quichean, Quichean, Quiche-Achi.
acd  Gikyode  -  acd  Ghana  1  309496  1497842  ACD  -  -  -  ak nzi  en  no  -  Sun Dec 30 11:05:51 CST 2012  -  Niger-Congo, Atlantic-Congo, Volta-Congo, Kwa, Nyo, Potou-Tano, Tano, Guang, North Guang.
ace  Aceh  Bahsa Acèh  ace  Indonesia (Sumatra)  11  820313  5388260  ATJ  -  ace  atj  su id  en id  no  -  Fri Dec 28 16:19:23 CST 2012  ATJEH, ATJEHNESE, ACHINESE, ACHEHNESE  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Sundic, Malayic, Achinese-Chamic, Achinese.
acf  Saint Lucian Creole French  Kwéyòl  acf  Saint Lucia  30  520449  2549694  ACF  -  -  -  en mfe bik lou hnn  en fr  no  -  Wed Sep 18 15:32:23 CDT 2013  Dominican Creole French, Grenadian Creole French, Kwéyòl, Lesser Antillean Creole French, Patois, Patwa  Creole, French based
ach  Acholi  Acholi  ach  Uganda  236  352653  1936682  ACO  ac  -  -  luo alz bts loa  en  no  -  Sat Feb 2 11:02:20 CST 2013  ACOLI, ATSCHOLI, SHULI, GANG, LWO, LWOO, AKOLI, ACOOLI, LOG ACOLI, DOK ACOLI  Nilo-Saharan, Eastern Sudanic, Nilotic, Western, Luo, Southern, Luo-Acholi, Alur-Acholi, Lango-Acholi.
acn  Achang  -  acn  China  1  231686  1258625  ACN  -  -  -  bo-Latn  en  no  -  Sun Dec 30 19:59:30 CST 2012  ACHUNG, ATSANG, ACH'ANG, ACANG, AHCHAN, NGACANG, NGATSANG, NGACHANG, NGAC'ANG, NGO CHANG, MÖNGHSA  Sino-Tibetan, Tibeto-Burman, Lolo-Burmese, Burmish, Northern.
acr  Achi  -  acr  Guatemala  2  268859  1523083  ACR  -  -  -  cak qut cki ckw quc cke usp quj acc pob poh mhi  en es  no  -  Fri Jan 25 09:59:31 CST 2013  RABINAL QUICHÉ  Mayan, Quichean-Mamean, Greater Quichean, Quichean, Quiche-Achi.
acr-x-rabinal  Rabinal Achi’  -  acr  Guatemala  0  0  0  ACR  -  -  -  cak qut cki ckw quc cke usp quj acc pob poh mhi  en es  no  -  -  RABINAL QUICHÉ  Mayan, Quichean-Mamean, Greater Quichean, Quichean, Quiche-Achi.
act  Achterhoeks  -  act  Netherlands  1  702  3512  ACT  -  -  -  nds-NL nl vls zea nds li fy  en  no  -  Thu Mar 14 10:33:04 CDT 2013  ACHTERHOEK, AACHTERHOEKS  Indo-European, Germanic, West, Low Saxon-Low Franconian, Low Saxon.
acu  Achuar-Shiwiar  -  acu  Peru  6  393214  2830621  ACU  -  -  acu  hub jiv agr  en  no  -  Wed Jan 30 20:56:20 CST 2013  ACHUAR, ACHUAL, ACHUARA, ACHUALE, JIVARO, MAINA  Jivaroan.
ada  Dangme  Dangme  ada  Ghana  217  345824  1658440  DGM  dg  -  gac1  sil gjn sbd kbp tpm ajg dts  en  no  -  Sat Feb 2 11:03:11 CST 2013  ADANGME  Niger-Congo, Atlantic-Congo, Volta-Congo, Kwa, Nyo, Ga-Dangme.
ade  Adele  -  ade  Togo  1  259184  1211917  ADE  -  -  -  knk emk snk dyu wwa hag bjn bba  en  no  -  Sun Dec 30 15:56:45 CST 2012  BIDIRE, BEDERE, GIDIRE, GADRE  Niger-Congo, Atlantic-Congo, Volta-Congo, Kwa, Nyo, Potou-Tano, Basila-Adele.
adh  Adhola  Jopadhola  adh  Uganda  0  0  0  ADH  -  -  -  luo ach alz loa tby bts  en  no  -  -  DHOPADHOLA, JOPADHOLA, LUDAMA  Nilo-Saharan, Eastern Sudanic, Nilotic, Western, Luo, Southern, Adhola.
adj  Adioukrou  -  adj  Côte d’Ivoire  5  281098  1230194  ADJ  -  -  -  dgi pau kno maf vap cfm bum  en  no  -  Fri Jan 25 09:59:42 CST 2013  ADYUKRU, ADJUKRU, ADYOUKROU, AJUKRU  Niger-Congo, Atlantic-Congo, Volta-Congo, Kwa, Nyo, Agneby.
ady  Adyghe  Адыгабзэ  ady  Russian Federation  102  44124  350315  ADY  ad  -  -  kbd cu  en  no  -  Wed Sep 18 17:44:34 CDT 2013  CIRCASSIAN, LOWER CIRCASSIAN, KIAKH, KJAX, WEST CIRCASSIAN, ADYGEI, ADYGEY  North Caucasian, Northwest, Circassian.
adz  Adzera  -  adz  Papua New Guinea  52  64852  348794  AZR  -  -  -  ha tbc ka-Latn bjn krl tmh iry zsm ms ifk id  en  no  -  Fri Dec 28 19:14:19 CST 2012  AZERA, ATZERA, ACIRA  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Huon Gulf, Markham, Upper, Adzera.
aeb-Latn  Tunisian Spoken Arabic  Tounsi  aeb  Tunisia  9  1215  9131  AEB  -  -  -  ca yby  en  no  -  Fri Sep 20 12:41:35 CDT 2013  TUNISIAN  Afro-Asiatic, Semitic, Central, South, Arabic.
aer  Eastern Arrernte  Arrernte  aer  Australia  8  8550  56782  AER  -  -  -  scn-x-tara  en  no  -  Sat Jan 12 07:14:46 CST 2013  EASTERN ARANDA, ARUNTA  Australian, Pama-Nyungan, Arandic, Urtwa.
aey  Amele  -  aey  Papua New Guinea  332  383749  2299615  AMI  -  -  -  viv mpx wed-x-topura aui mox kud gri pwg tpa dob tbo tte wed  en  no  -  Fri Dec 28 19:17:08 CST 2012  AMALE  Trans-New Guinea, Madang-Adelbert Range, Madang, Mabuso, Gum.
af  Afrikaans  Afrikaans  afr  South Africa  1307  5159756  31935777  AFK  af  af  afk  nl li vls zea nds-NL vmf  en  yes  Darrin Speegle, Petri Jooste, Tjaart Van der Walt, Friedel Wolff  Sat Feb 2 11:54:24 CST 2013  -  Indo-European, Germanic, West, Low Saxon-Low Franconian, Low Franconian.
agd  Agarabi  -  agd  Papua New Guinea  287  334810  1915902  AGD  -  -  -  sml ha bik  en  no  -  Sun Dec 30 12:44:54 CST 2012  AGARABE, BARE  Trans-New Guinea, Main Section, Central and Western, East New Guinea Highlands, Eastern, Gadsup-Auyana-Awa.
agg  Angor  -  agg  Papua New Guinea  289  248922  2024813  AGG  -  -  -  aia  en  no  -  Sun Dec 30 12:49:33 CST 2012  WATAPOR, SENAGI, ANGGOR  Trans-New Guinea, Senagi.
agm  Angaataha  -  agm  Papua New Guinea  294  394403  3646780  AGM  -  -  -  agg byr-x-waga rao byr ian iws ghs slm gdn nif old gof cbu  en  no  -  Fri Dec 28 19:19:28 CST 2012  LANGIMAR, ANGATAHA, ANGAATIYA, ANGAATAHA  Trans-New Guinea, Main Section, Central and Western, Angan.
agn  Agutaynen  -  agn  Philippines  8  243963  1447677  AGN  -  -  -  tl pam jv kyk msk krj  en  no  -  Sun Dec 30 18:28:07 CST 2012  AGUTAYNON, AGUTAYNO  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Meso Philippine, Kalamian.
agp  Paranan  -  agp  Philippines  0  0  0  AGP  -  -  -  kne mqb pag srn dgc djk due ivv ifk  en  no  -  -  PALANENYO, PLANAN  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Northern Philippine, Northern Luzon, Northern Cordilleran, Dumagat, Northern.
agr  Aguaruna  -  agr  Peru  3  235234  1867796  AGR  -  -  agr  hub acu jiv  en  no  -  Sun Dec 23 12:07:17 CST 2012  AGUAJUN, AHUAJUN  Jivaroan.
agu  Awakateko  -  agu  Guatemala  3  738310  4082724  AGU  -  -  -  mvc  en es  no  -  Sun Dec 23 12:09:43 CST 2012  AGUACATEC  Mayan, Quichean-Mamean, Greater Mamean, Ixilan.
agx  Aghul  Агъул  agx  Russian Federation  5  1153  9185  AGX  -  -  -  lez uzn sah dar tab gag-Cyrl ky cv tg ce  en  no  -  Fri Sep 20 12:11:44 CDT 2013  AGUL, AGHULSHUY, AGULY  North Caucasian, Northeast, Lezgian.
ahk  Akha  Akha  ahk  Myanmar  2  352503  1731761  AKA  aka  -  -  lhu  en  no  -  Fri Jan 25 10:00:24 CST 2013  KAW, EKAW, KO, AKA, IKAW, AK'A, AHKA, KHAKO, KHA KO, KHAO KHA KO, IKOR, AINI, YANI  Sino-Tibetan, Tibeto-Burman, Lolo-Burmese, Loloish, Southern, Akha, Hani, Ha-Ya.
aia  Arosi  -  aia  Solomon Islands  2  266479  1613017  AIA  -  -  -  stn gri alu wed snc mlu meu rro ksd kwf khz bts ho npy  en  no  -  Sun Dec 23 12:09:31 CST 2012  -  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Southeast Solomonic, Malaita-San Cristobal, San Cristobal.
aii  Neo-Aramaic Assyrian  -  aii  Iraq  3  35014  220739  AII  as*  arc  aii  -  en  no  -  Mon Jan 7 21:08:05 CST 2013  LISHANA ATURAYA, SURET, SURETH, SURYAYA SWADAYA, ASSYRIAN, NEO-SYRIAC, ASSYRISKI, AISORSKI, ASSYRIANCI  Afro-Asiatic, Semitic, Central, Aramaic, Eastern, Central, Northeastern.
ain  Ainu  Ainu Itak  ain  Japan  8  38030  287107  AIN  -  -  -  ppl mbt mbi gba kqn  en  no  -  Wed Sep 18 18:31:55 CDT 2013  AINU ITAK  Language Isolate.
ajg  Aja  -  ajg  Benin  35  62419  285341  AJG  -  -  aja  fon ee knk hna kno dgi ak bwu  en  no  -  Sat Feb 16 17:06:52 CST 2013  AJA, ADJA, HWÈ  Niger-Congo, Atlantic-Congo, Volta-Congo, Kwa, Left Bank, Gbe, Aja.
ak  Akan  Akan  aka  Ghana  176  367192  2009819  TWS  tw  ak  tws1  srr ja-Latn kno bum knk yal bwq mk-Latn  en  yes  Paa Kwesi Imbeah, Jojoo Imbeah  Sun Nov 3 16:20:45 CST 2013  -  Niger-Congo, Atlantic-Congo, Volta-Congo, Kwa, Nyo, Potou-Tano, Tano, Central, Akan.
ake  Akawaio  -  ake  Guyana  2  195625  1228079  ARB  -  -  -  pbc ubr nss msm  en  no  -  Fri Jan 25 10:06:03 CST 2013  ACEWAIO, AKAWAI, ACAHUAYO, KAPON  Carib, Northern, East-West Guiana, Macushi-Kapon, Kapon.
akh  Angal Heneng  -  akh  Papua New Guinea  0  0  0  AKH  -  -  -  sua hui tet gil btd  en  no  -  -  AUGU, WEST MENDI, WEST ANGAL HENENG, AGARAR, WAGE, KATINJA  Trans-New Guinea, Main Section, Central and Western, East New Guinea Highlands, West-Central, Angal-Kewa.
akl  Inakeanon  -  akl  Philippines  3  3240  19307  AKL  ikn  -  -  hil krj war hnn kyk bch bno bik mmn bku iry tl itv abx ceb sml  en  no  -  Fri Sep 13 17:29:10 CDT 2013  AKLAN, AKLANO, PANAY, AKLANON-BISAYAN  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Meso Philippine, Central Philippine, Bisayan, West, Aklan.
akz  Alabama  Albaamo innaaɬiilka  akz  USA  4  1278  10632  AKZ  -  -  -  csk tos dag kek ng mt art-x-tokipona loz  en  no  -  Fri Sep 20 10:57:21 CDT 2013  ALIBAMU  Muskogean, Eastern.
aln  Gheg Albanian  Gegnisht  aln  Serbia  2  395  3265  ALS  -  -  -  als aae zac  en  no  -  Wed Sep 18 18:50:53 CDT 2013  GEG  Indo-European, Albanian, Gheg.
alp  Alune  -  alp  Indonesia (Maluku)  0  0  0  ALP  -  -  -  rmy rug mva tvl yss-x-yawu ssx yss rom st  en  no  -  -  SAPALEWA, PATASIWA ALFOEREN  Austronesian, Malayo-Polynesian, Central-Eastern, Central Malayo-Polynesian, Central Maluku, East, Seram, Nunusaku, Three Rivers, Amalumute, Northwest Seram, Ulat Inai.
alr  Alutor  -  alr  Russian Federation  3  6736  51719  ALR  -  -  -  ckt kpy lez  en ru  no  -  Sat Feb 2 21:54:27 CST 2013  ALYUTOR, ALIUTOR, OLYUTOR  Chukotko-Kamchatkan, Northern, Koryak-Alyutor.
als  Tosk Albanian  -  als  Albania  1274  2908306  18978784  ALN  -  -  aln  aae aln zac  en  yes  -  Thu Jan 31 10:22:25 CST 2013  TOSK, ARNAUT, SHKIP, SHQIP, SKCHIP, SHQIPERË, ZHGABE  Indo-European, Albanian, Tosk.
alt  Southern Altai  Алтай  alt  Russian Federation  3  7683  56440  ALT  alt  -  alt  ky kaa-Cyrl kk  en  no  -  Wed Sep 18 18:53:53 CDT 2013  OIROT, OYROT, ALTAI  Altaic, Turkic, Northern.
alu  ’Are’are  -  alu  Solomon Islands  1  1360  7302  ALU  -  -  -  stn kwf gri haw  en  no  Katerine Naitoro  Tue Jan 22 15:32:06 CST 2013  AREARE  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Southeast Solomonic, Malaita-San Cristobal, Malaita, Southern.
alz  Alur  -  alz  Dem. Rep. of Congo  0  0  0  ALZ  -  -  -  luo ach adh tsc yap bts cri agd gup  en  no  -  -  LUR, ALORO, ALUA, ALULU, LURI, DHO ALUR, JO ALUR  Nilo-Saharan, Eastern Sudanic, Nilotic, Western, Luo, Southern, Luo-Acholi, Alur-Acholi, Alur.
am  Amharic  አማርኛ  amh  Ethiopia  551  1225957  6712469  AMH  am*  am  amh  ti tig  en  yes  Biniam Gebremichael, Aynalem Tesfaye  Sat Feb 2 11:53:51 CST 2013  ABYSSINIAN, ETHIOPIAN, AMARINYA, AMARIGNA  Afro-Asiatic, Semitic, South, Ethiopian, South, Transversal, Amharic-Argobba.
am-Latn  Amharic (Latin)  -  amh  Ethiopia  4  17101  134480  AMH  -  -  -  ti-Latn ms  en  no  -  Sat Jan 26 14:52:03 CST 2013  ABYSSINIAN, ETHIOPIAN, AMARINYA, AMARIGNA  Afro-Asiatic, Semitic, South, Ethiopian, South, Transversal, Amharic-Argobba.
amc  Amahuaca  -  amc  Peru  2  6123  58309  AMC  -  -  amc  shp kaq cao  en  no  -  Sat Jan 12 07:37:57 CST 2013  AMAWAKA, AMAGUACO, AMEUHAQUE, IPITINERI, SAYACO  Panoan, South-Central, Amahuaca.
ame  Yanesha'  -  ame  Peru  3  199124  1084981  AME  -  -  ame  sv kup byx mus toc  en  no  Anna Luisa Daigneault  Sun Dec 23 12:13:36 CST 2012  AMUESHA, AMUESE, AMUEIXA, AMOISHE, AMAGUES, AMAGE, OMAGE, AMAJO, LORENZO, AMUETAMO, AMAJE, YANESHA'  Arawakan, Maipuran, Western Maipuran.
ami  Amis  Pangcah  ami  Taiwan  1  8616  55303  ALV  ai  -  -  pag mqb msm bku  en  no  -  Sat Jan 12 08:35:23 CST 2013  AMI, AMIA, PAGCAH, PANGTSAH, BAKURUT, LAM-SI-HOAN, MARAN, SABARI, TANAH  Austronesian, Formosan, Paiwanic.
amm  Ama  -  amm  Papua New Guinea  287  291696  1876789  AMM  -  -  -  ja-Latn udu tgp knv  en  no  -  Sun Dec 30 12:51:06 CST 2012  SAWIYANU  Left May.
amn  Amanab  -  amn  Papua New Guinea  285  264391  1573739  AMN  -  -  -  mpx stn  en  no  -  Sun Dec 30 18:42:38 CST 2012  -  Trans-New Guinea, Northern, Border, Waris.
amp  Alamblak  -  amp  Papua New Guinea  288  336584  2244363  AMP  -  -  -  cjv hix opm sua luo izr  en  no  -  Fri Dec 28 19:20:00 CST 2012  -  Sepik-Ramu, Sepik, Sepik Hill, Alamblak.
amr  Amarakaeri  Amarakaeri  amr  Peru  4  127322  647051  AMR  -  -  amr  nch umb nhw nhe nah wwa mk-Latn dtp aro kea nap ff  en  no  -  Wed Sep 18 18:55:55 CDT 2013  AMARAKAIRE, AMARACAIRE, 'MASHCO'  Harakmbet.
amu  Guerrero Amuzgo  -  amu  Mexico  7  295118  2068912  AMU  -  -  -  ln azg gri fj nfr bgt ki xsm meu ktu pwg  en  no  -  Sun Dec 23 12:19:42 CST 2012  -  Oto-Manguean, Amuzgoan.
an  Aragonese  Aragonés  arg  Spain  6  2043664  12431494  AXX  -  an  -  es-MX es gl ast oc ext cbk ca lnc gsc pt  en es  yes  Guillermo Frías Marín, Juan Pablo Martínez Cortes  Fri Sep 13 11:14:00 CDT 2013  ARAGOIERAZ, ALTOARAGONÉS, ARAGONÉS, FABLA ARAGONESA, PATUÉS, HIGH ARAGONESE  Indo-European, Italic, Romance, Italo-Western, Western, Pyrenean-Mozarabic, Pyrenean.
ane  Xârâcùù  -  ane  New Caledonia  24  18724  91773  ANE  -  -  -  maf  en  no  -  Fri Sep 13 12:36:21 CDT 2013  XARACII, ANESU, HARANEU, KANALA, CANALA  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, New Caledonian, Southern, South, Xaracuu-Xaragure.
ang  Anglo-Saxon  Englisc  ang  -  2  109591  731868  -  -  ang  -  zea de da en  en  no  -  Sat Jan 12 08:51:26 CST 2013  -  Indo-European, Germanic, West, English.
ann  Obolo  -  ann  Nigeria  2  235112  1289235  ANN  -  -  -  efi  en  no  -  Sun Dec 30 20:18:46 CST 2012  ANDONI, ANDONE, ANDONNI  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Cross River, Delta Cross, Lower Cross, Obolo.
anv  Denya  -  anv  Cameroon  1  214414  1145402  ANV  -  -  -  lem bss mcu zpi ak gba  en  no  -  Sun Dec 30 21:16:36 CST 2012  ANYANG, AGNANG, ANYAN, ANYAH, EYAN, TAKAMANDA, OBONYA, NYANG  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Mamfe.
aoj  Mufian  -  aoj  Papua New Guinea  275  360998  2362644  AOJ  -  -  -  pwg  en  no  -  Fri Dec 28 19:47:38 CST 2012  SOUTHERN ARAPESH, MUHIANG, MUHIAN  Torricelli, Kombio-Arapesh, Arapesh.
aoj-x-filifita  Filifita  -  aoj  Papua New Guinea  287  278018  1808646  AOJ  -  -  -  aoj bts pwg sml  en  no  -  Wed Jan 9 08:55:03 CST 2013  SOUTHERN ARAPESH, MUHIANG, MUHIAN  Torricelli, Kombio-Arapesh, Arapesh.
aom  Ömie  -  aom  Papua New Guinea  282  315373  2281456  AOM  -  -  -  apz mcq ghs gvc  en  no  -  Fri Dec 28 19:54:46 CST 2012  AOMIE, UPPER MANAGALASI  Trans-New Guinea, Main Section, Eastern, Central and Southeastern, Koiarian, Baraic.
aon  Bumbita Arapesh  -  aon  Papua New Guinea  289  348726  2250892  AON  -  -  -  ape mer  en  no  -  Wed Jan 9 09:26:56 CST 2013  WERI  Torricelli, Kombio-Arapesh, Arapesh.
apa  Apache languages  -  apa  USA  2  155454  1226592  -  -  -  -  nv  en  no  -  Mon Sep 23 19:27:40 CDT 2013  COYOTERO  Na-Dene, Nuclear Na-Dene, Athapaskan-Eyak, Athapaskan, Apachean, Apache.
ape  Bukiyip  -  ape  Papua New Guinea  265  375236  2483531  APE  -  -  -  min zlm  en  no  -  Wed Jan 9 09:39:10 CST 2013  BUKIYÚP, MOUNTAIN ARAPESH  Torricelli, Kombio-Arapesh, Arapesh.
apm  Mescalero-Chiricahua Apache  -  apm  USA  0  0  0  APM  -  -  -  apw nv mps nso myk chd  en  no  -  -  -  Na-Dene, Nuclear Na-Dene, Athapaskan-Eyak, Athapaskan, Apachean, Navajo-Apache, Eastern Apache.
apn  Apinayé  -  apn  Brazil  2  26930  136011  APN  -  -  -  txu ram alu gri stn haw kzf mk-Latn xsm  en  no  -  Sun Dec 23 12:21:18 CST 2012  APINAJÉ, APINAGÉ  Macro-Ge, Ge-Kaingang, Ge, Northwest, Apinaye.
apu  Apurinã  -  apu  Brazil  6  418637  3581562  APU  -  -  -  cjo cpu mcb snc pad lgg sn kwj kqc  en  no  -  Sun Dec 23 12:21:39 CST 2012  IPURINÃN, KANGITE, POPENGARE  Arawakan, Maipuran, Southern Maipuran, Purus.
apw  Western Apache  -  apw  USA  1  155278  1224705  APW  -  -  -  nv  en  no  -  Sun Dec 23 12:25:45 CST 2012  COYOTERO  Na-Dene, Nuclear Na-Dene, Athapaskan-Eyak, Athapaskan, Apachean, Navajo-Apache, Western Apache-Navajo.
apy  Apalaí  -  apy  Brazil  5  269046  1881632  APA  -  -  -  car guz zia wiu mgd alu trn  en  no  -  Sun Dec 23 12:28:58 CST 2012  APARAI, APALAY  Carib, Northern, East-West Guiana, Wayana-Trio.
apz  Safeyoka  -  apz  Papua New Guinea  291  327588  2685881  APZ  -  -  -  mnb ak gog tw amm kyg adh aom ja-Latn ino  en  no  -  Fri Dec 28 20:15:05 CST 2012  AMPALE, AMPELE, AMBARI, SAFEYOKA  Trans-New Guinea, Main Section, Central and Western, Angan, Angan Proper.
ar  Arabic  العربية  ara  Saudi Arabia  1188  1487149  9860456  -  a  ar  arz  prs lki ur pes sd  en  yes  -  Thu Jan 31 07:52:12 CST 2013  HIGH ARABIC, AL FUS-HA, AL ARABIYA  Afro-Asiatic, Semitic, Central, South, Arabic.
ar-Latn-x-chat  Arabic (Chat Alphabet)  -  ara  Egypt  57  123331  721921  -  -  -  -  pau ext es  en  no  -  Sat Jan 12 10:48:55 CST 2013  -  Afro-Asiatic, Semitic, Central, South, Arabic.
arb  Standard Arabic  العربية  arb  Saudi Arabia  809  1049780  6796267  ABV  a  ar  arz  arz  en  yes  -  Sat Jan 12 11:14:38 CST 2013  HIGH ARABIC, AL FUS-HA, AL ARABIYA  Afro-Asiatic, Semitic, Central, South, Arabic.
arl  Arabela  -  arl  Peru  3  271774  2444526  ARL  -  -  arl  mer cul cao cav snc apu hch ki cni  en  no  -  Sun Dec 23 12:49:37 CST 2012  CHIRIPUNO, CHIRIPUNU  Zaparoan.
arn  Mapudungun  Mapudungun  arn  Chile  35  327450  2100131  ARU  mpd  -  aru  tzc tzo  en es  no  Mónica Olivares Flández  Wed Sep 18 18:59:23 CDT 2013  MAPUDUNGU, 'ARAUCANO', MAPUCHE  Araucanian.
aro  Araona  Orqnchi'a Aqoana  aro  Bolivia  2  921  7391  ARO  -  -  -  tna ese  en  no  -  Wed Sep 18 19:01:38 CDT 2013  CAVINA  Tacanan, Araona-Tacana, Araona.
arp  Arapaho  -  arp  USA  2  44835  452553  ARP  -  -  -  npy aia noa  en  no  -  Sat Jan 12 10:49:20 CST 2013  ARRAPAHOE  Algic, Algonquian, Plains, Arapaho.
art-x-tokipona  Toki Pona  Toki Pona  art  -  0  0  0  -  -  -  -  loz mt tos  en  started  -  -  -  Artificial.
ary-Latn  Moroccan Spoken Arabic  الدّارجة  ary  Morocco  0  0  0  ARY  -  -  -  ha knv slm sgb sml aeb-Latn swh sbl knv-x-ara sw  en  no  -  -  MAGHREBI ARABIC, MAGHRIBI COLLOQUIAL ARABIC  Afro-Asiatic, Semitic, Central, South, Arabic.
arz  Egyptian Spoken Arabic  مصرى  arz  Egypt  0  0  0  ARZ  -  arz  -  arb  en  no  -  -  LOWER EGYPT ARABIC, NORMAL EGYPTIAN ARABIC  Afro-Asiatic, Semitic, Central, South, Arabic.
as  Assamese  অসমীয়া  asm  India  140  438433  2876864  ASM  ae  as  asm*  bn bpy  en  yes  Amitakhya Phukan  Fri Sep 13 12:35:07 CDT 2013  ASAMBE, ASAMI, ASAMIYA  Indo-European, Indo-Iranian, Indo-Aryan, Eastern zone, Bengali-Assamese.
aso  Dano  -  aso  Papua New Guinea  288  355862  2375605  ASO  -  -  -  gba zpi mbi ain  en  no  -  Wed Jan 9 09:54:16 CST 2013  UPPER ASARO, ASARO  Trans-New Guinea, Main Section, Central and Western, East New Guinea Highlands, East-Central, Gahuku-Benabena.
ast  Asturian  Asturianu  ast  Spain  320  3855744  24788994  AUB  -  ast  aub  es ca oc gl pt fr an mwl  en es  yes  Marcos Costales, Ricardo Mones Lastra, Poli Mencía  Thu Jan 31 07:53:03 CST 2013  ASTUR-LEONESE, ASTURIAN-LEONESE, ASTURIANU  Indo-European, Italic, Romance, Italo-Western, Western, Gallo-Iberian, Ibero-Romance, West Iberian, Asturo-Leonese.
ata  Pele-Ata  -  ata  Papua New Guinea  345  427434  2581972  ATA  -  -  -  nak  en  no  -  Wed Jan 9 10:16:30 CST 2013  WASI, UASE, UASI, UASILAU, PELEATA  East Papuan, Yele-Solomons-New Britain, New Britain, Wasi.
atd  Ata Manobo  -  atd  Philippines  2  3184  18426  ATD  -  -  -  mbd  en  no  -  Fri Dec 7 13:56:18 CST 2012  ATAO MANOBO, ATA OF DAVAO, LANGILAN  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Southern Philippine, Manobo, Central, South, Ata-Tigwa.
atg  Ivbie North-Okpela-Arhe  -  atg  Nigeria  0  0  0  ATG  -  -  -  dag vmw lgg tsc tos gux kj ng kwj  en  no  -  -  -  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Edoid, North-Central, Ghotuo-Uneme-Yekhee.
atv  Northern Altai  Алтай тил  atv  Russian Federation  3  667  4891  ATV  -  -  -  alt ky tyv kaa-Cyrl gag-Cyrl cjs kk tt kum sah mhr uz chm kjh  en ru  no  -  Fri Sep 20 11:50:37 CDT 2013  TELEUT, TELENGUT  Altaic, Turkic, Northern.
aty  Aneityum  -  aty  Vanuatu  1  2278  11207  ATY  -  -  -  tbc ga-Latg lus bjn sco-x-scotland cnh wap ifb pag srb  en  no  -  Wed Dec 5 17:06:49 CST 2012  ANEITEUM, ANEITEUMESE, ANEJOM  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, South Vanuatu, Aneityum.
auc  Waorani  -  auc  Ecuador  2  10559  76457  AUC  -  -  1127  cot nhg aer ia rar  en es  no  -  Wed Jan 30 21:09:32 CST 2013  'AUCA', HUAORANI, WAODANI, HUAO, SABELA, AUISHIRI  Unclassified.
aui  Anuki  -  aui  Papua New Guinea  17  18461  138154  AUI  -  -  -  pwg mox gri  en  no  -  Wed Jan 9 10:18:25 CST 2013  GABOBORA  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Nuclear, North Papuan Mainland-D'Entrecasteaux, Anuki.
auj  Awjilah  -  auj  Libya  1  370  2577  AUJ  -  -  -  tmh  en  no  -  Sun Apr 14 09:24:45 CDT 2013  AUJILA, AUGILA, AOUDJILA  Afro-Asiatic, Berber, Eastern, Awjila-Sokna.
auv  Auvergnat  -  auv  France  1  1819  10962  AUV  -  -  auv1  fr mwl prv lnc gsc ca-valencia gl es  en  no  -  Mon Dec 9 14:14:58 CST 2013  AUVERNHAS, AUVERNE, OCCITAN  Indo-European, Italic, Romance, Italo-Western, Western, Gallo-Iberian, Ibero-Romance, Oc.
auy  Awiyaana  -  auy  Papua New Guinea  285  183160  1622643  AUY  -  -  -  pwg  en  no  -  Wed Jan 9 10:33:32 CST 2013  AUYANA  Trans-New Guinea, Main Section, Central and Western, East New Guinea Highlands, Eastern, Gadsup-Auyana-Awa.
av  Avar  Авар  ava  Russian Federation  3  179049  1395565  AVR  av  av  -  dar lez lbe tab kum  en ru  no  -  Mon Jan 7 22:02:11 CST 2013  AVARO, DAGESTANI  North Caucasian, Northeast, Avaro-Andi-Dido, Avar.
avt  Au  -  avt  Papua New Guinea  290  365119  2008137  AVT  -  -  -  mbi zpi pon  en  no  -  Thu Jan 10 11:19:48 CST 2013  -  Torricelli, Wapei-Palei, Wapei.
avu  Avokaya  -  avu  Dem. Rep. of Congo  1  384068  1822176  AVU  -  -  -  thk tpl maa tcf  en  no  -  Sun Dec 30 22:28:46 CST 2012  ABUKEIA, AVUKAYA  Nilo-Saharan, Central Sudanic, East, Moru-Madi, Central.
awa  Awadhi  अवधी  awa  India  4  212049  970486  AWD  -  -  awa*  mai hi hne mr  en  no  -  Wed Sep 18 19:10:16 CDT 2013  ABADI, ABOHI, AMBODHI, AVADHI, BAISWARI, KOJALI, KOSALI  Indo-European, Indo-Iranian, Indo-Aryan, East Central zone.
awb  Awa  -  awb  Papua New Guinea  285  430216  3150286  AWB  -  -  -  stn sny gym alu  en  no  -  Fri Jan 25 10:06:14 CST 2013  MOBUTA  Trans-New Guinea, Main Section, Central and Western, East New Guinea Highlands, Eastern, Gadsup-Auyana-Awa.
awi  Aekyom  -  awi  Papua New Guinea  1  1785  9051  AWI  -  -  -  mi knv tvl rap ha tzh mbt wsk tkl rw sw  en  no  -  Thu Dec 6 14:47:03 CST 2012  AWIN, AIWIN, AKIUM, WEST AWIN  Trans-New Guinea, Main Section, Central and Western, Central and South New Guinea-Kutubuan, Central and South New Guinea, Awin-Pare.
awx  Awara  -  awx  Papua New Guinea  63  40868  290451  AWX  -  -  -  pam jv msk  en  no  -  Thu Jan 10 11:04:34 CST 2013  -  Trans-New Guinea, Main Section, Central and Western, Huon-Finisterre, Finisterre, Wantoat.
ay  Aymara  Aymar  aym  Bolivia  321  1092807  9239707  -  ap  ay  aym  qug qvs qu slm qvz sw ha  en es  started  Alberto Escudero  Tue Sep 10 19:51:31 CDT 2013  -  Aymaran.
ayp  North Mesopotamian Spoken Arabic  -  ayp  Iraq  0  0  0  AYP  -  -  -  arb arz pes  en  no  -  -  SYRO-MESOPOTAMIAN VERNACULAR ARABIC, MOSLAWI, MESOPOTAMIAN QELTU ARABIC  Afro-Asiatic, Semitic, Central, South, Arabic.
az  Azerbaijani  Azərbaycan dili  aze  Azerbaijan  441  8436002  63552147  -  ajr  az  azb  tr crh kaa uz-Latn gag tk  en  yes  Metin Amiroff, Orkhan Jafarov  Sat Feb 2 12:15:58 CST 2013  AZERBAIJAN, AZERI TURK, AZERBAYDZHANI  Altaic, Turkic, Southern, Azerbaijani.
az-Arab  Azerbaijani  -  aze  Azerbaijan  747  1207803  8867303  -  -  -  -  fa pes glk lki pnb ur bal  en fa  no  -  Thu Jan 24 03:34:28 CST 2013  AZERBAIJAN, AZERI TURK, AZERBAYDZHANI  Altaic, Turkic, Southern, Azerbaijani.
az-Cyrl  Azerbaijani  -  aze  Azerbaijan  303  460004  3586777  -  -  -  azb1  ug tt uz ky ru  en ru  no  -  Sat Feb 2 15:27:01 CST 2013  AZERBAIJAN, AZERI TURK, AZERBAYDZHANI  Altaic, Turkic, Southern, Azerbaijani.
azb-Arab  South Azerbaijani  تورکجه  azb  Iran  58  126684  765657  AZB  -  -  -  lki fa pes glk bal  en fa  started  Seyed Hadi Mirvahedi  Thu Sep 19 08:20:30 CDT 2013  AZERI  Altaic, Turkic, Southern, Azerbaijani.
azc-x-tepehuan  Tepehuan  -  azc  Mexico  3  667065  4122094  -  -  -  -  kac pwg mwc xsm bmk  en es  no  -  Wed Sep 25 14:08:05 CDT 2013  TEPEHUÁN  Uto-Aztecan, Southern Uto-Aztecan, Sonoran, Tepiman.
azg  San Pedro Amuzgos Amuzgo  -  azg  Mexico  3  371667  2393759  AZG  -  -  -  amu ln gri nfr fj ki bgt bik  en  no  -  Sun Dec 23 12:54:07 CST 2012  AMUZGO, OAXACA, AMUZGO DE SAN PEDRO AMUZGOS  Oto-Manguean, Amuzgoan.
azj  North Azerbaijani  Azərbaycan  azj  Azerbaijan  896  1788416  13786617  AZE  -  -  -  tr crh kaa gag uz-Latn  en  yes  Metin Amiroff, Orkhan Jafarov  Tue Sep 10 08:43:42 CDT 2013  AZERBAIJAN, AZERI TURK, AZERBAYDZHANI  Altaic, Turkic, Southern, Azerbaijani.
azj-Cyrl  North Azerbaijani  -  azj  Azerbaijan  40  80456  626945  AZE  aj  -  azb1  ug tt uz  en ru  no  -  Wed Jan 23 23:18:07 CST 2013  AZERBAIJAN, AZERI TURK, AZERBAYDZHANI  Altaic, Turkic, Southern, Azerbaijani.
azz  Highland Puebla Nahuatl  -  azz  Mexico  3  659054  4847361  AZZ  -  -  -  nch  en  no  -  Sun Dec 23 12:57:11 CST 2012  SIERRA DE PUEBLA NÁHUAT, HIGHLAND PUEBLA NÁHUAT, SIERRA AZTEC, ZACAPOAXTLA NÁHUAT, ZACAPOAXTLA MEJICANO  Uto-Aztecan, Southern Uto-Aztecan, Aztecan, General Aztec, Aztec.
ba  Bashkir  Башҡорт  bak  Russian Federation  566  1529588  11279389  BXK  bak*  ba  -  tt kaa-Cyrl kk ky  en ru  no  -  Sat Jan 12 16:12:16 CST 2013  BASQUORT  Altaic, Turkic, Western, Uralian.
bal  Balochi  بلوچی  bal  Pakistan  243  309872  1954746  -  -  -  bgp*  pes prs lki glk mzn  en fa  no  Mostafa Daneshvar  Sat Sep 7 05:02:31 CDT 2013  BALUCHI, BALUCI, BALOCI, MAKRANI  Indo-European, Indo-Iranian, Iranian, Western, Northwestern, Balochi.
bal-Latn  Balochi (Latin)  Balúči  bal  Pakistan  3  618  3571  -  -  -  -  br gom brh-Latn kok-Latn ify ms ha cim pes-Latn gux  en  no  Mostafa Daneshvar  Mon Oct 7 22:00:44 CDT 2013  BALUCHI, BALUCI, BALOCI, MAKRANI  Indo-European, Indo-Iranian, Iranian, Western, Northwestern, Balochi.
ban  Bali  Basa Bali  ban  Indonesia (Java and Bali)  15  269189  1891349  BZC  -  -  bzc  jv su bjn pam tl id zsm krj hil ceb  en id  no  -  Wed Sep 18 19:14:59 CDT 2013  BALINESE  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Sundic, Bali-Sasak.
bao  Waimaha  -  bao  Colombia  2  232026  1392600  BAO  -  -  -  cbc  en es  no  -  Fri Jan 25 10:25:09 CST 2013  WAIMAJA, 'BARÁ', NORTHERN BARASANO, BARASANO  Tucanoan, Eastern Tucanoan, Central, Bara.
bar  Bavarian  Boarisch  bar  Austria  15  882423  5450499  BAR  -  bar  -  gsw vmf pfl de  en de  no  -  Sat Jan 12 16:14:42 CST 2013  BAYERISCH, BAIRISCH, BAVARIAN AUSTRIAN, OST-OBERDEUTSCH  Indo-European, Germanic, West, High German, German, Upper German, Bavarian-Austrian.
bas  Basaa  Basaa  bas  Cameroon  232  446982  2194081  BAA  bs  -  -  sm dua men bwu bnp  en fr  no  Emmanuel Ngué Um  Wed Sep 18 19:15:36 CDT 2013  BASSA, BASA, BISAA, NORTHERN MBENE, MVELE, MBELE, MEE, TUPEN, BIKYEK, BICEK  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Northwest, A, Basaa (A.40).
bav  Vengo  -  bav  Cameroon  1  248142  1126101  BAV  -  -  -  om yam  en  no  -  Mon Dec 31 05:46:08 CST 2012  BABUNGO, VENGOO, VENGI, PENGO, NGO, NGUU, NGWA, NGE  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Wide Grassfields, Narrow Grassfields, Ring, North.
bax  Bamun  -  bax  Cameroon  1  1885  8615  BAX  -  -  -  gba bum  en  no  -  Wed Dec 5 13:04:55 CST 2012  BAMOUN, BAMOUM, BAMUM, SHUMPAMEM  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Wide Grassfields, Narrow Grassfields, Mbam-Nkam, Nun.
bba  Bariba  -  bba  Benin  3  799788  3694306  BBA  -  -  bba  bm dyu hag cko maw  en  no  -  Fri Jan 25 10:25:33 CST 2013  BAATONU, BAATOMBU, BARUBA, BARGU, BURGU, BERBA, BARBA, BOGUNG, BARGAWA, BARGANCHI  Niger-Congo, Atlantic-Congo, Volta-Congo, North, Gur, Bariba.
bbb  Barai  -  bbb  Papua New Guinea  413  554607  3113960  BCA  -  -  -  nvm bs sr-Latn hr mcq hbs sr-Latn-ME kwf  en  no  -  Fri Dec 28 19:01:19 CST 2012  -  Trans-New Guinea, Main Section, Eastern, Central and Southeastern, Koiarian, Baraic.
bbc-Latn  Batak Toba  Hata Batak Toba  bbc  Indonesia (Sumatra)  11  4726  30989  BBC  -  -  -  bts kyk bjn su tl agn pam msk jv sml lcm bik sda hil id lbb  en  no  -  Fri Sep 20 16:14:11 CDT 2013  TOBA BATAK, BATTA  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Sundic, Sumatra, Batak, Southern.
bbj  Ghomálá’  Ghɔmálá’  bbj  Cameroon  17  7000  41396  BBJ  -  -  -  lee hig nap sbd lns pbi  en fr  no  -  Fri Nov 15 20:26:52 CST 2013  BANJUN, BANDJOUN, BANJOUN-BAHAM, BALOUM, BATIE, BAMILEKE-BANDJOUN, MANDJU, MAHUM  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Wide Grassfields, Narrow Grassfields, Mbam-Nkam, Bamileke.
bbr  Girawa  -  bbr  Papua New Guinea  290  321044  1877613  BBR  -  -  -  car ubr teo  en  no  -  Thu Jan 10 11:23:21 CST 2013  BEGASIN, BEGESIN, BAGASIN  Trans-New Guinea, Madang-Adelbert Range, Madang, Mabuso, Kokon.
bch  Bariai  -  bch  Papua New Guinea  382  456778  2582779  BCH  -  -  -  war akl hil krj itv  en  no  -  Thu Jan 10 12:25:03 CST 2013  KABANA  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Ngero-Vitiaz, Ngero, Bariai.
bci  Baoulé  Wawle  bci  Côte d’Ivoire  65  158050  795525  BCI  ao  -  bci  dyu  en  no  -  Sat Feb 2 15:28:30 CST 2013  BAULE, BAWULE  Niger-Congo, Atlantic-Congo, Volta-Congo, Kwa, Nyo, Potou-Tano, Tano, Central, Bia, Northern.
bcj  Bardi  Bardi  bcj  Australia  2  963  9001  BCJ  -  -  -  ibd  en  no  Claire Bowern  Thu Jan 10 20:34:45 CST 2013  BARD, BARDI, BADI  Australian, Nyulnyulan.
bco  Kaluli  -  bco  Papua New Guinea  0  0  0  BCO  -  -  -  emk man knk mnk  en  no  -  -  BOSAVI  Trans-New Guinea, Main Section, Central and Western, Central and South New Guinea-Kutubuan, Central and South New Guinea, Bosavi.
bcr  Babine  Nat'ooten-Witsuwit'en  bcr  Canada  0  0  0  BCR  -  -  -  crx blc caf  en  no  Chris Harvey  -  BABINE CARRIER, NORTHERN CARRIER  Na-Dene, Nuclear Na-Dene, Athapaskan-Eyak, Athapaskan, Canadian, Carrier-Chilcotin, Babine-Carrier.
bcw  Bana  -  bcw  Cameroon  8  405528  2152890  BCW  -  -  -  hig mhw  en  no  -  Fri Jan 25 10:34:51 CST 2013  BAZA, KOMA, KA-BANA, PAROLE DES BANA, MIZERAN  Afro-Asiatic, Chadic, Biu-Mandara, A, A.3.
bda  Bayot  -  bda  Senegal  0  0  0  BDA  -  -  -  tlf fai nyf gog kki xh  en  no  -  -  BAIOTE, BAIOT, BAYOTTE  Niger-Congo, Atlantic-Congo, Atlantic, Northern, Bak, Jola, Bayot.
bdd  Bunama  -  bdd  Papua New Guinea  272  222167  1645730  BDD  -  -  -  mpx mox pwg  en  no  -  Fri Dec 28 20:22:04 CST 2012  -  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Nuclear, North Papuan Mainland-D'Entrecasteaux, Dobu-Duau.
bdq  Bahnar  -  bdq  Viet Nam  1  1796  8593  BDQ  -  -  -  vi fil pam tl jv agn jvn cjm ctd bi hlt tcz dln  en vi  no  -  Mon Dec 9 21:36:58 CST 2013  BANA  Austro-Asiatic, Mon-Khmer, Eastern Mon-Khmer, Bahnaric, Central Bahnaric.
be  Belarusan  Беларуская  bel  Belarus  656  6130194  45666057  RUW  -  be  ruw  be-tarask rue uk bg ru mk  en  yes  -  Sat Sep 14 08:58:27 CDT 2013  BELARUSIAN, BELORUSSIAN, BIELORUSSIAN, WHITE RUSSIAN, WHITE RUTHENIAN, BYELORUSSIAN  Indo-European, Slavic, East.
be-Latn  Belarusan (Latin)  -  bel  Belarus  0  0  0  RUW  -  -  -  ru-Latn bg-Latn mk-Latn  en  no  -  -  BELARUSIAN, BELORUSSIAN, BIELORUSSIAN, WHITE RUSSIAN, WHITE RUTHENIAN, BYELORUSSIAN  Indo-European, Slavic, East.
be-tarask  Belarusan (Taraškievica)  Беларуская (тарашкевіца)  bel  Belarus  16  96565  748201  RUW  -  be-x-old  -  be ru uk  en  no  -  Sat Sep 14 08:57:19 CDT 2013  BELARUSIAN, BELORUSSIAN, BIELORUSSIAN, WHITE RUSSIAN, WHITE RUTHENIAN, BYELORUSSIAN  Indo-European, Slavic, East.
bef  Benabena  -  bef  Papua New Guinea  288  290792  1936064  BEF  -  -  -  mpx  en  no  -  Thu Jan 10 12:28:57 CST 2013  BENA  Trans-New Guinea, Main Section, Central and Western, East New Guinea Highlands, East-Central, Gahuku-Benabena.
bem  Bemba  Cibemba  bem  Zambia  106  250323  1803678  BEM  cw  -  bem  toi kqn lu tum loz xog nyy ng sw  en  no  -  Sat Feb 2 09:10:51 CST 2013  CHIBEMBA, ICHIBEMBA, WEMBA, CHIWEMBA  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, M, Bemba (M.40).
bew  Betawi  Bahasa Betawi  bew  Indonesia (Java and Bali)  2  689  5273  BEW  -  -  -  id zsm bjn jv-x-bms su iba jv mad  en  no  -  Fri Sep 20 16:28:06 CDT 2013  JAKARTA MALAY, BETAWI MALAY, BATAVI, BATAWI, MELAYU JAKARTE  Creole, Malay based.
bex  Jur Modo  -  bex  Sudan  2  256784  1224860  BEX  -  -  -  knv  en  no  -  Fri Jan 25 10:34:54 CST 2013  -  Nilo-Saharan, Central Sudanic, West, Bongo-Bagirmi, Bongo-Baka, Morokodo-Beli.
bfa  Bari  Bari  bfa  Sudan  3  18077  100674  BFA  bh  -  bfa  sg gri ln dgc fj  en  no  -  Sat Jan 12 17:09:12 CST 2013  BERI  Nilo-Saharan, Eastern Sudanic, Nilotic, Eastern, Bari.
bfd  Bafut  -  bfd  Cameroon  1  276479  1243526  BFD  -  -  -  gnd biv sbd dgi kno mnf srr bav  en  no  -  Mon Dec 31 06:52:30 CST 2012  BUFE, FU, FUT, BEFE  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Wide Grassfields, Narrow Grassfields, Mbam-Nkam, Ngemba.
bfq  Badaga  -  bfq  India  3  186  1162  BFQ  -  -  -  kn pi-Knda  en  no  -  Tue Oct 8 22:14:28 CDT 2013  BADAG, BADAGU, BADUGU, BADUGA, VADAGU  Dravidian, Southern, Tamil-Kannada, Kannada.
bfq-Latn  Badaga  -  bfq  India  3  428  3350  BFQ  -  -  -  chw viv gof mwp bmk dob  en  no  -  Sun Sep 22 19:36:43 CDT 2013  BADAG, BADAGU, BADUGU, BADUGA, VADAGU  Dravidian, Southern, Tamil-Kannada, Kannada.
bfq-Taml  Badaga  படக பாஷை  bfq  India  11  1235  8374  BFQ  -  -  -  ta pi-Taml  en  no  -  Thu Sep 26 23:01:55 CDT 2013  BADAG, BADAGU, BADUGU, BADUGA, VADAGU  Dravidian, Southern, Tamil-Kannada, Kannada.
bft-Latn  Balti  -  bft  Pakistan  4  428  2705  BFT  -  -  -  bo-Latn agu vun  en  no  -  Sun Sep 22 19:54:04 CDT 2013  SBALTI, BALTISTANI, BHOTIA OF BALTISTAN  Sino-Tibetan, Tibeto-Burman, Himalayish, Tibeto-Kanauri, Tibetic, Tibetan, Western.
bg  Bulgarian  Български  bul  Bulgaria  18105  53031602  344639744  BLG  bl  bg  blg  mk ru sr  en  yes  -  Sat Feb 2 17:43:55 CST 2013  BALGARSKI  Indo-European, Slavic, South, Eastern.
bg-Latn  Bulgarian (Latin)  -  bul  Bulgaria  43  228208  1453045  BLG  -  -  -  mk-Latn ru-Latn bs sr-Latn sl hr  en  no  -  Sat Jan 12 18:37:11 CST 2013  BALGARSKI  Indo-European, Slavic, South, Eastern.
bgp-Latn  Eastern Balochi  -  bgp  Pakistan  1  1835  10369  BGP  -  -  -  sw  en  no  -  Fri Dec 7 16:00:10 CST 2012  BALUCHI, BALUCI, BALOCI  Indo-European, Indo-Iranian, Iranian, Western, Northwestern, Balochi.
bgr  Bawm Chin  -  bgr  India  1  212719  1034493  BGR  -  -  -  lus cnh tcz vap su jv-x-bms  en  no  -  Mon Dec 31 08:11:43 CST 2012  BAWM, BAWNG, BAWN, BOM  Sino-Tibetan, Tibeto-Burman, Kuki-Chin-Naga, Kuki-Chin, Central.
bgt  Bughotu  -  bgt  Solomon Islands  0  0  0  BGT  -  -  -  gri fj pwg stn amu  en  no  -  -  BUGOTO, BUGOTA, BUGOTU, MBUGHOTU, MAHAGA  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Southeast Solomonic, Gela-Guadalcanal, Bughotu.
bh  Bihari  भोजपुरी  bih  India  110  306749  1741512  BHJ  -  bh  bhj*  hi hne raj ne mr awa  en  no  -  Tue Sep 10 08:49:20 CDT 2013  BHOJAPURI, BHOZPURI, BAJPURI, BIHARI  Indo-European, Indo-Iranian, Indo-Aryan, Eastern zone, Bihari.
bh-Latn  Bihari (Latin)  -  bih  Suriname  1  234067  1365828  -  -  -  -  hif hi-Latn ur-Latn pes-Latn  en  no  -  Tue Jan 22 17:10:05 CST 2013  -  Indo-European, Indo-Iranian, Indo-Aryan, Eastern zone, Bihari.
bhl  Bimin  -  bhl  Papua New Guinea  345  531162  3137026  BHL  -  -  -  fai mbs  en  no  -  Fri Dec 28 20:26:36 CST 2012  -  Trans-New Guinea, Main Section, Central and Western, Central and South New Guinea-Kutubuan, Central and South New Guinea, Ok, Mountain.
bho  Bhojpuri  भोजपुरी  bho  India  4  67155  377745  BHJ  -  bh  bhj  mag hi hne  en  no  -  Wed Jan 30 15:38:09 CST 2013  Bajpuri, Bhojapuri, Bhozpuri, Bihari, Deswali, Khotla, Piscimas  Indo-European, Indo-Iranian, Indo-Aryan, Eastern zone, Bihari.
bi  Bislama  Bislama  bis  Vanuatu  1062  1211410  6685245  BCY  lm  bi  bcy  tpi pis  en  yes  Sébastien Lanteigne, Eric Brandell, Murray Garde, Daryl Moon  Sat Feb 2 15:53:35 CST 2013  BICHELAMAR  Creole, English based, Pacific.
bib  Bisa  -  bib  Burkina Faso  1  242710  997126  BIB  -  -  -  biv ktj  en  no  -  Mon Dec 31 12:04:16 CST 2012  BISSA  Niger-Congo, Mande, Eastern, Eastern, Bissa.
big  Biangai  -  big  Papua New Guinea  261  290564  2048654  BIG  -  -  -  jv pam  en  no  -  Thu Jan 10 12:31:18 CST 2013  -  Trans-New Guinea, Main Section, Eastern, Central and Southeastern, Goilalan, Kunimaipa.
bik  Bicolano  Bicol  bik  Philippines  444  1412862  8614319  -  bi  bcl  bkl  hil hnn kyk tl ceb krj bjn iry pag slm msk jv sml su  en  no  -  Fri Sep 13 11:14:09 CDT 2013  BIKOL  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Meso Philippine, Central Philippine, Bikol, Coastal, Naga.
bim  Bimoba  -  bim  Ghana  5  834503  3909447  BIM  -  -  -  bud gux myk  en  no  -  Fri Jan 25 10:49:27 CST 2013  MOAR, MOOR  Niger-Congo, Atlantic-Congo, Volta-Congo, North, Gur, Central, Northern, Oti-Volta, Gurma, Moba.
bin  Edo  Ẹ̀dó  bin  Nigeria  3  22817  115737  EDO  ed  -  edo  iso ain  en  no  -  Sat Jan 12 17:59:13 CST 2013  BINI, BENIN, ADDO, OVIEDO, OVIOBA  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Edoid, North-Central, Edo-Esan-Ora.
biv  Southern Birifor  -  biv  Ghana  1  220686  905262  BIV  -  -  -  dga sbd srr  en  no  -  Mon Dec 31 11:52:51 CST 2012  BIRIFO, GHANA BIRIFOR  Niger-Congo, Atlantic-Congo, Volta-Congo, North, Gur, Central, Northern, Oti-Volta, Western, Northwest, Dagaari-Birifor, Birifor.
bjn  Banjar  -  bjn  Indonesia (Kalimantan)  40  251923  1775824  BJN  -  bjn  -  id zsm jv-x-bms su min jv ifk pam  en  no  -  Sat Sep 7 05:03:38 CDT 2013  BANJARESE, BANDJARESE, BANJAR MALAY  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Sundic, Malayic, Malayan, Local Malay.
bjr  Binumarien  -  bjr  Papua New Guinea  288  272025  2175667  BJR  -  -  -  stn aia  en  no  -  Thu Jan 10 12:46:01 CST 2013  BINUMARIA, BINAMARIR  Trans-New Guinea, Main Section, Central and Western, East New Guinea Highlands, Eastern, Tairora.
bjv  Bedjond  -  bjv  Chad  1  253156  1072593  MAP  -  -  -  tuo-BR rao mdv bav  en  no  -  Mon Dec 31 15:33:48 CST 2012  MBAY BEDIONDO, MBAY BEJONDO, BEDIONDO MBAI, BÉDJONDE, BEDJONDO, BEDIONDO, NANGNDA  Nilo-Saharan, Central Sudanic, West, Bongo-Bagirmi, Sara-Bagirmi, Sara, Sara Proper.
bkd  Binukid  -  bkd  Philippines  1  509  2758  BKD  -  -  -  bjn ifk hnn  en  no  -  Wed Jan 16 21:42:37 CST 2013  BINUKID MANOBO, BINOKID, BUKIDNON  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Southern Philippine, Manobo, North.
bkq  Bakairí  -  bkq  Brazil  1  255138  1806563  BKQ  -  -  -  udu nou tgp luo  en  no  -  Sun Dec 23 13:02:27 CST 2012  BACAIRÍ, KURÂ  Carib, Southern, Xingu Basin.
bku  Buhid  -  bku  Philippines  3  204967  1264522  BKU  -  -  -  war krj bjn hil tl id  en  no  -  Mon Dec 31 15:51:43 CST 2012  BUKIL, BANGON, BATANGAN  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Meso Philippine, South Mangyan, Buhid-Taubuid.
bla  Blackfoot  Siksika  bla  Canada  1  534  7959  BLC  -  -  -  cr-Latn cjo  en  no  -  Wed Jul 4 18:03:42 CDT 2012  PIKANII, BLACKFEET  Algic, Algonquian, Plains.
blc  Bella Coola  Nuxálk  blc  Canada  2  2835  16707  BEL  -  -  -  lil-x-mou lil-x-fou bcr hur-x-cow sek  en  no  -  Thu Jan 17 10:37:05 CST 2013  NUXALK  Salishan, Bella Coola.
ble  Balanta-Kentohe  -  ble  Guinea-Bissau  0  0  0  BLE  -  -  -  bum ntr dip din snk hif srr dww  en  no  -  -  BALANTA, BALANT, BALANTE, BALANDA, BALLANTE, BELANTE, BULANDA, BRASSA, ALANTE, FRASE  Niger-Congo, Atlantic-Congo, Atlantic, Northern, Bak, Balant-Ganja.
blh  Kuwaa  -  blh  Liberia  1  258968  1212066  BLH  -  -  -  hna grb gbo lee sbd ak neb  en  no  -  Mon Dec 31 16:24:17 CST 2012  KWAA, KOWAAO, BELLEH, BELLE  Niger-Congo, Atlantic-Congo, Volta-Congo, Kru, Kuwaa.
blu  Hmong Njua  -  blu  China  0  0  0  BLU  -  -  blu  hea hms zao bo-Latn  en  no  -  -  CHUANQIANDIAN MIAO, CHUANCHIENTIEN MIAO, SICHUAN-GUIZHOU-YUNNAN HMONG, TAK MIAO, MEO, MIAO, WESTERN MIAO, WESTERN HMONG  Hmong-Mien, Hmongic, Chuanqiandian.
blw  Balangao  -  blw  Philippines  38  50282  323127  BLW  -  -  -  pag nl  en  no  -  Sat Dec 8 09:46:04 CST 2012  BALANGAO BONTOC, BALANGAW, FARANGAO  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Northern Philippine, Northern Luzon, South-Central Cordilleran, Central Cordilleran, Nuclear Cordilleran, Balangao.
blz  Balantak  -  blz  Indonesia (Sulawesi)  1  194427  1271847  BLZ  -  -  -  lcm fj  en  no  -  Mon Dec 31 17:37:44 CST 2012  KOSIAN  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Sulawesi, Central Sulawesi, Eastern.
bm  Bambara  Bamanankan  bam  Mali  25  484007  2283461  BRA  ar  bm  bra  dyu emk knk kus dag  en fr  yes  Boukary Konaté  Fri Jan 25 10:49:00 CST 2013  BAMANANKAN, BAMANAKAN  Niger-Congo, Mande, Western, Central-Southwestern, Central, Manding-Jogo, Manding-Vai, Manding-Mokole, Manding, Manding-East, Northeastern Manding, Bamana.
bmh  Kein  -  bmh  Papua New Guinea  288  305604  1757898  BMH  -  -  -  agr aia  en  no  -  Thu Jan 10 12:35:08 CST 2013  BEMAL  Trans-New Guinea, Madang-Adelbert Range, Madang, Mabuso, Kokon.
bmk  Ghayavi  -  bmk  Papua New Guinea  17  20719  135575  BMK  -  -  -  pwg aui gri bdd fj  en  no  -  Thu Jan 10 12:35:33 CST 2013  GALAVI, BOIANAKI, BOANAKI, BOINAKI, BOANAI  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Nuclear, North Papuan Mainland-D'Entrecasteaux, Are-Taupota, Are.
bmr  Muinane  -  bmr  Colombia  2  149597  1325228  BMR  -  -  -  mnb ja-Latn trp car zpa amm aom  en es  no  -  Sun Dec 23 13:08:54 CST 2012  MUINANA, MUINANI, MUENAME  Witotoan, Boran.
bmu  Somba-Siawari  -  bmu  Papua New Guinea  349  352021  2423073  BMU  -  -  -  ssd kto kmh mna miq fai  en  no  -  Thu Jan 10 13:10:29 CST 2013  BULUM, BURUM, MINDIK, BURUM-MINDIK  Trans-New Guinea, Main Section, Central and Western, Huon-Finisterre, Huon, Western.
bn  Bengali  বাংলা  ben  Bangladesh  191  2885526  19543941  BNG  be*  bn  bng  as bpy  en  yes  Naushad Jamil, Khan Md. Anwarus Salam  Fri Sep 13 14:09:48 CDT 2013  BANGA-BHASA, BANGALA, BANGLA  Indo-European, Indo-Iranian, Indo-Aryan, Eastern zone, Bengali-Assamese.
bn-Latn  Bengali (Latin)  -  ben  Bangladesh  899  3892039  23222552  BNG  -  -  -  pes-Latn kok-Latn ur-Latn  en  no  -  Thu Jan 17 20:42:08 CST 2013  BANGA-BHASA, BANGALA, BANGLA  Indo-European, Indo-Iranian, Indo-Aryan, Eastern zone, Bengali-Assamese.
bnc  Bontok  -  bnc  Philippines  1  2127  12267  BNC  -  -  -  kne ifb ifk pag sbl itv ifu mqb bik  en  no  -  Thu Jan 24 09:57:03 CST 2013  BONTOK, IGOROT  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Northern Philippine, Northern Luzon, South-Central Cordilleran, Central Cordilleran, Nuclear Cordilleran, Bontok-Kankanay, Bontok.
bng  Benga  -  bng  Equatorial Guinea  1  2139  9749  BEN  -  -  -  ln ki  en  no  -  Sun Dec 9 06:33:16 CST 2012  -  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Northwest, A, Bube-Benga (A.30).
bno  Bantoanon  -  bno  Philippines  3  3384  19997  BNO  -  -  -  akl hil krj ceb hnn bik kyk tl  en  no  -  Sat Jan 12 20:16:35 CST 2013  BANTON, BANTUANON, ASIQ, SIMARANHON, CALATRAVANHON  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Meso Philippine, Central Philippine, Bisayan, Banton.
bnp  Bola  -  bnp  Papua New Guinea  515  616634  3049803  BNP  -  -  -  fj gri aia stn  en  no  -  Thu Jan 10 13:07:47 CST 2013  BAKOVI, BOLA-BAKOVI  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, Willaumez.
bnt-x-chaga  Chaga languages  -  bnt  Tanzania  4  430351  2904522  -  -  -  -  swh kki wmw pkb ki swb  en  no  -  Tue Oct 8 19:23:59 CDT 2013  -  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, E, Chaga (E.30).
bo  Tibetan  བོད་སྐད  bod  China  1943  939955  23150243  TIC  -  bo  tic  dz  en  no  Tshering Cigay Dorji  Mon Dec 2 14:10:46 CST 2013  WEI, WEIZANG, CENTRAL TIBETAN, BHOTIA, ZANG, PHOKE, DBUS, DBUSGTSANG, U  Sino-Tibetan, Tibeto-Burman, Himalayish, Tibeto-Kanauri, Tibetic, Tibetan, Central.
bo-Latn  Tibetan (Latin)  -  bod  China  32  480174  2247161  TIC  -  -  -  pam tl kyk jv agn  en  no  -  Sat Jan 12 21:01:01 CST 2013  WEI, WEIZANG, CENTRAL TIBETAN, BHOTIA, ZANG, PHOKE, DBUS, DBUSGTSANG, U  Sino-Tibetan, Tibeto-Burman, Himalayish, Tibeto-Kanauri, Tibetic, Tibetan, Central.
boa  Bora  -  boa  Peru  3  185349  1490504  BOA  -  -  boa  bon wiu moh bin yss-x-yawu  en  no  -  Sun Dec 23 13:09:36 CST 2012  -  Witotoan, Boran.
boj  Anjam  -  boj  Papua New Guinea  284  588783  3469869  BOJ  -  -  -  fj gri pap chr-Latn ln ig amu dgc pap-CW kqw  en  no  -  Mon Dec 9 14:26:19 CST 2013  BOGATI, BOM, BOGAJIM, BOGADJIM, LALOK  Trans-New Guinea, Madang-Adelbert Range, Madang, Rai Coast, Mindjim.
bon  Bine  -  bon  Papua New Guinea  288  289542  1852340  ORM  -  -  -  ram mbt aso  en  no  -  Thu Jan 10 13:15:35 CST 2013  ORIOMO, PINE  Trans-New Guinea, Trans-Fly-Bulaka River, Trans-Fly, Eastern Trans-Fly.
box  Buamu  -  box  Burkina Faso  0  0  0  BOX  -  -  -  ajg sm nfr yal agu myk neb st spp fud  en  no  -  -  EASTERN BOBO WULE, EASTERN BOBO OULE, RED BOBO, BWA, BWABA, BOUAMOU  Niger-Congo, Atlantic-Congo, Volta-Congo, North, Gur, Central, Northern, Bwamu.
bpr  Koronadal Blaan  -  bpr  Philippines  1  203293  988758  BIK  -  -  -  bps pap dyo bjn  en  no  -  Tue Jan 1 07:46:08 CST 2013  KORONADAL BILAAN, BILANES, BIRAAN, BARAAN, TAGALAGAD  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, South Mindanao, Bilic, Blaan.
bps  Sarangani Blaan  -  bps  Philippines  1  214400  1073787  BIS  -  -  -  bpr dyo bjn pap su  en  no  -  Tue Jan 1 08:13:56 CST 2013  BILAAN, BALUD, TUMANAO  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, South Mindanao, Bilic, Blaan.
bpy  Bishnupriya  -  bpy  India  0  0  0  BPY  mi*  bpy  bpy*  bn  en  no  -  -  BISHNUPURIYA, BISNA PURIYA, BISHNUPRIA MANIPURI  Indo-European, Indo-Iranian, Indo-Aryan, Eastern zone, Bengali-Assamese.
bqc  Boko  -  bqc  Benin  2  567541  2678968  BQC  -  -  -  sbd  en  no  -  Tue Jan 1 12:17:29 CST 2013  BOKONYA, BOKKO, BOO, BUSA-BOKO  Niger-Congo, Mande, Eastern, Eastern, Busa.
bqi  Bakhtiâri  بختیاری  bqi  Iran  0  0  0  -  -  -  -  pes prs bal lki mzn glk ckb  en  no  -  -  Lori, Lori-ye Khaveri  Indo-European, Indo-Iranian, Iranian, Western, Southwestern, Luri
br  Breton  Brezhoneg  bre  France  9766  12986692  77841749  BRT  -  br  brt  frr-x-fer  en fr  yes  Alan Drev, Thierry Vignaud, Ahmed Razoui, Fulup Jakez  Tue Sep 10 19:57:24 CDT 2013  BREZHONEG  Indo-European, Celtic, Insular, Brythonic.
br-x-falhuneg  Breton (Falhuneg)  Brezoneg  bre  France  9  13797  75183  BRT  -  -  -  sv br-x-unified  en  no  Mael Thépaut  Thu Mar 14 13:01:52 CDT 2013  BREZHONEG  Indo-European, Celtic, Insular, Brythonic.
br-x-unified  Breton (Unified)  Brezhoneg  bre  France  0  0  0  BRT  -  -  brt  frr-x-fer br-x-falhuneg  en fr  yes  Alan Drev, Thierry Vignaud, Ahmed Razoui, Fulup Jakez  -  BREZHONEG  Indo-European, Celtic, Insular, Brythonic.
brh-Latn  Brahui  Bráhuí  brh  Pakistan  164  65202  353293  BRH  -  -  -  rmy rom kkj kea mur  en  no  -  Fri Sep 20 17:04:49 CDT 2013  BRAHUIDI, BIRAHUI, BRAHUIGI, KUR GALLI  Dravidian, Northern.
bru  Eastern Bru  -  bru  Laos  4  262838  1253263  BRU  -  -  -  tl vi pam  en  no  -  Mon Jan 7 21:47:47 CST 2013  BROU, VANKIEU  Austro-Asiatic, Mon-Khmer, Eastern Mon-Khmer, Katuic, West Katuic, Brou-So.
brx  Bodo  बड़ो  brx  India  53  109586  788116  BRX  -  -  -  mai ne bh hi mr  en  no  -  Wed Sep 18 19:19:29 CDT 2013  BORO, BODI, BARA, BORONI, MECHI, MECHE, MECH, MECI, KACHARI  Sino-Tibetan, Tibeto-Burman, Jingpho-Konyak-Bodo, Konyak-Bodo-Garo, Bodo-Garo, Bodo.
bs  Bosnian  Bosanski  bos  Bosnia and Herzegovina  7242  13664357  94328831  BWF  -  bs  src1  hr sr-Latn  en  yes  Jasmin Custic, Eldar Murselovic, Mirsad Čirkić  Fri Sep 13 14:31:02 CDT 2013  -  Indo-European, Slavic, South, Western.
bs-Cyrl  Bosnian (Cyrillic)  босански  bos  Bosnia and Herzegovina  3  4734  30130  BWF  -  -  src4  sr  en  no  -  Tue Sep 10 09:58:11 CDT 2013  -  Indo-European, Slavic, South, Western.
bsb  Brunei Bisaya  -  bsb  Brunei  0  0  0  BSB  -  -  -  id ms su jv  en  no  Suhaila Saee  -  BISAYAH, BISAYA BUKIT, VISAYAK, BEKIAU, LORANG BUKIT  Austronesian, Malayo-Polynesian, North Borneo, Sabahan, Dusunic, Bisaya, Southern.
bsk-Latn  Burushaski (Latin)  Buruɕaski  bsk  Pakistan  2  1144  6327  BSK  -  -  -  kus mbt ha lia ppl kha pes-Latn fa-Latn miq  en  no  -  Mon Dec 9 14:25:31 CST 2013  BRUSHASKI, BURUSHAKI, BURUCAKI, BURUSHKI, BURUCASKI, BILTUM, KHAJUNA, KUNJUT  Language Isolate.
bsn  Barasana-Eduria  -  bsn  Colombia  7  570398  3788974  BSN  -  -  -  tav bao gvc  en es  no  -  Wed Dec 5 13:56:00 CST 2012  SOUTHERN BARASANO, PANEROA, EDURIA, EDULIA  Tucanoan, Eastern Tucanoan, Central, Southern.
bss  Akoose  -  bss  Cameroon  2  190671  1120912  BSS  -  -  -  anv  en  no  -  Wed Sep 18 19:23:56 CDT 2013  BAKOSSI, BEKOOSE, AKOSI, KOOSE, KOSI, NKOSI, NKOOSI  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Northwest, A, Lundu-Balong (A.10), Ngoe.
btb  Beti  -  btb  Cameroon  2  5880  28931  BTB  -  -  btb  itv blz ak  en fr  no  -  Thu Dec 6 19:27:35 CST 2012  -  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Northwest, A, Yaunde-Fang (A.70).
btd  Batak Dairi  Batak Pakpak  btd  Indonesia (Sumatra)  3  193646  1199657  BTD  -  -  -  btx su lcm jv-x-bms iba blz  en  no  -  Wed Sep 18 19:23:40 CDT 2013  DAIRI, PAKPAK, PAKPAK DAIRI  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Sundic, Sumatra, Batak, Northern.
btm  Batak Mandailing  Hata Mandailing  btm  Indonesia (Sumatra)  12  4126  29017  BTM  -  -  -  bbc-Latn bjn su bts jv-x-bms jv id zsm pam bik kyk slm tl  en  no  -  Fri Nov 15 20:40:03 CST 2013  MANDAILING BATAK, BATTA  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Sundic, Sumatra, Batak, Southern.
bts  Batak Simalungun  Sahap Simalungun  bts  Indonesia (Sumatra)  88  580324  3523871  BTS  -  -  -  aia sml  en  no  -  Tue Jan 1 20:58:36 CST 2013  TIMUR, SIMELUNGAN  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Sundic, Sumatra, Batak, Simalungan.
btx  Batak Karo  Cakap Karo  btx  Indonesia (Sumatra)  3  183782  1110844  BTX  -  -  -  su jv-x-bms iba lcm bjn sml ms  en  no  -  Wed Sep 18 19:26:46 CDT 2013  KARO BATAK  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Sundic, Sumatra, Batak, Northern.
btz  Batak Alas-Kluet  Batak Alas  btz  Indonesia (Sumatra)  4  1371  10144  BTZ  -  -  -  id zsm btx bjn su jv-x-bms btd bew iba  en  no  -  Sun Sep 22 20:36:59 CDT 2013  ALAS-KLUET BATAK  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Sundic, Sumatra, Batak, Northern.
bua  Buriat  Буряадай  bua  Russian Federation  1877  1354440  11227869  -  by  -  -  khk mn sah tyv ulc neg ky tg  en  no  Jargal Badagarov  Mon Sep 30 19:08:08 CDT 2013  BURYAT, BURIAT-MONGOLIAN, NORTHERN MONGOLIAN  Altaic, Mongolian, Eastern, Oirat-Khalkha, Khalkha-Buriat, Buriat.
buc  Bushi  -  buc  Madagascar  1  6489  48383  BUC  skl  -  buc*  xmv mg plt skg stn  en  no  -  Thu Jan 17 10:39:04 CST 2013  SHIBUSHI, KIBUSHI, KIBUKI, SHIBUSHI SHIMAWORE, SAKALAVA, ANTALAOTRA  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Borneo, Barito, East, Malagasy.
bud  Ntcham  -  bud  Togo  1  192015  1016873  BUD  -  -  -  bim om yo hus  en  no  -  Tue Jan 1 20:06:04 CST 2013  BASSAR, BASARE, BASSARI, BASARI, BASAR, NCHAM, NATCHAMBA, TOBOTE  Niger-Congo, Atlantic-Congo, Volta-Congo, North, Gur, Central, Northern, Oti-Volta, Gurma, Ntcham.
bug  Bugis  Basa Ugi  bug  Indonesia (Sulawesi)  5  170414  1332315  BPR  -  bug  bpr  pam mvp tl lcm jv su  en  no  -  Fri Jan 25 10:49:05 CST 2013  BUGINESE, BUGI, BOEGINEESCHE, BOEGINEZEN, UGI, DE', RAPPANG BUGINESE  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Sulawesi, South Sulawesi, Bugis.
buk  Bugawac  -  buk  Papua New Guinea  288  318219  1608288  BUK  -  -  -  nop  en  no  -  Thu Jan 10 15:09:54 CST 2013  BUKAWA, BUKAUA, BUKAWAC, KAWA, KAWAC, YOM GAWAC  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Huon Gulf, North.
bum  Bulu  Bulu  bum  Cameroon  17  48546  229302  BUM  bo  -  -  maf gba bnp dgi kno  en fr  no  -  Sat Jan 12 21:43:44 CST 2013  BOULOU  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Northwest, A, Yaunde-Fang (A.70).
bvr  Burarra  -  bvr  Australia  284  323362  2914320  BVR  -  -  -  tiw wmt ibd wbp  en  no  -  Sat Jan 12 21:54:18 CST 2013  Anbarra, Barera, Bawera, Burada, Bureda, Burera, Gidjingaliya Gujingalia, Gujalabiya, Gun-Guragone, Jikai, Tchikai  Australian, Gunwingguan, Burarran.
bvz  Bauzi  -  bvz  Indonesia (Irian Jaya)  1  510891  2715878  PAU  -  -  -  pes-Latn gur  en  no  -  Wed Jan 2 09:01:57 CST 2013  BAUDI, BAURI, BAUDJI, BAUDZI  Geelvink Bay, East Geelvink Bay.
bwq  Southern Bobo Madaré  -  bwq  Burkina Faso  1  214111  947252  BWQ  -  -  -  bm dyu xrb alu yal  en  no  -  Tue Sep 10 10:01:29 CDT 2013  BOBO FING, BOBO FI, BLACK BOBO, BOBO  Niger-Congo, Mande, Western, Northwestern, Samogo, Soninke-Bobo, Bobo.
bwu  Buli  -  bwu  Ghana  1  284536  1251299  BWU  -  -  -  dyu bm emk loz biv  en  no  -  Wed Jan 2 07:52:44 CST 2013  BUILSA, BULISA, KANJAGA, GURESHA  Niger-Congo, Atlantic-Congo, Volta-Congo, North, Gur, Central, Northern, Oti-Volta, Buli-Koma.
bxr  Russia Buriat  Буряад  bxr  Russian Federation  2  177855  1323089  MNB  -  bxr  -  khk mn ulc sah neg tyv ky  en  no  Jargal Badagarov  Mon Sep 16 16:42:02 CDT 2013  BURYAT, BURIAT-MONGOLIAN, NORTHERN MONGOLIAN  Altaic, Mongolian, Eastern, Oirat-Khalkha, Khalkha-Buriat, Buriat.
byr  Baruya  -  byr  Papua New Guinea  338  255027  2207815  BYR  -  -  -  byr-x-waga ktu ln fj  en  no  -  Thu Jan 10 15:11:27 CST 2013  BARUA, YIPMA  Trans-New Guinea, Main Section, Central and Western, Angan, Angan Proper.
byr-x-waga  Yipma/Wagamwa  -  byr  Papua New Guinea  16  3774  36084  BYR  -  -  -  byr stn  en  no  -  Thu Jan 10 15:13:01 CST 2013  BARUA, YIPMA  Trans-New Guinea, Main Section, Central and Western, Angan, Angan Proper.
byv  Medumba  Medumba  byv  Cameroon  1  8618  42443  BYV  du  -  -  bum mbi  en  no  Eddy Kwessi  Thu Jan 17 10:41:06 CST 2013  BAGANGTE, BANGANGTE, BAMILEKE-MEDUMBA  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Wide Grassfields, Narrow Grassfields, Mbam-Nkam, Bamileke.
byx  Qaqet  -  byx  Papua New Guinea  287  433590  2141773  BYX  -  -  -  loa aoj-x-filifita bts gbi  en  no  -  Thu Jan 10 15:28:44 CST 2013  MAQAQET, KAKAT, MAKAKAT, BAINING  East Papuan, Yele-Solomons-New Britain, New Britain, Baining-Taulil.
bzd  Bribri  -  bzd  Costa Rica  3  367456  1816046  BZD  -  -  -  otn mxb mks cjp pob zpu cnl mig  en es  no  -  Sun Dec 23 13:11:29 CST 2012  TALAMANCA  Chibchan, Talamanca.
bzh  Mapos Buang  -  bzh  Papua New Guinea  291  553111  2945420  BZH  -  -  -  mlp pes-Latn  en  no  -  Thu Jan 10 16:12:37 CST 2013  MAPOS, CENTRAL BUANG  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Huon Gulf, South, Hote-Buang, Buang.
bzj  Belize Kriol English  -  bzj  Belize  4  304724  1459599  BZJ  -  -  -  icr jam  en  no  -  Sun Dec 23 13:27:03 CST 2012  Creola, Kriol, Northern Central America Creole English  Creole, English based, Atlantic, Western
ca  Catalan  Català  cat  Spain  10005  29332671  179410556  CLN  an  ca  cln  oc ast es lad an fr gl pt  en  yes  Toni Hermoso Pulido  Sat Sep 14 17:24:05 CDT 2013  CATALÀ, CATALÁN, BACAVÈS, CATALONIAN  Indo-European, Italic, Romance, Italo-Western, Western, Gallo-Iberian, Ibero-Romance, East Iberian.
ca-valencia  Valencian  Valencià  cat  Spain  42  155297  1074432  CLN  -  -  -  ca es ast oc an fr  en ca es  yes  -  Fri Sep 13 22:06:56 CDT 2013  CATALÀ, CATALÁN, BACAVÈS, CATALONIAN  Indo-European, Italic, Romance, Italo-Western, Western, Gallo-Iberian, Ibero-Romance, East Iberian.
caa  Ch’orti’  -  caa  Guatemala  2  339394  1908977  CAA  -  -  -  nap nsn pt-CV pt-BR gl pap  en es  no  -  Sun Dec 23 15:42:14 CST 2012  -  Mayan, Cholan-Tzeltalan, Cholan, Chorti.
cab  Garífuna  Garífuna  cab  Honduras  41  265938  1921664  CAB  -  -  cab  tet  en es  no  -  Sat Feb 2 15:42:26 CST 2013  CARIBE, CENTRAL AMERICAN CARIB, BLACK CARIB  Arawakan, Maipuran, Northern Maipuran, Caribbean.
cac  Chuj  -  cac  Guatemala  1  255644  1368076  CAC  -  -  -  kjb knj jac  en  no  -  Thu Jan 10 18:27:42 CST 2013  -  Mayan, Kanjobalan-Chujean, Chujean.
cac-x-cac  San Sebastián Coatán Chuj  -  cac  Guatemala  0  0  0  CAC  -  -  -  kjb knj cnm jac  en  no  -  -  -  Mayan, Kanjobalan-Chujean, Chujean.
caf  Southern Carrier  -  caf  Canada  2  226072  1539039  CAF  -  -  -  crx clc  en  no  -  Sun Dec 23 15:33:35 CST 2012  -  Na-Dene, Nuclear Na-Dene, Athapaskan-Eyak, Athapaskan, Canadian, Carrier-Chilcotin, Babine-Carrier.
cai-x-mixe  Mixe  -  cai  Mexico  15  1280093  8851853  -  -  -  -  ncu pps myu cjp mig crn zav  en  no  -  Thu Sep 26 23:41:18 CDT 2013  -  Mixe-Zoque, Mixe.
cak  Cakchiquel  Kaqchikel  cak  Guatemala  67  684332  3967551  CAK  cq  -  cak1  qut acr quc usp mhi acc pob tzt quj mxt  en es  no  Peter Rohloff, Jameson Quinn  Tue Oct 8 17:36:49 CDT 2013  KAQCHIQUEL  Mayan, Quichean-Mamean, Greater Quichean, Quichean, Cakchiquel.
cao  Chácobo  -  cao  Bolivia  2  257359  1545820  CAO  -  -  -  shp  en es  no  -  Sun Dec 23 15:54:03 CST 2012  -  Panoan, Southern.
cap  Chipaya  -  cap  Bolivia  2  243185  2047008  CAP  -  -  -  amc cao qxh mcf kaq nuz  en  no  -  Sun Dec 23 16:15:51 CST 2012  -  Uru-Chipaya.
car  Carib  Kari'nya euran  car  Venezuela  2  239400  1757415  CRB  crb  -  -  apy bbr zia dgz ain sue nca  en  no  -  Sun Dec 23 16:16:44 CST 2012  CARIBE, CARIÑA, KALIHNA, KALINYA, GALIBI  Carib, Northern, Galibi.
cas  Tsimané  -  cas  Bolivia  1  213922  1446606  CAS  -  -  -  ncj  en  no  -  Wed Jan 2 19:09:18 CST 2013  CHIMANÉ, MOSETÉN  Mosetenan.
cav  Cavineña  -  cav  Bolivia  1  282541  2096386  CAV  -  -  -  tna ese nhg aro es-x-cant azz nch arl ycn  en es  no  -  Mon Dec 24 07:06:21 CST 2012  -  Tacanan, Araona-Tacana, Cavinena-Tacana, Cavinena.
cax  Chiquitano  Bésiro  cax  Bolivia  4  359603  2780312  CAX  -  -  cax*  ay  en es  started  -  Tue Sep 10 10:04:41 CDT 2013  CHIQUITO, TARAPECOSI  Macro-Ge, Chiquito.
cax-x-ilv  Chiquitano  Bésiro  cax  Bolivia  0  0  0  CAX  -  -  -  cax tca gri  en es  no  Eddie Ávila  -  CHIQUITO, TARAPECOSI  Macro-Ge, Chiquito.
cay  Cayuga  Gayogo̱hó:nǫ’  cay  Canada  3  174  1420  CAY  -  -  -  pib sw  en  started  -  Mon Jan 28 18:21:34 CST 2013  -  Iroquoian, Northern Iroquoian, Five Nations, Seneca-Onondaga, Seneca-Cayuga.
cbc  Carapana  -  cbc  Colombia  3  354376  2437273  CBC  -  -  -  tav bao tuo-CO myy pir gvc des tuo sri srq bsn not zia  en es  no  -  Wed Dec 5 14:33:14 CST 2012  MOCHDA, MOXDOA, KARAPANÁ, KARAPANO, CARAPANA-TAPUYA, MEXTÃ  Tucanoan, Eastern Tucanoan, Central, Tatuyo.
cbi  Chachi  -  cbi  Ecuador  4  345474  2443542  CBI  -  -  1122  tpm cof cya kde ctp kng sml knk  en  no  -  Wed Jan 30 15:42:08 CST 2013  CAYAPA, CHA' PALAACHI  Barbacoan, Cayapa-Colorado.
cbk  Chavacano  -  cbk  Philippines  3  360672  2182083  CBK  -  cbk-zam  -  es lad ast ext ca-valencia oc gl lnc ca mwl lms  en  no  -  Sun Feb 3 23:26:24 CST 2013  ZAMBOANGUEÑO, CHABAKANO  Creole, Spanish based.
cbm  Yepocapa Southwestern Kaqchikel  -  cbm  Guatemala  1  339656  2075564  CBM  -  -  -  ckk usp acc cki  en es  no  -  Mon Dec 24 07:13:21 CST 2012  -  Mayan, Quichean-Mamean, Greater Quichean, Quichean, Cakchiquel.
cbr  Cashibo-Cacataibo  -  cbr  Peru  3  186175  1035609  CBR  -  -  cbr  cao qvo ncl cnt nch zai quw zaa nhw  en  no  -  Mon Dec 24 07:21:10 CST 2012  CAXIBO, CACIBO, CACHIBO, CAHIVO, MANAGUA, HAGUETI  Panoan, Western.
cbs  Cashinahua  -  cbs  Peru  3  291432  2102631  CBS  -  -  cbs  en  en es  no  -  Wed Oct 3 20:35:32 CDT 2012  KAXINAWÁ, KAXYNAWA, CAXINAWA, CAXINAWÁ  Panoan, Southeastern.
cbt  Chayahuita  -  cbt  Peru  4  758573  4239939  CBT  -  -  cbt  qxw nah ncj mcd toc vap hva  en  no  -  Mon Dec 24 07:27:44 CST 2012  CHAYAWITA, CHAWI, TSHAAHUI, CHAYHUITA, CHAYABITA, SHAYABIT, BALSAPUERTINO, PARANAPURA, CAHUAPA  Cahuapanan.
cbu  Candoshi-Shapra  -  cbu  Peru  3  233622  2024920  CBU  -  -  cbu  gof bmk aui pwg  en  no  -  Mon Dec 24 07:28:22 CST 2012  KANDOSHI, CANDOSHI, CANDOXI, MURATO  Unclassified.
cbv  Cacua  -  cbv  Colombia  2  388586  2311210  CBV  -  -  -  kzi cnh hlt cnk bgr tav  en  no  -  Mon Dec 24 07:30:42 CST 2012  MACU DE CUBEO, MACU DE GUANANO, MACU DE DESANO, BÁDA, KÁKWA  Maku.
ccn-x-circassian  Circassian languages  Адыгэбзэ  ccn  Russian Federation  4625  5615220  41424060  -  -  -  -  cu ru  en ru  no  -  Tue Oct 8 18:33:26 CDT 2013  -  North Caucasian, Northwest, Circassian.
cco  Comaltepec Chinantec  -  cco  Mexico  4  386256  2156320  CCO  -  -  -  chj nap chq cnt fuf  en  no  -  Mon Dec 24 07:34:31 CST 2012  -  Oto-Manguean, Chinantecan.
ccx  Northern Zhuang  -  ccx  China  0  0  0  -  -  -  -  pam tl af jv vi agn czo jvn cdo nas  en  no  -  -  -  Tai-Kadai, Kam-Tai, Tai, Northern
cdo  Min Dong Chinese  Mìng-dĕ̤ng-ngṳ̄  cdo  China  2  86708  595763  CDO  -  cdo  -  vi tl pam  en  no  -  Sat Jan 12 21:59:18 CST 2013  EASTERN MIN  Sino-Tibetan, Chinese.
ce  Chechen  Нохчийн  che  Russian Federation  820  3410344  22165408  CJC  he*  ce  -  inh mk sah bg dar sr ky gag-Cyrl agx krc ru  en ru  no  Sarah Slye, Dietmar Fiesel  Sun Nov 3 18:17:37 CST 2013  -  North Caucasian, East Caucasian, Nakh, Chechen-Ingush.
ceb  Cebuano  Sinugboanong Binisaya  ceb  Philippines  194  1254911  7789674  CEB  cv  ceb  ceb  hil tl bik hnn krj iry akl jv kyk bno  en es  no  Joshua Verano  Sat Sep 14 09:37:06 CDT 2013  SUGBUHANON, SUGBUANON, VISAYAN, BISAYAN, BINISAYA, SEBUANO  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Meso Philippine, Central Philippine, Bisayan, Cebuan.
ceg  Chamacoco  -  ceg  Paraguay  1  492  2759  CEG  -  -  -  bzj pdt icr cs gsw  en  no  -  Mon Apr 8 21:01:30 CDT 2013  ISHIRO, JEYWO  Zamucoan.
cfm  Falam Chin  -  cfm  Myanmar  2  229178  1140321  HBH  -  -  fal  cnh bgr mwq ctd lus cnk hlt vap tcz zlm bjn  en  no  -  Sun Sep 15 23:35:20 CDT 2013  -  Sino-Tibetan, Tibeto-Burman, Kuki-Chin-Naga, Kuki-Chin, Northern.
ch  Chamorro  Chamoru  cha  Guam  64  933759  5956563  CJD  cm  ch  cjd  pag sml  en es  started  -  Sat Jan 12 22:11:37 CST 2013  TJAMORO  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Chamorro.
chd  Highland Oaxaca Chontal  -  chd  Mexico  2  213072  1762457  CHD  -  -  -  ncl nhw nch cof ino cav nhe  en  no  -  Mon Dec 24 07:35:10 CST 2012  HIGHLAND OAXACA CHONTAL, MOUNTAIN TEQUISTLATECO, TEQUISTLATEC  Hokan, Tequistlatecan.
chf  Tabasco Chontal  -  chf  Mexico  3  351377  1889571  CHF  -  -  -  lac mop ixi yua ixl acc quj tzj-x-eastern tiv  en  no  -  Mon Dec 24 07:36:17 CST 2012  YOCOT'AN  Mayan, Cholan-Tzeltalan, Cholan, Chol-Chontal.
chj  Ojitlán Chinanteco  -  chj  Mexico  2  6724  29327  CHJ  -  -  chj  cpa cnt  en  no  -  Sat Jan 12 23:05:38 CST 2013  -  Oto-Manguean, Chinantecan.
chk  Chuukese  Chuuk  chk  Micronesia  65  78332  477705  TRU  te  -  tru1  aau na  en  no  -  Fri Sep 13 14:24:16 CDT 2013  CHUUK, TRUK, TRUKESE, RUK, LAGOON CHUUKESE  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Micronesian, Micronesian Proper, Ponapeic-Trukic, Trukic.
chm  Mari  -  chm  Russian Federation  2  417386  3070130  -  -  -  -  ky koi  en ru  no  -  Tue Jan 22 14:02:26 CST 2013  CHEREMISS, MARI-HILLS, GORNO-MARIY  Uralic, Finno-Ugric, Finno-Permic, Finno-Cheremisic, Cheremisic.
chn  Chinook Wawa  Chinuk Wawa  chn  Canada  3  4405  30949  CRW  -  -  -  qug sw  en  no  Chase May  Wed Sep 18 19:30:15 CDT 2013  CHINOOK JARGON, CHINOOK PIDGIN  Pidgin, Amerindian.
cho  Choctaw  Chahta'  cho  USA  6  634394  3450929  CCT  -  cho  -  haw inb  en  no  Chris Harvey  Sat Jan 12 23:12:27 CST 2013  -  Muskogean, Western.
chp  Dene  Dënesųłıné  chp  Canada  3  1508  11066  CPW  -  -  -  scs clc  en  no  -  Sat Jan 12 23:10:24 CST 2013  CHIPEWYAN  Na-Dene, Nuclear Na-Dene, Athapaskan-Eyak, Athapaskan, Canadian, Hare-Chipewyan, Chipewyan.
chq  Quiotepec Chinantec  -  chq  Mexico  2  293095  1773438  CHQ  -  -  -  azg oj fkv mog  en  no  -  Mon Dec 24 07:38:52 CST 2012  HIGHLAND CHINANTECO  Oto-Manguean, Chinantecan.
chr  Cherokee  ᏣᎳᎩ  chr  USA  42  383108  2117275  CER  -  chr  chr  -  en  no  Joseph Erb, Roy Boney  Wed Jan 30 15:43:08 CST 2013  Tsalagi, Tslagi  Elati (Lower Cherokee, Eastern Cherokee), Kituhwa (Middle Cherokee), Otali (Upper Cherokee, Western Cherokee, Overhill Cherokee), Overhill-Middle Cherokee.
chr-Latn  Cherokee (Latin)  Tsalagi  chr  USA  27  61789  420179  CER  -  -  -  bpr bps pap-CW co scn yml pov dob pap  en  no  -  Sat Jan 12 23:13:47 CST 2013  Tsalagi, Tslagi  Elati (Lower Cherokee, Eastern Cherokee), Kituhwa (Middle Cherokee), Otali (Upper Cherokee, Western Cherokee, Overhill Cherokee), Overhill-Middle Cherokee.
chw  Chuwabu  Etxuwabo  chw  Mozambique  1  6902  48676  CHW  co  -  -  ngl  en  no  -  Thu Jan 17 10:43:05 CST 2013  CHWABO, CUWABO, CUABO, CHUABO, CHUAMBO, CHWAMPO, CUAMBO, CHICHWABO, CICUABO, TXUWABO, ECHUWABO, ECHUABO, LOLO  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, P, Makua (P.30).
chy  Cheyenne  Tsetsêhestâhese  chy  USA  4  4219  46748  CHY  -  chy  -  apy gub st  en  no  -  Sat Jan 12 23:16:05 CST 2013  -  Algic, Algonquian, Plains.
chz  Ozumacín Chinantec  -  chz  Mexico  3  327447  1835974  CHZ  -  -  -  cle cpa chj  en  no  -  Mon Dec 24 07:39:56 CST 2012  -  Oto-Manguean, Chinantecan.
cic  Chickasaw  -  cic  USA  3  3085  32722  CIC  -  -  cic  ptu cho  en  no  -  Sat Jan 12 23:15:45 CST 2013  -  Muskogean, Western.
cim  Cimbrian  Zimbrisch  cim  Italy  6  300  2175  CIM  -  -  -  sco-x-scotland gsw pfl bar pdc hsf vmf li sco zea  en  no  -  Sun Sep 22 20:44:06 CDT 2013  TZIMBRO, ZIMBRISCH  Indo-European, Germanic, West, High German, German, Upper German, Bavarian-Austrian.
cjk  Chokwe  Chokwe  cjk  Dem. Rep. of Congo  7  12701  83678  CJK  ck  -  cjk  lue nba gog kki loz toi nym  en  no  -  Sat Feb 2 15:55:59 CST 2013  COKWE, CIOKWE, TSHOKWE, TSCHIOKWE, SHIOKO, DJOK, IMO  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, K, Chokwe-Luchazi (K.20).
cjm  Eastern Cham  -  cjm  Viet Nam  1  2250  11116  CJM  -  -  -  jv tl vi  en vi  no  -  Fri Dec 21 09:46:55 CST 2012  TJAM, CHIEM, CHIEM THÀNH, BHAMAM  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Sundic, Malayic, Achinese-Chamic, Chamic, South, Coastal, Cham-Chru.
cjo  Ashéninka Pajonal  -  cjo  Peru  3  360674  3862097  CJO  -  -  -  cpu  en es  no  -  Wed Oct 3 20:51:54 CDT 2012  ATSIRI, PAJONAL, CAMPA  Arawakan, Maipuran, Southern Maipuran, Campa.
cjp  Cabécar  -  cjp  Costa Rica  4  201437  1073491  CJP  -  -  -  sw  en  no  -  Wed Jan 2 19:27:54 CST 2013  CHIRRIPÓ  Chibchan, Talamanca.
cjs  Shor  Шор тили  cjs  Russian Federation  2  1191  8997  CJS  -  -  cjs  kjh kaa-Cyrl alt kk tyv ky gag-Cyrl  en  no  -  Wed Sep 18 19:33:24 CDT 2013  SHORTSY, ABA, KONDOMA TATAR, MRAS TATAR, KUZNETS TATAR, TOM-KUZNETS TATAR  Altaic, Turkic, Northern.
cjv  Chuave  -  cjv  Papua New Guinea  217  286731  1621707  CJV  -  -  -  kue  en  no  -  Thu Jan 10 16:37:25 CST 2013  TJUAVE  Trans-New Guinea, Main Section, Central and Western, East New Guinea Highlands, Central, Chimbu.
ckb  Central Kurdish  کوردی  ckb  Iraq  33358  34775062  252873467  CKB  rda*  ckb  -  lki pes bal glk prs azb-Arab  en fa ar  no  Sahand T.  Mon Sep 30 23:49:55 CDT 2013  KURDI, SORANI  Indo-European, Indo-Iranian, Iranian, Western, Northwestern, Kurdish
cke  Eastern Kaqchikel  -  cke  Guatemala  1  330048  1887546  CKE  -  -  -  cki ckw qut acr  en es  no  -  Mon Dec 24 07:44:20 CST 2012  -  Mayan, Quichean-Mamean, Greater Quichean, Quichean, Cakchiquel.
cki  Santa María de Jesús Kaqchikel  -  cki  Guatemala  2  303293  1809770  CKI  -  -  -  ckw qut acr  en es  no  -  Mon Dec 24 07:46:26 CST 2012  -  Mayan, Quichean-Mamean, Greater Quichean, Quichean, Cakchiquel.
ckk  Akatenango Southwestern Kaqchikel  -  ckk  Guatemala  1  288998  1698752  CKK  -  -  -  cbm acc usp tzt  en es  no  -  Thu Jan 3 09:03:21 CST 2013  -  Mayan, Quichean-Mamean, Greater Quichean, Quichean, Cakchiquel.
cko  Anufo  -  cko  Ghana  1  270738  1123117  CKO  -  -  -  bm dyu bba  en  no  -  Thu Jan 3 09:31:03 CST 2013  CHOKOSI, CHAKOSI, KYOKOSI, TCHOKOSSI, TIOKOSSI  Niger-Congo, Atlantic-Congo, Volta-Congo, Kwa, Nyo, Potou-Tano, Tano, Central, Bia, Northern.
ckt  Chukchi  Ԓыгъоравэтԓьэн йиԓыйиԓ  ckt  Russian Federation  5  17918  170628  CKT  -  -  -  udm kbd ru alr  en  no  -  Wed Sep 18 19:34:07 CDT 2013  CHUKCHA, CHUCHEE, CHUKCHEE, LUORAVETLAN, CHUKCHI  Chukotko-Kamchatkan, Northern, Chukot.
ckv  Kavalan  Kbaran  ckv  Taiwan  5  456  3025  CKV  -  -  -  bik pag bjn ifk sml slm ifb hnn bnc sda  en  no  -  Sun Sep 22 20:54:57 CDT 2013  KUWARAWAN, KIWARAWA, KUVARAWAN, KIBALAN, KIWARAW, KUVALAN, KAVARAUAN, KVALAN, SHEKWAN, CABARAN, KABALAN, KABARAN, KAMALAN, KAVANAN, KBALAN  Austronesian, Formosan, Paiwanic.
ckw  Western Kaqchikel  -  ckw  Guatemala  3  407332  2258003  CKW  -  -  -  qut  en es  no  -  Thu Jan 10 21:37:05 CST 2013  -  Mayan, Quichean-Mamean, Greater Quichean, Quichean, Cakchiquel.
clc  Chilcotin  Tsilhqot’in  clc  Canada  0  0  0  CHI  -  -  -  caf bcr  en  no  -  -  TZILKOTIN  Na-Dene, Nuclear Na-Dene, Athapaskan-Eyak, Athapaskan, Canadian, Carrier-Chilcotin, Chilcotin.
cle  Lealao Chinantec  -  cle  Mexico  3  349684  2320366  CLE  -  -  -  cso cpa ifu otn tzt vap tcz mks ctd  en  no  -  Mon Dec 24 08:27:42 CST 2012  SAN JUAN LEALAO CHINANTECO  Oto-Manguean, Chinantecan.
cme  Cerma  -  cme  Burkina Faso  1  192021  1073568  GOT  -  -  -  xsm om  en  no  -  Thu Jan 3 09:57:47 CST 2013  GOUIN, GWE, GWEN, KIRMA  Niger-Congo, Atlantic-Congo, Volta-Congo, North, Gur, Central, Southern, Kirma-Tyurama.
cmn  Mandarin Chinese  官话  cmn  China  182  121383  1101903  CHN  chs  zh  chn  ja gan zh-Hant  en  no  -  Sat Sep 14 09:25:09 CDT 2013  MANDARIN, GUANHUA, BEIFANG FANGYAN, NORTHERN CHINESE, GUOYU, STANDARD CHINESE, PUTONGHUA  Sino-Tibetan, Chinese.
cmn-Hant  Mandarin Chinese (Traditional)  -  cmn  China  1  167  3437  CHN  -  -  cmn_hant  lzh yue gan wuu  en  no  -  Mon Dec 9 14:14:46 CST 2013  MANDARIN, GUANHUA, BEIFANG FANGYAN, NORTHERN CHINESE, GUOYU, STANDARD CHINESE, PUTONGHUA  Sino-Tibetan, Chinese.
cmn-Latn  Mandarin Chinese (Pinyin)  Pīnyīn  cmn  China  404  1618268  8364178  CMN  -  -  -  an vi pam  en  no  -  Sun Jan 13 00:15:44 CST 2013  Beifang Fangyan, Guanhua, Guoyu, Hanyu, Mandarin, Northern Chinese, Putonghua, Standard Chinese  Sino-Tibetan, Chinese
cnh  Haka Chin  Lai Pawi  cnh  Myanmar  69  1269658  6127330  CNH  hk  -  hak  lus bgr cnk vap mwq  en  no  -  Wed Sep 18 19:36:50 CDT 2013  HAKA, HAKHA, BAUNGSHE  Sino-Tibetan, Tibeto-Burman, Kuki-Chin-Naga, Kuki-Chin, Central.
cni  Asháninca  -  cni  Peru  4  174699  1898483  CNI  -  -  cni  cot cpu  en  no  -  Wed Oct 3 20:46:04 CDT 2012  'CAMPA'  Arawakan, Maipuran, Southern Maipuran, Campa.
cnk  Khumi Chin  -  cnk  Myanmar  1  236324  1226526  CNK  -  -  -  bgr cnh lus su jv pam tl  en  no  -  Thu Jan 3 10:06:47 CST 2013  Khami, Khimi, Khumi, Khuni, Khweymi  Sino-Tibetan, Tibeto-Burman, Kuki-Chin-Naga, Kuki-Chin, Southern, Khumi.
cnl  Lalana Chinantec  -  cnl  Mexico  2  305707  2094665  CNL  -  -  -  cpa cnt zaa zpc chj zav zad zpu  en  no  -  Mon Dec 24 08:33:48 CST 2012  -  Oto-Manguean, Chinantecan.
cnm  Ixtatán Chuj  -  cnm  Guatemala  3  1104720  6175110  CNM  -  -  -  cac knj  en  no  -  Thu Jan 10 18:28:08 CST 2013  CHUH, CHUJE, CHUHE  Mayan, Kanjobalan-Chujean, Chujean.
cnt  Tepetotutla Chinantec  -  cnt  Mexico  2  307361  2021182  CNT  -  -  -  cpa cso cuc chj cao cnl cbr mau acc  en  no  -  Mon Dec 24 08:46:30 CST 2012  -  Oto-Manguean, Chinantecan.
co  Corsican  Corsu  cos  France  150  791393  4686385  COI  -  co  coi  scn pap-CW pap rup it fur kea  en it fr  no  -  Tue Sep 10 19:51:55 CDT 2013  CORSU, CORSO, CORSE, CORSI  Indo-European, Italic, Romance, Southern, Corsican.
coe  Koreguaje  -  coe  Colombia  3  258341  2308558  COE  -  -  -  cbm ckk quj acc quc pob sey cut mbz mxt acr  en  no  -  Mon Dec 24 08:51:21 CST 2012  COREGUAJE, CORREGUAJE, KO'REUAJU, CAQUETÁ, CHAOCHA PAI  Tucanoan, Western Tucanoan, Northern, Coreguaje.
cof  Colorado  -  cof  Ecuador  3  307492  2306726  COF  -  -  cof  qvo cot cni nch kaq quw acc nhg cbi  en es  no  -  Wed Jan 30 15:54:00 CST 2013  TSACHILA  Barbacoan, Cayapa-Colorado.
cok  Santa Teresa Cora  -  cok  Mexico  1  1052  7820  COK  -  -  -  crn crn-x-presidio  en  no  -  Sat Jan 5 15:01:48 CST 2013  -  Uto-Aztecan, Southern Uto-Aztecan, Sonoran, Corachol.
con  Cofán  -  con  Ecuador  6  354435  2827568  CON  -  -  ccc*  snk sc cya pls zpq kaq sps tna mjc qwh  en es  no  -  Tue Sep 10 10:06:21 CDT 2013  KOFÁN, A'I, KOFANE  Chibchan, Cofan.
coo  Comox  -  coo  Canada  1  1524  9722  COO  -  -  -  mrh tzc tzo bkd lil-x-fou  en  no  -  Thu Jan 17 10:45:08 CST 2013  COMOX-SLIAMMON  Salishan, Central Salish, Northern.
coo-x-kla  Comox (Klahoose)  -  coo  Canada  0  0  0  COO  -  -  -  coo-x-sli  en  no  -  -  COMOX-SLIAMMON  Salishan, Central Salish, Northern.
coo-x-sli  Comox (Sliammon)  -  coo  Canada  0  0  0  COO  -  -  -  coo-x-kla  en  no  -  -  COMOX-SLIAMMON  Salishan, Central Salish, Northern.
cop  Coptic  ⲘⲉⲧⲢⲉⲙ̀ⲛⲭⲏⲙⲓ  cop  Egypt  3  210969  1381977  COP  -  -  -  -  en  yes  -  Mon Jan 21 09:54:27 CST 2013  NEO-EGYPTIAN  Afro-Asiatic, Egyptian.
cot  Caquinte  -  cot  Peru  3  195085  2417567  COT  -  -  cot  cni not  en  no  -  Mon Dec 24 09:41:51 CST 2012  CAQUINTE CAMPA, POYENISATI, 'CACHOMASHIRI'  Arawakan, Maipuran, Southern Maipuran, Campa.
cpa  Palantla Chinantec  -  cpa  Mexico  2  244281  1805880  CPA  -  -  -  chj cnt cnl cle ceb cso fil cuc tl jv cnh cao  en  no  -  Mon Dec 24 09:42:47 CST 2012  -  Oto-Manguean, Chinantecan.
cpb  Ucayali-Yurúa Ashéninka  -  cpb  Peru  0  0  0  CPB  -  -  -  cpu cjo mcb cni apu not sn  en es  no  -  -  -  Arawakan, Maipuran, Southern Maipuran, Campa.
cpc  Ajyíninka Apurucayali  -  cpc  Peru  0  0  0  CPC  -  -  -  cpb cpu cjo mcb cni apu not sn  en es  no  -  -  ASHÉNINCA APURUCAYALI, APURUCAYALI CAMPA, AJYÉNINKA, CAMPA  Arawakan, Maipuran, Southern Maipuran, Campa.
cps  Capiznon  Capiceño  cps  Philippines  72  12023  78519  CPS  -  -  -  en  en  no  -  Sun Sep 22 21:04:43 CDT 2013  CAPISANO, CAPISEÑO  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Meso Philippine, Central Philippine, Bisayan, Central, Peripheral.
cpu  Ashéninca Pichis  -  cpu  Peru  3  175471  1854665  CPU  -  -  cpu  cni cjo  en  no  -  Wed Oct 3 20:49:21 CDT 2012  PICHIS, ASHÉNINCA  Arawakan, Maipuran, Southern Maipuran, Campa.
cr  Cree  -  cre  Canada  6  55645  374173  -  -  cr  crm*  oj-Cans nsk iu  en  no  Chris Harvey  Tue Sep 10 10:14:12 CDT 2013  -  Algic, Algonquian, Central, Cree-Montagnais-Naskapi.
cr-Latn  Cree (Latin)  Nēhiyawēwin  cre  Canada  5  12335  112226  -  -  -  -  nez  en  no  -  Sun Jan 13 00:00:59 CST 2013  -  Algic, Algonquian, Central, Cree-Montagnais-Naskapi.
crg  Michif  -  crg  USA  9  13564  99230  CRG  -  -  -  mfe oj rcf kbr csk kek om cr-Latn enb  en fr  no  Dale McCreery  Sun Nov 3 19:06:36 CST 2013  FRENCH CREE, MITCHIF  Mixed Language, French-Cree.
crh  Crimean Tatar  Qırımtatar tili  crh  Uzbekistan  194  354739  2717803  CRH  -  crh  -  tr kaa tk az  en  no  -  Tue Sep 10 10:14:01 CDT 2013  CRIMEAN, CRIMEAN TURKISH  Altaic, Turkic, Southern.
cri  Sãotomense  Sãotomense  cri  São Tomé e Príncipe  33  108688  536481  CRI  -  -  1128  loz lch kea  en  no  -  Wed Jan 30 21:42:59 CST 2013  SÃO TOMENSE, FORRO  Creole, Portuguese based.
crk  Plains Cree  -  crk  Canada  3  1226  8317  CRP  -  -  -  csw oj-Cans nsk iu  en  no  Melanie Quinn  Sat Jan 12 23:56:54 CST 2013  WESTERN CREE  Algic, Algonquian, Central, Cree-Montagnais-Naskapi.
crk-Latn  Plains Cree (Latin)  -  crk  Canada  1  241  2527  CRP  -  -  -  csw-Latn sml sw lkt  en  no  Melanie Quinn  Sat Jan 12 23:58:19 CST 2013  WESTERN CREE  Algic, Algonquian, Central, Cree-Montagnais-Naskapi.
crm  Moose Cree  -  crm  Canada  0  0  0  CRM  -  -  -  csw ojb-Cans oj-Cans crk nsk ike scs-Cans iu den-Cans  en  no  -  -  YORK CREE, WEST SHORE CREE, WEST MAIN CREE  Algic, Algonquian, Central, Cree-Montagnais-Naskapi.
crn  El Nayar Cora  -  crn  Mexico  7  1065704  6774037  COR  -  -  -  crn-x-presidio  en  no  -  Mon Dec 24 09:46:19 CST 2012  -  Uto-Aztecan, Southern Uto-Aztecan, Sonoran, Corachol.
crn-x-presidio  Presidio de los Reyes  -  crn  Mexico  1  289552  2024830  COR  -  -  -  crn blz  en  no  -  Thu Jan 3 15:19:19 CST 2013  -  Uto-Aztecan, Southern Uto-Aztecan, Sonoran, Corachol.
crs  Seychelles Creole  Kreol Seselwa  crs  Seychelles  121  206404  1331610  CRS  sc  -  crs  rcf ht mfe acf lou  en fr  no  -  Sat Feb 2 16:13:55 CST 2013  SEYCHELLOIS CREOLE, SEYCHELLES CREOLE FRENCH, KREOL, CREOLE  Creole, French based.
crx  Carrier  -  crx  Canada  6  276193  1895425  CAR  -  -  -  caf  en  no  -  Thu Jan 10 21:45:44 CST 2013  CENTRAL CARRIER  Na-Dene, Nuclear Na-Dene, Athapaskan-Eyak, Athapaskan, Canadian, Carrier-Chilcotin, Babine-Carrier.
cs  Czech  Čeština  ces  Czech Republic  5476  10119141  68036547  CZC  b  cs  czc  sk sl  en  yes  -  Sat Feb 2 17:00:14 CST 2013  CESTINA, BOHEMIAN  Indo-European, Slavic, West, Czech-Slovak.
csa  Chinanteco  -  csa  Mexico  3  10869  52782  CSA  -  -  csa  fud  en  no  -  Sun Jan 13 08:31:34 CST 2013  -  Oto-Manguean, Chinantecan.
csb  Kashubian  Kaszëbsczi  csb  Poland  1262  1034354  6786271  CSB  -  csb  -  pl wen hsb  en pl  yes  Roman Drzeżdżon, Piotr Formella  Sun Jan 13 10:02:17 CST 2013  KASZUBSKI, CASHUBIAN, CASSUBIAN  Indo-European, Slavic, West, Lechitic.
csk  Jola-Kasa  -  csk  Senegal  2  252345  1694524  CSK  -  -  -  mt kek  en  yes  Outi Sane  Fri Jan 25 12:11:37 CST 2013  DIOLA-KASA, CASA, JÓOLA-KASA  Niger-Congo, Atlantic-Congo, Atlantic, Northern, Bak, Jola, Jola Proper, Jola Central, Jola-Kasa.
cso  Sochiapam Chinantec  -  cso  Mexico  2  339176  1947612  CSO  -  -  -  cnt cle cpa cof mjc chq cbr cao ifu cuc cnl  en es  no  -  Mon Dec 24 09:53:26 CST 2012  -  Oto-Manguean, Chinantecan.
csw  Swampy Cree  -  csw  Canada  2  2018  10284  CSW  -  -  crm  nsk iu  en  no  -  Wed Jan 30 15:56:18 CST 2013  YORK CREE, WEST SHORE CREE, WEST MAIN CREE  Algic, Algonquian, Central, Cree-Montagnais-Naskapi.
csw-Latn  Swampy Cree (Latin)  -  csw  Canada  0  0  0  CSW  -  -  -  nez crk-Latn moe ppl fai apu qug mic gdn  en  no  -  -  YORK CREE, WEST SHORE CREE, WEST MAIN CREE  Algic, Algonquian, Central, Cree-Montagnais-Naskapi.
cta  Tataltepec Chatino  -  cta  Mexico  4  473395  2389389  CTA  -  -  -  cya otn oto zpz mig mks mxb zai trq zaq mzi  en  no  -  Mon Dec 24 09:54:56 CST 2012  LOWLAND CHATINO  Oto-Manguean, Zapotecan, Chatino.
ctd  Tedim Chin  -  ctd  Myanmar  145  629949  3385164  CTD  -  -  tid  vap tcz lus cnh  en  no  -  Wed Jan 30 15:49:01 CST 2013  TEDIM, TIDDIM  Sino-Tibetan, Tibeto-Burman, Kuki-Chin-Naga, Kuki-Chin, Northern.
cti  Tila Chol  -  cti  Mexico  2  302185  1651333  CTI  chl  -  -  tzu tzo tzc tzz sg ilo yo ssg cuc its men acc cko  en  no  -  Thu Dec 27 14:04:57 CST 2012  -  Mayan, Cholan-Tzeltalan, Cholan, Chol-Chontal.
cto  Emberá-Catío  -  cto  Colombia  1  97973  704785  CTO  -  -  -  sja  en  no  -  Mon Dec 31 06:47:10 CST 2012  CATIO, KATIO, EMBENA, EYABIDA  Choco, Embera, Northern.
ctp  Western Highland Chatino  -  ctp  Mexico  3  489926  2487226  CTP  -  -  -  cya mbz mpm ctu mza xtn mxv lus hus itv ppl  en  no  -  Thu Dec 27 14:06:33 CST 2012  CHATINO DE LA ZONA ALTA OCCIDENTAL, WESTERN HIGHLAND CHATINO  Oto-Manguean, Zapotecan, Chatino.
ctu  Chol  -  ctu  Mexico  28  984519  5602013  CTU  chl  -  -  cti tzo ctp acc tzc mop tzu lac tzz knj  en  no  -  Sat Feb 2 16:14:38 CST 2013  -  Mayan, Cholan-Tzeltalan, Cholan, Chol-Chontal.
cu  Old Church Slavonic  Словѣньскъ  chu  Russian Federation  2  22625  158850  SLN  -  cu  -  ru  en  no  -  Thu Jan 10 22:31:10 CST 2013  -  Indo-European, Slavic, South, Eastern.
cua  Cua  -  cua  Viet Nam  1  1213  6000  CUA  -  -  -  ceb  en vi  no  -  Mon Dec 10 17:52:42 CST 2012  BONG MIEW, BÒNG MIEU  Austro-Asiatic, Mon-Khmer, Eastern Mon-Khmer, Bahnaric, North Bahnaric, East, Cua-Kayong.
cub  Cubeo  -  cub  Colombia  2  310899  2265439  CUB  -  -  -  tav myy des gym pir bao nen gvc  en  no  -  Thu Dec 27 14:10:00 CST 2012  CUVEO, KOBEUA, KUBWA, KOBEWA, PAMIWA, HEHENAWA  Tucanoan, Central Tucanoan.
cuc  Usila Chinantec  -  cuc  Mexico  2  254483  1954134  CUS  -  -  -  cnh lus cnt cfm due bas cti kno lbb dln acc  en  no  -  Thu Dec 27 14:09:59 CST 2012  -  Oto-Manguean, Chinantecan.
cui  Cuiba  -  cui  Colombia  30  670530  4970410  CUI  -  -  -  guh mwc tbo aro ura tpa soq  en es  no  -  Wed Dec 5 15:48:23 CST 2012  CUIVA, CUIBA-WÁMONAE  Guahiban.
cuk  San Blas Kuna  Dule gaya  cuk  Panama  186  513773  4095801  CUK  un  -  -  kvn sat br-x-unified br br-x-falhuneg ga-Latg bn-Latn yol otq ga  en  no  -  Sat Feb 2 16:54:59 CST 2013  SAN BLAS CUNA  Chibchan, Kuna.
cul  Kulina  -  cul  Brazil  3  18287  112973  CUL  -  -  -  arl  en es  no  -  Sun Jan 6 08:58:23 CST 2013  KULÍNA, KULYNA, CORINA, MADIJA, MADIHÁ  Arauan.
cut  Teutila Cuicatec  -  cut  Mexico  2  272664  1535795  CUT  -  -  -  quj bzj  en es  no  -  Thu Dec 27 14:15:10 CST 2012  -  Oto-Manguean, Mixtecan, Mixtec-Cuicatec, Cuicatec.
cux  Tepeuxila Cuicatec  -  cux  Mexico  2  377618  2201541  CUX  -  -  -  mio mxt mie acc pob mil  en  no  -  Thu Dec 27 14:15:40 CST 2012  -  Oto-Manguean, Mixtecan, Mixtec-Cuicatec, Cuicatec.
cv  Chuvash  Чӑваш  chv  Russian Federation  1510  1791188  14890664  CJU  cu  cv  -  ru bg  en ru  yes  Hèctor Alòs i Font  Fri Sep 13 14:25:45 CDT 2013  BULGAR  Altaic, Turkic, Bolgar.
cwt  Kuwaataay  -  cwt  Senegal  1  167217  1068346  CWT  -  -  -  dyo mbt  en  no  -  Thu Jan 3 16:03:49 CST 2013  KWATAY  Niger-Congo, Atlantic-Congo, Atlantic, Northern, Bak, Jola, Jola Proper, Kwatay.
cy  Welsh  Cymraeg  cym  Wales  2462  15862509  95811412  WLS  w  cy  wls  kw en  en  yes  Andrew Hawke, Dewi Evans, Kevin Donnelly  Fri Sep 13 11:18:50 CDT 2013  CYMRAEG  Indo-European, Celtic, Insular, Brythonic.
cya  Nopala Chatino  -  cya  Mexico  1  245043  1248227  CYA  -  -  -  ctp mio ncj cta  en  no  -  Thu Jan 3 16:15:29 CST 2013  -  Oto-Manguean, Zapotecan, Chatino.
czo  Min Zhong Chinese  -  czo  China  0  0  0  CZO  -  -  -  cdo pam vi tl agn nan jv jvn bru cmn-Latn ban  en  no  -  -  CENTRAL MIN  Sino-Tibetan, Chinese.
czt  Zotung Chin  -  czt  Myanmar  7  86486  509267  CZT  zo  -  -  cnk cnh lus mwq  en  no  -  Sun Jan 13 13:13:17 CST 2013  ZOTUNG, BANJOGI, BANDZHOGI  Sino-Tibetan, Tibeto-Burman, Kuki-Chin-Naga, Kuki-Chin, Central.
da  Danish  Dansk  dan  Denmark  763  1507911  9608681  DNS  d  da  dns  nb nn sv  en  yes  -  Sat Feb 2 17:26:15 CST 2013  DANSK, CENTRAL DANISH, SJAELLAND  Indo-European, Germanic, North, East Scandinavian, Danish-Swedish, Danish-Bokmal, Danish.
daa  Dangaléat  -  daa  Chad  0  0  0  DAA  -  -  -  son ha aa so bm  en  no  -  -  DANGLA, DANAL, DANGAL  Afro-Asiatic, Chadic, East, B, B.1, 1.
dad  Marik  -  dad  Papua New Guinea  0  0  0  DAD  -  -  -  tbc kne ifk ifb sbl ha  en  no  -  -  DAMI, HAM  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Ngero-Vitiaz, Vitiaz, Bel, Nuclear Bel, Southern.
daf  Dan  -  daf  Côte d’Ivoire  2  664605  3439848  DAF  -  -  -  moa  en  no  -  Thu Jan 3 18:39:54 CST 2013  YACOUBA, YAKUBA, DA, GIO, GIO-DAN  Niger-Congo, Mande, Eastern, Southeastern, Guro-Tura, Tura-Dan-Mano, Tura-Dan.
dag  Dagbani  -  dag  Ghana  3  9709  49683  DAG  -  -  dag  maw hag bm gux kus ify  en  no  -  Sat Jan 5 14:08:21 CST 2013  DAGBANE, DAGOMBA, DAGBAMBA  Niger-Congo, Atlantic-Congo, Volta-Congo, North, Gur, Central, Northern, Oti-Volta, Western, Southeast.
dah  Gwahatike  -  dah  Papua New Guinea  282  350260  2015985  DAH  -  -  -  nop  en  no  -  Fri Dec 28 20:31:57 CST 2012  GWATIKE, DAHATING  Trans-New Guinea, Main Section, Central and Western, Huon-Finisterre, Finisterre, Warup.
dak  Dakota  -  dak  USA  30  285005  1728385  DHG  -  -  -  lkt nii pon fai hus hsf ncj kut bim fi kms  en  no  -  Sat Jan 19 18:47:42 CST 2013  SIOUX  Siouan, Siouan Proper, Central, Mississippi Valley, Dakota.
dar  Dargwa  Дарган  dar  Russian Federation  1  858  6873  DAR  drg  -  -  krc inh tab  en  no  -  Thu Jan 17 10:47:08 CST 2013  DARGIN, DARGINTSY, KHIURKILINSKII  North Caucasian, Northeast, Lak-Dargwa.
ddg  Fataluku  Fataluku  ddg  East Timor  8  2696  17370  DDG  -  -  -  tet gfk ksd leu tgp hla nsn gri snk bnp  en  no  -  Sun Sep 22 21:09:04 CDT 2013  DAGAGA, DAGODA', DAGADA  Trans-New Guinea, South Bird's Head-Timor-Alor-Pantar, Timor-Alor-Pantar, Fataluku.
ddn  Dendi  -  ddn  Benin  2  3223  16234  DEN  -  -  den  hag bm  en  no  -  Tue Sep 10 10:14:41 CDT 2013  DANDAWA  Nilo-Saharan, Songhai, Southern.
de  German  Deutsch  deu  Germany  1038  2130778  15369908  GER  x  de  ger  pdc lb nds gsw nl  en  yes  Ed Jahn  Sat Feb 2 19:00:06 CST 2013  DEUTSCH, HOCHDEUTSCH, HIGH GERMAN  Indo-European, Germanic, West, High German, German, Middle German, East Middle German.
de-AT  German (Austria)  Deutsch  deu  Austria  697  1367218  10276122  GER  x  -  -  pdc lb nds gsw nl  en  yes  Ed Jahn  Sun Jan 13 13:58:02 CST 2013  DEUTSCH, HOCHDEUTSCH, HIGH GERMAN  Indo-European, Germanic, West, High German, German, Middle German, East Middle German.
de-CH  German (Switzerland)  Deutsch  deu  Switzerland  342  761769  5702555  GER  x  -  -  pdc lb nds gsw nl  en  yes  Ed Jahn  Sun Jan 13 13:57:34 CST 2013  DEUTSCH, HOCHDEUTSCH, HIGH GERMAN  Indo-European, Germanic, West, High German, German, Middle German, East Middle German.
de-DE  German (Germany)  Deutsch  deu  Germany  543  897013  6804065  GER  x  -  -  pdc lb nds gsw nl  en  yes  Ed Jahn  Sun Jan 13 15:04:15 CST 2013  DEUTSCH, HOCHDEUTSCH, HIGH GERMAN  Indo-European, Germanic, West, High German, German, Middle German, East Middle German.
ded  Dedua  -  ded  Papua New Guinea  269  267843  1930474  DED  -  -  -  mpp kgf yuw tby uvl  en  no  -  Fri Dec 28 20:34:30 CST 2012  -  Trans-New Guinea, Main Section, Central and Western, Huon-Finisterre, Huon, Eastern.
del  Delaware  Lenape  del  USA  0  0  0  -  -  -  -  fj gri twu kki dug dig qvz ssx  en  no  -  -  DELAWARE, LENNI-LENAPE, LENAPE, TLA WILANO  Algic, Algonquian, Eastern.
den  Slave  -  den  Canada  0  0  0  -  -  -  -  chp  en  no  -  -  SLAVI, DENÉ, MACKENZIAN, 'SLAVE'  Na-Dene, Nuclear Na-Dene, Athapaskan-Eyak, Athapaskan, Canadian, Hare-Chipewyan, Hare-Slavey.
den-Cans  Slave (Syllabics)  -  den  Canada  0  0  0  -  -  -  -  cr oj-Cans iu  en  no  -  -  SLAVI, DENÉ, MACKENZIAN, 'SLAVE'  Na-Dene, Nuclear Na-Dene, Athapaskan-Eyak, Athapaskan, Canadian, Hare-Chipewyan, Hare-Slavey.
des  Desano  -  des  Brazil  1  236260  1590562  DES  -  -  -  sri bao srq bsn  en  no  -  Sat Dec 29 16:43:53 CST 2012  DESÂNA, DESSANO, WINA, UINA, WIRÃ, BOLEKA, OREGU, KUSIBI  Tucanoan, Eastern Tucanoan, Central, Desano.
dga  Dagaare  -  dga  Ghana  2  7779  34823  DGA  -  -  dga  pam lnu mzm jv  en  no  -  Sun Jan 13 14:25:07 CST 2013  SOUTHERN DAGARI, DAGARI, DAGARA, DEGATI, DAGATI, DOGAARI, DAGAARE  Niger-Congo, Atlantic-Congo, Volta-Congo, North, Gur, Central, Northern, Oti-Volta, Western, Northwest, Dagaari-Birifor, Dagaari.
dgc  Casiguran Dumagat Agta  -  dgc  Philippines  0  0  0  DGC  -  -  -  due bnp ivv lcm leu fj snk pag ksd gri blz lbb kqw pap  en  no  -  -  CASIGURAN DUMAGAT  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Northern Philippine, Northern Luzon, Northern Cordilleran, Dumagat, Northern.
dgi  Northern Dagara  -  dgi  Burkina Faso  3  261260  1049763  DGI  -  -  -  biv maf ktj  en fr  no  -  Thu Jan 3 19:45:14 CST 2013  NORTHERN DAGAARE, DAGARI, DEGATI, DAGATI, DOGAARI, DAGAARI, DAGAARE  Niger-Congo, Atlantic-Congo, Volta-Congo, North, Gur, Central, Northern, Oti-Volta, Western, Northwest, Dagaari-Birifor, Dagaari.
dgo  Dogri  डोगरी  dgo  India  11  8560  46073  -  -  -  -  mai mr hi ne  en  no  -  Wed Sep 18 19:39:28 CDT 2013  Dhogaryali, Dogari, Dogri Jammu, Dogri Pahari, Dogri-Kangri, Dongari, Hindi Dogri, Tokkaru  Indo-European, Indo-Iranian, Indo-Aryan, Northern zone, Western Pahari.
dgz  Daga  -  dgz  Papua New Guinea  0  0  0  DGZ  -  -  -  tbc ifk ha ifb ppl bjn ain snk  en  no  -  -  DIMUGA, NAWP  Trans-New Guinea, Main Section, Eastern, Central and Southeastern, Dagan.
dhv  Drehu  Drehu  dhv  New Caledonia  2  14207  75133  DEU  lf  -  -  kus  en  no  -  Fri Sep 13 14:25:37 CDT 2013  DE'U, DREHU, LIFOU, LIFU  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Loyalty Islands.
dig  Chidigo  -  dig  Kenya  2  150246  1032158  DIG  -  -  -  dug nyf sw wmw  en  no  -  Thu Jan 3 19:55:13 CST 2013  KIDIGO, CHIDIGO  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, E, Nyika (E.40), Mijikenda.
dik  Southwestern Dinka  -  dik  Sudan  34  319339  1540444  DIK  -  -  dinka  dip  en  no  -  Thu Dec 27 14:20:20 CST 2012  REK, WESTERN DINKA  Nilo-Saharan, Eastern Sudanic, Nilotic, Western, Dinka-Nuer, Dinka.
din  Dinka  -  din  Sudan  33  471847  2236098  -  -  -  -  hif kos cri yon lwo mbi izr efi ku kmr alz  en  no  -  Tue Sep 10 10:15:10 CDT 2013  -  Nilo-Saharan, Eastern Sudanic, Nilotic, Western, Dinka-Nuer, Dinka.
dip  Northeastern Dinka  -  dip  Sudan  2  195092  898330  DIP  -  -  dinka  dik  en  no  -  Wed Jan 30 20:33:06 CST 2013  PADANG, WHITE NILE DINKA  Nilo-Saharan, Eastern Sudanic, Nilotic, Western, Dinka-Nuer, Dinka.
diq  Dimli  Zazaki  diq  Turkey  100  1136044  6697117  DIQ  -  diq  -  kmr ote  en tr  no  -  Tue Sep 10 10:21:17 CDT 2013  DIMILI, ZAZAKI, SOUTHERN ZAZA, ZAZA  Indo-European, Indo-Iranian, Iranian, Western, Northwestern, Zaza-Gorani.
diu  Diriku  -  diu  Namibia  15  3172  24154  DIU  -  -  -  kwn lue tum sn kj nba bem  en  no  -  Fri Sep 13 21:14:14 CDT 2013  DIRIKO, GCIRIKU, RUGCIRIKU, MBOGEDO, MBOGEDU, SHIMBOGEDU  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, K, Diriku (K.70).
djk  Eastern Maroon Creole  -  djk  Suriname  4  311694  1368221  DJK  -  -  -  srm srn  en  no  -  Sat Feb 2 18:06:41 CST 2013  NDYUKA, NDJUKÁ, NJUKÁ, 'DJUKA', 'DJOEKA', AUKAANS, OKANISI, AUKAN  Creole, English based, Atlantic, Suriname, Ndyuka.
djr  Djambarrpuyngu  Yolŋu Matha  djr  Australia  55  424613  3555034  DJR  -  -  -  ibd  en  no  -  Mon Oct 1 20:13:27 CDT 2012  DJAMBARBWINGU, JAMBAPUING, JAMBAPUINGO  Australian, Pama-Nyungan, Yuulngu, Dhuwal.
dlc  Elfdalian  Övdalską  dlc  Sweden  3  34987  183895  DLC  -  -  -  is fo nn nb  en sv  started  Yair Sapir  Wed Jan 16 22:23:49 CST 2013  DALSKA, DALMAAL, DALECARLIAN  Indo-European, Germanic, North, East Scandinavian, Danish-Swedish, Swedish.
dlm  Dalmatian  Viklasun  dlm  Croatia  7  3571  24786  DLM  -  -  -  en  en  no  -  Sun Sep 22 21:22:41 CDT 2013  RAGUSAN, VEGLIOTE  Indo-European, Italic, Romance, Italo-Western, Italo-Dalmatian.
dln  Darlong  -  dln  Bangladesh  0  0  0  DLN  -  -  -  lus bgr cnh tcz ctd cfm vap cnk kno  en  no  -  -  DALONG  Sino-Tibetan, Tibeto-Burman, Kuki-Chin-Naga, Kuki-Chin, Central.
dmn-x-bamana  Bamana languages  -  dmn  Mali  0  0  0  -  -  -  -  emk knk kus man mnk bba dag  en  no  Boukary Konaté  -  -  Niger-Congo, Mande, Western, Central-Southwestern, Central, Manding-Jogo, Manding-Vai, Manding-Mokole, Manding, Manding-East, Northeastern Manding, Bamana.
dng  Dungan  Хуэйзў йүян  dng  Kyrgyzstan  8  2109  12466  DNG  -  -  -  uz uzn tg dar gag-Cyrl ug ude lez ulc gld azj-Cyrl kaa-Cyrl cv  en  no  -  Sun Sep 22 21:32:29 CDT 2013  DZHUNYAN, TUNGAN, HUIZU, ZWN'JAN, KWUIZWU  Sino-Tibetan, Chinese.
dnj  Dan  -  dnj  Côte d’Ivoire  0  0  0  DAF  -  -  -  moa  en  no  -  -  YACOUBA, YAKUBA, DA, GIO, GIO-DAN  Niger-Congo, Mande, Eastern, Southeastern, Guro-Tura, Tura-Dan-Mano, Tura-Dan.
dnj-x-east  Eastern Dan  -  dnj  Côte d’Ivoire  0  0  0  DAF  -  -  -  dnj-x-west  en  no  -  -  YACOUBA, YAKUBA, DA, GIO, GIO-DAN  Niger-Congo, Mande, Eastern, Southeastern, Guro-Tura, Tura-Dan-Mano, Tura-Dan.
dnj-x-west  Western Dan  -  dnj  Côte d’Ivoire  0  0  0  DAF  -  -  -  dnj-x-east  en  no  -  -  YACOUBA, YAKUBA, DA, GIO, GIO-DAN  Niger-Congo, Mande, Eastern, Southeastern, Guro-Tura, Tura-Dan-Mano, Tura-Dan.
dob  Dobu  -  dob  Papua New Guinea  0  0  0  DOB  -  -  -  mox bdd viv aui pwg sbe mpx bmk meu tbo gri swp fj  en  no  -  -  -  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Nuclear, North Papuan Mainland-D'Entrecasteaux, Dobu-Duau.
doi  Dogri  डोगरी  doi  India  0  0  0  -  -  -  -  mai mr hi ne  en  no  -  -  Dhogaryali, Dogari, Dogri Jammu, Dogri Pahari, Dogri-Kangri, Dongari, Hindi Dogri, Tokkaru  Indo-European, Indo-Iranian, Indo-Aryan, Northern zone, Western Pahari.
dop  Lukpa  -  dop  Benin  3  221233  1076670  DOP  -  -  -  gri ln amu  en  no  -  Fri Jan 25 12:12:27 CST 2013  LOKPA, LOGBA, LEGBA, LUGBA, DOMPAGO  Niger-Congo, Atlantic-Congo, Volta-Congo, North, Gur, Central, Southern, Grusi, Eastern.
drc  Minderico  -  drc  Portugal  6  95169  784296  -  -  -  -  pt gl es oc mwl  en pt  no  Peter Bouda  Wed Feb 20 10:51:44 CST 2013  Mende, Piação do Ninhou  -
drt  Drents  -  drt  Netherlands  1  1214  5694  DRT  -  -  -  nl act nds-NL vls zea nds li fy  en  no  -  Thu Mar 14 10:50:13 CDT 2013  DRENTE  Indo-European, Germanic, West, Low Saxon-Low Franconian, Low Saxon.
dsb  Lower Sorbian  Dolnoserbski  dsb  Germany  27  163390  1150826  WEE  -  dsb  -  hsb szl sr-Latn sl hr  en  yes  Bernhard Baier, Michał Wjelk  Tue Sep 10 10:21:20 CDT 2013  NIEDERSORBISCH, BAS SORABE, WENDISH, LUSATIAN, LOWER LUSATIAN, DOLNOSERBSKI, DELNOSERBSKI  Indo-European, Slavic, West, Sorbian.
dsh  Daasanach  -  dsh  Ethiopia  1  661  3608  DSH  -  -  -  xon bim  en  no  -  Wed Mar 13 22:11:09 CDT 2013  DASENECH, DAASANECH, DATHANAIK, DATHANAIC, DATHANIK, GHELEBA, GELEBA, GELEB, GELEBINYA, GALLAB, GALUBA, GELAB, GELUBBA, DAMA, MARILLE, MERILE, MERILLE, MORILLE, RESHIAT, RUSSIA, 'SHANGILLA'  Afro-Asiatic, Cushitic, East, Western Omo-Tana.
dtp  Central Dusun  Boros Dusun  dtp  Malaysia (Sabah)  92  70869  462041  DTP  -  -  -  bjn srb zsm id ifk su ifb jv-x-bms  en  no  -  Sat Sep 21 10:23:49 CDT 2013  DUSUN, DUSAN, DUSUM, DUSUR, KADAYAN, KEDAYAN, KADASAN, CENTRAL KADAZAN  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Borneo, Northwest, Sabahan, Dusunic, Dusun, Central.
dts  Toro So Dogon  -  dts  Mali  0  0  0  DTS  -  -  -  sbd gjn knk bba  en  no  -  -  -  Niger-Congo, Atlantic-Congo, Volta-Congo, Dogon
dua  Duala  Duala  dua  Cameroon  44  52639  286959  DOU  da  -  -  lol tn bas lia  en  no  -  Sun Jan 13 14:50:15 CST 2013  DOUALA, DIWALA, DWELA, DUALLA, DWALA  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Northwest, A, Duala (A.20).
due  Umiray Dumaget Agta  -  due  Philippines  2  1884  10084  DUE  -  -  -  su  en  no  -  Mon Oct 1 22:32:27 CDT 2012  UMIREY DUMAGAT, UMIRAY AGTA  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Northern Philippine, Northern Luzon, Northern Cordilleran, Dumagat, Southern.
dug  Chiduruma  -  dug  Kenya  2  173195  1186455  DUG  -  -  -  nyf  en  no  -  Fri Jan 25 12:16:34 CST 2013  -  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, E, Nyika (E.40), Mijikenda.
dum  Middle Dutch  Dietsch  dum  Netherlands  9  1648  11336  -  -  -  -  en  en  no  -  Sun Sep 22 21:54:47 CDT 2013  -  -
dun  Dusun Deyah  Dusun Deyah  dun  Indonesia (Kalimantan)  5  514  3687  DUN  -  -  -  id bjn zsm jv-x-bms btz su ifk btx srb bik  en  no  -  Sun Sep 22 22:05:07 CDT 2013  DEAH, DEJAH  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Borneo, Barito, East, Central-South, Central.
dv  Maldivian  ދިވެހި  div  Maldives  644  1674949  15938996  SNM  -  dv  div  -  en  no  -  Wed Jan 30 13:03:17 CST 2013  MALIKH, MAHL, MALKI, DIVEHI, DIVEHLI, DIVEHI BAS  Indo-European, Indo-Iranian, Indo-Aryan, Sinhalese-Maldivian.
dwr  Dawro  -  dwr  Ethiopia  1  126858  1105459  -  -  -  -  wal om  en  no  -  Fri Jan 4 17:22:51 CST 2013  -  Afro-Asiatic, Omotic, North, Gonga-Gimojan, Gimojan, Ometo-Gimira, Ometo, Central.
dws  Dutton World Speedwords  -  dws  -  1  2492  8598  -  -  -  -  nap lij tzm wa pap ff  en  no  -  Thu Dec 6 20:24:54 CST 2012  -  Artificial.
dww  Dawawa  -  dww  Papua New Guinea  0  0  0  DWW  -  -  -  dob pwg aui bmk meu mox viv bdd ksd sbe gri tbo alu fj ha  en  no  -  -  DAWANA  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Nuclear, North Papuan Mainland-D'Entrecasteaux, Kakabai.
dyo  Jola-Fogny  Jóola-Fóoñi  dyo  Senegal  6  245652  1718960  DYO  do  -  dyo  bps bpr ifk bjn ifb rmy  en fr  yes  Outi Sane  Thu Jan 31 08:40:28 CST 2013  DIOLA-FOGNY, DYOLA, JÓOLA, JOLA, YOLA  Niger-Congo, Atlantic-Congo, Atlantic, Northern, Bak, Jola, Jola Proper, Jola Central, Jola-Fogny.
dyu  Jula  Jula  dyu  Burkina Faso  3  227885  1042479  DYU  jl  -  dyu*  bm emk knk kus man mnk bba bwq kcc dag mmn cko  en  yes  -  Tue Sep 10 10:25:24 CDT 2013  DYULA, DYOULA, DIULA, DIOULA, DJULA  Niger-Congo, Mande, Western, Central-Southwestern, Central, Manding-Jogo, Manding-Vai, Manding-Mokole, Manding, Manding-East, Northeastern Manding, Bamana.
dz  Dzongkha  ཇོང་ཁ  dzo  Bhutan  1953  193192  4223489  DZO  -  dz  dzo  bo  en  started  Tshering Cigay Dorji  Wed Jan 30 11:04:41 CST 2013  DRUKKE, DRUKHA, DUKPA, BHUTANESE, JONKHA, BHOTIA OF BHUTAN, BHOTIA OF DUKPA, ZONGKHAR, RDZONGKHA  Sino-Tibetan, Tibeto-Burman, Himalayish, Tibeto-Kanauri, Tibetic, Tibetan, Southern.
ee  Ewe  Eʋegbe  ewe  Ghana  153  480777  2448912  EWE  ew  ee  ewe  hna  en  no  -  Sat Feb 2 18:29:22 CST 2013  EIBE, EBWE, EVE, EFE, EUE, VHE, GBE, KREPI, KREPE, POPO  Niger-Congo, Atlantic-Congo, Volta-Congo, Kwa, Left Bank, Gbe.
efi  Efik  Efịk  efi  Nigeria  465  374658  2173359  EFK  ef  -  ibb  hif ann ig  en  no  -  Sat Feb 2 18:58:54 CST 2013  CALABAR  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Cross River, Delta Cross, Lower Cross, Obolo, Efik.
eja  Jola-Felupe  -  eja  Guinea-Bissau  0  0  0  EJA  -  -  -  dyo csk bpr ifk phi-x-blaan bps kne bkd pov pap kea bjn  en  no  -  -  EDIAMAT, FULUP, FELOUP, FELUP, FELUPE, FLOUP, FLUP  Niger-Congo, Atlantic-Congo, Atlantic, Northern, Bak, Jola, Jola Proper, Jola Central, Her-Ejamat.
ekk  Standard Estonian  Eesti  ekk  Estonia  1576  10319790  80327808  EST  st  et  est  vro fi  en  yes  -  Tue Sep 10 10:26:55 CDT 2013  EESTI  Uralic, Finno-Ugric, Finno-Permic, Finno-Cheremisic, Finno-Mordvinic, Finno-Lappic, Baltic-Finnic.
el  Greek  Ελληνικά  ell  Greece  634  15142713  103437229  GRK  g  el  grk  pnt grc tsd  en  yes  -  Sun Feb 3 01:32:44 CST 2013  ELLINIKA, GREC, GRAECAE, ROMAIC, NEO-HELLENIC  Indo-European, Greek, Attic.
el-Latn  Greek (Latin)  -  ell  Greece  594  1756247  11829606  GRK  -  -  -  lt el-Latn-x-chat  en  no  -  Sun Jan 13 17:05:10 CST 2013  ELLINIKA, GREC, GRAECAE, ROMAIC, NEO-HELLENIC  Indo-European, Greek, Attic.
el-Latn-x-chat  Greek (Latin - chat)  -  ell  Greece  111  285586  1921231  GRK  -  -  -  el-Latn  en  no  -  Sun Jan 13 16:57:09 CST 2013  ELLINIKA, GREC, GRAECAE, ROMAIC, NEO-HELLENIC  Indo-European, Greek, Attic.
el-polyton  Polytonic Greek  -  ell  Greece  1  1982  13034  GRK  -  -  ell_polytonic  grc el rmn-Grek-x-south rmn-Grek-x-north pnt tsd  en  no  -  Mon Dec 9 14:12:08 CST 2013  ELLINIKA, GREC, GRAECAE, ROMAIC, NEO-HELLENIC  Indo-European, Greek, Attic.
emi  Mussau-Emira  -  emi  Papua New Guinea  0  0  0  EMI  -  -  -  lcm tgp stn nak fj sda  en  no  -  -  EMIRA-MUSSAU, MUSAU-EMIRA  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, St. Matthias.
emk  Eastern Maninkakan  -  emk  Guinea  3  11011  138940  MNI  -  -  mni  bm dyu knk mnk  en  no  -  Tue Sep 10 10:26:17 CDT 2013  Eastern Malinke, Kankan Maninka, Mande, Maninka, Southern Maninka  Niger-Congo, Mande, Western, Central-Southwestern, Central, Manding-Jogo, Manding-Vai, Manding-Mokole, Manding, Manding-East, Southeastern Manding.
emk-Nkoo  Eastern Maninkakan  -  emk  Guinea  325  154343  1233279  MNI  -  -  -  -  en fr  no  -  Thu Mar 14 16:13:49 CDT 2013  MANINKA, MANDE, SOUTHERN MANINKA  Niger-Congo, Mande, Western, Central-Southwestern, Central, Manding-Jogo, Manding-Vai, Manding-Mokole, Manding, Manding-East, Southeastern Manding.
eml  Emiliano-Romagnolo  Emiliàn e Rumagnòl  eml  Italy  5  628314  3531032  EML  -  eml  eml  lmo rm fur lld lij it  en  no  Federico L. G. Faroldi  Sun Jan 13 16:52:30 CST 2013  EMILIANO, EMILIAN, SAMMARINESE  Indo-European, Italic, Romance, Italo-Western, Western, Gallo-Iberian, Gallo-Romance, Gallo-Italian.
emp  Northern Emberá  -  emp  Panama  1  352416  2468251  EMP  -  -  -  cto  en  no  -  Mon Dec 31 07:17:32 CST 2012  EMPERA, EBERA BEDEA, ATRATO, DARIEN, DARIENA, PANAMA EMBERA, CHOLO, EERÃ  Choco, Embera, Northern.
en  English  English  eng  USA  7780  29448206  197670416  ENG  -  en  eng  trf sco-ulster sco-x-scotland pcm  hi  yes  Dr. Hans Zarkoff  Sat Feb 2 19:21:09 CST 2013  -  Indo-European, Germanic, West, English.
en-AU  English (Australia)  English (Australia)  eng  Australia  497  1428285  9289308  ENG  -  -  -  trf sco pcm  hi  started  -  Sun Jan 13 18:15:55 CST 2013  -  Indo-European, Germanic, West, English.
en-BW  English (Botswana)  English (Botswana)  eng  Botswana  44246  17534918  108418165  ENG  -  -  -  trf sco pcm tn  hi  started  Thapelo Otlogetswe  Mon Aug 13 19:51:22 CDT 2012  -  Indo-European, Germanic, West, English.
en-CA  English (Canada)  English (Canada)  eng  Canada  1562  3867938  24836318  ENG  -  -  -  trf sco pcm fr-CA  hi  started  -  Sun Jan 13 18:16:10 CST 2013  -  Indo-European, Germanic, West, English.
en-GB  English (Great Britain)  English (Great Britain)  eng  United Kingdom  10984  12392175  79908087  ENG  -  -  -  trf sco pcm fr-CA  hi  yes  -  Wed Jul 17 16:32:31 CDT 2013  -  Indo-European, Germanic, West, English.
en-HK  English (Hong Kong)  English (Hong Kong)  eng  Hong Kong  811  3048679  18765166  ENG  -  -  -  trf sco pcm  hi  started  -  Sun Jan 13 18:15:20 CST 2013  -  Indo-European, Germanic, West, English.
en-IE  English (Ireland)  English (Ireland)  eng  Ireland  5279  11363974  72142394  ENG  -  -  -  trf sco pcm  hi  started  -  Tue Jul 16 08:19:47 CDT 2013  HIBERNO-ENGLISH  Indo-European, Germanic, West, English.
en-IN  English (India)  English (India)  eng  India  1019  2888402  17454840  ENG  -  -  -  trf sco pcm  hi  started  -  Sun Jan 13 21:36:07 CST 2013  -  Indo-European, Germanic, West, English.
en-JM  English (Jamaica)  English (Jamaica)  eng  Jamaica  250  655138  4266441  ENG  -  -  -  trf sco pcm jam  hi  started  -  Sun Jan 13 21:35:49 CST 2013  -  Indo-European, Germanic, West, English.
en-KE  English (Kenya)  English (Kenya)  eng  Kenya  2480  3424292  22704154  ENG  -  -  -  trf sco pcm fr-CA  hi  started  -  Sun Jan 13 21:36:57 CST 2013  -  Indo-European, Germanic, West, English.
en-NG  English (Nigeria)  English (Nigeria)  eng  Nigeria  790  2632208  16944994  ENG  -  -  -  trf sco pcm fr-CA  hi  started  -  Mon Jan 14 21:41:07 CST 2013  -  Indo-European, Germanic, West, English.
en-NZ  English (New Zealand)  English (New Zealand)  eng  New Zealand  592  1797572  11322947  ENG  -  -  -  trf sco pcm fr-CA  hi  started  -  Mon Jan 14 21:40:39 CST 2013  -  Indo-European, Germanic, West, English.
en-PH  English (Philippines)  English (Philippines)  eng  Philippines  106  329812  2100875  ENG  -  -  -  trf sco pcm fr-CA  hi  started  -  Mon Jan 14 21:39:55 CST 2013  -  Indo-European, Germanic, West, English.
en-SG  English (Singapore)  English (Singapore)  eng  Singapore  486  1948000  11129082  ENG  -  -  -  trf sco pcm  hi  started  -  Mon Jan 14 21:40:05 CST 2013  -  Indo-European, Germanic, West, English.
en-Shaw  English (Shavian)  -  eng  United Kingdom  11  79546  364856  ENG  -  -  -  -  en  no  -  Sun Feb 17 14:55:36 CST 2013  -  Indo-European, Germanic, West, English.
en-TT  English (Trinidad and Tobago)  English (Trinidad and Tobago)  eng  Trinidad and Tobago  4257  4985348  32004182  ENG  -  -  -  trf sco pcm fr-CA  hi  started  Solange James  Tue Sep 10 10:28:48 CDT 2013  -  Indo-European, Germanic, West, English.
en-US  English (United States)  English (United States)  eng  USA  1494  5409840  33417083  ENG  -  -  -  trf sco pcm fr-CA  hi  yes  Kevin Scannell  Mon Jan 14 23:15:22 CST 2013  -  Indo-European, Germanic, West, English.
en-ZA  English (South Africa)  English (South Africa)  eng  South Africa  623  833892  5476410  ENG  -  -  -  trf sco pcm fr-CA  hi  yes  Dwayne Bailey  Mon Jan 14 23:15:12 CST 2013  -  Indo-European, Germanic, West, English.
enb  Markweeta  -  enb  Kenya  2  145087  1130515  ENB  -  -  -  spy  en  no  -  Sat Jan 5 10:24:09 CST 2013  ENDO-MARAKWET, MARAKUET, MARKWETA  Nilo-Saharan, Eastern Sudanic, Nilotic, Southern, Kalenjin, Nandi-Markweta, Markweta.
enf  Forest Enets  Онэй базаан  enf  Russian Federation  15  896  6251  ENF  -  -  -  dar ug uzn mo tab tg inh  en  no  -  Sun Sep 22 22:24:49 CDT 2013  -  Uralic, Samoyed, Northern Samoyed, Enets.
enm  Middle English  Englisce  enm  United Kingdom  52  420009  2208014  -  -  -  -  en sco-x-scotland trf yol  en  no  -  Sun Sep 22 22:50:54 CDT 2013  -  -
enq  Enga  -  enq  Papua New Guinea  0  0  0  ENQ  -  -  -  kyc ipi yby knv sw swh kg twu  en  no  -  -  CAGA, TSAGA, TCHAGA  Trans-New Guinea, Main Section, Central and Western, East New Guinea Highlands, West-Central, Enga.
eo  Esperanto  Esperanto  epo  -  986  18579724  118250534  ESP  -  eo  1115  lad ext es cbk mwl oc  en  yes  Jacob Nordfalk  Tue Sep 10 10:27:42 CDT 2013  LA LINGVO INTERNACIA  Artificial.
erg  Sie  -  erg  Vanuatu  1  1815  10110  ERG  -  -  -  id zsm nss  en  no  -  Thu Dec 13 21:18:55 CST 2012  EROMANGA, ERROMANGA, ERRAMANGA  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, South Vanuatu, Erromanga.
es  Spanish  Español  spa  Spain  1272  4485061  28231326  SPN  s  es  spn  ast lad gl an oc ca mwl ext pt  en  yes  -  Sat Feb 2 19:44:17 CST 2013  ESPAÑOL, CASTELLANO, CASTILIAN  Indo-European, Italic, Romance, Italo-Western, Western, Gallo-Iberian, Ibero-Romance, West Iberian, Castilian.
es-AR  Spanish (Argentina)  Español  spa  Argentina  132  304045  1910242  SPN  s  -  -  ast lad gl an oc ca mwl ext pt  en  started  -  Wed Jan 23 17:14:26 CST 2013  ESPAÑOL, CASTELLANO, CASTILIAN  Indo-European, Italic, Romance, Italo-Western, Western, Gallo-Iberian, Ibero-Romance, West Iberian, Castilian.
es-BO  Spanish (Bolivia)  Español  spa  Bolivia  106  140191  876853  SPN  s  -  -  ast lad gl an oc ca mwl ext pt  en  started  -  Wed Jan 23 17:14:35 CST 2013  ESPAÑOL, CASTELLANO, CASTILIAN  Indo-European, Italic, Romance, Italo-Western, Western, Gallo-Iberian, Ibero-Romance, West Iberian, Castilian.
es-CL  Spanish (Chile)  Español  spa  Chile  59  75129  462850  SPN  s  -  -  ast lad gl an oc ca mwl ext pt  en  started  -  Wed Jan 23 17:14:36 CST 2013  ESPAÑOL, CASTELLANO, CASTILIAN  Indo-European, Italic, Romance, Italo-Western, Western, Gallo-Iberian, Ibero-Romance, West Iberian, Castilian.
es-CO  Spanish (Colombia)  Español  spa  Colombia  72  70033  429322  SPN  s  -  -  ast lad gl an oc ca mwl ext pt  en  started  -  Wed Jan 23 17:14:40 CST 2013  ESPAÑOL, CASTELLANO, CASTILIAN  Indo-European, Italic, Romance, Italo-Western, Western, Gallo-Iberian, Ibero-Romance, West Iberian, Castilian.
es-CR  Spanish (Costa Rica)  Español  spa  Costa Rica  131  153446  1009537  SPN  s  -  -  ast lad gl an oc ca mwl ext pt  en  started  -  Wed Jan 23 17:56:32 CST 2013  ESPAÑOL, CASTELLANO, CASTILIAN  Indo-European, Italic, Romance, Italo-Western, Western, Gallo-Iberian, Ibero-Romance, West Iberian, Castilian.
es-CU  Spanish (Cuba)  Español  spa  Cuba  19  22342  146480  SPN  s  -  -  ast lad gl an oc ca mwl ext pt  en  started  -  Wed Jan 23 17:56:35 CST 2013  ESPAÑOL, CASTELLANO, CASTILIAN  Indo-European, Italic, Romance, Italo-Western, Western, Gallo-Iberian, Ibero-Romance, West Iberian, Castilian.
es-EC  Spanish (Ecuador)  Español  spa  Ecuador  61  45207  285207  SPN  s  -  -  ast lad gl an oc ca mwl ext pt  en  started  -  Wed Jan 23 17:56:39 CST 2013  ESPAÑOL, CASTELLANO, CASTILIAN  Indo-European, Italic, Romance, Italo-Western, Western, Gallo-Iberian, Ibero-Romance, West Iberian, Castilian.
es-ES  Spanish (Spain)  Español  spa  Spain  135  513131  3185076  SPN  s  -  -  ast lad gl an oc ca mwl ext pt  en  yes  -  Wed Jan 23 17:05:23 CST 2013  ESPAÑOL, CASTELLANO, CASTILIAN  Indo-European, Italic, Romance, Italo-Western, Western, Gallo-Iberian, Ibero-Romance, West Iberian, Castilian.
es-GT  Spanish (Guatemala)  Español  spa  Guatemala  29  115361  650587  SPN  s  -  -  ast lad gl an oc ca mwl ext pt  en  started  -  Wed Jan 23 17:56:44 CST 2013  ESPAÑOL, CASTELLANO, CASTILIAN  Indo-European, Italic, Romance, Italo-Western, Western, Gallo-Iberian, Ibero-Romance, West Iberian, Castilian.
es-HN  Spanish (Honduras)  Español  spa  Honduras  146  182629  1132972  SPN  s  -  -  ast lad gl an oc ca mwl ext pt  en  started  -  Wed Jan 23 17:56:58 CST 2013  ESPAÑOL, CASTELLANO, CASTILIAN  Indo-European, Italic, Romance, Italo-Western, Western, Gallo-Iberian, Ibero-Romance, West Iberian, Castilian.
es-MX  Spanish (Mexico)  Español  spa  Mexico  1101  2843129  17425563  SPN  s  -  -  ast lad gl an oc ca mwl ext pt  en  started  -  Wed Jan 23 20:16:51 CST 2013  ESPAÑOL, CASTELLANO, CASTILIAN  Indo-European, Italic, Romance, Italo-Western, Western, Gallo-Iberian, Ibero-Romance, West Iberian, Castilian.
es-NI  Spanish (Nicaragua)  Español  spa  Nicaragua  1844  3297262  20745215  SPN  s  -  -  ast lad gl an oc ca mwl ext pt  en  started  -  Wed Jan 23 20:16:09 CST 2013  ESPAÑOL, CASTELLANO, CASTILIAN  Indo-European, Italic, Romance, Italo-Western, Western, Gallo-Iberian, Ibero-Romance, West Iberian, Castilian.
es-PA  Spanish (Panama)  Español  spa  Panama  33  26394  160802  SPN  s  -  -  ast lad gl an oc ca mwl ext pt  en  started  -  Wed Jan 23 18:42:57 CST 2013  ESPAÑOL, CASTELLANO, CASTILIAN  Indo-European, Italic, Romance, Italo-Western, Western, Gallo-Iberian, Ibero-Romance, West Iberian, Castilian.
es-PE  Spanish (Peru)  Español  spa  Peru  1133  3260665  20285860  SPN  s  -  -  ast lad gl an oc ca mwl ext pt  en  started  -  Wed Jan 23 20:16:38 CST 2013  ESPAÑOL, CASTELLANO, CASTILIAN  Indo-European, Italic, Romance, Italo-Western, Western, Gallo-Iberian, Ibero-Romance, West Iberian, Castilian.
es-PR  Spanish (Puerto Rico)  Español  spa  Puerto Rico  842  912031  5845225  SPN  s  -  -  ast lad gl an oc ca mwl ext pt  en  started  -  Wed Jan 23 22:34:51 CST 2013  ESPAÑOL, CASTELLANO, CASTILIAN  Indo-European, Italic, Romance, Italo-Western, Western, Gallo-Iberian, Ibero-Romance, West Iberian, Castilian.
es-PY  Spanish (Paraguay)  Español  spa  Paraguay  968  1189109  7545391  SPN  s  -  -  ast lad gl an oc ca mwl ext pt  en  started  -  Wed Jan 23 22:34:38 CST 2013  ESPAÑOL, CASTELLANO, CASTILIAN  Indo-European, Italic, Romance, Italo-Western, Western, Gallo-Iberian, Ibero-Romance, West Iberian, Castilian.
es-SV  Spanish (El Salvador)  Español  spa  El Salvador  22  25587  182385  SPN  s  -  -  ast lad gl an oc ca mwl ext pt  en  started  -  Thu Jan 24 00:34:03 CST 2013  ESPAÑOL, CASTELLANO, CASTILIAN  Indo-European, Italic, Romance, Italo-Western, Western, Gallo-Iberian, Ibero-Romance, West Iberian, Castilian.
es-UY  Spanish (Uruguay)  Español  spa  Uruguay  681  706152  4906515  SPN  s  -  -  ast lad gl an oc ca mwl ext pt  en  started  -  Wed Jan 23 22:34:54 CST 2013  ESPAÑOL, CASTELLANO, CASTILIAN  Indo-European, Italic, Romance, Italo-Western, Western, Gallo-Iberian, Ibero-Romance, West Iberian, Castilian.
es-VE  Spanish (Venezuela)  Español  spa  Venezuela  197  2804744  17596943  SPN  s  -  -  ast lad gl an oc ca mwl ext pt  en  started  -  Wed Jan 23 22:34:51 CST 2013  ESPAÑOL, CASTELLANO, CASTILIAN  Indo-European, Italic, Romance, Italo-Western, Western, Gallo-Iberian, Ibero-Romance, West Iberian, Castilian.
es-x-cant  Cantabrian  Cántabru  spa  Spain  2  124111  762848  SPN  -  -  -  es ast ext cbk gl oc  en  no  Diegu San Gabriel  Tue Jan 15 08:13:41 CST 2013  ESPAÑOL, CASTELLANO, CASTILIAN  Indo-European, Italic, Romance, Italo-Western, Western, Gallo-Iberian, Ibero-Romance, West Iberian, Castilian.
ese  Ese Ejja  Tiatinagua  ese  Bolivia  3  332389  2259625  ESE  -  -  -  mpx tna  en es  no  -  Wed Sep 18 19:41:22 CDT 2013  ESE EJA, ESE EXA, TIATINAGUA, 'CHAMA', HUARAYO  Tacanan, Tiatinagua.
esi  North Alaskan Inupiatun  -  esi  USA  2  138063  1376458  ESI  -  -  -  kl iu-Latn esk esu  en  no  David Vadiveloo  Mon Dec 31 07:55:35 CST 2012  NORTH ALASKAN INUPIAT, INUPIAT, 'ESKIMO'  Eskimo-Aleut, Eskimo, Inuit.
esk  Northwest Alaska Inupiatun  -  esk  USA  2  11764  111151  ESK  -  -  -  iu-Latn kl om agr  en  no  -  Fri Jan 25 19:36:16 CST 2013  NORTHWEST ALASKA INUPIAT, INUPIATUN, 'ESKIMO'  Eskimo-Aleut, Eskimo, Inuit.
ess-Cyrl  Central Siberian Yupik  Юпик  ess  USA  7  438  3374  ESS  -  -  -  ude gld ru mhr bg gag-Cyrl uz  en  no  -  Sun Sep 22 22:59:14 CDT 2013  ST. LAWRENCE ISLAND 'ESKIMO'  Eskimo-Aleut, Eskimo, Yupik, Siberian.
esu  Central Yupik  Yugtun  esu  USA  13  80292  734863  ESU  -  -  -  kl mt esi iu-Latn  en  no  -  Wed Sep 18 19:42:19 CDT 2013  CENTRAL ALASKAN YUPIK, WEST ALASKA 'ESKIMO'  Eskimo-Aleut, Eskimo, Yupik, Alaskan.
et  Estonian  Eesti  est  Estonia  1812  10736091  83198852  EST  st  et  est  fi fkv se lt  en  yes  -  Sun Feb 3 11:13:14 CST 2013  EESTI  Uralic, Finno-Ugric, Finno-Permic, Finno-Cheremisic, Finno-Mordvinic, Finno-Lappic, Baltic-Finnic.
etr  Edolo  -  etr  Papua New Guinea  0  0  0  ETR  -  -  -  nak knv twu nyd knv-x-ara knv-x-fly luy  en  no  -  -  ETORO, EDOLO ADO, ETOLO  Trans-New Guinea, Main Section, Central and Western, Central and South New Guinea-Kutubuan, Central and South New Guinea, Bosavi.
eu  Basque  Euskara  eus  Spain  977  17728786  146233189  BSQ  -  eu  bsq  nl tet nds-NL  en es  yes  Julen Ruiz Aizpuru, Alberto Fernández  Fri Sep 13 14:31:00 CDT 2013  VASCUENSE, EUSKERA, EUSKARA.  Basque.
eve  Even  Эвэды торэн  eve  Russian Federation  9  66224  532458  EVE  -  -  eve  neg ulc gld ude sah ky bxr khk gag-Cyrl evn uzn tyv  en ru  no  Elena Klyachko  Wed Nov 6 22:29:16 CST 2013  LAMUT, EWEN, EBEN, ORICH, ILQAN  Altaic, Tungus, Northern, Even.
evn  Evenki  Эвэды̄ турэ̄н  evn  China  14  59135  438064  EVN  -  -  evn  lez sah neg gag-Cyrl ky eve bxr  en ru  no  Elena Klyachko  Thu Nov 7 07:08:11 CST 2013  EWENKE, EWENKI, OWENKE, SOLON, SUOLUN, KHAMNIGAN  Altaic, Tungus, Northern, Evenki.
ewo  Ewondo  -  ewo  Cameroon  4  319  1804  EWO  -  -  -  bum  en  no  -  Wed Sep 18 19:48:10 CDT 2013  EWUNDU, JAUNDE, YAOUNDE, YAUNDE  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Northwest, A, Yaunde-Fang (A.70).
ext  Extremaduran  Estremeñu  ext  Spain  2  405397  2492150  EXT  -  ext  -  cbk es ast lad lnc oc ca gsc  en es  no  -  Tue Sep 10 10:31:48 CDT 2013  EXTREMEÑO, EHTREMEÑU, CAHTÚO, CAHTÚÖ  Indo-European, Italic, Romance, Italo-Western, Western, Gallo-Iberian, Ibero-Romance, West Iberian, Castilian.
fa  Persian  فارسی  fas  Iran  1007  1834223  11083198  -  pr  fa  -  bal mzn lki glk azb-Arab ur ckb  en  yes  -  Fri Sep 13 14:13:42 CDT 2013  WESTERN FARSI, PARSI, FARSI  Indo-European, Indo-Iranian, Iranian, Western, Southwestern, Persian.
fa-Latn  Persian (Latin)  -  fas  Iran  0  0  0  -  -  -  -  bvz uz-Latn hns ur-Latn bn-Latn  en  no  -  -  PERSIAN, PARSI  Indo-European, Indo-Iranian, Iranian, Western, Southwestern, Persian.
faa  Fasu  -  faa  Papua New Guinea  0  0  0  FAA  -  -  -  ipi mnb alu teo ain  en  no  -  -  NAMOME  Trans-New Guinea, Main Section, Central and Western, Central and South New Guinea-Kutubuan, Kutubuan, West.
fai  Faiwol  -  fai  Papua New Guinea  276  322802  1776528  FAI  -  -  -  bhl bjn ha kha  en  no  -  Fri Dec 28 20:40:16 CST 2012  FAIWOLMIN, FEGOLMIN, UNKIA, KAUWOL, KAWOL, KAVWOL  Trans-New Guinea, Main Section, Central and Western, Central and South New Guinea-Kutubuan, Central and South New Guinea, Ok, Mountain.
fal  South Fali  -  fal  Cameroon  5  236819  1092740  FAL  -  -  -  due yap  en  no  -  Fri Jan 25 12:22:33 CST 2013  -  Niger-Congo, Atlantic-Congo, Volta-Congo, North, Adamawa-Ubangi, Adamawa, Fali.
fat  Fanti  -  fat  Ghana  2  5473  27806  TWS  -  -  tws3  tw  en  no  -  Tue Jan 15 09:16:53 CST 2013  -  Niger-Congo, Atlantic-Congo, Volta-Congo, Kwa, Nyo, Potou-Tano, Tano, Central, Akan.
fax  Fala  Fala  fax  Spain  6  1370  8255  FAX  -  -  -  ext gsc gl oc prv pt lnc es mwl ca ast sc  en  no  -  Sun Sep 22 23:14:15 CDT 2013  A FALA DE XÁLIMA, A FALA DO XÃLIMA, GALAICO-EXTREMADURAN, 'CHAPURREÁU'  Indo-European, Italic, Romance, Italo-Western, Western, Gallo-Iberian, Ibero-Romance, West Iberian, Portuguese-Galician.
ff  Fulah  Pulaar  ful  Cameroon  1773  2164545  13765092  -  fd  ff  -  rmy nap yap to lij rom luo djk gl  en fr rmy nap  yes  -  Mon Dec 2 12:11:19 CST 2013  ADAMAWA FULANI, PEUL, PEULH, FUL, FULA, FULBE, BOULBE, EASTERN FULANI, FULFULDE, FOULFOULDE, PULLO, GAPELTA, PELTA HAY, DOMONA, PLADINA, PALATA, PALDIDA, PALDENA, DZEMAY, ZEMAY, ZAAKOSA, PULE, TAAREYO, SANYO, BIIRA  Niger-Congo, Atlantic-Congo, Atlantic, Northern, Senegambian, Fula-Wolof, Fulani, Eastern.
fi  Finnish  Suomi  fin  Finland  1535  3910922  31728349  FIN  fi  fi  fin  fkv ekk vro  en  yes  -  Sun Feb 3 11:03:14 CST 2013  SUOMI, SUOMEA  Uralic, Finno-Ugric, Finno-Permic, Finno-Cheremisic, Finno-Mordvinic, Finno-Lappic, Baltic-Finnic, Finnic.
fil  Filipino  Filipino  fil  Philippines  30  9327  62174  -  -  -  -  tl pam hil kyk agn jv cps krj msk jvn ban bik bbc-Latn ceb su  en  no  -  Sun Sep 22 23:12:19 CDT 2013  -  -
fit  Tornedalen Finnish  meänkieli  fit  Sweden  100  30212  228831  FIT  -  -  -  fi fkv ekk vro se ubr smj shp kaq  en  no  -  Mon Sep 23 11:15:40 CDT 2013  TORNEDALEN (MEÄNKIELI, TORNE VALLEY FINNISH, TORNEDALSFINSKA, NORTH FINNISH)  Uralic, Finno-Ugric, Finno-Permic, Finno-Cheremisic, Finno-Mordvinic, Finno-Lappic, Balto-Finnic, Finnic.
fiz  Izere  -  fiz  Nigeria  0  0  0  FIZ  -  -  -  pam dga jv lnu  en  no  -  -  IZAREK, FIZERE, FEZERE, FESEREK, AFIZAREK, AFIZARE, AFUSARE, JARI, JARAWA, JARAWAN DUTSE, HILL JARAWA, JOS-ZARAZON  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Platoid, Plateau, Central, South-Central.
fj  Fijian  vakaViti  fij  Fiji  264  1019906  5274969  FJI  fn  fj  fji  gri pwg  en  yes  Gabe Lalasava  Fri Sep 13 08:35:19 CDT 2013  FIJI, STANDARD FIJIAN, EASTERN FIJIAN, NADROGA, NADRONGA  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Central Pacific, East Fijian-Polynesian, East Fijian.
fkv  Kven Finnish  Kväänin kieli  fkv  Norway  56  52072  428325  FKV  -  -  -  fi ekk et vro se  en nb  no  Mervi Haavisto  Tue Nov 26 12:28:38 CST 2013  KVEN, NORTH FINNISH  Uralic, Finno-Ugric, Finno-Permic, Finno-Cheremisic, Finno-Mordvinic, Finno-Lappic, Balto-Finnic, Finnic.
fo  Faroese  Føroyskt  fao  Faroe Islands  1897  2306099  15084508  FAE  fr  fo  fae  is nn  en  yes  Jacob Sparre Andersen  Fri Sep 13 10:25:04 CDT 2013  FØROYSKT  Indo-European, Germanic, North, West Scandinavian.
fon  Fon  Fɔngbè  fon  Benin  6  73999  325438  FOA  fo  -  foa  hna bwq nfr  en fr  no  -  Tue Jan 15 00:07:20 CST 2013  FO, FON-GBE, FONNU, FOGBE, DAHOMEEN, DJEDJI  Niger-Congo, Atlantic-Congo, Volta-Congo, Kwa, Left Bank, Gbe, Fon.
for  Fore  -  for  Papua New Guinea  0  0  0  FOR  -  -  -  dww bmk pwg alu aui  en  no  -  -  -  Trans-New Guinea, Main Section, Central and Western, East New Guinea Highlands, East-Central, Fore.
fr  French  Français  fra  France  1000  4063127  25261950  FRN  f  fr  frn  fr-x-jer fr-x-nor oc ca ast es  en  yes  -  Sun Feb 3 10:40:31 CST 2013  FRANÇAIS  Indo-European, Italic, Romance, Italo-Western, Western, Gallo-Iberian, Gallo-Romance, Gallo-Rhaetian, Oïl, French.
fr-CA  French (Canada)  Français  fra  Canada  1556  3474873  23000900  FRN  f  -  -  es oc wa  en  yes  -  Wed Jan 16 23:55:41 CST 2013  FRANÇAIS  Indo-European, Italic, Romance, Italo-Western, Western, Gallo-Iberian, Gallo-Romance, Gallo-Rhaetian, Oïl, French.
fr-FR  French (France)  Français  fra  France  516  2676145  17348154  FRN  f  -  -  fr-x-jer fr-x-nor ca oc ia ast pcd es  en  yes  -  Wed Jan 16 23:55:04 CST 2013  FRANÇAIS  Indo-European, Italic, Romance, Italo-Western, Western, Gallo-Iberian, Gallo-Romance, Gallo-Rhaetian, Oïl, French.
fr-x-jer  Jèrriais  Jèrriais  fra  France  684  483568  3058420  FRA  -  -  -  fr  en fr  yes  Tony Scott Warren  Thu Jan 17 11:34:30 CST 2013  FRANÇAIS  Indo-European, Italic, Romance, Italo-Western, Western, Gallo-Iberian, Gallo-Romance, Gallo-Rhaetian, Oïl, French
fr-x-nor  Norman  -  fra  France  2  262696  1630959  FRN  -  nrm  -  pcd fr fr-x-jer wa frp  en  no  -  Thu Jan 10 22:22:23 CST 2013  FRANÇAIS  Indo-European, Italic, Romance, Italo-Western, Western, Gallo-Iberian, Gallo-Romance, Gallo-Rhaetian, Oïl, French.
frp  Arpitan  Arpitan  frp  France  2  69030  418535  FRA  -  frp  -  lnc lad gsc lms prv an es  en fr  no  -  Sun Mar 31 08:19:44 CDT 2013  PATOIS, FRANCO-PROVENÇAL  Indo-European, Italic, Romance, Italo-Western, Western, Gallo-Iberian, Gallo-Romance, Gallo-Rhaetian, Oïl, Southeastern.
frr  Northern Frisian  -  frr  Germany  362  395418  2439442  FRR  -  frr  -  nl fy lb nds-NL nds de  en  no  Mark Williamson  Thu Jan 17 10:36:52 CST 2013  NORDFRIESISCH  Indo-European, Germanic, West, Frisian.
frr-x-fer  Northern Frisian (Öömrang)  -  frr  Germany  2  3439  19111  FRR  -  -  -  lb ga-Latg nl nds-NL frr-x-moo  en nl de  no  Mark Williamson  Thu Jan 17 08:30:16 CST 2013  NORDFRIESISCH  Indo-European, Germanic, West, Frisian.
frr-x-moo  Northern Frisian (Frasch)  -  frr  Germany  11  24804  148874  FRR  -  -  -  de lb nds pdc nl frr-x-fer gsw  en nl de  no  Mark Williamson  Thu Jan 17 08:34:37 CST 2013  NORDFRIESISCH  Indo-European, Germanic, West, Frisian.
fuc  Pulaar  -  fuc  Senegal  1  1690  10432  FUC  -  -  fum1  fuf fuv rmy son aa lmo  en  no  -  Mon Dec 9 14:15:11 CST 2013  PULAAR FULFULDE, PEUL, PEULH  Niger-Congo, Atlantic-Congo, Atlantic, Northern, Senegambian, Fula-Wolof, Fulani, Western.
fud  East Futuna  Fakafutuna  fud  Wallis and Futuna  3  29355  143999  FUD  ft  -  -  sm tvl wls tkl to niu  en  no  -  Mon Dec 9 14:12:19 CST 2013  FUTUNIAN  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Central Pacific, East Fijian-Polynesian, Polynesian, Nuclear, Samoic-Outlier, Futunic.
fuf  Pular  Pulaar  fuf  Guinea  1  2894  16996  FUF  pl  -  -  fuv nap to rom yap  en fr  no  Oumar Bah  Thu Jan 31 08:10:47 CST 2013  FUTA JALLON, FOUTA DYALON, FULBE, FULLO FUUTA, FUTA FULA, FOULA FOUTA, FULFULDE JALON, JALON, PULAR, PULAAR  Niger-Congo, Atlantic-Congo, Atlantic, Northern, Senegambian, Fula-Wolof, Fulani, West Central.
fur  Friulian  Furlan  fur  Italy  4192  10721439  61784833  FRL  -  fur  frl  it lmo lld co  en it  yes  Andrea Tami  Tue Sep 10 10:35:51 CDT 2013  FURLAN, FRIOULAN, FRIOULIAN, PRIULIAN, FRIULANO  Indo-European, Italic, Romance, Italo-Western, Western, Gallo-Iberian, Gallo-Romance, Gallo-Rhaetian, Rhaetian.
fuv  Nigerian Fulfulde  -  fuv  Nigeria  1  159151  951510  FUV  -  -  -  fuf son yap wo  en  no  -  Sat Jan 5 12:33:07 CST 2013  KANO-KATSINA-BORORRO FULFULDE  Niger-Congo, Atlantic-Congo, Atlantic, Northern, Senegambian, Fula-Wolof, Fulani, East Central.
fy  Frisian  Frysk  fry  Netherlands  388  7719213  48397332  FRI  -  fy  fri  nds-NL vls nl zea li nds  en nl  yes  Eeltje de Vries, Wim Benes  Fri Sep 13 11:57:50 CDT 2013  FRYSK, FRIES, WEST FRISIAN  Indo-European, Germanic, West, Frisian.
ga  Irish  Gaeilge  gle  Ireland  142008  98075797  1085651160  GLI  gc  ga  gli1  gd ga-Latg en  en  yes  Kevin Scannell  Thu Mar 22 20:25:22 CDT 2007  IRISH, ERSE, GAEILGE  Indo-European, Celtic, Insular, Goidelic.
ga-Latg  Irish (Uncial)  Gaeilge (Seanchló)  gle  Ireland  0  0  0  GLI  -  -  -  ga ga-x-slais gd  en  no  -  -  IRISH, ERSE, GAEILGE  Indo-European, Celtic, Insular, Goidelic.
ga-x-slais  Irish (slashes)  Gaeilge (slaiseanna)  gle  Ireland  2  148905  871598  GLI  -  -  -  ga gd ga-Latg  en  started  -  Thu Jan 17 08:42:25 CST 2013  IRISH, ERSE, GAEILGE  Indo-European, Celtic, Insular, Goidelic.
gaa  Ga  Ga  gaa  Ghana  121  138230  722375  GAC  ga  -  gac2  lef dag vmw maw  en  no  -  Sun Feb 3 10:32:01 CST 2013  AMINA, GAIN, ACCRA, ACRA  Niger-Congo, Atlantic-Congo, Volta-Congo, Kwa, Nyo, Ga-Dangme.
gag  Gagauz  -  gag  Moldova  4  227406  1669011  GAG  -  gag  gag  tr crh tk azj  en tr  no  -  Fri Jan 25 13:06:26 CST 2013  GAGAUZI  Altaic, Turkic, Southern, Turkish.
gag-Cyrl  Gagauz (Cyrillic)  -  gag  Moldova  1  122599  868687  GAG  -  -  -  kaa-Cyrl ky kum uzn azj-Cyrl sah alt  en  no  -  Mon Dec 9 14:10:15 CST 2013  GAGAUZI  Altaic, Turkic, Southern, Turkish.
gah  Alekano  -  gah  Papua New Guinea  0  0  0  GAH  -  -  -  aso yby ipi mmx  en  no  -  -  GAHUKU, GAFUKU, GAHUKU-GAMA  Trans-New Guinea, Main Section, Central and Western, East New Guinea Highlands, East-Central, Gahuku-Benabena.
gam  Kandawo  -  gam  Papua New Guinea  0  0  0  GAM  -  -  -  kue loa kcc sbe dyu bm kus hz stn  en  no  -  -  NARAKE  Trans-New Guinea, Main Section, Central and Western, East New Guinea Highlands, Central, Jimi.
gan  Gan Chinese  贛語  gan  China  389  180191  2252390  KNN  -  gan  -  cmn ja  en  no  -  Thu Jan 17 14:32:19 CST 2013  GAN, KAN  Sino-Tibetan, Chinese.
gaw  Nobonob  -  gaw  Papua New Guinea  0  0  0  GAW  -  -  -  bmh amn aey ha  en  no  -  -  BUTELKUD-GUNTABAK, GARUH, NOBONOB, NOBNOB  Trans-New Guinea, Madang-Adelbert Range, Madang, Mabuso, Hanseman.
gay  Gayo  Basa Gayo  gay  Indonesia (Sumatra)  3  405  2562  GYO  -  -  -  kqw jv-x-bms btx su id btd zsm ljp bjn jv  en  no  -  Sun Sep 22 23:25:31 CDT 2013  GAJO  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Sundic, Gayo.
gba  Gbaya  Gbaya  gba  Central African Republic  1  9224  41497  -  gba  -  -  bum  en fr  no  -  Sat Jan 26 19:24:10 CST 2013  GBAYA NORD-OUEST, GBAYA  Niger-Congo, Atlantic-Congo, Volta-Congo, North, Adamawa-Ubangi, Ubangi, Gbaya-Manza-Ngbaka, Northwest.
gbi  Galela  -  gbi  Indonesia (Maluku)  4  288024  1644279  GBI  -  -  -  loa  en  no  -  Sat Jan 5 12:46:37 CST 2013  -  West Papuan, North Halmahera, North, Galela-Loloda.
gbm  Garhwali  -  gbm  India  10  1731  10678  GBM  -  -  -  ne mr npi mai hi hne bh sa new mag  en  no  -  Fri Nov 15 21:06:22 CST 2013  GADHAVALI, GADHAWALA, GADWAHI, GASHWALI, GODAULI, GORWALI, GURVALI, PAHARI GARHWALI, GIRWALI  Indo-European, Indo-Iranian, Indo-Aryan, Northern zone, Garhwali.
gbo  Northern Grebo  -  gbo  Liberia  2  272307  1143759  GRB  -  -  -  moa  en  no  -  Sun Dec 30 16:00:31 CST 2012  -  Niger-Congo, Atlantic-Congo, Volta-Congo, Kru, Western, Grebo, Liberian.
gcf  Guadeloupean Creole French  Kréyòl Gwadloupéyen  gcf  Guadeloupe  9  1597  9687  GCF  -  -  -  acf crs ht ubr mfe ifk srb bik ga-Latg rcf  en  no  -  Sun Sep 22 23:34:34 CDT 2013  -  -
gd  Scottish Gaelic  Gàidhlig  gla  Scotland  14749  17523805  109527798  GLS  gcs  gd  gls  ga  en fr es  yes  Caoimhín Ó Donnaíle, Michael Bauer  Thu Jan 2 21:23:10 CST 2014  GÀIDHLIG, GAELIC  Indo-European, Celtic, Insular, Goidelic.
gde  Gude  -  gde  Nigeria  1  217017  1201738  GDE  -  -  -  son  en  no  -  Sat Jan 5 12:37:30 CST 2013  GOUDE, CHEKE, TCHADE, SHEDE, MAPODI, MAPUDA, MUDAYE, MOCIGIN, MOTCHEKIN  Afro-Asiatic, Chadic, Biu-Mandara, A, A.8.
gdn  Umanakaina  -  gdn  Papua New Guinea  0  0  0  GDN  -  -  -  pwg bmk stn aui sbe for kwf fj ha alu  en  no  -  -  GWEDENA, GWEDA, GWEDE, GVEDE, UMANIKAINA  Trans-New Guinea, Main Section, Eastern, Central and Southeastern, Dagan.
gdr  Wipi  -  gdr  Papua New Guinea  0  0  0  GDR  -  -  -  pwg dob gbi bmk tby fj ha dww stn  en  no  -  -  ORIOMO, JIBU, WIPI  Trans-New Guinea, Trans-Fly-Bulaka River, Trans-Fly, Eastern Trans-Fly.
gfk  Patpatar  -  gfk  Papua New Guinea  0  0  0  GFK  -  -  -  ksd stn kto hla lcm bnp gri su fj  en  no  -  -  GELIK, PATPARI  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, South New Ireland-Northwest Solomonic, Patpatar-Tolai.
ghs  Guhu-Samane  -  ghs  Papua New Guinea  263  490954  3038486  GHS  -  -  -  aia  en  no  -  Fri Dec 28 20:43:20 CST 2012  PAIAWA, TAHARI, MURI, BIA, MID-WARIA  Trans-New Guinea, Main Section, Eastern, Binanderean, Guhu-Samane.
gil  Kiribati  Kiribati  gil  Kiribati  6  276057  1381766  GLB  gb  -  -  mi rar tkl stn hla ty bnp tvl fj kwf  en  no  -  Wed Sep 18 19:51:21 CDT 2013  GILBERTESE, IKIRIBATI  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Micronesian, Micronesian Proper, Ikiribati.
git  Gitxsan  -  git  Canada  0  0  0  GIT  -  -  -  bcr jam  en  no  -  -  GITKSAN, GITYSKYAN, GIKLSAN  Penutian, Tsimshian.
gjn  Gonja  -  gjn  Ghana  2  3900  18550  DUM  -  -  dum  hna ada ntr  en  no  -  Fri Sep 13 11:15:45 CDT 2013  NGBANYITO  Niger-Congo, Atlantic-Congo, Volta-Congo, Kwa, Nyo, Potou-Tano, Tano, Guang, North Guang.
gkn  Gokana  Gòkánà  gkn  Nigeria  2  266973  1059889  GKN  gn  -  -  nap fuf ff srn  en  no  -  Fri Jan 25 15:02:37 CST 2013  -  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Cross River, Delta Cross, Ogoni, East.
gkp  Guinea Kpelle  -  gkp  Guinea  1  1621  8043  GKP  -  -  gkp1  sbd maw om  en  no  -  Sun Feb 17 15:23:04 CST 2013  KPELE, GUERZE, GERZE, GERSE, GBESE, PESSA, PESSY, KPWESSI, AKPESE, KPELESE, KPELESETINA, KPESE, KPERESE, NORTHERN KPELE  Niger-Congo, Mande, Western, Central-Southwestern, Southwestern, Kpelle.
gl  Galician  Galego  glg  Spain  4775  29891922  182705435  GLN  -  gl  gln  pt es an ast oc lnc mwl  en es  yes  -  Fri Sep 13 14:18:10 CDT 2013  GALEGO, GALLEGO  Indo-European, Italic, Romance, Italo-Western, Western, Gallo-Iberian, Ibero-Romance, West Iberian, Portuguese-Galician.
gld  Nanai  нани  gld  Russian Federation  0  0  0  GLD  -  -  gld*  ulc ude  en  no  -  -  NANAJ, GOLD, GOLDI, HEZHEN, HEZHE, HECHE  Altaic, Tungus, Southern, Southeast, Nanaj.
glk  Gilaki  گیﻝکی  glk  Iran  5  439755  2326848  GLK  -  glk  -  pes bal lki prs mzn azb-Arab  en  no  -  Tue Sep 10 13:43:13 CDT 2013  GELAKI, GILANI, GUILAKI, GUILANI  Indo-European, Indo-Iranian, Iranian, Western, Northwestern, Caspian.
gmo  Gamo-Gofa-Dawro  -  gmo  Ethiopia  3  373183  2965918  -  -  -  -  wal om  en  no  -  Wed Dec 11 11:34:43 CST 2013  -  Afro-Asiatic, Omotic, North, Gonga-Gimojan, Gimojan, Ometo-Gimira, Ometo, Central.
gmv  Gamo  -  gmv  Ethiopia  1  127322  936306  -  -  -  -  wal dwr ha so  en  no  -  Sat Jan 5 12:54:11 CST 2013  -  Afro-Asiatic, Omotic, North, Gonga-Gimojan, Gimojan, Ometo-Gimira, Ometo, Central.
gn  Guarani  Avañe'ẽ  grn  Paraguay  149  603315  4479278  -  gi  gn  gun  kgk tqo gyr  en es  started  Luis Cardozo, Iván Prieto Corvalán  Fri Sep 13 08:28:49 CDT 2013  AVAÑE'E  Tupi, Tupi-Guarani, Guarani (I).
gnd  Zulgo-Gemzek  -  gnd  Cameroon  1  362294  1645553  GND  -  -  -  maf  en  no  -  Sat Jan 5 12:55:40 CST 2013  GEMJEK, GUEMSHEK  Afro-Asiatic, Chadic, Biu-Mandara, A, A.5.
gng  Ngangam  -  gng  Togo  0  0  0  GNG  -  -  -  bim xon-x-liko xon-x-likp gux bud sbd tpm  en  no  -  -  DYE, GANGAM, GANGUM, NGANGAN, NBANGAM, MIGANGAM, MIJIEM  Niger-Congo, Atlantic-Congo, Volta-Congo, North, Gur, Central, Northern, Oti-Volta, Gurma.
gnw  Western Bolivian Guaraní  -  gnw  Bolivia  1  219713  1335010  GNW  -  -  -  gui gyr  en es  no  -  Mon Dec 31 15:48:11 CST 2012  SIMBA, SIMBA GUARANÍ  Tupi, Tupi-Guarani, Guarani (I).
gof  Gofa  -  gof  Ethiopia  1  119003  924153  -  -  -  -  gmv dwr wal om  en  no  -  Sat Jan 5 13:02:31 CST 2013  -  Afro-Asiatic, Omotic, North, Gonga-Gimojan, Gimojan, Ometo-Gimira, Ometo, Central.
gog  Gogo  -  gog  Tanzania  2  175162  1151848  GOG  -  -  -  wmw sw  en  no  -  Sat Jan 5 13:27:51 CST 2013  CHIGOGO  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, G, Gogo (G.10).
goh  Old High German  Althochdeutsch  goh  Germany  8  15542  95233  -  -  -  -  sco en trf de  en  no  -  Wed Sep 18 19:52:27 CDT 2013  DEUTSCH, HOCHDEUTSCH, HIGH GERMAN  Indo-European, Germanic, West, High German, German, Middle German, East Middle German.
gom  Goan Konkani  Konkani (Amchi Bhas)  gom  India  4  2231  16337  GOM  -  -  -  bn-Latn pes-Latn  en  no  -  Wed Sep 18 19:56:27 CDT 2013  GOMATAKI, GOAN  Indo-European, Indo-Iranian, Indo-Aryan, Southern zone, Konkani.
gor  Gorontalo  Bahasa Hulonthalo  gor  Indonesia (Sulawesi)  77  287745  1927787  GRL  -  -  -  luo men kj  en  no  -  Sat Jan 5 13:24:37 CST 2013  HULONTALO  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Sulawesi, Mongondow-Gorontalo, Gorontalic.
gos  Gronings  -  gos  Netherlands  1  806  4319  GOS  -  -  -  nds-NL nl act li zea vls fy drt nds af de  en  no  -  Thu Mar 14 11:43:27 CDT 2013  GRONINGEN, GRUNNINGS  Indo-European, Germanic, West, Low Saxon-Low Franconian, Low Saxon.
got  Gothic  Gutisk  got  Ukraine  36  457699  2928670  GOF  -  got  -  cbs toj  en  no  -  Thu Jan 17 09:04:27 CST 2013  -  Indo-European, Germanic, East.
grb  Grebo  -  grb  Liberia  0  0  0  -  -  -  -  moa  en  no  -  -  -  Niger-Congo, Atlantic-Congo, Volta-Congo, Kru, Western, Grebo, Liberian.
grc  Ancient Greek  Ἑλληνική ἀρχαία  grc  Greece  28  351213  2153953  GKO  -  -  -  el pnt  en  yes  -  Wed Sep 18 20:01:42 CDT 2013  -  Indo-European, Greek, Attic.
gri  Ghari  -  gri  Solomon Islands  4  26294  141873  GRI  -  -  -  fj bgt stn pwg aia meu amu  en  no  -  Thu Jan 17 09:02:57 CST 2013  GARI, TANGARARE, SUGHU, WEST GUADALCANAL  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Southeast Solomonic, Gela-Guadalcanal, Guadalcanal.
grt  Garo  -  grt  India  20  32395  258493  GRT  -  -  -  bbc-Latn bts agn hil jv  en  no  -  Mon Dec 31 11:44:03 CST 2012  GARROW, MANDE  Sino-Tibetan, Tibeto-Burman, Jingpho-Konyak-Bodo, Konyak-Bodo-Garo, Bodo-Garo, Garo.
gsc  Gascon  -  gsc  France  35  136358  787311  GSC  -  -  -  lnc lms prv es mwl an ast  en fr  yes  Bruno Gallart, Damien Mooney  Tue Sep 10 13:43:51 CDT 2013  OCCITAN  Indo-European, Italic, Romance, Italo-Western, Western, Gallo-Iberian, Ibero-Romance, Oc.
gsw  Swiss German  Schwiizerdütsch  gsw  Switzerland  173  3220781  20384089  GSW  -  als  -  de pdc pfl ksh vmf bar lb nds li  en de  no  Francesca Frontini  Thu Jan 17 09:46:01 CST 2013  SCHWYZERDÜTSCH  Indo-European, Germanic, West, High German, German, Upper German, Alemannic.
gu  Gujarati  ગુજરાતી  guj  India  3302  8108245  56539455  GJR  gu*  gu  gjr  -  en  yes  -  Sun Feb 3 11:07:04 CST 2013  GUJRATHI, GUJERATI, GUJERATHI  Indo-European, Indo-Iranian, Indo-Aryan, Central zone, Gujarati.
gub  Guajajára  -  gub  Brazil  3  1101129  6219934  GUB  -  -  -  gn gyr  en  no  -  Mon Dec 31 16:21:07 CST 2012  GUAZAZARA, TENETEHAR, TENETEHÁRA  Tupi, Tupi-Guarani, Tenetehara (IV).
guc  Wayuu  Wayuunaiki  guc  Colombia  253  353362  2776939  GUC  wy  -  guc  swh mhl lag om pbb rai wmw  en es  no  Ornela Quintero  Wed Sep 18 20:02:21 CDT 2013  GUAJIRO, GOAJIRO, GUAJIRA, WAYUNAIKI  Arawakan, Maipuran, Northern Maipuran, Caribbean.
guh  Guahibo  -  guh  Colombia  2  344209  3093555  GUH  -  -  -  cui pwg  en  no  -  Thu Dec 27 14:28:27 CST 2012  GUAJIBO, GOAHIBO, GUAIGUA, GUAYBA, WAHIBO, GOAHIVA, 'SICUANI'  Guahiban.
gui  Eastern Bolivian Guaraní  -  gui  Bolivia  6  239996  1456818  GUI  gib  -  -  gnw  en es  no  -  Thu Dec 27 14:31:45 CST 2012  'CHIRIGUANO'  Tupi, Tupi-Guarani, Guarani (I).
gul  Sea Island Creole English  -  gul  USA  2  564461  2700709  GUL  -  -  -  pcm hwc jam  en  no  -  Thu Dec 27 16:24:27 CST 2012  GULLAH, GEECHEE  Creole, English based, Atlantic, Eastern, Northern.
gum  Guambiano  -  gum  Colombia  3  336810  2466039  GUM  -  -  -  ifu mxt blw bnc ctp mbz ivv cya  en es  no  -  Thu Dec 27 16:48:49 CST 2012  GUAMBIA, MOGUEX  Barbacoan, Coconucan.
gun  Mbyá Guaraní  -  gun  Paraguay  1  177894  1041662  GUN  -  -  -  gub gnw gui  en  no  -  Sat Jan 5 13:46:18 CST 2013  MBYÁ, MBUA  Tupi, Tupi-Guarani, Guarani (I).
guo  Guayabero  -  guo  Colombia  2  280063  2218505  GUO  -  -  -  ifu tzt ay stp cbs bjn cui  en es  no  -  Thu Dec 27 16:26:18 CST 2012  JIW, CUNIMÍA, MÍTUS, MÍTIA  Guahiban.
gup  Gunwinggu  Kunwinjku  gup  Australia  2  3138  24738  GUP  -  -  -  ibd pam sua wbp wmt su alz izr mmn hnn bhl jv  en  no  Murray Garde  Tue Jan 22 10:38:04 CST 2013  GUNAWITJI, MAYALI, KUNWINJKU  Australian, Gunwingguan, Gunwinggic.
gur  Farefare  -  gur  Ghana  7  889869  4241064  GUR  -  -  -  kus emk mos  en fr  no  -  Wed Sep 18 20:07:11 CDT 2013  FAREFARE, GURENNE, GURUNE, NANKANI  Niger-Congo, Atlantic-Congo, Volta-Congo, North, Gur, Central, Northern, Oti-Volta, Western, Northwest.
gur-x-nink  Ninkare  -  gur  Ghana  1  211875  1009511  GUR  -  -  -  gur mos emk kus  en  no  -  Tue Feb 19 15:54:23 CST 2013  FAREFARE, GURENNE, GURUNE, NANKANI  Niger-Congo, Atlantic-Congo, Volta-Congo, North, Gur, Central, Northern, Oti-Volta, Western, Northwest.
guu  Yanomamö  -  guu  Venezuela  1  2175  12353  GUU  -  -  guu  sco-ulster trf en goh  en  no  -  Mon Dec 9 14:14:28 CST 2013  YANOMAME, YANOMAMI, GUAICA, GUAHARIBO, GUAJARIBO  Yanomam.
guw  Gun-Gbe  Gungbe  guw  Benin  61  134224  768010  GUW  eg  -  -  bg-Latn  en  no  -  Sun Feb 3 12:09:29 CST 2013  ALADA, ALADA-GBE, GUN-ALADA, GUN, GOUN, EGUN, GU, GUGBE  Niger-Congo, Atlantic-Congo, Volta-Congo, Kwa, Left Bank, Gbe, Aja.
gux  Gourmanchéma  -  gux  Burkina Faso  1  214740  1018768  GUX  -  -  -  hag dag bim  en  no  -  Sat Jan 5 14:11:07 CST 2013  GOURMA, GOURMANTCHE, GURMA, MIGULIMANCEMA, GOULMACEMA, GULMANCEMA, GULIMANCEMA  Niger-Congo, Atlantic-Congo, Volta-Congo, North, Gur, Central, Northern, Oti-Volta, Gurma.
guz  Ekegusii  -  guz  Kenya  271  305053  2071450  GUZ  -  -  -  ki mer ln meu gri sw  en  no  Troy Speier  Sun Jul 7 09:15:53 CDT 2013  KISII, KOSOVA, GUZII, GUSII  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, E, Kuria (E.10).
gv  Manx Gaelic  Gaelg  glv  Isle of Man  386  1833439  10969093  MJD  -  gv  -  cy  en  yes  Phil Kelly  Tue Jul 31 18:39:18 CDT 2012  GAELG, GAILCK, MANX GAELIC  Indo-European, Celtic, Insular, Goidelic.
gvc  Guanano  -  gvc  Brazil  7  517626  3264491  GVC  -  -  -  pir myy tav bao bsn sue des cbc zia  en  no  -  Thu Dec 27 16:50:38 CST 2012  WANÂNA, WANANO, UANANA, ANANA, KÓTEDIA, KÓTIRYA  Tucanoan, Eastern Tucanoan, Northern.
gvf  Golin  -  gvf  Papua New Guinea  0  0  0  GVF  -  -  -  kue snk cjv wmw su kwn sw swh kne  en  no  -  -  GOLLUM, GUMINE  Trans-New Guinea, Main Section, Central and Western, East New Guinea Highlands, Central, Chimbu.
gwi  Gwich’in  -  gwi  Canada  49  349230  2638357  KUC  -  -  -  om  en  no  -  Thu Dec 27 16:54:28 CST 2012  KUTCHIN, LOUCHEUX  Na-Dene, Nuclear Na-Dene, Athapaskan-Eyak, Athapaskan, Canadian, Han-Kutchin.
gym  Ngäbere  Ngäbere  gym  Panama  157  512574  3143066  GYM  ngb  -  -  nen ckk  en  no  -  Sun Feb 3 12:27:04 CST 2013  VALIENTE, CHIRIQUI, NGOBERE, NGÄBERE, GUAYMÍ  Chibchan, Guaymi.
gyr  Guarayu  -  gyr  Bolivia  6  234964  1508166  GYR  -  -  gua  gnw gui gn kgk pah gub cut urb  en  no  -  Wed Jan 30 20:34:03 CST 2013  'GUARAYO'  Tupi, Tupi-Guarani, Guarayu-Siriono-Jora (II).
ha  Hausa  Hausa  hau  Nigeria  1205  3974510  23602771  HUA  ha  ha  gej  iry adz ifk bjn pwg snk bik sw sml tmh itv  en  started  Hirokazu Nakamura, Mustapha Abubakar  Fri Sep 13 11:15:10 CDT 2013  HAUSAWA, HAOUSSA, ABAKWARIGA, MGBAKPA, HABE, KADO  Afro-Asiatic, Chadic, West, A, A.1.
haa  Hän  Hän  haa  USA  0  0  0  HAA  -  -  -  tce tgx hnj gwi pls  en  no  -  -  HAN-KUTCHIN, MOOSEHIDE, DAWSON  Na-Dene, Nuclear Na-Dene, Athapaskan-Eyak, Athapaskan, Canadian, Han-Kutchin.
hae  Eastern Oromo  -  hae  Ethiopia  1  180  1222  HAE  -  -  -  bjn son iry ha hnn snk  en  no  -  Wed Apr 24 21:29:01 CDT 2013  'QOTU' OROMO, HARAR, HARER, 'QOTTU', 'QUOTTU', 'QWOTTU', 'KWOTTU', ITTU  Afro-Asiatic, Cushitic, East, Oromo.
hag  Hanga  -  hag  Ghana  1  202056  927571  HAG  -  -  -  dag gux cko bm  en  no  -  Sat Jan 5 13:53:15 CST 2013  ANGA  Niger-Congo, Atlantic-Congo, Volta-Congo, North, Gur, Central, Northern, Oti-Volta, Western, Southeast.
hai  Haida  -  hai  Canada  4  3924  28279  -  -  -  -  tl pam msk fil kyk agn jv hil lnu  en  no  -  Tue Jan 29 10:46:22 CST 2013  MASSET  Na-Dene, Haida.
hak  Hakka Chinese  Hak-kâ-fa  hak  China  173  270606  1925083  HAK  -  hak  -  nan  en  no  -  Fri Jan 25 15:03:04 CST 2013  HAKKA, HOKKA, KEJIA, KECHIA, KE, XINMINHUA, MAJIAHUA, TU GUANGDONGHUA  Sino-Tibetan, Chinese.
har  Harari  -  har  Ethiopia  13  14469  83260  HAR  -  -  -  am tig ti  en am  no  Fahmi Hussein  Thu Nov 14 12:59:05 CST 2013  HARARRI, ADARE, ADERE, ADERINYA, ADARINNYA, GEY SINAN  Afro-Asiatic, Semitic, South, Ethiopian, South, Transversal, Harari-East Gurage.
has  Haisla  X̄a'’islak̓ala  has  Canada  2  118  907  HAS  -  -  -  gur eo gur-x-nink lms emk nak lnc lad io  en  started  -  Mon Oct 1 13:13:19 CDT 2012  -  Wakashan, Northern.
haw  Hawaiian  ʻŌlelo Hawaiʻi  haw  USA  51  196864  961188  HWI  -  haw  hwi  to bnp mi mlu stn tkl sm fj  en  yes  Keola Donaghy, Joseph Colton, Jim Thompson  Mon Dec 9 14:09:19 CST 2013  'OLELO HAWAI'I, 'OLELO HAWAI'I MAKUAHINE  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Central Pacific, East Fijian-Polynesian, Polynesian, Nuclear, East, Central, Marquesic.
hay  Haya  -  hay  Tanzania  2  113391  906320  HAY  -  -  -  lg nyo nyn ttj mho xog  en  no  -  Fri Jan 25 15:21:42 CST 2013  EKIHAYA, RUHAYA, ZIBA  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, J, Haya-Jita (J.20).
hbs  Serbo-Croatian  -  hbs  Serbia  34  13393534  89158596  SRC  -  sh  -  mk-Latn bg-Latn cs sk wen uk-Latn  en  started  -  Thu Jan 24 10:32:19 CST 2013  SERBIAN, MONTENEGRIN  Indo-European, Slavic, South, Western.
hbs-Cyrl  Serbo-Croatian (Cyrillic)  -  hbs  Serbia  180  186954  1246150  SRC  -  -  -  mk bg ru uk  en ru  started  -  Thu Jan 24 10:46:10 CST 2013  SERBIAN, MONTENEGRIN  Indo-European, Slavic, South, Western.
hch  Huichol  -  hch  Mexico  6  321713  3102513  HCH  -  -  -  arl cni cof cav bon snc nhg cot  en es  no  -  Thu Dec 27 17:04:29 CST 2012  -  Uto-Aztecan, Southern Uto-Aztecan, Sonoran, Corachol.
hdn  Northern Haida  -  hdn  Canada  1  210  1493  HAI  -  -  -  msk jv-x-bms bjn tl  en  no  Jordan Lachler  Tue Jan 29 10:44:12 CST 2013  MASSET  Na-Dene, Haida.
he  Hebrew  עברית  heb  Israel  2575  7759956  48002779  HBR  q  he  hbr  yi  en  yes  -  Tue Sep 10 11:04:44 CDT 2013  IVRIT  Afro-Asiatic, Semitic, Central, South, Canaanite.
he-Latn  Hebrew (Latin)  -  heb  Israel  125  327744  2077382  HBR  -  -  -  pau pes-Latn ti-Latn  en  no  -  Wed Jan 16 00:15:10 CST 2013  IVRIT  Afro-Asiatic, Semitic, Central, South, Canaanite.
hea  Northern Qiandong Miao  -  hea  China  1  2796  13718  HEA  -  -  hea  gos fr-x-jer lou  en  no  -  Mon Dec 9 14:14:17 CST 2013  NORTHERN QIANDONG MIAO, CHIENTUNG MIAO, EAST GUIZHOU MIAO, HMU, MIAO, BLACK MIAO, HEH MIAO, HEI MIAO, CENTRAL MIAO, NORTHERN EAST-GUIZHOU MIAO  Hmong-Mien, Hmongic, Qiandong.
heh  Hehe  -  heh  Tanzania  1  136050  1015337  HEH  -  -  -  kde lue bem wmw  en  no  -  Sat Jan 5 14:18:42 CST 2013  KIHEHE  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, G, Bena-Kinga (G.60).
hi  Hindi  हिंदी  hin  India  1552  15715354  85551746  HND  hi*  hi  hnd  bho mag hne bh mai ne mr  en  yes  -  Sun Feb 3 12:08:45 CST 2013  KHARI BOLI, KHADI BOLI  Indo-European, Indo-Iranian, Indo-Aryan, Central zone, Western Hindi, Hindustani.
hi-Latn  Hindi (Latin)  -  hin  India  1261  2896210  16144586  HND  -  -  -  hns hif ur-Latn npy ne-Latn  en  no  -  Tue Sep 10 11:00:11 CDT 2013  KHARI BOLI, KHADI BOLI  Indo-European, Indo-Iranian, Indo-Aryan, Central zone, Western Hindi, Hindustani.
hif  Fiji Hindi  -  hif  Fiji  3  519864  2843755  HIF  -  hif  -  hns bh-Latn hi-Latn din  en  no  -  Mon Dec 9 14:11:27 CST 2013  FIJIAN HINDI, FIJI HINDUSTANI  Indo-European, Indo-Iranian, Indo-Aryan, East Central zone.
hig  Kamwe  -  hig  Nigeria  1  250454  1301656  HIG  -  -  -  bcw gde  en  no  -  Sat Jan 5 14:19:07 CST 2013  HIGI, HIJI, HIGGI, VACAMWE  Afro-Asiatic, Chadic, Biu-Mandara, A, A.3.
hil  Hiligaynon  Hiligaynon  hil  Philippines  804  661415  4062563  HIL  hv  -  hil  ceb krj tl akl kyk bik hnn jv  en  yes  Francis Dimzon  Wed Sep 18 20:10:41 CDT 2013  ILONGGO, HILIGAINON  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Meso Philippine, Central Philippine, Bisayan, Central, Peripheral.
hix  Hixkaryána  -  hix  Brazil  1  346490  2305150  HIX  -  -  -  car sbl  en  no  -  Mon Dec 31 16:11:05 CST 2012  HIXKARIANA, HISHKARYANA, PARUKOTO-CHARUMA, PARUCUTU, CHAWIYANA, KUMIYANA, SOKAKA, WABUI, FARUARU, SHEREWYANA, XEREWYANA, XEREU, HICHKARYANA  Carib, Southern, Southern Guiana.
hla  Halia  -  hla  Papua New Guinea  288  340334  1664444  HLA  -  -  -  mi tkl rar ty gil bnp alu rap tvl rmy  en  no  -  Wed Jan 30 08:31:33 CST 2013  TASI  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, South New Ireland-Northwest Solomonic, Nehan-North Bougainville, Buka, Halia.
hlt  Matu Chin  -  hlt  Myanmar  1  2374  13171  HLT  -  -  hlt  cnk cnh mwq pam ctd bgr tl jv su lcm kyk  en  no  -  Mon Dec 9 14:14:19 CST 2013  Nga La  Sino-Tibetan, Tibeto-Burman, Sal, Kuki-Chin-Naga, Kuki-Chin, Southern
hmn  Hmong  -  hmn  China  1110  4763491  25556996  -  hm  -  -  eo csa lt  en  no  -  Fri Sep 13 15:21:48 CDT 2013  CHUANQIANDIAN MIAO, CHUANCHIENTIEN MIAO, SICHUAN-GUIZHOU-YUNNAN HMONG, TAK MIAO, MEO, MIAO, WESTERN MIAO, WESTERN HMONG  Hmong-Mien, Hmongic, Chuanqiandian.
hms  Southern Qiandong Miao  -  hms  China  1  2223  11302  HMS  -  -  hms  hea msk bo-Latn kyk  en  no  -  Mon Dec 9 14:14:10 CST 2013  SOUTHERN QIANDONG MIAO, HMU, MIAO, BLACK MIAO, CENTRAL MIAO, SOUTHERN EAST-GUIZHOU MIAO  Hmong-Mien, Hmongic, Qiandong.
hmt  Hamtai  -  hmt  Papua New Guinea  1  3099  19385  HMT  -  -  -  war sg znd  en  no  -  Tue Jan 1 16:24:17 CST 2013  HAMDAY, KAPAU, KAMEA, WATUT, 'KUKUKUKU'  Trans-New Guinea, Main Section, Central and Western, Angan, Angan Proper.
hna  Mina  -  hna  Cameroon  3  223900  1035863  HNA  -  -  hna  ee mnk man knk gjn fon  en  no  -  Fri Jan 25 15:21:08 CST 2013  HINA, BESLERI  Afro-Asiatic, Chadic, Biu-Mandara, A, A.7.
hne  Chhattisgarhi  छत्तीसगढ़ी  hne  India  103  351179  1741626  HNE  -  -  hne*  hi bh bho mag mai  en  no  G Karunakar, Ravishankar Shrivastava  Wed Sep 18 20:11:50 CDT 2013  LARIA, KHALTAHI  Indo-European, Indo-Iranian, Indo-Aryan, East Central zone.
hni  Hani  -  hni  China  2  7310  42501  HNI  -  -  hni  sas hla ff  en  no  -  Tue Jan 15 23:34:23 CST 2013  HANHI, HAW, HANI PROPER  Sino-Tibetan, Tibeto-Burman, Lolo-Burmese, Loloish, Southern, Akha, Hani, Ha-Ya.
hnj  Hmong Njua  -  hnj  China  1  2871  14250  BLU  -  -  blu  hea hms zao bo-Latn  en  no  -  Mon Dec 9 14:14:05 CST 2013  CHUANQIANDIAN MIAO, CHUANCHIENTIEN MIAO, SICHUAN-GUIZHOU-YUNNAN HMONG, TAK MIAO, MEO, MIAO, WESTERN MIAO, WESTERN HMONG  Hmong-Mien, Hmongic, Chuanqiandian.
hnn  Hanunoo  -  hnn  Philippines  4  207567  1268508  HNN  -  -  -  krj ceb hil bik sml bku akl bjn su tl  en  no  -  Sat Jan 5 14:29:20 CST 2013  HANONOO  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Meso Philippine, South Mangyan, Hanunoo.
hns  Caribbean Hindustani  Sarnámi  hns  Suriname  6  306489  1782397  HNS  -  -  -  hif hi-Latn ur-Latn pes-Latn  en  no  -  Sat Dec 21 08:17:34 CST 2013  -  Indo-European, Indo-Iranian, Indo-Aryan, Eastern zone, Bihari.
ho  Hiri Motu  Hiri Motu  hmo  Papua New Guinea  357  462824  2714696  POM  mo  ho  -  meu mlu aia  en  no  -  Sun Feb 3 12:42:58 CST 2013  POLICE MOTU, PIDGIN MOTU, HIRI  Pidgin, Motu based.
hop  Hopi  -  hop  USA  5  194942  1289043  HOP  -  -  -  kyk  en  no  -  Thu Dec 27 17:05:35 CST 2012  -  Uto-Aztecan, Northern Uto-Aztecan, Hopi.
hot  Hote  -  hot  Papua New Guinea  0  0  0  HOT  -  -  -  buk lia twu bts tet sml  en  no  -  -  HO'TEI, HOTEC, MALEI, MALÊ  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Huon Gulf, South, Hote-Buang, Hote.
hr  Croatian  Hrvatski  hrv  Croatia  1954  14918089  99251393  CRX  c  hr  src2  sl mk-Latn  en  yes  -  Sun Feb 3 14:53:38 CST 2013  SERBIAN, MONTENEGRIN  Indo-European, Slavic, South, Western.
hr-Glag  Croatian (Glagolitic)  -  hrv  Croatia  3  4694  35075  CRX  -  -  -  -  en  no  -  Thu Jan 17 15:23:01 CST 2013  -  Indo-European, Slavic, South, Western.
hsb  Upper Sorbian  Hornjoserbsce  hsb  Germany  820  1167610  8138764  WEN  -  hsb  wee  dsb sr-Latn hr bs szl sl cs pl  en pl de  yes  Edi Werner, Bernhard Baier, Michał Wjelk  Wed Jan 30 20:58:36 CST 2013  OBERSORBISCH, HAUT SORABE, UPPER LUSATIAN, WENDISH, HORNJOSERBSKI, HORNOSERBSKI  Indo-European, Slavic, West, Sorbian.
hsf  Southeastern Huastec  -  hsf  Mexico  1  2119  12190  HAU  -  -  hus  hva kvn kjb dak sbl  en es  no  -  Mon Dec 9 14:14:00 CST 2013  SOUTHEASTERN HUASTECO, SAN FRANCISCO CHONTLA HUASTEC  Mayan, Huastecan.
ht  Haitian Creole  Kreyòl Ayisyen  hat  Haiti  296  36068162  198994712  HAT  cr  ht  hat  crs acf mfe rcf  en fr  yes  John Rigdon, Jean Came Poulard, Jeff Allen  Fri Sep 13 10:23:54 CDT 2013  -  Creole, French based.
hto  Minica Huitoto  -  hto  Colombia  2  224323  1550129  HTO  -  -  -  huu an  en es  no  -  Thu Dec 27 17:07:27 CST 2012  MI+NI+CA, MENECA, MINICA  Witotoan, Witoto, Witoto Proper, Minica-Murui.
hu  Hungarian  Magyar  hun  Hungary  4526  10897914  80214752  HNG  h  hu  hng  pau br-x-falhuneg  en  yes  -  Mon Jul 15 13:29:16 CDT 2013  MAGYAR  Uralic, Finno-Ugric, Ugric, Hungarian.
hub  Huambisa  -  hub  Peru  2  240102  1892307  HUB  -  -  -  acu jiv agr  en es  no  -  Thu Dec 27 17:11:55 CST 2012  HUAMBIZA, WAMBISA  Jivaroan.
hui  Huli  -  hui  Papua New Guinea  994  1454327  9118605  HUI  -  -  -  znd sw  en  no  -  Sat Jan 5 15:09:24 CST 2013  HULI-HULIDANA, HURI  Trans-New Guinea, Main Section, Central and Western, East New Guinea Highlands, West-Central, Huli.
hur  Halkomelem  hən̓q̓əmin̓əm̓  hur  Canada  3  2965  20345  HUR  -  -  -  sec tzh ty rap mbs rar wls tkl rmn mbt tvl mi mbi  en  no  -  Thu Jan 10 21:49:59 CST 2013  -  Salishan, Central Salish, Halkomelem.
hur-x-cow  Halkomelem (Cowichan)  Hul’q’umi’num’  hur  Canada  0  0  0  HUR  -  -  -  la vmw sek  en  no  -  -  -  Salishan, Central Salish, Halkomelem.
hur-x-upr  Halkomelem (Upriver)  Halq’eméylem  hur  Canada  0  0  0  HUR  -  -  -  sec tzh ty rap rar mbs wls tkl rmn mbt mi tvl  en  no  -  -  -  Salishan, Central Salish, Halkomelem.
hus  Huastec  Tenek  hus  Mexico  6  361035  2062065  HUS  -  -  1118  ifu bik dak lkt ctp ifb lus kvn kjb tzo  en es  yes  José Luis González, Jesús Carretero  Sun Feb 3 12:47:22 CST 2013  TANTOYUCA HUASTEC  Mayan, Huastecan.
hus-x-veracruz  Veracruz Huastec  Tenek  hus  Mexico  1  254921  1459859  HUS  -  -  -  ifu bik dak lkt ctp ifb lus kvn kjb tzo  en es  no  José Luis González, Jesús Carretero  Wed Sep 25 10:40:27 CDT 2013  TANTOYUCA HUASTEC  Mayan, Huastecan.
huu  Murui Huitoto  -  huu  Peru  3  119635  550761  HUU  -  -  huu  hto  en es  no  -  Thu Dec 27 17:12:34 CST 2012  BUE, WITOTO  Witotoan, Witoto, Witoto Proper, Minica-Murui.
huv  San Mateo del Mar Huave  ombeayiiüts  huv  Mexico  35  332794  2194514  HUV  -  -  -  tl agn bjn msk hil pam kyk bku su  en es  no  Sam Herrera  Sun Feb 3 13:08:37 CST 2013  -  Huavean.
hva  San Luís Potosí Huastec  -  hva  Mexico  5  368345  2067267  HVA  -  -  hva  ncl kjb ncj  en es  no  -  Thu Dec 27 17:18:52 CST 2012  POTOSINO HUASTEC  Mayan, Huastecan.
hwc  Hawaiʻi Pidgin  -  hwc  USA  471  586359  2842467  HAW  -  -  -  en  en  no  -  Thu Dec 27 17:23:06 CST 2012  PIDGIN, HAWAI'I CREOLE ENGLISH, HCE  Creole, English based, Pacific.
hy  Armenian  Հայերեն  hye  Armenia  2101  3863495  29296168  ARM  r  hy  arm  xcl  en  yes  -  Sun Feb 3 14:54:55 CST 2013  HAIEREN, SOMKHURI, ENA, ERMENICE, ERMENI DILI, ARMJANSKI YAZYK  Indo-European, Armenian.
hy-Latn  Armenian (Latin)  -  hye  Armenia  73  514242  3927211  ARM  -  -  -  nl br  en  no  -  Sat Sep 14 16:28:35 CDT 2013  HAIEREN, SOMKHURI, ENA, ERMENICE, ERMENI DILI, ARMJANSKI YAZYK  Indo-European, Armenian.
hy-x-ear  Eastern Armenian  -  hye  Armenia  1  11307  79661  ARM  rea  -  -  hy  en  no  -  Thu Jan 17 09:59:46 CST 2013  HAIEREN, SOMKHURI, ENA, ERMENICE, ERMENI DILI, ARMJANSKI YAZYK  Indo-European, Armenian.
hz  Herero  Otjiherero  her  Namibia  73  217368  1551628  HER  hr  hz  -  kwn nyk ng sn ndc wmw kj rw nyn lg seh dig nyo kki tum rn sw pkb ki kue nyf  en  no  -  Mon Dec 2 12:10:40 CST 2013  OTJIHERERO, OCHIHERERO  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, R, Herero (R.30).
ia  Interlingua  Interlingua  ina  -  33  1149308  7374911  INR  -  ia  1119  fr es cbk ast ca oc pt  en  yes  Giovanni Sora  Tue Sep 10 11:00:09 CDT 2013  INTERLINGUA DE IALA  Artificial.
ian  Iatmul  -  ian  Papua New Guinea  0  0  0  IAN  -  -  -  abt-x-wosera abt son srr wmw pkb lag sw swh  en  no  -  -  BIG SEPIK, NGEPMA KWUNDI, GEPMA KWUDI, GEPMA KWUNDI  Sepik-Ramu, Sepik, Middle Sepik, Ndu.
iar  Purari  -  iar  Papua New Guinea  5  556  3898  IAR  -  -  -  sco-x-scotland frr-x-fer tbc dgz bnc myw ga-Latg aai  en  no  -  Sun Sep 22 23:40:55 CDT 2013  KORIKI, EVORRA, NAMAU, IAI, MAIPUA  Trans-New Guinea, Eleman, Purari.
iba  Iban  Iban  iba  Malaysia (Sarawak)  549  1711458  10590419  IBA  ia  -  -  bjn id zsm jv-x-bms su btx zlm  en  no  Suhaila Saee  Sun Feb 3 13:10:17 CST 2013  SEA DAYAK  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Sundic, Malayic, Malayic-Dayak, Ibanic.
ibb  Ibibio  Ibibio  ibb  Nigeria  2  2877  15738  IBB  -  -  ibb  efi ig din ny hif dip  en  no  -  Wed Sep 18 20:14:02 CDT 2013  -  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Cross River, Delta Cross, Lower Cross, Obolo, Efik.
ibd  Iwaidja  -  ibd  Australia  0  0  0  IBD  -  -  -  bvr gup wbp tiw wmt mpj  en  no  -  -  Eiwaja, Ibadjo, Iwaidji, Iwaydja, Jiwadja, Karadjee, Limba  Australian, Yiwaidjan, Yiwaidjic.
ibl  Ibaloi  -  ibl  Philippines  5  54805  304529  IBL  -  -  -  pag msm mbd ami atd ify  en  no  -  Fri Sep 13 15:22:54 CDT 2013  IBALOY, IBADOY, INIBALOI, NABALOI, BENGUET-IGOROT, IGODOR  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Northern Philippine, Northern Luzon, South-Central Cordilleran, Southern Cordilleran, Pangasinic, Benguet, Ibaloi-Karao.
icr  Islander Creole English  -  icr  Colombia  2  165576  801965  ICR  -  -  -  jam bzj  en es  no  -  Thu Dec 27 17:18:40 CST 2012  Bende, San Andrés Creole  Creole, English based, Atlantic, Western.
id  Indonesian  Bahasa Indonesia  ind  Indonesia (Java and Bali)  1660  17609764  127051700  INZ  in  id  inz  jv-x-bms bjn su min  en  yes  Ferli Deni Iskander  Sun Feb 3 14:53:03 CST 2013  BAHASA INDONESIA  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Sundic, Malayic, Malayan, Local Malay.
ie  Interlingue  Interlingue  ile  -  466  967322  6082401  ILE  -  ie  -  nov ca ast oc ia es fr  en  no  -  Thu Jan 17 17:29:43 CST 2013  Occidental  Artificial.
ifb  Batad Ifugao  -  ifb  Philippines  1  214739  1276034  IFB  -  -  -  ifk bjn pag sbl ms war  en  no  -  Sat Jan 5 14:37:43 CST 2013  BATAD  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Northern Philippine, Northern Luzon, South-Central Cordilleran, Central Cordilleran, Nuclear Cordilleran, Ifugao.
ifk  Tuwali Ifugao  -  ifk  Philippines  2  203555  1194712  IFK  -  -  -  ifb bjn itv zsm id bnc pag kne ify jv-x-bms  en  no  -  Fri Sep 13 15:24:30 CDT 2013  KIANGAN IFUGAO, QUIANGAN, GILIPANES, TUWALI  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Northern Philippine, Northern Luzon, South-Central Cordilleran, Central Cordilleran, Nuclear Cordilleran, Ifugao.
ifu  Mayoyao Ifugao  -  ifu  Philippines  1  240269  1343805  IFU  -  -  -  ifb ifk war tzt sbl lus  en sw no  no  -  Sat Jan 5 15:24:17 CST 2013  MAYOYAO, MAYAOYAW  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Northern Philippine, Northern Luzon, South-Central Cordilleran, Central Cordilleran, Nuclear Cordilleran, Ifugao.
ify  Keley-i Kallahan  -  ify  Philippines  1  795846  4719618  IFY  -  -  -  ifk ifb bjn ms dag yap jv-x-bms  en  no  -  Sat Jan 5 15:24:57 CST 2013  ANTIPOLO IFUGAO, KELEYQIQ IFUGAO, KELEY-I  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Northern Philippine, Northern Luzon, South-Central Cordilleran, Southern Cordilleran, Pangasinic, Benguet, Kallahan.
ig  Igbo  Igbo  ibo  Nigeria  75  413830  2256497  IGR  ib  ig  igr  ln ki bng fj sw  en  started  Chinedu Uchechukwu, Ogechi Nnadi, Ijem Ofili  Sat Feb 2 19:52:15 CST 2013  IBO  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Igboid, Igbo.
igl  Igala  Igala  igl  Nigeria  1  6417  34370  IGL  aa  -  -  bim  en  no  -  Thu Jan 17 16:36:57 CST 2013  IGARA  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Defoid, Yoruboid, Igala.
ign  Ignaciano  -  ign  Bolivia  2  526784  3481665  IGN  -  -  -  tbo inb  en es  no  -  Sat Jan 5 15:17:36 CST 2013  MOXO, MOXOS, MOJOS  Arawakan, Maipuran, Southern Maipuran, Bolivia-Parana.
ii  Sichuan Yi  -  iii  China  2  343  6018  III  -  ii  iii  -  en  no  -  Wed Jan 30 11:06:38 CST 2013  NORTHERN YI, I, 'LOLO', 'NORTHERN LOLO', SEN NOSU, GNI, NYI, NUOSU  Sino-Tibetan, Tibeto-Burman, Lolo-Burmese, Loloish, Northern, Yi.
ik  Inupiaq  Iñupiaq  ipk  USA  4  100569  1197284  -  -  ik  -  csk art-x-tokipona  en  no  -  Fri Jan 25 19:37:21 CST 2013  NORTH ALASKAN INUPIAT, INUPIAT, 'ESKIMO'  Eskimo-Aleut, Eskimo, Inuit.
ike  Eastern Canadian Inuktitut  -  ike  Canada  1  944  9656  ESB  -  -  esb  ojb-Cans cr nsk crk csw scs-Cans den-Cans  en  no  -  Mon Dec 9 14:13:55 CST 2013  EASTERN CANADIAN 'ESKIMO', EASTERN ARCTIC 'ESKIMO', INUIT  Eskimo-Aleut, Eskimo, Inuit.
ili  Ili Turki  -  ili  China  2  139  983  ILI  -  -  -  tr uz-Latn tk uzn-Latn ug-Latn crh  en  no  -  Mon Sep 23 11:05:49 CDT 2013  T'URK, TUERKE  Altaic, Turkic, Eastern.
ilo  Ilocano  Ilokano  ilo  Philippines  1120  2379678  15457320  ILO  il  ilo  ilo  sg tzu tzc  en  no  Eugene Carmelo C. Pedro, Joe Maza  Sun Feb 3 14:09:13 CST 2013  ILOKO, ILOKANO  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Northern Philippine, Northern Luzon, Ilocano.
imo  Imbongu  -  imo  Papua New Guinea  287  328156  2080985  IMO  -  -  -  ach kj zne luo ng kki  en  no  -  Sat Feb 16 17:18:38 CST 2013  IMBO UNGU, IBO UGU, IMBONGGO, AWA, AUA, AU, IMBO UNGO  Trans-New Guinea, Main Section, Central and Western, East New Guinea Highlands, Central, Hagen, Kaugel.
inb  Inga  -  inb  Colombia  3  417118  1890375  INB  -  -  -  qxw qvs qug qvz qup lbb tbo  en es  no  -  Wed Dec 5 16:06:39 CST 2012  HIGHLAND INGA  Quechuan, Quechua II, B.
inh  Ingush  ГІалгІай  inh  Russian Federation  3  2502  19963  INH  ing  -  -  ce dar  en  no  -  Wed Sep 18 21:29:44 CDT 2013  GHALGHAY, INGUS  North Caucasian, North Central, Chechen-Ingush.
ino  Inoke-Yate  -  ino  Papua New Guinea  0  0  0  INO  -  -  -  mnb yby bef swh alu haw kng for  en  no  -  -  INOKE, YATE  Trans-New Guinea, Main Section, Central and Western, East New Guinea Highlands, East-Central, Kamano-Yagaria.
io  Ido  Ido  ido  -  21  2764995  15284152  -  -  io  1120  eo lms lnc ext oc lad es  en  no  -  Thu Jan 17 18:07:34 CST 2013  -  Artificial.
iou  Tuma-Irumu  -  iou  Papua New Guinea  0  0  0  IOU  -  -  -  awx wca fi bts miq  en  no  -  -  GUMIA, UPPER IRUMU, TUMA, IRUMU  Trans-New Guinea, Main Section, Central and Western, Huon-Finisterre, Finisterre, Wantoat.
ipi  Ipili  -  ipi  Papua New Guinea  287  360831  2456113  IPI  -  -  -  kyc chw lu aso kqn kg ain swh  en  no  -  Sat Feb 16 17:24:46 CST 2013  IPILI-PAIELA, IPILI-PAYALA  Trans-New Guinea, Main Section, Central and Western, East New Guinea Highlands, West-Central, Enga.
irk  Iraqw  -  irk  Tanzania  13  186995  1190336  IRK  -  -  -  son sw bwu  en  no  -  Sat Jan 5 15:36:02 CST 2013  MBULU, MBULUNGE, EROKH, IRAKU  Afro-Asiatic, Cushitic, South.
iry  Iraya  -  iry  Philippines  5  204359  1201757  IRY  -  -  -  hnn bik ceb ha hil akl tl  en  no  -  Sat Jan 5 22:07:15 CST 2013  -  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Northern Philippine, Bashiic-Central Luzon-Northern Mindoro, Northern Mindoro.
is  Icelandic  Íslenska  isl  Iceland  3244  10947577  69412689  ICE  ic  is  ice  fo nn  en  yes  -  Sun Feb 3 13:28:55 CST 2013  ÍSLENSKA, YSLENSKA  Indo-European, Germanic, North, West Scandinavian.
iso  Isoko  Isoko  iso  Nigeria  81  133671  679044  ISO  is  -  -  urh ig nfr bnp  en  no  -  Sun Feb 3 14:47:20 CST 2013  'IGABO', 'SOBO', 'BIOTU'  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Edoid, Southwestern.
ist  Istriot  -  ist  Croatia  7  3731  26262  IST  -  -  -  en  en  no  -  Sun Sep 22 23:46:52 CDT 2013  -  Indo-European, Italic, Romance, Italo-Western, Italo-Dalmatian.
it  Italian  Italiano  ita  Italy  2079  7826698  51067975  ITN  i  it  itn  fur ia lld co lmo ro  en  yes  -  Sun Feb 3 16:36:53 CST 2013  ITALIANO  Indo-European, Italic, Romance, Italo-Western, Italo-Dalmatian.
itl  Itelmen  итэнмэн  itl  Russian Federation  3  265  2315  ITL  -  -  -  neg ckt lez sah ru  en  no  -  Sun Sep 22 23:48:04 CDT 2013  ITELYMEM, WESTERN ITELMEN, KAMCHADAL, KAMCHATKA  Chukotko-Kamchatkan, Southern.
its  Isekiri  -  its  Nigeria  39  21702  113345  ITS  it  -  -  yo tzu ilo tpm sg hag dag maw  en  no  -  Fri Sep 13 14:06:42 CDT 2013  ITSEKIRI, ISHEKIRI, SHEKIRI, JEKRI, CHEKIRI, IWERE, IRHOBO, WARRI, ISELEMA-OTU, SELEMO  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Defoid, Yoruboid, Edekiri.
itv  Itawit  -  itv  Philippines  5  240621  1366425  ITV  -  -  -  war pag ifk hnn krj  en  no  -  Sat Jan 5 22:22:15 CST 2013  ITAWIS, TAWIT, ITAWES  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Northern Philippine, Northern Luzon, Northern Cordilleran, Ibanagic, Ibanag.
iu  Inuktitut  ᐃᓄᒃᑎᑐᑦ  iku  Canada  854  406876  3284622  -  -  iu  -  nsk csw cr ojb-Cans oj-Cans  en  no  Tim Pasch, Éric Poncet  Sun Sep 15 22:00:20 CDT 2013  EASTERN CANADIAN 'ESKIMO', EASTERN ARCTIC 'ESKIMO', INUIT  Eskimo-Aleut, Eskimo, Inuit.
iu-Latn  Inuktitut (Latin)  Inuktitut  iku  Canada  2  2652504  36569421  -  -  -  -  kl esk ik  en fr  no  Rachael Petersen  Mon Nov 26 16:46:36 CST 2012  EASTERN CANADIAN 'ESKIMO', EASTERN ARCTIC 'ESKIMO', INUIT  Eskimo-Aleut, Eskimo, Inuit.
ivv  Ivatan  Ivatan  ivv  Philippines  1  2097  11728  IVV  iv  -  -  ha dgc  en  no  -  Thu Jan 17 18:17:36 CST 2013  -  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Northern Philippine, Bashiic-Central Luzon-Northern Mindoro, Bashiic, Ivatan.
iws  Sepik Iwam  -  iws  Papua New Guinea  289  374197  2412006  IWS  -  -  -  msy aui abx sml  en  no  -  Sat Feb 16 17:47:06 CST 2013  YAWENIAN  Sepik-Ramu, Sepik, Upper Sepik, Iwam.
ixi  Nebaj Ixil  -  ixi  Guatemala  2  325879  1762502  IXI  -  -  -  ixl-x-ixl  en  no  -  Thu Dec 27 18:23:00 CST 2012  -  Mayan, Quichean-Mamean, Greater Mamean, Ixilan.
ixl  Ixil  -  ixl  Guatemala  3  628374  3509143  IXL  -  -  -  yua chf lac mop ttc hla bba tiv  en  no  -  Wed Dec 11 10:07:58 CST 2013  -  Mayan, Quichean-Mamean, Greater Mamean, Ixilan.
ixl-x-ixl  San Juan Cotzal Ixil  -  ixl  Guatemala  0  0  0  IXL  -  -  -  ixi yua chf lac mop ttc hla bba tiv  en  no  -  -  -  Mayan, Quichean-Mamean, Greater Mamean, Ixilan.
izh  Ingrian  Ižoran keel  izh  Russian Federation  17  1026  7724  IZH  -  -  -  ubr fit ekk fi krl gcf ngu azg fkv shp  en  no  -  Sun Sep 22 23:58:37 CDT 2013  IZHOR  Uralic, Finno-Ugric, Finno-Permic, Finno-Cheremisic, Finno-Mordvinic, Finno-Lappic, Baltic-Finnic.
izr  Izere  -  izr  Nigeria  1  215634  970642  FIZ  -  -  -  pam dga jv lnu  en  no  -  Sat Jan 5 22:13:09 CST 2013  IZAREK, FIZERE, FEZERE, FESEREK, AFIZAREK, AFIZARE, AFUSARE, JARI, JARAWA, JARAWAN DUTSE, HILL JARAWA, JOS-ZARAZON  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Platoid, Plateau, Central, South-Central.
ja  Japanese  日本語  jpn  Japan  1469  880472  13734510  JPN  j  ja  jpn  cmn gan  en  no  -  Sat Sep 14 09:26:10 CDT 2013  -  Japanese, Japanese.
ja-Latn  Japanese (Romaji)  -  jpn  Japan  57  138834  815568  JPN  -  -  -  amm zpa msm ak mbd  en  no  -  Tue Jan 15 00:16:16 CST 2013  -  Japanese, Japanese.
jac  Jakalteko  -  jac  Guatemala  2  263229  1648265  JAC  -  -  -  knj  en  no  -  Thu Dec 27 18:23:59 CST 2012  -  Mayan, Kanjobalan-Chujean, Kanjobalan, Kanjobal-Jacaltec.
jac-x-eastern  Eastern Jakalteko  -  jac  Guatemala  0  0  0  JAC  -  -  -  knj  en  no  -  -  -  Mayan, Kanjobalan-Chujean, Kanjobalan, Kanjobal-Jacaltec.
jae  Yabem  -  jae  Papua New Guinea  0  0  0  JAE  -  -  -  buk hot dah kgf  en  no  -  -  LAULABU, JABEM, JABIM, YABIM  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Huon Gulf, North.
jam  Jamaican Creole English  Jumiekan Kriol  jam  Jamaica  18  307050  1372687  JAM  -  -  -  icr bzj djk  en  no  -  Wed Sep 18 21:33:06 CDT 2013  Southwestern Caribbean Creole English  Creole, English based, Atlantic, Western.
jao  Yanyuwa  Yanyuwa  jao  Australia  2  158  1181  JAO  -  -  -  ibd son dig  en  no  -  Tue Jan 15 00:12:17 CST 2013  YANYULA, JANJULA, ANYULA, WADIRI, YANULA, ANIULA, ANULA, LEEANUWA  Australian, Pama-Nyungan, Yanyuwan.
jax  Jambi Malay  -  jax  Indonesia (Sumatra)  5  1102  8145  JAX  -  -  -  id zsm bjn jv-x-bms su bew min jv iba zlm ifk bsb  en  no  -  Sun Sep 22 23:58:22 CDT 2013  -  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Sundic, Malayic, Malayan, Local Malay.
jbo  Lojban  Lojban  jbo  -  496  794468  4153771  -  -  jbo  -  sm fud  en  no  -  Thu Jan 17 20:37:33 CST 2013  -  Artificial.
jbu  Jukun Takum  -  jbu  Nigeria  0  0  0  JBU  -  -  -  miq ha tpm bba wmw sw bim swh gux  en  no  -  -  DIYI, NJIKUM, JUKUN  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Platoid, Benue, Jukunoid, Central, Jukun-Mbembe-Wurbo, Jukun.
jct-Latn  Krimchak  Kırımçakça  jct  Uzbekistan  0  0  0  JCT  -  -  -  tr crh kaa azj tk gag uz-Latn ky-Latn kk-Latn ha zsm id  en  no  -  -  JUDEO-CRIMEAN TURKISH, KRIMCHAK  Altaic, Turkic, Western, Ponto-Caspian.
jic  Tol  -  jic  Honduras  2  363965  2112551  JIC  -  -  -  gur emk ext eo nak ast eml sbl lnc kao  en  no  -  Thu Dec 27 18:27:04 CST 2012  TOLPAN, JICAQUE, XICAQUE  Language Isolate.
jiv  Shuar  -  jiv  Ecuador  1084  893220  7311490  JIV  -  -  1125  acu hub agr  en es  no  -  Wed Jan 30 21:25:07 CST 2013  JIVARO, XIVARO, JIBARO, CHIWARO, SHUARA  Jivaroan.
jmc  Machame  -  jmc  Tanzania  2  147016  980868  JMC  -  -  -  old vun swh pkb wmw kki ng ki heh kde kam  en  no  -  Sat Jan 5 22:41:34 CST 2013  MACHAME, KIMASHAMI  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, E, Chaga (E.30).
jpx  Japanese (family)  日本語  jpx  Japan  0  0  0  -  j  -  -  cmn gan  en  no  -  -  -  Japanese, Japanese.
jut  Jutish  Jyske  jut  Denmark  11  7678  38014  JUT  -  -  -  nn da nb sv nl nds-NL  en da  no  -  Sat Jan 26 08:11:45 CST 2013  JUTLANDISH, JYSK, WESTERN DANISH  Indo-European, Germanic, North, East Scandinavian, Danish-Swedish, Danish-Bokmal, Danish.
jv  Javanese  Basa Jawa  jav  Indonesia (Java and Bali)  712  2820605  19492937  JAN  -  jv  jan  pam jvn tl su agn kyk krj msk ceb bjn hil  en  started  Andhika Padmawan  Tue Sep 10 11:05:28 CDT 2013  JAWA, DJAWA  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Sundic, Javanese.
jv-x-bms  Banyumasan  -  jav  Indonesia (Java and Bali)  2  458610  3535179  JAN  -  map-bms  -  id zsm ms bjn su jv  en  no  -  Sat Sep 14 09:04:33 CDT 2013  JAWA, DJAWA  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Sundic, Javanese.
jvn  Caribbean Javanese  -  jvn  Suriname  2  296772  1891338  JVN  -  -  -  jv pam tl su  en  no  -  Thu Dec 27 18:30:25 CST 2012  SURINAME JAVANESE  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Sundic, Javanese.
ka  Georgian  ქართული  kat  Georgia  1210  6754915  57150862  GEO  ge  ka  geo  xmf  en  no  Oto Magaldadze  Sun Feb 3 17:32:21 CST 2013  KARTULI, GRUZINSKI  South Caucasian, Georgian.
ka-Latn  Georgian (Latin)  -  kat  Georgia  44  221837  1720951  GEO  -  -  -  adz ha rm hwc kpr  en  no  -  Thu Jan 17 21:35:02 CST 2013  KARTULI, GRUZINSKI  South Caucasian, Georgian.
kaa  Karakalpak  Qaraqalpaqsha  kaa  Uzbekistan  230  440762  3584594  KAC  -  kaa  -  tr crh tk kk-Latn uz-Latn  en tr  no  -  Thu Jan 17 21:46:09 CST 2013  QARAQULPAQS, KARAKLOBUK, TCHORNY, KLOBOUKI  Altaic, Turkic, Western, Aralo-Caspian.
kaa-Cyrl  Karakalpak (Cyrillic)  -  kaa  Uzbekistan  549  703044  5486202  KAC  -  -  -  kk ky  en  no  -  Fri Jan 25 19:57:42 CST 2013  KARAKLOBUK, TCHORNY, KLOBOUKI  Altaic, Turkic, Western, Aralo-Caspian.
kab  Kabyle  Taqbaylit  kab  Algeria  60  552179  3469093  KYL  kby  kab  -  tzm emk tmh esk mos  en  no  Jenia Gutova  Sun Feb 3 15:31:57 CST 2013  -  Afro-Asiatic, Berber, Northern, Kabyle.
kac  Jingpho  Kachin  kac  Myanmar  11  434524  2008489  CGP  ah  -  -  bts pam iba tl jv  en  no  -  Wed Sep 18 21:35:01 CDT 2013  KACHIN, JINGHPAW, CHINGPAW, CHINGP'O, MARIP  Sino-Tibetan, Tibeto-Burman, Jingpho-Konyak-Bodo, Jingpho-Luish, Jingpho.
kam  Kamba  Kĩkamba  kam  Kenya  62  126837  815617  KIK  kb  -  -  sw ki pkb wmw kki dig nyf  en  no  -  Sun Feb 3 15:41:26 CST 2013  KIKAMBA, KEKAMBA  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, E, Kikuyu-Kamba (E.20).
kao  Xaasongaxango  -  kao  Mali  1  205025  972298  KAO  -  -  -  emk snk sus  en  no  -  Sat Jan 5 22:30:31 CST 2013  XASONGA, KASSONKE, KHASSONKA, KHASSONKÉ, KHASONKE, KASONKE, KASSON, KASSO, XAASONGA, XASONKE  Niger-Congo, Mande, Western, Central-Southwestern, Central, Manding-Jogo, Manding-Vai, Manding-Mokole, Manding, Manding-West.
kaq  Capanahua  -  kaq  Peru  3  403430  2923775  KAQ  -  -  -  shp  en es  no  -  Thu Dec 27 18:30:14 CST 2012  KAPANAWA  Panoan, North-Central.
kbc  Kadiwéu  -  kbc  Brazil  1  220305  1906335  KBC  -  -  -  chr-Latn  en  no  -  Sun Jan 6 09:34:38 CST 2013  MBAYA-GUAIKURU, CADUVÉO, EDIU-ADIG  Mataco-Guaicuru, Guaicuruan.
kbd  Kabardian  Адыгэбзэ  kbd  Russian Federation  1958  2561074  19102249  KAB  kbr  kbd  -  ady cu ru  en ru  no  -  Thu Jan 17 23:00:26 CST 2013  BESLENEI, UPPER CIRCASSIAN, EAST CIRCASSIAN, KABARDINO-CHERKES, KABARDO-CHERKES  North Caucasian, Northwest, Circassian.
kbh  Camsá  -  kbh  Colombia  2  230452  1836600  KBH  -  -  -  lue  en es  no  -  Sun Jan 6 09:46:11 CST 2013  KAMSA, COCHE, SIBUNDOY, KAMEMTXA, KAMSE, CAMËNTSËÁ  Language Isolate.
kbm  Iwal  -  kbm  Papua New Guinea  0  0  0  KBM  -  -  -  bum bhl izr  en  no  -  -  KAIWA  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Huon Gulf, South, Kaiwa.
kbp  Kabiyè  Kabɩyɛ  kbp  Togo  3  174991  1012358  KBP  kab  -  kbp  dop  en  no  -  Fri Jan 25 19:58:02 CST 2013  KABRE, CABRAI, KABURE, KABYE, CABRAIS  Niger-Congo, Atlantic-Congo, Volta-Congo, North, Gur, Central, Southern, Grusi, Eastern.
kbr  Kafa  -  kbr  Ethiopia  0  0  0  KBR  -  -  -  om enb crg wal wo gof  en  no  -  -  KAFA, KEFA, KEFFA, KAFFA, CAFFINO, MANJO  Afro-Asiatic, Omotic, North, Gonga-Gimojan, Gonga, South.
kca  Khanty  хӑнты ясӑӈ  kca  Russian Federation  1  1750  11455  KCA  -  -  -  cv ru azj-Cyrl mhr  en ru  no  Zsófia Schön  Thu Sep 12 17:28:09 CDT 2013  KHANTI, HANTY, XANTY, OSTYAK  Uralic, Finno-Ugric, Ugric, Ob Ugric.
kcc  Lubila  -  kcc  Nigeria  2  1738  9610  KCC  -  -  -  kg yaf sop kmb lua lu loz  en fr  no  -  Fri Sep 13 11:17:10 CDT 2013  LUBILO, KABILA, KABIRE, OJOR, OFOR  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Cross River, Delta Cross, Upper Cross, Central, East-West, Loko.
kck  Kalanga  Ikalanga  kck  Botswana  29  30081  165781  KCK  kl  -  -  loz lu xog  en  no  -  Wed Sep 18 21:39:24 CDT 2013  CHIKALANGA, KALAKA, SEKALAÑA, SEKALAKA  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, S, Shona (S.10).
kde  Makonde  -  kde  Tanzania  3  11105  76803  KDE  -  -  kde  heh kki wmw lue sw dig  en  no  -  Thu Jan 17 21:45:05 CST 2013  CHIMAKONDE, CHINIMAKONDE, KONDE, MATAMBWE  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, P, Yao (P.20).
kdl  Tsikimba  -  kdl  Nigeria  0  0  0  KDL  -  -  -  gnd bm ha dmn-x-bamana bwu kno ivv bba tsc haw  en  no  -  -  AGAUSHI, AUNA, KIMBA, AKIMBA, KAMBARI, KAMBERRI, KAMBERCHI  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Kainji, Western, Kambari.
kdr  Karaim  karaj tili  kdr  Lithuania  7  3069  27022  KDR  -  -  -  en  en  no  -  Mon Sep 23 11:16:06 CDT 2013  KARAITE  Altaic, Turkic, Western, Ponto-Caspian.
kea  Kabuverdianu  Kriolu  kea  Cape Verde Islands  1433  2576679  15138291  KEA  -  -  kea  pap pap-CW pt pt-CV cri oc es gl  en pt  no  José Pedro Ferreira, Waldir Pimenta  Thu Aug 22 21:29:08 CDT 2013  CABOVERDIANO, CAPE VERDE CREOLE  Creole, Portuguese based.
kek  Kekchi  Q’eqchi’  kek  Guatemala  106  1336493  8125114  KEK  gk  -  1116  ie mt  en es  no  -  Sun Feb 3 15:45:50 CST 2013  QUECCHÍ, CACCHÉ  Mayan, Quichean-Mamean, Greater Quichean, Kekchi.
ken  Kenyang  -  ken  Cameroon  1  199627  1118184  KEN  -  -  -  sbd ada  en  no  -  Sun Jan 6 07:43:29 CST 2013  NYANG, BAYANGI, BANYANG, BANYANGI, BANJANGI, MANYANG  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Mamfe.
kew  West Kewa  -  kew  Papua New Guinea  349  331319  2011307  KEW  -  -  -  kjs hag maw gri fj nfr  en  no  -  Sat Feb 16 17:50:10 CST 2013  PASUMA  Trans-New Guinea, Main Section, Central and Western, East New Guinea Highlands, West-Central, Angal-Kewa.
kez  Kukele  -  kez  Nigeria  1  169538  1129652  KEZ  -  -  -  pam jv kha dga tl  en  no  -  Sun Jan 6 07:42:58 CST 2013  UKELE, BAKELE  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Cross River, Delta Cross, Upper Cross, Central, North-South, Koring-Kukele, Kukele.
kfr-Gujr  Kachchi  કચ્છી  kfr  India  42  8616  53437  KFR  -  -  -  gu pi-Gujr  en  no  -  Mon Dec 2 19:12:48 CST 2013  KACHCHHI, KUTCHCHI, CUCHI, CUTCH, KUTCHIE, KACHI, KATCH, KAUTCHY, KATCHI  Indo-European, Indo-Iranian, Indo-Aryan, Northwestern zone, Sindhi.
kg  Kongo  Kikongo  kon  Dem. Rep. of Congo  564  759938  4621385  KON  mk  kg  -  ktu yaf kcc swh lu nym ng  en fr  started  Anderson Sunda-Meya  Sun Feb 3 16:04:35 CST 2013  KIKONGO, CONGO, KICONGO, KONGO  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, H, Kongo (H.10).
kgf  Kube  -  kgf  Papua New Guinea  287  226158  1477559  KGF  -  -  -  ded buk  en  no  -  Sat Feb 16 18:01:51 CST 2013  MONGI, HUBE  Trans-New Guinea, Main Section, Central and Western, Huon-Finisterre, Huon, Eastern.
kgk  Kaiwá  -  kgk  Brazil  1  291854  1966934  KGK  -  -  -  gn gun gnw  en  no  -  Sun Jan 6 09:36:01 CST 2013  CAIWA, CAINGUA, CAYUA, CAIUA, KAYOVA, KAIOVA  Tupi, Tupi-Guarani, Guarani (I).
kgp  Kaingang  Kaingáng  kgp  Brazil  3  395123  1603232  KGP  -  -  -  tzu  en  no  -  Wed Sep 18 21:41:45 CDT 2013  COROADO, COROADOS, CAINGANG, BUGRE  Macro-Ge, Ge-Kaingang, Kaingang, Northern.
kha  Khasi  Khasi  kha  India  136  225589  1156409  KHI  ks  -  kha  miq dyu kus lia jv bm kez  en  no  Allen Kharbteng  Wed Sep 18 21:43:27 CDT 2013  KAHASI, KHASIYAS, KHUCHIA, KASSI, KHASA, KHASHI  Austro-Asiatic, Mon-Khmer, Northern Mon-Khmer, Khasian.
khk  Halh Mongolian  -  khk  Mongolia  1  1387581  9781327  KHK  -  -  -  bua sah ky xal  en  no  Sanlig Badral  Thu Jan 24 14:39:31 CST 2013  HALH, KHALKHA MONGOLIAN, MONGOL, CENTRAL MONGOLIAN  Altaic, Mongolian, Eastern, Oirat-Khalkha, Khalkha-Buriat, Mongolian Proper.
khw  Khowar  کھوار  khw  Pakistan  148  46612  271028  KHW  -  -  -  glk az-Arab ur pes lah pnb fa lki sdh ckb  en  no  -  Mon Dec 2 19:09:37 CST 2013  KHAWAR, CHITRALI, CITRALI, CHITRARI, ARNIYA, PATU, QASHQARI, KASHKARI  Indo-European, Indo-Iranian, Indo-Aryan, Northwestern zone, Dardic, Chitral.
khz  Keapara  -  khz  Papua New Guinea  0  0  0  KHZ  -  -  -  meu ksd gri pwg stn fj bmk  en  no  -  -  KEAPARA, KEREPUNU  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Peripheral, Central Papuan, Sinagoro-Keapara.
ki  Gikuyu  Gĩkũyũ  kik  Kenya  275  440414  2878228  KIU  kq  ki  -  kam mer swh pkb ln gri wmw nyf dig fj  en  yes  Peter Waiganjo Wagacha, Guy De Pauw  Mon Dec 2 12:15:24 CST 2013  KIKUYU, GEKOYO, GIGIKUYU  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, E, Kikuyu-Kamba (E.20).
kib  Koalib  -  kib  Sudan  1  1252  6492  KIB  -  -  -  ki ig mer  en  no  -  Thu Apr 4 09:15:18 CDT 2013  KAWALIB, KOWALIB, NGIRERE, NIRERE, RERE, LGALIGE, ABRI  Niger-Congo, Kordofanian, Kordofanian Proper, Heiban, West-Central, Central, Rere.
kiu  Northern Zazaki  Zazakiyê Zımey  kiu  Turkey  42  23573  143751  QKV  -  -  -  diq mwl kmr ku lad ote oc ca-valencia es gul  en  no  -  Mon Sep 23 00:15:19 CDT 2013  ZAZA, NORTHERN ZAZA, ZAZAKI, ALEVICA, DIMILKI, DERSIMKI, SO-BÊ, ZONÊ MA  Indo-European, Indo-Iranian, Iranian, Western, Northwestern, Zaza-Gorani.
kj  Kwanyama  Oshikwanyama  kua  Angola  764  772636  5581286  KUY  ky  kj  -  ng nyk bem umb lue xog kki loz luy heh sw zu  en  no  -  Mon Dec 2 14:09:45 CST 2013  OCHIKWANYAMA, KUANYAMA, KWANJAMA, KWANCAMA, CUANHAMA, OVAMBO, HUMBA  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, R, Ndonga (R.20).
kjb  Q’anjob’al  -  kjb  Guatemala  2  945255  4913177  KJB  -  -  -  knj cac jac cnm  en  no  -  Sun Jan 6 08:02:41 CST 2013  SANTA EULALIA KANJOBAL, KANHOBAL, CONOB  Mayan, Kanjobalan-Chujean, Kanjobalan, Kanjobal-Jacaltec.
kjh  Khakas  Хакас  kjh  Russian Federation  3  7288  54593  KJH  khk  -  kjh  kk alt kaa-Cyrl  en  no  -  Wed Sep 18 21:45:41 CDT 2013  KHAKHAS, KHAKHASS, ABAKAN TATAR, YENISEI TATAR  Altaic, Turkic, Northern.
kjs  East Kewa  -  kjs  Papua New Guinea  287  274682  1728191  KJS  -  -  -  kew imo gri fj  en  no  -  Sat Feb 16 18:13:50 CST 2013  -  Trans-New Guinea, Main Section, Central and Western, East New Guinea Highlands, West-Central, Angal-Kewa.
kk  Kazakh  Қазақша  kaz  Kazakhstan  30092  41930890  335515530  KAZ  az  kk  kaz  ky ba  en  yes  Akmaral Mussayeva  Sun Feb 3 16:37:35 CST 2013  KAZAK, KAISAK, KOSACH, QAZAQ  Altaic, Turkic, Western, Aralo-Caspian.
kk-Latn  Kazakh (Latin)  -  kaz  Kazakhstan  1  4673  39160  KAZ  -  -  -  tk kaa ky-Latn  en  no  -  Mon Oct 1 22:28:14 CDT 2012  KAZAK, KAISAK, KOSACH, QAZAQ  Altaic, Turkic, Western, Aralo-Caspian.
kkc  Odoodee  -  kkc  Papua New Guinea  0  0  0  KKC  -  -  -  son pao so mnk man  en  no  -  -  KALAMO, NOMAD, TOMU, TOMU RIVER, ODODEI  Trans-New Guinea, Main Section, Central and Western, Central and South New Guinea-Kutubuan, Central and South New Guinea, East Strickland.
kki  Kagulu  -  kki  Tanzania  1  125478  927890  KKI  -  -  -  gog wmw sw suk nym dig lue  en  no  -  Sun Jan 6 08:16:15 CST 2013  CHIKAGULU, KAGURU, NORTHERN SAGARA, KININGO, WETUMBA, SOLWA, MANGAHERI  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, G, Gogo (G.10).
kkj  Kako  -  kkj  Cameroon  1  263271  1265818  KKJ  -  -  -  tzh  en  no  -  Sun Jan 6 08:15:54 CST 2013  YAKA, KAKA, NKOXO, DIKAKA, MKAKO  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Northwest, A, Kako (A.90).
kkz  Kaska  -  kkz  Canada  0  0  0  KKZ  -  -  -  caf  en  no  -  -  CASKA, EASTERN NAHANE, NAHANE, NAHANI  Na-Dene, Nuclear Na-Dene, Athapaskan-Eyak, Athapaskan, Tahltan-Kaska.
kl  Kalaallisut  Kalaallisut  kal  Greenland  1170  767730  7639488  ESG  gl  kl  esg  iu-Latn esi esu ik fi  en da  no  -  Mon Feb 4 10:02:15 CST 2013  GREENLANDIC ESKIMO, GREENLANDIC, KALAALLISUT  Eskimo-Aleut, Eskimo, Inuit.
kld  Kamilaroi  Gamilaraay  kld  Australia  5  5083  37254  KLD  -  -  -  tiw  en  started  -  Thu Jan 17 22:11:06 CST 2013  CAMILEROI, GAMILARAAY, GAMILAROI  Australian, Pama-Nyungan, Wiradhuric.
kln  Kalenjin  Kalenjin  kln  Kenya  77  365943  2608141  KLN  kj  -  -  ain  en  no  -  Thu Jan 24 11:20:45 CST 2013  -  Nilo-Saharan, Eastern Sudanic, Nilotic, Southern, Kalenjin, Nandi-Markweta, Nandi.
km  Khmer  ខ្មែរ  khm  Cambodia  2396  2092998  29223451  KMR  cb  km  kmr  -  en  yes  -  Sun Feb 3 16:22:14 CST 2013  KHMER, CAMBODIAN  Austro-Asiatic, Mon-Khmer, Eastern Mon-Khmer, Khmer.
kma  Konni  -  kma  Ghana  1  229941  1110818  KMA  -  -  -  biv cme  en  no  -  Mon Jan 7 13:30:51 CST 2013  KONI, KOMA, KOMUNG  Niger-Congo, Atlantic-Congo, Volta-Congo, North, Gur, Central, Northern, Oti-Volta, Buli-Koma.
kmb  Kimbundu  Kimbundu  kmb  Angola  6  21346  117025  MLO  kim  -  009  lch kcc sop yaf lua lun  en  no  -  Fri Sep 13 14:12:50 CDT 2013  LUANDA, LUNDA, LOANDE, KIMBUNDU, KIMBUNDO, NORTH MBUNDU, NBUNDU, N'BUNDO, DONGO, NDONGO, KINDONGO  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, H, Mbundu (H.20).
kmg  Kâte  -  kmg  Papua New Guinea  239  157239  1056410  KMG  -  -  -  kgf bon aso ded  en  no  -  Sun Feb 17 19:48:38 CST 2013  KAI, KÂTE DONG  Trans-New Guinea, Main Section, Central and Western, Huon-Finisterre, Huon, Eastern.
kmh  Kalam  -  kmh  Papua New Guinea  0  0  0  KMH  -  -  -  kmh-x-mini zlm fai daa bmu bbr  en  no  -  -  AFORO, KARAM  Trans-New Guinea, Main Section, Central and Western, East New Guinea Highlands, Kalam, Kalam-Kobon.
kmh-x-mini  Minimib  -  kmh  Papua New Guinea  0  0  0  KMH  -  -  -  avt zlm gdr usp  en  no  -  -  AFORO, KARAM  Trans-New Guinea, Main Section, Central and Western, East New Guinea Highlands, Kalam, Kalam-Kobon.
kmo  Kwoma  -  kmo  Papua New Guinea  0  0  0  KMO  -  -  -  tbo swh pwg sbe ign alu ha dww  en  no  -  -  WASHKUK  Sepik-Ramu, Sepik, Middle Sepik, Nukuma.
kmr  Northern Kurdish  Kurdî  kmr  Kurdistan  1333  4324556  25369364  KUR  rd  ku  kdb1  tr diq az zza jam li  en tr  yes  Erdal Ronahi, Rêzan Tovjîn  Sun Feb 3 16:22:50 CST 2013  KURDI, NORTHERN KURDISH, KERMANJI, KIRMANJI, KIRDASI, KIRMÂNCHA, BÂHDINÂNI, KURMANJI  Indo-European, Indo-Iranian, Iranian, Western, Northwestern, Kurdish.
kms  Kamasau  -  kms  Papua New Guinea  286  350620  1789782  KMS  -  -  -  nii imo mbt ubu-x-nopenge ubu ubu-x-kala yap myk  en  no  -  Mon Dec 9 14:23:55 CST 2013  WAND TUAN  Torricelli, Marienberg.
kmu  Kanite  -  kmu  Papua New Guinea  0  0  0  KMU  -  -  -  ino for viv swh knv sgb dww mnb  en  no  -  -  -  Trans-New Guinea, Main Section, Central and Western, East New Guinea Highlands, East-Central, Kamano-Yagaria.
kmz  Khorasani Turkish  Turki Khorasani  kmz  Iran  3  1098  9667  KMZ  -  -  -  en  en  no  -  Mon Dec 2 10:37:06 CST 2013  QUCHANI  Altaic, Turkic, Southern, Turkish.
kmz-Arab  Khorasani Turkish  -  kmz  Iran  0  0  0  KMZ  -  -  -  az-Arab lki azb-Arab fa ckb pes  en  no  -  -  QUCHANI  Altaic, Turkic, Southern, Turkish.
kn  Kannada  ಕನ್ನಡ  kan  India  11322  22779287  177835756  KJV  ka*  kn  kjv  pi-Knda  en  yes  Pranava Swaroop Madhyastha  Fri Sep 13 14:23:18 CDT 2013  KANARESE, CANARESE, BANGLORI, MADRASSI  Dravidian, Southern, Tamil-Kannada, Kannada.
kn-Latn  Kannada (Latin)  -  kan  India  67  98981  750214  KJV  -  -  -  ptu gri son heh  en  no  -  Sun Feb 17 20:26:28 CST 2013  KANARESE, CANARESE, BANGLORI, MADRASSI  Dravidian, Southern, Tamil-Kannada, Kannada.
knc  Central Kanuri  -  knc  Nigeria  1  1421  10649  KPH  -  -  kph  ha swb  en  no  -  Wed Jan 30 18:26:51 CST 2013  YERWA KANURI, KANOURI, BERIBERI, BORNU, KANOURY  Nilo-Saharan, Saharan, Western, Kanuri.
kne  Kankanaey  -  kne  Philippines  1  180901  997104  KNE  -  -  -  sbl ifb ifk pag iry  en  no  -  Sun Jan 6 08:25:00 CST 2013  CENTRAL KANKANAEY, KANKANAI, KANKANAY  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Northern Philippine, Northern Luzon, South-Central Cordilleran, Central Cordilleran, Nuclear Cordilleran, Bontok-Kankanay, Kankanay.
kng  Koongo  Kikongo  kng  Dem. Rep. of Congo  17  141669  819889  KON  kg  kg  kon  ktu yaf kcc lu sw  en fr  started  Anderson Sunda-Meya  Wed Jan 30 21:13:42 CST 2013  KIKONGO, CONGO, KICONGO, KONGO  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, H, Kongo (H.10).
knj  Akateko  -  knj  Guatemala  2  339335  1692349  KNJ  -  -  -  jac  en es  no  -  Thu Dec 27 18:33:54 CST 2012  ACATECO, ACATEC, SAN MIGUEL ACATÁN KANJOBAL, CONOB  Mayan, Kanjobalan-Chujean, Kanjobalan, Kanjobal-Jacaltec.
knk  Kuranko  -  knk  Sierra Leone  1  216477  1033770  KHA  -  -  -  emk bm dyu kno  en  no  -  Sun Jan 6 09:04:25 CST 2013  KORANKO  Niger-Congo, Mande, Western, Central-Southwestern, Central, Manding-Jogo, Manding-Vai, Manding-Mokole, Mokole.
kno  Kono  -  kno  Sierra Leone  1  340459  1340356  KNO  -  -  -  lus dgi knk bm biv maf  en  no  -  Sun Jan 6 09:04:10 CST 2013  KONNOH  Niger-Congo, Mande, Western, Central-Southwestern, Central, Manding-Jogo, Manding-Vai, Vai-Kono.
knv  Tabo  -  knv  Papua New Guinea  5  18986  148448  KNV  -  -  -  snp xla tte mpt for  en  no  -  Sat Jan 19 10:33:33 CST 2013  WAIA, KENEDIBI, KAWAKARUBI, TAKALUBI, TAKARUBI, HIWI, HIBARADAI  Trans-New Guinea, Trans-Fly-Bulaka River, Trans-Fly, Waia.
knv-x-ara  Tabo (Aramia River)  -  knv  Papua New Guinea  290  332016  2546478  KNV  -  -  -  knv-x-fly  en  no  -  Tue Sep 17 12:44:18 CDT 2013  WAIA, KENEDIBI, KAWAKARUBI, TAKALUBI, TAKARUBI, HIWI, HIBARADAI  Trans-New Guinea, Trans-Fly-Bulaka River, Trans-Fly, Waia.
knv-x-fly  Tabo (Fly River)  -  knv  Papua New Guinea  290  333254  2526524  KNV  -  -  -  knv-x-ara  en  no  -  Tue Sep 17 12:46:58 CDT 2013  WAIA, KENEDIBI, KAWAKARUBI, TAKALUBI, TAKARUBI, HIWI, HIBARADAI  Trans-New Guinea, Trans-Fly-Bulaka River, Trans-Fly, Waia.
ko  Korean  한국어  kor  Korea  4596  5537601  28466326  KKN  ko  ko  kkn  -  en  yes  -  Sun Feb 3 17:37:07 CST 2013  HANGUOHUA, HANGUK MAL  Language Isolate.
kog  Kogi  -  kog  Colombia  1  458  3235  KOG  -  -  -  amu ln fj gri stp  en es  no  -  Sun Apr 14 20:00:47 CDT 2013  KOGUI, COGHUI, KOGI, KAGABA, KAGGABA, COGUI  Chibchan, Aruak.
koi  Komi-Permyak  Перем Коми  koi  Russian Federation  2  216467  1563549  KOI  -  koi  koi*  kpv mhr mrj ky udm ru  en ru  no  Niko Partanen  Fri Sep 13 11:18:52 CDT 2013  PERMYAK, KOMI-PERMYAT, KAMA PERMYAK, KOMI-PERM  Uralic, Finno-Ugric, Finno-Permic, Permic.
kok-Latn  Konkani  Konknni  kok  India  510  735658  5123511  -  kt  -  -  bn-Latn  en  no  -  Thu Jan 24 11:33:34 CST 2013  KONKAN STANDARD, BANKOTI, KUNABI, NORTH KONKAN, CENTRAL KONKAN, CONCORINUM, CUGANI, KONKANESE  Indo-European, Indo-Iranian, Indo-Aryan, Southern zone, Konkani.
koo  Konzo  -  koo  Uganda  64  93258  768517  KOO  lhk  -  koo1  ttj nnb nyo nyn lg  en  no  -  Sun Feb 3 16:39:50 CST 2013  RUKONJO, OLUKONJO, KONJO, OLUKONZO, LHUKONZO  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, J, Konzo (J.40).
kos  Kosraean  -  kos  Micronesia  2  22974  122529  KSI  os  -  -  vap din yi-Latn hus  en  no  -  Sat Jan 19 11:39:54 CST 2013  KUSAIE, KOSRAE  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Micronesian, Micronesian Proper, Kusaiean.
kpe  Kpelle  -  kpe  Guinea  2  4374  22825  -  -  -  gkp1  sbd  en  no  -  Sat Jan 19 11:43:41 CST 2013  KPELE, GUERZE, GERZE, GERSE, GBESE, PESSA, PESSY, KPWESSI, AKPESE, KPELESE, KPELESETINA, KPESE, KPERESE, NORTHERN KPELE  Niger-Congo, Mande, Western, Central-Southwestern, Southwestern, Kpelle.
kpf  Komba  -  kpf  Papua New Guinea  0  0  0  KPF  -  -  -  stl nl act sdz  en  no  -  -  -  Trans-New Guinea, Main Section, Central and Western, Huon-Finisterre, Huon, Western.
kpj  Karajá  -  kpj  Brazil  1  155526  1180084  KPJ  -  -  -  iso ckk  en  no  -  Sun Jan 6 21:42:26 CST 2013  XAMBIOÁ, CHAMBOA, YNÃ  Macro-Ge, Karaja.
kpr  Korafe-Yegha  -  kpr  Papua New Guinea  277  643897  4058748  KPR  -  -  -  ka-Latn ha  en  no  -  Fri Jan 25 19:58:58 CST 2013  KORAPE, KORAFI, KWARAFE, KAILIKAILI  Trans-New Guinea, Main Section, Eastern, Binanderean, Binanderean Proper.
kpv  Komi-Zyrian  -  kpv  Russian Federation  1747  1170146  8457293  KPV  -  kv  -  koi ky mrj mhr udm ru  en ru  yes  Niko Partanen  Fri Jan 25 20:22:00 CST 2013  KOMI  Uralic, Finno-Ugric, Finno-Permic, Permic.
kpw  Kobon  -  kpw  Papua New Guinea  0  0  0  KPW  -  -  -  kmh-x-mini kto son bku avt  en  no  -  -  -  Trans-New Guinea, Main Section, Central and Western, East New Guinea Highlands, Kalam, Kalam-Kobon.
kpx  Mountain Koiali  -  kpx  Papua New Guinea  0  0  0  KPX  -  -  -  tgp fud haw fj twu hif nak niu tkl st bgt  en  no  -  -  MOUNTAIN KOIARI  Trans-New Guinea, Main Section, Eastern, Central and Southeastern, Koiarian, Koiaric.
kpy  Koryak  Нымылан  kpy  Russian Federation  2  442  4011  KPY  -  -  -  alr ckt chm mhr mrj udm koi ky  en  no  -  Wed Sep 18 21:47:22 CDT 2013  NYMYLAN  Chukotko-Kamchatkan, Northern, Koryak-Alyutor.
kqc  Doromu-Koki  -  kqc  Papua New Guinea  0  0  0  KQC  -  -  -  aui pwg bmk fj viv dob  en  no  -  -  DORAM, DOROMU  Trans-New Guinea, Main Section, Eastern, Central and Southeastern, Manubaran.
kqf  Kakabai  -  kqf  Papua New Guinea  0  0  0  KQF  -  -  -  dob aui dww viv sbe pwg mox mpx bmk meu  en  no  -  -  IGORA  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Nuclear, North Papuan Mainland-D'Entrecasteaux, Kakabai.
kqn  Kaonde  Kikaonde  kqn  Zambia  13  84466  584466  KQN  kd  -  kqn  lu bem lua sop toi  en  no  -  Sun Feb 3 19:19:34 CST 2013  CHIKAONDE, CHIKAHONDE, KAWONDE, LUBA KAONDE  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, L, Kaonde (L.40).
kqp  Kimré  -  kqp  Chad  1  254419  1121808  KQP  -  -  -  srn blz nl  en  no  -  Sun Jan 6 09:03:41 CST 2013  GABRI-KIMRÉ  Afro-Asiatic, Chadic, East, A, A.2, 1.
kqw  Kandas  -  kqw  Papua New Guinea  0  0  0  KQW  -  -  -  ksd gfk bnp due sus dgc srr snk  en  no  -  -  KING  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, South New Ireland-Northwest Solomonic, Patpatar-Tolai.
kr  Kanuri  Kanuri  kau  Nigeria  2  2754  20742  -  -  kr  kph  ha swb  en  no  -  Tue Jan 29 22:44:04 CST 2013  YERWA KANURI, KANOURI, BERIBERI, BORNU, KANOURY  Nilo-Saharan, Saharan, Western, Kanuri.
krc  Karachay-Balkar  Къарачай-Малкъар  krc  Russian Federation  3  264453  2012194  KRC  bal  krc  -  kum kaa-Cyrl dar ky  en  no  -  Fri Jan 25 20:22:00 CST 2013  KARACHAY, KARACHAI, KARACHAYLA, KARACHAITSY, KARACAYLAR  Altaic, Turkic, Western, Ponto-Caspian.
kri  Krio  Krio  kri  Sierra Leone  12  262678  1075830  KRI  -  -  kri  jam  en  no  -  Wed Sep 18 21:48:25 CDT 2013  CREOLE, PATOIS  Creole, English based, Atlantic, Krio.
krj  Kinaray-a  Kinaray-a  krj  Philippines  14  240395  1439428  KRJ  knr  -  -  hil ceb tl kyk akl hnn msk bik  en  no  -  Wed Sep 18 21:49:35 CDT 2013  HINARAY-A, KINIRAY-A, KARAY-A, ANTIQUEÑO, HAMTIKNON, SULUD, ATI, PANAYANO  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Meso Philippine, Central Philippine, Bisayan, West, Kinarayan.
krl  Karelian  Karjalan kieli  krl  Russian Federation  66  56086  486327  KRL  -  -  krl  fi vep ekk stl rm hwc nl ha eu  en fi  no  -  Wed Sep 18 21:50:46 CDT 2013  KARELY, KARELIAN PROPER, SOBSTVENNO-KAREL'SKIJ-JAZYK, SEVERNO-KAREL'SKIJ, KAREL'SKOGO JAZYKA  Uralic, Finno-Ugric, Finno-Permic, Finno-Cheremisic, Finno-Mordvinic, Finno-Lappic, Baltic-Finnic.
ks  Kashmiri  -  kas  India  2  1113  7036  KSH  -  ks  ksh*  mai ne mr npi hi  en  no  -  Fri Sep 13 11:19:18 CDT 2013  KESHUR, KASCHEMIRI, CASHMIRI, CASHMEEREE, KACMIRI  Indo-European, Indo-Iranian, Indo-Aryan, Northwestern zone, Dardic, Kashmiri.
ksd  Kuanua  Kuanua  ksd  Papua New Guinea  1102  1297722  6262091  KSD  -  -  -  stn bnp meu fj pwg gri alu bmk kwf  en  no  -  Fri Sep 13 14:14:52 CDT 2013  TOLAI, GUNANTUNA, TINATA TUNA, TUNA, BLANCHE BAY, NEW BRITAIN LANGUAGE  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, South New Ireland-Northwest Solomonic, Patpatar-Tolai.
ksf  Bafia  -  ksf  Cameroon  4  533  3366  KSF  -  -  -  mua zsm naf son id bjn cak yut ifk  en  no  -  Mon Sep 23 00:10:57 CDT 2013  RIKPA, LEFA', RIPEY, RIKPA', BEKPAK  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Northwest, A, Bafia (A.50).
ksh  Kölsch  Ripoarisch  ksh  Germany  2  160675  978149  KOR  -  ksh  -  nds pdc gsw pfl lb li de  en de  no  -  Sat Jan 19 11:47:16 CST 2013  RIPUARIAN, RIPOARISCH  Indo-European, Germanic, West, High German, German, Middle German, West Middle German, Ripuarian Franconian.
ksr  Borong  -  ksr  Papua New Guinea  0  0  0  KSR  -  -  -  nop mnk man lia mnb ubu-x-andale son adh  en  no  -  -  NAAMA  Trans-New Guinea, Main Section, Central and Western, Huon-Finisterre, Huon, Eastern.
ksw  S’gaw Karen  -  ksw  Myanmar  40  15472  187164  KSW  kr*  -  ksw*  my pi-Mymr  en  no  -  Sun Sep 15 20:58:57 CDT 2013  S'GAW, S'GAU, S'GAW KAYIN, KANYAW, PAGANYAW, PWAKANYAW, WHITE KAREN, BURMESE KAREN, YANG KHAO, PCHCKNYA, KYETHO  Sino-Tibetan, Tibeto-Burman, Karen, Sgaw-Bghai, Sgaw.
ktj  Plapo Krumen  -  ktj  Côte d’Ivoire  5  75410  340024  KTJ  -  -  -  dgi biv bib kno  en  no  -  Sun Jan 13 21:54:27 CST 2013  PLAPO  Niger-Congo, Atlantic-Congo, Volta-Congo, Kru, Western, Grebo, Ivoirian.
kto  Kuot  -  kto  Papua New Guinea  290  353054  1969705  KTO  -  -  -  pam mmx lcm tl gur agn ksd  en  no  -  Sun Feb 17 20:20:30 CST 2013  KUAT, PANARAS  East Papuan, Yele-Solomons-New Britain, New Britain, Kuot.
ktu  Kituba  -  ktu  Dem. Rep. of Congo  6  50943  287750  KTU  -  -  ktu  kng ln nym  en  no  -  Sat Jan 19 11:49:31 CST 2013  KIKONGO-KUTUBA, KIKONGO SIMPLIFIÉ, KIKONGO YA LETA, KILETA, KIKONGO COMMERCIAL, KIBULAMATADI  Creole, Kongo based.
ku  Kurdish  Kurdî  kur  Kurdistan  273  2129317  12385577  -  rd  ku  -  tr  en tr  yes  Erdal Ronahi, Rêzan Tovjîn  Fri Jan 18 21:40:09 CST 2013  KURDI, NORTHERN KURDISH, KERMANJI, KIRMANJI, KIRDASI, KIRMÂNCHA, BÂHDINÂNI, KURMANJI  Indo-European, Indo-Iranian, Iranian, Western, Northwestern, Kurdish.
ku-Arab  Kurdish (Arabic)  -  kur  Iraq  0  0  0  -  rda*  -  -  lki pes bal  en  no  Sahand T.  -  KURDI, SORANI  Indo-European, Indo-Iranian, Iranian, Western, Northwestern, Kurdish
kub  Kutep  -  kub  Nigeria  1  267975  1225523  KUB  -  -  -  zh-Latn cmn-Latn fil tl  en  no  -  Sun Jan 6 15:53:36 CST 2013  KUTEB, KUTEV, MBARIKE, ZUMPER, 'JOMPRE', ATI  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Platoid, Benue, Jukunoid, Yukuben-Kuteb.
kud  ’Auhelawa  -  kud  Papua New Guinea  0  0  0  KUD  -  -  -  dob viv sbe pwg aui mox kqf bdd bmk mpx meu tbo dww gri khz  en  no  -  -  NUAKATA, KURADA, 'URADA  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Nuclear, Suauic.
kue  Kuman  -  kue  Papua New Guinea  287  545800  3258357  KUE  -  -  -  kwn  en  no  -  Fri Jan 25 20:30:38 CST 2013  CHIMBU, SIMBU  Trans-New Guinea, Main Section, Central and Western, East New Guinea Highlands, Central, Chimbu.
kum  Kumyk  Къумукъ  kum  Russian Federation  3  146521  1022441  KSK  kmk  -  -  krc kaa-Cyrl ky  en  no  -  Wed Sep 18 21:52:59 CDT 2013  KUMUK, KUMUKLAR, KUMYKI  Altaic, Turkic, Western, Ponto-Caspian.
kup  Kunimaipa  -  kup  Papua New Guinea  0  0  0  KUP  -  -  -  opm bjn gfk nij slm  en  no  -  -  -  Trans-New Guinea, Main Section, Eastern, Central and Southeastern, Goilalan, Kunimaipa.
kus  Kusaal  -  kus  Ghana  2  201023  935271  KUS  -  -  -  dyu bm hag  en  no  -  Sun Jan 6 16:04:53 CST 2013  KUSALE, KUSASI  Niger-Congo, Atlantic-Congo, Volta-Congo, North, Gur, Central, Northern, Oti-Volta, Western, Southeast, Kusaal.
kut  Kutenai  Ktunaxa  kut  Canada  0  0  0  KUN  -  -  -  sum noo lkt  en  no  -  -  KTUNAXA, KOOTENAI, KOOTENAY  Language Isolate.
kv  Komi  Коми  kom  Russian Federation  788  470559  3466348  -  km*  kv  -  mhr mrj ky udm ru  en ru  no  Niko Partanen  Sat Jan 19 12:39:50 CST 2013  KOMI  Uralic, Finno-Ugric, Finno-Permic, Permic.
kvn  Border Kuna  -  kvn  Colombia  4  358021  2930799  KUA  -  -  -  cuk hsf hus hva eml ga-Latg gvf  en  no  -  Thu Dec 27 18:37:41 CST 2012  COLOMBIA CUNA, CAIMAN NUEVO, CUNA, PAYA-PUCURO  Chibchan, Kuna.
kw  Cornish  Kernewek  cor  United Kingdom  831  1372856  8601696  CRN  -  kw  -  br-x-falhuneg yol gd br ga-Latg cy  en  no  Paul Bowden, Edi Werner, John Gillingham  Sun Sep 29 16:00:03 CDT 2013  KERNOWEK, KERNEWEK, CURNOACK  Indo-European, Celtic, Insular, Brythonic.
kw-kkcor  Common Cornish  Kernewek Kemmyn  cor  United Kingdom  5  61010  354408  CRN  -  -  -  kw-x-mod kw-uccor  en  started  Paul Bowden, Edi Werner  Wed Sep 11 12:47:48 CDT 2013  KERNOWEK, KERNEWEK, CURNOACK  Indo-European, Celtic, Insular, Brythonic.
kw-uccor  Unified Cornish  Kernewek Unyes  cor  United Kingdom  77  68538  424056  CRN  -  -  -  kw-kkcor kw-x-mod  en  no  Paul Bowden, Edi Werner  Mon Jan 21 21:44:17 CST 2013  KERNOWEK, KERNEWEK, CURNOACK  Indo-European, Celtic, Insular, Brythonic.
kw-x-mod  Modern Cornish  Kernûak Nowedga  cor  United Kingdom  1  9903  57047  CRN  -  -  -  kw-kkcor kw-uccor  en  no  Paul Bowden, Edi Werner  Tue Sep 10 13:48:23 CDT 2013  KERNOWEK, KERNEWEK, CURNOACK  Indo-European, Celtic, Insular, Brythonic.
kwf  Kwara’ae  Kwara’ae  kwf  Solomon Islands  2  306412  1627035  KWF  kw  -  -  mlu stn lcm aia  en  no  -  Fri Jan 25 20:31:36 CST 2013  FIU  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Southeast Solomonic, Malaita-San Cristobal, Malaita, Northern.
kwi  Awa-Cuaiquer  -  kwi  Colombia  3  247831  1727338  KWI  -  -  kwi  ain ppl soq mti sw ha wmw  en  no  -  Wed Jan 30 15:36:11 CST 2013  COAIQUER, QUAIQUER, KWAIKER, AWA, AWA PIT, CUAIQUER  Barbacoan, Pasto.
kwj  Kwanga  -  kwj  Papua New Guinea  0  0  0  KWJ  -  -  -  lgg mhi tsc sw ts swh dig zne gux swc tsz pkb  en  no  -  -  Gawanga, Kawanga  Sepik, Nukuma.
kwk  Kwakiutl  Kwak̕wala  kwk  Canada  0  0  0  KWK  -  -  -  rm ha krl ka-Latn iry adz  en  no  -  -  KWAGIUTL, KWAK'WALA  Wakashan, Northern.
kwn  Kwangali  Rukwangali  kwn  Namibia  27  35889  262541  KWN  wg  -  -  hz sn tum  en  no  -  Mon Feb 4 09:41:45 CST 2013  SIKWANGALI, RUKWANGALI, KWANGARI, KWANGARE  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, K, Kwangwa (K.40).
kxm  Northern Khmer  -  kxm  Thailand  1  220631  1241012  KXM  -  -  -  th  en th  no  -  Sun Jan 6 15:54:04 CST 2013  -  Austro-Asiatic, Mon-Khmer, Eastern Mon-Khmer, Khmer.
kxx  Likuba  -  kxx  Congo  2  16273  104938  KXX  -  -  -  lu lua kmb lun yaf  en  no  -  Wed Mar 13 21:44:55 CDT 2013  KUBA  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Northwest, C, Mbosi (C.30).
ky  Kirghiz  Кыргыз  kir  Kyrgyzstan  495  1275390  10028337  KDO  kz  ky  kdo  kaa-Cyrl alt kk tt  en  yes  Ilyas Bakirov  Mon Feb 4 10:18:26 CST 2013  KARA-KIRGIZ, KIRGIZ, KYRGYZ  Altaic, Turkic, Western, Aralo-Caspian.
ky-Latn  Kirghiz (Latin)  -  kir  Kyrgyzstan  0  0  0  KDO  -  -  -  kk-Latn tk kaa uz-Latn  en  no  -  -  KARA-KIRGIZ, KIRGIZ  Altaic, Turkic, Western, Aralo-Caspian.
kyc  Kyaka  -  kyc  Papua New Guinea  77  300937  1972816  KYC  -  -  -  enq ipi sw wmw dig old tte  en  no  -  Mon Sep 23 10:03:11 CDT 2013  BAIYER, ENGA-KYAKA  Trans-New Guinea, Main Section, Central and Western, East New Guinea Highlands, West-Central, Enga.
kyg  Keyagana  -  kyg  Papua New Guinea  0  0  0  KYG  -  -  -  ino kmu mnb amm knv bef udu knv-x-ara tgp for  en  no  -  -  KEIGANA, KEIAGANA, KE'YAGANA  Trans-New Guinea, Main Section, Central and Western, East New Guinea Highlands, East-Central, Kamano-Yagaria.
kyh  Karok  Karuk  kyh  USA  2  2832  22269  KYH  -  -  -  sn  en  no  -  Sat Jan 19 18:29:09 CST 2013  KARUK  Hokan, Northern, Karok-Shasta.
kyk  Kamayo  -  kyk  Philippines  0  0  0  KYK  kmy  -  -  tl krj hil ceb pam bik jv  en  no  -  -  -  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Meso Philippine, Central Philippine, Mansakan, Northern.
kyq  Kenga  -  kyq  Chad  1  247495  1249057  KYQ  -  -  -  bim xsm  en  no  -  Sun Jan 6 16:20:24 CST 2013  KENGE, CENGE  Nilo-Saharan, Central Sudanic, West, Bongo-Bagirmi, Sara-Bagirmi, Bagirmi.
kyu  Western Kayah  -  kyu  Myanmar  21  285021  2175120  KYU  -  -  -  -  en  no  -  Sun Jan 6 22:08:47 CST 2013  KAYAH LI, KARENNI, KARENNYI, RED KAREN, YANG DAENG, KARIENG DAENG  Sino-Tibetan, Tibeto-Burman, Karen, Sgaw-Bghai, Kayah.
kyz  Kayabí  -  kyz  Brazil  1  355766  2205492  KYZ  -  -  -  pah mi rar zne znd gui gnw kgk tkl  en  no  -  Sun Jan 6 22:11:08 CST 2013  KAJABÍ, CAIABI, PARUA, MAQUIRI  Tupi, Tupi-Guarani, Kayabi-Arawete (V).
kze  Kosena  -  kze  Papua New Guinea  0  0  0  KZE  -  -  -  auy bmk pwg for usa  en  no  -  -  -  Trans-New Guinea, Main Section, Central and Western, East New Guinea Highlands, Eastern, Gadsup-Auyana-Awa.
kzf  Da’a Kaili  -  kzf  Indonesia (Sulawesi)  5  247343  1614299  KZF  -  -  -  pmf mvp  en  no  -  Fri Jan 25 20:32:01 CST 2013  DA'A, BUNGGU  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Sulawesi, Central Sulawesi, West Central, Kaili-Pamona, Kaili.
kzi  Kelabit  -  kzi  Malaysia (Sarawak)  3  2530  14441  KZI  -  -  -  jv-x-bms su zsm bjn id  en  no  Suhaila Saee  Sat Jan 19 12:10:43 CST 2013  KALABIT, KERABIT  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Borneo, Northwest, North Sarawakan, Dayic, Kelabitic.
la  Latin  Lingua Latina  lat  Vatican State  3276  20694789  143228526  LTN  -  la  ltn  fr pt ia it sc  en  yes  -  Wed Jan 30 20:19:23 CST 2013  LATINA  Indo-European, Italic, Latino-Faliscan.
lac  Lacandon  -  lac  Mexico  5  466746  2420725  LAC  -  -  -  mop chf yua ixl ixi acc hva ctu quj tiv jac knj cbr  en  no  -  Thu Dec 27 18:55:16 CST 2012  -  Mayan, Yucatecan, Yucatec-Lacandon.
lad  Ladino  Dzhudezmo  lad  Israel  5  265048  1582777  SPJ  -  lad  lad  es gl pt ca cbk  en es  no  Carlos Manuel Colina  Wed Jan 30 20:40:10 CST 2013  JUDEO SPANISH, SEFARDI, DZHUDEZMO, JUDEZMO, SPANYOL, HAQUETIYA  Indo-European, Italic, Romance, Italo-Western, Western, Gallo-Iberian, Ibero-Romance, West Iberian, Castilian.
lag  Langi  Kɨlaangi  lag  Tanzania  2  15535  108161  LAG  -  -  -  fj om stn aia ki  en sw  started  Oliver Stegen  Sat Jan 19 12:11:36 CST 2013  KILANGI, IRANGI, LANGI, RANGI  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, F, Nyilamba-Langi (F.30).
lah  Lahnda  -  lah  Pakistan  593  1193492  6191962  -  -  -  -  ur glk az-Arab pes  en  no  -  Thu Jan 24 14:15:13 CST 2013  LAHANDA, LAHNDI  Indo-European, Indo-Iranian, Indo-Aryan, Northwestern zone, Lahnda.
lam  Lamba  -  lam  Zambia  137  140074  1034943  LAB  -  -  -  bem lu kqn xog toi nyy loz  en  no  -  Sun Feb 17 12:10:41 CST 2013  ICHILAMBA, CHILAMBA  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, M, Bisa-Lamba (M.50), Lamba.
las  Lama  -  las  Togo  1  219600  1044800  LAS  -  -  -  dop ln fj amu gri ki  en  no  -  Sun Jan 6 16:19:50 CST 2013  LAMBA, LOSSO  Niger-Congo, Atlantic-Congo, Volta-Congo, North, Gur, Central, Southern, Grusi, Eastern.
lb  Luxembourgeois  Lëtzebuergesch  ltz  Luxembourg  425  4056583  26814045  LUX  lx  lb  lux  nds de nl pdc fy  en de  yes  Michel Weimerskirch  Fri Jan 18 21:40:03 CST 2013  LUXEMBURGISH, LUXEMBURGIAN, LUXEMBOURGISH, LETZBURGISCH, LËTZEBUERGESCH, MOSELLE FRANCONIAN, FRANKISH  Indo-European, Germanic, West, High German, German, Middle German, Moselle Franconian.
lbb  Label  -  lbb  Papua New Guinea  0  0  0  LBB  -  -  -  lcm kqw pam bnp ksd gfk hla kto su jv  en  no  -  -  -  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, South New Ireland-Northwest Solomonic, Patpatar-Tolai.
lbe  Lak  Лак  lbe  Russian Federation  249  461938  3760124  LBE  lak  lbe  -  lez tg tab agx ce uzn kum av cv dar sah  en  no  -  Mon Dec 9 14:55:21 CST 2013  LAKI, KAZIKUMUKHTSY  North Caucasian, Northeast, Lak-Dargwa.
lch  Lucazi  -  lch  Angola  1  8029  45227  LCH  lc  -  -  nba kmb tsc ts cri lue  en  no  -  Sat Jan 19 12:14:38 CST 2013  CHILUCHAZI, LUJAZI, LUJASH, LUTSHASE, LUXAGE, LUCHAZI, LUTCHAZ, PONDA  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, K, Chokwe-Luchazi (K.20).
lcm  Tungag  -  lcm  Papua New Guinea  326  442677  2321967  LCM  -  -  -  pam agn bik tl su kyk  en  no  -  Fri Dec 28 20:56:41 CST 2012  TUNGAK, LAVONGAI, LAVANGAI, DANG  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, Lavongai-Nalik.
lee  Lyélé  -  lee  Burkina Faso  2  251289  1116128  LEE  -  -  -  yam  en  no  -  Sun Jan 6 16:51:58 CST 2013  LELE  Niger-Congo, Atlantic-Congo, Volta-Congo, North, Gur, Central, Southern, Grusi, Northern.
lef  Lelemi  -  lef  Ghana  1  202017  1126461  LEF  -  -  -  fj gri ln dig  en  no  -  Mon Jan 7 09:30:17 CST 2013  LEFANA, LAFANA, BUEM  Niger-Congo, Atlantic-Congo, Volta-Congo, Kwa, Nyo, Potou-Tano, Lelemi, Lelemi-Akpafu.
lem  Nomaande  -  lem  Cameroon  1  249341  1392553  LEM  -  -  -  anv bss  en  no  -  Mon Jan 7 13:31:09 CST 2013  NOOMAANTE, NUMAND, LEMANDE, MANDI, MANDE, PIMENC  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Mbam, West (A.40).
leu  Kara  -  leu  Papua New Guinea  0  0  0  LEU  -  -  -  bnp lbb gri yal khz ksd meu kqf  en  no  -  -  LEMUSMUS, LEMAKOT  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, Lavongai-Nalik.
lez  Lezgi  Лезги чlал  lez  Russian Federation  215  285937  2147597  LEZ  -  lez  -  agx tab uz kum tg gag-Cyrl dar lbe ky cv ru  en ru  no  -  Sun Dec 1 20:48:25 CST 2013  LEZGIAN, LEZGHI, LEZGIN, KIURINSTY  North Caucasian, Northeast, Lezgian.
lg  Luganda  Oluganda  lug  Uganda  125  364939  2790176  LAP  lu  lg  lap1  xog nyo ttj nyn hay rw  en  started  San Emmanuel James, Jackson Ssekiryango, Kizito Birabwa  Tue Sep 10 11:32:44 CDT 2013  LUGANDA  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, J, Nyoro-Ganda (J.10).
lgg  Lugbara  Lugbara  lgg  Uganda  190  303441  1680149  LUG  lg  -  -  mhi bts maw dag  en  no  -  Mon Feb 4 10:12:58 CST 2013  HIGH LUGBARA  Nilo-Saharan, Central Sudanic, East, Moru-Madi, Central.
lhu  Lahu  Lahu  lhu  China  12  352957  1600217  LAH  -  -  -  ahk  en  no  -  Wed Sep 18 21:54:11 CDT 2013  LOHEI, LAHUNA, LAKU, KAIXIEN, NAMEN, MUSSUH, MUHSO, MUSSO, MUSSAR, MOSO  Sino-Tibetan, Tibeto-Burman, Lolo-Burmese, Loloish, Southern, Akha, Lahu.
li  Limburgish  Limburgs  lim  Netherlands  851  1890172  11634190  DUT  -  li  -  nds-NL vls zea nl fy sdz gos act nds stl af ksh de da lb  en nl  no  Kenneth Rohde Christiansen, Mathieu van Woerkom  Tue Sep 10 11:15:17 CDT 2013  LIMBURGIAN, LIMBURGIC, LIMBURGS, LIMBOURGEOIS  Indo-European, Germanic, West, Low Saxon-Low Franconian, Low Franconian.
lia  Limba  -  lia  Sierra Leone  3  251659  1304347  LIA  -  -  lia  kha miq dua knv-x-ara  en  no  -  Fri Jan 25 20:33:08 CST 2013  YIMBA, YUMBA  Niger-Congo, Atlantic-Congo, Atlantic, Southern, Limba.
lid  Nyindrou  -  lid  Papua New Guinea  349  475741  2569818  LID  -  -  -  nss nij bkd bjn ha snk btx slm sml tbc gfk aa  en  no  -  Fri Dec 28 19:11:59 CST 2012  LINDROU, LINDAU, SALIEN, NYADA  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Admiralty Islands, Eastern, Manus, West.
lif  Limbu  -  lif  Nepal  1  136899  1463233  LIF  -  -  -  hne hi ne  en  no  -  Mon Jan 7 08:15:26 CST 2013  YAKTHUNG PAN  Sino-Tibetan, Tibeto-Burman, Himalayish, Mahakiranti, Kiranti, Eastern.
lif-Limb  Limbu  ᤕᤰᤌᤢᤱ ᤐᤠᤴ  lif  Nepal  213  203699  1648871  LIF  -  -  -  -  en  no  -  Sun Jan 6 23:17:38 CST 2013  YAKTHUNG PAN  Sino-Tibetan, Tibeto-Burman, Himalayish, Mahakiranti, Kiranti, Eastern.
lij  Tabarkin  Lìgure  lij  Italy  27  280851  1620983  LIJ  -  lij  -  vec gl lmo an sc lld-x-fas pt-BR nap oc it  en  no  Alessio Gastaldi, Mark Williamson  Sat Jan 19 18:42:18 CST 2013  LÍGURU, LIGURE, LIGURIAN  Indo-European, Italic, Romance, Italo-Western, Western, Gallo-Iberian, Gallo-Romance, Gallo-Italian.
lil  Lillooet  Ucwalmícwts  lil  Canada  1  8156  59527  LIL  -  -  -  shs blc  en  no  -  Sat Jan 19 18:30:29 CST 2013  ST'AT'IMCETS  Salishan, Interior Salish, Northern.
lil-x-fou  Lillooet (Fountain)  St’aá’imcets  lil  Canada  0  0  0  LIL  -  -  -  blc lil-x-mou  en  no  -  -  ST'AT'IMCETS, NORTHERN ST'AT'IMCETS  Salishan, Interior Salish, Northern.
lil-x-mou  Lillooet (Mount Currie)  Lil'wat7úlmec  lil  Canada  0  0  0  LIL  -  -  -  lil-x-fou blc  en  no  -  -  ST'AT'IMCETS, LOWER ST'AT'IMCETS  Salishan, Interior Salish, Northern.
lis-Lisu  Lisu  ꓡꓲꓢꓴ  lis  China  160  37539  392506  LIS  -  -  -  -  en  no  -  Thu Apr 25 11:42:04 CDT 2013  LISSU, LISAW, LI-SHAW, LI-HSAW, LU-TZU, LESUO, LI, LISHU, LISO, LEISU, LESHUOOPA, LOISU, SOUTHERN LISU, YAO YEN, YAW-YEN, YAW YIN, YEH-JEN, CHUNG, CHELI, CHEDI, LIP'A, LUSU, KHAE  Sino-Tibetan, Tibeto-Burman, Lolo-Burmese, Loloish, Northern, Lisu.
liv  Liv  Līvõ  liv  Latvia  257  33944  229704  LIV  -  -  -  ekk vro mxp toj tzt smj se fit mxq lvs fi lv fkv  en  no  -  Mon Sep 23 07:36:11 CDT 2013  LIVONIAN  Uralic, Finno-Ugric, Finno-Permic, Finno-Cheremisic, Finno-Mordvinic, Finno-Lappic, Baltic-Finnic.
ljp  Lampung Api  Bahasa Lampung Api  ljp  Indonesia (Sumatra)  2  180863  1145207  LJP  -  -  -  bjn id zsm iba su bts zlm bsb jv-x-bms nij jv  en  no  -  Wed Sep 18 21:56:24 CDT 2013  API, LAMPONG  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Sundic, Lampungic, Pesisir.
lki  Laki  -  lki  Iran  45  93258  557749  LKI  -  -  -  pes fa bal glk mzn prs  en  no  Rasoul Azizi  Tue Sep 10 11:11:06 CDT 2013  ALAKI, LEKI  Indo-European, Indo-Iranian, Iranian, Western, Northwestern, Kurdish
lkt  Lakota  Lakȟótiyapi  lkt  USA  4  85728  525537  LKT  -  -  -  dak ha pon nii bim  en  no  -  Wed Sep 18 21:57:32 CDT 2013  LAKHOTA, TETON  Siouan, Siouan Proper, Central, Mississippi Valley, Dakota.
lld  Ladin  Ladin  lld  Italy  222  617999  3653031  LLD  rh  -  -  oc lmo lnc ca ast mwl fur fr es  en it  no  Oliver Streiter, Mathias Stuflesser  Wed Sep 18 21:58:18 CDT 2013  DOLOMITE  Indo-European, Italic, Romance, Italo-Western, Western, Gallo-Iberian, Gallo-Romance, Gallo-Rhaetian, Rhaetian.
lld-x-bad  Ladin (Badiot)  -  lld  Italy  1  102530  594301  LLD  -  -  -  lld-x-fas lld-x-gar lmo ast ca  en it  no  Oliver Streiter, Mathias Stuflesser  Sat Jan 26 19:24:50 CST 2013  DOLOMITE  Indo-European, Italic, Romance, Italo-Western, Western, Gallo-Iberian, Gallo-Romance, Gallo-Rhaetian, Rhaetian.
lld-x-fas  Ladin (Fascian)  -  lld  Italy  1  16271  90105  LLD  -  -  -  lld-x-bad lld-x-gar ca oc vec ast  en it  no  Oliver Streiter, Mathias Stuflesser  Thu Jan 24 21:05:13 CST 2013  DOLOMITE  Indo-European, Italic, Romance, Italo-Western, Western, Gallo-Iberian, Gallo-Romance, Gallo-Rhaetian, Rhaetian.
lld-x-gar  Ladin (Gherdeina)  -  lld  Italy  1  101299  572880  LLD  -  -  -  lld-x-bad lld-x-fas lmo mwl oc ca ast  en it  no  Oliver Streiter, Mathias Stuflesser  Thu Jan 24 21:06:15 CST 2013  DOLOMITE  Indo-European, Italic, Romance, Italo-Western, Western, Gallo-Iberian, Gallo-Romance, Gallo-Rhaetian, Rhaetian.
lmo  Lombard  Lombard  lmo  Italy  3  2064973  11650112  LMO  -  lmo  -  vec lms ca-valencia cbk lld-x-fas mwl oc lad lij ast es  en it  no  -  Mon Jan 21 21:41:01 CST 2013  LOMBARDO  Indo-European, Italic, Romance, Italo-Western, Western, Gallo-Iberian, Gallo-Romance, Gallo-Italian.
lms  Limousin  -  lms  France  165  1028239  5564820  LMS  -  -  -  prv lnc gsc es an ca ast  en fr  no  Bruno Gallart  Thu Jan 24 21:44:42 CST 2013  LEMOSIN, OCCITAN  Indo-European, Italic, Romance, Italo-Western, Western, Gallo-Iberian, Ibero-Romance, Oc.
ln  Lingala  Lingála  lin  Dem. Rep. of Congo  265  885723  5330859  LIN  li  ln  lin  ktu amu gri fj ki sw kg  en fr  yes  Mike Nkongolo, Denis Jacquerye, Etienne Ruedin  Mon Dec 2 16:35:42 CST 2013  NGALA  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Northwest, C, Bangi-Ntomba (C.40), Lusengo.
lnc  Languedocien  -  lnc  France  2  82889  487416  LNC  -  -  prv1  gsc lms prv es ast ca mwl lad gl  en  yes  Bruno Gallart  Wed Jan 30 23:11:56 CST 2013  LENGADOUCIAN, LANGUEDOC, LANGADOC, OCCITAN, OCCITANI  Indo-European, Italic, Romance, Italo-Western, Western, Gallo-Iberian, Ibero-Romance, Oc.
lns  Lamnso’  -  lns  Cameroon  2  4534  19825  NSO  -  -  nso  nap  en  no  -  Fri Sep 13 10:24:42 CDT 2013  NSO, NSO', NSAW, NSHO', LAMSO, LAMNSOK, BANSO, BANSO', BANSAW, PANSO  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Wide Grassfields, Narrow Grassfields, Ring, East.
lnu  Longuda  -  lnu  Nigeria  4  43777  229886  LNU  -  -  -  jv tl pam dga agn  en  no  -  Sat Jan 19 19:12:06 CST 2013  NUNGUDA, NUNGURABA, NUNGURA, LANGUDA, LONGURA  Niger-Congo, Atlantic-Congo, Volta-Congo, North, Adamawa-Ubangi, Adamawa, Waja-Jen, Longuda.
lo  Lao  ລາວ  lao  Laos  106  140679  2103229  NOL  la*  lo  nol  -  en  no  Anousak Souphavanh  Mon Feb 4 21:54:06 CST 2013  LAOTIAN TAI, LAOTIAN, PHOU LAO, EASTERN THAI, LUM LAO, LAO WIANG, LAO KAO, RONG KONG, TAI LAO, LAO-TAI, LÀO, LAO-LUM, LAO-NOI, LAOTHIAN  Tai-Kadai, Kam-Tai, Be-Tai, Tai-Sek, Tai, Southwestern, East Central, Lao-Phutai.
loa  Loloda  -  loa  Indonesia (Maluku)  0  0  0  LOL  -  -  -  gbi tby alu tlb  en  no  -  -  LODA, NORTH LOLODA  West Papuan, North Halmahera, North, Galela-Loloda.
lol  Mongo-Nkundu  Mongo-Nkundu  lol  Dem. Rep. of Congo  0  0  0  MOM  lom  -  -  knv-x-ara dua nia kqn xog tn lia kez xsm lu kck  en  no  -  -  MONGO, LOMONGO  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Northwest, C, Mongo (C.70).
lot  Otuho  -  lot  Sudan  1  1727  10457  LOT  -  -  lot  rw jv pam  en  no  -  Mon Dec 9 14:13:46 CST 2013  LOTUKO, LOTUHO, LOTUXO, LOTUKA, LATTUKA, LATUKO, LATUKA, LATOOKA, OTUXO, OLOTORIT  Nilo-Saharan, Eastern Sudanic, Nilotic, Eastern, Lotuxo-Teso, Lotuxo-Maa, Lotuxo.
lou  Louisiana Creole French  -  lou  USA  14  101475  526670  LOU  -  -  -  fr-x-jer fr mfe ie crs rcf wa ht  en  no  Kevin Rottet  Mon Jan 21 21:43:22 CST 2013  -  Creole, French based.
loz  Lozi  Silozi  loz  Zambia  96  279036  1520011  LOZ  sk  -  lbm1  sw kck toi xog tsc bem  en  no  -  Wed Sep 18 22:01:03 CDT 2013  SILOZI, ROZI, TOZVI, ROTSE, RUTSE, KOLOLO  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, S, Sotho-Tswana (S.30).
lt  Lithuanian  Lietuvių  lit  Lithuania  5574  20042206  157342134  LIT  l  lt  lit  lvs el-Latn ltg pt et  en  yes  -  Mon Feb 4 22:19:38 CST 2013  LIUTUVISKAI, LIETUVI, LITOVSKIY, LITEWSKI, LITAUISCHE  Indo-European, Baltic, Eastern.
ltg  Latgalian  Latgaļu  ltg  Latvia  693  752547  5501335  -  -  ltg  -  lvs lt inb mk-Latn  en  yes  -  Tue Sep 10 13:49:00 CDT 2013  East Latvian, High Latvian.  Indo-European, Baltic, Eastern
lu  Luba-Katanga  Kiluba  lub  Dem. Rep. of Congo  37  92298  626170  LUH  ku  -  -  kqn lua sop bem yaf xog loz kck lg sw  en  no  -  Mon Dec 2 12:34:44 CST 2013  LUBA-SHABA, KILUBA  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, L, Luba (L.30).
lua  Luba-Kasai  Tshiluba  lua  Dem. Rep. of Congo  7  80106  510912  LUB  sh  -  lub  lu sop kqn kcc yaf pem kmb lun  en  no  -  Fri Sep 13 14:33:46 CDT 2013  LUBA-LULUA, TSHILUBA, WESTERN LUBA, LUVA  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, L, Luba (L.30).
lue  Luvale  Luvale  lue  Zambia  23  79789  640063  LUE  lv  -  lue  kki nba cjk lun dig tum kde lch nym heh  en  no  -  Tue Sep 10 11:24:31 CDT 2013  LUENA, LWENA, CHILUVALE, LOVALE, LUBALE  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, K, Chokwe-Luchazi (K.20).
lun  Lunda  Lunda  lun  Zambia  4  13114  106383  LVN  ld  -  mlo1  lue rnd  en  no  -  Fri Sep 13 14:34:32 CDT 2013  CHILUNDA, CHOKWE-LUNDA  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, K, Salampasu-Ndembo (K.30).
luo  Dholuo  Dholuo  luo  Kenya  191  379102  2164003  LUO  lo  -  -  ach alz tby loa alu bts gbi  en  no  -  Fri Sep 13 12:43:56 CDT 2013  DHOLUO, NILOTIC KAVIRONDO, KAVIRONDO LUO  Nilo-Saharan, Eastern Sudanic, Nilotic, Western, Luo, Southern, Luo-Acholi, Luo.
lup  Lumbu  -  lup  Gabon  1  2018  12672  LUP  -  -  -  blh hna  en  no  -  Wed May 8 14:47:56 CDT 2013  ILUMBU, BALOUMBOU  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Northwest, B, Sira (B.40).
lus  Mizo  Mizo ṭawng  lus  India  3067  7342876  39918367  LSH  ls  -  lus  cnh bgr vap kno tcz  en  no  -  Wed Sep 18 22:04:49 CDT 2013  DULIEN, DUHLIAN TWANG, LUSAI, LUSEI, LUSHEI, LUKHAI, LUSAGO, LE, SAILAU, HUALNGO, WHELNGO, LUSHAI  Sino-Tibetan, Tibeto-Burman, Kuki-Chin-Naga, Kuki-Chin, Central.
lut  Lushootseed  -  lut  USA  0  0  0  LUT  -  -  -  thp coo  en  no  Chris Harvey  -  -  Salishan, Central Salish, Twana.
luy  Oluluyia  -  luy  Kenya  7  37237  299930  LUY  -  -  -  xog lg bem hay  en  no  -  Wed Jan 2 16:20:46 CST 2013  LULUYIA, LUHYA  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, J, Masaba-Luyia (J.30), Luyia.
lv  Latvian  Latviešu  lav  Latvia  2574  10583388  78292042  LAT  lt  lv  lat  lt  en  yes  -  Tue Sep 10 11:27:27 CDT 2013  LATVISKA, 'LETTISH', 'LETTISCH'  Indo-European, Baltic, Eastern.
lvs  Standard Latvian  Latviešu  lvs  Latvia  6175  16365584  120218877  LAT  lt  lv  lat  lt  en  yes  -  Thu Jan 31 09:49:09 CST 2013  LATVISKA, 'LETTISH', 'LETTISCH'  Indo-European, Baltic, Eastern.
lwo  Luwo  -  lwo  Sudan  1  254716  1326862  LWO  -  -  -  dip din  en  no  -  Mon Jan 7 13:30:31 CST 2013  LWO, JUR LUO, JUR LWO, JO LWO, DHE LWO, DHE LUWO, GIUR  Nilo-Saharan, Eastern Sudanic, Nilotic, Western, Luo, Northern, Jur.
lzh  Literary Chinese  -  lzh  China  1  11251  735776  -  -  zh-classical  -  wuu gan  en  no  -  Tue Jan 29 22:11:07 CST 2013  MANDARIN, GUANHUA, BEIFANG FANGYAN, NORTHERN CHINESE, GUOYU, STANDARD CHINESE, PUTONGHUA  Sino-Tibetan, Chinese.
lzz  Laz  Lazuri  lzz  Turkey  58  18411  141123  LZZ  -  -  -  snk gri nl bts fj eu mer btx srn  en  no  -  Mon Sep 23 08:50:04 CDT 2013  LAZURI, LAZE, CHAN, CHANZAN, ZAN, CHANURI  South Caucasian, Zan.
lzz-Geor  Laz (Georgian)  ლაზური  lzz  Turkey  19  4995  41448  LZZ  -  -  -  xmf ka sva-Geor  en  no  -  Mon Sep 23 08:56:53 CDT 2013  LAZURI, LAZE, CHAN, CHANZAN, ZAN, CHANURI  South Caucasian, Zan.
maa  San Jerónimo Tecóatl Mazatec  -  maa  Mexico  2  55382  336593  MAA  -  -  -  maj vmy mzi  en es  no  -  Thu Dec 27 18:55:01 CST 2012  SAN JERÓNIMO MAZATECO, NORTHERN HIGHLAND MAZATECO  Oto-Manguean, Popolocan, Mazatecan.
mad  Madura  Bhesa Medura  mad  Indonesia (Java and Bali)  3  3452  26153  MHJ  -  -  mhj  jv-x-bms bjn zsm id su bik min jv pam  en  no  -  Wed Sep 18 22:04:00 CDT 2013  MADURESE, MADHURA, BASA MATHURA  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Sundic, Madurese.
maf  Mafa  -  maf  Cameroon  2  2480  12242  MAF  -  -  -  bum biv lus  en  no  -  Thu Jan 3 19:11:21 CST 2013  'MATAKAM', MOFA, NATAKAN  Afro-Asiatic, Chadic, Biu-Mandara, A, A.5.
mag  Magahi  -  mag  India  2  2432  12296  MQM  -  -  mqm  hne  en  no  -  Fri Sep 13 11:00:52 CDT 2013  MAGADHI, MAGAYA, MAGHAYA, MAGHORI, MAGI, MAGODHI, BIHARI  Indo-European, Indo-Iranian, Indo-Aryan, Eastern zone, Bihari.
mai  Maithili  मैथिली  mai  India  1017  2584481  15234075  MKP  -  -  mai  hi ne mag hne mr bho awa  en  yes  -  Wed Sep 18 22:05:31 CDT 2013  MAITLI, MAITILI, METHLI, TIRAHUTIA, BIHARI, TIRHUTI, TIRHUTIA, APABHRAMSA  Indo-European, Indo-Iranian, Indo-Aryan, Eastern zone, Bihari.
maj  Jalapa de Díaz Mazatec  -  maj  Mexico  4  92954  554482  MAJ  -  -  -  vmy  en es  no  -  Thu Dec 27 19:00:18 CST 2012  SAN FELIPE JALAPA DE DÍAZ MAZATECO, LOWLAND MAZATECO  Oto-Manguean, Popolocan, Mazatecan.
mak-Latn  Makasar  Basa Mangkasara'  mak  Indonesia (Sulawesi)  5  174077  1385057  MSR  -  -  -  mvp sda bug lcm krj tl hil su msk jv pam agn sml  en  no  -  Thu Sep 19 11:58:31 CDT 2013  MAKASSAR, MACASSARESE, MACASSAR, MAKASSA, MAKASSARESE, TAENA, TENA, GOA, MENGKASARA, MANGASARA, MAKASSAARSCHE  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Sulawesi, South Sulawesi, Makassar.
mam  Mam  Mam  mam  Guatemala  76  829083  5056574  MAM  mz  -  mam  ttc knj tzh kjb ty  en  no  Ana Secundina Méndez Romero, Jameson Quinn  Wed Sep 18 22:06:01 CDT 2013  HUEHUETENANGO MAM  Mayan, Quichean-Mamean, Greater Mamean, Mamean.
man  Mandingo  -  man  Senegal  39  268237  1403519  -  -  -  -  dyu kao bm kus  en  no  Allan Callister  Sat Jan 26 19:24:58 CST 2013  MANDING, MANDINGO, MANDINGUE, MANDINQUE, MANDE, SOCÉ  Niger-Congo, Mande, Western, Central-Southwestern, Central, Manding-Jogo, Manding-Vai, Manding-Mokole, Manding, Manding-West.
maq  Chiquihuitlán Mazatec  -  maq  Mexico  2  385170  2102582  MAQ  -  -  -  vmy mau maj mzi ram bon cya zpm  en es  no  -  Thu Dec 27 18:57:18 CST 2012  SAN JUAN CHIQUIHUITLÁN MAZATECO  Oto-Manguean, Popolocan, Mazatecan.
mas  Maasai  -  mas  Kenya  0  0  0  MET  -  -  -  brh-Latn okv cs gah it  en  no  -  -  MASAI, MAA  Nilo-Saharan, Eastern Sudanic, Nilotic, Eastern, Lotuxo-Teso, Lotuxo-Maa, Ongamo-Maa.
mau  Mazateco  Mazateco  mau  Mexico  189  407049  3058514  MAU  maz  -  -  vmy maj mzi  en es  no  -  Tue Feb 5 07:39:09 CST 2013  MAZATECO, HUAUTLA DE JIMENEZ MAZATECO, HIGHLAND MAZATECO, MAZATEC  Oto-Manguean, Popolocan, Mazatecan.
mav  Sateré-Mawé  -  mav  Brazil  3  502004  2638518  MAV  -  -  -  ur-Latn mi  en  no  -  Sun Jan 6 17:05:25 CST 2013  MAUE, MABUE, MARAGUA, SATARÉ, ANDIRA, ARAPIUM  Tupi, Mawe-Satere.
maw  Mampruli  -  maw  Ghana  1  240298  1191448  MAW  -  -  -  hag dag kus gux  en  no  -  Mon Jan 7 13:46:25 CST 2013  MAMPRULE, MANPELLE, NGMAMPERLI  Niger-Congo, Atlantic-Congo, Volta-Congo, North, Gur, Central, Northern, Oti-Volta, Western, Southeast.
maz  Central Mazahua  Jñatrjo  maz  Mexico  4  312327  1581333  MAZ  -  -  maz  ote otm  en es  no  -  Wed Sep 18 22:08:31 CDT 2013  -  Oto-Manguean, Otopamean, Otomian, Mazahua.
mbb  Western Bukidnon Manobo  -  mbb  Philippines  1  273586  1536498  MBB  -  -  -  mbt mbi mbs ms  en  no  -  Fri Sep 13 11:20:12 CDT 2013  -  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Southern Philippine, Manobo, Central, West.
mbc  Macushi  -  mbc  Guyana  0  0  0  MBC  -  -  -  ake pbc thk nss car ha ubr kng  en  no  -  -  MAKUSHI, MAKUXI, MACUSI, MACUSSI, TEWEYA, TEUEIA  Carib, Northern, East-West Guiana, Macushi-Kapon, Macushi.
mbd  Dibabawon Manobo  -  mbd  Philippines  2  2189  12981  MBD  -  -  -  ibl ami pag ja-Latn atd  en  no  -  Fri Sep 13 11:20:52 CDT 2013  MANDAYA, DIBABAON, DEBABAON  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Southern Philippine, Manobo, Central, East.
mbh  Mangseng  -  mbh  Papua New Guinea  0  0  0  MBH  -  -  -  sua bnp krj hil zne pam bch tpi tlb mi lbb  en  no  -  -  MANGSING, MASEGI, MASEKI  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Ngero-Vitiaz, Vitiaz, Southwest New Britain, Arawe-Pasismanua, Arawe.
mbi  Ilianen Manobo  -  mbi  Philippines  1  2443  13399  MBI  -  -  -  mbt mbb mbs ppl ain tvl zpi ms  en  no  -  Sat Jan 19 19:36:04 CST 2013  ILIANEN  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Southern Philippine, Manobo, Central, West.
mbj  Nadëb  -  mbj  Brazil  1  359247  1738909  MBJ  -  -  -  son om  en  no  -  Sun Jan 6 17:03:34 CST 2013  NADEB MACU, MAKÚ NADËB, MAKUNADÖBÖ, NADÖBÖ, ANODÖUB, KABORI, KABARI, XIRIWAI, XURIWAI  Maku.
mbl  Maxakalí  -  mbl  Brazil  1  241378  1358564  MBL  -  -  -  tzh  en  no  -  Sun Jan 6 17:03:46 CST 2013  CAPOSHO, CUMANASHO, MACUNI, MONAXO, MONOCHO  Macro-Ge, Maxakali.
mbp  Malayo  -  mbp  Colombia  1  868  5971  MBP  -  -  -  quw mti swh pkb qxr kki qvo ki dww  en  no  -  Wed Dec 5 15:16:28 CST 2012  MAROCASERO, MARACASERO, SANJA, SANKA, SANCÁ, AROSARIO, ARSARIO, GUAMAKA, GUAMACA, WIWA  Chibchan, Aruak.
mbs  Sarangani Manobo  -  mbs  Philippines  0  0  0  MBS  -  -  -  mbi zsm id jv-x-bms  en  no  -  -  -  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Southern Philippine, Manobo, South.
mbt  Matigsalug Manobo  -  mbt  Philippines  92  628878  3713240  MBT  -  -  -  mbi mbb mbs ppl tvl ain rar  en  no  -  Fri Sep 13 10:42:34 CDT 2013  MATIG-SALUG MANOBO  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Southern Philippine, Manobo, Central, South, Ata-Tigwa.
mbz  Amoltepec Mixtec  -  mbz  Mexico  3  31974  198227  MBZ  -  -  -  mpm mxt  en es  no  -  Sun Nov 17 14:50:03 CST 2013  WESTERN SOLA DE VEGA MIXTEC, AMOLTEPEC MIXTEC  Otomanguean, Eastern Otomanguean, Amuzgo-Mixtecan, Mixtecan, Mixtec.
mcb  Machiguenga  -  mcb  Peru  4  396780  3976154  MCB  -  -  -  cpu not cjo cni tbg apu sn omw-x-veq ndc kpr miq  en es  no  -  Thu Dec 27 19:08:17 CST 2012  MATSIGANGA, MATSIGENKA, MAÑARIES  Arawakan, Maipuran, Southern Maipuran, Campa.
mcd  Sharanahua  -  mcd  Peru  3  383580  2698725  MCD  -  -  mcd  kaq shp nah ubr agd ncj nuz ngu ifb  en  no  -  Thu Dec 27 19:10:23 CST 2012  -  Panoan, South-Central, Yaminahua-Sharanahua.
mcf  Matsés  -  mcf  Peru  4  259853  2123628  MCF  -  -  mcf  kaq nhi ncl cbr amc acc ncj sei nuz shp cap  en  no  -  Thu Dec 27 19:12:23 CST 2012  MAYORUNA, MAXURUNA, MAJURUNA, MAYIRUNA, MAXIRONA, MAGIRONA, MAYUZUNA  Panoan, Northern.
mco  Coatlán Mixe  -  mco  Mexico  7  313227  2084792  MCO  -  -  -  mir toj crn  en  no  -  Tue Feb 5 21:53:21 CST 2013  SOUTHEASTERN MIXE  Mixe-Zoque, Mixe, Eastern Mixe.
mcq  Ese  -  mcq  Papua New Guinea  0  0  0  MCQ  -  -  -  alu gri stn fj khz pad bmk pwg  en  no  -  -  MANAGULASI  Trans-New Guinea, Main Section, Eastern, Central and Southeastern, Koiarian, Baraic.
mcu  Cameroon Mambila  -  mcu  Cameroon  1  257574  1112579  MYA  -  -  -  anv  en  no  -  Mon Jan 7 14:46:16 CST 2013  MAMBILLA, MAMBERE, NOR, TORBI, LAGUBI, TAGBO, TONGBO, BANG, BLE, JULI, BEA  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Northern, Mambiloid, Mambila-Konja, Mambila.
mda  Mada  -  mda  Nigeria  2  349866  1598837  MDA  -  -  -  yam  en  no  -  Mon Jan 7 14:59:59 CST 2013  MADDA, YIDDA  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Platoid, Plateau, Western, Southwestern, A.
mdf  Moksha  мокшень кяль  mdf  Russian Federation  3  85865  667303  MDF  mok  mdf  -  myv ru  en  no  -  Tue Jan 29 18:42:05 CST 2013  MORDVIN-MOKSHA, MORDOV, MORDOFF, MOKSHAN  Uralic, Finno-Ugric, Finno-Permic, Finno-Cheremisic, Finno-Mordvinic, Mordvinic.
mdv  Santa Lucía Monteverde Mixtec  -  mdv  Mexico  4  29278  177163  MDV  -  -  -  mpm mxv  en es  no  -  Thu Dec 27 19:14:29 CST 2012  -  Oto-Manguean, Mixtecan, Mixtec-Cuicatec, Mixtec.
med  Melpa  -  med  Papua New Guinea  0  0  0  MED  -  -  -  zne krj ny-x-nya imo hil bch akl  en  no  -  -  MEDLPA, HAGEN  Trans-New Guinea, Main Section, Central and Western, East New Guinea Highlands, Central, Hagen.
mee  Mengen  -  mee  Papua New Guinea  0  0  0  MEE  -  -  -  stn kwf lcm bnp mak-Latn ksd haw mi krj mmn  en  no  -  -  POENG  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Ngero-Vitiaz, Vitiaz, Mengen.
mej  Meyah  -  mej  Indonesia (Irian Jaya)  1  322297  1855435  MEJ  -  -  -  kwn  en  no  -  Mon Jan 7 14:45:50 CST 2013  MEAX, MEYACH, MEAH, MEJAH, MEJACH  East Bird's Head, Meax.
mek  Mekeo  -  mek  Papua New Guinea  0  0  0  MEK  -  -  -  stn mee tkl khz npy gdn swp haw  en  no  -  -  MEKEO-KOVIO  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Peripheral, Central Papuan, West Central Papuan, Nuclear.
men  Mende  -  men  Sierra Leone  3  116448  589810  MFY  -  -  mfy  sg bas bfa ilo tsc  en  no  -  Mon Jan 7 22:22:48 CST 2013  BOUMPE, HULO, KOSSA, KOSSO  Niger-Congo, Mande, Western, Central-Southwestern, Southwestern, Mende-Loma, Mende-Bandi, Mende-Loko.
meq  Merey  -  meq  Cameroon  1  291299  1414568  MEQ  -  -  -  gnd dgc  en  no  -  Mon Jan 7 15:38:04 CST 2013  MERI, MERE, MOFU DE MERI  Afro-Asiatic, Chadic, Biu-Mandara, A, A.5.
mer  Kimîîru  -  mer  Kenya  19  63914  417800  MER  -  -  -  sw rw ki pkb  en  no  -  Sun Jan 20 08:30:22 CST 2013  KIMERU  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, E, Kikuyu-Kamba (E.20), Meru.
meu  Motu  Motu  meu  Papua New Guinea  1039  992118  5927439  MEU  mtu  -  -  ho gri pwg  en  no  -  Fri Sep 13 14:35:54 CDT 2013  TRUE MOTU, PURE MOTU  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Peripheral, Central Papuan, Sinagoro-Keapara.
mfb  Bangka  -  mfb  Indonesia (Sumatra)  21  5945  37270  MFB  -  -  -  jv pam tl bjn id vkt su msk zsm kyk jvn jv-x-bms agn ban bbc-Latn bsb  en  no  -  Mon Dec 2 10:14:17 CST 2013  BELOM, MAPOR, MAPORESE  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Sundic, Sumatra, Lom.
mfe  Morisyen  Morisyen  mfe  Mauritius  486  613746  3492475  MFE  ce  -  -  crs rcf ht acf lou br bim non  en fr  no  -  Wed Sep 18 22:12:59 CDT 2013  MAURITIUS CREOLE FRENCH, KREOLE, KREOL, MAURITIAN, MAURYSEN  Creole, French based.
mfh  Matal  -  mfh  Cameroon  1  237714  1270832  MFH  -  -  -  nak emk gur  en  no  -  Mon Jan 7 15:38:16 CST 2013  MOUKTELE, MUKTILE, MUKTELE, BALDA  Afro-Asiatic, Chadic, Biu-Mandara, A, A.5.
mfi  Wandala  -  mfi  Cameroon  1  252692  1398973  MFI  -  -  -  gri ln sw  en  no  -  Mon Jan 7 15:38:33 CST 2013  MANDARA, NDARA, MANDARA MONTAGNARD  Afro-Asiatic, Chadic, Biu-Mandara, A, A.4, Mandara Proper, Mandara.
mfq  Moba  -  mfq  Togo  2  461288  1959046  MFQ  -  -  -  gux hag bim xon bba maw mfq-x-lok cko tbc kus  en  no  -  Mon Jan 7 16:30:48 CST 2013  MOAB, MOARE, MOA, BEN  Niger-Congo, Atlantic-Congo, Volta-Congo, North, Gur, Central, Northern, Oti-Volta, Gurma, Moba.
mfq-x-lok  Moba Lok  -  mfq  Togo  0  0  0  MFQ  -  -  -  mfq dag inb yo xon yap bim  en  no  -  -  MOAB, MOARE, MOA, BEN  Niger-Congo, Atlantic-Congo, Volta-Congo, North, Gur, Central, Northern, Oti-Volta, Gurma, Moba.
mfy  Mayo  Yoreme  mfy  Mexico  14  62945  406943  MAY  myo  -  -  yaq  en es  no  -  Wed Sep 18 22:14:24 CDT 2013  -  Uto-Aztecan, Southern Uto-Aztecan, Sonoran, Cahita.
mfz  Mabaan  -  mfz  Sudan  1  236784  1283368  MFZ  -  -  -  mbt dyu ha bm wo  en  no  -  Mon Jan 7 19:45:08 CST 2013  MAABAN, MEBAN, SOUTHERN BURUN, GURA, TUNGAN, BARGA, TONKO, ULU  Nilo-Saharan, Eastern Sudanic, Nilotic, Western, Luo, Northern, Maban-Burun, Maban.
mg  Malagasy  Malagasy  mlg  Madagascar  10788  23807569  161632465  MEX  mg  mg  -  buc stn gri  en fr  yes  Rado Ramarotafika  Mon Dec 2 17:09:00 CST 2013  MALGACHE, STANDARD MALAGASY  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Borneo, Barito, East, Malagasy.
mgd  Moru  -  mgd  Sudan  2  4561  23610  MGD  -  -  -  mhi  en  no  -  Sat Jan 5 09:23:34 CST 2013  KALA MORU  Nilo-Saharan, Central Sudanic, East, Moru-Madi, Northern.
mh  Marshallese  Kajin Majōl  mah  Marshall Islands  43  926976  4687638  MZM  mh  mh  mzm  nhy hus  en  started  Marco Mora  Fri Sep 13 14:36:19 CDT 2013  EBON  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Micronesian, Micronesian Proper, Marshallese.
mhi  Ma’di  Ma’di  mhi  Uganda  8  37669  170352  MHI  mdi  -  -  lgg  en  no  -  Sun Jan 20 08:32:38 CST 2013  MA'ADI, MA'DITI, MA'DI, MADI  Nilo-Saharan, Central Sudanic, East, Moru-Madi, Southern.
mhl  Mauwake  -  mhl  Papua New Guinea  0  0  0  MHL  -  -  -  ki stn mer alu fj twu kwf sw gri gil  en  no  -  -  ULINGAN, MAWAKE  Trans-New Guinea, Madang-Adelbert Range, Adelbert Range, Pihom-Isumrud-Mugil, Pihom, Kumilan.
mho  Mashi  Mashi  mho  Zambia  2  7170  52855  MHO  msh  -  -  lg nyo ttj nyn xog koo nnb  en  no  -  Sat Jan 19 19:50:39 CST 2013  MASI  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, K, Kwangwa (K.40).
mhr  Meadow Mari  Олык Марий  mhr  Russian Federation  1110  1678810  12720009  MAL  -  mhr  -  mrj ky  en  no  -  Fri Jan 25 20:42:54 CST 2013  Mari, Eastern Mari, Cheremis, Low Mari, Mari-Woods, Lugovo Mari  Uralic, Mari
mhw  Mbukushu  Thimbukushu  mhw  Namibia  4  148504  1094222  MHW  -  -  -  koo  en  no  -  Fri Sep 13 14:37:28 CDT 2013  MBUKUSHI, MAMBUKUSH, MAMPUKUSH, MBUKUHU, THIMBUKUSHU, GOVA, KUSSO  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, K, Kwangwa (K.40).
mhx  Lhao Vo  -  mhx  Myanmar  140  392379  2092276  MHX  -  -  -  pam kac tl kyk jv  en  no  -  Mon Jan 7 20:03:15 CST 2013  MATU, MALU, LAWNG, LAUNGWAW, LAUNGAW, LANSU, LANG, MULU, DISO, ZI, LHAO VO  Sino-Tibetan, Tibeto-Burman, Lolo-Burmese, Burmish, Northern.
mi  Maori  Māori  mri  New Zealand  453  1918066  9855117  MBF  ma  mi  mbf  rar tkl ty tvl wls rap gil to haw bnp  en  yes  Karaitiana Taiuru, John Cocks  Tue Sep 10 11:33:15 CDT 2013  NEW ZEALAND MAORI  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Central Pacific, East Fijian-Polynesian, Polynesian, Nuclear, East, Central, Tahitic.
mia  Miami  Myaamia  mia  USA  0  0  0  MIA  -  -  -  bim cr-Latn cjo csw-Latn bla xon mur gdn  en  no  -  -  MIAMI-ILLINOIS, MIAMI-MYAAMIA  Algic, Algonquian, Central.
mib  Atatláhuca Mixtec  -  mib  Mexico  2  384968  1825770  MIB  -  -  -  mig xtn mdv mpm zab mie mxv zai mil zaw  en es  no  -  Thu Dec 27 19:16:03 CST 2012  SAN ESTEBAN ATATLÁHUCA MIXTECO, SOUTH CENTRAL TLAXIACO MIXTECO, ATATLÁHUCA MIXTEC  Oto-Manguean, Mixtecan, Mixtec-Cuicatec, Mixtec.
mic  Micmac  Míkmawísimk  mic  Canada  31  99649  817720  MIC  -  -  mic  csw-Latn cr-Latn ppl mbt drt mna fi bim mbi  en fr  no  -  Mon Dec 9 14:55:20 CST 2013  MI'GMAW, MIIGMAO, MI'KMAW, RESTIGOUCHE  Algic, Algonquian, Eastern.
mie  Ocotepec Mixtec  -  mie  Mexico  2  382929  1820506  MIE  -  -  -  mib cux mil mit mig  en es  no  -  Thu Dec 27 19:20:46 CST 2012  SANTO TOMÁS OCOTEPEC MIXTECO, OCOTEPEC MIXTEC  Oto-Manguean, Mixtecan, Mixtec-Cuicatec, Mixtec.
mif  Mofu-Gudur  -  mif  Cameroon  1  280353  1418607  MIF  -  -  -  meq son gnd ha  en  no  -  Mon Jan 7 19:44:39 CST 2013  MOFOU, MOFOU DE GOUDOUR, MOFU-SUD, MOFU SOUTH  Afro-Asiatic, Chadic, Biu-Mandara, A, A.5.
mig  San Miguel el Grande Mixtec  -  mig  Mexico  2  233686  1287972  MIG  -  -  -  mib  en es  no  -  Thu Dec 27 19:21:41 CST 2012  -  Oto-Manguean, Mixtecan, Mixtec-Cuicatec, Mixtec.
mih  Chayuco Mixtec  -  mih  Mexico  3  376433  1815185  MIH  -  -  -  mxt mio mjc mza mxv  en es  no  -  Thu Dec 27 19:22:23 CST 2012  CHAYUCU MIXTECO, EASTERN JAMILTEPEC-CHAYUCO MIXTECO  Oto-Manguean, Mixtecan, Mixtec-Cuicatec, Mixtec.
mik  Mikasuki  -  mik  USA  1  459  5050  MIK  -  -  -  mus  en  no  -  Thu Jan 10 06:57:57 CST 2013  HITCHITI, MIKASUKI SEMINOLE, MICCOSUKEE  Muskogean, Eastern.
mil  Peñoles Mixtec  -  mil  Mexico  4  450172  2575525  MIL  -  -  -  mit mib mig mie pps cux mio mim  en es  no  -  Thu Dec 27 19:22:56 CST 2012  EASTERN MIXTECO  Oto-Manguean, Mixtecan, Mixtec-Cuicatec, Mixtec.
mim  Alacatlatzala Mixtec  -  mim  Mexico  1  6630  32603  MIM  -  -  -  mxb mza  en es  no  -  Sun Jan 6 19:48:37 CST 2013  HIGHLAND GUERRERO MIXTECO, ALACATLATZALA MIXTEC  Oto-Manguean, Mixtecan, Mixtec-Cuicatec, Mixtec.
min  Minangkabau  -  min  Indonesia (Sumatra)  10  3658970  26289378  MPU  -  min  mpu  bjn zsm jv-x-bms id su ifk bik  en id  no  -  Sat Sep 14 08:03:44 CDT 2013  MINANG, PADANG  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Sundic, Malayic, Malayan, Para-Malay.
mio  Pinotepa Nacional Mixtec  -  mio  Mexico  2  402038  1933119  MIO  -  -  -  mxt  en es  no  -  Thu Dec 27 19:23:15 CST 2012  WESTERN JAMILTEPEC MIXTECO, COASTAL MIXTECO, LOWLAND JICALTEPEC MIXTECO  Oto-Manguean, Mixtecan, Mixtec-Cuicatec, Mixtec.
miq  Mískito  Mískitu  miq  Nicaragua  203  366340  2147017  MIQ  mis  -  miq  kha sum ha iry  en es  no  -  Wed Sep 18 22:15:09 CDT 2013  MÍSQUITO, MÍSKITU, MOSQUITO, MARQUITO  Misumalpan.
mir  Isthmus Mixe  Ayuk  mir  Mexico  2  204079  1597571  MIR  mx  -  -  toj mxp mco mxq tzt  en es  no  -  Thu Dec 27 19:30:55 CST 2012  ISTHMUS MIXE, EASTERN MIXE, GUICHICOVI MIXE  Mixe-Zoque, Mixe, Eastern Mixe.
mit  Southern Puebla Mixtec  -  mit  Mexico  2  314558  2010447  MIT  -  -  -  mil mio mib mxv  en es  no  -  Thu Dec 27 19:31:14 CST 2012  SOUTHERN PUEBLA MIXTEC, ACATLÁN MIXTECO  Oto-Manguean, Mixtecan, Mixtec-Cuicatec, Mixtec.
miu  Cacaloxtepec Mixtec  -  miu  Mexico  2  2100  10663  MIU  mxo  -  -  mxv mxb mim mks miz mza amu  en es  no  -  Fri Sep 13 12:47:26 CDT 2013  HUAJUAPAN MIXTECO, CACALOXTEPEC MIXTEC  Oto-Manguean, Mixtecan, Mixtec-Cuicatec, Mixtec.
miz  Coatzospan Mixtec  -  miz  Mexico  3  401128  1798834  MIZ  -  -  -  mxv miu xtn xtd mim mpm mza mbz ain ppl mbt  en es  no  -  Thu Dec 27 19:31:31 CST 2012  TEOTITLÁN MIXTECO, SAN JUAN COATZOSPAN MIXTECO, COATZOSPAN MIXTEC  Oto-Manguean, Mixtecan, Mixtec-Cuicatec, Mixtec.
mjc  San Juan Colorado Mixtec  -  mjc  Mexico  2  367586  1795540  MJC  -  -  -  mih mio mxt mza cya guh cao mxv rkb mcd pls  en es  no  -  Thu Dec 27 19:31:53 CST 2012  -  Oto-Manguean, Mixtecan, Mixtec-Cuicatec, Mixtec.
mjw  Karbi  -  mjw  India  127  225481  1524968  MJW  -  -  -  pam jv jv-x-bms agn msk tl kyk  en  no  -  Mon Jan 28 00:00:16 CST 2013  MANCHATI, MIKIRI, KARBI, KARBI KARBAK, ARLENG ALAM  Sino-Tibetan, Tibeto-Burman, Mikir.
mk  Macedonian  Македонски  mkd  Macedonia  2041  12841703  84620225  MKJ  mc  mk  mkj  bg sr ru bs-Cyrl uk rue be  en ru  yes  Дамјан Георгиевски  Fri Sep 13 12:17:59 CDT 2013  MAKEDONSKI, SLAVIC, MACEDONIAN SLAVIC  Indo-European, Slavic, South, Eastern.
mk-Latn  Macedonian (Latin)  -  mkd  Macedonia  322  622049  3739495  MKJ  -  -  -  bg-Latn bs sr-Latn sl hr ru-Latn cs  en  no  -  Wed Sep 11 13:03:55 CDT 2013  MAKEDONSKI, SLAVIC, MACEDONIAN SLAVIC  Indo-European, Slavic, South, Eastern.
mks  Silacayoapan Mixtec  -  mks  Mexico  3  484876  2359505  MKS  -  -  -  miu  en es  no  -  Thu Dec 27 19:32:36 CST 2012  -  Oto-Manguean, Mixtecan, Mixtec-Cuicatec, Mixtec.
ml  Malayalam  മലയാളം  mal  India  755  3299118  33275567  MJS  my*  ml  mjs  pi-Mlym  en  yes  -  Fri Sep 13 14:39:07 CDT 2013  ALEALUM, MALAYALANI, MALAYALI, MALEAN, MALIYAD, MALLEALLE, MOPLA  Dravidian, Southern, Tamil-Kannada, Tamil-Kodagu, Tamil-Malayalam, Malayalam.
mlh  Mape  -  mlh  Papua New Guinea  0  0  0  MLH  -  -  -  kmg nen dah nop cwt ain tn luo ksr  en  no  -  -  -  Trans-New Guinea, Main Section, Central and Western, Huon-Finisterre, Huon, Eastern.
mlp  Bargam  -  mlp  Papua New Guinea  282  625367  3455545  MLP  -  -  -  bik hus war  en  no  -  Fri Jan 25 21:07:35 CST 2013  MUGIL, BUNU, SAKER  Trans-New Guinea, Madang-Adelbert Range, Adelbert Range, Pihom-Isumrud-Mugil, Mugil.
mlu  To'abaita  To’abaita  mlu  Solomon Islands  1  5861  30567  MLU  ob  -  -  kwf meu stn ho aia  en  no  -  Mon Jan 21 21:44:51 CST 2013  TO'AMBAITA, TO'ABAITA, MALU, MALU'U  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Southeast Solomonic, Malaita-San Cristobal, Malaita, Northern.
mlv  Mwotlap  -  mlv  Vanuatu  1  1992  9078  MLV  -  -  -  nds-NL nl vls  en  no  Alex François  Tue Jan 22 10:50:36 CST 2013  MOTALAVA, MOTLAV  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, East Vanuatu.
mmn  Mamanwa  -  mmn  Philippines  1  1646  9660  MMN  -  -  -  itv msk kyk bku krj hnn hil sml  en  no  -  Sun Mar 24 18:34:01 CDT 2013  MAMANWA NEGRITO, MINAMANWA  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Meso Philippine, Central Philippine, Mamanwa.
mmo  Mangga Buang  -  mmo  Papua New Guinea  0  0  0  MMO  -  -  -  bzh twu ctd pam bik mvp bts  en  no  -  -  MANGA BUANG, KAIDEMUI  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Huon Gulf, South, Hote-Buang, Buang.
mms  Southern Mam  -  mms  Guatemala  1  159206  1084694  MMS  -  -  -  mvc mvj  en es  no  -  Mon Jan 7 20:05:27 CST 2013  SAN JUAN OSTUNCALCO MAM, OSTUNCALCO MAM, QUETZALTENANGO MAM, MAM QUETZALTECO  Mayan, Quichean-Mamean, Greater Mamean, Mamean.
mmx  Madak  -  mmx  Papua New Guinea  548  584454  3086399  MMX  -  -  -  emk  en  no  -  Fri Dec 28 21:16:10 CST 2012  MANDAK, LELET  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, Madak.
mn  Mongolian  Монгол  mon  Mongolia  2859  6716330  45890299  -  kha  mn  khk  bua  en ru  yes  Sanlig Badral  Fri Sep 13 12:48:05 CDT 2013  HALH, KHALKHA MONGOLIAN, MONGOL, CENTRAL MONGOLIAN  Altaic, Mongolian, Eastern, Oirat-Khalkha, Khalkha-Buriat, Mongolian Proper.
mn-Latn  Mongolian (Latin)  -  mon  Mongolia  271  506585  3378887  -  -  -  -  ur-Latn tr om xtn lnu  en  no  -  Mon Jan 21 23:04:38 CST 2013  HALH, KHALKHA MONGOLIAN, MONGOL, CENTRAL MONGOLIAN  Altaic, Mongolian, Eastern, Oirat-Khalkha, Khalkha-Buriat, Mongolian Proper.
mn-Mong  Mongolian (Mongolian)  -  mon  Mongolia  1442  1219227  10840946  -  -  -  khk_mong  -  en  no  -  Sat Sep 14 17:50:40 CDT 2013  HALH, KHALKHA MONGOLIAN, MONGOL, CENTRAL MONGOLIAN  Altaic, Mongolian, Eastern, Oirat-Khalkha, Khalkha-Buriat, Mongolian Proper.
mna  Mbula  -  mna  Papua New Guinea  0  0  0  MNA  -  -  -  gri pwg ksd leu kwf fj alu  en  no  -  -  MANGAP-MBULA, MANGAABA, MANGAAWA, MANGAAVA, MANGAP. KAIMANGA  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Ngero-Vitiaz, Vitiaz, Mangap-Mbula.
mnb  Muna  -  mnb  Indonesia (Sulawesi)  4  149094  1160938  MYN  -  -  -  ja-Latn  en  no  -  Tue Jan 8 08:43:44 CST 2013  WUNA, MOUNAN  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Sulawesi, Muna-Buton, Muna.
mnc  Manchu  -  mnc  China  135  103671  652176  MJF  -  -  -  snk id zsm tet iba  en  no  -  Wed Oct 9 10:57:49 CDT 2013  MAN  Altaic, Tungus, Southern, Southwest.
mnf  Mundani  -  mnf  Cameroon  1  239346  1085095  MUN  -  -  -  mnk bwu  en  no  -  Tue Jan 8 08:27:11 CST 2013  -  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Wide Grassfields, Narrow Grassfields, Momo.
mnk  Mandinka  -  mnk  Senegal  37  262027  1290533  MNK  -  -  -  emk dyu kao bm kus  en  no  Allan Callister  Tue Jan 8 08:53:36 CST 2013  MANDING, MANDINGO, MANDINGUE, MANDINQUE, MANDE, SOCÉ  Niger-Congo, Mande, Western, Central-Southwestern, Central, Manding-Jogo, Manding-Vai, Manding-Mokole, Manding, Manding-West.
mo  Moldavian  Молдовеняскэ  ron  Romania  20  91813  639165  RUM  -  mo  -  mhr  en  no  Mark Williamson  Sat Jan 19 08:13:05 CST 2013  RUMANIAN, MOLDAVIAN, DACO-RUMANIAN, MOLDOVAN  Indo-European, Italic, Romance, Eastern.
moa  Mwan  -  moa  Côte d’Ivoire  4  48476  245087  MOA  -  -  -  mzw kpe bwu  en  no  -  Mon Jan 21 21:48:59 CST 2013  MUAN, MONA, MOUAN, MUANA, MWA  Niger-Congo, Mande, Eastern, Southeastern, Nwa-Ben, Wan-Mwan.
moe  Montagnais  Innu-aimun  moe  Canada  8  61133  534831  MOE  -  -  -  nez cr-Latn qug csw-Latn  en fr  no  -  Thu Jan 3 21:25:50 CST 2013  INNU AIMUN, INNU  Algic, Algonquian, Central, Cree-Montagnais-Naskapi.
mog  Mongondow  -  mog  Indonesia (Sulawesi)  2  215466  1367047  MOG  -  -  -  blz ibl ubr  en  no  -  Tue Jan 8 09:43:19 CST 2013  BOLAANG MONGONDOW, MONGONDOU, MINAHASSA  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Sulawesi, Mongondow-Gorontalo, Mongondowic.
moh  Mohawk  Kanien’kéha  moh  Canada  84  178293  1249145  MOH  -  -  -  mbi zpi ppl ain aso ter mbt  en  no  -  Wed Sep 18 22:17:16 CDT 2013  -  Iroquoian, Northern Iroquoian, Five Nations, Mohawk-Oneida.
mop  Mopán Maya  -  mop  Belize  1  380411  1929587  MOP  -  -  -  lac chf  en  no  -  Sun Jan 6 19:51:02 CST 2013  MAYA MOPÁN, MOPANE  Mayan, Yucatecan, Mopan-Itza.
mos  Mòoré  Mòoré  mos  Burkina Faso  11  297078  1394597  MHM  mm  -  mhm  hag gur kus emk dga mnk bm  en fr  yes  -  Thu Jan 31 09:47:13 CST 2013  MOOSE, MORE, MOLE, MOSSI, MOSHI  Niger-Congo, Atlantic-Congo, Volta-Congo, North, Gur, Central, Northern, Oti-Volta, Western, Northwest.
mox  Molima  -  mox  Papua New Guinea  272  363078  2423403  MOX  -  -  -  bdd pwg gri  en  no  -  Fri Dec 28 21:20:53 CST 2012  EBADIDI, SALAKAHADI, MORIMA  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Nuclear, North Papuan Mainland-D'Entrecasteaux, Bwaidoga.
mpg  Marba  -  mpg  Chad  1  569  2888  MPG  -  -  -  gri pwg bmk  en  no  -  Mon Jan 28 06:52:26 CST 2013  'AZUMEINA, AZUMEINA, MARABA, KOLONG, KULUNG  Afro-Asiatic, Chadic, Masa.
mpj  Martu Wangka  -  mpj  Australia  3  2113  21050  MPJ  -  -  -  wmt wbp pjt piu ibd tiw  en  no  -  Mon Jan 21 21:56:34 CST 2013  -  Australian, Pama-Nyungan, South-West, Wati.
mpm  Yosondúa Mixtec  -  mpm  Mexico  2  452006  2121318  MPM  -  -  -  mxv  en  no  -  Thu Dec 27 19:32:54 CST 2012  SANTIAGO YOSONDÚA MIXTECO, YOSONDÚA MIXTEC, SOUTHERN TLAXIACO MIXTECO  Oto-Manguean, Mixtecan, Mixtec-Cuicatec, Mixtec.
mpp  Migabac  -  mpp  Papua New Guinea  0  0  0  MPP  -  -  -  ded big mbh jv pam jvn tl mee kmg ban  en  no  -  -  MIGABA'  Trans-New Guinea, Main Section, Central and Western, Huon-Finisterre, Huon, Eastern.
mps  Dadibi  -  mps  Papua New Guinea  0  0  0  MPS  -  -  -  hui tkl knv gux wls tvl imo  en  no  -  -  DARIBI, KARIMUI  Trans-New Guinea, Teberan-Pawaian, Teberan.
mpt  Mian  -  mpt  Papua New Guinea  0  0  0  MPT  -  -  -  knv knv-x-ara fai bhl knv-x-fly kqn teo  en  no  -  -  MIANMIN  Trans-New Guinea, Main Section, Central and Western, Central and South New Guinea-Kutubuan, Central and South New Guinea, Ok, Mountain.
mpx  Misima-Panaeati  -  mpx  Papua New Guinea  392  657575  3836434  MPX  -  -  -  tbo pwg sw mox gri  en  no  -  Fri Jan 25 21:07:58 CST 2013  PANAIETI, PANAEATI, PANEYATE, PANEATE, PANAYETI  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Peripheral, Kilivila-Louisiades, Misima.
mqb  Mbuko  -  mqb  Cameroon  1  302036  1397227  MQB  -  -  -  ami ifb pag ifk war  en  no  -  Tue Jan 8 09:44:44 CST 2013  MBUKU, MBOKU, MBOKOU  Afro-Asiatic, Chadic, Biu-Mandara, A, A.5.
mqj  Mamasa  -  mqj  Indonesia (Sulawesi)  0  0  0  MQJ  -  -  -  sda mvp ptu mak-Latn lcm su bjn sml slm lbb bik blz bbc-Latn msk  en  no  -  -  -  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Sulawesi, South Sulawesi, Northern, Toraja-Sa'dan.
mr  Marathi  मराठी  mar  India  2732  7523035  51481416  MRT  mr*  mr  mrt  hi ne new mai hne  en  yes  -  Wed Sep 11 08:53:27 CDT 2013  MAHARASHTRA, MAHARATHI, MALHATEE, MARTHI, MURUTHU  Indo-European, Indo-Iranian, Indo-Aryan, Southern zone.
mrh  Mara Chin  -  mrh  India  522  860248  5223620  MRH  -  -  -  ne-Latn qvs quh ign  en  no  -  Sun Mar 24 21:40:54 CDT 2013  LAKHER, ZAO, MARAM, MIRA, MARA  Sino-Tibetan, Tibeto-Burman, Kuki-Chin-Naga, Kuki-Chin, Southern.
mrj  Hill Mari  Марий  mrj  Russian Federation  2  213142  1556299  MRJ  mar  mrj  -  mhr ky  en ru  no  -  Mon Jan 21 21:55:00 CST 2013  CHEREMISS, MARI-HILLS, GORNO-MARIY, HIGH MARI  Uralic, Finno-Ugric, Finno-Permic, Finno-Cheremisic, Cheremisic.
ms  Malay  Bahasa Melayu  msa  Malaysia (Peninsular)  998  12110286  86719280  MLI  ml  ms  mli  su jv  en  yes  -  Fri Sep 13 12:21:08 CDT 2013  BAHASA MALAYSIA, BAHASA MALAYU, MALAYU, MELAJU, MELAYU, STANDARD MALAY  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Sundic, Malayic, Malayan, Local Malay.
ms-Arab  Malay (Arabic)  -  mly  Malaysia (Peninsular)  67  80070  513353  MLI  -  -  mly_arab  pes glk prs sd az-Arab ps bal  en  no  -  Sun Sep 15 15:36:38 CDT 2013  BAHASA MALAYSIA, BAHASA MALAYU, MALAYU, MELAJU, MELAYU, STANDARD MALAY  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Sundic, Malayic, Malayan, Local Malay.
ms-Thai  Malay (Thai)  -  msa  Thailand  0  0  0  -  -  -  -  th kxm pww  en th  no  -  -  ORAK LAWOI', LAWTA, CHAW TALAY, CHAWNAM, LAWOI  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Sundic, Malayic, Malayan, Para-Malay.
msk  Mansaka  -  msk  Philippines  0  0  0  MSK  -  -  -  kyk tl pam krj jv hil  en  no  -  -  MANDAYA MANSAKA  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Meso Philippine, Central Philippine, Mansakan, Eastern, Mandayan.
msm  Agusan Manobo  -  msm  Philippines  3  241440  1365025  MSM  -  -  -  mbd atd ibl ami pag ja-Latn  en  no  -  Tue Jan 8 09:50:06 CST 2013  AGUSAN  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Southern Philippine, Manobo, Central, East.
msw  Mansoanka  -  msw  Guinea-Bissau  0  0  0  MSW  -  -  -  gba ain ppl mbt mbi zpi gul  en  no  -  -  MANSOANCA, MASWANKA, SUA, KUNANT, KUNANTE  Niger-Congo, Atlantic-Congo, Atlantic, Southern, Sua.
msy  Aruamu  -  msy  Papua New Guinea  288  365868  2251919  MSY  -  -  -  pes-Latn bjn srb  en  no  -  Fri Dec 28 21:37:48 CST 2012  MIKAREW, ARIAWIAI, MAKARUP, MAKARUB, MIKARUP, MIKAREW-ARIAW  Sepik-Ramu, Ramu, Ramu Proper, Ruboni, Misegian.
mt  Maltese  Malti  mlt  Malta  4671  6557805  48804398  MLS  mt  mt  mls  tzs csk kek  en  yes  -  Thu Feb 7 09:35:15 CST 2013  MALTI  Afro-Asiatic, Semitic, Central, South, Arabic.
mta  Cotabato Manobo  -  mta  Philippines  2  259097  1404226  MTA  -  -  -  ceb hnn bps iry bpr bik hil su id bjn  en  no  -  Mon Sep 16 16:55:36 CDT 2013  -  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Southern Philippine, Manobo, South.
mti  Maiwa  -  mti  Papua New Guinea  0  0  0  MTI  -  -  -  dgz wmw sw swh ha pkb ain gdn  en  no  -  -  -  Trans-New Guinea, Main Section, Eastern, Central and Southeastern, Dagan.
mtj  Moskona  -  mtj  Indonesia (Irian Jaya)  0  0  0  MTJ  -  -  -  mej ja-Latn kwn  en  no  -  -  SABENA, MENINGGO, MENINGO  East Bird's Head, Meax.
mto  Totontepec Mixe  -  mto  Mexico  2  380842  2559988  MTO  -  -  -  ncu pps myu cjp crn zav  en  no  -  Thu Dec 27 19:35:20 CST 2012  NORTHWESTERN MIXE  Mixe-Zoque, Mixe, Western Mixe.
mua  Mundang  -  mua  Chad  1  9606  42418  MUA  ou  -  -  luo  en  no  -  Mon Jan 21 21:59:36 CST 2013  MOUNDAN, MOUNDANG, KAELE, NDA  Niger-Congo, Atlantic-Congo, Volta-Congo, North, Adamawa-Ubangi, Adamawa, Mbum-Day, Mbum, Northern, Tupuri-Mambai.
muh  Mündü  -  muh  Sudan  5  454332  2019508  MUH  -  -  -  kus mbt mi  en  no  -  Fri Jan 25 21:09:02 CST 2013  MUNDO, MOUNTOU, MONDU, MONDO  Niger-Congo, Atlantic-Congo, Volta-Congo, North, Adamawa-Ubangi, Ubangi, Sere-Ngbaka-Mba, Ngbaka-Mba, Ngbaka, Eastern, Mundu.
mur  Murle  -  mur  Sudan  1  209715  1149059  MUR  -  -  -  wo dag bm cwt dyu  en  no  -  Tue Jan 8 10:58:37 CST 2013  MURELEI, MERULE, MOURLE, MURULE, BEIR, AJIBBA, AGIBA, ADKIBBA  Nilo-Saharan, Eastern Sudanic, Eastern, Surmic, South, Southwest, Didinga-Murle, Murle.
mus  Muskogee  Mvskoke  mus  USA  4  20286  147690  CRK  -  mus  -  nl da nb  en  no  -  Thu Jan 24 21:11:05 CST 2013  CREEK, MUSCOGEE  Muskogean, Eastern.
mux  Bo-Ung  -  mux  Papua New Guinea  0  0  0  MUX  -  -  -  ubu-x-nopenge ubu-x-andale ubu-x-kala imo med tsc ny-x-nya xog loz lch  en  no  -  -  TEMBALO, BO-UNG, MBOUNG  Trans-New Guinea, Main Section, Central and Western, East New Guinea Highlands, Central, Hagen, Kaugel.
mva  Manam  -  mva  Papua New Guinea  0  0  0  MVA  -  -  -  mee stn mmn su krj bch iba zne  en  no  -  -  MANUM  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Schouten, Kairiru-Manam, Manam.
mvc  Central Mam  -  mvc  Guatemala  2  346169  2039696  MVC  -  -  -  mms ttc mvj knj kjb cnm tzh mop jac agu hva lac  en  no  -  Thu Dec 27 19:36:10 CST 2012  COMITANCILLO MAM, WESTERN MAM, MAM OCCIDENTAL, MAM MARQUENSE, SAN MARCOS COMITANCILLAS MAM  Mayan, Quichean-Mamean, Greater Mamean, Mamean.
mvj  Todos Santos Cuchumatán Mam  -  mvj  Guatemala  2  256923  1505785  MVJ  -  -  -  mms ttc mvc knj kjb tzh agu  en  no  -  Thu Dec 27 20:46:32 CST 2012  -  Mayan, Quichean-Mamean, Greater Mamean, Mamean.
mvp  Duri  -  mvp  Indonesia (Sulawesi)  1  168347  1165898  MVP  -  -  -  su msk lcm kyk pam  en  no  -  Tue Jan 8 10:58:57 CST 2013  MASENREMPULU, MASSENREMPULU  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Sulawesi, South Sulawesi, Northern, Masenrempulu.
mwc  Are  -  mwc  Papua New Guinea  0  0  0  MWC  -  -  -  pwg bmk aui wed kqf tte rro yml tpa dob kud wed-x-topura meu mpx gdn viv khz gri tbo fj sbe stn  en  no  -  -  MUKAWA  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Nuclear, North Papuan Mainland-D'Entrecasteaux, Are-Taupota, Are.
mwl  Mirandese  Mirandés  mwl  Portugal  1419  8159801  46009720  MWL  -  mwl  -  es cbk an oc lad ast ca-valencia gl pt  en  no  José Pedro Ferreira  Fri Sep 13 10:34:07 CDT 2013  MIRANDA DO DOURO, MIRANDESA, MIRANDES  Indo-European, Italic, Romance, Italo-Western, Western, Gallo-Iberian, Ibero-Romance, West Iberian, Asturo-Leonese.
mwp  Kala Lagaw Ya  -  mwp  Australia  173  231848  1667198  MWP  -  -  -  wim war itv  en  no  -  Thu Jan 24 21:15:53 CST 2013  KALA YAGAW YA, YAGAR YAGAR, MABUIAG, KALA LAGAU LANGGUS, LANGUS, KALA LAGAW  Australian, Pama-Nyungan, Kala Lagaw Ya.
mwq  Mün Chin  -  mwq  Myanmar  1  276446  1252300  MWQ  -  -  -  cnh cnk bgr tl  en  no  -  Wed Jan 30 06:47:14 CST 2013  MÜN, NG'MEN, CHO, YAWDWIN, MINDAT, 'CHINBOK'  Sino-Tibetan, Tibeto-Burman, Kuki-Chin-Naga, Kuki-Chin, Southern.
mwv  Mentawai  Mentawai  mwv  Indonesia (Sumatra)  3  143194  994578  MWV  mwi  -  -  btx hnn lcm sml bjn  en id  no  -  Wed Sep 18 22:20:25 CDT 2013  MENTAWEI, MENTAWI  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Sundic, Sumatra, Mentawai.
mww  White Miao  -  mww  China  4  5889  31483  MWW  -  -  -  csa eo lt  en  no  -  Wed Sep 18 22:21:23 CDT 2013  WHITE MEO, WHITE MIAO, MEO KAO, WHITE LUM, PEH MIAO, PE MIAO, CHUAN MIAO, BAI MIAO  Hmong-Mien, Hmongic, Chuanqiandian.
mxb  Tezoatlán Mixtec  -  mxb  Mexico  6  414484  1997317  MXB  -  -  -  mim mks mig otn miu xtn mxv mpm mzi trq mza cta tcf  en  no  -  Thu Dec 27 19:52:05 CST 2012  TEZOATLÁN DE SEGURA Y LUNA MIXTECO  Oto-Manguean, Mixtecan, Mixtec-Cuicatec, Mixtec.
mxi  Mozarabic  -  mxi  Spain  1  1946  13125  MXI  -  -  moz  ia es fr ast lnc ca it cbk oc pt gl lad  en  no  -  Mon Dec 9 14:13:43 CST 2013  -  Indo-European, Italic, Romance, Italo-Western, Western, Pyrenean-Mozarabic, Mozarabic.
mxp  Tlahuitoltepec Mixe  -  mxp  Mexico  5  250597  1722298  MXP  -  -  -  toj tzt mxq fit shp smj cbs liv vro se  en  no  -  Thu Dec 27 19:51:26 CST 2012  WEST CENTRAL MIXE  Mixe-Zoque, Mixe, Western Mixe.
mxq  Juquila Mixe  -  mxq  Mexico  31  210421  1380907  MXQ  -  -  -  mxp toj tzt fit smj shp cbs vro se ekk fkv  en  no  -  Tue Oct 2 10:47:46 CDT 2012  SOUTH CENTRAL MIXE  Mixe-Zoque, Mixe, Eastern Mixe.
mxt  Jamiltepec Mixtec  -  mxt  Mexico  6  399264  2016236  MXT  -  -  -  mio  en  no  -  Wed Sep 18 22:22:26 CDT 2013  EASTERN JAMILTEPEC-SAN CRISTOBAL MIXTECO  Oto-Manguean, Mixtecan, Mixtec-Cuicatec, Mixtec.
mxv  Metlatónoc Mixteco  Tu'un Sávi  mxv  Mexico  32  70052  385539  MXV  -  -  mxv  fj dig rnd miq ts  en es  no  Joaquin J. Martínez  Fri Sep 13 10:41:08 CDT 2013  SAN RAFAEL MIXTECO  Oto-Manguean, Mixtecan, Mixtec-Cuicatec, Mixtec.
my  Myanmar  မြန်မာဘာသာ  mya  Myanmar  4  2324400  29885389  BMS  bu  my  bms  pi-Mymr ksw  en  started  Ngwe Tun  Wed Sep 11 09:12:57 CDT 2013  BAMA, BAMACHAKA, MYEN  Sino-Tibetan, Tibeto-Burman, Lolo-Burmese, Burmish, Southern.
myk  Mamara Senoufo  -  myk  Mali  1  265923  1172037  MYK  -  -  -  fj lef ln gri amu  en  no  -  Tue Jan 8 18:21:09 CST 2013  MINIYANKA, MINYA, MIANKA, MINIANKA, MAMARA, TUPIIRE  Niger-Congo, Atlantic-Congo, Volta-Congo, North, Gur, Senufo, Suppire-Mamara.
myu  Mundurukú  -  myu  Brazil  2  322289  1954677  MYU  -  -  -  mav rai byx mva kup  en  no  -  Thu Dec 27 19:55:17 CST 2012  MUNDURUCU, WEIDYENYE, PAIQUIZE, PARI, CARAS-PRETAS  Tupi, Munduruku.
myv  Erzya  Эрзянь  myv  Russian Federation  3  207835  1573043  MYV  ez  myv  -  mdf  en  no  -  Fri Jan 25 21:19:52 CST 2013  MORDVIN-ERZYA, MORDVIN, ERZIA  Uralic, Finno-Ugric, Finno-Permic, Finno-Cheremisic, Finno-Mordvinic, Mordvinic.
myw  Muyuw  -  myw  Papua New Guinea  0  0  0  MYW  -  -  -  pag aai tbc ifk kne bnc  en  no  -  -  MUYU, MUYUA, MURUA, MURUWA, MUYUWA  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Peripheral, Kilivila-Louisiades, Kilivila.
myy  Macuna  -  myy  Colombia  1  276868  1686278  MYY  -  -  -  bsn tav bao gvc des cbc  en  no  -  Sun Jan 6 19:52:39 CST 2013  MAKUNA, BUHAGANA, ROEA, EMOA, IDE, YEBA, SUROA, TABOTIRO JEJEA, UMUA, WUHÁNA, PANEROA, JEPA-MATSI, YEPÁ-MAHSÁ  Tucanoan, Eastern Tucanoan, Central, Southern.
mza  Santa María Zacatepec Mixtec  -  mza  Mexico  10  184502  934453  MZA  -  -  -  mio  en es  no  -  Thu Dec 27 19:59:27 CST 2012  ZACATEPEC MIXTEC, SANTA MARÍA ZACATEPEC MIXTEC, SOUTHERN PUTLA MIXTECO, 'TACUATE'  Oto-Manguean, Mixtecan, Mixtec-Cuicatec, Mixtec.
mzi  Ixcatlán Mazatec  -  mzi  Mexico  5  111628  643528  MAO  -  -  mao  vmy maj  en es  no  -  Wed Jan 30 20:41:46 CST 2013  SAN PEDRO IXCATLÁN MAZATECO  Oto-Manguean, Popolocan, Mazatecan.
mzk  Nigeria Mambila  -  mzk  Nigeria  1  269596  1176037  MZK  -  -  -  icr bzj bum  en  no  -  Tue Jan 8 18:21:35 CST 2013  MAMBILLA, MABILA, MAMBERE, NOR, NOR TAGBO, LAGUBI, TONGBO, BANG  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Northern, Mambiloid, Mambila-Konja, Mambila.
mzm  Mumuye  -  mzm  Nigeria  1  265047  1235678  MUL  -  -  -  dga jv pam tl  en  no  -  Tue Jan 8 18:21:55 CST 2013  YORO  Niger-Congo, Atlantic-Congo, Volta-Congo, North, Adamawa-Ubangi, Adamawa, Leko-Nimbari, Mumuye-Yandang, Mumuye.
mzn  Mazanderani  ﻡَﺯِﺭﻮﻨﻳ  mzn  Iran  2  64231  345179  MZN  -  mzn  -  pes bal prs  en  no  -  Thu Jan 10 21:58:28 CST 2013  TABRI, MAZANDARANI  Indo-European, Indo-Iranian, Iranian, Western, Northwestern, Caspian.
mzw  Deg  -  mzw  Ghana  1  232539  1018797  MZW  -  -  -  dga xsm  en  no  -  Tue Jan 8 20:35:14 CST 2013  DEGHA, MO, MMFO, ACULO, JANELA, BURU  Niger-Congo, Atlantic-Congo, Volta-Congo, North, Gur, Central, Southern, Grusi, Western.
mzz  Maiadomu  -  mzz  Papua New Guinea  0  0  0  MZZ  -  -  -  kqf mox aui pwg viv kud dob sbe bmk mwc dww  en  no  -  -  -  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Nuclear, North Papuan Mainland-D'Entrecasteaux, Bwaidoga.
na  Nauruan  Dorerin Naoero  nau  Nauru  3  13633  83720  NRU  nr  na  -  jv-x-bms  en  no  -  Sat Jan 19 08:51:59 CST 2013  -  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Micronesian, Nauruan.
nab  Southern Nambikuára  -  nab  Brazil  1  988436  4148298  NAB  -  -  -  esk toc dws  en  no  -  Sun Jan 6 20:08:51 CST 2013  NAMBIQUARA, NAMBIKWARA  Nambiquaran.
naf  Nabak  -  naf  Papua New Guinea  0  0  0  NAF  -  -  -  stl buk lia ntr nop dah nl tbc  en  no  -  -  NABA, WAIN  Trans-New Guinea, Main Section, Central and Western, Huon-Finisterre, Huon, Western.
nah  Náhuatl  Nāhuatl  nah  Mexico  86  3148915  23764604  NAI  nht  nah  nhn  ppl mcd cya  en es  no  Rada Mihalcea  Wed Jan 9 14:34:50 CST 2013  EASTERN HUASTECA AZTEC, HIDALGO NÁHUATL, HUASTECA NÁHUATL  Uto-Aztecan, Southern Uto-Aztecan, Aztecan, General Aztec, Aztec.
nai-x-huave  Huave  -  nai  Mexico  0  0  0  -  -  -  -  tl agn bjn msk hil pam kyk bku su  en es  no  Sam Herrera  -  -  Huavean.
nak  Nakanai  -  nak  Papua New Guinea  281  455648  2443504  NAK  -  -  -  eo  en  no  -  Fri Dec 28 21:40:00 CST 2012  NAKONAI  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, Willaumez.
nan  Min Nan Chinese  Bân-lâm-gú  nan  China  189  819885  5585801  -  -  zh-min-nan  -  cdo hak vi tl  en  no  -  Tue Jan 29 21:06:53 CST 2013  Minnan, Southern Min  Sino-Tibetan, Chinese.
nap  Napoletano-Calabrese  Napulitano  nap  Italy  63  648372  3934768  NPL  -  nap  -  lij scn-x-tara it to fur sc  en it  no  -  Thu Jan 24 21:19:55 CST 2013  NEAPOLITAN-CALABRESE, NEAPOLITAN, NNAPULITANO  Indo-European, Italic, Romance, Italo-Western, Italo-Dalmatian.
naq  Nama  Nàmá  naq  Namibia  28  56963  336194  NAQ  na  -  -  sba pap pap-CW ksd sat mpx mfi ttg chr-Latn  en  no  -  Wed Sep 11 12:55:38 CDT 2013  NAMAN, NAMAKWA, NAMAQUA, MAQUA, TAMA, TAMMA, TAMAKWA, BERDAMA, BERGDAMARA, KAKUYA BUSHMAN NASIE, ROOI NASIE, 'HOTTENTOT', 'KLIPKAFFER', 'KLIPKAFFERN', 'KHOEKHOEGOWAP', 'KHOEKHOEGOWAB'  Khoisan, Southern Africa, Central, Nama.
nas  Naasioi  -  nas  Papua New Guinea  21  168144  1521386  NAS  -  -  -  pam jv jvn agn tl ban lnu msk wsk  en  no  -  Mon Sep 23 10:03:15 CDT 2013  NASIOI, KIETA, KIETA TALK, AUNGE  East Papuan, Bougainville, East, Nasioi.
nb  Norwegian Bokmål  Norsk bokmål  nob  Norway  1136  2868198  19311770  NRR  n  no  nrr  nn da sv jut nl-NL  en  yes  Trond Trosterud  Fri Sep 13 12:47:21 CDT 2013  BOKMAAL, RIKSMAAL, DANO-NORWEGIAN, NORWEGIAN  Indo-European, Germanic, North, East Scandinavian, Danish-Swedish, Danish-Bokmal, Bokmal.
nba  Nyemba  -  nba  Angola  4  12505  76119  NBA  -  -  nba  lch lue  en  no  -  Fri Sep 13 15:25:26 CDT 2013  GANGUELA, GANGUELLA, NGANGELA, NHEMBA, GANGELA  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, K, Chokwe-Luchazi (K.20).
nca  Iyo  -  nca  Papua New Guinea  0  0  0  NCA  -  -  -  mgd luo car adh imo ff bfa  en  no  -  -  NAHO, NABU  Trans-New Guinea, Main Section, Central and Western, Huon-Finisterre, Finisterre, Gusap-Mot.
ncg  Nisga’a  Nisg̱a’a  ncg  Canada  0  0  0  NCG  -  -  -  git hai gwi  en  no  -  -  NASS, NISKA, NISHKA, NISK'A, NISHGA  Penutian, Tsimshian.
nch  Central Huasteca Nahuatl  -  nch  Mexico  2  274512  2118644  NCH  nhh  -  -  nhw nhe azz  en es  no  -  Thu Dec 27 20:05:14 CST 2012  -  Uto-Aztecan, Southern Uto-Aztecan, Aztecan, General Aztec, Aztec.
ncj  Northern Puebla Nahuatl  -  ncj  Mexico  62  327342  2534920  NCJ  -  -  -  azz  en es  no  -  Tue Feb 5 22:02:33 CST 2013  NORTH PUEBLA AZTEC  Uto-Aztecan, Southern Uto-Aztecan, Aztecan, General Aztec, Aztec.
ncl  Michoacán Nahuatl  -  ncl  Mexico  5  354586  2584910  NCL  -  -  -  nch nhw ncj nhe nuz azz nhi ngu hva  en es  no  -  Thu Dec 27 20:06:28 CST 2012  MICHOACÁN NAHUAL, MICHOACÁN AZTEC  Uto-Aztecan, Southern Uto-Aztecan, Aztecan, General Aztec, Aztec.
ncu  Chumburung  -  ncu  Ghana  1  285904  1537889  NCU  -  -  -  trc zat  en  no  -  Tue Jan 8 20:35:54 CST 2013  NCHUMBURUNG, NCHIMBURU, NCHUMMURU, KYONGBORONG  Niger-Congo, Atlantic-Congo, Volta-Congo, Kwa, Nyo, Potou-Tano, Tano, Guang, North Guang.
nd  Ndebele  isiNdebele  nde  Zimbabwe  3  57764  502003  NDF  -  -  -  zu xh nr ss  en  no  -  Wed Sep 18 22:24:07 CDT 2013  TABELE, TEBELE, ISINDE'BELE, SINDEBELE, NORTHERN NDEBELE  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, S, Nguni (S.40).
ndc  Ndau  Cindau  ndc  Zimbabwe  1  1009  7730  NDC  nda  -  -  sn kwn rw tum hz lue  en  no  James Mlambo  Sat Jan 19 10:01:01 CST 2013  CHINDAU, NDZAWU, NJAO, SOUTHEAST SHONA, SOFALA  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, S, Shona (S.10).
ndh  Ndali  Kindali  ndh  Tanzania  4  1061  7429  NDH  -  -  -  bem ng lue tum kj cjk sw xog bda swh swc suk  en sw  no  Oliver Stegen  Thu Dec 19 08:38:28 CST 2013  -  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, M, Nyika-Safwa (M.20).
nds  Low Saxon  Plattdüütsch  nds  Germany  1632  5569756  34928258  SXN  lwx  nds  ige  nl lb de ksh fy zea li vls pdc  en nl de  yes  Heiko Evermann  Wed Jan 30 20:50:36 CST 2013  NEDDERSASSISCH, NIEDERSAECHSISCH, NEDERSAKSISCH, LOW GERMAN, PLATTDNNTSCH, NEDDERDNNTSCH  Indo-European, Germanic, West, Low Saxon-Low Franconian, Low Saxon.
nds-NL  Dutch Low Saxon  -  nds  Netherlands  2  955631  5958577  SXN  -  nds-nl  -  vls zea nl li fy nds  en  no  -  Fri Sep 13 11:21:42 CDT 2013  NEDDERSASSISCH, NIEDERSAECHSISCH, NEDERSAKSISCH, LOW GERMAN, PLATTDNNTSCH, NEDDERDNNTSCH  Indo-European, Germanic, West, Low Saxon-Low Franconian, Low Saxon.
ndz  Ndogo  -  ndz  Sudan  1  342814  1394260  NDZ  -  -  -  mza mim kkj  en  no  -  Tue Jan 8 20:35:39 CST 2013  -  Niger-Congo, Atlantic-Congo, Volta-Congo, North, Adamawa-Ubangi, Ubangi, Sere-Ngbaka-Mba, Sere, Sere-Bviri, Ndogo-Sere.
ne  Nepali  नेपाली  nep  Nepal  252  1435795  9638238  NEP  np*  ne  nep  hi mai mr new hne  en  yes  Krishna Parajuli  Thu Feb 7 09:05:29 CST 2013  NEPALESE, GORKHALI, GURKHALI, KHASKURA, PARBATIYA, EASTERN PAHARI  Indo-European, Indo-Iranian, Indo-Aryan, Northern zone, Eastern Pahari.
ne-Latn  Nepali (Latin)  -  nep  Nepal  2  25302  156205  NEP  -  -  -  aia npy pwg hi-Latn  en hi-Latn  no  -  Sat Jan 19 10:04:52 CST 2013  NEPALESE, GORKHALI, GURKHALI, KHASKURA, PARBATIYA, EASTERN PAHARI  Indo-European, Indo-Iranian, Indo-Aryan, Northern zone, Eastern Pahari.
neb  Toura  -  neb  Côte d’Ivoire  1  306315  1431497  NEB  -  -  -  sm moa fud  en  no  -  Tue Jan 8 20:56:25 CST 2013  TURA, WEEN  Niger-Congo, Mande, Eastern, Southeastern, Guro-Tura, Tura-Dan-Mano, Tura-Dan.
neg  Negidal  -  neg  Russian Federation  5  12010  86963  NEG  -  -  -  ulc eve gld bua sah ude  en ru  no  Elena Klyachko  Sun Feb 3 20:41:42 CST 2013  NEGIDALY, NEGHIDAL  Altaic, Tungus, Northern, Negidal.
nen  Nengone  Nengone  nen  New Caledonia  2  14703  72973  NEN  re  -  -  dhv ckk gym it ain  en  no  -  Fri Sep 13 15:31:06 CDT 2013  MARÉ, IWATENU  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Loyalty Islands.
new  Nepal Bhasa  नेपालभास।  new  Nepal  233  1377482  8784268  NEW  -  new  -  mr ne mai hi  en  no  Prabindra Shakya  Wed Sep 11 14:25:28 CDT 2013  NEPAL BHASA, NEWAR  Sino-Tibetan, Tibeto-Burman, Himalayish, Mahakiranti, Newari.
nez  Nez Perce  Niimiipuutímt  nez  USA  2  9461  75245  NEZ  -  -  -  qug  en  no  Phil Cash Cash  Wed Jul 4 20:57:33 CDT 2012  -  Penutian, Plateau Penutian, Sahaptin.
nfr  Nafaanra  -  nfr  Ghana  1  232743  999464  NFR  -  -  -  amu gri fj myk ln ki  en  no  -  Tue Jan 8 20:56:38 CST 2013  NAFANA, NAFAARA, PANTERA-FANTERA, BANDA, DZAMA, GAMBO  Niger-Congo, Atlantic-Congo, Volta-Congo, North, Gur, Senufo, Nafaanra.
ng  Ndonga  Oshiwambo  ndo  Namibia  58  174045  1166959  NDG  od  ng  1114  kj swh bem nyk ts  en  no  -  Wed Sep 11 10:07:03 CDT 2013  OCHINDONGA, OSHINDONGA, OSINDONGA, OTJIWAMBO, OWAMBO, AMBO, OSHIWAMBO  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, R, Ndonga (R.20).
ngl  Lomwe  Elomwe  ngl  Mozambique  1  8624  66244  NGL  le  -  -  vmw chw dig dug nyf loz  en  no  -  Thu Jan 24 21:16:17 CST 2013  NGULU, INGULU, NGURU, MIHAVANE, MIHAVANI, MIHAWANI, WESTERN MAKUA, LOMUE, ILOMWE, ELOMWE, ALOMWE, WALOMWE, CHILOWE, CILOWE, ACILOWE  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, P, Makua (P.30).
ngu  Guerrero Nahuatl  -  ngu  Mexico  12  502418  3871753  NAH  nhg  -  -  nuz nhe nhw ncj azz nhi nch ncl nhm  en es  no  -  Fri Sep 13 12:21:21 CDT 2013  GUERRERO AZTEC  Uto-Aztecan, Southern Uto-Aztecan, Aztecan, General Aztec, Aztec.
nhe  Eastern Huasteca Nahuatl  -  nhe  Mexico  2  277675  2172273  NAI  nhh  -  -  nhw nch  en es  no  -  Thu Dec 27 20:06:55 CST 2012  EASTERN HUASTECA AZTEC, HIDALGO NÁHUATL, HUASTECA NÁHUATL  Uto-Aztecan, Southern Uto-Aztecan, Aztecan, General Aztec, Aztec.
nhg  Tetelcingo Nahuatl  -  nhg  Mexico  2  245286  1829108  NHG  -  -  -  nhw nhe azz es-x-cant nuz nch ngu ncj pt-BR  en es  no  -  Thu Dec 27 20:08:15 CST 2012  TETELCINGO AZTEC  Uto-Aztecan, Southern Uto-Aztecan, Aztecan, General Aztec, Aztec.
nhi  Zacatlán-Ahuacatlán-Tepetzintla Nahuatl  -  nhi  Mexico  1  200574  1498597  -  -  -  -  ncj nhe azz nhw ngu ncl nhn nsu  en es  no  -  Sun Jan 6 20:42:58 CST 2013  Ahuacatlán and Tepetzintla, Ahuacatlán y Tepetzintla, Aztec of Zacatlán, Náhuatl de Zacatlán, Tenango Nahuatl  Uto-Aztecan, Southern Uto-Aztecan, Aztecan, General Aztec, Aztec.
nhm  Morelos Nahuatl  -  nhm  Mexico  1  15284  104884  NHM  -  -  -  nhn nhy nhi ngu nsu nhe ncj nhw azz  en es  no  -  Sun Jan 6 20:57:04 CST 2013  -  Uto-Aztecan, Southern Uto-Aztecan, Aztecan, General Aztec, Aztec.
nhn  Central Náhuatl  Nauatlajtoli  nhn  Mexico  2  7252  57362  NHN  nhc  -  -  nhy nhm nsu npl nhi  en es  no  -  Wed Sep 18 22:26:32 CDT 2013  CENTRAL AZTEC, TLAXCALA-PUEBLA NÁHUATL  Uto-Aztecan, Southern Uto-Aztecan, Aztecan, General Aztec, Aztec.
nhs  Southeastern Puebla/Sierra Negra Nahuatl  -  nhs  Mexico  5  44676  313579  NHS  -  -  -  nhy nhm nhn nhi nuz nhe nhw ngu ncj ppl  en es  no  -  Mon Sep 23 20:40:44 CDT 2013  SOUTHEASTERN PUEBLA NÁHUATL, TEHUACÁN NÁHUATL  Uto-Aztecan, Southern Uto-Aztecan, Aztecan, General Aztec, Aztec.
nhu  Noone  -  nhu  Cameroon  1  270317  1182090  NHU  -  -  -  moa gbo  en  no  -  Tue Jan 8 21:13:19 CST 2013  NONI, NOORI  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Beboid, Eastern.
nhw  Western Huasteca Nahuatl  -  nhw  Mexico  2  272164  2159232  NHW  nhh  -  -  nhe nch  en es  no  -  Thu Dec 27 20:10:52 CST 2012  WESTERN HUASTECA AZTEC, TAMAZUNCHALE NÁHUATL, HUASTECA NÁHUATL  Uto-Aztecan, Southern Uto-Aztecan, Aztecan, General Aztec, Aztec.
nhx  Isthmus-Mecayapan Nahuatl  -  nhx  Mexico  5  140271  972792  NAU  -  -  -  nuz nch ngu ncl nhw nhe azz sei nhg nhi ncj  en es  no  -  Thu Dec 27 20:10:42 CST 2012  ISTHMUS NAHUAT, ISTHMUS AZTEC, MECAYAPAN NAHUAT  Uto-Aztecan, Southern Uto-Aztecan, Aztecan, General Aztec, Aztec.
nhy  Northern Oaxaca Nahuatl  -  nhy  Mexico  5  286960  2077262  NHY  -  -  -  nhn  en es  no  -  Thu Dec 27 20:12:03 CST 2012  OAXACA NORTE NÁHUATL  Uto-Aztecan, Southern Uto-Aztecan, Aztecan, General Aztec, Aztec.
nia  Nias  Nias  nia  Indonesia (Sumatra)  2  187505  1121590  NIP  ni  -  -  lol miq dua  en  no  -  Fri Jan 25 21:25:47 CST 2013  BATU  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Sundic, Sumatra, Northern.
nif  Nek  -  nif  Papua New Guinea  0  0  0  NIF  -  -  -  ian kmh-x-mini gdr aoj-x-filifita puu bjn ha tbc  en  no  -  -  -  Trans-New Guinea, Main Section, Central and Western, Huon-Finisterre, Finisterre, Erap.
nii  Nii  -  nii  Papua New Guinea  0  0  0  NII  -  -  -  med kms fai dak lkt pon  en  no  -  -  EK NII  Trans-New Guinea, Main Section, Central and Western, East New Guinea Highlands, Central, Wahgi.
nij  Ngaju  Ngaju  nij  Indonesia (Kalimantan)  45  255363  1586439  NIJ  -  -  -  su bjn jv-x-bms jv ms pam  en  no  -  Tue Sep 10 20:03:04 CDT 2013  NGADJU, NGAJU DAYAK, BIADJU, SOUTHWEST BARITO  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Borneo, Barito, West, South.
nim  Nilamba  -  nim  Tanzania  1  116330  903683  NIM  -  -  -  sw kki  en  no  -  Wed Jan 9 12:15:01 CST 2013  NYILAMBA, IKINILAMBA, IRAMBA, NILYAMBA, IKINIRAMBA, ILAMBA, NIRAMBA, KINIRAMBA  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, F, Nyilamba-Langi (F.30).
nin  Ninzo  -  nin  Nigeria  0  0  0  NIN  -  -  -  zne znd dig tsc loz sop cri ts rw mhi sw nyf xsm kck  en  no  -  -  NINZO, NUNZO, GBHU D AMAR RANDFA, AMAR TITA, ANCHA (INCHA), KWASU (AKIZA), SAMBE, FADAN WATE (HATE)  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Platoid, Plateau, Western, Southwestern, A.
niu  Niue  Niuē  niu  Niue  134  313952  1714045  NIQ  nn  -  -  tkl to wls tvl fud  en  no  Emani Fakaotimanava-Lui  Wed Sep 18 22:28:54 CDT 2013  NIUEAN, 'NIUEFEKAI'  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Central Pacific, East Fijian-Polynesian, Polynesian, Tongic.
niv  Gilyak  Нивхгу диф  niv  Russian Federation  2  4036  26656  NIV  -  -  Nivkh*  lez cv mk bg sah tg be  en  no  -  Wed Sep 18 22:29:35 CDT 2013  NIVKH, NIVKHI  Language Isolate.
njo  Ao Naga  Ao  njo  India  49  72473  493607  NJO  -  -  njo  pam jv agn tl su jvn  en  no  -  Wed Sep 18 22:30:28 CDT 2013  AORR, PAIMI, CHOLIMI, NOWGONG, HATIGORIA, URI, AO  Sino-Tibetan, Tibeto-Burman, Kuki-Chin-Naga, Naga, Ao.
nko  Nkonya  -  nko  Ghana  2  268424  1531448  NKO  -  -  -  sld ktj lem  en  no  -  Thu Dec 27 20:14:29 CST 2012  -  Niger-Congo, Atlantic-Congo, Volta-Congo, Kwa, Nyo, Potou-Tano, Tano, Guang, North Guang.
nl  Dutch  Nederlands  nld  Netherlands  2130  5672363  36119864  DUT  o  nl  dut  nds-NL vls zea li nds fy de lb af da  en  yes  Anneke Bart  Mon Feb 4 13:31:49 CST 2013  NEDERLANDS, HOLLANDS  Indo-European, Germanic, West, Low Saxon-Low Franconian, Low Franconian.
nl-BE  Dutch (Belgium)  Nederlands  nld  Belgium  321  534228  3417031  DUT  o  -  -  nds-NL vls zea li nds fy de lb af da  en  started  Anneke Bart  Wed Jan 23 22:37:04 CST 2013  NEDERLANDS, HOLLANDS  Indo-European, Germanic, West, Low Saxon-Low Franconian, Low Franconian.
nl-NL  Dutch (Netherlands)  Nederlands  nld  Netherlands  166  177382  1215305  DUT  o  -  -  nds-NL vls zea li nds fy de lb af da  en  started  Anneke Bart  Wed Jan 23 22:36:14 CST 2013  NEDERLANDS, HOLLANDS  Indo-European, Germanic, West, Low Saxon-Low Franconian, Low Franconian.
nmf  Tangkhul Naga  -  nmf  India  3  9532  74654  NMF  tt  -  -  lcm su  en  no  -  Sat Jan 19 10:24:09 CST 2013  TANGKHUL, TAGKHUL, THANGKHULM, CHAMPHUNG, LUHUPPA, LUPPA, SOMRA  Sino-Tibetan, Tibeto-Burman, Kuki-Chin-Naga, Naga, Tangkhul.
nn  Norwegian Nynorsk  Norsk nynorsk  nno  Norway  1397  10949076  69219261  NRN  -  nn  nrn  nb sv da  en  yes  Trond Trosterud  Mon Jan 21 00:44:17 CST 2013  LANDSMAAL, NEW NORSE, NYNORSK, NORWEGIAN  Indo-European, Germanic, North, West Scandinavian.
nnb  Nandi  Kinande  nnb  Dem. Rep. of Congo  1  1085  9384  NNB  kin  -  -  koo mho ttj  en  no  -  Thu Jan 24 21:16:51 CST 2013  KINANDI, KINANDE, NANDE, NORTHERN NANDE, NDANDE, ORUNDANDE  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, J, Konzo (J.40).
nnd  West Ambae  -  nnd  Vanuatu  1  1123  5743  NND  -  -  -  bnp gil stn gri kwf  en  no  -  Sat Feb 16 07:18:43 CST 2013  OPA  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, East Vanuatu.
nnw  Southern Nuni  -  nnw  Burkina Faso  1  287426  1245022  NNW  -  -  -  gde yam  en  no  -  Wed Jan 9 12:14:34 CST 2013  NOUNI, NUNUMA, NOUNOUMA, NUNA, NUNE, NIBULU, NURUMA  Niger-Congo, Atlantic-Congo, Volta-Congo, North, Gur, Central, Southern, Grusi, Northern.
no  Norwegian  Norsk  nor  Norway  3300  6534653  42887077  -  -  -  -  da sv  en  yes  -  Fri Sep 13 12:50:12 CDT 2013  -  Indo-European, Germanic, North, East Scandinavian, Danish-Swedish
noa  Woun Meu  -  noa  Panama  3  313683  2094791  NOA  -  -  -  ood ifu hi-Latn  en  no  -  Sun Jan 6 21:38:09 CST 2013  WAUN MEO, WAUNANA, WAUMEO, WOUNMEU, WOUNAAN, NOANAMA, NOENAMA, NONAMA, CHOCAMA, CHANCO  Choco.
nod  Northern Thai  กำเมือง  nod  Thailand  8  958  11720  NOD  -  -  -  en  en  no  -  Wed Oct 9 11:18:47 CDT 2013  LANNA, LAN NA, LANATAI, 'YUAN', PHYAP, PHAYAP, PAYAP, KAMMÜANG, KAMMYANG, MYANG, KAM MU'ANG, MU'ANG, KHON MUNG, KHON MYANG, TAI NYA, LA NYA, NORTHERN THAI, WESTERN LAOTIAN  Tai-Kadai, Kam-Tai, Be-Tai, Tai-Sek, Tai, Southwestern, East Central, Chiang Saeng.
nog  Nogai  Ногай тили  nog  Russian Federation  484  356175  2627618  NOG  -  -  -  kaa-Cyrl ky kk uz tt uzn alt gag-Cyrl tyv kum tk-Cyrl sah ru  en ru  no  Fran Tyers  Tue Oct 1 11:59:23 CDT 2013  NOGAY, NOGHAY, NOGHAI, NOGHAYLAR, NOGAITSY, NOGALAR  Altaic, Turkic, Western, Aralo-Caspian.
non  Old Norse  Norrœnt  non  -  3  10217  56280  -  -  -  -  is fo nn nb mfe sv  en  no  -  Wed Sep 18 22:33:05 CDT 2013  -  -
noo  Nuu-Chah-Nulth  Nuučaan̓uł  noo  Canada  2  1033  9825  NOO  -  -  -  kut om  en  no  -  Fri Jan 25 08:02:52 CST 2013  NUTKA, NUUCHAHNULTH  Wakashan, Southern.
noo-x-barkley  Nuu-chah-nulth (Barkley)  -  noo  Canada  0  0  0  NOO  -  -  -  kut noo-x-eha-nuc noo-x-nitinaht noo-x-she  en  no  -  -  NUTKA, NUUCHAHNULTH, NOOTKA  Wakashan, Southern.
noo-x-eha-nuc  Nuu-chah-nulth (Ehattesaht Nuchatlaht)  -  noo  Canada  0  0  0  NOO  -  -  -  kut noo-x-barkley noo-x-nitinaht noo-x-she  en  no  -  -  NUTKA, NUUCHAHNULTH  Wakashan, Southern.
noo-x-nitinaht  Nitinaht  Diidiitidq  noo  Canada  2  523  5203  NOO  -  -  -  noo-x-eha-nuc noo-x-barkley noo-x-she  en  no  -  Fri Jan 25 08:06:34 CST 2013  NUTKA, NUUCHAHNULTH  Wakashan, Southern.
noo-x-she  Nuu-chah-nulth (Tseshaht)  c̓išaaʔatḥ  noo  Canada  0  0  0  NOO  -  -  -  noo-x-barkley noo-x-eha-nuc noo-x-nitinaht  en  no  -  -  NUTKA, NUUCHAHNULTH  Wakashan, Southern.
nop  Numanggang  -  nop  Papua New Guinea  365  655911  4517970  NOP  -  -  -  dah  en  no  -  Fri Dec 28 21:44:22 CST 2012  MANGGANG, NUMANGANG, NUMANGAN, BOANA, KAI, NGAIN, SUGU  Trans-New Guinea, Main Section, Central and Western, Huon-Finisterre, Finisterre, Erap.
not  Nomatsiguenga  -  not  Peru  3  200638  1913821  NOT  -  -  not  cot cni  en  no  -  Thu Dec 27 20:34:48 CST 2012  NOMATSIGUENGA CAMPA, ATIRI  Arawakan, Maipuran, Southern Maipuran, Campa.
nou  Ewage-Notu  -  nou  Papua New Guinea  0  0  0  NOU  -  -  -  kpr mti rw drc ka-Latn ha kwn  en  no  -  -  NOTU, EWAGE  Trans-New Guinea, Main Section, Eastern, Binanderean, Binanderean Proper.
nov  Novial  Novial  nov  -  9  144750  901939  -  -  nov  -  ie lad ia fr ca ast es oc  en  no  -  Sat Jan 19 10:25:55 CST 2013  -  Artificial.
npi  Nepali  -  npi  Nepal  0  0  0  NEP  -  ne  -  mai hi mr bh hne mag new  en  no  Krishna Parajuli  -  NEPALESE, GORKHALI, GURKHALI, KHASKURA, PARBATIYA, EASTERN PAHARI  Indo-European, Indo-Iranian, Indo-Aryan, Northern zone, Eastern Pahari.
npl  Southeastern Puebla Nahuatl  -  npl  Mexico  1  274163  1450579  NHS  -  -  -  nhy nhm nsu nhn nhi  en  no  -  Wed Jan 9 12:17:13 CST 2013  SOUTHEASTERN PUEBLA NÁHUATL, TEHUACÁN NÁHUATL  Uto-Aztecan, Southern Uto-Aztecan, Aztecan, General Aztec, Aztec.
npy  Napu  -  npy  Indonesia (Sulawesi)  1  188002  1230023  NAP  -  -  -  aia gri stn  en  no  -  Wed Jan 9 13:21:35 CST 2013  PEKUREHUA  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Sulawesi, Central Sulawesi, West Central, Kaili-Pamona, Pamona.
nr  Ndebele  isiNdebele  nbl  South Africa  17  125457  1169653  NEL  nbl  -  nel  zu nd xh ss  en  yes  Dwayne Bailey, Friedel Wolff  Wed Sep 18 22:33:50 CDT 2013  NREBELE, NDZUNDZA, TRANSVAAL NDEBELE, SOUTHERN NDEBELE  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, S, Sotho-Tswana (S.30), Sotho, Northern.
nrn  Norn  Norn  nrn  United Kingdom  8  1022  6812  NON  -  -  -  en  en  no  -  Wed Oct 9 12:14:14 CDT 2013  -  Indo-European, Germanic, North, West Scandinavian.
nsk  Naskapi  -  nsk  Canada  10  6701  43313  NSK  -  -  -  cr oj-Cans iu den-Cans  en  no  -  Thu Dec 27 20:35:45 CST 2012  INNU AIMUUN  Algic, Algonquian, Central, Cree-Montagnais-Naskapi.
nsn  Nehan  -  nsn  Papua New Guinea  0  0  0  NSN  -  -  -  gfk agn lbb hla lcm jv nij ksd pam kqw su sxn mee  en  no  -  -  NISSAN, NIHAN  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, South New Ireland-Northwest Solomonic, Nehan-North Bougainville, Nehan.
nso  Northern Sotho  Sesotho sa Leboa  nso  South Africa  418  1581735  8732398  SRT  se  nso  srt  tn st  en  yes  Friedel Wolff, Dwayne Bailey  Wed Feb 6 17:46:21 CST 2013  PEDI, SEPEDI, TRANSVAAL SOTHO, SESOTHO SA LEBOA  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, S, Sotho-Tswana (S.30), Sotho, Northern.
nss  Nali  -  nss  Papua New Guinea  0  0  0  NSS  -  -  -  lid bjn slm id zsm nij su jv-x-bms  en  no  -  -  YIRU  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Admiralty Islands, Eastern, Manus, East.
nsu  Sierra Negra Nahuatl  -  nsu  Mexico  5  24243  165844  -  -  -  -  nhn nhy  en es  no  -  Thu Dec 27 20:36:25 CST 2012  Náhuatl de la Sierra Negra  Uto-Aztecan, Southern Uto-Aztecan, Aztecan, General Aztec, Aztec.
ntp  Northern Tepehuan  -  ntp  Mexico  2  248847  1993529  NTP  -  -  -  kac iba mek bmk mwc swp rom waj aia  en  no  -  Thu Dec 27 20:37:19 CST 2012  NORTHERN TEPEHUÁN  Uto-Aztecan, Southern Uto-Aztecan, Sonoran, Tepiman.
ntr  Delo  -  ntr  Ghana  1  271863  1289991  NTR  -  -  -  mzw ln xsm cme  en  no  -  Wed Jan 9 13:21:52 CST 2013  NTRUBO, NTRIBU, NTRIBOU  Niger-Congo, Atlantic-Congo, Volta-Congo, North, Gur, Central, Southern, Grusi, Eastern.
nus  Nuer  -  nus  Sudan  43  288451  1388484  NUS  -  -  nus*  tbz ada  en  no  -  Fri Sep 13 11:24:33 CDT 2013  NAATH, NAADH  Nilo-Saharan, Eastern Sudanic, Nilotic, Western, Dinka-Nuer, Nuer.
nuz  Tlamacazapa Nahuatl  -  nuz  Mexico  1  18649  140716  NUZ  -  -  -  ngu nhe nhw nch nhi ncj ncl azz nhm nhx  en  no  -  Wed Jan 9 19:59:44 CST 2013  -  Uto-Aztecan, Southern Uto-Aztecan, Aztecan, General Aztec, Aztec.
nv  Navajo  Diné bizaad  nav  USA  10  282180  2095565  NAV  nv  nv  nav  apw apa dtp min sek  en  no  Shawn Nez, Mark Williamson  Mon Dec 2 12:34:46 CST 2013  DINÉ, NAVAHO, DINE  Na-Dene, Nuclear Na-Dene, Athapaskan-Eyak, Athapaskan, Apachean, Navajo-Apache, Western Apache-Navajo.
nvm  Namiae  -  nvm  Papua New Guinea  0  0  0  -  -  -  -  bbb mcq kwf jbu meu agd ubr teo  en  no  -  -  Namiai  Trans-New Guinea, Southeast Papuan, Koiarian, Baraic.
nwi  Southwest Tanna  -  nwi  Vanuatu  4  44241  281264  NWI  -  -  -  bjv  en  no  -  Sat Jan 19 10:28:01 CST 2013  -  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, South Vanuatu, Tanna.
ny  Chichewa  Chicheŵa  nya  Malawi  259  1526588  11172860  NYJ  cn  ny  nyj  seh tum swk sn yao wmw dig sw kki  en  yes  Soyapi Mumba, Edmond Kachale  Fri Sep 13 16:40:12 CDT 2013  CHINYANJA, CHEWA, NYANJA  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, N, Nyanja (N.30).
ny-x-nya  Nyanja  Cinyanja  nya  Malawi  18  18398  132465  NYJ  cin  -  nya_chinyanja  ny seh tum swk toi dig swc bem wmw kki yao sw sn nba  en  no  Edmond Kachale  Mon Sep 16 20:27:54 CDT 2013  CHINYANJA, CHEWA  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, N, Nyanja (N.30).
nyd  Olunyole  -  nyd  Kenya  1  1247  10238  NYD  -  -  -  xog hay  en  no  -  Wed Jan 2 16:18:39 CST 2013  OLUNYORE, LUNYORE, NYOLE, NYOOLE, LUNYOLE, OLUNYOLE  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, J, Masaba-Luyia (J.30), Luyia.
nyf  Kigiryama  -  nyf  Kenya  5  205954  1371991  NYF  -  -  -  dug dig pkb wmw swh swc kki  en  no  -  Fri Jan 25 21:25:55 CST 2013  GIRIAMA, AGIRYAMA, KIGIRIAMA, NIKA, NYIKA, KINYIKA  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, E, Nyika (E.40), Mijikenda.
nyk  Nyaneka  Nyaneka  nyk  Angola  2  6495  51327  NYK  nk  -  -  umb kj ng xog zu hz lue  en  no  -  Fri Sep 13 15:31:40 CDT 2013  LUNYANEKA, NHANEKA, NHANECA  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, R, South Mbundu (R.10).
nym  Nyamwezi  -  nym  Tanzania  2  2494  15795  NYZ  -  -  nyz  kki suk swh lue loz bem  en  no  -  Fri Jan 25 16:16:17 CST 2013  KINYAMWEZI, KINYAMWESI, NYAMWESI, NAMWEZI  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, F, Sukuma-Nyamwezi (F.20).
nyn  Nyankore  Runyankore  nyn  Uganda  196  321756  2536079  NYN  rr  -  nyn1  ttj nyo lg rw rn xog  en  no  -  Tue Feb 5 22:24:06 CST 2013  NKOLE, NYANKOLE, RUNYANKOLE, ULUNYANKOLE, ULUNYANKORE, RUNYANKORE, RUNYANKORE-RUKIGA  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, J, Nyoro-Ganda (J.10).
nyo  Nyoro  -  nyo  Uganda  5  9798  80678  NYR  -  -  -  ttj nyn lg xog rw mho  en  no  -  Thu Jan 24 21:37:13 CST 2013  RUNYORO  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, J, Nyoro-Ganda (J.10).
nyy  Nyakyusa-Ngonde  -  nyy  Tanzania  3  144743  1102840  NYY  -  -  -  bem  en  no  -  Wed Jan 9 16:28:31 CST 2013  IKINYAKYUSA, MOMBE, NGONDE, IKINGONDE, KONDE, NKONDE, NYAKUSA, NYIKYUSA, SOCHILE, SOKILE, SOKILI, KUKWE, NYEKYOSA  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, M, Nyakyusa (M.30).
nzi  Nzema  Nzema  nzi  Ghana  136  241530  1367806  NZE  nz  -  nze  knk mnk emk  en  no  -  Tue Feb 5 08:12:18 CST 2013  NZIMA, APPOLO  Niger-Congo, Atlantic-Congo, Volta-Congo, Kwa, Nyo, Potou-Tano, Tano, Central, Bia, Southern.
nzm  Zeme Naga  -  nzm  India  1  1002  5495  NZM  -  -  -  pam jv tl lnu su kyk ban  en  no  -  Sun Mar 31 16:17:58 CDT 2013  KACHCHA, KACHA, KUTCHA, MEZAMA, SANGRIMA, SENGIMA, ARUNG, EMPUI, JEME, ZEMI  Sino-Tibetan, Tibeto-Burman, Kuki-Chin-Naga, Naga, Zeme.
obo  Obo Manobo  -  obo  Philippines  0  0  0  OBO  -  -  -  msm atd mbd ibl ami mog pag ja-Latn ifk crs tpz  en  no  -  -  OBO BAGOBO, BAGOBO, KIDAPAWAN MANOBO  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Southern Philippine, Manobo, Central, South, Obo.
oc  Occitan  Occitan  oci  France  2898  9900972  60207405  -  -  oc  -  es ca ast an mwl gl fr pt  en fr es  yes  Bruno Gallart, Maxime Caillon  Fri Sep 13 10:30:25 CDT 2013  LENGADOUCIAN, LANGUEDOC, LANGADOC, OCCITAN, OCCITANI  Indo-European, Italic, Romance, Italo-Western, Western, Gallo-Iberian, Ibero-Romance, Oc.
oge  Old Georgian  ენაჲ ქართული  oge  Georgia  9  2988  22687  -  -  -  -  en  en  no  -  Wed Oct 9 12:44:12 CDT 2013  -  South Caucasian, Georgian.
oge-x-khutsuri  Old Georgian (Khutsuri)  -  oge  Georgia  3  443  3687  -  -  -  -  ka  en  no  -  Wed Oct 9 14:22:55 CDT 2013  -  South Caucasian, Georgian.
ogo  Khana  Khana  ogo  Nigeria  2  49621  268586  OGO  og  -  -  mnk jbo bwu bas  en  no  -  Fri Jan 25 08:07:12 CST 2013  Kana, Ogoni  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Cross River, Delta Cross, Ogoni, East.
oj  Ojibwa  Anishinaabemowin  oji  Canada  177  166517  1467713  -  -  -  -  om crg gwi sbd  en  no  Chris Harvey, Anton Treuer  Fri Sep 13 10:28:28 CDT 2013  SAULTEAUX, PLAINS OJIBWAY, OJIBWAY, OJIBWE  Algic, Algonquian, Central, Ojibwa.
oj-Cans  Ojibwe (Syllabics)  -  oji  Canada  9  160043  924378  -  -  -  -  cr csw nsk crk ike iu  en  no  -  Mon Sep 16 18:34:13 CDT 2013  OJIBWAY  Algic, Algonquian, Central, Ojibwa.
ojb-Cans  Northwestern Ojibwa  -  ojb  Canada  1  1203  7599  OJB  -  -  ojb  cr csw nsk crk iu  en  no  -  Mon Dec 9 14:13:35 CST 2013  NORTHERN OJIBWA, OJIBWAY, OJIBWE  Algic, Algonquian, Central, Ojibwa.
oka  Okanagan  Nsilxcín  oka  Canada  3  484  4608  OKA  -  -  -  coo  en  no  -  Thu Jan 10 22:13:13 CST 2013  OKANAGAN-COLVILLE, OKANAGON, OKANOGAN  Salishan, Interior Salish, Southern.
okv  Orokaiva  -  okv  Papua New Guinea  0  0  0  ORK  -  -  -  kpr gri kzf meu khz fj mna  en  no  -  -  ORAKAIVA  Trans-New Guinea, Main Section, Eastern, Binanderean, Binanderean Proper.
old  Mochi  -  old  Tanzania  1  146873  966818  OLD  -  -  -  vun jmc swh pkb kki wmw ki swb  en  no  -  Wed Jan 9 16:05:33 CST 2013  MOSHI, KIMOSHI, MOSI  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, E, Chaga (E.30).
om  Oromo  Afaan Oromoo  orm  Ethiopia  2753  4403878  33022557  -  oa  om  gax  wal so dwr son gof lag xon maw vag aa  en  yes  Sisay Adugna, Aynieee Tesfaye, Belayneh Melka, Dawit Boka  Mon Jan 13 17:20:36 CST 2014  GALLA, OROMOO  Afro-Asiatic, Cushitic, East, Oromo.
oma  Omaha-Ponca  Umoⁿhoⁿ  oma  USA  1  22  125  OMA  -  -  -  udu osx  en  no  Vida Stabler  Mon Oct 1 13:31:11 CDT 2012  MAHAIRI, PONKA, UMANHAN, PPANKKA  Siouan, Siouan Proper, Central, Mississippi Valley, Dhegiha.
omq-x-amuzgo  Amuzgo  -  omq  Mexico  8  586937  3948261  -  -  -  -  ln gri fj nfr bgt ki xsm ktu pwg meu  en es  no  -  Wed Sep 25 10:16:24 CDT 2013  -  Oto-Manguean, Amuzgoan.
omq-x-chatino  Chatino  -  omq  Mexico  4  1069464  5413343  -  -  -  -  zpz omq-x-mixtec mio mjc zap zaq cbi  en es  no  -  Wed Sep 25 10:29:15 CDT 2013  -  Oto-Manguean, Zapotecan, Chatino.
omq-x-mazatec  Mazateco  -  omq  Mexico  196  1092360  7083632  -  -  -  -  war omq-x-mixtec pps bum  en es  no  -  Wed Sep 25 14:11:31 CDT 2013  -  Oto-Manguean, Popolocan, Mazatecan.
omq-x-mixtec  Mixtec languages  Tu'un Sávi  omq  Mexico  89  4658017  23617683  -  -  -  -  cya omq-x-chatino pps pls cta zai ctp ifu tpt ify  en es  no  Joaquin J. Martínez  Fri Oct 11 11:22:30 CDT 2013  -  Oto-Manguean, Mixtecan, Mixtec-Cuicatec, Mixtec.
omw  South Tairora  -  omw  Papua New Guinea  0  0  0  OMW  -  -  -  omw-x-aat omw-x-veq tbg not mcb tgp kwn ksd ndc jmc  en  no  -  -  -  Trans-New Guinea, Main Section, Central and Western, East New Guinea Highlands, Eastern, Tairora.
omw-x-aat  Aatasara  -  omw  Papua New Guinea  0  0  0  OMW  -  -  -  tbg not tgp mcb ndc kwn rug ksd  en  no  -  -  -  Trans-New Guinea, Main Section, Central and Western, East New Guinea Highlands, Eastern, Tairora.
omw-x-veq  Veqaura  -  omw  Papua New Guinea  0  0  0  OMW  -  -  -  omw-x-aat tbg not mcb kwn ndc tgp sn kpr mcq gvc ksd stn khz  en  no  -  -  -  Trans-New Guinea, Main Section, Central and Western, East New Guinea Highlands, Eastern, Tairora.
ong  Olo  -  ong  Papua New Guinea  0  0  0  ONG  -  -  -  fud sm ubu-x-nopenge jbo ubu imo ubu-x-kala rom  en  no  -  -  ORLEI  Torricelli, Wapei-Palei, Wapei.
ood  Tohono O’odham  -  ood  USA  6  629796  3060442  PAP  -  -  -  noa pes-Latn  en  no  Mark Williamson  Wed Sep 18 22:37:36 CDT 2013  PAPAGO-PIMA, O'ODHAM, O'OTHHAM, NEVOME, NEBOME, UPPER PIMAN  Uto-Aztecan, Southern Uto-Aztecan, Sonoran, Tepiman.
opm  Oksapmin  -  opm  Papua New Guinea  131  527198  3056812  OPM  -  -  -  kup gfk bjn nij bts id bku slm zsm jv-x-bms su tl  en  no  -  Mon Sep 23 10:41:58 CDT 2013  -  Trans-New Guinea, Oksapmin.
or  Oriya  ଓଡ଼ିଆ  ori  India  457  512807  3353450  ORY  oi*  or  ory*  -  en  yes  -  Tue Sep 10 11:33:56 CDT 2013  URIYA, UTKALI, ODRI, ODRUM, OLIYA, ORISSA, VADIYA, YUDHIA  Indo-European, Indo-Iranian, Indo-Aryan, Eastern zone, Oriya.
ore  Orejón  -  ore  Peru  2  1974  12294  ORE  -  -  -  an  en  no  -  Tue Jan 8 10:07:07 CST 2013  COTO, KOTO, PAYAGUA, MAI JA, OREGON, ORECHON, TUTAPI  Tucanoan, Western Tucanoan, Southern.
ory  Oriya  -  ory  India  1  270911  1771292  ORY  -  -  -  -  en  no  -  Thu Jan 24 15:16:26 CST 2013  URIYA, UTKALI, ODRI, ODRUM, OLIYA, ORISSA, VADIYA, YUDHIA  Indo-European, Indo-Iranian, Indo-Aryan, Eastern zone, Oriya.
os  Osetin  Иронау  oss  Georgia  194  512723  3716569  OSE  oss  os  ose  os-x-dig  en ru  no  -  Wed Feb 6 17:33:55 CST 2013  OSSETE  Indo-European, Indo-Iranian, Iranian, Eastern, Northeastern.
os-x-dig  Digor  -  oss  Georgia  1  2282  15132  OSE  dgr  -  -  os  en  no  -  Wed Jan 23 09:44:04 CST 2013  OSSETE  Indo-European, Indo-Iranian, Iranian, Eastern, Northeastern.
osx  Old Saxon  Sahsisk  osx  -  73  61982  339241  -  -  -  -  goh sco trf en wim frr-x-fer ifb  en  no  -  Wed Sep 18 22:38:24 CDT 2013  -  -
ote  Mezquital Otomi  Ñhähñu  ote  Mexico  8  307290  1509028  OTE  -  -  1111  otm otq  en es  no  -  Thu Sep 26 22:02:57 CDT 2013  HÑÃHÑU, OTOMÍ DEL VALLE DE MEZQUITAL  Oto-Manguean, Otopamean, Otomian, Otomi.
otm  Eastern Highland Otomi  -  otm  Mexico  2  370557  1784362  OTM  -  -  -  ote  en es  no  -  Thu Dec 27 20:40:33 CST 2012  EASTERN OTOMÍ, SIERRA OTOMÍ, YUHU, HUEHUETLA OTOMÍ, OTOMÍ DEL ORIENTE  Oto-Manguean, Otopamean, Otomian, Otomi.
otn  Tenango Otomi  -  otn  Mexico  2  408590  2043875  OTN  -  -  -  mks mxb mig cta mzi ots otm ote bzd trq cle cjp tcf otq miu  en  no  -  Thu Dec 27 20:43:09 CST 2012  -  Oto-Manguean, Otopamean, Otomian, Otomi.
oto  Otomian languages  Hñähñu  oto  Mexico  9  1586306  7895306  -  -  -  -  cta zai ch kng mzi  en es  no  -  Sat Sep 14 10:44:16 CDT 2013  -  Oto-Manguean, Otopamean, Otomian, Otomi.
oto-x-mazahua  Mazahuan languages  -  oto  Mexico  21  332893  1700844  -  mzh  -  -  otm  en es  no  -  Sat Sep 14 11:17:30 CDT 2013  -  Oto-Manguean, Otopamean, Otomian, Mazahua.
otq  Querétaro Otomi  -  otq  Mexico  2  30201  157270  OTQ  -  -  -  ote otm ha sat ots ka-Latn cuk luo kqc tr hui br-x-falhuneg  en  no  -  Fri Jan 11 20:16:21 CST 2013  HÑÃHÑO, QUERÉTARO OTOMÍ, WESTERN OTOMÍ, QUERÉTARO-MÉXICO OTOMÍ  Oto-Manguean, Otopamean, Otomian, Otomi.
ots  Estado de México Otomi  -  ots  Mexico  2  366504  1860075  OTS  -  -  -  otn ote zai otq otm bao tav cbr  en es  no  -  Thu Dec 27 20:45:08 CST 2012  HÑATHO, STATE OF MEXICO OTOMÍ  Oto-Manguean, Otopamean, Otomian, Otomi.
ozm  Koonzime  -  ozm  Cameroon  5  295116  1380329  NJE  -  -  -  nnw crn-x-presidio bss bas ee  en  no  -  Fri Jan 25 21:28:11 CST 2013  NZIME, DJIMU, ZIMU, KOOZIME, KOOZHIME, KOONCIMO, DZIMOU  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Northwest, A, Makaa-Njem (A.80).
pa  Panjabi  ਪੰਜਾਬੀ  pan  India  2549  6570568  37205213  PNJ  pj*  pa  pnj1  -  en  yes  -  Mon Feb 4 12:06:08 CST 2013  PUNJABI, GURMUKHI, GURUMUKHI  Indo-European, Indo-Iranian, Indo-Aryan, Central zone, Panjabi.
pab  Parecís  -  pab  Brazil  4  189034  1508104  PAB  -  -  -  ng  en  no  -  Wed Jan 9 20:03:08 CST 2013  PARESSÍ, PARESÍ, HALITI  Arawakan, Maipuran, Central Maipuran.
pad  Paumarí  Paumarí  pad  Brazil  3  392169  3107711  PAD  -  -  -  mcq gri fj kwj miq apu pwg  en  no  -  Thu Dec 27 20:53:05 CST 2012  PURUPURÚ  Arauan.
pag  Pangasinan  Pangasinan  pag  Philippines  553  1230874  7528615  PNG  pn  pag  -  itv bik ifk ifb bjn ibl sbl kne  en  no  -  Tue Feb 5 22:40:44 CST 2013  -  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Northern Philippine, Northern Luzon, South-Central Cordilleran, Southern Cordilleran, Pangasinic.
pah  Tenharim  -  pah  Brazil  1  294043  2007006  PAH  -  -  -  kgk gn  en  no  -  Wed Jan 9 19:51:56 CST 2013  TENHAREM, TENHARIN  Tupi, Tupi-Guarani, Kawahib (VI).
pam  Pampangan  Kapampangan  pam  Philippines  185  3518004  22251758  PMP  -  pam  pmp  tl jv agn jv-x-bms kyk msk jvn su  en tl  started  Jose Navarro, Edwin Camaya, Ernie Turla  Fri Sep 13 10:33:43 CDT 2013  PAMPANGO, PAMPANGUEÑO, KAPAMPANGAN  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Northern Philippine, Bashiic-Central Luzon-Northern Mindoro, Central Luzon, Pampangan.
pao  Northern Paiute  -  pao  USA  1  180872  1200751  PAO  -  -  -  son so  en  no  -  Wed Jan 9 20:10:33 CST 2013  PAVIOTSO  Uto-Aztecan, Northern Uto-Aztecan, Numic, Western.
pap  Papiamentu  Papiamentu  pap  Netherlands Antilles  4730  7512278  43152152  PAE  paa  pap  -  kea co scn it fur bpr srm bps rup srn  en es  no  Urso Wieske, Peter Damiana  Mon Sep 9 19:02:05 CDT 2013  PAPIAMENTO, PAPIAM, PAPIAMENTOE, PAPIAMEN, CURAÇOLEÑO, CURASSESE  Creole, Iberian based.
pap-CW  Papiamento (Curaçao)  -  pap  Netherlands Antilles  581  338692  2043407  PAE  pa  -  -  kea bpr it ifk  en  yes  -  Sat Jun 1 15:39:49 CDT 2013  PAPIAMENTO, PAPIAM, PAPIAMENTOE, PAPIAMEN, CURAÇOLEÑO, CURASSESE  Creole, Iberian based.
pau  Palauan  Tekoi er a Belau  pau  Palau  12  69254  350704  PLU  pu  -  plu  ar-Latn-x-chat dgi maf  en  no  -  Fri Sep 13 15:32:24 CDT 2013  BELAUAN, PALAU  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Palauan.
paw  Pawnee  Pawnee  paw  USA  2  950  9153  PAW  -  -  -  rai cpu cjo nyn kmo omw-x-aat  en  no  -  Wed Jan 23 10:40:13 CST 2013  -  Caddoan, Northern, Pawnee-Kitsai, Pawnee.
pbb  Páez  -  pbb  Colombia  3  175509  1334671  PBB  -  -  pbb  ln lag dug kde  en  no  -  Thu Jan 10 22:15:06 CST 2013  NASA YUWE  Paezan.
pbc  Patamona  -  pbc  Guyana  1  215849  1432534  PBC  -  -  -  ake kng  en  no  -  Wed Jan 9 20:11:17 CST 2013  INGARIKO, EREMAGOK, KAPON  Carib, Northern, East-West Guiana, Macushi-Kapon, Kapon.
pbi  Parkwa  -  pbi  Cameroon  1  272566  1384514  PBI  -  -  -  hig  en  no  -  Wed Jan 9 16:06:06 CST 2013  PODOKO, PADUKO, PODOKWO, PODOGO, PADOGO, PADOKWA, PAWDAWKWA, PAREKWA, GWADI PAREKWA, KUDALA  Afro-Asiatic, Chadic, Biu-Mandara, A, A.4, Mandara Proper, Podoko.
pbs  Central Pame  -  pbs  Mexico  2  32841  208964  PBS  -  -  -  rtm  en es  no  -  Sat May 4 10:38:44 CDT 2013  CENTRAL PAME, SANTA MARÍA ACAPULCO PAME, CHICHIMECA-PAME CENTRAL  Oto-Manguean, Otopamean, Pamean.
pcd  Picard  Picard  pcd  France  187  294353  1800959  PCD  -  pcd  frn2  fr fr-x-nor fr-x-jer fur lld wa ca  en  no  -  Sat Sep 7 04:28:28 CDT 2013  ROUCHI, CHTIMI  Indo-European, Italic, Romance, Italo-Western, Western, Gallo-Iberian, Gallo-Romance, Gallo-Rhaetian, Oïl, French.
pcm  Nigerian Pidgin  Naija  pcm  Nigeria  8  277148  1366448  PCM  -  -  pcm  trf gul en hwc sco  en  no  -  Wed Jan 23 10:43:54 CST 2013  NIGERIAN CREOLE ENGLISH, NIGERIAN PIDGIN ENGLISH  Creole, English based, Atlantic, Krio.
pdc  Pennsylvania German  Deitsch  pdc  USA  97  246364  1614843  PDC  -  pdc  -  pfl de vmf gsw lb ksh nds af li fy nl pdt zea  en de  no  -  Fri Sep 13 11:57:37 CDT 2013  PENNSYLVANISH, PENNSYLVANIA DUTCH  Indo-European, Germanic, West, High German, German, Middle German, West Middle German.
pdt  Plautdietsch  Plautdietsch  pdt  Canada  129  61592  388386  GRN  -  -  -  ksh vmf pdc nds pfl de  en de  no  -  Wed Sep 18 22:42:27 CDT 2013  LOW GERMAN, MENNONITE GERMAN, MENNONITEN PLATT  Indo-European, Germanic, West, Low Saxon-Low Franconian, Low Saxon.
pem  Phende  Kipende  pem  Dem. Rep. of Congo  1  8577  57636  PEM  kip  -  -  lua yaf  en  no  -  Thu Jan 24 21:41:06 CST 2013  KIPENDE, GIPHENDE, PENDE, GIPENDE, PINDI, PINJI  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, K, Holu (K.10).
pes  Iranian Persian  فارسی  pes  Iran  1183  3424151  19446301  PES  pr  -  prs  bal prs lki mzn glk  en  yes  -  Wed Jan 30 18:32:15 CST 2013  WESTERN FARSI, PARSI, FARSI  Indo-European, Indo-Iranian, Iranian, Western, Southwestern, Persian.
pes-Latn  Western Farsi (Latin)  -  pes  Iran  431  412897  2530673  PES  -  -  -  bvz uz-Latn hns ur-Latn bn-Latn  en  no  -  Wed Jan 23 10:53:48 CST 2013  PERSIAN, PARSI  Indo-European, Indo-Iranian, Iranian, Western, Southwestern, Persian.
pez  Eastern Penan  Ha' Penan  pez  Malaysia (Sarawak)  0  0  0  PEZ  -  -  -  cnh cfm jv-x-bms zsm id srb lus su bgr bjn vkt ctd  en  no  Rachael Petersen, Ian Mackenzie  -  'PUNAN'  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Borneo, Punan-Nibong.
pfl  Pfaelzisch  Pfälzisch  pfl  Germany  2  303260  2048104  PFL  -  pfl  -  pdc gsw  en de  no  -  Thu Jan 10 22:17:17 CST 2013  PFÄLZISCHE, PFÄLZISCH  Indo-European, Germanic, West, High German, German, Middle German, West Middle German, Rhenisch Fraconian.
phi-x-blaan  Blaan languages  -  phi  Philippines  2  417693  2062545  -  -  -  -  pov pap ifk mta bjn kne  en  no  -  Tue Oct 8 19:38:50 CDT 2013  -  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, South Mindanao, Bilic, Blaan.
pi  Pali  -  pli  India  2  10013089  86221299  PLL  -  pi  -  sa ne hi  en  no  Wie-Ming Ang  Tue Jan 29 18:08:18 CST 2013  -  Indo-European, Indo-Iranian, Indo-Aryan, Unclassified.
pi-Cyrl  Pali (Cyrillic)  -  pli  India  1  5587051  67276271  PLL  -  -  -  bxr ulc  en  no  -  Fri Jan 25 08:07:14 CST 2013  -  Indo-European, Indo-Iranian, Indo-Aryan, Unclassified.
pi-Gujr  Pali (Gujarati)  -  pli  India  1  10011981  85166502  PLL  -  -  -  gu  en  no  -  Fri Feb 15 22:43:19 CST 2013  -  Indo-European, Indo-Iranian, Indo-Aryan, Unclassified.
pi-Knda  Pali (Kannada)  -  pli  India  1  5587209  48315564  PLL  -  -  -  kn  en  no  -  Sat Feb 16 07:15:53 CST 2013  -  Indo-European, Indo-Iranian, Indo-Aryan, Unclassified.
pi-Latn  Pali (Latin)  Farsi  pli  India  246  6016462  59098006  PLL  -  pi  -  sg ilo gri tzu cax  en  no  Wie-Ming Ang  Wed Jan 23 08:36:26 CST 2013  -  Indo-European, Indo-Iranian, Indo-Aryan, Unclassified.
pi-Mlym  Pali (Malayalam)  -  pli  India  1  5587051  48338307  PLL  -  -  -  ml  en  no  -  Sat Feb 16 12:10:27 CST 2013  -  Indo-European, Indo-Iranian, Indo-Aryan, Unclassified.
pi-Mymr  Pali (Myanmar)  -  pli  India  1  5589770  49395288  PLL  -  -  -  my  en  no  -  Sat Feb 16 13:58:04 CST 2013  -  Indo-European, Indo-Iranian, Indo-Aryan, Unclassified.
pi-Sinh  Pali (Sinhala)  -  pli  India  1  1297838  12362308  PLL  -  -  -  si  en  no  -  Sat Feb 16 18:10:39 CST 2013  -  Indo-European, Indo-Iranian, Indo-Aryan, Unclassified.
pi-Taml  Pali (Tamil)  -  pli  India  1  10011981  94307915  PLL  -  -  -  ta  en  no  -  Sat Feb 16 19:52:00 CST 2013  -  Indo-European, Indo-Iranian, Indo-Aryan, Unclassified.
pi-Telu  Pali (Telugu)  -  pli  India  1  10011981  85166502  PLL  -  -  -  te  en  no  -  Sun Feb 17 09:00:10 CST 2013  -  Indo-European, Indo-Iranian, Indo-Aryan, Unclassified.
pi-Thai  Pali (Thai)  -  pli  India  1  10012255  86257221  PLL  -  -  -  th  en  no  -  Sun Feb 17 12:02:22 CST 2013  -  Indo-European, Indo-Iranian, Indo-Aryan, Unclassified.
pib  Yine  -  pib  Peru  3  293517  2472738  PIB  -  -  -  swh wmw dgz kki soq kde swc swb tum mti pkb dig  en es  no  -  Thu Dec 27 20:55:56 CST 2012  PIRO, PIRRO, PIRA, SIMIRINCHE, SIMIRANCH, CONTAQUIRO, YINE  Arawakan, Maipuran, Southern Maipuran, Purus.
pih  Pitcairn-Norfolk  Norfuk  pih  Norfolk Island  2  10169  63510  PIH  -  pih  -  lad ca ext djk es  en  no  -  Thu Jan 10 22:19:38 CST 2013  PITCAIRN ENGLISH  Cant, English-Tahitian.
pim  Powhatan  PoHaTan  pim  USA  2  93  761  PIM  -  -  -  de fy prg  en  no  Ian Custalow  Mon Oct 1 22:26:19 CDT 2012  VIRGINIA ALGONKIAN  Algic, Algonquian, Eastern.
pio  Piapoco  -  pio  Colombia  2  320004  2633938  PIO  -  -  -  ycn cof zai cta zat mbp qvo qxr cni  en es  no  -  Thu Dec 27 20:59:15 CST 2012  -  Arawakan, Maipuran, Northern Maipuran, Inland.
pir  Piratapuyo  -  pir  Brazil  2  261544  1780431  PIR  -  -  -  gvc tav bao  en  no  -  Wed Jan 9 20:26:09 CST 2013  WAIKINO, PIRA-TAPUYA, UAIKENA, UAICANA, WAIKHARA, WAINA, UAIANA, UAINANA  Tucanoan, Eastern Tucanoan, Northern.
pis  Pijin  Pijin  pis  Solomon Islands  51  1159742  6552149  PIS  sp  -  pis  bi tpi  en  no  -  Wed Sep 18 22:43:08 CDT 2013  SOLOMONS PIDGIN, NEO-SOLOMONIC  Creole, English based, Pacific.
piu  Pintupi-Luritja  -  piu  Australia  4  33102  333567  PIU  -  -  -  pjt wbp wmt mpj  en  no  -  Fri Jan 25 08:10:25 CST 2013  PINTUBI, BINDDIBU, LORIDJA  Australian, Pama-Nyungan, South-West, Wati.
pjt  Pitjantjatjara  Pitjantjatjara  pjt  Australia  9  16959  129377  PJT  -  -  -  piu wbp wmt mpj  en  no  Peter Ruwoldt  Fri Jan 25 08:13:31 CST 2013  PITJANTJARA  Australian, Pama-Nyungan, South-West, Wati.
pkb  Kipfokomo  -  pkb  Kenya  1  165959  1147915  PKB  -  -  -  sw wmw dig kki nyf  en  no  -  Wed Jan 9 16:37:40 CST 2013  -  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, E, Nyika (E.40), Pokomo.
pko  Pökoot  Pökoot  pko  Kenya  11  1342  8572  PKO  -  -  -  enb spy adh tum cjk old lcm lue swc kwn  en  no  -  Wed Oct 9 15:01:32 CDT 2013  PöKOT, SUK, PAKOT  Nilo-Saharan, Eastern Sudanic, Nilotic, Southern, Kalenjin, Pokot.
pl  Polish  Polski  pol  Poland  6985  8374229  60346253  PQL  p  pl  pql  sk hsb csb szl mk-Latn sl bs  en  yes  -  Mon Jul 15 16:54:57 CDT 2013  POLSKI, POLNISCH  Indo-European, Slavic, West, Lechitic.
pls  San Marcos Tlalcoyalco Popoloca  -  pls  Mexico  2  351687  2061016  PLS  -  -  -  ura mio pps mxt cya azg amu mza  en  no  -  Thu Dec 27 20:59:08 CST 2012  NORTHERN POPOLOCA, TLALCOYALCO POPOLOCA  Oto-Manguean, Popolocan, Chocho-Popolocan, Popolocan.
plt  Plateau Malagasy  Malagasy  plt  Madagascar  6716  12980484  90686306  MEX  mg  mg  mex  buc xmv skg  en fr  yes  Rado Ramarotafika  Tue Sep 10 20:40:30 CDT 2013  MALGACHE, STANDARD MALAGASY, MALAGASY, OFFICIAL MALAGASY  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Borneo, Barito, East, Malagasy.
pmf  Pamona  -  pmf  Indonesia (Sulawesi)  3  311065  1838147  BCX  -  -  -  kzf mvp sml nij npy  en  no  -  Wed Jan 9 17:07:23 CST 2013  BARE'E, BAREE, POSO, TAA, WANA  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Sulawesi, Central Sulawesi, West Central, Kaili-Pamona, Pamona.
pms  Piemontese  Piemontèis  pms  Italy  3  1657000  9619622  PMS  -  pms  -  lij kno lld eml dgi fur maf oc it  en  no  -  Tue Sep 10 11:55:14 CDT 2013  PIEMONTÈIS, PIEDMONTESE  Indo-European, Italic, Romance, Italo-Western, Western, Gallo-Iberian, Gallo-Romance, Gallo-Italian.
pnb  Western Panjabi  شاہ مکھی پنجابی  pnb  Pakistan  949  1547715  8186365  PNB  pjn*  pnb  pnb  skr ur lki azb-Arab pes  en  no  -  Wed Jan 30 20:44:41 CST 2013  WESTERN PUNJABI, LAHNDA, LAHANDA, LAHNDI  Indo-European, Indo-Iranian, Indo-Aryan, Northwestern zone, Lahnda.
pne  Western Penan  -  pne  Malaysia (Sarawak)  0  0  0  PNE  -  -  -  pez ms zsm id jv-x-bms bjn su vkt iba nij jv mad war cnh btx  en  no  -  -  NIBONG, NIBON, 'PUNAN'  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Borneo, Punan-Nibong.
pnt  Pontic  Ποντιακά  pnt  Greece  16  53363  345021  PNT  -  pnt  -  el grc  en  no  -  Wed Jan 23 10:47:30 CST 2013  PONTIC GREEK  Indo-European, Greek, Attic.
pob  Western Poqomchi’  -  pob  Guatemala  1  502342  2792813  POB  -  -  -  acc cbm poh usp qut  en  no  -  Wed Jan 9 20:36:47 CST 2013  WESTERN POCOMCHÍ, POCOMCHÍ  Mayan, Quichean-Mamean, Greater Quichean, Pocom.
poe  San Juan Atzingo Popoloca  -  poe  Mexico  1  258636  1589708  POE  -  -  -  pls  en  no  -  Wed Jan 9 20:36:59 CST 2013  ATZINGO POPOLOCA, EASTERN POPOLOCA, SOUTHERN POPOLOCA  Oto-Manguean, Popolocan, Chocho-Popolocan, Popolocan.
poh  Poqomchi’  -  poh  Guatemala  2  1533696  8500815  POH  -  -  -  acc ckk quc cbm acr  en  no  -  Wed Dec 11 10:50:04 CST 2013  TACTIC POKOMCHÍ, POCOMCHÍ, POCONCHÍ, POKONCHÍ  Mayan, Quichean-Mamean, Greater Quichean, Pocom.
poh-x-eastern  Eastern Poqomchi’  -  poh  Guatemala  0  0  0  POH  -  -  -  acc ckk quc cbm acr  en  no  -  -  TACTIC POKOMCHÍ, POCOMCHÍ, POCONCHÍ, POKONCHÍ  Mayan, Quichean-Mamean, Greater Quichean, Pocom.
poi  Highland Popoluca  -  poi  Mexico  28  243610  1462775  POI  -  -  -  cso nhx  en  no  -  Mon Oct 1 13:51:12 CDT 2012  HIGHLAND POPOLUCA  Mixe-Zoque, Zoque, Veracruz Zoque.
pon  Pohnpeian  Mahsen en Pohnpei  pon  Micronesia  47  95648  575763  PNF  pp  -  pnf  jv-x-bms  en  no  -  Fri Sep 13 15:34:41 CDT 2013  PONAPEAN  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Micronesian, Micronesian Proper, Ponapeic-Trukic, Ponapeic.
pot  Potawatomi  Bodéwadminwen  pot  USA  217  289062  2201448  POT  -  -  -  lkt cr-Latn ppl csw-Latn dak nhy  en  no  -  Tue Oct 1 20:19:02 CDT 2013  POTTAWOTOMI  Algic, Algonquian, Central.
pov  Upper Guinea Crioulo  -  pov  Guinea-Bissau  1  2033  11436  POV  -  -  gbc  kea pap pap-CW co scn cri bpr bps fur rup srm  en  no  -  Mon Dec 9 14:13:31 CST 2013  PORTUGUESE CREOLE, KRIULO  Creole, Portuguese based.
ppl  Pipil  Nawat  ppl  El Salvador  247  199511  1369530  PPL  -  -  ppl  ain mbt mbi nhy  en es  no  Alan R. King  Wed Sep 18 22:44:47 CDT 2013  NAHUAT, NAWAT  Uto-Aztecan, Southern Uto-Aztecan, Aztecan, General Aztec, Pipil.
ppo  Folopa  -  ppo  Papua New Guinea  285  304106  1874950  PPO  -  -  -  xla bwu yss-x-yawu twu gvf tgp kpx st kjs  en  no  -  Fri Dec 28 21:49:57 CST 2012  PODOPA, POLOPA, PODOBA, FORABA  Trans-New Guinea, Teberan-Pawaian, Teberan.
pps  San Luís Temalacayuca Popoloca  -  pps  Mexico  11  121649  747142  PPS  -  -  -  mza zpt azg pls mpm mxv bfa sg mim vmy xtn mxb  en es  no  -  Thu Dec 27 21:08:52 CST 2012  TEMALACAYUCA POPOLOCA  Oto-Manguean, Popolocan, Chocho-Popolocan, Popolocan.
pqw-x-penan  Penan languages  -  pqw  Malaysia (Sarawak)  3  271344  1485860  -  -  -  -  cnh cfm jv-x-bms zsm id srb lus su bgr bjn vkt ctd  en  no  Rachael Petersen, Ian Mackenzie  Sun Nov 17 13:03:14 CST 2013  'PUNAN'  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Borneo, Punan-Nibong.
prf  Paranan  -  prf  Philippines  0  0  0  AGP  -  -  -  kne mqb pag srn dgc djk due ivv ifk  en  no  -  -  PALANENYO, PLANAN  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Northern Philippine, Northern Luzon, Northern Cordilleran, Dumagat, Northern.
prg  Prussian  Prūsiskan  prg  Poland  649  180019  1331537  PRG  -  -  -  ify ms  en pl lv  yes  -  Wed Sep 18 22:46:28 CDT 2013  OLD PRUSSIAN  Indo-European, Baltic, Western.
pri  Paicî  -  pri  New Caledonia  0  0  0  PRI  -  -  -  omq-x-amuzgo amu gri ln fj xsm nfr ki pwg  en  no  -  -  PATI, PAACI, CI, PONERIHOUEN  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, New Caledonian, Northern, Central.
prq  Ashéninca Perené  -  prq  Peru  2  1326  10249  CPP  -  -  cpp  cbs  en  no  -  Wed Sep 11 14:23:56 CDT 2013  PERENÉ, CAMPA  Arawakan, Maipuran, Southern Maipuran, Campa.
prs  Dari  دری  prs  Afghanistan  17  100870  552387  PRS  -  -  -  pes bal glk lki mzn  en  no  -  Wed Sep 18 23:02:06 CDT 2013  PERSIAN, EASTERN FARSI, PARSI  Indo-European, Indo-Iranian, Iranian, Western, Southwestern, Persian.
prv  Provençal  -  prv  France  2  42880  249224  PRV  -  -  pro  lms lnc gsc ca es mwl gl ast cbk fr  en fr  no  Bruno Gallart  Wed Jan 30 20:46:00 CST 2013  PROUVENÇAU, MISTRALIEN  Indo-European, Italic, Romance, Italo-Western, Western, Gallo-Iberian, Ibero-Romance, Oc.
ps  Pushto  پښﺕﻭ  pus  Pakistan  2833  7006242  36702436  -  -  ps  -  glk lki pes prs  en ur  no  -  Mon Jan 21 20:45:14 CST 2013  PAKHTO, PASHTO  Indo-European, Indo-Iranian, Iranian, Eastern, Southeastern, Pashto.
pst-Latn  Central Pashto  Pax̌to  pst  Pakistan  6  2029  11971  PST  -  -  -  ha wbl-Latn pbi az bgt pwg hif  en  no  -  Wed Oct 9 15:44:48 CDT 2013  MAHSUDI  Indo-European, Indo-Iranian, Iranian, Eastern, Southeastern, Pashto.
pt  Portuguese  Português  por  Portugal  3444  5682669  35842657  POR  t  pt  -  gl es ast cbk oc mwl  en  yes  -  Tue Feb 5 09:12:03 CST 2013  PORTUGUÊS  Indo-European, Italic, Romance, Italo-Western, Western, Gallo-Iberian, Ibero-Romance, West Iberian, Portuguese-Galician.
pt-AO  Portuguese (Angola)  Português (Angola)  por  Angola  286  407532  2581628  POR  t  -  -  gl es ast mwl cbk oc  en  no  -  Thu Jan 24 22:12:24 CST 2013  PORTUGUÊS  Indo-European, Italic, Romance, Italo-Western, Western, Gallo-Iberian, Ibero-Romance, West Iberian, Portuguese-Galician.
pt-BR  Brazilian Portuguese  Português do Brasil  por  Brazil  100  407240  2738722  POR  t  -  por_BR  gl es an oc mwl  en  yes  -  Thu Jan 31 06:57:56 CST 2013  PORTUGUÊS  Indo-European, Italic, Romance, Italo-Western, Western, Gallo-Iberian, Ibero-Romance, West Iberian, Portuguese-Galician.
pt-CV  Portuguese (Cape Verde)  Português (Cabo Verde)  por  Cape Verde Islands  206  662101  4280856  POR  t  -  -  gl es ast cbk mwl oc  en  no  -  Thu Jan 24 22:12:38 CST 2013  PORTUGUÊS  Indo-European, Italic, Romance, Italo-Western, Western, Gallo-Iberian, Ibero-Romance, West Iberian, Portuguese-Galician.
pt-GW  Portuguese (Guinea Bissau)  Português (Guiné-Bissau)  por  Guinea-Bissau  1  8581  54356  POR  t  -  -  gl es  en  no  -  Wed Sep 11 14:15:25 CDT 2013  PORTUGUÊS  Indo-European, Italic, Romance, Italo-Western, Western, Gallo-Iberian, Ibero-Romance, West Iberian, Portuguese-Galician.
pt-MZ  Portuguese (Mozambique)  Português (Moçambique)  por  Mozambique  87  423294  2741934  POR  t  -  -  gl es cbk ast mwl oc  en  no  -  Thu Jan 24 22:12:34 CST 2013  PORTUGUÊS  Indo-European, Italic, Romance, Italo-Western, Western, Gallo-Iberian, Ibero-Romance, West Iberian, Portuguese-Galician.
pt-PT  Portuguese (Portugal)  Português (Portugal)  por  Portugal  154  398455  2494562  POR  t  -  por  gl es ast cbk mwl oc  en  yes  -  Thu Jan 31 06:55:15 CST 2013  PORTUGUÊS  Indo-European, Italic, Romance, Italo-Western, Western, Gallo-Iberian, Ibero-Romance, West Iberian, Portuguese-Galician.
pt-ST  Portuguese (São Tomé and Príncipe)  Português (São Tomé and Príncipe)  por  São Tomé e Príncipe  1097  1873722  11950734  POR  t  -  -  gl es cbk mwl ast oc  en  no  -  Fri Jan 25 09:11:29 CST 2013  PORTUGUÊS  Indo-European, Italic, Romance, Italo-Western, Western, Gallo-Iberian, Ibero-Romance, West Iberian, Portuguese-Galician.
pt-TL  Portuguese (Timor-Leste)  Português (Timor-Leste)  por  East Timor  662  1301216  8349135  POR  t  -  -  gl es cbk ast mwl oc  en  no  -  Fri Jan 25 09:11:20 CST 2013  PORTUGUÊS  Indo-European, Italic, Romance, Italo-Western, Western, Gallo-Iberian, Ibero-Romance, West Iberian, Portuguese-Galician.
ptp  Patep  -  ptp  Papua New Guinea  0  0  0  PTP  -  -  -  pam tl vi lnu agn mbh lbb  en  no  -  -  PTEP  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Huon Gulf, South, Hote-Buang, Buang, Mumeng.
ptu  Bambam  -  ptu  Indonesia (Sulawesi)  1  190360  1329081  PTU  -  -  -  mvp fj  en  no  -  Wed Jan 9 19:23:40 CST 2013  PITU-ULUNNA-SALU  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Sulawesi, South Sulawesi, Northern, Pitu Ulunna Salu.
pua  Western Highland Purepecha  P'urhépecha  pua  Mexico  9  1063  8133  PUA  -  -  -  en es  en es  no  -  Mon Dec 2 08:43:24 CST 2013  WESTERN HIGHLAND PURÉPECHA, TARASCO, TARASCAN  Language Isolate.
puu  Punu  -  puu  Gabon  1  1374  9216  PUU  -  -  -  dig pem kcc kqn kki  en  no  -  Mon Apr 29 20:56:42 CDT 2013  IPUNU, YIPUNU, POUNO, PUNO, YIPOUNOU  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Northwest, B, Sira (B.40).
pwg  Gapapaiwa  -  pwg  Papua New Guinea  269  309443  2092061  PWG  -  -  -  bmk aui gri meu fj bdd mox bgt alu stn  en  no  -  Fri Dec 28 21:56:14 CST 2012  MANAPE, GAPA, PAIWA  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Nuclear, North Papuan Mainland-D'Entrecasteaux, Are-Taupota, Are.
pwn  Paiwan  -  pwn  Taiwan  2  2441  14632  PWN  -  -  -  ivv lus due hnn kno maf  en  no  -  Tue Jul 23 17:38:18 CDT 2013  PAIUAN, PAYOWAN, LI-LI-SHA, SAMOBI, SAMOHAI, SAPREK, TAMARI, KADAS, KALE-WHAN, KAPIANGAN, KATAUSAN, BUTANGLU, STIMUL  Austronesian, Formosan, Paiwanic.
pww  Pwo Northern Karen  -  pww  Thailand  1  310680  1333937  PWW  -  -  -  th kxm  en  no  -  Wed Jan 9 19:23:59 CST 2013  PHLONG  Sino-Tibetan, Tibeto-Burman, Karen, Pwo.
qu  Quechua  Runa Simi  que  Bolivia  303  4297261  35758523  -  qub  qu  qec1  inb hnn mqb ivv ifu sml sbl ay  en es  yes  Amos Batto, Chris Loza, Michael Mohler  Wed Sep 11 14:18:28 CDT 2013  CENTRAL BOLIVIAN QUECHUA, QUECHUA BOLIVIANO  Quechuan, Quechua II, C.
qu-x-ancash  Ancash Quechua  -  que  Peru  7  488155  4376848  -  -  -  -  qvm qub qvn qxh qul qvo quh qxr  en es  no  -  Sun Sep 15 21:39:53 CDT 2013  -  Quechuan.
qub  Huallaga Huánuco Quechua  -  qub  Peru  2  126182  1204644  QUB  -  -  -  qvn qvh qvm qxo qxn  en es  no  -  Fri Jan 25 21:59:03 CST 2013  -  Quechuan, Quechua I.
quc  K’iche’  Qatzijob'al  quc  Guatemala  77  574325  3268894  QUC  qc  -  1117  cak acr qut cki ckw cke  en es  no  Peter Rohloff, Diego Alburez  Wed Dec 11 10:25:49 CST 2013  Cachabel, Central Quiché, Chiquel, Quiché  Mayan, Quichean-Mamean, Greater Quichean, Quichean, Quiche-Achi.
qud  Calderón Highland Quichua  -  qud  Ecuador  1  1035  8866  QUD  -  -  qud1  qxr qvo qu-x-ancash qvn qub qxn qul qxo qxh qvh qvm  en es  no  -  Mon Dec 9 14:13:25 CST 2013  CALDERÓN QUICHUA, PICHINCHA QUICHUA, CAYAMBE QUICHUA  Quechuan, Quechua II, B.
quf  Lambayeque Quechua  -  quf  Peru  0  0  0  QUF  -  -  -  qvc qvs  en es  no  -  -  FERREÑAFE  Quechuan, Quechua II, A.
qug  Chimborazo Highland Quichua  Kichwa  qug  Ecuador  9  75932  689462  QUG  qi  -  qug  qvz qup qvs qve  en es  no  -  Wed Sep 18 23:04:38 CDT 2013  -  Quechuan, Quechua II, B.
quh  South Bolivian Quechua  -  quh  Bolivia  2  159365  1438858  QUH  -  -  -  qxa quz quy  en es  yes  Amos Batto  Thu Dec 27 21:08:57 CST 2012  CENTRAL BOLIVIAN QUECHUA, QUECHUA BOLIVIANO  Quechuan, Quechua II, C.
quj  Joyabaj K’iche’  -  quj  Guatemala  1  269504  1491011  QUJ  -  -  -  acc ckk tzj-x-eastern cbm pob usp  en es  no  -  Fri Jan 11 08:50:49 CST 2013  -  Mayan, Quichean-Mamean, Greater Quichean, Quichean, Quiche-Achi.
qul  North Bolivian Quechua  -  qul  Bolivia  1  126615  1174183  QUL  -  -  -  quh qub qxh qvs qvn qxa quz qup qvz qvh qxo qvw  en es  no  -  Wed Jan 9 20:42:56 CST 2013  NORTH LA PAZ QUECHUA  Quechuan, Quechua II, C.
qup  Southern Pastaza Quechua  -  qup  Peru  2  219105  1902637  QUP  -  -  -  qvz qvs qug quz quy  en es  no  -  Thu Jan 10 22:22:37 CST 2013  INGA  Quechuan, Quechua II, B.
qut  West Central K’iche’  -  qut  Guatemala  3  315103  1672110  QUT  -  -  -  cak ckw cki cke acr usp quc  en es  no  -  Thu Dec 27 21:10:51 CST 2012  SOUTHWESTERN QUICHÉ, CANTEL QUICHÉ  Mayan, Quichean-Mamean, Greater Quichean, Quichean, Quiche-Achi.
quw  Tena Lowland Quichua  -  quw  Ecuador  0  0  0  QUW  -  -  -  qvo qxr qud qxh qvn qul qub qvz  en es  no  -  -  YUMBO  Quechuan, Quechua II, B.
quy  Ayacucho Quechua  -  quy  Peru  6  115648  1168115  QUY  qua  -  quy  qvs qup quz qva qxa qxu  en es  no  -  Fri Sep 13 12:22:52 CDT 2013  CHANKA  Quechuan, Quechua II, C.
quz  Cusco Quechua  -  quz  Peru  70  531418  5114149  QUZ  qu  -  quz  qve quy qva qxu qvs qvz qxa  en es  no  -  Wed Feb 6 16:34:10 CST 2013  CUSCO QUECHUA  Quechuan, Quechua II, C.
qva  Ambo-Pasco Quechua  -  qva  Peru  4  7412  61541  QEG  -  -  qeg  quy quz  en es  no  -  Tue Sep 10 14:56:39 CDT 2013  AMBO-PASCO QUECHUA  Quechuan, Quechua I.
qvc  Cajamarca Quechua  -  qvc  Peru  4  431523  3723493  QNT  -  -  qnt  quf  en es  no  -  Thu Jan 31 10:17:03 CST 2013  -  Quechuan, Quechua II, A.
qve  Eastern Apurímac Quechua  -  qve  Peru  1  224215  2022551  QEA  -  -  -  quz quy quf qvs qvz qxa qva qup qug qxu quh qvc qul qub  en es  no  -  Thu Jan 10 08:02:41 CST 2013  -  Quechuan, Quechua II, C.
qvh  Huamalíes-Dos de Mayo Huánuco Quechua  -  qvh  Peru  3  202718  1850069  QEJ  -  -  qej  qvm qxo qub qxn qvn qxh qul qvo quh  en es  no  -  Thu Dec 27 21:29:14 CST 2012  -  Quechuan, Quechua I.
qvm  Margos-Yarowilca-Lauricocha Quechua  Runa Shimi  qvm  Peru  5  355841  3215250  QEI  -  -  qei  qvh qxo qxn qvn  en es  no  -  Wed Sep 18 22:48:13 CDT 2013  -  Quechuan, Quechua I.
qvn  North Junín Quechua  -  qvn  Peru  4  359290  3231429  QJU  -  -  qju  qxo qxn qvm qvh  en es  no  -  Thu Jan 10 22:29:11 CST 2013  TARMA-JUNÍN QUECHUA, JUNÍN QUECHUA  Quechuan, Quechua I.
qvo  Napo Lowland Quechua  -  qvo  Ecuador  1  115908  1040096  QLN  -  -  -  qul qxh qub qvz qvs qvn  en es  no  -  Fri Jan 11 09:12:41 CST 2013  INGANO, LOWLAND NAPO QUICHUA, NAPO QUICHUA  Quechuan, Quechua II, B.
qvs  San Martín Quechua  Qiv'vorin  qvs  Peru  3  362703  3225785  QSA  -  -  -  qvz qup qug quz quy quf qva  en es  no  -  Thu Dec 27 21:38:38 CST 2012  UCAYALI, LAMISTA, LAMISTO, LAMA, LAMANO, MOTILÓN  Quechuan, Quechua II, B.
qvw  Huaylla Wanca Quechua  -  qvw  Peru  2  344734  1632996  QHU  -  -  -  qxw toc inb  en es  no  -  Thu Jan 10 22:31:36 CST 2013  SOUTHERN HUANCAYO QUECHUA, HUANCA HUAYLLA QUECHUA  Quechuan, Quechua I.
qvz  Northern Pastaza Quichua  -  qvz  Ecuador  3  408137  3620828  QLB  -  -  -  qup qvs qug  en es  no  -  Thu Dec 27 21:39:02 CST 2012  BOBONAZA QUICHUA, NORTHERN PASTAZA QUICHUA, PASTAZA QUICHUA, ALAMA, CANELOS QUICHUA, SARAYACU QUICHUA  Quechuan, Quechua II, B.
qwh  Huaylas Ancash Quechua  -  qwh  Peru  4  339594  2922867  QAN  -  -  qan  qxo qxn qvm qvh qxh qvn  en es  no  -  Fri Jan 25 09:04:42 CST 2013  -  Quechuan, Quechua I.
qxa  Chiquián Ancash Quechua  -  qxa  Peru  4  6654  59663  QEC  -  -  qec1  quy quz  en es  no  -  Fri Sep 13 11:33:27 CDT 2013  -  Quechuan, Quechua I.
qxh  Panao Huánuco Quechua  -  qxh  Peru  2  163621  1472183  QEM  -  -  -  qub qvw qvn  en es  no  -  Thu Dec 27 21:48:05 CST 2012  PACHITEA QUECHUA  Quechuan, Quechua I.
qxn  Northern Conchucos Ancash Quechua  -  qxn  Peru  5  406637  3686248  QED  -  -  qed  qxo qvm qvh qvn  en es  no  -  Wed Sep 18 23:07:22 CDT 2013  CONCHUCOS QUECHUA, NORTHERN CONCHUCOS QUECHUA  Quechuan, Quechua I.
qxo  Southern Conchucos Ancash Quechua  -  qxo  Peru  3  371078  3408387  QEH  -  -  -  qxn qvm qvh qvn  en es  no  -  Thu Dec 27 21:52:46 CST 2012  CONCHUCOS QUECHUA, SOUTHERN CONCHUCOS QUECHUA  Quechuan, Quechua I.
qxr  Cañar Highland Quichua  -  qxr  Ecuador  1  594  5626  QQC  -  -  -  qvo qvn qub qul qvz  en es  no  -  Sat May 4 11:05:41 CDT 2013  -  Quechuan, Quechua II, B.
qxu  Arequipa-La Unión Quechua  -  qxu  Peru  4  5044  47467  QAR  -  -  qar  quy quz  en es  no  -  Tue Sep 10 14:47:26 CDT 2013  AREQUIPA QUECHUA, COTAHUASI QUECHUA  Quechuan, Quechua II, C.
qxw  Jauja Wanca Quechua  -  qxw  Peru  2  349486  1668204  QHJ  -  -  -  qvw inb qub qvn qxh quh qu-x-ancash qvh qul qxn ifu toc qxo qvm quz qvc  en es  no  -  Fri Sep 13 11:50:38 CDT 2013  SHAUSHA WANKA QUECHUA, HUANCA JAUJA QUECHUA  Quechuan, Quechua I.
rai  Ramoaaina  -  rai  Papua New Guinea  0  0  0  RAI  -  -  -  ksd kqw gfk leu lbb cme bnp srr lag stn vag om  en  no  -  -  DUKE OF YORK, MALU, RAMUAINA  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, South New Ireland-Northwest Solomonic, Patpatar-Tolai.
raj  Rajasthani  राजस्थानी  raj  India  19  2848  17108  -  -  -  -  en  en  no  -  Sat Nov 16 18:07:15 CST 2013  -  -
ram  Canela  -  ram  Brazil  2  416511  2037151  RAM  -  -  -  zpm maq  en  no  -  Thu Jan 10 08:17:27 CST 2013  KANELA  Macro-Ge, Ge-Kaingang, Ge, Northwest, Timbira.
rao  Rao  -  rao  Papua New Guinea  1  1167  6658  RAO  -  -  -  dig sw ach  en  no  -  Mon Aug 5 19:09:46 CDT 2013  ANNABERG, RAO BRERI  Sepik-Ramu, Ramu, Ramu Proper, Annaberg, Rao.
rap  Rapa Nui  'Arero rapa nui  rap  Chile  9  7810  40627  PBA  rpn  -  -  ty wls mi  en  no  -  Wed Sep 18 23:10:16 CDT 2013  EASTER ISLAND, PASCUENSE  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Central Pacific, East Fijian-Polynesian, Polynesian, Nuclear, East, Rapanui.
rar  Rarotongan  Māori Kūki 'Āirani  rar  Cook Islands  52  56253  275576  RRT  ra  -  rrt  mi ty tkl tvl wls rap gil hla tzh mbt rmn  en  no  Tama'ine Ma'uke  Wed Sep 18 23:12:43 CDT 2013  COOK ISLAND, COOK ISLANDS MAORI, MAORI, KUKI AIRANI, RAROTONGAN-MANGAIAN  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Central Pacific, East Fijian-Polynesian, Polynesian, Nuclear, East, Central, Tahitic.
raw  Rawang  -  raw  Myanmar  172  232693  1373061  RAW  -  -  -  tl pam agn vi jv cdo  en  no  -  Fri Aug 9 17:09:06 CDT 2013  NUNG RAWANG, GANUNG-RAWANG, HKANUNG, NUNG, KRANGKU, TARON, KIUTZE, CH'OPA, CHIUTSE  Sino-Tibetan, Tibeto-Burman, Nungish.
rcf  Réunion Creole French  Kreol Renyone  rcf  Reunion  9  32000  187074  RCF  rcr  -  -  ht crs mfe acf lou  en  no  -  Thu Jan 24 22:15:45 CST 2013  -  Creole, French based.
rej-Latn  Rejang  Baso Hejang  rej  Indonesia (Sumatra)  13  3825  26540  REJ  -  -  -  nzm pam jv su sas tl id zlm jvn bjn  en  no  -  Wed Oct 9 15:27:11 CDT 2013  REDJANG, REJANG-LEBONG, JANG, DJANG, DJANG BELE TEBO  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Sundic, Malayic, Malayan, Para-Malay.
rgn  Romagnol  -  eml  Italy  36  5590  34471  -  -  -  -  rm ist lld it nap fur scn prv co lnc sc oc lij lmo  en  no  -  Wed Oct 9 15:59:32 CDT 2013  EMILIANO, EMILIAN, SAMMARINESE  Indo-European, Italic, Romance, Italo-Western, Western, Gallo-Iberian, Gallo-Romance, Gallo-Italian.
rif-Latn  Tarifit  Tarifit  rif  Morocco  70  20425  133259  RIF  -  -  -  kab tzm tmh stl nl nds-NL tbc fy act de  en  no  -  Wed Oct 9 17:36:33 CDT 2013  RIFI, RIFIA, NORTHERN SHILHA, SHILHA  Afro-Asiatic, Berber, Northern, Zenati, Riff.
rif-Tfng  Tarifit (Tifinagh)  -  rif  Morocco  18  11958  104135  RIF  -  -  -  tzm-Tfng  en  no  -  Wed Oct 9 17:25:11 CDT 2013  RIFI, RIFIA, NORTHERN SHILHA, SHILHA  Afro-Asiatic, Berber, Northern, Zenati, Riff.
rim  Nyaturu  -  rim  Tanzania  1  151115  1009800  RIM  -  -  -  kki pkb wmw ki  en  no  -  Fri Jan 11 09:15:55 CST 2013  TURU, KINYATURU, RIMI, LIMI, KIRIMI, REMI, KIREMI, KEREMI, WANYATURU, WALIMI  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, F, Nyilamba-Langi (F.30).
rkb  Rikbaktsa  -  rkb  Brazil  2  290225  2132652  ART  -  -  -  skg mjc st  en  no  -  Thu Jan 10 08:16:49 CST 2013  ARIPAKTSA, ERIKBATSA, ERIKPATSA, CANOEIRO  Macro-Ge, Rikbaktsa.
rm  Romansch  Rumantsch  roh  Switzerland  2810  3810560  25339688  RHE  rhs  rm  rhe  lmo eml lld it ka-Latn ha hwc  en it de  no  Gion-Andri Cantieni  Tue Sep 10 21:19:00 CDT 2013  RHETO-ROMANCE, RHAETO-ROMANCE, ROMANSH, ROMANCHE, RUMANTSCH  Indo-European, Italic, Romance, Italo-Western, Western, Gallo-Iberian, Gallo-Romance, Gallo-Rhaetian, Rhaetian.
rmn  Balkan Romani  -  rmn  Serbia  4  11530  70746  RMN  rm  -  rmn  mk-Latn  en  no  -  Wed Sep 11 10:09:43 CDT 2013  -  Indo-European, Indo-Iranian, Indo-Aryan, Central zone, Romani, Balkan.
rmn-BG  Bulgarian Romany  цигански (България)  rmn  Bulgaria  2  1177  8585  RMN  -  -  -  bg ru sr hbs-Cyrl mk sr-ME uk bs-Cyrl  en ru bg  no  -  Fri Sep 13 20:07:54 CDT 2013  -  Indo-European, Indo-Iranian, Indo-Aryan, Central zone, Romani, Balkan.
rmn-Grek  Greek Romani  Ρομανί  rmn  Greece  22  5567  37703  RMN  -  -  -  el pnt tsd grc  en el  no  -  Fri Sep 13 20:53:09 CDT 2013  -  Indo-European, Indo-Iranian, Indo-Aryan, Central zone, Romani, Balkan.
rmn-Grek-x-north  Greek Romani (North)  Ρομανί (Βόρεια Ελλάδα)  rmn  Greece  11  2919  19721  RMN  -  -  -  tsd grc  en el  no  -  Fri Sep 13 20:37:06 CDT 2013  -  Indo-European, Indo-Iranian, Indo-Aryan, Central zone, Romani, Balkan.
rmn-Grek-x-south  Greek Romani (South)  Ρομανί (Νότια Ελλάδα)  rmn  Greece  12  3066  20922  RMN  -  -  -  en  en el  no  -  Fri Sep 13 20:51:45 CDT 2013  -  Indo-European, Indo-Iranian, Indo-Aryan, Central zone, Romani, Balkan.
rmo  Sinte Romani  -  rmo  Serbia  1  227112  1210364  RMO  -  -  -  rmn br  en  no  -  Fri Jan 11 15:25:09 CST 2013  ROMMANES, SINTE, SINTI  Indo-European, Indo-Iranian, Indo-Aryan, Central zone, Romani, Northern.
rmy  Vlax Romani  -  rmy  Romania  4  210968  1141183  RMY  -  rmy  -  rmn rmo btx lcm  en  no  -  Fri Sep 13 19:46:05 CDT 2013  GYPSY, TSIGENE, ROMANESE, VLAX ROMANY, DANUBIAN  Indo-European, Indo-Iranian, Indo-Aryan, Central zone, Romani, Vlax.
rn  Rundi  Kirundi  run  Burundi  14  114566  866935  RUD  ru  rn  rud1  rw lg nyn ttj  en fr  no  Adriana Toni  Fri Sep 13 15:44:37 CDT 2013  KIRUNDI, URUNDI  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, J, Rwanda-Rundi (J.60).
rnd  Ruund  Uruund  rnd  Dem. Rep. of Congo  20  32016  202986  RND  dr  -  -  lun swc swh lue tum  en  no  -  Wed Feb 6 16:59:34 CST 2013  URUUND, NORTHERN LUNDA, LUUNDA, CHILUWUNDA, MUATIAMVUA, LUWUNDA, LUNDA-KAMBORO, LUNDA KAMBOVE  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, K, Salampasu-Ndembo (K.30).
ro  Romanian  Română  ron  Romania  4759  16695303  110378412  RUM  m  ro  rum  oc ca ia lnc sc it es ast gl pt fr  en  yes  Alexandru Szasz  Tue Sep 10 12:18:45 CDT 2013  RUMANIAN, MOLDAVIAN, DACO-RUMANIAN, ROMÂNA  Indo-European, Italic, Romance, Eastern.
rom  Romani  Romani ćhib  rom  Romania  9  771388  4383549  -  -  -  -  wls tkl sm tvl  en  no  -  Sun Feb 3 22:01:16 CST 2013  -  Indo-European, Indo-Iranian, Indo-Aryan, Central zone, Romani, Balkan.
rom-Cyrl  Romany (Cyrillic)  -  rom  Bulgaria  0  0  0  -  -  -  -  bg ru sr hbs-Cyrl mk sr-ME uk bs-Cyrl  en ru bg  no  -  -  -  Indo-European, Indo-Iranian, Indo-Aryan, Central zone, Romani, Balkan.
roo  Rotokas  -  roo  Papua New Guinea  0  0  0  ROO  -  -  -  tbg omw-x-aat omw-x-veq omw tqo kwn not ksd mcb kpr tgp khz  en  no  -  -  -  East Papuan, Bougainville, West, Rotokas.
rop  Kriol  Kriol  rop  Australia  1262  1128006  6679888  ROP  -  -  -  tcs na  en  no  Greg Dickson  Tue Jan 15 19:02:20 CST 2013  ROPER-BAMYILI CREOLE  Creole, English based, Pacific.
rro  Waima  -  rro  Papua New Guinea  0  0  0  RRO  -  -  -  meu mwc ho alu pwg khz npy gri kud bmk mlu swp tbo aui stn kqf  en  no  -  -  WAIMA  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Peripheral, Central Papuan, West Central Papuan, Nuclear.
rtm  Rotuman  Faeag Rotuma  rtm  Fiji  4  6338  29778  RTM  -  -  -  tvl tkl mbi mbt ppl nak hla luo ty niu  en  no  -  Wed Sep 18 23:15:12 CDT 2013  ROTUNA, RUTUMAN  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Central Pacific, West Fijian-Rotuman, Rotuman.
ru  Russian  Русский  rus  Russian Federation  17497  46212981  354050358  RUS  u  ru  rus  bg cu uk rue sr mk  en  yes  -  Mon Feb 4 12:27:56 CST 2013  RUSSKI, RUSSKY  Indo-European, Slavic, East.
ru-Latn  Russian (Latin)  -  rus  Russian Federation  31  872418  6669426  RUS  -  -  -  bg-Latn mk-Latn uk-Latn be-Latn cs sl sr-Latn  en ru  no  -  Wed Sep 11 14:24:12 CDT 2013  RUSSKI  Indo-European, Slavic, East.
rue  Rusyn  русиньскый язык  rue  Ukraine  4  105975  736176  RUE  -  rue  -  uk ru bg be  en  no  -  Thu Jan 24 22:18:41 CST 2013  RUTHENIAN, CARPATHIAN, CARPATHO-RUSYN  Indo-European, Slavic, East.
rug  Roviana  Roviana  rug  Solomon Islands  1  6811  38543  RUG  rv  -  -  gri kzf bgt fj  en  no  -  Thu Jan 24 22:19:12 CST 2013  ROBIANA, RUVIANA, RUBIANA  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, South New Ireland-Northwest Solomonic, New Georgia, West.
rup  Aromanian  Armãneashce  rup  Greece  77  315706  2170527  RUP  -  roa-rup  rmy1  ro scn it fur co sc  en  no  -  Tue Jan 29 20:57:33 CST 2013  MACEDO-RUMANIAN, MACEDO ROMANIAN, ARUMANIAN, AROMANIAN, ARMINA, VLACH  Indo-European, Italic, Romance, Eastern.
ruq  Megleno Romanian  Влахесте  ruq  Greece  28  3357  22809  RUQ  -  -  -  mo ru bg sr mk hbs-Cyrl uk rmn-BG  en  no  -  Mon Dec 2 08:26:56 CST 2013  MEGLENITIC, MEGLENITE  Indo-European, Italic, Romance, Eastern.
rut  Rutul  МыхIабишды чIел  rut  Russian Federation  3  1261  9624  RUT  -  -  -  av agx lez dar gag-Cyrl kum ce ky ru  en  no  -  Wed Oct 9 17:04:31 CDT 2013  RUTAL, RUTULY, RUTULTSY, MYKHANIDY, CHAL, MUKHAD  North Caucasian, Northeast, Lezgian.
rw  Kinyarwanda  Ikinyarwanda  kin  Rwanda  14809  24135408  182759428  RUA  yw  rw  rua1  rn lg nyn ttj  en fr  yes  Jackson Muhirwe, Steve Murphy, Philibert Ndandali  Mon Dec 2 16:38:14 CST 2013  RUANDA, KINYARWANDA, IKINYARWANDA, ORUNYARWANDA, URUNYARUANDA  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, J, Rwanda-Rundi (J.60).
rwo  Rawa  -  rwo  Papua New Guinea  563  650744  4587880  RWO  -  -  -  ubu ubu-x-kala imo ubu-x-nopenge ubu-x-andale zne xh kld gor  en  no  -  Tue Dec 3 11:06:55 CST 2013  RAUA, ERAWA, EREWA  Trans-New Guinea, Main Section, Central and Western, Huon-Finisterre, Finisterre, Gusap-Mot.
rwo-x-karo  Karo  -  rwo  Papua New Guinea  0  0  0  RWO  -  -  -  ubu ubu-x-kala imo ubu-x-nopenge ubu-x-andale zne xh kld gor  en  no  -  -  RAUA, ERAWA, EREWA  Trans-New Guinea, Main Section, Central and Western, Huon-Finisterre, Finisterre, Gusap-Mot.
rwo-x-rawa  Rawa  -  rwo  Papua New Guinea  0  0  0  RWO  -  -  -  rwo-x-karo zne nca hz mgd nnd kld kwn ach  en  no  -  -  RAUA, ERAWA, EREWA  Trans-New Guinea, Main Section, Central and Western, Huon-Finisterre, Finisterre, Gusap-Mot.
ryu  Central Okinawan  沖縄口  ryu  Japan  2  720  7047  RYU  -  -  -  ja  en ja  no  Michael Bauer  Wed Sep 18 23:17:38 CDT 2013  OKINAWAN, LUCHU  Japanese, Ryukyuan, Amami-Okinawan, Southern Amami-Okinawan.
sa  Sanskrit  संस्कृतम्  san  India  1307  2966467  21138533  SKT  -  sa  skt  pi ne hi  en  no  -  Wed Jan 30 17:07:10 CST 2013  -  Indo-European, Indo-Iranian, Indo-Aryan.
sab  Buglere  -  sab  Panama  1  442907  2423619  SAB  -  -  -  bwu  en  no  -  Thu Jan 10 08:38:10 CST 2013  BOKOTA, BOGOTA, BOFOTA, BOBOTA, BOCOTA, BUKUETA, NORTENYO, MURIRE, VERAGUAS SABANERO  Chibchan, Guaymi.
sah  Yakut  Саха тыла  sah  Russian Federation  19  413121  3283363  UKT  yk*  sah  sah  ky uz bua cv  en  no  -  Thu Jan 31 10:17:30 CST 2013  SAKHA, YAKUT-SAKHA  Altaic, Turkic, Northern.
sas  Sasak  -  sas  Indonesia (Nusa Tenggara)  1  190192  1231013  SAS  -  -  -  jv-x-bms id su zsm  en  no  -  Fri Jan 11 15:25:21 CST 2013  LOMBOK  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Sundic, Bali-Sasak.
sat  Santhali  Hor  sat  India  14  81961  473324  SNT  -  -  sat*  bn-Latn br cuk  en  no  -  Wed Sep 18 23:20:14 CDT 2013  HOR, HAR, SATAR, SANTHALI, SANDAL, SANGTAL, SANTAL, SENTALI, SAMTALI, SANTHIALI, SONTHAL  Austro-Asiatic, Munda, North Munda, Kherwari, Santali.
saz  Saurashtra  ꢱꣃꢬꢵꢰ꣄ꢜ꣄ꢬꢵ  saz  India  30  18891  134081  SAZ  -  -  -  -  en  no  Prabu Rengachari, Gerard Meijssen  Wed Sep 18 22:50:14 CDT 2013  SAURASHTRI, SOURASHTRA, SOWRASHTRA, PATNULI  Indo-European, Indo-Iranian, Indo-Aryan, Central zone, Gujarati.
sba  Ngambay  Ngambay  sba  Chad  2  9763  49222  SBA  ng  -  -  naq aa  en fr  no  -  Fri Jan 25 09:45:19 CST 2013  SARA, SARA NGAMBAI, GAMBA, GAMBAYE, GAMBLAI, NGAMBAI  Nilo-Saharan, Central Sudanic, West, Bongo-Bagirmi, Sara-Bagirmi, Sara, Sara Proper.
sbd  Southern Samo  -  sbd  Burkina Faso  3  268593  1122443  SBD  -  -  -  bm kpe dyu  en  no  -  Sat Dec 29 19:37:15 CST 2012  SAN, SANE  Niger-Congo, Mande, Eastern, Eastern, Samo.
sbe  Saliba  -  sbe  Papua New Guinea  0  0  0  SBE  -  -  -  swp viv pwg aui meu mox bmk bdd mpx kcc  en  no  -  -  -  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Nuclear, Suauic.
sbl  Botolan Sambal  -  sbl  Philippines  2  231028  1422840  SBL  -  -  -  pag war  en  no  -  Sat Dec 29 21:05:38 CST 2012  AETA NEGRITO, BOTOLAN ZAMBAL  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Northern Philippine, Bashiic-Central Luzon-Northern Mindoro, Central Luzon, Sambalic.
sc  Sardinian  Sardu  srd  Italy  659  1059044  6593372  -  -  sc  -  gl oc pt lnc es mwl cbk lij ast ro lmo prv gsc it  en it  yes  -  Mon Dec 2 14:09:28 CST 2013  SARD, SARDARESE, LOGUDORESE, CENTRAL SARDINIAN  Indo-European, Italic, Romance, Southern, Sardinian.
scn  Sicilian  Sicilianu  scn  Italy  128  1286323  8106026  SCN  -  scn  -  it co rmy pap fur  en it  no  -  Sat Jan 26 13:52:51 CST 2013  CALABRO-SICILIAN, SICILIANU  Indo-European, Italic, Romance, Italo-Western, Italo-Dalmatian.
scn-x-tara  Tarantino  -  scn  Italy  7  525138  3608462  SCN  -  roa-tara  -  nap it ia ro fr fur  en it  no  -  Tue Sep 10 08:11:45 CDT 2013  CALABRO-SICILIAN  Indo-European, Italic, Romance, Italo-Western, Italo-Dalmatian.
sco  Scots  Scots  sco  United Kingdom  153  286801  1747528  SCO  -  sco  sco  en trf goh yol ga gd lus  en  no  Caroline Macafee, Tony Dyer  Tue Sep 10 12:10:18 CDT 2013  LALLANS, LOWLAND SCOTS  Indo-European, Germanic, West, English.
sco-ulster  Ulster Scots  Ullans  sco  Ireland  55  84810  552347  SCO  -  -  -  sco-x-scotland en trf  en  no  -  Sat Jan 26 19:20:02 CST 2013  ULLANS  Indo-European, Germanic, West, English.
sco-x-scotland  Scots (Scotland)  Scots  sco  United Kingdom  2  78625  506533  SCO  -  sco  -  en sco-ulster  en  no  Caroline Macafee  Sat Jan 26 19:26:30 CST 2013  LALLANS, LOWLAND SCOTS  Indo-European, Germanic, West, English.
scs  North Slavey  -  scs  Canada  1  218  1419  SCS  -  -  -  chp  en  no  -  Thu Dec 13 17:01:35 CST 2012  SLAVI, DENÉ, MACKENZIAN, 'SLAVE'  Na-Dene, Nuclear Na-Dene, Athapaskan-Eyak, Athapaskan, Canadian, Hare-Chipewyan, Hare-Slavey.
scs-Cans  North Slavey (Syllabics)  -  scs  Canada  1  218  980  SCS  -  -  -  cr nsk oj-Cans iu  en  no  -  Thu Dec 13 17:37:27 CST 2012  SLAVI, DENÉ, MACKENZIAN, 'SLAVE'  Na-Dene, Nuclear Na-Dene, Athapaskan-Eyak, Athapaskan, Canadian, Hare-Chipewyan, Hare-Slavey.
sd  Sindhi  ﺲﻧڌﻱ، ﺲﻧﺩھی ،  snd  Pakistan  953  2521246  13513898  SND  nd*  sd  snd*  glk prs  en  yes  Abdul Rahim Nizamani  Fri Sep 13 14:06:38 CDT 2013  -  Indo-European, Indo-Iranian, Indo-Aryan, Northwestern zone, Sindhi.
sda  Toraja-Sa’dan  -  sda  Indonesia (Sulawesi)  3  153823  1053076  SDA  -  -  -  mvp ptu lcm su bjn min sml  en  no  -  Mon Feb 18 23:02:43 CST 2013  SA'DAN, SADAN, SADANG, TORAJA, TORADJA, TAE', TA'E, SOUTH TORAJA, SA'DANSCHE  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Sulawesi, South Sulawesi, Northern, Toraja-Sa'dan.
sdc  Sassarese Sardinian  Sassaresu  sdc  Italy  44  9543  64383  SDC  -  -  -  scn co rup it pap-CW fur pov pap io kea  en it  no  -  Sat Nov 16 17:53:12 CST 2013  NORTHWESTERN SARDINIAN, SASSARESE  Indo-European, Italic, Romance, Southern, Sardinian.
sdh  Southern Kurdish  کوردی خوارگ  sdh  Iran  120  24531  153839  SDH  -  -  -  en  en  no  -  Sun Nov 17 12:45:26 CST 2013  -  Indo-European, Indo-Iranian, Iranian, Western, Northwestern, Kurdish
sdz  Sallands  -  sdz  Netherlands  1  1415  7240  SNK  -  -  -  nl nds-NL act zea gos vls li drt nds fy de lb af da  en  no  -  Thu Mar 14 13:38:18 CDT 2013  SALLAND, SALLAN  Indo-European, Germanic, West, Low Saxon-Low Franconian, Low Saxon.
se  Northern Sámi  Davvisámegiella  sme  Norway  1023  2006227  15315412  LPR  -  se  lpi  smj fi ekk toj fkv tzt fy mk-Latn vro sv  en no  yes  Trond Trosterud, Linda Wiechetek  Fri Sep 13 11:57:39 CDT 2013  'NORTHERN LAPPISH', 'NORWEGIAN LAPP', SAAMI, SAME, SAMIC, 'LAPP'  Uralic, Finno-Ugric, Finno-Permic, Finno-Cheremisic, Finno-Mordvinic, Finno-Lappic, Lappic, Northern.
sec  Sechelt  Shashishalhem  sec  Canada  0  0  0  SEC  -  -  -  hur-x-upr  en  no  -  -  -  Salishan, Central Salish, Northern.
seh  Sena  Cisena  seh  Mozambique  1  43241  308123  SEH  sen  -  -  ny tum wmw dig kki sw  en  no  -  Sun Jan 20 11:54:25 CST 2013  CISENA, CHISENA  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, N, Senga-Sena (N.40), Sena.
sei  Seri  Cmique Itom  sei  Mexico  17  93645  555063  SEI  -  -  -  cao nhx nch  en es  no  -  Wed Sep 18 23:22:45 CDT 2013  -  Hokan, Salinan-Seri.
sek  Sekani  Tsek’ehne  sek  Canada  0  0  0  SEK  -  -  -  caf crx kkz  en  no  -  -  -  Na-Dene, Nuclear Na-Dene, Athapaskan-Eyak, Athapaskan, Canadian, Beaver-Sekani.
sey  Secoya  -  sey  Ecuador  6  218036  1533261  SEY  -  -  1123  snn  en es  no  -  Wed Jan 30 11:55:28 CST 2013  -  Tucanoan, Western Tucanoan, Northern, Siona-Secoya.
sg  Sango  Sängö  sag  Central African Republic  477  765552  3794676  SAJ  sg  sg  saj  tzu ilo bfa gri men yo zne fj tzc ln omq-x-amuzgo  en fr  no  -  Mon Dec 2 14:09:21 CST 2013  SANGHO  Creole, Ngbandi based.
sgb  Mag-antsi Ayta  -  sgb  Philippines  1  225259  1322125  SGB  -  -  -  sbl ifk ifb itv bku bnc pag  en  no  -  Mon Feb 18 22:53:57 CST 2013  MAG-ANCHI SAMBAL  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Northern Philippine, Bashiic-Central Luzon-Northern Mindoro, Central Luzon, Sambalic.
sgc  Kipsigis  -  sgc  Kenya  10  1454  9574  -  -  -  -  ppl ain mbi zpi mbt gba luo fai  en  no  -  Wed Oct 9 17:56:06 CDT 2013  -  Nilo-Saharan, Eastern Sudanic, Nilotic, Southern, Kalenjin, Nandi-Markweta, Kipsigis.
sgs  Samogitian  Žemaitėška  sgs  Lithuania  3  336256  2783646  -  -  bat-smg  -  lt  en  no  -  Tue Jan 29 18:11:17 CST 2013  -  Indo-European, Baltic, Eastern.
sgz  Sursurunga  -  sgz  Papua New Guinea  0  0  0  SGZ  -  -  -  lbb kqw lcm su gfk bjn bnp btd ksd due pam  en  no  -  -  -  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, South New Ireland-Northwest Solomonic, Patpatar-Tolai.
shh  Shoshoni  Sosoni'  shh  USA  11  5077  46396  SHH  -  -  -  nds  en  no  -  Sat Oct 5 21:28:48 CDT 2013  SHOSHONE  Uto-Aztecan, Northern Uto-Aztecan, Numic, Central.
shi-Latn  Tachelhit (Latin)  Tacelḥit  shi  Morocco  2  104948  875848  SHI  -  -  -  tmh ha bjn ifb itv id zsm ifk  en  no  -  Thu Sep 19 12:21:03 CDT 2013  TASHILHEET, TACHILHIT, TASHELHIT, TASOUSSIT, SHILHA, SUSIUA, SOUTHERN SHILHA  Afro-Asiatic, Berber, Northern, Atlas.
shi-Tfng  Tachelhit (Tifinagh)  -  shi  Morocco  62  30441  191194  SHI  -  -  -  tzm-Tfng rif-Tfng  en  no  -  Wed Oct 9 22:03:35 CDT 2013  TASHILHEET, TACHILHIT, TASHELHIT, TASOUSSIT, SHILHA, SUSIUA, SOUTHERN SHILHA  Afro-Asiatic, Berber, Northern, Atlas.
shk  Shilluk  -  shk  Sudan  2  179993  923874  SHK  -  -  shk  gux bim lwo agu ajg  en  no  -  Tue Feb 19 10:46:59 CST 2013  COLO, DHOCOLO, CHULLA, SHULLA  Nilo-Saharan, Eastern Sudanic, Nilotic, Western, Luo, Northern, Shilluk.
shn  Shan  -  shn  Myanmar  51  12829  193756  SJN  -  -  -  my pi-Mymr  en  no  -  Fri Nov 15 21:52:40 CST 2013  SHA, TAI SHAN, SAM, THAI YAI, TAI YAI, GREAT THAI, TAI LUANG, 'NGIO', 'NGIOW', 'NGIAW', 'NGIAO', 'NGEO'  Tai-Kadai, Kam-Tai, Be-Tai, Tai-Sek, Tai, Southwestern, East Central, Northwest.
shp  Shipibo-Conibo  -  shp  Peru  5  919969  5723539  SHP  -  -  shp  amc kaq  en es  no  -  Thu Jan 31 10:17:48 CST 2013  -  Panoan, North-Central.
shs  Shuswap  Secwepemctsín  shs  Canada  3  1886  13041  SHS  -  -  -  lil hur mbi zpi  en  yes  Neskie Manuel, Mona Jules, Gabe Archie  Sun Jan 20 12:02:57 CST 2013  SECWEPEMC, SECWEPEMCTSIN  Salishan, Interior Salish, Northern.
si  Sinhala  සිංහල  sin  Sri Lanka  429  3064568  20064919  SNH  sn  si  snh*  pi-Sinh  en  yes  Tharindu Dananjaya Delgolla  Wed Sep 11 15:03:44 CDT 2013  SINHALESE, SINGHALESE, SINGHALA, CINGALESE  Indo-European, Indo-Iranian, Indo-Aryan, Sinhalese-Maldivian.
sid  Sidamo  Sidaama  sid  Ethiopia  174  198913  1627637  SID  dm  -  -  gmo wal gof gmv mqj gbi om  en  no  Daniel Worku  Mon Jan 13 19:31:44 CST 2014  SIDÁMO 'AFÓ, SIDAMINYA  Afro-Asiatic, Cushitic, East, Highland.
sig  Paasaal  -  sig  Ghana  1  276550  1217759  SIG  -  -  -  cme kma ntr mzw  en  no  -  Tue Feb 19 10:39:00 CST 2013  PASAALE, FUNSILE, SOUTHERN SISAALA  Niger-Congo, Atlantic-Congo, Volta-Congo, North, Gur, Central, Southern, Grusi, Western.
sil  Tumulung Sisaala  -  sil  Ghana  1  240092  1119871  SIL  -  -  -  sbd hag maw mzw man cme mnk  en  no  -  Tue Feb 19 10:44:15 CST 2013  SISAI, ISSALA, HISSALA, SISALA TUMU, ISAALUNG  Niger-Congo, Atlantic-Congo, Volta-Congo, North, Gur, Central, Southern, Grusi, Western.
sim  Mende  -  sim  Papua New Guinea  0  0  0  SIM  -  -  -  kj ng kwj sw sml dig  en  no  -  -  SEIM, TAU, KUBIWAT  Sepik-Ramu, Sepik, Middle Sepik, Nukuma.
sio-x-dakota  Dakota languages  -  sio  USA  25  146339  898040  -  -  -  -  nii pon fai hus hsf ncj kut bim fi kms  en  no  -  Tue Oct 8 20:24:08 CDT 2013  -  Siouan, Siouan Proper, Central, Mississippi Valley, Dakota.
sja  Epena  -  sja  Colombia  2  237104  1681829  SJA  -  -  1126*  cto emp var kew des  en es  no  -  Tue Sep 10 15:18:08 CDT 2013  SAIJA, EPENÁ SAIJA, EPEA PEDÉE, SOUTHERN EMBERA, SOUTHERN EMPERA, CHOLO  Choco, Embera, Southern.
sjd  Kildin Sami  Кӣллт са̄мь кӣлл  sjd  Russian Federation  35  10267  99577  LPD  -  -  -  cv sah mhr koi kpv kv lez  en ru  no  -  Wed Oct 9 22:39:38 CDT 2013  'KILDIN LAPPISH', 'LAPP', SAAM  Uralic, Finno-Ugric, Finno-Permic, Finno-Cheremisic, Finno-Mordvinic, Finno-Lappic, Lappic, Central.
sk  Slovak  Slovenčina  slk  Slovakia  7740  11198713  74502209  SLO  v  sk  slo  cs sl sr-Latn bs pl hr hbs mk-Latn bg-Latn  en  yes  -  Fri Aug 23 22:34:39 CDT 2013  SLOVAKIAN, SLOVENCINA  Indo-European, Slavic, West, Czech-Slovak.
skg  Sakalava Malagasy  -  skg  Madagascar  176  180823  1251022  SKG  vz  -  -  xmv buc plt rkb  en  no  -  Tue Feb 5 20:13:17 CST 2013  -  Austronesian, Malayo-Polynesian, Greater Barito, East, Malagasy
skr  Seraiki  سرائیکی  skr  Pakistan  3  4920  23580  SKR  -  -  skr  pnb ur  en  no  -  Wed Sep 18 23:25:28 CDT 2013  RIASITI, BAHAWALPURI, MULTANI, SOUTHERN PANJABI, SIRAIKI  Indo-European, Indo-Iranian, Indo-Aryan, Northwestern zone, Lahnda.
sl  Slovenian  Slovenščina  slv  Slovenia  2872  13841612  93432614  SLV  sv  sl  slv  sr-Latn bs hr mk-Latn sk bg-Latn cs  en  yes  -  Wed Feb 6 22:12:00 CST 2013  SLOVENSCINA, SLOVENE  Indo-European, Slavic, South, Western.
sld  Sissala  -  sld  Burkina Faso  1  205863  1004486  SLD  -  -  -  lem nko  en  no  -  Tue Feb 19 11:14:18 CST 2013  SISAALI  Niger-Congo, Atlantic-Congo, Volta-Congo, North, Gur, Central, Southern, Grusi, Western.
sli  Lower Silesian  Schläsch  sli  Poland  45  8034  64215  SLI  -  -  -  de gsw pdc lb pfl vmf ksh nds bar li fy da ca  en  no  -  Thu Oct 10 13:28:46 CDT 2013  LOWER SCHLESISCH  Indo-European, Germanic, West, High German, German, Middle German, East Middle German.
sll  Salt-Yui  -  sll  Papua New Guinea  0  0  0  SLL  -  -  -  gvf bbc-Latn kue gfk bts  en  no  -  -  SALT, SALT-IUI, YUI, IUI  Trans-New Guinea, Main Section, Central and Western, East New Guinea Highlands, Central, Chimbu.
slm  Pangutaran Sama  -  slm  Philippines  1  2110  12545  SLM  -  -  -  sml bjn hnn bik ifk su mmn bku  en  no  -  Wed Apr 24 22:27:06 CDT 2013  -  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Sama-Bajaw, Sulu-Borneo, Western Sulu Sama.
slr  Salar  Salırça  slr  China  26  22800  177981  SLR  -  -  -  tr jct-Latn kdr crh tk az gag uzn-Latn kaa  en  no  -  Thu Oct 10 13:42:35 CDT 2013  SALA  Altaic, Turkic, Southern.
sm  Samoan  Gagana Sāmoa  smo  Western Samoa  568  2170106  11130333  SMY  sm  sm  smy  fud tkl tvl haw  en  started  Tim Knapp, Soane Tupou, James Collins, Sonya Van Schaijik  Tue Sep 10 11:44:02 CDT 2013  -  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Central Pacific, East Fijian-Polynesian, Polynesian, Nuclear, Samoic-Outlier, Samoan.
sma  South Saami  Åarjelsaemien gïele  sma  Sweden  179  164056  1441492  LPC  -  -  -  af  en  yes  Linda Wiechetek, David Jonasson, Neeta Jääskö  Wed Sep 18 23:27:58 CDT 2013  'LAPP', SOUTHERN LAPP  Uralic, Finno-Ugric, Finno-Permic, Finno-Cheremisic, Finno-Mordvinic, Finno-Lappic, Lappic, Southern.
smj  Lule Saami  Julevsámegiella  smj  Sweden  445  394102  2817586  LPL  -  -  -  se  en  yes  Linda Wiechetek, Neeta Jääskö  Fri Sep 13 11:52:15 CDT 2013  LULE, 'LAPP'  Uralic, Finno-Ugric, Finno-Permic, Finno-Cheremisic, Finno-Mordvinic, Finno-Lappic, Lappic, Southern.
smk  Bolinao  -  smk  Philippines  0  0  0  SMK  -  -  -  bik sbl pag iry hnn kne ha sml bnc bjn ifk slm sgb  en  no  -  -  BOLINAO SAMBAL, BOLINAO ZAMBAL  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Northern Philippine, Bashiic-Central Luzon-Northern Mindoro, Central Luzon, Sambalic.
sml  Sinama  Bahasa Sinama  sml  Philippines  4  6553  45156  SML  -  -  -  hnn bik bjn bts hil su abx kyk tl  en  no  Luke Schroeder  Fri Sep 13 11:28:21 CDT 2013  SIASI SAMA, CENTRAL SINAMA, SAMAL, SINAMA  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Sama-Bajaw, Sulu-Borneo, Inner Sulu Sama.
smn  Inari Saami  Anarâškielâ  smn  Finland  53  32678  303203  LPI  -  -  -  ekk se mt vro fkv smj csk fi  en  no  Neeta Jääskö  Wed Sep 19 17:35:56 CDT 2012  INARI 'LAPPISH', ANAR, 'FINNISH LAPP', 'LAPP', SÁMI, SAMIC, SAAM, SAAME  Uralic, Finno-Ugric, Finno-Permic, Finno-Cheremisic, Finno-Mordvinic, Finno-Lappic, Lappic, Eastern.
sms  Skolt Saami  sääˊmǩiõll  sms  Finland  2  1034  8775  LPK  -  -  -  se et fi  en  no  Neeta Jääskö  Wed Sep 19 20:19:21 CDT 2012  SKOLT LAPPISH, RUSSIAN LAPP, 'LAPP', SAAME, SAME, LOPAR, KOLTA, KOLTTA  Uralic, Finno-Ugric, Finno-Permic, Finno-Cheremisic, Finno-Mordvinic, Finno-Lappic, Lappic, Central.
sn  Shona  chiShona  sna  Zimbabwe  273  333479  2612132  SHD  ca  sn  shd  ndc tum ny seh rw kwn  en  yes  Boniface Manyame, James Mlambo  Mon Dec 2 14:09:14 CST 2013  'SWINA', CHISHONA  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, S, Shona (S.10).
snc  Sinaugoro  -  snc  Papua New Guinea  0  0  0  SNC  -  -  -  khz meu gri pwg bmk dww rro mwc ksd fj alu stn ho  en  no  -  -  SINAGORO  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Peripheral, Central Papuan, Sinagoro-Keapara.
snk  Soninke  -  snk  Mali  3  8874  47012  SNN  -  -  snn  ha  en fr  no  -  Wed Jan 16 09:54:18 CST 2013  MARKA, MARAKA, SARAKOLE, SARAKULE, SARAWULE, SERAHULI, SILABE, TOUBAKAI, WAKORE, GADYAGA, ASWANIK, DIAWARA  Niger-Congo, Mande, Western, Northwestern, Samogo, Soninke-Bobo, Soninke-Boso, Soninke.
snn  Siona  -  snn  Colombia  3  241703  1766034  SIN  -  -  1121  sey xsm miq tav gux  en es  no  -  Wed Jan 30 20:57:25 CST 2013  SIONI, PIOJE, PIOCHE-SIONI  Tucanoan, Western Tucanoan, Northern, Siona-Secoya.
snp  Siane  -  snp  Papua New Guinea  0  0  0  SNP  -  -  -  snp-x-lambau kng yby bef ktu swh knv ln  en  no  -  -  SIANI  Trans-New Guinea, Main Section, Central and Western, East New Guinea Highlands, East-Central, Siane.
snp-x-lambau  Siane (Lambau)  -  snp  Papua New Guinea  0  0  0  SNP  -  -  -  yby bef kng ktu kud ln swh chw gor  en  no  -  -  SIANI  Trans-New Guinea, Main Section, Central and Western, East New Guinea Highlands, East-Central, Siane.
sny  Saniyo-Hiyewe  -  sny  Papua New Guinea  0  0  0  SNY  -  -  -  ain ipi tvl rtm bon mbt  en  no  -  -  SANIO-HIOWE, SANIO, SANIYO, HIOWE, HIYOWE  Sepik-Ramu, Sepik, Sepik Hill, Sanio.
so  Somali  Soomaaliga  som  Somalia  3104  9449403  64606335  SOM  -  so  som  om son kne ha wal  en  yes  Mohamed I. Mursal  Mon Feb 4 10:44:22 CST 2013  AF-SOOMAALI, AF-MAXAAD TIRI, COMMON SOMALI, STANDARD SOMALI  Afro-Asiatic, Cushitic, East, Somali.
son  Songhay  Soŋay  son  Mali  10  68739  355644  SON  -  -  -  so om mif mnk snk ha  en  yes  Abdoul Cisse, Mohomodou Houssouba  Sun Jan 20 12:13:40 CST 2013  SONGHAI, SONGAY, SONGAI, SONGOI, SONGOY, SONGHOY, SONRAI, SONRHAI, KOROBORO SENNI SONGHAY, SONGAY SENNI, EAST SONGHAY, GAO SONGHAY, KOYRA SENNI SONGHAY  Nilo-Saharan, Songhai, Southern.
sop  Songe  Kisonge  sop  Dem. Rep. of Congo  17  170547  1139451  SOP  ksn  -  -  lua lu kqn kcc bem  en  no  -  Mon Dec 2 16:30:43 CST 2013  SONGYE, KISONGYE, LUSONGE, KALEBWE, NORTHEAST LUBA, YEMBE, KISONGE, LUBA-SONGI, KISONGI  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, L, Songye (L.20).
soq  Kanasi  -  soq  Papua New Guinea  0  0  0  SOQ  -  -  -  mti dgz kud wmw sbe kqf dob sw swh viv mwc  en  no  -  -  SONA  Trans-New Guinea, Main Section, Eastern, Central and Southeastern, Dagan.
soy  Miyobe  -  soy  Benin  1  201461  1055828  SOY  -  -  -  ada ken kbp  en  no  -  Tue Feb 19 11:16:46 CST 2013  SORUBA, BIJOBE, BIYOBE, SOROUBA, SOLLA, UYOBE, MIYOBE, MEYOBE, KAYOBE, KUYOBE, SOLAMBA  Niger-Congo, Atlantic-Congo, Volta-Congo, North, Gur, Central, Northern, Oti-Volta, Gurma.
spl  Selepet  -  spl  Papua New Guinea  0  0  0  SEL  -  -  -  kpf kng tbc yaf snp itv ifk dgz ch  en  no  -  -  SELEPE  Trans-New Guinea, Main Section, Central and Western, Huon-Finisterre, Huon, Western.
spp  Supyire Senoufo  -  spp  Mali  1  248482  1187718  SPP  -  -  -  myk nfr amu ig gri  en  no  -  Tue Feb 19 11:22:43 CST 2013  SUPYIRE, SUP'IDE, SUPPIRE  Niger-Congo, Atlantic-Congo, Volta-Congo, North, Gur, Senufo, Suppire-Mamara.
sps  Saposa  -  sps  Papua New Guinea  0  0  0  SPS  -  -  -  leu hla pag gil bik plt snk  en  no  -  -  -  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, South New Ireland-Northwest Solomonic, Nehan-North Bougainville, Saposa-Tinputz.
spy  Sabaot  -  spy  Kenya  2  147401  1168066  SPY  -  -  -  enb kbr  en  no  -  Sat Dec 29 22:10:50 CST 2012  MT. ELGON MAASAI  Nilo-Saharan, Eastern Sudanic, Nilotic, Southern, Kalenjin, Elgon.
sq  Albanian  Shqip  sqi  Albania  4801  11690239  71137517  -  al  sq  -  zac to  en  yes  -  Mon Feb 4 14:08:52 CST 2013  TOSK, ARNAUT, SHKIP, SHQIP, SKCHIP, SHQIPERË, ZHGABE  Indo-European, Albanian, Tosk.
squ  Squamish  Skwxwú7mesh-ulh sníchim  squ  Canada  0  0  0  SQU  -  -  -  lil-x-fou lil blc  en  no  -  -  -  Salishan, Central Salish, Squamish.
sr  Serbian (Cyrillic)  Српски (ћирилица)  srp  Serbia  887  1038408  6974406  SDD  sb  sr  src5  bs-Cyrl mk bg ru uk rue  en  yes  Goran Rakic, Toma Tasovac  Fri Sep 13 12:25:06 CDT 2013  MONTENEGRIN.  Indo-European, Slavic, South, Western.
sr-Latn  Serbian (Latin)  Srpski (latinica)  srp  Serbia  3454  5876686  41515692  SDD  sbo  -  src3  sl mk-Latn  en  yes  Goran Rakic, Toma Tasovac  Wed Sep 11 14:28:00 CDT 2013  MONTENEGRIN.  Indo-European, Slavic, South, Western.
sr-Latn-ME  Montenegrin (Latin)  -  srp  Montenegro  235  794760  5564748  SDD  -  -  -  sl mk-Latn  en  started  Goran Rakic, Toma Tasovac  Tue Jan 29 17:40:04 CST 2013  MONTENEGRIN.  Indo-European, Slavic, South, Western.
sr-ME  Montenegrin (Cyrillic)  -  srp  Montenegro  96  143663  1127118  SDD  sb  -  -  bs-Cyrl mk bg ru uk rue  en ru  started  Goran Rakic, Toma Tasovac  Tue Jan 29 17:06:45 CST 2013  MONTENEGRIN.  Indo-European, Slavic, South, Western.
srb  Sora  -  srb  India  1  1917  12391  SRB  -  -  -  jv-x-bms bjn zsm id  en  no  -  Tue Apr 30 15:10:38 CDT 2013  SAORA, SAONRAS, SHABARI, SABAR, SAURA, SAVARA, SAWARIA, SWARA, SABARA  Austro-Asiatic, Munda, South Munda, Koraput Munda, Sora-Juray-Gorum, Sora-Juray.
src  Logudorese Sardinian  -  src  Italy  1  2145  13314  SRD  -  -  srd  mxi es pt gl ast oc ia cbk mwl lnc lad ca ro  en  no  -  Mon Dec 9 14:13:21 CST 2013  SARD, SARDARESE, LOGUDORESE, CENTRAL SARDINIAN  Indo-European, Italic, Romance, Southern, Sardinian.
sri  Siriano  -  sri  Colombia  2  173245  1328268  SRI  -  -  -  srq des cbc tuo-CO  en es  no  -  Fri Jan 25 22:24:16 CST 2013  -  Tucanoan, Eastern Tucanoan, Central, Desano.
srl  Isirawa  -  srl  Indonesia (Irian Jaya)  1  311  1993  SRL  -  -  -  wmw tqo  en  no  -  Sun Jan 20 20:36:26 CST 2013  SAWERI, SABERI, OKWASAR  Trans-New Guinea, Main Section, Central and Western, Dani-Kwerba, Northern, Isirawa.
srm  Saramaccan  Sramakatongo  srm  Suriname  55  625547  2813811  SRM  srm  -  -  djk pap srn kea pap-CW jam pov co due bpr bps dgc cri  en  no  -  Tue Feb 5 19:47:24 CST 2013  -  Creole, English based.
srn  Sranan  Sranantongo  srn  Suriname  92  619094  3298145  SRN  sr  srn  -  djk  en  no  -  Tue Sep 10 08:10:07 CDT 2013  SRANAN TONGO, TAKI-TAKI, SURINAAMS, SURINAMESE, SURINAME CREOLE ENGLISH  Creole, English based, Atlantic, Suriname.
srq  Sirionó  -  srq  Bolivia  2  257466  1572725  SRQ  -  -  -  sri des cbc cpu myy mcb  en es  no  -  Thu Dec 27 22:19:01 CST 2012  -  Tupi, Tupi-Guarani, Guarayu-Siriono-Jora (II).
srr  Serer-Sine  Seereer  srr  Senegal  2  4475  21500  SES  er  -  ses  tw kno  en fr  no  -  Wed Jan 16 10:00:35 CST 2013  SÉRÈRE-SINE, SERER, SERRER, SEREER, SEEREER, SERER-SIN, SINE-SALOUM, SEEX, SINE-SINE  Niger-Congo, Atlantic-Congo, Atlantic, Northern, Senegambian, Serer.
ss  Swati  siSwati  ssw  Swaziland  49  332436  3153412  SWZ  swi  ss  swz1  zu nr xh nd ts  en  yes  Friedel Wolff, Dwayne Bailey  Tue Sep 10 14:53:30 CDT 2013  SWAZI, ISISWAZI, SISWATI, TEKELA, TEKEZA  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, S, Nguni (S.40).
ssd  Siroi  -  ssd  Papua New Guinea  0  0  0  SSD  -  -  -  mna mwv kqn ipi kue ain lu gfk wmw loz mee  en  no  -  -  SUROI  Trans-New Guinea, Madang-Adelbert Range, Madang, Rai Coast, Kabenau.
ssg  Seimat  -  ssg  Papua New Guinea  0  0  0  SSG  -  -  -  hla mi sg tkl gil tgg nij ilo haw rom  en  no  -  -  NINIGO  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Admiralty Islands, Western.
ssx  Samberigi  -  ssx  Papua New Guinea  0  0  0  SSX  -  -  -  twu mna alu bgt npy mee okv  en  no  -  -  SAU, SANABERIGI  Trans-New Guinea, Main Section, Central and Western, East New Guinea Highlands, West-Central, Angal-Kewa.
st  Southern Sotho  Sesotho  sot  Lesotho  1715  4158880  22927012  SSO  su  st  sso  tn nso  en  yes  Friedel Wolff, Dwayne Bailey  Wed Sep 11 10:13:00 CDT 2013  SUTO, SUTHU, SOUTO, SESOTHO, SISUTHO, SOTHO, SUTU, SESUTU  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, S, Sotho-Tswana (S.30), Sotho, Southern.
stl  Stellingwerfs  -  stl  Netherlands  2  4602  25604  STL  -  -  -  nl nds-NL sdz act drt gos zea vls nds de-DE fy li  en  no  -  Thu Mar 14 15:35:57 CDT 2013  STELLINGWERFSTELLINGWARFS  Indo-European, Germanic, West, Low Saxon-Low Franconian, Low Saxon.
stn  Owa  -  stn  Solomon Islands  3  269278  1436857  STN  -  -  -  fj pwg  en  no  -  Fri Jan 25 22:17:45 CST 2013  OWA RAHA, ANGANIWAI, ANGANIWEI, NARIHUA, SANTA ANA, WANONI  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Southeast Solomonic, Malaita-San Cristobal, San Cristobal.
stp  Southeastern Tepehuan  -  stp  Mexico  2  421439  2145192  STP  -  -  -  omq-x-amuzgo amu xsm ln azg gri kog mer fj bng nfr  en  no  -  Thu Dec 27 22:27:05 CST 2012  SOUTHEASTERN TEPEHUÁN, TEPEHUÁN SURESTE  Uto-Aztecan, Southern Uto-Aztecan, Sonoran, Tepiman, Southern Tepehuan.
stq  Saterfriesisch  Seeltersk  stq  Germany  14  325516  2072347  FRS  -  stq  -  ksh  en de  no  -  Wed Jan 16 10:04:40 CST 2013  OSTFRIESISCH, SATERLANDIC FRISIAN, SEELTERSK FRISIAN  Indo-European, Germanic, West, Frisian.
str  Straits Salish  -  str  Canada  2  1426  8151  STR  -  -  -  bnp trf ghs  en  no  -  Sat Jan 26 13:51:28 CST 2013  STRAITS  Salishan, Central Salish, Straits.
su  Sunda  Basa Sunda  sun  Indonesia (Java and Bali)  330  1045946  7153456  SUO  -  su  suo  jv-x-bms bjn jv id pam zsm tl  en  started  Mang Jamal, Hawe Setiawan, Mikihiro Moriyama, Iwa Lukmana  Fri Jan 25 16:43:20 CST 2013  SUNDANESE, PRIANGAN  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Sundic, Sundanese.
sua  Sulka  -  sua  Papua New Guinea  166  798936  3788648  SLK  -  -  -  krj mmn mee pam lcm wsk hil tl cps kyk  en  no  -  Mon Sep 23 10:41:55 CDT 2013  -  East Papuan, Yele-Solomons-New Britain, New Britain, Sulka.
sue  Suena  -  sue  Papua New Guinea  0  0  0  SUE  -  -  -  mti soq nou fj wmw bmk pwg gdn sw dgz  en  no  -  -  YEMA, YARAWE, YARAWI  Trans-New Guinea, Main Section, Eastern, Binanderean, Binanderean Proper.
suk  Sukuma  -  suk  Tanzania  3  182388  1156132  SUA  -  -  sua  nym kki gog loz bem pkb sop sw ln tum  en  no  -  Fri Jan 25 16:07:28 CST 2013  KISUKUMA  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, F, Sukuma-Nyamwezi (F.20).
sum  Sumo-Mayangna  -  sum  Nicaragua  2  37301  227284  SUM  myg  -  -  miq lef swh ha fj aui gux  en es  no  -  Fri Jan 25 16:19:50 CST 2013  SUMU, SOUMO, SUMOO, WOOLWA, SUMO, ULWA  Misumalpan.
sur  Mwaghavul  -  sur  Nigeria  1  255193  1236841  SUR  -  -  -  udu myk  en  no  -  Tue Feb 19 11:51:11 CST 2013  SURA  Afro-Asiatic, Chadic, West, A, A.3, Angas Proper, 1.
sus  Susu  -  sus  Guinea  3  212037  1001862  SUD  -  -  sud  snk kao knk ha kno  en  no  -  Fri Jan 25 16:21:38 CST 2013  SOSO, SUSOO, SOUSSOU, SOSE  Niger-Congo, Mande, Western, Central-Southwestern, Central, Susu-Yalunka.
suz  Sunwar  -  suz  Nepal  0  0  0  SUZ  -  -  -  lif mai ne npi bh hi taj mr  en  no  -  -  SUNUWAR, SUNBAR, SUNWARI, MUKHIYA, KWOICO LO  Sino-Tibetan, Tibeto-Burman, Himalayish, Mahakiranti, Kham-Magar-Chepang-Sunwari, Sunwari.
sv  Swedish  Svenska  swe  Sweden  1278  3710583  24170795  SWD  z  sv  swd  no nn nb da nl  en  yes  -  Wed Sep 11 10:19:56 CDT 2013  SVENSKA, RUOTSI  Indo-European, Germanic, North, East Scandinavian, Danish-Swedish, Swedish.
sva-Geor  Svan  -  sva  Georgia  1  473  3443  SVA  -  -  -  xmf ka  en  no  -  Thu Mar 14 19:02:38 CDT 2013  LUSHNU, SVANURI  South Caucasian, Svan.
sw  Swahili  Kiswahili  swa  Tanzania  1042  4761424  31085152  -  sw  sw  -  wmw pkb dig tum kki swb nyf loz kam ki  en  yes  Jason Githeko, Alberto Escudero, Martin Benjamin  Sun Nov 3 20:46:28 CST 2013  KISWAHILI, KISUAHELI  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, G, Swahili (G.40).
sw-Arab  Swahili (Arabic)  -  swa  Tanzania  0  0  0  SWA  -  -  -  ayp bal sd bqi glk ur ps fa ar  en  no  Kevin Donnelly  -  KISWAHILI, KISUAHELI  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, G, Swahili (G.40).
swb  Maore Comorian  -  swb  Comoros Islands  20  172790  866427  SWB  orr  -  swb*  swh wmw pkb swc dig kki nyf  en fr  no  -  Sat Jan 26 13:59:32 CST 2013  COMORES SWAHILI, KOMORO, COMORO, COMORIAN  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, G, Swahili (G.40).
swc  Congo Swahili  -  swc  Dem. Rep. of Congo  26  31056  217557  SWC  zs  -  -  swh wmw pkb dig kki swb  en  no  -  Mon Feb 4 10:45:06 CST 2013  ZAÏRE SWAHILI  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, G, Swahili (G.40).
swg  Swabian  -  swg  Germany  91  18211  118093  SWG  -  -  -  gsw pfl pdc sli de bar vmf lb ksh pdt nds cim li  en  no  -  Thu Oct 10 14:26:35 CDT 2013  SCHWÄBISCH, SUABIAN, SCHWAEBISCH  Indo-European, Germanic, West, High German, German, Upper German, Alemannic.
swh  Swahili  Kiswahili  swh  Tanzania  3  2196012  14043717  SWA  sw  sw  swa  wmw pkb dig kki swb tum kam loz nyf ki nym  en  yes  Jason Githeko, Alberto Escudero, Martin Benjamin  Thu Jan 31 10:23:01 CST 2013  KISWAHILI, KISUAHELI  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, G, Swahili (G.40).
swk  Malawi Sena  -  swk  Malawi  1  1545  10710  SWK  -  -  -  seh ny tum kki dig wmw sw  en  no  -  Thu Aug 8 15:20:35 CDT 2013  CISENA, CHISENA  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, N, Senga-Sena (N.40), Sena.
swn  Sawknah  -  swn  Libya  1  250  1845  SWN  -  -  -  stl nl  en  no  -  Mon Apr 15 16:11:49 CDT 2013  SOKNA  Afro-Asiatic, Berber, Eastern, Awjila-Sokna.
swn-x-foqaha  El-Foqaha  -  swn  Libya  1  225  1779  SWN  -  -  -  tmh auj  en  no  -  Mon Apr 15 16:44:06 CDT 2013  SOKNA  Afro-Asiatic, Berber, Eastern, Awjila-Sokna.
swp  Suau  -  swp  Papua New Guinea  363  300009  1775003  SWP  -  -  -  sbe wed meu kqf kud dob yml mwc rro ho  en  no  -  Fri Dec 28 22:01:31 CST 2012  IOU  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Nuclear, Suauic.
sxb  Suba  -  suh  Kenya  0  0  0  SUH  -  -  -  lg xog wmw nyn nyo pkb sw kki dig swh mer lu rw  en  no  -  -  -  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, E, Kuria (E.10).
sxn  Sangir  -  sxn  Indonesia (Sulawesi)  1  208407  1344272  SAN  -  -  -  jv pam lcm krj tl  en  no  -  Sun Dec 30 07:13:31 CST 2012  SANGIHÉ, SANGIRESE, SANGI, SANGIH  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Sulawesi, Sangir-Minahasan, Sangiric.
syr  Syriac  ܠܫܢܐ ܣܘܪܝܝܐ  syr  Iraq  0  0  0  -  -  -  -  -  en  no  -  -  -  Afro-Asiatic, Semitic, Central, Aramaic, Eastern, Central, Northeastern.
szl  Silesian  Ślůnsko godka  szl  Poland  3  243197  1750420  -  -  szl  -  wen hsb dsb hr pl  en  no  Grzegorz Kulik  Sat Jan 26 14:03:03 CST 2013  Szlonzokian  Indo-European, Slavic, West, Lechitic
ta  Tamil  தமிழ்  tam  India  1070  5632070  51134865  TCV  tl*  ta  tcv  bfq-Taml pi-Taml  en  yes  Yagna Kalyanaraman, Muguntharaj Subramanian, Pranava Swaroop Madhyastha, Elanjelian Venugopal  Thu Feb 7 20:27:35 CST 2013  TAMALSAN, TAMBUL, TAMILI, TAMAL, DAMULIAN  Dravidian, Southern, Tamil-Kannada, Tamil-Kodagu, Tamil-Malayalam, Tamil.
tab  Tabassaran  Табасаран  tab  Russian Federation  3  134967  989991  TAB  tbn  -  -  lez kum dar uzn av  en  no  -  Wed Sep 18 23:31:27 CDT 2013  TABASARAN, TABASARANTSY, GHUMGHUM  North Caucasian, Northeast, Lezgian.
tac  Western Tarahumara  -  tac  Mexico  3  373448  2534495  TAC  -  -  -  tar bon nak kjs xla  en es  no  -  Thu Dec 27 23:01:08 CST 2012  BAJA TARAHUMARA, RALÁMULI DE LA TARAHUMARA BAJA, ROCOROIBO TARAHUMARA  Uto-Aztecan, Southern Uto-Aztecan, Sonoran, Tarahumaran, Tarahumara.
taj  Eastern Tamang  तामाङ  taj  Nepal  2  169125  1187644  TAJ  -  -  taj  lif mai mr hne bh ne hi  en  no  -  Wed Sep 11 10:33:55 CDT 2013  -  Sino-Tibetan, Tibeto-Burman, Himalayish, Tibeto-Kanauri, Tibetic, Tamangic.
tar  Central Tarahumara  Rarámuri  tar  Mexico  2  322980  2209800  TAR  -  -  -  tac  en  no  -  Wed Sep 18 23:34:17 CDT 2013  CENTRAL TARAHUMARASAMACHIQUE TARAHUMARA  Uto-Aztecan, Southern Uto-Aztecan, Sonoran, Tarahumaran, Tarahumara.
tav  Tatuyo  -  tav  Colombia  2  290864  1823419  TAV  -  -  -  cbc bao  en es  no  -  Thu Dec 27 23:00:18 CST 2012  PAMOA, OA, TATUTAPUYO, JUNA  Tucanoan, Eastern Tucanoan, Central, Tatuyo.
tbc  Takia  -  tbc  Papua New Guinea  197  527546  2647661  TBC  -  -  -  ifk ifb ha pag bjn bik srb zsm id adz tmh itv  en  no  -  Mon Sep 23 10:42:04 CDT 2013  -  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Ngero-Vitiaz, Vitiaz, Bel, Nuclear Bel, Northern.
tbg  North Tairora  -  tbg  Papua New Guinea  632  709605  4884740  TBG  -  -  -  mcb not  en  no  -  Fri Dec 28 22:08:03 CST 2012  -  Trans-New Guinea, Main Section, Central and Western, East New Guinea Highlands, Eastern, Tairora.
tbg-x-arau  Tairora (Arau)  -  tbg  Papua New Guinea  0  0  0  TBG  -  -  -  tbg omw omw-x-aat omw-x-veq fj lch roo rug jmc lag  en  no  -  -  -  Trans-New Guinea, Main Section, Central and Western, East New Guinea Highlands, Eastern, Tairora.
tbl  Tboli  -  tbl  Philippines  0  0  0  TBL  -  -  -  stl nl fud nl-NL sdz din mbi act zsr  en  no  -  -  TIBOLI, T'BOLI, 'TAGABILI'  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, South Mindanao, Bilic, Tboli.
tbo  Tawala  -  tbo  Papua New Guinea  262  246609  1482431  TBO  -  -  -  gri  en  no  -  Fri Dec 28 22:15:58 CST 2012  TAWARA, TAVARA, TAVORA, TAVALA  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Nuclear, North Papuan Mainland-D'Entrecasteaux, Are-Taupota, Taupota.
tby  Tabaru  -  tby  Indonesia (Maluku)  4  216436  1400460  TBY  -  -  -  gbi loa alu luo stn sml  en  no  -  Tue Feb 19 12:24:33 CST 2013  TOBARU  West Papuan, North Halmahera, North, Tobaru.
tbz  Ditammari  -  tbz  Benin  3  699616  3896699  TBZ  -  -  tbz  nus rmy  en fr  no  -  Fri Jan 25 16:25:45 CST 2013  DITAMARI, TAMARI, SOMBA  Niger-Congo, Atlantic-Congo, Volta-Congo, North, Gur, Central, Northern, Oti-Volta, Eastern.
tca  Ticuna  -  tca  Peru  6  682456  3789667  TCA  -  -  tca  cax-x-ilv dww ksd snk gfk yml  en es  no  -  Thu Dec 27 23:01:33 CST 2012  TIKUNA, TUKUNA  Language Isolate.
tcc  Datooga  -  tcc  Tanzania  2  135321  1106904  TCC  -  -  -  ha iry gmv  en  no  -  Tue Feb 19 12:27:23 CST 2013  DATOGA, DATOG, TATOGA, TATOG, TATURU, 'MANGATI'  Nilo-Saharan, Eastern Sudanic, Nilotic, Southern, Tatoga.
tce  Southern Tutchone  -  tce  Canada  0  0  0  TCE  -  -  -  haa  en  no  -  -  -  Na-Dene, Nuclear Na-Dene, Athapaskan-Eyak, Athapaskan, Tutchone.
tcf  Malinaltepec Me’phaa  -  tcf  Mexico  1  7463  50876  TCF  tln  -  -  tpl mxb mig mpm mks bts son  en es  no  -  Thu Dec 27 23:03:20 CST 2012  Malinaltepec Tlapanec, Eastern Tlapanec, Mè’phàà Mañuwìín, Me’phaa, tlapaneco de Malinaltepec  Oto-Manguean, Subtiaba-Tlapanecan
tcs  Torres Strait Creole  Yumplatok  tcs  Australia  41  81817  400197  TCS  -  -  -  tpi gul rop jam hwc bi  en  no  -  Wed Sep 18 22:53:31 CDT 2013  TORRES STRAIT PIDGIN, TORRES STRAIT BROKEN, CAPE YORK CREOLE, LOCKHART CREOLE  Creole, English based, Pacific.
tcy  Tulu  ತುಳು  tcy  India  177  22139  157401  TCY  -  -  -  kn pi-Knda bfq  en  no  -  Mon Oct 14 10:43:48 CDT 2013  TAL, THALU, TILU, TULUVA BHASA, TULLU, THULU  Dravidian, Southern, Tulu.
tcz  Thado Chin  -  tcz  India  179  493431  2950236  TCZ  -  -  -  vap ctd bgr lus cnh pam jv ifu  en  no  -  Tue Sep 10 14:51:37 CDT 2013  THADOU, THADO-UBIPHEI, THADO-PAO, KUKI, KUKI-THADO, THAADOU KUKI  Sino-Tibetan, Tibeto-Burman, Kuki-Chin-Naga, Kuki-Chin, Northern.
te  Telugu  తెలుగు  tel  India  569  4701072  37219699  TCW  tu*  te  tcw*  pi-Telu  en  yes  Hariharan Ramamurthy  Fri Sep 13 14:05:32 CDT 2013  TELEGU, ANDHRA, GENTOO, TAILANGI, TELANGIRE, TELGI, TENGU, TERANGI, TOLANGAN  Dravidian, South-Central, Telugu.
tee  Huehuetla Tepehua  -  tee  Mexico  3  307782  2201196  TEE  -  -  -  tpt  en es  no  -  Thu Dec 27 23:07:43 CST 2012  HIDALGO TEPEHUA  Totonacan, Tepehua.
tem  Themne  -  tem  Sierra Leone  3  192307  891345  TEJ  -  -  tej  lia dag  en  no  -  Sat Jan 26 14:08:05 CST 2013  TEMNE, TIMNE, TIMENE, TIMMANNEE, TEMEN  Niger-Congo, Atlantic-Congo, Atlantic, Southern, Mel, Temne, Temne-Banta.
teo  Teso  Ateso  teo  Uganda  55  121114  891791  TEO  ie  -  -  gil  en  no  -  Fri Dec 28 12:38:59 CST 2012  ATESO, IKUMAMA, BAKEDI, BAKIDI, ETOSSIO, ELGUMI, WAMIA  Nilo-Saharan, Eastern Sudanic, Nilotic, Eastern, Lotuxo-Teso, Teso-Turkana, Teso.
ter  Terêna  -  ter  Brazil  1  229621  1712504  TEA  -  -  -  ilo  en  no  -  Thu Jan 10 08:39:15 CST 2013  TERENO, ETELENA  Arawakan, Maipuran, Southern Maipuran, Bolivia-Parana.
tet  Tetun  Tetun  tet  East Timor  280  1335413  8575720  TTM  ttp  tet  ttm  eu bjn pap-CW  en  yes  Peter Gossner  Wed Jan 30 21:47:32 CST 2013  TETUM, TETTUM, TETO, TETU, TETUNG, BELU, BELO, FEHAN, TETUN BELU  Austronesian, Malayo-Polynesian, Central-Eastern, Central Malayo-Polynesian, Timor, Nuclear Timor, East.
tew  Tewa  -  tew  USA  1  127574  935874  TEW  -  -  -  lkt  en  no  -  Thu Jan 10 09:03:22 CST 2013  -  Kiowa Tanoan, Tewa-Tiwa, Tewa.
tfr  Teribe  -  tfr  Panama  1  302302  1618445  TFR  -  -  -  agn hil tl  en  no  -  Thu Jan 10 09:04:31 CST 2013  TERRABA, TIRIBI, TIRRIBI, NORTENYO, QUEQUEXQUE, NASO  Chibchan, Talamanca.
tg  Tajiki  Тоҷикӣ  tgk  Tajikistan  2121  3933182  26095196  PET  tj  tg  pet  uz  en  no  Roger Kovacs  Tue Sep 10 16:04:45 CDT 2013  TADZHIK, TAJIKI PERSIAN, GALCHA  Indo-European, Indo-Iranian, Iranian, Western, Southwestern, Persian.
tgg  Tangga  -  tgg  Papua New Guinea  0  0  0  TGG  -  -  -  lcm mee stn kwf lbb kqw gfk nsn mna haw btx  en  no  -  -  TANGA  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, South New Ireland-Northwest Solomonic, Patpatar-Tolai.
tgp  Tangoa  -  tgp  Vanuatu  4  31181  162432  TGP  -  -  -  gri aia fj npy bnp  en  no  -  Sat Jan 26 14:10:12 CST 2013  SANTO  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, North and Central Vanuatu, Northeast Vanuatu-Banks Islands, West Santo.
tgx  Tagish  Tāgizi Dene  tgx  Canada  0  0  0  TGX  -  -  -  tce wam cut chp ru-Latn aon  en  no  -  -  -  Na-Dene, Nuclear Na-Dene, Athapaskan-Eyak, Athapaskan, Tahltan-Kaska.
th  Thai  ภาษาไทย  tha  Thailand  1160  3398756  63640195  THJ  si  th  thj  pww kxm  en  yes  -  Mon Feb 4 11:50:46 CST 2013  CENTRAL TAI, STANDARD THAI, THAIKLANG, SIAMESE  Tai-Kadai, Kam-Tai, Be-Tai, Tai-Sek, Tai, Southwestern, East Central, Chiang Saeng.
thk  Kitharaka  -  thk  Kenya  1  149764  1010746  THA  -  -  -  ki mer stn sw kam  en  no  -  Tue Feb 19 12:28:59 CST 2013  KITHARAKA, SARAKA, SHAROKA  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, E, Kikuyu-Kamba (E.20), Meru.
thp  Thompson  Nłeʔkepmxcin  thp  Canada  5  2664  16798  THP  -  -  -  shs mbb coo  en  no  -  Sat Jan 26 14:10:55 CST 2013  NTLAKAPMUK, NKLAPMX  Salishan, Interior Salish, Northern.
ti  Tigrigna  ትግርኛ  tir  Eritrea  1496  2198717  11539946  TGN  ti*  ti  tgn  am tig  en  yes  Biniam Gebremichael, Merhawie Woldezion  Wed Sep 11 10:37:10 CDT 2013  TIGRINYA, TIGRAY  Afro-Asiatic, Semitic, South, Ethiopian, North.
ti-Latn  Tigrigna (Latin)  -  tir  Ethiopia  2  4989  27546  TGN  -  -  -  am-Latn tet id eu  en  no  -  Sat Jan 26 14:52:46 CST 2013  TIGRINYA, TIGRAY  Afro-Asiatic, Semitic, South, Ethiopian, North.
tig  Tigré  ትግረ  tig  Eritrea  33  77211  359062  TIE  -  -  -  am ti har  en  no  Merhawie Woldezion  Mon Jan 13 16:39:13 CST 2014  KHASA, XASA  Afro-Asiatic, Semitic, South, Ethiopian, North.
tik  Tikar  -  tik  Cameroon  0  0  0  TIK  -  -  -  gaa bci sbd fon  en  no  -  -  TIKAR-EAST, TIKARI, TIKALI, NDOB, TINGKALA, NDOME  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Tikar.
tim  Timbe  -  tim  Papua New Guinea  0  0  0  TIM  -  -  -  spl kpf nij  en  no  -  -  -  Trans-New Guinea, Main Section, Central and Western, Huon-Finisterre, Huon, Western.
tiv  Tiv  Tiv  tiv  Nigeria  73  184942  914107  TIV  tv  -  tiv  nl snk  en  no  -  Thu Feb 7 20:35:37 CST 2013  'MUNSHI'  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Tivoid.
tiw  Tiwi  -  tiw  Australia  0  0  0  TIW  -  -  -  wbp ibd bvr wmt mpj  en  no  Aidan Wilson  -  -  Australian, Tiwian.
tk  Turkmen  Türkmençe  tuk  Turkmenistan  5149  7330086  57300198  TCK  tm  tk  tuk_latn  tr az crh kaa kk-Latn ky-Latn uz-Latn  en  yes  Gurban Mühemmet Tewekgeli, Jumamurat Bayjanov  Wed Jan 30 18:22:38 CST 2013  TURKOMANS, TURKMENLER, TURKMANIAN, TRUKHMEN, TRUKHMENY, TURKMANI  Altaic, Turkic, Southern, Turkmenian.
tk-Cyrl  Turkmen (Cyrillic)  -  tuk  Turkmenistan  219  186536  1397521  TCK  -  -  tck  kaa-Cyrl ky gag-Cyrl tt kum kk uz uzn tyv azj-Cyrl alt  en ru  no  -  Sun Sep 15 19:45:50 CDT 2013  TURKOMANS, TURKMENLER, TURKMANIAN, TRUKHMEN, TRUKHMENY, TURKMANI  Altaic, Turkic, Southern, Turkmenian.
tkl  Tokelauan  Faka-Tokelau  tkl  Tokelau  12  94397  464920  TOK  oe  -  -  tvl wls mi ty rar rap niu gil hla to fud sm  en  no  -  Wed Sep 18 23:37:16 CDT 2013  TOKELAU  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Central Pacific, East Fijian-Polynesian, Polynesian, Nuclear, Samoic-Outlier, Tokelauan.
tku  Upper Necaxa  -  tot  Mexico  0  0  0  -  -  -  -  top too tos nch nhw ncl nuz nah nhe  en  no  -  -  PATLA-CHICONTLA TOTONAC  Totonacan, Totonac.
tl  Tagalog  Tagalog  tgl  Philippines  44  1547372  9705375  TGL  tg  tl  tgl  ceb hil kyk pam krj agn jv msk bik jvn su jv-x-bms ban  en  yes  Ramil Sagum, Jan Michael C. Alonzo, Girard Aquino  Tue Sep 10 15:09:15 CDT 2013  FILIPINO, PILIPINO  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Meso Philippine, Central Philippine, Tagalog.
tl-Tglg  Tagalog (Tagalog)  -  tgl  Philippines  150  66003  507771  TGL  -  -  tgl_tglg  -  en  no  -  Thu Sep 19 09:57:56 CDT 2013  FILIPINO, PILIPINO  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Meso Philippine, Central Philippine, Tagalog.
tlb  Tobelo  -  tlb  Indonesia (Maluku)  1  201729  1334981  TLB  -  -  -  gbi tby loa bch zne hil krj akl bku  en  no  -  Tue Feb 19 12:36:19 CST 2013  -  West Papuan, North Halmahera, North, Tobelo.
tlf  Telefol  -  tlf  Papua New Guinea  0  0  0  TLF  -  -  -  fai bhl lcm dyo  en  no  -  -  TELEFOMIN, TELEFOLMIN, TELEEFOOL  Trans-New Guinea, Main Section, Central and Western, Central and South New Guinea-Kutubuan, Central and South New Guinea, Ok, Mountain.
tli  Tlingit  Lingít  tli  USA  8  18809  116828  TLI  -  -  -  son om dwr gwi kpe  en  started  -  Sat Jan 26 14:57:20 CST 2013  THLINGET, TLINKIT  Na-Dene, Nuclear Na-Dene, Tlingit.
tll  Tetela  Ɔtɛtɛla  tll  Dem. Rep. of Congo  105  155137  998505  TEL  ot  -  -  pem ng kj yaf sw ts kg wmw emk  en  no  -  Mon Dec 2 18:09:12 CST 2013  OTETELA, SUNGU  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Northwest, C, Tetela (C.80).
tly  Talysh  Tolyšə  tly  Azerbaijan  199  50012  332725  TLY  -  -  -  az gde kea yam pst-Latn fur wbl-Latn lij pbi  en  no  -  Mon Oct 14 11:02:45 CDT 2013  TALISH, TALESH, TALYSHI  Indo-European, Indo-Iranian, Iranian, Western, Northwestern, Talysh.
tmh  Tamashek  Tamasheq  tmh  Niger  3  754941  5358426  -  -  -  -  ha bjn mqb  en fr  no  -  Fri Jan 25 22:19:20 CST 2013  TAMASHEQ, TAMACHEK, TOMACHECK, TAMASHEKIN, TUAREG, TOUAREG, TOURAGE, AMAZIGH, TAHOUA, TEWELLEMET, TAHOUA TAMAJEQ  Afro-Asiatic, Berber, Tamasheq, Southern.
tn  Tswana  Setswana  tsn  Botswana  8239  9042492  50080375  TSW  tn  tn  tsw  nso st en  en  yes  Thapelo Otlogetswe, Sternly Simon, Dwayne Bailey, Friedel Wolff  Fri Sep 13 12:45:43 CDT 2013  CHUANA, COANA, CUANA, SETSWANA, SECHUANA, BEETJUANS, WESTERN SOTHO  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, S, Sotho-Tswana (S.30), Tswana.
tna  Tacana  -  tna  Bolivia  2  250974  1582124  TNA  -  -  -  aro ese  en es  no  -  Thu Dec 27 23:08:32 CST 2012  -  Tacanan, Araona-Tacana, Cavinena-Tacana, Tacana Proper.
to  Tongan  Faka-Tonga  ton  Tonga  109  499407  2703887  TOV  to  to  tov  niu tkl mi fud tvl wls haw  en  no  Tēvita O. Ka'ili, Brian Romanowski, Edwin Liava'a  Tue Sep 10 12:05:03 CDT 2013  TONGA  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Central Pacific, East Fijian-Polynesian, Polynesian, Tongic.
tob  Toba  Qom l’aqtac  tob  Argentina  7  18135  126475  TOB  tob  -  tob  ha rm ka-Latn  en  no  -  Tue Sep 10 15:15:28 CDT 2013  CHACO SUR, QOM, TOBA QOM  Mataco-Guaicuru, Guaicuruan.
toc  Coyutla Totonac  -  toc  Mexico  2  589615  2665093  TOC  -  -  -  qvw qxw tos top cbt inb  en es  no  -  Thu Dec 27 23:12:03 CST 2012  -  Totonacan, Totonac.
toi  Tonga  -  toi  Zambia  61  137108  1064670  TOI  cg  -  toi  bem loz xog lu kqn tum yao  en  no  -  Fri Sep 13 09:03:23 CDT 2013  CHITONGA, ZAMBEZI, PLATEAU TONGA  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, M, Lenje-Tonga (M.60), Tonga.
toj  Tojolabal  -  toj  Mexico  25  387571  2091964  TOJ  tjo  -  toj  tzt mxp fit mxq shp cbs smj se mpm  en es  no  Jameson Quinn  Tue Feb 5 21:41:55 CST 2013  CHAÑABAL, COMITECO  Mayan, Kanjobalan-Chujean, Chujean.
too  Xicotepec de Juárez Totonac  -  too  Mexico  2  233086  1957275  TOO  -  -  -  tot nah nch azz ncl nhw nhe ncj nuz ngu top tos  en es  no  -  Thu Dec 27 23:11:52 CST 2012  NORTHERN TOTONACA, VILLA JUÁREZ TOTONACA  Totonacan, Totonac.
top  Papantla Totonac  -  top  Mexico  3  324862  2265899  TOP  -  -  top  tos toc tot nhw zai nch mxb dag  en es  no  -  Wed Jan 30 20:59:55 CST 2013  LOWLAND TOTONACA  Totonacan, Totonac.
tos  Totonaca  Totonaco  tos  Mexico  2  348587  2407029  TOS  tot  -  -  top kek nhw dag art-x-tokipona toc mt ncl nch  en es  no  -  Fri Sep 13 11:33:23 CDT 2013  HIGHLAND TOTONACA, TOTONAC, TOTONACO  Totonacan, Totonac.
tot  Patla-Chicontla Totonac  -  tot  Mexico  2  327520  2826876  TOT  -  -  -  too top  en  no  -  Thu Jan 10 09:37:47 CST 2013  PATLA-CHICONTLA TOTONAC  Totonacan, Totonac.
tpa  Taupota  -  tpa  Papua New Guinea  0  0  0  TPA  -  -  -  tbo pwg bmk kud aui viv mwc gri kqf rro alu mpx dww  en  no  -  -  -  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Nuclear, North Papuan Mainland-D'Entrecasteaux, Are-Taupota, Taupota.
tpi  Tok Pisin  Tok Pisin  tpi  Papua New Guinea  224  1507172  7786593  PDG  mp  tpi  pdg  bi pis pam tcs lbb lcm tl agn bbc-Latn jvn kto mbh fil jv tgg  en  yes  Helge Søgaard, Craig Alan Volker  Mon Sep 23 10:41:56 CDT 2013  PISIN, PIDGIN, NEOMELANESIAN, NEW GUINEA PIDGIN ENGLISH, MELANESIAN ENGLISH  Creole, English based, Pacific.
tpl  Tlacoapa Me’phaa  -  tpl  Mexico  2  2376  15763  TPL  -  -  -  tcf  en es  no  -  Wed Sep 11 14:14:54 CDT 2013  Mi’phàà Minuíí Mi’pa, Tlacoapa Tlapanec, Tlapaneco de Tlacoapa  Oto-Manguean, Subtiaba-Tlapanecan
tpm  Tampulma  -  tpm  Ghana  3  893915  3975510  TAM  -  -  -  hag maw bwu dag yo gux swh  en  no  -  Tue Feb 19 12:50:05 CST 2013  TAMPRUSI, TAMPOLE, TAMPOLEM, TAMPOLENSE, TAMPLIMA, TAMPELE  Niger-Congo, Atlantic-Congo, Volta-Congo, North, Gur, Central, Southern, Grusi, Western.
tpn  Tupinambá  Tupi  tpn  Brazil  12  3061  21070  TPN  -  -  -  gun rar zne kwn gn tgp  en  no  -  Mon Oct 14 12:05:28 CDT 2013  OLD TUPÍ  Tupi, Tupi-Guarani, Tupi (III).
tpt  Tlachichilco Tepehua  -  tpt  Mexico  2  203488  1481501  TPT  -  -  -  tee ify mpm mbz ifu dag xtn  en  no  -  Fri Dec 28 08:26:19 CST 2012  -  Totonacan, Tepehua.
tpz  Tinputz  -  tpz  Papua New Guinea  0  0  0  TPZ  -  -  -  msm mbd sps ibl atd  en  no  -  -  VASUII, WASOI, TIMPUTS, VASUI  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Meso Melanesian, New Ireland, South New Ireland-Northwest Solomonic, Nehan-North Bougainville, Saposa-Tinputz.
tqo  Toaripi  -  tqo  Papua New Guinea  2  11677  67062  TPI  -  -  -  gn roo gui gil rmy tbg rom gnw mi  en  no  -  Tue Feb 5 21:38:00 CST 2013  MOTUMOTU, EAST ELEMA  Trans-New Guinea, Eleman, Eleman Proper, Eastern.
tr  Turkish  Türkçe  tur  Turkey  655  2908431  21539040  TRK  tk  tr  trk  crh tk gag azj kaa uz-Latn ha kmr  en  yes  -  Tue Sep 10 12:11:04 CDT 2013  TÜRKÇE, TÜRKISCH, ANATOLIAN  Altaic, Turkic, Southern, Turkish.
trc  Copala Triqui  -  trc  Mexico  5  416051  2263820  TRC  -  -  -  trq ncu mxb  en es  no  -  Fri Dec 28 08:41:44 CST 2012  SAN JUAN COPALA TRIQUE, TRIQUI  Oto-Manguean, Mixtecan, Trique.
trf  Trinidadian Creole English  -  trf  Trinidad and Tobago  7  25993  134848  TRF  -  -  -  en-SG en pcm sco osx hwc goh yol gul  en  no  Solange James  Tue Nov 27 11:39:33 CST 2012  -  Creole, English based, Atlantic, Eastern, Southern.
trn  Trinitario  -  trn  Bolivia  1  167601  1215859  TRN  -  -  -  luo msm mbd pmf ja-Latn ty  en  no  -  Tue Feb 19 12:36:28 CST 2013  MOXOS, MOJOS  Arawakan, Maipuran, Southern Maipuran, Bolivia-Parana.
trp  Kok Borok  Kokborok (Tripuri)  trp  India  2  20433  137530  TRP  -  -  -  bts ja-Latn grt  en  no  -  Wed Sep 18 23:39:47 CDT 2013  TRIPURI, TIPURA, USIPI MRUNG, TRIPURA, KAKBARAK, KOKBARAK  Sino-Tibetan, Tibeto-Burman, Jingpho-Konyak-Bodo, Konyak-Bodo-Garo, Bodo-Garo, Bodo.
trq  San Martín Itunyoso Triqui  -  trq  Mexico  7  385756  1904046  TRQ  -  -  -  mig ify yap mxb zaw zpa dag yo xtn trc cta  en es  no  -  Fri Dec 28 08:46:32 CST 2012  SAN MARTÍN ITUNYOSO TRIQUI, TRIQUI  Oto-Manguean, Mixtecan, Trique.
ts  Tsonga  Xitsonga  tso  South Africa  321  974115  5907094  TSO  ts  ts  tso  tsc sw  en  yes  Friedel Wolff, Dwayne Bailey  Tue Sep 10 16:03:21 CDT 2013  SHITSONGA, THONGA, TONGA, SHANGANA, SHANGAAN  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, S, Tswa-Ronga (S.50).
tsc  Tswa  Xitshwa  tsc  Mozambique  2  11698  65576  TSC  aw  -  -  ts loz lch  en  no  -  Sat Jan 26 15:21:05 CST 2013  SHITSHWA, KITSHWA, SHEETSHWA, XITSHWA, TSHWA  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, S, Tswa-Ronga (S.50).
tsd  Tsakonian  Τσακώνικα γρούσσα  tsd  Greece  2  849  4896  TSD  -  -  -  el pnt grc  en el  no  -  Wed Sep 18 23:42:22 CDT 2013  TSAKONIA  Indo-European, Greek, Doric.
tsg  Tausug  Bahasa Sūg  tsg  Philippines  18  3909  25498  TSG  -  -  -  bjn hnn bik bku war sml slm ms hil zsm id su  en  no  -  Sat Nov 16 17:40:38 CST 2013  TAW SUG, SULU, SULUK, TAUSOG, MORO JOLOANO  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Meso Philippine, Central Philippine, Bisayan, South, Butuan-Tausug.
tsw  Tsishingini  -  tsw  Nigeria  0  0  0  KAM  -  -  -  kdl mks otn mxb yal bzd bnp ha kqw snk  en  no  -  -  KAMBARI, KAMBERRI, KAMBERCHI, SALKA, ASHINGINI  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Kainji, Western, Kambari.
tsz  Purepecha  P'urhépecha  tsz  Mexico  168  398508  3221578  TSZ  trs  -  1112  lgg  en es  no  -  Wed Jan 9 14:27:55 CST 2013  Phorhépecha, Porhé, Tarascan, Tarasco  Tarascan.
tt  Tatar  Татарча  tat  Russian Federation  438  1724435  13166871  TTR  tat  tt  ttr  ba ky kaa-Cyrl azj-Cyrl uz kk  en ru  no  -  Tue Feb 5 18:52:03 CST 2013  TARTAR  Altaic, Turkic, Western, Uralian.
tta  Tutelo  Tutelo  tta  USA  1  1396  12893  TTA  -  -  -  swh  en  no  -  Mon Oct 1 20:14:45 CDT 2012  SAPONI  Siouan, Siouan Proper, Southeastern, Tutelo.
ttc  Tektiteko  -  ttc  Guatemala  2  230592  1358760  TTC  -  -  -  mam mms mvj mvc tzh  en  no  -  Tue Feb 19 13:12:53 CST 2013  TECO, TECTITÁN MAM  Mayan, Quichean-Mamean, Greater Mamean, Mamean.
tte  Bwanabwana  -  tte  Papua New Guinea  0  0  0  TTE  -  -  -  kud viv dob mpx sbe mwc aui pwg bmk kqf mox gri fj  en  no  -  -  TUBETUBE  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Nuclear, Suauic.
ttg  Tutong  Tutong  ttg  Brunei  246  125575  824654  TTG  -  -  -  bjn min id zsm jv-x-bms bik su hnn  en  no  -  Fri Sep 13 11:51:38 CDT 2013  TUTUNG  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Borneo, Northwest, North Sarawakan, Berawan-Lower Baram, Lower Baram, Central, B.
ttj  Tooro  -  ttj  Uganda  41  75769  600167  TTJ  rt  -  -  nyo nyn lg hay xog rw rn koo mho kwn nnb nym lu  en  no  -  Sat Sep 14 16:35:16 CDT 2013  RUTOORO, ORUTORO, RUTORO, TORO  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, J, Nyoro-Ganda (J.10).
tts  Northeastern Thai  ภาษาอีสาน  tts  Thailand  48  5298  71881  TTS  -  -  -  th nod pww kxm urk pi-Thai  en  no  -  Mon Oct 14 12:31:13 CDT 2013  ISAN, ISAAN, ISSAN  Tai-Kadai, Kam-Tai, Be-Tai, Tai-Sek, Tai, Southwestern, East Central, Lao-Phutai.
tuc  Mutu  -  tuc  Papua New Guinea  909  1079503  6222745  TUC  -  -  -  mna mbd msm el-Latn mvp atd ibl tpz  en  no  -  Tue Dec 3 10:56:56 CST 2013  TUAM-MUTU, TUAM, TUOM  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Ngero-Vitiaz, Ngero, Tuam.
tuc-x-oov  Mutu Oov  -  tuc  Papua New Guinea  0  0  0  TUC  -  -  -  tuc-x-tuam mna mbd msm el-Latn mvp atd ibl tpz  en  no  -  -  TUAM-MUTU, TUAM, TUOM  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Ngero-Vitiaz, Ngero, Tuam.
tuc-x-tuam  Mutu Tuam  -  tuc  Papua New Guinea  0  0  0  TUC  -  -  -  tuc-x-oov mna emi gfk tgg leu nsn  en  no  -  -  TUAM-MUTU, TUAM, TUOM  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Ngero-Vitiaz, Ngero, Tuam.
tuf  Central Tunebo  -  tuf  Colombia  2  281413  1683469  TUF  -  -  -  mio  en  no  -  Thu Jan 10 10:05:59 CST 2013  COBARÍA TUNEBO  Chibchan, Chibchan Proper, Tunebo.
tum  Tumbuka  chiTumbuka  tum  Malawi  7  108366  751118  TUW  tb  tum  -  ny swh wmw seh yao kki swc  en  no  -  Sat Jan 26 15:25:03 CST 2013  TUMBOKA, CHITUMBUKA, TAMBOKA, TAMBUKA, TIMBUKA, TOMBUCAS  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, N, Tumbuka (N.20).
tuo  Tucano  -  tuo  Brazil  3  500172  3180829  TUO  -  -  -  bao cbc gvc des yo gym yap pir fal  en  no  -  Fri Dec 28 09:01:11 CST 2012  TUKÁNA, TAKUNA, DAXSEA  Tucanoan, Eastern Tucanoan, Northern.
tuo-BR  Tucano (Brazil)  -  tuo  Brazil  0  0  0  TUO  -  -  -  tuo-CO  en  no  -  -  TUKÁNA, TAKUNA, DAXSEA  Tucanoan, Eastern Tucanoan, Northern.
tuo-CO  Tucano (Colombia)  -  tuo  Colombia  1  209143  1504443  TUO  -  -  -  cbc tuo-BR  en es  no  -  Fri Dec 28 09:23:50 CST 2012  TUKÁNA, TAKUNA, DAXSEA  Tucanoan, Eastern Tucanoan, Northern.
tvl  Tuvaluan  Tuvalu  tvl  Tuvalu  15  42529  215656  ELL  vl  -  -  tkl wls mi rar ty fud rap to niu gil mbt  en  no  -  Wed Sep 18 23:44:59 CDT 2013  ELLICE, ELLICEAN, TUVALU  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Central Pacific, East Fijian-Polynesian, Polynesian, Nuclear, Samoic-Outlier, Ellicean.
tw  Twi  Twi  twi  Ghana  229  432144  2269083  TWS  tw  tw  ass  fat srr kno ja-Latn biv bum iso bnp dgi  en  no  -  Wed Feb 6 20:32:36 CST 2013  -  Niger-Congo, Atlantic-Congo, Volta-Congo, Kwa, Nyo, Potou-Tano, Tano, Central, Akan.
twu  Termanu  -  twu  Indonesia (Nusa Tenggara)  5  236524  1360356  TWU  -  -  -  kwf gri alu ptu mlu fj lcm  en  no  -  Tue Feb 19 13:14:57 CST 2013  Central Rote, Pa’da, Rote, Rote Tengah, Roti, Rotinese  Austronesian, Malayo-Polynesian, Central-Eastern, Central Malayo-Polynesian, Timor, Extra-Ramelaic, West.
txu  Kayapó  -  txu  Brazil  1  397120  2079789  TXU  -  -  -  ram  en  no  -  Thu Jan 10 09:49:44 CST 2013  KOKRAIMORO  Macro-Ge, Ge-Kaingang, Ge, Northwest, Kayapo.
ty  Tahitian  Reo Tahiti  tah  French Polynesia  440  1527516  8061169  THT  th  ty  tht  rar rap mi tkl wls hla tvl gil sec tzh rmn rom mbt sm  en fr  no  Christin Livine  Mon Dec 2 14:09:34 CST 2013  -  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Central Pacific, East Fijian-Polynesian, Polynesian, Nuclear, East, Central, Tahitic.
tyv  Tuva  Тыва дыл  tyv  Russian Federation  14  247795  1869066  TUN  -  tyv  tyv  ky alt kaa-Cyrl tt kum kk gag-Cyrl uzn sah kjh khk bua xal  en ru  no  -  Fri Sep 13 22:10:45 CDT 2013  TUVA, TUVAN, TUVIA, TYVA, TOFA, TOKHA, SOYOT, SOYON, SOYOD, TANNU-TUVA, TUBA, TUVINIAN, URIANKHAI, URIANKHAI-MONCHAK, URYANKHAI, DIBA, KÖK MUNGAK  Altaic, Turkic, Northern.
tzc  Chamula Tzotzil  Bats’ik’op  tzc  Mexico  3  356529  2075041  TZC  tzo  -  tzc  tzz tzu tzs tze ilo cti sg tzh tzj arn  en es  no  Jameson Quinn  Thu Jan 31 10:27:12 CST 2013  CHAMULA  Mayan, Cholan-Tzeltalan, Tzeltalan.
tze  Chenalhó Tzotzil  -  tze  Mexico  5  584797  3587189  TZE  -  -  -  tzz tzc tzs  en es  no  -  Fri Dec 28 09:30:49 CST 2012  CHENALÓ  Mayan, Cholan-Tzeltalan, Tzeltalan.
tzh  Tzeltal  Bats'il k'op  tzh  Mexico  27  44087  264201  TZH  tze  -  tzc1  ty sec rap rar tkl mbs wls mbt tzo tzc  en es  no  -  Wed Dec 11 11:04:45 CST 2013  HIGHLAND TZELTAL, TENEJAPA, CHANAL, CANCUC, TENANGO  Mayan, Cholan-Tzeltalan, Tzeltalan.
tzj  Tz’utujil  Tz’utujil  tzj  Guatemala  1  1873  11417  TZJ  -  -  -  acc usp  en  no  Peter Rohloff, Cristy Sumoza  Wed Nov 7 16:38:46 CST 2012  TZUTUJIL ORIENTAL, SANTIAGO ATITLÁN TZUTUJIL, TZUTUHIL  Mayan, Quichean-Mamean, Greater Quichean, Quichean, Tzutujil.
tzj-x-eastern  Eastern Tz’utujil  -  tzj  Guatemala  3  242406  1485152  TZJ  -  -  -  tzt acc usp  en  no  Peter Rohloff, Cristy Sumoza  Fri Jan 25 22:28:59 CST 2013  TZUTUJIL ORIENTAL, SANTIAGO ATITLÁN TZUTUJIL, TZUTUHIL  Mayan, Quichean-Mamean, Greater Quichean, Quichean, Tzutujil.
tzm  Tamazight  -  tzm  Morocco  1192  2275828  14861394  TZM  -  -  tzm  kab tmh emk nl  en  no  -  Mon Jan 21 12:13:46 CST 2013  CENTRAL SHILHA, MIDDLE ATLAS BERBER, SHILHA  Afro-Asiatic, Berber, Northern, Atlas.
tzm-Tfng  Central Atlas Tamazight  ⵜⴰⵎⴰⵣⵉⵖⵜ  tzm  Morocco  435  174036  1084597  TZM  -  -  tzm_tfng  rif-Tfng shi-Tfng  en fr  yes  -  Wed Oct 9 21:42:09 CDT 2013  CENTRAL SHILHA, MIDDLE ATLAS BERBER, SHILHA  Afro-Asiatic, Berber, Northern, Atlas.
tzo  Tzotzil  Bats’i K’op  tzo  Mexico  359  1953680  12053337  -  tzo  -  tzc  cti tzh mt ilo sg tzj  en es  no  Jameson Quinn  Tue Sep 10 12:27:47 CDT 2013  CHAMULA  Mayan, Cholan-Tzeltalan, Tzeltalan.
tzs  San Andrés Larrainzar Tzotzil  -  tzs  Mexico  2  276378  1646088  TZS  -  -  -  tze tzz tzc  en es  no  -  Fri Dec 28 09:29:27 CST 2012  SAN ANDRÉS TZOTZIL  Mayan, Cholan-Tzeltalan, Tzeltalan.
tzt  Western Tz’utujil  -  tzt  Guatemala  0  0  0  TZT  -  -  -  tzj-x-eastern toj mxp acc  en  no  Peter Rohloff  -  -  Mayan, Quichean-Mamean, Greater Quichean, Quichean, Tzutujil.
tzu  Huixtán Tzotzil  -  tzu  Mexico  3  272834  1672698  TZU  -  -  -  tzz tzc ilo sg cti yo its  en  no  -  Thu Jan 10 22:36:41 CST 2013  HUIXTECO  Mayan, Cholan-Tzeltalan, Tzeltalan.
tzz  Zinacantán Tzotzil  -  tzz  Mexico  5  321798  1951582  TZZ  -  -  -  tze tzu tzc tzs  en  no  -  Sat Jan 26 15:30:07 CST 2013  ZINACANTECO TZOTZIL  Mayan, Cholan-Tzeltalan, Tzeltalan.
ubr  Ubir  -  ubr  Papua New Guinea  320  333291  1961430  UBR  -  -  -  mcd  en  no  -  Fri Dec 28 22:20:27 CST 2012  UBIRI, KUBIRI  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Nuclear, North Papuan Mainland-D'Entrecasteaux, Are-Taupota, Are.
ubu  Umbu-Ungu  -  ubu  Papua New Guinea  837  1213892  8339182  UMB  -  -  -  imo  en  no  -  Mon Feb 18 22:21:04 CST 2013  UBU UGU, KAUGEL, KAUIL, GAWIGL, GAWIL, KAKOLI  Trans-New Guinea, Main Section, Central and Western, East New Guinea Highlands, Central, Hagen, Kaugel.
ubu-x-andale  Umbu-Ungu Andale  -  ubu  Papua New Guinea  288  368414  2601226  UMB  -  -  -  ubu-x-kala ubu-x-nopenge imo  en  no  -  Mon Feb 18 21:54:29 CST 2013  UBU UGU, KAUGEL, KAUIL, GAWIGL, GAWIL, KAKOLI  Trans-New Guinea, Main Section, Central and Western, East New Guinea Highlands, Central, Hagen, Kaugel.
ubu-x-kala  Umbu-Ungu Kala  -  ubu  Papua New Guinea  288  483469  3349336  UMB  -  -  -  ubu-x-andale ubu-x-nopenge imo  en  no  -  Mon Feb 18 22:01:34 CST 2013  UBU UGU, KAUGEL, KAUIL, GAWIGL, GAWIL, KAKOLI  Trans-New Guinea, Main Section, Central and Western, East New Guinea Highlands, Central, Hagen, Kaugel.
ubu-x-nopenge  Umbu-Ungu No Penge  -  ubu  Papua New Guinea  261  362009  2388620  UMB  -  -  -  ubu-x-kala ubu-x-andale imo  en  no  -  Thu Sep 26 23:02:07 CDT 2013  UBU UGU, KAUGEL, KAUIL, GAWIGL, GAWIL, KAKOLI  Trans-New Guinea, Main Section, Central and Western, East New Guinea Highlands, Central, Hagen, Kaugel.
ude  Udihe  -  ude  Russian Federation  3  22757  168713  UDE  -  -  -  gld ulc eve neg uzn yux  en ru  no  -  Sun Feb 3 23:02:36 CST 2013  UDEKHE, UDEGEIS  Altaic, Tungus, Southern, Southeast, Udihe.
udi  Udi  Удин муз  udi  Azerbaijan  4  1107  7918  UDI  -  -  -  en  en  no  -  Mon Oct 14 12:46:10 CDT 2013  UDIN, UTI  North Caucasian, Northeast, Lezgian.
udm  Udmurt  Удмурт  udm  Russian Federation  1312  1033135  7478551  UDM  um*  udm  -  kpv koi mhr ru chm mrj ky bg uk sah mk myv sr nog cv  en ru  yes  Niko Partanen  Sun Nov 3 13:25:30 CST 2013  VOTIAK, VOTYAK  Uralic, Finno-Ugric, Finno-Permic, Permic.
udu  Uduk  -  udu  Ethiopia  1  283118  1382363  UDU  -  -  -  tgp  en  no  -  Sun Dec 30 09:18:47 CST 2012  TWAMPA, KWANIM PA, BURUN, KEBEIRKA, OTHAN, KORARA, KUMUS  Nilo-Saharan, Komuz, Koman.
ug  Uyghur  Уйғур  uig  China  488  859386  6690846  UIG  ug  ug  -  uz azj-Cyrl kaa-Cyrl ky tt  en  no  -  Tue Sep 10 14:18:53 CDT 2013  UIGHUR, UYGUR, UIGUR, UIGHUIR, UIGUIR, WEIWUER, WIGA  Altaic, Turkic, Eastern.
ug-Arab  Uyghur (Arabic)  -  uig  China  707  953287  7766877  UIG  -  -  uig  ckb glk az-Arab prs pes  en  no  -  Fri Sep 13 10:24:29 CDT 2013  UIGHUR, UYGUR, UIGUR, UIGHUIR, UIGUIR, WEIWUER, WIGA  Altaic, Turkic, Eastern.
ug-Latn  Uyghur (Latin)  -  uig  China  91  158766  1358076  UIG  -  -  uig_latn  uz-Latn kk-Latn kaa crh tr tk  en  no  -  Wed Jan 30 21:03:02 CST 2013  UIGHUR, UYGUR, UIGUR, UIGHUIR, UIGUIR, WEIWUER, WIGA  Altaic, Turkic, Eastern.
uk  Ukrainian  Українська  ukr  Ukraine  27510  38790718  294868548  UKR  k  uk  ukr  ru bg rue sr mk be cu  en  yes  -  Wed Sep 11 11:33:19 CDT 2013  -  Indo-European, Slavic, East.
uk-Latn  Ukrainian (Latin)  -  ukr  Ukraine  193  191837  1235367  UKR  -  -  -  sr-Latn-ME bs hr hbs sl sk mk-Latn bg-Latn cs ru-Latn be-Latn pl hsb  en  no  -  Mon Feb 4 10:36:09 CST 2013  -  Indo-European, Slavic, East.
ulc  Ulch  -  ulc  Russian Federation  0  0  0  ULC  -  -  -  gld neg ude  en  no  -  -  ULCHI, ULCHA, ULYCH, OLCH, OLCHA, OLCHIS, HOCHE, HOL-CHIH  Altaic, Tungus, Southern, Southeast, Nanaj.
umb  Umbundu  Umbundu  umb  Angola  286  518424  3388450  MNF  ub  -  mnf  nyk kj ng xog  en pt  no  -  Thu Feb 7 20:31:51 CST 2013  UMBUNDO, M'BUNDO, QUIMBUNDO, OVIMBUNDU, SOUTH MBUNDU, NANO, MBALI, MBARI, MBUNDU BENGUELLA  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, R, South Mbundu (R.10).
unm  Unami  Lënapei lixsëwakàn  unm  USA  28  2102  15506  DEL  -  -  -  en  en  no  -  Mon Oct 14 12:55:58 CDT 2013  DELAWARE, LENNI-LENAPE, LENAPE, TLA WILANO  Algic, Algonquian, Eastern.
ur  Urdu  ﺍﺭﺩﻭ  urd  Pakistan  1569  7903739  41363751  URD  ud*  ur  urd  pnb skr pes lki glk  en ar  yes  Ammar Kalimullah  Fri Sep 13 14:10:45 CDT 2013  -  Indo-European, Indo-Iranian, Indo-Aryan, Central zone, Western Hindi, Hindustani.
ur-Latn  Urdu (Latin)  -  urd  Pakistan  1  319  1657  URD  -  -  -  hns hi-Latn  en  started  -  Tue Sep 10 15:14:07 CDT 2013  -  Indo-European, Indo-Iranian, Indo-Aryan, Central zone, Western Hindi, Hindustani.
ura  Urarina  -  ura  Peru  3  284850  2310455  URA  -  -  ura  pls khz rro  en  no  -  Fri Dec 28 09:43:36 CST 2012  SHIMACU, SIMACU, ITUCALI  Unclassified.
urb  Kaapor  -  urb  Brazil  3  444243  2370852  URB  -  -  -  niu to  en pt  no  -  Thu Jan 10 10:24:45 CST 2013  -  Tupi, Tupi-Guarani, Oyampi (VIII).
urh  Urhobo  Urhobo  urh  Nigeria  2  8870  49124  URH  ur  -  -  iso bin ig  en  no  -  Fri Sep 13 15:37:37 CDT 2013  BIOTU, 'SOBO'  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Edoid, Southwestern.
urk  Urak Lawoi’  -  urk  Thailand  1  213410  1492792  URK  -  -  -  th kxm pww  en th  no  -  Tue Feb 19 13:45:43 CST 2013  ORAK LAWOI', LAWTA, CHAW TALAY, CHAWNAM, LAWOI  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Sundic, Malayic, Malayan, Para-Malay.
usa  Usarufa  -  usa  Papua New Guinea  282  226012  2012923  USA  -  -  -  pwg bdd  en  no  -  Fri Dec 28 22:25:08 CST 2012  USURUFA, UTURUPA  Trans-New Guinea, Main Section, Central and Western, East New Guinea Highlands, Eastern, Gadsup-Auyana-Awa.
usp  Uspanteko  -  usp  Guatemala  3  236738  1467755  USP  -  -  -  qut  en  no  -  Fri Jan 25 22:33:28 CST 2013  -  Mayan, Quichean-Mamean, Greater Quichean, Uspantec.
uun  Kulon-Pazeh  Pazih  uun  Taiwan  32  3930  24780  KNG  -  -  -  bjn ivv pwn mmn lus su lbb due hnn bnp ami slm jv bm sml  en  no  -  Mon Oct 14 13:11:59 CDT 2013  KULON  Austronesian, Formosan, Paiwanic.
uvl  Lote  -  uvl  Papua New Guinea  0  0  0  UVL  -  -  -  mee mbh mva mi stn rar  en  no  -  -  UVOL  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Ngero-Vitiaz, Vitiaz, Mengen.
uz  Uzbek  Ўзбек  uzb  Uzbekistan  27475  40893319  317163255  -  uz  uz  -  ky ug  en  yes  -  Fri Sep 13 16:16:31 CDT 2013  ÖZBEK  Altaic, Turkic, Eastern.
uz-Latn  Uzbek (Latin)  O'zbek (Lotincha)  uzb  Uzbekistan  17  439902  3815595  -  -  -  uzb  id zsm bjn jv-x-bms crh tr  en  no  -  Sat Sep 14 16:37:34 CDT 2013  ÖZBEK  Altaic, Turkic, Eastern.
uzn  Northern Uzbek  -  uzn  Uzbekistan  9497  16097916  122218061  UZB  uz  -  uzb1  ky ug  en  yes  -  Thu Jan 31 10:32:22 CST 2013  ÖZBEK  Altaic, Turkic, Eastern.
uzn-Latn  Northern Uzbek (Latin)  O'zbek  uzn  Uzbekistan  64  182836  1483724  UZB  -  -  uzb  id zsm bjn jv-x-bms crh tr  en  no  -  Sun Sep 15 21:59:50 CDT 2013  ÖZBEK  Altaic, Turkic, Eastern.
vag  Vagla  -  vag  Ghana  3  222245  1008611  VAG  -  -  -  mzw sil maw hag tpm cme  en  no  Jonathan Brindle  Tue Feb 19 13:41:34 CST 2013  VAGALA, SITI, SITIGO, KIRA, KONOSAROLA, PAXALA  Niger-Congo, Atlantic-Congo, Volta-Congo, North, Gur, Central, Southern, Grusi, Western.
vai  Vai  -  vai  Liberia  2  5807  17555  VAI  -  -  vai  -  en  no  -  Sun Sep 15 19:48:28 CDT 2013  VEI, VY, GALLINAS, GALLINES  Niger-Congo, Mande, Western, Central-Southwestern, Central, Manding-Jogo, Manding-Vai, Vai-Kono.
vap  Vaiphei  -  vap  India  117  690854  3873175  VAP  -  -  -  ctd tcz lus cnh bgr  en  no  -  Sat Jan 26 19:17:28 CST 2013  BHAIPEI, VAIPEI, VEIPHEI  Sino-Tibetan, Tibeto-Burman, Kuki-Chin-Naga, Kuki-Chin, Northern.
var  Huarijío  -  var  Mexico  17  193057  1648676  VAR  -  -  -  yaq  en  no  -  Thu Jan 10 10:12:52 CST 2013  GUARIJÍO, WARIHÍO, VARIHÍO  Uto-Aztecan, Southern Uto-Aztecan, Sonoran, Tarahumaran, Guarijio.
ve  Venda  Tshivenḓa  ven  South Africa  291  953275  5636716  VEN  ve  ve  tsh  swb chw dig nyf kck sw  en  yes  Friedel Wolff, Dwayne Bailey  Wed Feb 6 19:44:17 CST 2013  CHIVENDA  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, S, Venda (S.20).
vec  Venetian  Vèneto  vec  Italy  128  1333629  7516510  VEC  -  vec  vec  cbk ca-valencia lld-x-fas lij lmo lad oc an es  en it  no  Antonio Polo  Wed Jan 30 21:05:02 CST 2013  VENETO  Indo-European, Italic, Romance, Italo-Western, Western, Gallo-Iberian, Gallo-Romance, Gallo-Italian.
vep  Veps  Vepsän kel'  vep  Russian Federation  2  49940  390495  VEP  -  vep  vep  et  en  no  -  Wed Jan 30 21:08:31 CST 2013  VEPSIAN, 'CHUDY', 'CHUHARI', 'CHUKHARI'  Uralic, Finno-Ugric, Finno-Permic, Finno-Cheremisic, Finno-Mordvinic, Finno-Lappic, Baltic-Finnic.
vi  Vietnamese  Tiếng Việt  vie  Viet Nam  1766  5436599  27138122  VIE  vt  vi  vie  pam tl agn cdo jv jvn  en  yes  Hien Pham, Duy Nguyen, Clytie Siddall  Mon Feb 4 11:25:28 CST 2013  KINH, GIN, JING, CHING, VIET, ANNAMESE  Austro-Asiatic, Mon-Khmer, Viet-Muong, Vietnamese.
vif  Vili  TshiVili  vif  Congo  0  0  0  VIF  -  -  -  loz lua lch yaf  en  no  Paul David Humber  -  TSIVILI, CIVILI, FIOTE, FIOT  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, H, Kongo (H.10).
viv  Iduna  -  viv  Papua New Guinea  168  385264  3021032  VIV  -  -  -  kud dob tte aui yml mox pwg kqf tpa wed-x-topura mpx bdd bmk mwc sbe dww tbo gri mzz  en  no  -  Mon Sep 23 10:51:43 CDT 2013  VIVIGANA, VIVIGANI  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Nuclear, North Papuan Mainland-D'Entrecasteaux, Bwaidoga.
vkt  Tenggarong Kutai Malay  Kutai Tenggarong  vkt  Indonesia (Kalimantan)  12  5185  36891  VKT  -  -  -  id zsm bjn jv-x-bms su jv bew bsb iba nij  en  no  -  Sat Nov 16 17:23:00 CST 2013  KUTAI, TENGGARONG  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Sundic, Malayic, Malayan, Local Malay.
vls  Vlaams  West-Vlams  vls  Belgium  3  665218  3973608  VLS  -  vls  -  nds-NL zea li nl fy nds af lb de  en  no  -  Wed Sep 11 12:42:44 CDT 2013  FLAMAND, VLAEMSCH, WEST VLAAMS, WEST-VLOAMS  Indo-European, Germanic, West, Low Saxon-Low Franconian, Low Franconian.
vmf  Mainfränkisch  Oschdfräqgisch  vmf  Germany  67  26782  160052  VMF  -  -  -  pdc pfl gsw de bar ksh af li  en de  started  Bina Meusl  Wed Sep 18 23:50:11 CDT 2013  FRANCONIAN  Indo-European, Germanic, West, High German, German, Middle German, West Middle German, Moselle Franconian.
vmw  Makhuwa  Emakhuwa  vmw  Mozambique  3  43724  325032  VMW  mac  -  vmw  chw ngl dig loz swh nyf  en  no  -  Sat Jan 26 18:36:02 CST 2013  CENTRAL MAKHUWA, MAKHUWA-MAKHUWANA, MACUA, EMAKUA, MAKUA, MAKOANE, MAQUOUA, MAKHUWWA OF NAMPULA  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, P, Makua (P.30).
vmy  Ayautla Mazatec  -  vmy  Mexico  3  258025  1690455  VMY  -  -  -  maj mzi  en  no  -  Mon Dec 9 14:17:49 CST 2013  -  Oto-Manguean, Popolocan, Mazatecan.
vo  Volapük  Volapük  vol  -  851  10172730  62717588  -  -  vo  -  vep  en  no  -  Tue Jan 22 17:51:23 CST 2013  -  Artificial.
vot  Vod  Vađđa ceeli  vot  Russian Federation  104  17712  123592  VOD  -  -  -  fit fi ekk vro izh fkv toj se om  en  no  -  Thu Oct 17 23:17:13 CDT 2013  VOTIAN, VOTE, VODIAN, VOTISH, VOTIC  Uralic, Finno-Ugric, Finno-Permic, Finno-Cheremisic, Finno-Mordvinic, Finno-Lappic, Baltic-Finnic.
vro  Võro  Võro  vro  Estonia  328  567476  3819048  EST  -  fiu-vro  -  ekk fi fkv toj  en fi ekk  no  -  Sat Feb 2 21:00:38 CST 2013  -  Uralic, Finno-Ugric, Finno-Permic, Finno-Cheremisic, Finno-Mordvinic, Finno-Lappic, Baltic-Finnic.
vun  Vunjo  -  vun  Tanzania  2  137100  960755  VUN  -  -  -  old jmc swh kki wmw pkb ki swb  en  no  -  Tue Feb 19 13:39:57 CST 2013  KIVUNJO, WUNJO, KIWUNJO, MARANGU  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, E, Chaga (E.30).
wa  Walloon  Walon  wln  Belgium  19  798536  4359631  FRN  -  wa  frn1  fr fr-x-jer fr-x-nor pcd nov  en fr  yes  Pablo Saratxaga  Sun Sep 15 00:15:03 CDT 2013  FRANÇAIS  Indo-European, Italic, Romance, Italo-Western, Western, Gallo-Iberian, Gallo-Romance, Gallo-Rhaetian, Oïl, French.
waj  Waffa  -  waj  Papua New Guinea  0  0  0  WAJ  -  -  -  tbg-x-arau tbg omw-x-aat bmk omw-x-veq omw om pwg wal rai lag  en  no  -  -  -  Trans-New Guinea, Main Section, Central and Western, East New Guinea Highlands, Eastern, Tairora.
wal  Wolaytta  Wolayttattuwaa  wal  Ethiopia  59  640597  5386147  WBC  wl  -  -  gof dwr om gmv so lag son  en  no  Tewodros Abebe  Tue Dec 3 10:01:35 CST 2013  WELLAMO, WELAMO, WOLLAMO, WALLAMO, WALAMO, UALAMO, UOLLAMO, WOLAITTA, WOLAITA, WOLAYTA, WOLATAITA, BORODDA, UBA, OMETO  Afro-Asiatic, Omotic, North, Gonga-Gimojan, Gimojan, Ometo-Gimira, Ometo, Central.
wam  Wampanoag  -  wam  USA  11  236459  1880938  WAM  -  -  -  mwq nez ain  en  no  -  Sat Jan 26 19:01:42 CST 2013  MASSACHUSETT, MASSACHUSETTS, NATICK  Algic, Algonquian, Eastern.
wap  Wapishana  -  wap  Guyana  1  410978  2098200  WAP  -  -  -  ifk bik ifb bjn xtd bim  en  no  -  Wed Jan 30 08:50:49 CST 2013  WAPITXANA, WAPISIANA, VAPIDIANA, WAPIXANA  Arawakan, Maipuran, Northern Maipuran, Wapishanan.
war  Waray-Waray  Winaray  war  Philippines  393  1321926  8185717  WRY  sa  war  wry  itv akl bku hil bch bik krj wim abx ifk  en  no  Harvey Fiji, Voltaire Oyzon  Thu Feb 7 09:14:22 CST 2013  SAMAREÑO, SAMARAN, SAMAR-LEYTE, WARAY, BINISAYA  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Meso Philippine, Central Philippine, Bisayan, Central, Warayan, Samar-Waray.
way  Wayana  -  way  Suriname  2  146344  1169776  WAY  -  -  -  haw lcm twu  en  no  -  Tue Feb 19 14:32:03 CST 2013  OAYANA, WAJANA, UAIANA, OYANA, OIANA, ALUKUYANA, UPURUI, ROUCOUYENNE  Carib, Northern, East-West Guiana, Wayana-Trio.
wbl-Latn  Wakhi  x̌ik zik  wbl  Pakistan  2  414  2401  WBL  -  -  -  azj bim  en  no  -  Thu Sep 19 12:33:20 CDT 2013  WAKHANI, WAKHIGI, VAKHAN, KHIK  Indo-European, Indo-Iranian, Iranian, Eastern, Southeastern, Pamir.
wbp  Warlpiri  -  wbp  Australia  2  158027  1162379  WBP  -  -  -  ibd piu pjt bvr tiw wmt mpj  en  no  -  Fri Dec 28 17:16:42 CST 2012  WALBIRI, ELPIRA, ILPARA, WAILBRI, WALPIRI  Australian, Pama-Nyungan, South-West, Ngarga.
wca  Yanomámi  -  wca  Brazil  2  409948  1930653  WCA  -  -  -  gri fj twu pwg ki  en  no  -  Tue Feb 19 14:36:51 CST 2013  WAICÁ, WAIKÁ, YANOAM, YANOMAM, YANOMAMÉ, SURARA, XURIMA, PARAHURI  Yanomam.
wed  Wedau  -  wed  Papua New Guinea  0  0  0  WED  -  -  -  wed-x-topura tpa pwg bmk mwc ksd tbo khz snc kqf dww npy meu gri  en  no  -  -  WEDAUN, WEDAWAN  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Nuclear, North Papuan Mainland-D'Entrecasteaux, Are-Taupota, Taupota.
wed-x-topura  Topura  -  wed  Papua New Guinea  0  0  0  WED  -  -  -  tpa tbo pwg bmk aui kud gri viv mwc alu dww  en  no  -  -  WEDAUN, WEDAWAN  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Nuclear, North Papuan Mainland-D'Entrecasteaux, Are-Taupota, Taupota.
wen  Sorbian  -  wen  Germany  351  464003  3465931  -  -  -  -  szl hr sr-Latn bs sl cs pl sk mk-Latn  en  no  Edi Werner, Bernhard Baier  Sat Jan 26 16:18:46 CST 2013  -  Indo-European, Slavic, West, Sorbian.
wer  Weri  -  wer  Papua New Guinea  0  0  0  WER  -  -  -  msk itv zlm kyk sua mmn su bjn jv hil  en  no  -  -  WELI, WELE  Trans-New Guinea, Main Section, Eastern, Central and Southeastern, Goilalan, Kunimaipa.
wim  Wik-Mungkan  -  wim  Australia  280  373980  2799733  WIM  -  -  -  war bjn jv-x-bms itv su krj zsm msk id bku  en  no  -  Sat Jan 26 16:01:27 CST 2013  WIK-MUNKAN, MUNKAN  Australian, Pama-Nyungan, Paman, Middle Pama.
wiu  Wiru  -  wiu  Papua New Guinea  0  0  0  WIU  -  -  -  ipi bon ain soq ter ssx sny knv gah  en  no  -  -  WITU  Trans-New Guinea, Main Section, Central and Western, East New Guinea Highlands, Wiru.
wls  Wallisian  Faka’uvea  wls  Wallis and Futuna  65  158919  823097  WAL  wa  -  -  tkl tvl ty rap mi rar fud to gil niu  en fr  no  -  Wed Sep 18 23:52:46 CDT 2013  UVEAN, EAST UVEAN, WALLISIEN  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Central-Eastern Oceanic, Remote Oceanic, Central Pacific, East Fijian-Polynesian, Polynesian, Nuclear, Samoic-Outlier, East Uvean-Niuafo'ou.
wmt  Walmajarri  -  wmt  Australia  0  0  0  WMT  -  -  -  wbp ibd tiw pjt piu bvr mpj  en  no  -  -  WALMATJARI, WALMATJIRI, WALMAJIRI, WOLMERI  Australian, Pama-Nyungan, South-West, Ngumbin.
wmw  Mwani  -  wmw  Mozambique  2  137078  978723  WMW  -  -  -  swh swc tum nyf swb  en  no  -  Sun Dec 30 09:35:32 CST 2012  KIMWANI, MWANE, MUANE, QUIMUANE, IBO  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, G, Swahili (G.40).
wnc  Wantoat  -  wnc  Papua New Guinea  0  0  0  WNC  -  -  -  jv bch mee hil su krj itv pam kyk bjn msk mmn  en  no  -  -  -  Trans-New Guinea, Main Section, Central and Western, Huon-Finisterre, Finisterre, Wantoat.
wnu  Usan  -  wnu  Papua New Guinea  0  0  0  WNU  -  -  -  ubr iba na pam jv frr fy lb oc  en  no  -  -  WANUMA  Trans-New Guinea, Madang-Adelbert Range, Adelbert Range, Pihom-Isumrud-Mugil, Pihom, Numugenan.
wo  Wolof  Wolof  wol  Senegal  57  1209471  6171639  WOL  wo  wo  wol  mnk mur son  en fr  started  El Hadji Beye, Tel Monks  Sat Jan 26 16:18:41 CST 2013  OUOLOF, YALLOF, WALAF, VOLOF, WARO-WARO  Niger-Congo, Atlantic-Congo, Atlantic, Northern, Senegambian, Fula-Wolof, Wolof.
wob  Wè Northern  -  wob  Côte d’Ivoire  1  270086  1185712  WOB  -  -  -  ktj grb gbo biv  en  no  -  Tue Feb 19 14:22:39 CST 2013  WOBÉ, OUOBE, WÈÈ  Niger-Congo, Atlantic-Congo, Volta-Congo, Kru, Western, Wee, Wobe.
wos  Hanga Hundi  -  wos  Papua New Guinea  0  0  0  WOS  -  -  -  abt-x-wosera abt-x-maprik abt swh wmw swc pkb kg  en  no  -  -  KWASENGEN, WEST WOSERA  Sepik-Ramu, Sepik, Middle Sepik, Ndu.
wrh  Wiradhuri  -  wrh  Australia  1  567  5201  WRH  -  -  -  kld tiw ibd itv  en  no  Faith Baisden, Geoff Anderson  Tue Jan 29 09:17:16 CST 2013  WIRADJURI, BERREMBEEL, WARANDGERI, WEROGERY, WIIRATHERI, WIRA-ATHOREE, WIRADURI, WIRAJEREE, WIRASHURI, WIRATHERI, WIRRACHAREE, WIRAIDYURI, WIRRAI'YARRAI, WOORAGURIE, WORDJERG  Australian, Pama-Nyungan, Wiradhuric.
wrs  Waris  -  wrs  Papua New Guinea  0  0  0  WRS  -  -  -  mwc auy puu pwg kwn bmk ssd  en  no  -  -  WALSA  Trans-New Guinea, Northern, Border, Waris.
wsk  Waskia  -  wsk  Papua New Guinea  0  0  0  WSK  -  -  -  pam su jv sua rw hil bjn lcm  en  no  -  -  WOSKIA, VASKIA  Trans-New Guinea, Madang-Adelbert Range, Adelbert Range, Pihom-Isumrud-Mugil, Isumrud, Kowan.
wuu  Wu Chinese  吴語  wuu  China  1  25382  418073  WUU  -  wuu  -  gan ja cmn  en  no  -  Tue Jan 29 21:30:46 CST 2013  WU  Sino-Tibetan, Chinese.
wuv  Wuvulu-Aua  -  wuv  Papua New Guinea  0  0  0  WUV  -  -  -  wed alu wed-x-topura tpa pwg gri rro cme mwc meu bmk  en  no  -  -  AUA-VIWULU, VIWULU-AUA  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Admiralty Islands, Western.
wwa  Waama  -  wwa  Benin  1  1037  5152  WWA  -  -  ako  xsm ha hag tby gbi kea mk-Latn maw  en  no  -  Mon Dec 9 14:14:47 CST 2013  YOABU, YOABOU  Niger-Congo, Atlantic-Congo, Volta-Congo, North, Gur, Central, Northern, Oti-Volta, Eastern.
wya  Wyandot  -  wya  USA  1  56  686  WYA  -  -  -  eu  en  no  -  Sat Jan 26 16:18:31 CST 2013  WENDAT, WYENDAT, WYANDOTTE  Iroquoian, Northern Iroquoian, Huron.
wym  Wymysorys  Wymysöryś  wym  Poland  73  9853  62236  -  -  -  -  frr-x-fer lb kw  en  no  -  Thu Oct 17 23:21:35 CDT 2013  Wilamowicean  Indo-European, Germanic, West, High German, German, Middle German, East Middle German
xal  Kalmyk-Oirat  Къумукъ  xal  Russian Federation  17  196337  1238952  KGZ  klk*  xal  -  tyv ky khk alt kaa-Cyrl bxr tk-Cyrl uzn gag-Cyrl kum sah ru  en  no  Jargal Badagarov  Mon Sep 30 17:29:11 CDT 2013  KALMUK, KALMUCK, KALMACK, QALMAQ, KALMYTSKII JAZYK, KHAL:MAG, OIRAT, VOLGA OIRAT, EUROPEAN OIRAT, WESTERN MONGOLIAN  Altaic, Mongolian, Eastern, Oirat-Khalkha, Oirat-Kalmyk-Darkhat.
xav  Xavánte  -  xav  Brazil  1  483795  2558340  XAV  -  -  -  ty rap wmw sw  en  no  -  Thu Jan 10 10:12:59 CST 2013  AKUÊN, AKWEN, A'WE, CHAVANTE, SHAVANTE, CRISCA, PUSCITI, TAPACUA  Macro-Ge, Ge-Kaingang, Ge, Central, Acua.
xbi  Kombio  -  xbi  Papua New Guinea  351  234241  1444796  XBI  -  -  -  ar-Latn-x-chat ssg bm dmn-x-bamana  en  no  -  Tue Dec 3 10:24:26 CST 2013  Endangen  Torricelli, Kombio-Arapesh, Kombio.
xbi-x-wamp  Kombio Wampukuamp  -  xbi  Papua New Guinea  0  0  0  XBI  -  -  -  tgg bm ssg lcm dyu kus ar-Latn-x-chat fai kwf fj  en  no  -  -  Endangen  Torricelli, Kombio-Arapesh, Kombio.
xbi-x-yani  Kombio Yanimoi  -  xbi  Papua New Guinea  0  0  0  XBI  -  -  -  xbi-x-wamp ar-Latn-x-chat ssg bm  en  no  -  -  Endangen  Torricelli, Kombio-Arapesh, Kombio.
xcl  Classical Armenian  -  xcl  Armenia  2  673594  4102714  -  -  -  -  hy hy-x-ear  en hy  no  -  Sat Feb 16 07:45:13 CST 2013  HAIEREN, SOMKHURI, ENA, ERMENICE, ERMENI DILI, ARMJANSKI YAZYK  Indo-European, Armenian.
xcl-Latn  Classical Armenian (Latin)  -  xcl  Armenia  2  1332  8658  -  -  -  -  sbl  en  no  -  Fri Feb 15 20:39:33 CST 2013  HAIEREN, SOMKHURI, ENA, ERMENICE, ERMENI DILI, ARMJANSKI YAZYK  Indo-European, Armenian.
xh  Xhosa  isiXhosa  xho  South Africa  174  377824  3292802  XOS  xo  xh  xos  nd zu nr ss xog bem lg ng  en  yes  Dwayne Bailey, Friedel Wolff  Fri Sep 13 11:41:20 CDT 2013  ISIXHOSA, XOSA, KOOSA, 'KAFFER', 'KAFFIR', 'CAFFRE', 'CAFRE', 'CAUZUH'  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, S, Nguni (S.40).
xla  Kamula  -  xla  Papua New Guinea  0  0  0  KHM  -  -  -  ssx knv twu nak knv-x-fly bwu knv-x-ara  en  no  -  -  KAMURA, WAWOI  Trans-New Guinea, Main Section, Central and Western, Central and South New Guinea-Kutubuan, Central and South New Guinea, Awin-Pare.
xmf  Mingrelian  მარგალური  xmf  Georgia  370  2093317  16689583  XMF  -  xmf  -  ka  en  no  -  Sat Jan 26 17:36:34 CST 2013  MARGALURI, MEGREL, MEGRULI  South Caucasian, Zan.
xmv  Antankarana Malagasy  -  xmv  Madagascar  23  14411  109328  XMV  tnk  -  -  buc plt skg  en  no  -  Sat Feb 2 20:41:12 CST 2013  ANTANKARANA, TANKARANA  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Borneo, Barito, East, Malagasy.
xog  Soga  Lusoga  xog  Uganda  2  11554  84570  SOG  -  -  -  lg hay nyo ttj toi bem lu loz  en  no  Minah Nabirye, Gilles-Maurice de Schryver  Sat Jan 26 17:05:05 CST 2013  LUSOGA, OLUSOGA  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, J, Nyoro-Ganda (J.10).
xon  Konkomba  -  xon  Ghana  2  443210  2062226  KOS  -  -  -  bim gux myk bud tpm  en  no  -  Tue Feb 19 15:26:50 CST 2013  LIKPAKPALN, KPANKPAM, KOM KOMBA  Niger-Congo, Atlantic-Congo, Volta-Congo, North, Gur, Central, Northern, Oti-Volta, Gurma.
xon-x-liko  Likoonli Konkomba  -  xon  Ghana  1  221089  1028389  KOS  -  -  -  xon-x-likp bim gux myk bud tpm  en  no  -  Tue Feb 19 15:26:29 CST 2013  LIKPAKPALN, KPANKPAM, KOM KOMBA  Niger-Congo, Atlantic-Congo, Volta-Congo, North, Gur, Central, Northern, Oti-Volta, Gurma.
xon-x-likp  Likpakpaaln Konkomba  -  xon  Ghana  1  222121  1033837  KOS  -  -  -  xon-x-liko bim myk gux bud tpm  en  no  -  Tue Feb 19 15:26:37 CST 2013  LIKPAKPALN, KPANKPAM, KOM KOMBA  Niger-Congo, Atlantic-Congo, Volta-Congo, North, Gur, Central, Northern, Oti-Volta, Gurma.
xrb  Eastern Karaboro  -  xrb  Burkina Faso  1  285696  1197023  KAR  -  -  -  bwq myk man mnk  en  no  -  Tue Feb 19 14:43:00 CST 2013  KAR, KER, KLER  Niger-Congo, Atlantic-Congo, Volta-Congo, North, Gur, Senufo, Karaboro.
xsi  Sio  -  xsi  Papua New Guinea  0  0  0  SIO  -  -  -  mna ssd twu alu ssx stn mlu lcm rmy sda kwf ksd ain  en  no  -  -  SIGAWA  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, North New Guinea, Ngero-Vitiaz, Vitiaz, Sio.
xsm  Kasem  -  xsm  Burkina Faso  7  317699  1370414  KAS  -  -  kas  ln gri omq-x-amuzgo wwa amu biv cme knv-x-ara hag bng  en fr  no  -  Tue Oct 1 19:49:50 CDT 2013  KASSEM, KASIM, KASENA, KASSENA  Niger-Congo, Atlantic-Congo, Volta-Congo, North, Gur, Central, Southern, Grusi, Northern.
xtd  Diuxi-Tilantongo Mixtec  -  xtd  Mexico  2  294120  1722339  MIS  -  -  -  xtn mpm mxv wap miz mbz  en es  no  -  Fri Dec 28 09:48:46 CST 2012  CENTRAL NOCHISTLÁN MIXTECO, DIUXI MIXTEC  Oto-Manguean, Mixtecan, Mixtec-Cuicatec, Mixtec.
xtm  Magdalena Peñasco Mixtec  -  xtm  Mexico  0  0  0  QMP  -  -  -  xtn mpm dag maw bm  en  no  -  -  -  Oto-Manguean, Mixtecan, Mixtec-Cuicatec, Mixtec.
xtn  Northern Tlaxiaco Mixtec  -  xtn  Mexico  2  77049  354214  MOS  -  -  -  mpm mxv  en es  no  -  Fri Dec 28 09:46:52 CST 2012  NORTHERN TLAXIACO MIXTEC, SAN JUAN ÑUMÍ MIXTECO, ÑUMÍ MIXTECO  Oto-Manguean, Mixtecan, Mixtec-Cuicatec, Mixtec.
yaa  Yaminahua  -  yaa  Peru  2  274929  1837932  YAA  -  -  -  mcd apu shp stn ami miq ja-Latn mcb kzf snc khz  en es  no  -  Fri Dec 28 09:49:47 CST 2012  YAMINAWA, JAMINAWÁ, YUMINAHUA, YAMANAWA  Panoan, South-Central, Yaminahua-Sharanahua.
yad  Yagua  -  yad  Peru  3  215151  1840627  YAD  -  -  yad  omw-x-aat tbg omw  en  no  -  Fri Dec 28 09:52:12 CST 2012  YAHUA, LLAGUA, YAVA, YEGUA  Peba-Yaguan.
yaf  Yaka  -  yaf  Dem. Rep. of Congo  5  5580  33080  YAF  -  -  -  kng kcc lu lua  en  no  -  Fri Jan 25 16:47:03 CST 2013  KIYAKA, IAKA, IYAKA  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, H, Yaka (H.30).
yai  Yagnobi  яғнобӣ зивок  yai  Tajikistan  8  1379  8879  YAI  -  -  -  tg uz bg ude mk sr uk cv  en  no  -  Thu Oct 17 23:45:48 CDT 2013  YAGNOB  Indo-European, Indo-Iranian, Iranian, Eastern, Northeastern.
yal  Yalunka  -  yal  Guinea  1  202973  980151  YAL  -  -  -  sus snk kno agu bnp ha  en  no  -  Tue Feb 19 15:12:53 CST 2013  DJALLONKE, DYALONKE, DIALONKE, JALONKE, YALUNKE  Niger-Congo, Mande, Western, Central-Southwestern, Central, Susu-Yalunka.
yam  Yamba  -  yam  Cameroon  1  275567  1201232  YAM  -  -  -  nnw lee gde bav mda bfd pbi  en  no  -  Sun Dec 30 09:49:54 CST 2012  'KAKA', MBEM, MBUBEM, KAKAYAMBA, BEBAROE, BOENGA KO MUZOK, SWE'NGA  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Wide Grassfields, Narrow Grassfields, Mbam-Nkam, Nkambe.
yao  Yao  Ciyawo  yao  Malawi  3  34121  299148  YAO  ya  -  yao  tum kki toi swh swc ny  en  no  -  Fri Jan 25 16:48:44 CST 2013  CHIYAO, ACHAWA, ADSAWA, ADSOA, AJAWA, AYAWA, AYO, AYAO, DJAO, HAIAO, HIAO, HYAO, JAO, VEIAO, WAJAO  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, P, Yao (P.20).
yap  Yapese  Thin nu Waab  yap  Micronesia  2  17745  91926  YPS  yp  -  yps  ify luo  en  no  Keira Ballantyne  Fri Jan 25 16:49:47 CST 2013  -  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Yapese.
yaq  Yaqui  -  yaq  Mexico  3  267380  1802987  YAQ  -  -  -  mfy tee var zad cbi fai  en  no  -  Wed Sep 18 23:55:30 CDT 2013  -  Uto-Aztecan, Southern Uto-Aztecan, Sonoran, Cahita.
yby  Yaweyuha  -  yby  Papua New Guinea  267  458748  3281547  YBY  -  -  -  snp snp-x-lambau gah ng ino knv gdn kmu kki kng swh kg xla ipi  en  no  -  Mon Sep 23 10:55:11 CDT 2013  YABIYUFA, YAWIYUHA  Trans-New Guinea, Main Section, Central and Western, East New Guinea Highlands, East-Central, Siane.
ycn  Yucuna  -  ycn  Colombia  8  399843  2936075  YCN  -  -  -  nhg cav tav ese cke qvo qud  en es fr  no  -  Fri Dec 28 09:51:09 CST 2012  MATAPI, YUKUNA  Arawakan, Maipuran, Northern Maipuran, Inland.
ydd  Eastern Yiddish  -  ydd  Israel  1  1845  12333  YDD  -  -  ydd  he  en he  started  Raphael Finkel, Jordan Kutzik  Wed Jan 30 11:03:11 CST 2013  JUDEO-GERMAN, YIDDISH  Indo-European, Germanic, West, High German, Yiddish.
yi  Yiddish  ייִדיש  yid  Israel  1850  3760832  24026984  -  -  yi  -  he  en he  yes  Raphael Finkel, Jordan Kutzik  Fri Sep 13 10:24:33 CDT 2013  JUDEO-GERMAN, YIDDISH  Indo-European, Germanic, West, High German, Yiddish.
yi-Latn  Yiddish (Latin)  Yidish  yid  Israel  31  495742  3086959  -  -  -  -  pdc vmf vap lij ksh de nds  en  no  Jordan Kutzik  Sat Jan 26 17:12:51 CST 2013  JUDEO-GERMAN, YIDDISH  Indo-European, Germanic, West, High German, Yiddish.
ykg  Northern Yukaghir  -  ykg  Russian Federation  2  1102  10422  YKG  -  -  ykg  yux sah  en ru  no  -  Sat Jan 26 17:06:18 CST 2013  YUKAGIR, JUKAGIR, ODUL, TUNDRA, TUNDRE, NORTHERN YUKAGIR  Yukaghir.
yle  Yele  -  yle  Papua New Guinea  0  0  0  YLE  -  -  -  ajg xrb men rwo-x-karo spp bba son bas  en  no  -  -  YELEJONG, ROSSEL, YELA, YELETNYE  East Papuan, Yele-Solomons-New Britain, Yele-Solomons, Yele.
yli  Angguruk Yali  -  yli  Indonesia (Irian Jaya)  1  219875  1347604  YLI  -  -  -  nl frr bku  en  no  -  Tue Feb 19 14:43:08 CST 2013  NORTHERN YALI, ANGGURUK, YALIMO  Trans-New Guinea, Main Section, Central and Western, Dani-Kwerba, Southern, Ngalik-Nduga.
yml  Iamalele  -  yml  Papua New Guinea  0  0  0  YML  -  -  -  mox kqf dob viv kud mzz mwc aui pwg wed mpx  en  no  -  -  YAMALELE  Austronesian, Malayo-Polynesian, Central-Eastern, Eastern Malayo-Polynesian, Oceanic, Western Oceanic, Papuan Tip, Nuclear, North Papuan Mainland-D'Entrecasteaux, Bwaidoga.
yo  Yoruba  Yorùbá  yor  Nigeria  401  1451220  7840213  YOR  yr  yo  yor  its hag sg tzu ilo dag maw gux cko mpm  en  started  Tope Faro, Tunde Adegbola, Àyọ Akande  Sat Feb 2 20:41:56 CST 2013  YOOBA, YARIBA, YORÙBÁ  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Defoid, Yoruboid, Edekiri.
yol  Yola  -  yol  -  1  673  3696  -  -  -  -  frr-x-fer sco en-GB ga-Latg kw  en  no  -  Sat Feb 16 08:41:09 CST 2013  -  -
yon  Yongkom  -  yon  Papua New Guinea  0  0  0  YON  -  -  -  din ain izr ifk dip kcc snk srb  en  no  -  -  YONGOM, YONGGOM  Trans-New Guinea, Main Section, Central and Western, Central and South New Guinea-Kutubuan, Central and South New Guinea, Ok, Lowland.
yrb  Yareba  -  yrb  Papua New Guinea  0  0  0  YRB  -  -  -  aby sue mwc wed bmk pwg dww tpa wed-x-topura aui soq snc  en  no  -  -  MIDDLE MUSA  Trans-New Guinea, Main Section, Eastern, Central and Southeastern, Yareban.
yrk  Nenets  ненэцяʼ вада  yrk  Russian Federation  0  0  0  YRK  -  -  -  bg mk sr ru be hbs-Cyrl uk  en  no  -  -  NENEC, NENTSE, NENETSY, YURAK, YURAK SAMOYED  Uralic, Samoyedic, Northern Samoyedic.
yrl  Nhengatu  Nheengatu  yrl  Brazil  2  279  2055  YRL  -  -  -  swh mti ain wmw kue kwn  en  no  -  Fri Oct 18 00:03:26 CDT 2013  YERAL, GERAL, LÍNGUA GERAL, NYENGATÚ, NHEENGATU, NYENGATO, ÑEEGATÚ, WAENGATU, COASTAL TUPIAN, MODERN TUPÍ  Tupi, Tupi-Guarani, Tupi (III).
yss  Yessan-Mayo  -  yss  Papua New Guinea  575  610566  3493712  YSS  -  -  -  mbi bon mbt wiu efi aer bin ibb sny nen ti-Latn  en  no  -  Tue Dec 3 10:41:38 CST 2013  MAYO-YESAN, MAIO-YESAN, YASYIN, YESAN  Sepik-Ramu, Sepik, Tama.
yss-x-yamano  Yessan-Mayo (Yamano)  -  yss  Papua New Guinea  0  0  0  YSS  -  -  -  mbi nen mbt wiu bon ckk cbm  en  no  -  -  MAYO-YESAN, MAIO-YESAN, YASYIN, YESAN  Sepik-Ramu, Sepik, Tama.
yss-x-yawu  Yessan-Mayo (Yawu)  -  yss  Papua New Guinea  0  0  0  YSS  -  -  -  yss-x-yamano mbi bon mbt wiu efi aer bin ibb sny  en  no  -  -  MAYO-YESAN, MAIO-YESAN, YASYIN, YESAN  Sepik-Ramu, Sepik, Tama.
yua  Yucatec Maya  Màaya T'àan  yua  Mexico  124  272950  1719442  YUA  may  -  yua  kjb ixi hva mop chf  en es  no  Jameson Quinn  Wed Sep 18 23:58:04 CDT 2013  PENINSULAR MAYA, YUCATECO MAYAN  Mayan, Yucatecan, Yucatec-Lacandon.
yuc  Yuchi  yUdjEha  yuc  USA  2  124  940  YUC  -  -  -  gn  en  no  -  Thu Jan 10 18:28:35 CST 2013  UCHEAN, Euchee  Language Isolate.
yue  Yue Chinese  粵語  yue  China  2  1151045  5885058  YUH  -  zh-yue  -  gan wuu ja cmn  en  no  -  Tue Jan 29 22:56:48 CST 2013  YUET YUE, GWONG DUNG WAA, CANTONESE, YUE, YUEH, YUEYU, BAIHUA  Sino-Tibetan, Chinese.
yue-Hans  Yue Chinese (Simplified)  -  yue  China  1  1052327  2104716  YUH  -  -  -  yue gan wuu cmn  en  no  -  Tue Jan 29 22:02:07 CST 2013  YUET YUE, GWONG DUNG WAA, CANTONESE, YUE, YUEH, YUEYU, BAIHUA  Sino-Tibetan, Chinese.
yuj  Karkar-Yuri  -  yuj  Papua New Guinea  0  0  0  YUJ  -  -  -  gil mi dgz bbr car ain  en  no  -  -  YURI, KARKAR  Language Isolate.
yut  Yopno  -  yut  Papua New Guinea  0  0  0  YUT  -  -  -  ha krl adz tbc nif iry ifk kmh-x-mini hwc naf  en  no  -  -  YUPNA  Trans-New Guinea, Main Section, Central and Western, Huon-Finisterre, Finisterre, Yupna.
yuw  Yau  -  yuw  Papua New Guinea  0  0  0  YUW  -  -  -  bbc-Latn jvn bts mog agn ded pam kyk tl jv trp  en  no  -  -  URUWA  Trans-New Guinea, Main Section, Central and Western, Huon-Finisterre, Finisterre, Uruwa.
yux  Southern Yukaghir  Одул  yux  Russian Federation  4  2883  22684  YUX  -  -  -  ykg bxr ude gld ulc sah evn neg eve bua  en ru  no  -  Thu Sep 19 00:01:02 CDT 2013  YUKAGIR, JUKAGIR, ODUL, KOLYMA, KOLYM, SOUTHERN YUKAGIR  Yukaghir.
yuz  Yuracare  -  yuz  Bolivia  1  131505  1207070  YUE  -  -  -  qvo tzo quh qxh tzc  en  no  -  Tue Feb 19 15:55:31 CST 2013  YURA  Language Isolate.
yva  Yawa  -  yva  Indonesia (Irian Jaya)  0  0  0  YVA  -  -  -  ksd mnb agd soq gdn ndc sue stn wmw sn  en  no  -  -  YAPANANI, MORA, TURU, MANTEMBU, YAVA, IAU  Geelvink Bay, Yawa.
za  Zhuang  Vahcuengh  zha  China  5  42535  318085  -  -  za  ccx  sas  en  no  Mark Williamson  Sat Jan 26 17:07:46 CST 2013  CHUANG, TAI CHUANG, VAH CUENGH, CANGVA  Tai-Kadai, Kam-Tai, Be-Tai, Tai-Sek, Tai, Northern.
zaa  Sierra de Juárez Zapotec  -  zaa  Mexico  2  280866  1562807  ZAA  -  -  -  zai zaq  en es  no  -  Fri Dec 28 09:53:35 CST 2012  ATEPEC ZAPOTECO, IXTLÁN ZAPOTECO  Oto-Manguean, Zapotecan, Zapotec.
zab  San Juan Guelavía Zapotec  -  zab  Mexico  0  0  0  ZAB  -  -  -  zai zpa zaw zpf  en  no  -  -  WESTERN TLACOLULA ZAPOTECO, GUELAVÍA ZAPOTEC  Oto-Manguean, Zapotecan, Zapotec.
zac  Ocotlán Zapotec  -  zac  Mexico  2  306589  1782533  ZAC  -  -  -  sq aat als aae zai aln ote zpa  en es  no  -  Fri Dec 28 10:03:13 CST 2012  WESTERN OCOTLÁN ZAPOTEC, OCOTLÁN ZAPOTEC, CENTRAL OCOTLÁN ZAPOTECO  Oto-Manguean, Zapotecan, Zapotec.
zad  Cajonos Zapotec  -  zad  Mexico  3  259982  1662584  ZAD  -  -  -  zty zpq  en es  no  -  Fri Dec 28 10:01:13 CST 2012  SAN PEDRO CAJONOS ZAPOTECO, SOUTHERN VILLA ALTA ZAPOTECO, CAJONOS ZAPOTEC  Oto-Manguean, Zapotecan, Zapotec.
zae  Yareni Zapotec  -  zae  Mexico  3  7144  41926  ZAE  -  -  -  zaq  en es  no  -  Fri Dec 28 10:14:15 CST 2012  WESTERN IXTLÁN ZAPOTECO, TEOCOCUILCO DE MARCOS PÉREZ ZAPOTECO, SANTA ANA YARENI, ETLA ZAPOTEC  Oto-Manguean, Zapotecan, Zapotec.
zai  Isthmus Zapotec  diidxazá  zai  Mexico  69  400344  2303703  ZAI  zpi  -  -  zab zpa zaw zaq zaa zat dag zpf maw scn  en es  no  -  Thu Sep 19 00:03:44 CDT 2013  ZAPOTECO, ÍSTMO  Oto-Manguean, Zapotecan, Zapotec.
zam  Miahuatlán Zapotec  -  zam  Mexico  6  510768  2643790  ZAM  -  -  zam  zao azg zpt ogo zpu zpi  en es  no  -  Wed Jan 30 21:10:28 CST 2013  CENTRAL MIAHUATLÁN ZAPOTEC  Oto-Manguean, Zapotecan, Zapotec.
zao  Ozolotepec Zapotec  -  zao  Mexico  2  341754  1727345  ZAO  -  -  -  zpm zpi zpo yon  en  no  -  Fri Dec 28 10:19:16 CST 2012  -  Oto-Manguean, Zapotecan, Zapotec.
zap  Zapoteco  Diidxazá  zap  Mexico  8  148069  738720  -  zpi  -  -  myk nfr  en es  no  -  Tue Sep 10 12:05:44 CDT 2013  ZAPOTECO  Oto-Manguean, Zapotecan, Zapotec.
zaq  Aloápam Zapotec  -  zaq  Mexico  4  74037  410230  ZAQ  -  -  -  zaa zae  en es  no  -  Fri Dec 28 10:18:47 CST 2012  ALOÁPAM ZAPOTEC  Oto-Manguean, Zapotecan, Zapotec.
zar  Rincón Zapotec  -  zar  Mexico  3  321338  2024647  ZAR  -  -  -  zsr  en es  no  -  Fri Dec 28 10:21:52 CST 2012  RINCÓN ZAPOTEC, YAGALLO ZAPOTECO, NORTHERN VILLA ALTA ZAPOTECO  Oto-Manguean, Zapotecan, Zapotec.
zas  Santo Domingo Albarradas Zapotec  -  zas  Mexico  2  284599  1700269  ZAS  -  -  -  zaw cbm ckk tbc  en es  no  -  Fri Dec 28 10:27:35 CST 2012  ALBARRADAS ZAPOTEC  Oto-Manguean, Zapotecan, Zapotec.
zat  Tabaa Zapotec  -  zat  Mexico  0  0  0  ZAT  -  -  -  zpq zai rm bg-Latn tob lld quj  en es  no  -  -  CENTRAL VILLA ALTA ZAPOTECO, TABAA ZAPOTECO, TABÁ ZAPOTEC  Oto-Manguean, Zapotecan, Zapotec.
zav  Yatzachi Zapotec  -  zav  Mexico  2  241335  1636171  ZAV  -  -  -  zad zpu zpq zpc zpt cnl ctp mop zty  en es  no  -  Fri Dec 28 22:25:41 CST 2012  YATZACHI ZAPOTEC, VILLA ALTA ZAPOTECO  Oto-Manguean, Zapotecan, Zapotec.
zaw  Mitla Zapotec  -  zaw  Mexico  2  233460  1584174  ZAW  -  -  -  zpa zai zpf zab dag zas xtn trq lgg gux  en  no  -  Fri Dec 28 10:28:34 CST 2012  EAST CENTRAL TLACOLULA ZAPOTECO, EAST VALLEY ZAPOTECO  Oto-Manguean, Zapotecan, Zapotec.
zca  Coatecas Altas Zapotec  -  zca  Mexico  0  0  0  ZAP  -  -  -  zad zpu zpo zpi zav zam  en es  no  -  -  SAN JUAN COATECAS ALTAS ZAPOTEC  Oto-Manguean, Zapotecan, Zapotec.
zea  Zeeuws  Zeêuws  zea  Netherlands  3  41037  252270  ZEA  -  zea  -  nds-NL vls nl li fy nds de lb af da  en  no  -  Sat Jan 26 18:30:01 CST 2013  ZEAWS, ZEALANDIC, ZEÊUWS  Indo-European, Germanic, West, Low Saxon-Low Franconian, Low Franconian
zh  Chinese  中文  zho  China  427  267205  2442890  -  chs  -  -  zh-Hant ja  en  no  -  Wed Sep 11 12:05:22 CDT 2013  -  Sino-Tibetan, Chinese.
zh-Hant  Chinese (Traditional)  繁體中文  zho  China  19  17280  383037  -  chs  -  -  zh ja  en  no  -  Wed Sep 11 12:11:00 CDT 2013  -  Sino-Tibetan, Chinese.
zh-Latn  Chinese (Latin script)  -  zho  China  89  565892  2927592  -  -  -  -  an ca-valencia vi  en  no  -  Sat Jan 26 19:17:35 CST 2013  Beifang Fangyan, Guanhua, Guoyu, Hanyu, Mandarin, Northern Chinese, Putonghua, Standard Chinese  Sino-Tibetan, Chinese
zia  Zia  -  zia  Papua New Guinea  0  0  0  ZIA  -  -  -  sue dob tte sbe aui pwg bmk fj  en  no  -  -  TSIA, LOWER WARIA, ZIYA  Trans-New Guinea, Main Section, Eastern, Binanderean, Binanderean Proper.
zlm  Sarawak Malay  -  zlm  Malaysia (Peninsular)  397  888334  5484066  MLI  -  -  -  bjn id zsm jv-x-bms min su iba  en  no  Suhaila Saee  Sat Jan 26 19:17:20 CST 2013  BAHASA MALAYSIA, BAHASA MALAYU, MALAYU, MELAJU, MELAYU, STANDARD MALAY  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Sundic, Malayic, Malayan, Local Malay.
znd  Zande  Pa-Zande  znd  Dem. Rep. of Congo  2  27095  148327  ZAN  zn  -  -  akl kwn  en  no  -  Sat Jan 26 18:57:24 CST 2013  PAZANDE, ZANDI, AZANDE, SANDE, ASANDE, BADJANDE, BAZENDA  Niger-Congo, Atlantic-Congo, Volta-Congo, North, Adamawa-Ubangi, Ubangi, Zande, Zande-Nzakara.
zne  Zande  Pa-Zande  zne  Dem. Rep. of Congo  5  27843  152675  ZAN  zn  -  -  akl rw kwn  en  no  -  Sat Feb 2 20:30:04 CST 2013  PAZANDE, ZANDI, AZANDE, SANDE, ASANDE, BADJANDE, BAZENDA  Niger-Congo, Atlantic-Congo, Volta-Congo, North, Adamawa-Ubangi, Ubangi, Zande, Zande-Nzakara.
zom  Zo  -  zom  Myanmar  2  1978  10483  ZOM  -  -  -  ctd vap tcz lus hlt cnk dln cnh mwq cfm bgr  en  no  -  Sat Nov 16 16:52:34 CST 2013  ZORNI, ZOMI, ZOU, ZO, KUKI CHIN  Sino-Tibetan, Tibeto-Burman, Kuki-Chin-Naga, Kuki-Chin, Northern.
zos  Francisco León Zoque  -  zos  Mexico  2  259883  1823257  ZOS  -  -  -  es-x-cant es cav nhg cti es-GT fax  en es  no  -  Fri Dec 28 10:32:02 CST 2012  SANTA MAGDALENA ZOQUE  Mixe-Zoque, Zoque, Chiapas Zoque.
zpa  Lachiguiri Zapotec  Diitza  zpa  Mexico  2  3448  21628  ZPA  zpl  -  -  zai zaw ja-Latn zab  en es  no  -  Wed Nov 7 14:27:48 CST 2012  NORTHWESTERN TEHUANTEPEC ZAPOTECO, SANTIAGO LACHIGUIRI ZAPOTECO, LACHIGUIRI ZAPOTEC  Oto-Manguean, Zapotecan, Zapotec.
zpc  Choapan Zapotec  -  zpc  Mexico  2  289527  1868559  ZPC  -  -  -  zav zpu zad zaa cnl zpl zaq zai  en es  no  -  Fri Dec 28 10:32:12 CST 2012  CHOAPAN ZAPOTEC, CHOÁPAM ZAPOTECO  Oto-Manguean, Zapotecan, Zapotec.
zpf  San Pedro Quiatoni Zapotec  -  zpf  Mexico  1  6249  31562  ZPF  -  -  -  zaw zab myk  en es  no  -  Thu Jan 10 10:35:26 CST 2013  SAN PEDRO QUIATONI ZAPOTEC, QUIATONI ZAPOTECO, EASTERN TLACOLULA ZAPOTECO  Oto-Manguean, Zapotecan, Zapotec.
zpi  Santa María Quiegolani Zapotec  -  zpi  Mexico  2  331607  1737142  ZPI  -  -  -  mbi zpm nds-NL zao gba nl act fy sdz li  en es  no  -  Fri Dec 28 10:32:47 CST 2012  SANTA MARÍA QUIEGOLANI ZAPOTEC, QUIEGOLANI ZAPOTEC, WESTERN YAUTEPEC ZAPOTECO  Oto-Manguean, Zapotecan, Zapotec.
zpl  Lachixío Zapotec  -  zpl  Mexico  2  327803  1950282  ZPL  -  -  -  zaq zaa zpc zpz zae cta zai scn jbo  en es  no  -  Fri Dec 28 10:32:17 CST 2012  EASTERN SOLA DE VEGA ZAPOTEC, SOLA DE VEGA ESTE ZAPOTECO  Oto-Manguean, Zapotecan, Zapotec.
zpm  Mixtepec Zapotec  -  zpm  Mexico  2  257719  1341080  ZPM  -  -  -  zao  en es  no  -  Fri Dec 28 10:37:16 CST 2012  EASTERN MIAHUATLÁN ZAPOTECO, SAN JUAN MIXTEPEC ZAPOTECO, MIXTEPEC ZAPOTEC  Oto-Manguean, Zapotecan, Zapotec.
zpo  Amatlán Zapotec  -  zpo  Mexico  3  361314  1761962  ZPO  -  -  -  ztq zao om  en es  no  -  Fri Dec 28 10:37:19 CST 2012  NORTHEASTERN MIAHUATLÁN, SAN FRANCISCO LOGUECHE ZAPOTECO, SAN CRISTÓBAL AMATLÁN ZAPOTECO, AMATLÁN ZAPOTEC  Oto-Manguean, Zapotecan, Zapotec.
zpq  Zoogocho Zapotec  -  zpq  Mexico  2  304938  1951124  ZPQ  -  -  -  zty zat zav zad bg-Latn tob zaq  en es  no  -  Fri Dec 28 10:37:38 CST 2012  SAN BARTOLOMÉ ZOOGOCHO ZAPOTECO, ZOOGOCHO ZAPOTEC  Oto-Manguean, Zapotecan, Zapotec.
zpt  San Vicente Coatlán Zapotec  -  zpt  Mexico  2  253712  1331151  ZPT  -  -  -  pps zad zpu kao zav xtd  en es  no  -  Fri Dec 28 10:38:05 CST 2012  SOUTHERN EJUTLA ZAPOTECO, SAN VICENTE COATLÁN ZAPOTEC, COATLÁN ZAPOTECO  Oto-Manguean, Zapotecan, Zapotec.
zpu  Yalálag Zapotec  -  zpu  Mexico  3  324214  1914075  ZPU  -  -  -  zad zav zpc zpt ctp zpq zty zpf cnl  en es  no  -  Fri Dec 28 10:39:06 CST 2012  -  Oto-Manguean, Zapotecan, Zapotec.
zpv  Chichicapan Zapotec  -  zpv  Mexico  2  270667  1662762  ZPV  -  -  -  cbi zpf zai mxt zad mio  en es  no  -  Fri Dec 28 10:39:41 CST 2012  SAN BALTAZAR CHICHICAPAN ZAPOTEC, EASTERN OCOTLÁN ZAPOTECO  Oto-Manguean, Zapotecan, Zapotec.
zpz  Texmelucan Zapotec  -  zpz  Mexico  4  439886  2039413  ZPZ  -  -  -  cta lmo mwl lms ast ca-valencia zab cbk lad oc lnc  en es  no  -  Fri Dec 28 10:42:37 CST 2012  CENTRAL SOLA DE VEGA ZAPOTECO, SAN LORENZO TEXMELUCAN ZAPOTECO, PAPABUCO, TEXMELUCAN ZAPOTEC  Oto-Manguean, Zapotecan, Zapotec.
zro  Záparo  -  zro  Ecuador  1  1376  9917  ZRO  -  -  1124  hub jiv zae qug acu agr qvz chn mrh  en es  no  -  Mon Dec 9 14:13:14 CST 2013  ZÁPARA, KAYAPWE  Zaparoan.
zsm  Standard Malay  Bahasa Melayu  zsm  Malaysia (Peninsular)  130  9191417  66648510  MLI  ml  ms  -  id jv-x-bms bjn su  en id  yes  -  Tue Sep 10 12:10:24 CDT 2013  BAHASA MALAYSIA, BAHASA MALAYU, MALAYU, MELAJU, MELAYU, STANDARD MALAY  Austronesian, Malayo-Polynesian, Western Malayo-Polynesian, Sundic, Malayic, Malayan, Local Malay.
zsr  Southern Rincon Zapotec  -  zsr  Mexico  2  216239  1295506  ZSR  -  -  -  zar  en es  no  -  Thu Jan 10 22:17:18 CST 2013  RINCÓN-SUR ZAPOTEC  Oto-Manguean, Zapotecan, Zapotec.
ztq  Quioquitani-Quierí Zapotec  -  ztq  Mexico  2  276051  1438918  ZTQ  -  -  -  zpo xon-x-likp xon-x-liko gwi om zpf  en es  no  -  Fri Dec 28 10:49:52 CST 2012  -  Oto-Manguean, Zapotecan, Zapotec.
ztu  Güilá Zapotec  -  ztu  Mexico  1  1442  10851  ZTU  -  -  ztu1  plt zpa zab buc xmv  en es  no  -  Mon Dec 9 14:13:05 CST 2013  SAN PABLO GÜILÁ ZAPOTEC  Oto-Manguean, Zapotecan, Zapotec.
zty  Yatee Zapotec  -  zty  Mexico  2  315152  1860388  ZTY  -  -  -  zpu  en es  no  -  Fri Dec 28 10:50:20 CST 2012  YATEE ZAPOTEC  Oto-Manguean, Zapotecan, Zapotec.
zu  Zulu  isiZulu  zul  South Africa  292  651658  5723788  ZUU  zu  zu  zuu  xh nd nr ss xog bem  en  yes  Friedel Wolff, Dwayne Bailey  Sat Feb 2 10:32:24 CST 2013  ISIZULU, ZUNDA  Niger-Congo, Atlantic-Congo, Volta-Congo, Benue-Congo, Bantoid, Southern, Narrow Bantu, Central, S, Nguni (S.40).
zun  Zuni  Shiwi'ma  zun  USA  2  19280  160996  ZUN  -  -  -  ifb ifk  en  no  -  Sat Jan 26 18:49:59 CST 2013  ZUÑI  Language Isolate.
zyj  Youjiang Zhuang  -  zyj  China  6  853  5544  -  -  -  -  en  en  no  -  Fri Oct 18 00:05:31 CDT 2013  -  Tai-Kadai, Kam-Tai, Tai, Northern
zza  Zaza  -  zza  Turkey  93  1126852  6643343  -  -  -  -  kmr ote"""

def getKey(dic, value):
  return [k for k,v in sorted(dic.items()) if value in v]

ISO2LANG = defaultdict(list)
for i in iso6963.split('\n'):
  code, langname,_ = i.split('  ')
  ISO2LANG[code].append(langname.lower())
  
for i in retired_iso6393.split('\n'):
  line = i.split('  ')
  code = line[0]; langname = line[1]
  ISO2LANG[code].append(langname.lower())

RETIRED2ISO = defaultdict(list)
for i in retired_iso6393.split('\n'):
  line = i.split('  ')
  oldcode = line[0]
  newcode = [line[3]] if line[3] else re.findall(r'\[([^]]*)\]',line[4])
  RETIRED2ISO[oldcode] = newcode
  
for i in crubadantable.split('\n'):
  line = i.split('  '); code = line[3]
  ISO2LANG[code].append(line[0])
  ISO2LANG[code].append(line[1])
  ##print line[3], line[0], line[1]  

LANG2ISO = defaultdict(list)
for k,v in ISO2LANG.items():
  for i in v:
    LANG2ISO[i].append(k)
  
def langiso(languagename):
  return getKey(ISO2LANG, languagename)

def isiso(code):
  '''Check whether a code is an iso-696-3 code.'''
  for line in iso6963.split('\n'):
    if code == line.split(' ')[0].strip():
      return True
  return False

def wikicode2iso(wikicode):
  '''Given a wikipedia language code return its corresponding iso-6393 code.
     Check whether the code is an iso-639-1 code (see isomapping) or appears
     in the list of special codes (wikispecialcodes). Else check whether it 
     already is an iso-639-3 code.
     (No iso-codes are found for be-x-old, nds-nl, nah, roa-tara and eml.)'''
  #return langiso({i.split('  ')[3]:i.split('  ')[1].lower() \
                  #for i in listofwikis.split('\n')}[wikicode].lower())
  wikicode = wikicode.split()[0]
  wikilang = defaultdict()
  for i in isomapping.split('\n'):
      wikilang[i.split(' 	')[0]] = i.split(' 	')[2].lower()
  for i in wikispecialcodes.split('\n'):
      wikilang[i.split(' ')[0]] = i.split(' ')[1]
  try:   
    return wikilang[wikicode].lower() 
  except KeyError:
    if isiso(wikicode):
      return wikicode
    else:
      return None

WIKI2ISO = defaultdict()
for i in listofwikis.split('\n'):
  wikicode = i.split('  ')[-2].split()[0]
  #print(wikicode, wikicode2iso(wikicode))
  WIKI2ISO[wikicode] = wikicode2iso(wikicode)

#print(WIKI2ISO['aa'])
#print(wikicode2iso('aa'))


def macrolang():
  macro2lang = defaultdict(list)
  for i in iso6395.split('\n'):
    lastmarco = ""; lang = ""
    if len(i.split('  ')) == 4 and i[0] != " ":
      lastmacro, lang = i.split('  ')[0], i.split('  ')[2]
    else:
      lang = i.strip().split('  ')[0]
    macro2lang[lastmacro].append(lang)
  return macro2lang
    
MACRO2LANG = macrolang()

##print len(MACRO2LANG)
#for i in ISO2LANG:
#  print i, ISO2LANG[i]
#for i in LANG2ISO:
#  print i, LANG2ISO[i]
