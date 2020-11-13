# mugmag

"ドリンクを飲む"を会話のきっかけにするスマートコースター「mugmag」

## デモ動画

## アーキテクチャ

[![アーキテクチャ](https://github.com/RyogaTakao/HackAichi2020/blob/master/presentation/Architecture.png?raw=true)](https://github.com/RyogaTakao/HackAichi2020/blob/master/presentation/Architecture.png?raw=true)

## 選択テーマ

### 三密を避けたリモートワークで失われたFACE TO FACEコミュニケーションをAI/IoTを使って復活せよ!

## 製品概要

### 雑談 × 飲み物 × TECH

[![×Tech](https://github.com/RyogaTakao/HackAichi2020/blob/futureREADME/presentation/%C3%97Tech.png?raw=true)](https://github.com/RyogaTakao/HackAichi2020/blob/futureREADME/presentation/%C3%97Tech.png?raw=true)

### 背景(製品開発のきっかけ，課題等）

COVID-19(新型コロナウイルス)の影響により世の中で様々なことがオンライン化し，人とのコミュニケーションが**対人からテキストベースに変化**している．
そんな中，様々な効果を含んでいるFace to Faceでの雑談が消えようとしている．
私たち自身も，授業のオンライン化で学校に登校しなくなり，「雑談のしずらさ」を感じている．
withコロナ時代における雑談の手法としては，ビデオ会議ツールやSNSを利用することが挙げられる．
しかし，ビデオ会議ツールは目的が無いとセッティングが難しく，SNSはテキストベースのため細かいニュアンスが伝わりにくい．
そのため，私たちは **「オンライン化により雑談のハードルが上がった」** ことを課題とした．

### 製品説明（具体的な製品の説明）

本製品は，**ビデオチャットができるスマートコースター**である．

- オンライン化により人との関わりが減った学生や会社員のためのスマートコースター

- コーヒーブレイク中にビデオチャットで雑談を行うことができる

### 特長

1. マグカップを電話の受話器のような役割に
    - マグカップの動作がトリガーとなり，電話での雑談を開始

2. 通話可能な範囲を制限
    - 1つのAPIキーの中でルームが形成されるため，同じ設定間でのみテレビ電話が繋がる仕組み
    そのため，同じ組織内でのみのランダム通話が可能

3. 会話量によりマッチング範囲を限定
    - 音声認識により会話量をテキスト形式で取得
    文量によってレベル分けを行い，マッチングの範囲を限定

4. 2~4人での通話
    - 1:1による必ず話さなければならないというプレッシャーを軽減するために複数人でのランダム通話を実現

5. Node-REDによる開発
    - フローによる処理の分かりやすさ
    - JSON形式でフローが保存できるため，共有がしやすい

### 解決出来ること

1. コミュニケーション開始のハードルが低くなる

    - 飲み物を持ち上げるだけでビデオチャットが始まる

2. 業務に支障のない時間で雑談できる

    - 最長で5分間しか繋げることができない

    - 飲み物をコースターの上に置いたら通話が終了する

3. 新しい出会い・発見に繋げることができる

    - オンラインだからこそ実現できたランダムマッチングにより，新しい出会いが生まれる

    - 新しく出会う人と話すことにより，新たな発見が得られる

### 今後の展望

- 会話相手をパーソナライズ

    部署別やSNS連携により，身の回りの人と優先的に接続

- 休憩のタイミングをパーソナライズ

    過去の雑談ログから休憩のタイミングを学習させ，休憩のタイミングを提示

### 注力したこと（こだわり等）

## 開発技術

### 活用した技術

#### 使用言語

- HTML
- CSS
- JavaScript
- Python 3

#### フレームワーク・ライブラリ・モジュール

- Node-RED（ラズパイ，IBM Cloud）
- kioskモード
- julius
- skyway

#### API・データ

- IBM Cloudant
- skyway

#### デバイス

- Raspberry Pi 4
- ラズベリーパイカメラ
- ラズベリーパイ用 5インチ DSIタッチLCDスクリーン
- USBマイク
- LEDライト

#### その他

- なし

### 必須なセットアップ

- 使用したデータベースノードのインストール

    $ npm install node-red-node-cf-cloudant

- 使用した音声認識エンジンのインストール

    [JELLYWAREのサイト](https://jellyware.jp/kurage/raspi/julius.html)を参考に，上からjuliusのインストールまでを行う

### 独自技術

#### ハッカソンで開発した独自機能・技術

- アプリケーションの画面や画面遷移等

    - ホーム画面

    [![ホーム画面](https://github.com/RyogaTakao/HackAichi2020/blob/futureREADME/presentation/home.png?raw=true)](https://github.com/RyogaTakao/HackAichi2020/blob/futureREADME/presentation/home.png?raw=true)

    - 時計画面

    [![時計画面](https://github.com/RyogaTakao/HackAichi2020/blob/futureREADME/presentation/clock.png?raw=true)](https://github.com/RyogaTakao/HackAichi2020/blob/futureREADME/presentation/clock.png?raw=true)

    - 通話画面

- アプリケーション本体の処理

#### 製品に取り入れた研究内容（データ・ソフトウェアなど）（※アカデミック部門の場合のみ提出必須）

- なし

#### 事前開発プロダクト

- なし

## 開発チーム

### 名城大学

- [RyogaTakao](https://github.com/RyogaTakao): チームリーダー，開発サポート(フロントエンド，サーバーサイド，組み込み)
- [YoshiharuSenna](https://github.com/YoshiharuSenna): サーバーサイド
- [MinatoyaRyota](https://github.com/MinatoyaRyota): ハードウェア
- [OkazakiTatsuya](https://github.com/TatsuyaOkazaki324): 組み込み，フロントエンド
- [saki0501a](https://github.com/saki0501a): 情報収集，資料作成
