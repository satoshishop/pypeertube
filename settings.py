auth_data = {'username': "test",
             'password': "5k8j9NTo292xcuRGYQVCzTUMzaw3Rt"
             }

config = { "path":"/path/to/your/videos",
           "site":"https://peertube.satoshishop.de",
           "channel":"testchannel",
           "channelID":None, #if you don't change it, we'll use the channel name to get it from the site
           "category":None,
           "licence":7, 
           "language":"en",
           "privacy":1, #1 = public and 2 = private
           "nsfw":False, #If your videos are NSFW, change this to True
           "commentsEnabled":True,
           "downloadEnabled":True,
           "exclude_list":["/exclude/folder","/exclude/"],
           "support":"If you like our service, drop some satoshis here"
         }

custom_tags = ["set","your","own","tags"] #function "add_custom_tags" searches these tags in video titles and sets them on hit

#licence - english
# 1 = Attribution
# 2 = Attribution - Share Alike
# 3 = Attribution - No Derivatives
# 4 = Attribution - Non Commercial
# 5 = Attribution - Non Commercial - Share Alike
# 6 = Attribution - Non Commercial - No Derivatives
# 7 = Public Domain Dedication

#category
#1 = Music
#2 = Films
#3 = Vehicles
#4 = Art
#5 = Sports
#6 = Travels
#7 = Gaming
#8 = People
#9 = Comedy
#10 = Entertainment
#11 = News &amp; Politics
#12 = How To
#13 = Education
#14 = Activism
#15 = Science &amp; Technology
#16 = Animals
#17 = Kids
#18 = Food

#languages
#ab = Abkhazian
#aa = Afar
#af = Afrikaans
#ak = Akan
#sq = Albanian
#ase = American Sign Language
#am = Amharic
#ar = Arabic
#an = Aragonese
#hy = Armenian
#as = Assamese
#av = Avaric
#ay = Aymara
#az = Azerbaijani
#bm = Bambara
#ba = Bashkir
#eu = Basque
#be = Belarusian
#bn = Bengali
#bi = Bislama
#bs = Bosnian
#bzs = Brazilian Sign Language
#br = Breton
#bfi = British Sign Language
#bg = Bulgarian
#my = Burmese
#ca = Catalan
#ch = Chamorro
#ce = Chechen
#zh = Chinese
#csl = Chinese Sign Language
#cv = Chuvash
#kw = Cornish
#co = Corsican
#cr = Cree
#hr = Croatian
#cs = Czech
#cse = Czech Sign Language
#da = Danish
#dsl = Danish Sign Language
#dv = Dhivehi
#nl = Dutch
#dz = Dzongkha
#en = English
#eo = Esperanto
#et = Estonian
#ee = Ewe
#fo = Faroese
#fj = Fijian
#fi = Finnish
#fr = French
#fsl = French Sign Language
#ff = Fulah
#gl = Galician
#lg = Ganda
#ka = Georgian
#de = German
#gsg = German Sign Language
#el = Greek
#gn = Guarani
#gu = Gujarati
#ht = Haitian
#ha = Hausa
#he = Hebrew
#hz = Herero
#hi = Hindi
#ho = Hiri Motu
#hu = Hungarian
#is = Icelandic
#ig = Igbo
#id = Indonesian
#iu = Inuktitut
#ik = Inupiaq
#ga = Irish
#it = Italian
#ja = Japanese
#jsl = Japanese Sign Language
#jv = Javanese
#kl = Kalaallisut
#kn = Kannada
#kr = Kanuri
#ks = Kashmiri
#kk = Kazakh
#km = Khmer
#ki = Kikuyu
#rw = Kinyarwanda
#ky = Kirghiz
#tlh = Klingon
#kv = Komi
#kg = Kongo
#ko = Korean
#avk = Kotava
#kj = Kuanyama
#ku = Kurdish
#lo = Lao
#lv = Latvian
#li = Limburgan
#ln = Lingala
#lt = Lithuanian
#jbo = Lojban
#lu = Luba-Katanga
#lb = Luxembourgish
#mk = Macedonian
#mg = Malagasy
#ms = Malay (macrolanguage)
#ml = Malayalam
#mt = Maltese
#gv = Manx
#mi = Maori
#mr = Marathi
#mh = Marshallese
#mn = Mongolian
#na = Nauru
#nv = Navajo
#ng = Ndonga
#ne = Nepali (macrolanguage)
#nd = North Ndebele
#se = Northern Sami
#no = Norwegian
#nb = Norwegian Bokmål
#nn = Norwegian Nynorsk
#ny = Nyanja
#oc = Occitan
#oj = Ojibwa
#or = Oriya (macrolanguage)
#om = Oromo
#os = Ossetian
#pks = Pakistan Sign Language
#pa = Panjabi
#fa = Persian
#pl = Polish
#pt = Portuguese
#ps = Pushto
#qu = Quechua
#ro = Romanian
#rm = Romansh
#rn = Rundi
#ru = Russian
#rsl = Russian Sign Language
#sm = Samoan
#sg = Sango
#sc = Sardinian
#sdl = Saudi Arabian Sign Language
#gd = Scottish Gaelic
#sr = Serbian
#sh = Serbo-Croatian
#sn = Shona
#ii = Sichuan Yi
#sd = Sindhi
#si = Sinhala
#sk = Slovak
#sl = Slovenian
#so = Somali
#sfs = South African Sign Language
#nr = South Ndebele
#st = Southern Sotho
#es = Spanish
#su = Sundanese
#sw = Swahili (macrolanguage)
#ss = Swati
#sv = Swedish
#swl = Swedish Sign Language
#tl = Tagalog
#ty = Tahitian
#tg = Tajik
#ta = Tamil
#tt = Tatar
#te = Telugu
#th = Thai
#bo = Tibetan
#ti = Tigrinya
#to = Tonga (Tonga Islands)
#ts = Tsonga
#tn = Tswana
#tr = Turkish
#tk = Turkmen
#tw = Twi
#ug = Uighur
#uk = Ukrainian
#ur = Urdu
#uz = Uzbek
#ve = Venda
#vi = Vietnamese
#wa = Walloon
#cy = Welsh
#fy = Western Frisian
#wo = Wolof
#xh = Xhosa
#yi = Yiddish
#yo = Yoruba
#za = Zhuang
#zu = Zulu