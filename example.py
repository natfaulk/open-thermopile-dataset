import math
import os

import pandas as pd

CAM_POS = [0, 2.5, 2.5]
FOV_DIST = math.tan(math.radians(30)) * CAM_POS[2]

# returns true if argument is within the camera's field of view
# argument _pos is a tuple or list of [x,y]
def xyPosInFOV(_pos):
  inFOV_x = abs(_pos[0] - CAM_POS[0]) < FOV_DIST
  inFOV_y = abs(_pos[1] - CAM_POS[1]) < FOV_DIST

  return inFOV_x and inFOV_y

# loop through dataframe and split values between in and out of FOV
# argument is a pandas dataframe
# returns two dataframes with in and out of fov data
def inOutFOV(_df):
  inlist = []
  outlist = []
  count = 0
  for i, row in _df.iterrows():
    if xyPosInFOV([row['x'], row['y']]):
      inlist.append(count)
    else:
      outlist.append(count)
    count += 1

  df_infov = _df.iloc[inlist]
  df_outfov = _df.iloc[outlist]

  return df_infov, df_outfov

if __name__ == '__main__':
  # CSV filepath
  csv_filepath = os.path.join('data', 'day1', 'subject1_sample.csv')

  # read CSV into a pandas dataframe
  df = pd.read_csv(csv_filepath, index_col = 'index')

  # convert time so that it is seconds from the start of the experiment
  df['time'] = pd.to_datetime(df['time'])
  df['time'] = (df['time'] - df.iloc[0]['time']).dt.total_seconds()

  print(df.head())

  # filter so that keeping only values that are in fov
  df_infov, df_outfov = inOutFOV(df)
  print(df_infov.head())
