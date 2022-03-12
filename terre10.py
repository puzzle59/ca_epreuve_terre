import sys
if len(sys.argv[1:])==1:
    full_date=sys.argv[1]
    tf_hour=int(full_date[0:2])
    tf_minute=full_date[3:]
    ampm="AM"
    if tf_hour == 00 and tf_minute==00:
        hour_amp="00"
    elif tf_hour <=9:
        hour_amp="0"+str(tf_hour)
    elif tf_hour <12:
        hour_amp=tf_hours
    elif tf_hour==12 and tf_minute==00:
        hour_amp="00"
        ampm="PM"
    elif tf_hour <22:
        hour_amp="0"+str(tf_hour%12)
        ampm="PM"
    else:
        hour_amp=tf_hour
        hour_amp=str(tf_hour%12)
        ampm="PM"
    print(f"{hour_amp}:{tf_minute}{ampm}")
