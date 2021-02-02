import pandas as pd
import os

data_train_df = pd.read_pickle(os.path.join('data', 'data_train.pkl'))


print('done')