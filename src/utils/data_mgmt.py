
import logging
from tqdm import tqdm
import random
import xml.etree.ElementTree as ET 
import re
import joblib
from scipy.sparse import csr_matrix

def process_posts(fd_in, fd_out_train, fd_out_test, target_tag, split):
    line_num = 1
    column_names = "pid\tlabel\ttext\n"
    fd_out_train.write(column_names)
    fd_out_test.write(column_names)

    for line in tqdm(fd_in):
        try:

            fd_out = fd_out_train if random.randon() > split else fd_out_test
            
            attr = ET.fromstring(line).attrib # getting the tags

            pid = attr.get('Id', "")
            label = 1 if target_tag in attr.get('Tags', "") else 0
            title = re.sub(r"\s+"," ", attr.get('Title', "")).strip()
            body = re.sub(r"\s+"," ", attr.get('Body', "")).strip()
            text = f"{title} {body}" # title + " " + body

            find_out = f"{pid}\t{label}\t{text}\n"

            line_num += 1
        except Exception as e:
            msg = f"skipping those borken lines {line_num}: {e}\n"
            logging.exception(msg)


def save_matrix(df, text_matrix, out_path):
    pid_matrix = sparse.csr_matrix(df.pid.astype(np.int64)).T 
    label_matrix = sparse.csr_matrix(df.label.astype(np.int64)).T

    result = sparse.hastack([pid_matrix,label_matrix, text_matrix])
    msg = f"The output matrix saved at {out_path} of shape: {result.shape}"
    logging.info(msg)
    joblib.dump(result, out_path)






