# open-thermopile-dataset

For more information about this dataset see the published article.  
For data citation, please cite the published article.  

## Data format

There are four subjects, subjects 1-3 are male, subject 4 is female.

There are two sub directories in the data directory:  
Day 1:  
  - subject1.csv - the large dataset used for training
  - subject1_coat.csv - a smaller dataset with Subject 1 wearing thick winter clothing

Day 2:
  - subject1.csv
  - subject2.csv
  - subject3.csv
  - subject4.csv

Each CSV file has the same format. The first row is a header row, with every subequent row a single reading.  
The first column is an index column, followed by 64 pixels from the device - p0 - p64, the onboard thermistor, the time in the format yyyy-MM-dd HH:mm:ss.sss, the x position, and finally the y position.

## Experimental setup
This data is the raw unprocessed data from the thermopile and the HTC Vive ground truth. The subjects walked about a 5 m by 5 m area arbitrarily, and therefore are not always within the field of view of the sensor. Therefore, the first step before using this data for positioning, should be to remove all samples out of the field of view of the sensor. The sensor is positioned at x = 0 m, y = 2.5 m, z (height abouve the floor) = 2.5 m.

## Example Python code
See example.py for example code that loads a csv to a dataframe and performs some rudimentary preprocessing upon the data.  
