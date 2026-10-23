# playerSkillsUISystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Skills System/playerSkillsUISystem.cs:8`

**概要**: スキルメニューUIを制御し、カテゴリ／スロットの表示切替、選択中スキル情報の表示、必要ポイントの消費確認とスロット解放を行う。`playerSkillsSystem` と `playerExperienceSystem` を参照して表示とポイント消費を同期する。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Locked Skill Name | `showLockedSkillName` | `bool` | true | オンにすると未解放スキルでも実際の名前を表示する。 |
| Locked Skill Name To Show | `lockedSkillNameToShow` | `string` | "???" | 未解放時にスキル名欄へ表示する代替文字列。 / 表示条件: `showLockedSkillName` がオフのとき |
| Show Locked Skill Description | `showLockedSkillDescription` | `bool` | true | オンにすると未解放スキルでも実際の説明文を表示する。 |
| Locked Skill Description To Show | `lockedSkillDescriptionToShow` | `string` | "???" | 未解放時に説明欄へ表示する代替文字列。 / 表示条件: `showLockedSkillDescription` がオフのとき |
| Use Double Press To Show Increase Skill Button Enabled | `useDoublePressToShowIncreaseSkillButtonEnabled` | `bool` | true | オンにすると同スロットの二度押しでポイント使用確認を出す。 |

### Skill UI State Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | スキルUIの処理状況をコンソールに出力する。 |

### Main Elements

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Skills Menu Panel | `skillsMenuPanel` | `GameObject` | – | スキルメニューとして開閉されるUIパネル。 / 表示条件: `showElementSettings` がオンのとき |
| Current Skill Category Name Text | `currentSkillCategoryNameText` | `Text` | – | 選択中カテゴリ名を表示するテキスト。 / 表示条件: `showElementSettings` がオンのとき |
| Current Skill Name Text | `currentSkillNameText` | `Text` | – | 選択中スキル名を表示するテキスト。 / 表示条件: `showElementSettings` がオンのとき |
| Current Skill Description Text | `currentSkillDescriptionText` | `Text` | – | 選択中スキルの説明文を表示するテキスト。 / 表示条件: `showElementSettings` がオンのとき |
| Current Skill Level Description Text | `currentSkillLevelDescriptionText` | `Text` | – | 現在のスキルレベルの説明を表示するテキスト。 / 表示条件: `showElementSettings` がオンのとき |
| Current Skill Points Text | `currentSkillPointsText` | `Text` | – | 所持スキルポイント数を表示するテキスト。 / 表示条件: `showElementSettings` がオンのとき |
| Required Skill Points Text | `requiredSkillPointsText` | `Text` | – | 次段階に必要なスキルポイントを表示するテキスト。 / 表示条件: `showElementSettings` がオンのとき |
| Confirm Use Skill Points Panel | `confirmUseSkillPointsPanel` | `RectTransform` | – | スキルポイント使用の確認を表示するパネル。 / 表示条件: `showElementSettings` がオンのとき |
| Player Experience Manager | `playerExperienceManager` | `playerExperienceSystem` | – | スキルポイント残量を管理する`playerExperienceSystem`。 / 表示条件: `showElementSettings` がオンのとき |
| Player Skills Manager | `playerSkillsManager` | `playerSkillsSystem` | – | 参照するスキル情報を提供する`playerSkillsSystem`。 / 表示条件: `showElementSettings` がオンのとき |
| Category Scroll Bar | `categoryScrollBar` | `Scrollbar` | – | カテゴリ一覧のスクロール位置を制御するバー。 / 表示条件: `showElementSettings` がオンのとき |
| Category List Content | `categoryListContent` | `RectTransform` | – | カテゴリ一覧の要素を並べるコンテナ。 / 表示条件: `showElementSettings` がオンのとき |
| Category Scroll Rect | `categoryScrollRect` | `ScrollRect` | – | カテゴリ一覧のスクロール制御を行う`ScrollRect`。 / 表示条件: `showElementSettings` がオンのとき |

### Event Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Event On Skill Menu Opened | `eventOnSkillMenuOpened` | `UnityEvent` | – | スキルメニューを開いた時に実行するイベント。 / 表示条件: `showEventSettings` がオンのとき |
| Event On Skill Menu Closed | `eventOnSkillMenuClosed` | `UnityEvent` | – | スキルメニューを閉じた時に実行するイベント。 / 表示条件: `showEventSettings` がオンのとき |
| Event On Skill Points Used | `eventOnSkillPointsUsed` | `UnityEvent` | – | ポイント消費が成功した時に実行するイベント。 / 表示条件: `showEventSettings` がオンのとき |
| Event On Not Enough Skill Points | `eventOnNotEnoughSkillPoints` | `UnityEvent` | – | ポイント不足で消費に失敗した時に実行するイベント。 / 表示条件: `showEventSettings` がオンのとき |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `skillUICategoryInfoList` | `List<skillUICategoryInfo>` | new List<skillUICategoryInfo> () | – |
| `skillsMenuOpened` | `bool` | – | – |
| `currentSkillUICategoryInfo` | `skillUICategoryInfo` | – | – |
| `currentSkillUIInfo` | `skillUIInfo` | – | – |
| `previousSkillUIInfo` | `skillUIInfo` | – | – |
| `currentSkillSlotPanelInfo` | `skillSlotPanelInfo` | – | – |
| `skillSlotsName` | `string` | "Skill Slot " | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `updateSkillSlots()` | 各スロットのロック／解放／アクティブ表示を切り替え、レベル使用時は現在レベルと総数の文字も更新する。 |
| `openOrCloseSkillsMenu(bool state)` | `skillsMenuOpened` とパネル表示を切り替え、開く際はスロット更新・先頭カテゴリ選択・スクロール初期化・オープンイベントを行う。 |
| `checkSkillPressed(GameObject skillSlot)` | 選択スロットの情報と押下アイコンを更新し、再押下か設定次第でポイント使用確認パネルを表示する（完了・未解放なら中断）。 |
| `updateCurrentSkillInfo()` | 選択中スキルのカテゴリ名・名前・説明・レベル説明・所持／必要ポイントをロック表示とローカライズを考慮して更新する。 |
| `confirmUseSkillPointsOnCurrentSkillSlot()` | 選択スキルにポイントを消費してスロット表示と解放対象を更新し、成否で `eventOnSkillPointsUsed` か不足イベントを発火する。 |
| `cancelUseSkillPointsOnCurrentSkillSlot()` | ポイント使用確認パネルを非表示にするだけ。 |
| `unlockSkillSlot(int skillSlotIndex)` | 指定スロットを解放表示に変え、`unlockSkillSlotByName` でデータ側の `skillUnlocked` も true にする。 |
| `checkSkillCategoryPressed(GameObject categorySlot)` | 押したカテゴリのパネルだけを表示し、その先頭スキルを選択状態にして確認パネルを閉じる。 |
| `resetScroll(Scrollbar scrollBarToReset)` | 2フレーム待ってから `scrollBarToReset.value` を1にするコルーチンを開始する。 |
| `resetScrollRectTransfrom(RectTransform listContent, ScrollRect scrollRectToReset)` | レイアウトを再構築して2フレーム待ち、`verticalNormalizedPosition` を1に戻すコルーチンを開始する。 |
| `assignSkillsToSlots()` | 各UIスロットへカテゴリ名・スキル名から `categorySkillIndex` と `skillIndex` を割り当てて更新する（未発見なら -1）。 |
| `assignSkillsNamesToSlots(int listIndex)` | 指定カテゴリの各スロットGameObject名を `skillSlotsName` + スキル名に設定して更新する。 |
| `activateAllSkills(int listIndex)` | 指定カテゴリを選択し、各スロットを押下扱いにして `confirmUseSkillPointsOnCurrentSkillSlot` を順に実行する。 |
| `updateComponent()` | `GKC_Utils.updateComponent` とシーンのダーティ更新のみを行う。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnSkillMenuOpened` | `UnityEvent` | – |
| `eventOnSkillMenuClosed` | `UnityEvent` | – |
| `eventOnSkillPointsUsed` | `UnityEvent` | – |
| `eventOnNotEnoughSkillPoints` | `UnityEvent` | – |

## 内部型

- `skillUICategoryInfo`（class）
- `skillUIInfo`（class）
