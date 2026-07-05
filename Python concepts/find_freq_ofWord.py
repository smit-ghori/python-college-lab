import string

para = """The sun was shining brightly over the small village. Children played in the park while birds sang in the trees. A friendly dog chased a red ball across the grass, and everyone laughed happily. Later, the children sat under a large tree and shared sandwiches, fruit, and juice. The day was warm, the sky was clear, and the village felt peaceful and joyful. Before going home, everyone thanked each other for a wonderful day at the park."""

words = para.lower().split(" ")

d1 = dict()

for word in words:
    word = word.strip(string.punctuation)
    d1[word] = d1.get(word, 0) + 1

print(d1)
