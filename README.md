# ちひろヨガスタジオ クライアント確認用テストサイト

デザイン案（Figma）をスマホ幅で確認するための静的サイトです。WordPress版ではありません。

- `index.html` TOP
- `terms.html` 利用規約 / `privacy.html` プライバシーポリシー / `tokushoho.html` 特定商取引法に基づく表記
- 全ページ `noindex`（検索に出さない設定）
- 更新手順: `python3 tools/build.py` で HTML を再生成 → commit → push（画像を差し替えたら `tools/build.py` の `V` を更新）
