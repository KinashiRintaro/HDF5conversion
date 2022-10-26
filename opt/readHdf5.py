import h5py
 
with h5py.File("mdmp-app.hdf5", "r") as f:
    data_1 = f["monipad/monipad_active_energy_burneds"][0, 0]
    data_11 = f["monipad/monipad_active_energy_burneds"][0, 1]
    data_2 = f["monipad/monipad_dyskinetic_symptoms"][0, 1]
    data_3 = f["user/personal_users"][0, 1]
    print(data_1)
    print(data_11)
    print(data_2)
    print(data_3)