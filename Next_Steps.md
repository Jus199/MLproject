## Clean the media piped data
We must clean the data by compressing all the landmarked frames (which are all vidoes at 25fps) down to a consistent amount of frames so the sliding window can then be later implemented. 

We will also have to handle the blank/NaN values when mediapipe could not detect a hand. 

We will also need to normilize the coordinates so the model does not base things off of scale.
    We can do this via pre-sequence normalization, by cenering each squence around the wrist landmark so the model learns hand shapes relative to wrist position. Giving it a normalization that is not reliant on screen position, which will be good for the real time inference. 
    We could als do a standard scaling of subtracting mean and divide by the std across the whole data set, this is less complex, but probably gives a worse result.

We have to handle the missing hands, some signs are two handed. When only one hand is present the other 63 columns will be all zero. 

We also need to drop low quality sequences (with less than the sliding window amount of frames)

## Split the data
then we must split and clean the data. 