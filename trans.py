aplhabet = {
    "ა":"a",
    "ბ":"b",
    "გ":"g",
    "დ":"d",
    "ე":"e",
    "ვ":"v",
    "ზ":"z",
    "თ":"t",
    "ი":"i",
    "კ":"k’",
    "ლ":"l",
    "მ":"m",
    "ნ":"n",
    "ო":"o",
    "პ":"p’",
    "ჟ":"zh",
    "რ":"r",
    "ს":"s",
    "ტ":"t’",
    "უ":"u",
    "ფ":"p",
    "ქ":"k",
    "ღ":"gh",
    "ყ":"q’",
    "შ":"sh",
    "ჩ":"ch",
    "ც":"ts",
    "ძ":"dz",
    "წ":"ts’",
    "ჭ":"ch’",
    "ხ":"kh",
    "ჯ":"j",
    "ჰ":"h"}

def transctipt(word):
    tr = ""
    for s in word:
        val = aplhabet.get(s)
        if val is not None: 
            tr = tr + val
        if val is None: 
            tr = tr + s
    return tr


# ss = "საღამო მშვიდობისა!"

# print(transctipt(ss))



    
