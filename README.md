# mugmag

HackAichi2020で使用するリポジトリ

## デモ動画

## アーキテクチャ

![アーキテクチャ](https://github.com/RyogaTakao/HackAichi2020/blob/master/presentation/Architecture.png?raw=true)

## 選択テーマ

### 三密を避けたリモートワークで失われたFACE TO FACEコミュニケーションをAI/IoTを使って復活せよ!

## 製品概要

### 雑談 × 飲み物 × TECH

### 背景(製品開発のきっかけ, 課題等）

### 製品説明（具体的な製品の説明）

### 特長

1. マグカップを電話の受話器のような役割に
    - マグカップの動作がトリガーとなり, 電話での雑談を開始

2. 通話可能な範囲を制限
    - 1つのAPIキーの中でルームが形成されるため, 同じ設定間でのみテレビ電話が繋がる仕組み
    そのため, 同じ組織内でのみのランダム通話が可能

3. 会話量によりマッチング範囲を限定
    - 音声認識により会話量をテキスト形式で取得
    文量によってレベル分けを行い, マッチングの範囲を限定

4. 2~4人での通話
    - 1:1による必ず話さなければならないというプレッシャーを軽減するために複数人でのランダム通話を実現

5. Node-REDによる開発
    - フローによる処理の分かりやすさ
    - JSON形式でフローが保存できるため, 共有がしやすい

### 解決出来ること

### 今後の展望

### 注力したこと（こだわり等）

## 開発技術

### 活用した技術

#### 使用言語

- HTML
- CSS
- JavaScript
- Python 3

#### フレームワーク・ライブラリ・モジュール

- Node-RED
- kioskモード
- julius
- cloudant

#### API・データ

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

    [JELLYWAREのサイト](https://jellyware.jp/kurage/raspi/julius.html)を参考に, 上からjuliusのインストールまでを行う

### 独自技術

#### ハッカソンで開発した独自機能・技術

#### 製品に取り入れた研究内容（データ・ソフトウェアなど）（※アカデミック部門の場合のみ提出必須）

- なし

#### 事前開発プロダクト

- なし

## 開発チーム

### 名城大学

- [RyogaTakao](https://github.com/RyogaTakao): チームリーダー, 開発サポート(フロントエンド, サーバーサイド, 組み込み)
- [YoshiharuSenna](https://github.com/YoshiharuSenna): サーバーサイド
- [MinatoyaRyota](https://github.com/MinatoyaRyota): ハードウェア
- [OkazakiTatsuya](https://github.com/TatsuyaOkazaki324): 組み込み, フロントエンド
- [saki0501a](https://github.com/saki0501a): 情報収集, 資料作成
