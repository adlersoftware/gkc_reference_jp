# playerSkillsSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Skills System/playerSkillsSystem.cs:6`

**概要**: プレイヤーのスキルツリーを保持し、カテゴリ／スキルの値・Bool・レベル・解放状態とスキルポイント消費を管理する中核コンポーネント。テンプレートとの保存・読み込み、初期化イベント、ステータス増加、エディタ用の一括操作も備える。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Player Skills Active | `playerSkillsActive` | `bool` | true | スキルシステム全体を稼働させるかどうか。 |
| Initialize Skills Values At Start Active | `initializeSkillsValuesAtStartActive` | `bool` | true | オンにすると開始時にスキル値の初期化を実行する。 |
| Initialize Skills Only When Loading Game | `initializeSkillsOnlyWhenLoadingGame` | `bool` | – | オンにするとセーブ読込時のみ初期化を実行する。 |
| Save Current Player Skills To Save File | `saveCurrentPlayerSkillsToSaveFile` | `bool` | – | 現在のスキル状況をセーブデータに保存するかどうか。 |

### Skill Settings Template

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Initialize Values When Not Loading From Template | `initializeValuesWhenNotLoadingFromTemplate` | `bool` | – | オンにすると非読込時にテンプレートから状態を復元する。 |
| Main Skill Settings Template | `mainSkillSettingsTemplate` | `skillSettingsTemplate` | – | スキルの解放状態を保存・読込するテンプレート。 |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Player Stats System | `mainPlayerStatsSystem` | `playerStatsSystem` | – | スキル効果でステータスを増加させる対象の`playerStatsSystem`。 |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `skillCategoryInfoList` | `List<skillCategoryInfo>` | new List<skillCategoryInfo> () | – |
| `currentSkillInfo` | `skillInfo` | – | – |
| `currentSkillLevelInfo` | `skillLevelInfo` | – | – |
| `isLoadingGame` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `isLoadingGameActive()` | 読み込み中フラグ `isLoadingGame` の値を返すだけ。 |
| `initializeSkillsValues()` | テンプレート由来の完了スキルに値・Bool・解放・最終レベルを反映し、各スキルの初期化イベントを発火する。 |
| `setIsLoadingGameState(bool state)` | 読み込み中フラグ `isLoadingGame` を `state` に設定するだけ。 |
| `isLoadingGameState()` | 読み込み中フラグ `isLoadingGame` を返すだけ。 |
| `increasePlayerSkill(string skillName, float skillExtraValue)` | 有効時のみ名前一致スキルの `currentValue` に `skillExtraValue` を加算し、増加イベントを発火する。 |
| `getSkillValue(string skillName)` | 名前一致スキルの `currentValue` を返し、見つからなければ -1 を返す。 |
| `updateSkillValue(string skillName, float newValue)` | 有効時のみ名前一致スキルの `currentValue` を `newValue` に上書きし、イベントは発火しない。 |
| `enableOrDisableBoolPlayerSkill(string skillName, bool boolSkillValue)` | 有効時のみ名前一致スキルの `currentBoolState` を設定し、`eventToActivateBoolSkill` を発火する。 |
| `getBoolSkillValue(string skillName)` | 名前一致スキルの `currentBoolState` を返し、見つからなければ false を返す。 |
| `updateBoolSkillValue(string skillName, bool boolSkillValue)` | 有効時のみ名前一致スキルの `currentBoolState` を設定するだけで、イベントは発火しない。 |
| `getSkillInfoByIndex(int categoryIndex, int skillIndex)` | インデックスが範囲内なら該当 `skillInfo` を返し、範囲外なら null を返す。 |
| `useSkillPoints(int categoryIndex, int skillIndex, int totalSkillPoints, bool ignoreSkillPoints)` | ポイント充足か `ignoreSkillPoints` ならレベル・値・イベント・ステータスを反映して `skillActive` を立て、消費ポイント数を返す（不足時 -1）。 |
| `getSkillByName(string skillName)` | 名前一致スキルを `useSkillPoints` に 0 ポイント・`ignoreSkillPoints` true で渡して有効化する。 |
| `disableSkillByName(string skillName)` | 有効かつアクティブな該当スキルの完了を解除し、値0／Bool反転のうえ `skillActive` を false にする。 |
| `disableAllSkills()` | 有効な全スキルの完了を解除し値0・Bool反転・レベル0に戻すが、`skillActive` は変更しない。 |
| `unlockSkillSlotByName(string skillName)` | 名前一致スキルの `skillUnlocked` を true にするだけ。 |
| `getCategoryIndex(string categoryName)` | カテゴリ名が一致するインデックスを返し、無ければ -1 を返す。 |
| `getSkillIndex(string skillName)` | 名前一致スキルのカテゴリ内インデックスを返し、無ければ -1 を返す。 |
| `getSkillIndex(string skillCategoryName, string skillName)` | 指定カテゴリ内で名前一致するスキルのインデックスを返し、無ければ -1 を返す。 |
| `setPlayerSkillsActiveState(bool state)` | `playerSkillsActive` を `state` に設定するだけ。 |
| `saveSettingsToTemplate()` | テンプレートを再構築し各スキルの名前・`skillEnabled`・`skillComplete` を保存してシーンをダーティにする。 |
| `loadSettingsFromTemplate(bool loadingFromEditor)` | 名前一致で `skillEnabled` と完了状態をテンプレートから反映し、`loadingFromEditor` 時のみ保存とダーティ更新を行う。 |
| `setAllSkillsCompleteStateOnTemplate(bool state)` | テンプレート全スキルの `skillComplete` を `state` にして更新とダーティ保存を行う。 |
| `enableAllSkillsOnEditor()` | 全カテゴリに `enableOrDisableSkillsOnEditor(true, i)` を適用して `skillEnabled` を立てる。 |
| `disableAllSkillsOnEditor()` | 全カテゴリのスキルの `skillEnabled` を false にする。 |
| `enableSkillsOnEditor(int categoryIndex)` | 指定カテゴリの全スキルの `skillEnabled` を true にして更新する。 |
| `disableSkillsOnEditor(int categoryIndex)` | 指定カテゴリの全スキルの `skillEnabled` を false にして更新する。 |
| `enableOrDisableSkillsOnEditor(bool state, int categoryIndex)` | 指定カテゴリ全スキルの `skillEnabled` を `state` にし、`updateComponent` を呼ぶ。 |
| `activateSkillsOnEditor(int categoryIndex)` | 指定カテゴリの有効スキルへ設定値を反映する `activateOrDeactivateSkillsOnEditor(true, …)` を呼ぶ。 |
| `deactivateSkillsOnEditor(int categoryIndex)` | 指定カテゴリの有効スキルの値とBoolを無効側へ戻す `activateOrDeactivateSkillsOnEditor(false, …)` を呼ぶ。 |
| `activateOrDeactivateSkillsOnEditor(bool state, int categoryIndex)` | 有効スキルのみBoolは設定値／反転、それ以外は `valueToConfigure` か0を `currentValue` に入れて更新する。 |
| `setPlayerSkillsActiveStateFromEditor(bool state)` | `playerSkillsActive` を設定したうえで `updateComponent` を呼ぶ。 |
| `updateComponent()` | `GKC_Utils.updateComponent` とシーンのダーティ更新のみを行う。 |

## 内部型

- `skillCategoryInfo`（class）
- `skillInfo`（class）
- `skillLevelInfo`（class）
- `skillTemplateCategoryInfo`（class）
- `skillTemplateInfo`（class）
