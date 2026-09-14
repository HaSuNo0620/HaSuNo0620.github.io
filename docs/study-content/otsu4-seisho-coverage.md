# 乙4「性質・火災予防・消火」カバレッジ

この文書は、人間が教材の試験範囲と出典を監査するための一覧。knowledge node を正本とし、Story 側はこれらを参照する。

## 第4類共通の性質
- `class4.definition.flammable-liquid` — `fdma-fire-law`
- `class4.prevention.avoid-ignition` — `egov-decree`
- `class4.prevention.limit-vapor` — `egov-decree`

## 特殊引火物
- `class4.classification.special` — `fdma-fire-law`
- `class4.ether.special` — `fdma-fire-law`
- `class4.ether.boiling` — `pubchem-ether`
- `class4.ether.vapor` — `pubchem-ether`

## 第一石油類
- `class4.classification.first` — `fdma-fire-law`
- `class4.gasoline.first` — `fdma-fire-law`
- `class4.toluene.first` — `fdma-fire-law`, `pubchem-toluene`

## アルコール類
- `class4.classification.alcohol` — `fdma-fire-law`
- `class4.ethanol.alcohol` — `fdma-fire-law`, `pubchem-ethanol`
- `class4.ethanol.water` — `pubchem-ethanol`, `pubchem-alcohol-fire`

## 第二石油類
- `class4.classification.second` — `fdma-fire-law`
- `class4.kerosene.second` — `fdma-fire-law`

## 第三石油類
- `class4.classification.third` — `fdma-fire-law`

## 第四石油類
- `class4.classification.fourth` — `fdma-fire-law`

## 動植物油類
- `class4.classification.animal-vegetable` — `fdma-fire-law`

## 代表物質の識別
- `class4.gasoline.flash`, `class4.gasoline.water`, `class4.gasoline.vapor`
- `class4.kerosene.flash`, `class4.kerosene.water`
- `class4.toluene.water`, `class4.toluene.vapor`
- `class4.ether.boiling`, `class4.ether.vapor`

## 火災予防
- `class4.response.remove-ignition` — `egov-decree`
- `class4.response.vapor-low-areas` — `pubchem-gasoline`, `pubchem-toluene`, `pubchem-ether`
- `class4.response.identify-before-action` — `fdma-fire-law`, `egov-decree`

## 消火原理・消火方法
- `class4.extinguishing.match-agent` — `egov-decree`
- `class4.extinguishing.alcohol-resistant-foam` — `pubchem-alcohol-fire`
- `class4.extinguishing.avoid-solid-stream-alcohol` — `pubchem-alcohol-fire`

## 水溶性／非水溶性の区別
- `class4.ethanol.water`
- `class4.gasoline.water`
- `class4.kerosene.water`
- `class4.toluene.water`

## 蒸気・静電気・着火源に関する判断
- `class4.prevention.avoid-ignition`
- `class4.prevention.limit-vapor`
- `class4.gasoline.vapor`
- `class4.toluene.vapor`
- `class4.ether.vapor`
- `class4.response.vapor-low-areas`

## MVPで残しているStory coverage warning

MVPでは3ケース×2バリアントで学習形式そのものを検証するため、知識グラフ全体を先に正本として持ちつつ、以下はまだStory側で十分に測定していない。validator の warning は意図的に残し、次のStory追加時に解消する。

### Story未登場 (`NO_STORY_COVERAGE`)
- `class4.classification.animal-vegetable`
- `class4.classification.fourth`
- `class4.classification.third`
- `class4.definition.flammable-liquid`

### 遭遇のみで、適用・識別をまだ測っていない (`ENCOUNTER_ONLY_COVERAGE`)
- `class4.ethanol.alcohol`
- `class4.ether.special`
- `class4.extinguishing.avoid-solid-stream-alcohol`
- `class4.toluene.first`

> 注: MVPでは静電気を独立ノードとしてまだ分離せず、火花を含む着火源管理として扱う。Story の有効性確認後、法令・物化を含む完全版へ拡張する。
