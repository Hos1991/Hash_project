import hashlib
import csv
from collections import OrderedDict
def hash_password_hack(input_file_name, output_file_name):
    list_code = [*range(1000, 10000, 1)]
    with open(input_file_name) as f:
        reader = csv.reader(f)
        f2t = OrderedDict()
        goli = OrderedDict()
        for row in reader:
            name = row[0]
            code = row[1]
            i = 0
            for i in range(len(list_code)):
                text = str(list_code[i])
                ggb = hashlib.sha256(text.encode())
                text_hashed = ggb.hexdigest()
                i = i + 1
                if text_hashed == code:
                    final = list_code[i]-1
                    f2t = {name: final }
            goli.update(f2t)
    with open(output_file_name, 'w') as q:
        for key in goli.keys():
            q.write("%s,%s\n"%(key,str(goli[key])))