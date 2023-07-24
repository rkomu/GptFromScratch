# Tokenize
class Tokenizer():
    # map string to int
    def mapStringToInt(characters:list):
        return {ch:i for i, ch in enumerate(characters)}

    # map to int to string
    def mapIntToString(characters:list):
        return {i:ch for i, ch in enumerate(characters)}

    # string to int
    def encoder(string:str, CharMaps:list):
        return [CharMaps[c] for c in string]

    # int to string
    def decoder(int_list:list):
        return ''.join()


# Training and validate 
class DataLoader():
    def __init__(self, data) -> None:
        self.data = data

    # split data into validation and training data.
    def splitData(self, splitPercentage=0.9):
        n = int(splitPercentage*len(self.data))
        val_data = self.data[n:]
        train_data = self.data[:n]

        return train_data, val_data
    
    def getBlock(data:list, block_size=8):
        return data[:block_size+1]
    
    