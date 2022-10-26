import h5py
 
with h5py.File("test.hdf5", "r") as f:
    data_1 = f["test"][0, 0]
    data_2 = f["test"][0, 1]
    print(data_1)
    print(data_2)