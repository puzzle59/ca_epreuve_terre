import sys
if len(sys.argv[1:])==1:
    full_date=sys.argv[1]
    tf_hour=int(full_date[0:2])
    tf_minute=int(full_date[3:])
    if tf_hour == 00 and tf_minute==00:
        hour_amp="00"
        minute_amp="00"
        ampm="AM"
    elif tf_hour <=9:
        hour_amp="0"+str(tf_hour)
        if tf_minute<=9:
            minute_amp="0"+str(tf_minute)
        else:
            minute_amp=tf_minute
        ampm="AM"
    elif tf_hour <12:
        hour_amp=tf_hour
        if tf_minute<=9:
            minute_amp="0"+str(tf_minute)
        else:
            minute_amp=tf_minute

        ampm="AM"
    elif tf_hour==12 and tf_minute==00:
        hour_amp="00"
        minute_amp="0"+str(tf_minute)
        ampm="PM"
    elif tf_hour <22:
        hour_amp="0"+str(tf_hour%12)
        if tf_minute<=9:
            minute_amp="0"+str(tf_minute)
        else:
            minute_amp=tf_minute
        ampm="PM"
    else:
        hour_amp=tf_hour
        hour_amp=str(tf_hour%12)
        if tf_minute<=9:
            minute_amp="0"+str(tf_minute)
        else:
            minute_amp=tf_minute
        ampm="PM"
    print(f"{hour_amp}:{minute_amp}{ampm}")
