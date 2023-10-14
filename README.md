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

| Table                          | Row Count |
|--------------------------------|-----------|
| base_kondate_likes             | 536649    |
| base_kondate_recipes           | 144223    |
| base_kondates                  | 35928     |
| ingredients                    | 12725006  |
| kondate_categories             | 16        |
| kondate_category_user_kondates | 79876     |
| recipes                        | 1715595   |
| search_categories              | 1099      |
| search_category_recipes        | 164912    |
| steps                          | 0         |

(stepsの数が0なのは原因不明です．．．解凍時のshasum値は正しかったです)

### バージョン履歴
- v1.0.0 
  - 2023/10/14:リポジトリ公開
