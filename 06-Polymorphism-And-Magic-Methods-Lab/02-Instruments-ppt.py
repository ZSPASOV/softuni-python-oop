def play_instrument(instrument):
    return instrument.play()

# Test Code
class Piano:
    def play(self):
        print("playing the piano")

piano = Piano()
play_instrument(piano)
