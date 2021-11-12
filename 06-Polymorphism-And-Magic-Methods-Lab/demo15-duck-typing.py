class Baba:
    def __len__(self):
        return 42


baba = Baba()

print(len(baba)) # 42
print(baba.__len__())