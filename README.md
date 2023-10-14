# クックパッドレシピデータセット
クックパッド社が提供するデータベースをDocker環境で構築するリポジトリです．
実行には以下のURLにある国立情報学研究所との契約の上，Cookpadデータセットの取得が必要です．[対象URL](https://www.nii.ac.jp/dsc/idr/cookpad/)


## 環境構築
各自でDockerをインストールしておいてください．

Cookpadのレシピデータが取得できればcookpad_data.sqlが得られると思うので以下のパスに配置します．
```
data\cookpad_data.sql
```

以下のコマンドでビルドします．
```
docker-compose up -d 
```

## 確認テスト
正しくデータベースサーバ構築できているかを確認するには以下のPythonを実行します．(Python環境は各自で用意してください)

- python connect_test.py


この時，以下でモジュールをインストールする必要があります．

```
pip install -r requirements.txt
```

実行結果以下のようになれば正常に構築できています．


