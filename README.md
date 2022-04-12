# 急いでいる方はこちら
**手っ取り早く概要を知りたいという方は、次の動画をご覧ください（注：音が出ます）**  
https://youtu.be/KrbE1ARE5dA
# memo_con_appとは
[メモコン](https://github.com/ken-hashimoto/memo_con)にログイン機能やメモの保存機能を追加してwebアプリにしたものです。  
[herokuにデプロイしています。ぜひご確認ください。](https://memo-con.herokuapp.com/)
# 使い方
基本的な使い方は[こちら](https://github.com/ken-hashimoto/memo_con)を参照してください。  
以下では今回初めて追加された機能の使い方について説明します。  
初めて使う方はまず会員登録を行ってください。  
無事会員登録することができたら、自動的にログインされた状態になります。
メモしたい内容を書き込み、「保存」をおすとタイトルを入力するダイアログが表示されるので入力し「OK」を押します。（何も入力しなかった場合は「無題」として保存されます。）
するとマイページに保存したメモが一覧で表示され、そこから削除や内容の編集も行えるようになります。  
以上の流れを一枚の画像にまとめました。
<img src="https://user-images.githubusercontent.com/98263011/162753987-8809bd8c-7703-4fb2-b74a-0a8d953af5fa.png" width="100%">

# 注意点
* 念のため、機密性の高い情報は保存しないようにお願いします。
* ~~現時点ではデータベースにsqlite3を使用しているのですがherokuではsqlite3はサポートされていないようなので少なくとも 24 時間に 1 回はデータベース全体が失われるみたいです。  
近々postgreSQLに移行したいと考えていますがそれまではこのことを念頭に置いた上でお使いください。~~ 　　**postgreSQLへの移行が完了しました**
# 今後のアップデート予定
* ~~postgreSQLへの移行~~ **完了（2022/04/12）**
* ~~退会機能の追加~~ **完了（2022/04/12）**
* マイページに保存されたメモのソート機能追加
# 使用例
<img src="https://user-images.githubusercontent.com/98263011/162879610-56caa8da-6d38-4e89-b99a-456be1bf847d.gif" width="100%">