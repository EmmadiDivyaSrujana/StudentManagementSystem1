from pymediainfo import MediaInfo


media_info = MediaInfo.parse('g:\\Simple.mp4')
for track in media_info.tracks:
    #print(track.track_type)
    print(track.format_info)

    #if track.track_type == 'Video':
    #    print (track.bit_rate, track.bit_rate_mode, track.codec)

