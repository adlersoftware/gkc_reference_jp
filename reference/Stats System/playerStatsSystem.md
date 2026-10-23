# playerStatsSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Stats System/playerStatsSystem.cs:7`

**概要**: キャラクターの数値・boolステータスを`statInfoList`で保持し、増減、上限Clamp、イベント発火、テンプレート保存/読込の中心となるクラス。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Player Stats Active | `playerStatsActive` | `bool` | true | ONにするとこのキャラのステータス機能を有効にする。 |
| Initialize Stats Values At Start Active | `initializeStatsValuesAtStartActive` | `bool` | true | ONにすると開始時に各ステータスを初期値へ設定する。 |
| Initialize Stats Only When Loading Game | `initializeStatsOnlyWhenLoadingGame` | `bool` | – | ONにするとセーブ読込時だけ初期化を実行する。 |
| Save Current Player Stats To Save File | `saveCurrentPlayerStatsToSaveFile` | `bool` | – | ONにするとステータス値もセーブデータに保存する。 |
| Use By AI | `useByAI` | `bool` | – | ONなら`Awake`で初期化しAIでも値を揃える。 |

### Stats Settings Template

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Initialize Values When Not Loading From Template | `initializeValuesWhenNotLoadingFromTemplate` | `bool` | – | ONならセーブ読込以外はテンプレート値で初期化する。 |
| Main Stats Settings Template | `mainStatsSettingsTemplate` | `statsSettingsTemplate` | – | 初期値の保存と読込に使う`statsSettingsTemplate`。 |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `statInfoList` | `List<statInfo>` | new List<statInfo> () | – |
| `isLoadingGame` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `initializeStatsValues()` | 有効時のみ、条件に応じてテンプレートを読み込み、各`statInfo`の初期化イベントを発火する。 |
| `setIsLoadingGameState(bool state)` | 読み込み中かどうかの`isLoadingGame`を`state`に設定するだけ。 |
| `isLoadingGameState()` | `isLoadingGame`の値をそのまま返すだけ。 |
| `getStatMaxAmountByIndex(int statIndex)` | 指定インデックスの最大値を返し、他ステータス参照時はその値（負なら現在値）を用いる。 |
| `getStatMaxAmountByName(string statName)` | 名前で探した最大値を返し、`useMaxAmount`が無効か不一致なら-1を返す。 |
| `isStatOnMaxAmount(string statName)` | 名前で探したステータスの現在値が最大値以上かを返し、それ以外はfalse。 |
| `increasePlayerStatWithNameAndAmount(string statNameAndAmountString)` | `;`区切りの「名前;数値」を分解し、値が正なら`increasePlayerStat`を呼ぶ。 |
| `setTemporalStatName(string statName)` | 一時ステータス名`temporalStatName`を設定するだけ。 |
| `increasePlayerStateOfTemporalStat(float statExtraValue)` | 保持した一時ステータス名で増加させ、その後`temporalStatName`を空にする。 |
| `increasePlayerStatByMultiplier(string statName, float statMultiplier)` | 現在値の`statMultiplier`%を計算し、現在値が正なら加算する。 |
| `increasePlayerStat(string statName, float statExtraValue)` | 名前一致のステータスへ値を加算し、上限があればClampして増加イベントを発火する。 |
| `increaseExtraPlayerStat(string statName, float statExtraValue)` | 加算に加え`extraCurrentValue`にも値を積み、上限Clampと増加イベントを行う。 |
| `usePlayerStat(string statName, float statValueToUse)` | 値を減算して0未満を0にし、使用イベントを発火する。 |
| `usePlayerStatByIndex(int statIndex, float statValueToUse)` | インデックスの範囲を確認してから、その名前で`usePlayerStat`を呼ぶ。 |
| `addOrRemovePlayerStatAmount(string statName, float amountToUse)` | 符号付きの値を加算して0と上限でClampし、正なら追加、負なら使用イベントを発火する。 |
| `getStatName(int index)` | 指定インデックスのステータス名を返し、範囲外なら空文字を返す。 |
| `getStatsNames()` | 全ステータス名を新しいリストにして返す。 |
| `getStatValue(string statName)` | 名前一致のステータス現在値を返し、見つからなければ-1を返す。 |
| `checkIfStatValueAvailable(string statName, int statAmount)` | 現在値が`statAmount`以上かを返し、一致するステータスがなければfalse。 |
| `getStatValueByIndex(int statIndex)` | インデックスの現在値を返し、負のインデックスなら-1を返す。 |
| `getStatValueIndex(string statName)` | ステータス名のリスト内インデックスを返し、見つからなければ-1。 |
| `updateStatValue(string statName, float newValue)` | 現在値を置き換えて上限Clampし、設定時イベントが有効ならインデックスと値を渡して発火する。 |
| `updateStatValueExternally(int statIndex, float newValue)` | インデックスを名前に変換し、外部更新版の`updateStatValueExternally`を呼ぶ。 |
| `updateStatValueExternally(string statName, float newValue)` | 現在値を置き換えてClampし、外部更新用イベントが有効なら発火する。 |
| `updateStatValue(int statIndex, float newValue)` | インデックスを名前に変換して`updateStatValue`を呼ぶだけ。 |
| `enableOrDisableBoolPlayerStat(string statName, bool boolStateValue)` | boolステータスの状態を設定し、bool有効化イベントを発火する。 |
| `getBoolStatValue(string statName)` | 名前一致のboolステータス状態を返し、見つからなければfalse。 |
| `updateBoolStatValue(string statName, bool boolStateValue)` | boolステータスの状態を保存するだけで、イベントは発火しない。 |
| `setPlayerStatsActiveState(bool state)` | `playerStatsActive`を`state`に設定するだけ。 |
| `saveSettingsToTemplate()` | テンプレートへ全ステータスの名前・数値・boolをコピーし、シーンをダーティにして保存ログを出す。 |
| `loadSettingsFromTemplate(bool loadingFromEditor)` | テンプレートと同名のステータスへ値とboolを戻し、エディタ読込時は更新とダーティ処理も行う。 |
| `initializeAllStatValuesFromEditor()` | 全ステータスの初期化イベントを発火した後、コンポーネント更新とシーンのダーティ処理を行う。 |
| `initializeStatValueFromEditor(string statName, bool updateComponentValue)` | 指定ステータスの初期化イベントを発火し、フラグが真ならコンポーネント更新とダーティ処理も行う。 |
| `updateStatValueFromEditor(string statName, float newValue)` | `updateStatValue`で値を更新した後、コンポーネント更新とシーンのダーティ処理を行う。 |
| `setPlayerStatsActiveStateFromEditor(bool state)` | 有効状態を設定した後、コンポーネント更新とシーンのダーティ処理を行う。 |
| `updateComponent()` | `GKC_Utils.updateComponent`でこのコンポーネントを更新するだけ。 |

## 内部型

- `statInfo`（class）
- `statTemplateInfo`（class）
