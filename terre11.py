import sys
if len(sys.argv[1:])==1:
    time=sys.argv[1]
    tf_hour=int(time[0:2])
    tf_minute=time[3:5]
    ampm=time[5:]
    if tf_hour==12 and tf_minute=="00" and ampm=="AM":
        ampm_hour="00"
    if tf_hour==12 and tf_minute=="00" and ampm=="PM":
        ampm_hour="12"
    if tf_hour< 10 and ampm=="AM":
        ampm_hour="0"+str(tf_hour)
    elif tf_hour < 12 and ampm=="AM":
        ampm_hour=tf_hour
    elif tf_hour< 10 and ampm=="PM":
        ampm_hour=tf_hour+12
    elif tf_hour < 12 and ampm=="PM":
        ampm_hour=tf_hour+12
    print(f"{ampm_hour}:{tf_minute}")
#devait mettre mot de passe pour save à chaque fois
#histoire de permission de fichier . il y en a des choses à voir


else:
    print("erreur")
