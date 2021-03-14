#Code


#		python code
#		script_name: hello
#
#		author: Siddharth
#		description: composition
#
#   set up
from earsketch import *

#   Initialized
init()
setTempo(120)

#  varible
chord = RD_UK_HOUSE__5THCHORD_2
secondarybeat = HIPHOP_BASSSUB_001
mainbeat = HOUSE_MAIN_BEAT_003

#   Music
fitMedia(chord, 1, 1, 16)
setEffect(1, VOLUME, GAIN, -60, 1, 5, 12)
setEffect(1, VOLUME, GAIN, 5, 12, -60, 16)

fitMedia(secondarybeat, 2, 1, 12)

setEffect(2, DELAY, DELAY_TIME, 500)
fitMedia(mainbeat, 3, 1, 8)
setEffect(2, REVERB, REVERB_TIME, 200)
#   Finish
finish()