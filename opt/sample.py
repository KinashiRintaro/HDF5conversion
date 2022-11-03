import h5py

with h5py.File('sample_dataset.hdf5', mode='w') as f:
    # vlen=str でないとUnicode文字が使えないので注意
    str_dtype = h5py.special_dtype(vlen=str)

    dataset = f.create_dataset(
    'str_dataset', shape=(1,1), dtype=str_dtype)
    dataset[0,0] = 'あいう'
    # 以下の形式でhdf5ファイルに保存
    # b'\xe3\x81\x82\xe3\x81\x84\xe3\x81\x86'

with h5py.File("sample_dataset.hdf5", "r") as f:
    data = f["str_dataset"][0,0]
    # 出力時にデコードを行う
    print(data.decode('utf-8'))
    print(data)
    # 出力：あいう