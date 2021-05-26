import pandas as pd
info = pd.DataFrame({"P":[4, 7, 1, 8, 9],
                   "Q":[6, 8, 10, 15, 11],
                   "R":[17, 13, 12, 16, 14],
                   "S":[15, 19, 7, 21, 9]},
                   index =["Parker", "William", "Smith", "Terry", "Phill"])
print(info)

newinfo=info.reindex(['Parker',1,2,3,4,5], fill_value =100)
print(newinfo)

