import h5py
 
with h5py.File("mdmp-app.hdf5", "w") as f:
    # 読み込んだCSVの形状を取得
    matrix = (4, 2)

    # 以下の形状でグループ（フォルダ）を作成できる
    g_monipad=f.create_group('monipad')

    # データセット（ファイルに当たるもの）を作成
    dset = f.create_dataset("monipad/monipad_active_energy_burneds", matrix)
    dset[0, 0] = 3.0
    dset[0, 1] = 10.0

    dset = f.create_dataset("monipad/monipad_dyskinetic_symptoms", matrix)
    dset[0, 0] = 5.0
    dset[0, 1] = 12.0

    g_user=f.create_group('user')
    dset = f.create_dataset("user/personal_users", matrix)
    dset[0, 0] = 103.0
    dset[0, 1] = 104.0