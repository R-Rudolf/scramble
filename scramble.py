__author__ = 'Rudolf Horvath'


class TextBlock:
    textTypes = {"word":0, "special":1}

    def scramble(self):
        """
        >>> test = TextBlock("alma", "word")
        >>> test.scramble()
        >>> print test.text
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

    def toString(self):
        return self.text

    def __init__(self, text, type):
        assert type in TextBlock.textTypes, "Not valid textType"
        self.type = TextBlock.textTypes[type]
        self.text = text


class TextSplitter:

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

    def toString(self):
        res = ""
        for block in self.blocks:
            res += block.toString()
        return res

