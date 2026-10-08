# VOICEVOX動画生成

Webサイト本体とは独立した GitHub Actions の動画生成機能です。

## 使い方

1. リポジトリで Issue を作成します。
2. タイトルを `[voicevox-video] 動画名` で始めます。
3. 本文に JSON をそのまま貼ります（Markdownのコードフェンスは不要）。
4. Actions → **VOICEVOX narrated video** → 対応する実行 → **Artifacts** からMP4とWAVを取得します。

Issue経由の自動生成は、リポジトリ所有者が開いたIssueに限定されています。

## JSON例

```json
{
  "speaker": 3,
  "scenes": [
    {
      "title": "BKT転移",
      "caption": "渦対が解離する位相転移",
      "narration": "二次元エックスワイ模型では、渦と反渦の対が温度上昇によって解離します。"
    }
  ]
}
```

既存の `video_jobs/bkt-demo.json` を試す場合は Actions の **Run workflow** を使えます。

- `speaker: 3` はずんだもん（ノーマル）を想定しています。
- シーン数1～15、ナレーションは1シーン240文字以下です。
- `tts.quest` の無料VOICEVOX APIを使用します。混雑時の待機や429制限により失敗することがあります。
- 音声はVOICEVOXの各キャラクターの利用規約に従って利用してください。動画のクレジット表記も確認してください。
- Artifacts保存期間は7日です。
- \`motion\` を指定すると、Pillowで描いた動的スピン場をFFmpegで動画化します。現在のモードは \`spins\`（スピン配向）、\`vortex_pair\`（渦対）、\`unbinding\`（渦対の解離）です。これは概念図であり、実際のXY模型のMD/MC軌道ではありません。Manimによる数式アニメーションは未実装です。
- 通常のサイト用GitHub Pagesワークフローは変更していません。初回のファイル追加コミットではサイト側の既存のpushトリガーも通常通り動きますが、Issueによる動画生成ではサイトのデプロイは起こりません。
