__author__ = 'Rudolf Horvath'

import doctest


class TextBlock:
    """
    This class represents a text sequence. It can have a given type like *word*, *special*,
    and it can be scrambled.
    """
    textTypes = {"word":0, "special":1}

    def scramble(self):
        """
        This function leaves the first and last character in this TextBlock in place,
        but the remaining middle characters will be written back in a reverse order.

        >>> test = TextBlock("alma", "word")
        >>> test.scramble()
        >>> print test
        amla
        """
        block = self.text
        length = len(block)
        wasStr = False
        if length < 4:
            return
        if type(block) == type(''):
            wasStr = True
            block = list(block)
        for j in range(1, (length/2)):
            tmp = block[j]
            block[j] = block[length-j-1]
            block[length-j-1] = tmp
        if wasStr:
            self.text = ''.join(block)
        else:
            self.text = block

    def __str__(self):
        return self.text

    def __init__(self, text, type):
        assert type in TextBlock.textTypes, "Not valid textType"
        self.type = TextBlock.textTypes[type]
        self.text = text


class TextSplitter:
    """
    This class splits a given text sequence into words and other remaining character sequences.
    It can be given, what characters don't represent words.
    The word blocks can be scrambled, to get a special text.

    >>> test = TextSplitter("According to research at Cambridge University, it doesn't matter in what order the letters in a word are, the only important thing is that the first and last letter be at the right place. The rest can be a total mess and you can still read it without a problem. This is because the human mind does not read every letter by itself, but the word as a whole.")
    >>> test.scrambleWords()
    >>> print test
    Anidroccg to rcraeseh at Cgdirbmae Utisreviny, it dseon't mettar in waht oedrr the lrettes in a wrod are, the olny inatropmt tnihg is taht the fsrit and lsat letter be at the rhgit pcale. The rset can be a tatol mses and you can slitl raed it wuohtit a pelborm. Tihs is bsuacee the hamun mnid deos not raed erevy letter by ilestf, but the wrod as a wlohe.
    """

    def scrambleWords(self):
        for block in self.blocks:
            if block.type == TextBlock.textTypes["word"]:
                block.scramble()

    def __init__(self, input, splitTokens=" .,?!;'\n\t\"\r"):
        self.blocks = []
        if len(input) == 0:
            return
        tmpBlock = ""
        splitFlow = input[0] in splitTokens
        for item in input:
            if item in splitTokens:
                if not splitFlow:
                    newBlock = TextBlock(tmpBlock, "word")
                    self.blocks.append(newBlock)
                    tmpBlock = ""
                    splitFlow = True
            else:
                if splitFlow:
                    newBlock = TextBlock(tmpBlock, "special")
                    self.blocks.append(newBlock)
                    tmpBlock = ""
                    splitFlow = False
            tmpBlock += item
        lastBlockType = "special" if input[-1] in splitTokens else "word"
        newBlock = TextBlock(tmpBlock, lastBlockType)
        self.blocks.append(newBlock)

    def __str__(self):
        res = ""
        for block in self.blocks:
            res += str(block)
        return res


if __name__ == "__main__":
    doctest.testmod(verbose=True)
    #doctest.testfile("scramble.test", verbose=True)