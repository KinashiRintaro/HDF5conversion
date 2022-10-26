import h5py
 
with h5py.File("test.hdf5", "w") as f:
    dset = f.create_dataset("test", (2, 2))
    dset[0, 0] = 3.0
    dset[0, 1] = 10.0