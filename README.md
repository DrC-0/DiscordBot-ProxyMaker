# DiscordBot-ProxyMaker

デュエルマスターズのデッキレシピURLをDiscordで送ると、印刷用PDFを生成して返すDiscord Botです。

## 使い方

### コマンド

```
!pdfmake <デッキレシピURL> [オプション]
```

**URL**: `gachi-matome.com` のデッキレシピページのURLを指定します。

**オプション**:

| オプション | 説明 |
|---|---|
| `-ngr` | GRカードをPDFに含めない |
| `-nsp` | 超次元カードをPDFに含めない |

**例**:
```
!pdfmake https://gachi-matome.com/deckrecipe-detail-dm/?tcgrevo_deck_maker_deck_id=xxxxx
!pdfmake https://gachi-matome.com/deckrecipe-detail-dm/?tcgrevo_deck_maker_deck_id=xxxxx -ngr -nsp
```

## セットアップ

### 前提

- [uv](https://docs.astral.sh/uv/) がインストールされていること
- Discord Bot Token が取得済みであること

### 手順

1. リポジトリをクローン

```bash
git clone https://github.com/DrC-0/DiscordBot-ProxyMaker.git
cd DiscordBot-ProxyMaker
```

2. `.env` ファイルを作成し、Discord Bot Token を設定

```
TOKEN=your_discord_bot_token_here
```

3. 依存関係をインストール

```bash
uv sync
```

4. Botを起動

```bash
uv run pdfbot.py
```

### Dockerで実行する場合

```bash
docker build -t discordbot-proxymaker .
docker run --env-file .env discordbot-proxymaker
```

## 注意事項

本プロジェクトはデュエル・マスターズおよびWizards of the Coastの知的財産を利用しています。

デュエル・マスターズはタカラトミー/Wizards of the Coastの登録商標です。カード画像等の著作権はそれぞれの権利者に帰属します。本プロジェクトは非公式のファンメイドツールであり、権利者とは一切関係ありません。

権利者から要請があった場合は、速やかに本リポジトリを削除します。
