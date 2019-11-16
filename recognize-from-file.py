from libs.reader_file import FileReader

song = None
seconds = 5

r = FileReader('/home/kwok/projects/audio-fingerprint-identifying-python/mp3/beatles.mp3')

print(r.parse_audio())
