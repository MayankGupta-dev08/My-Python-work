'''Using some other word instead of self as an argument'''

class Sample:
    text = "Yes, it's working. "
    def show(slf, word):
        slf.word = word
        print("Example of using something else other than self as the default parameter. ", slf.text, slf.word)

s = Sample()
s.show("Hurray!!")