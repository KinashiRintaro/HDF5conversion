import h5py
import numpy as np
import pandas as pd
 
with h5py.File("mdmp-app.hdf5", "w") as f:
    # 読み込んだCSVの形状を取得
    matrix = (4, 2)

    # 以下の形状でグループ（フォルダ）を作成できる
    g_monipad=f.create_group('/monipad')

    str_dtype = h5py.special_dtype(vlen=str)

    # データセット（ファイルに当たるもの）を作成
    # dset = g_monipad.create_dataset(
    #     name="monipad_active_energy_burneds", 
    #     shape=matrix, 
    #     dtype=str_dtype
    #     )
    dset = g_monipad.create_dataset(
        name="monipad_active_energy_burneds", 
        shape=(2,), 
        dtype=str_dtype
        )
    dset[0] = "one peace"
    dset[1] = 'あいう'

    # 以下の記述でg_monipadに属するデータセットの数がデバック可能
    # print(g_monipad)
    # print(dset)

    dset = g_monipad.create_dataset(
        name="monipad_dyskinetic_symptoms", 
        shape=matrix, 
        dtype=np.int8
        )
    dset[0, 0] = 5.0
    dset[0, 1] = 12.0

    g_user=f.create_group('user')
    dset = f.create_dataset("user/personal_users", matrix)
    dset[0, 0] = 100.0
    dset[0, 1] = 104.0


    # mdmp-app.hdf5
    #     - monipad
    #         - monipad_active_energy_burneds
    #         - monipad_dyskinetic_symptoms
    #     - user
    #         - monipad_dyskinetic_symptoms
    pass