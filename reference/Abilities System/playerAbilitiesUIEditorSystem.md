# playerAbilitiesUIEditorSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Abilities System/playerAbilitiesUIEditorSystem.cs:11`

**概要**: アビリティUIの編集画面を開閉し、ホイールとスロット一覧を更新するUIコンポーネント。スロット生成やスクロール位置のリセットも行う。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Abilities Wheel Scale | `abilitiesWheelScale` | `float` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Abilities UI Editor Active | `abilitiesUIEditorActive` | `bool` | – | – |
| Moving Slot From Full Abilities Panel | `movingSlotFromFullAbilitiesPanel` | `bool` | – | – |
| Moving Slot From Current Abilities Panel | `movingSlotFromCurrentAbilitiesPanel` | `bool` | – | – |

### UI Elements

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Abilities UI Editor Object | `abilitiesUIEditorObject` | `GameObject` | – | – |
| Full Abilities UI Editor List Scroll Rect | `fullAbilitiesUIEditorListScrollRect` | `ScrollRect` | – | – |
| Full Abilities UI Editor Scrollbar | `fullAbilitiesUIEditorScrollbar` | `Scrollbar` | – | – |
| Full Abilities UI Editor Content | `fullAbilitiesUIEditorContent` | `Transform` | – | – |
| Current Wheel Abilities Panel Background Transform | `currentWheelAbilitiesPanelBackgroundTransform` | `Transform` | – | – |
| Current Grid Abilities Panel Background Transform | `currentGridAbilitiesPanelBackgroundTransform` | `Transform` | – | – |
| Full Abilities Panel Transform | `fullAbilitiesPanelTransform` | `Transform` | – | – |
| Main Abilities Wheel Transform | `mainAbilitiesWheelTransform` | `Transform` | – | – |
| Original Abilities Wheel Parent | `originalAbilitiesWheelParent` | `Transform` | – | – |
| Abilities Wheel Position | `abilitiesWheelPosition` | `Transform` | – | – |
| Ability List Element | `abilityListElement` | `GameObject` | – | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Ability Slot Info List | `abilitySlotInfoList` | `List<playerAbilitiesUISystem.abilitySlotInfo>` | new List<playerAbilitiesUISystem.abil… | – |
| Temporal Ability Slot Info List | `temporalAbilitySlotInfoList` | `List<playerAbilitiesUISystem.abilitySlotInfo>` | new List<playerAbilitiesUISystem.abil… | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Player Abilities UI System | `mainPlayerAbilitiesUISystem` | `playerAbilitiesUISystem` | – | – |
| Main Player Abilities System | `mainPlayerAbilitiesSystem` | `playerAbilitiesSystem` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `openOrCloseAbilitiesUIEditor(bool state)` | 編集UIの表示を `state` に合わせて切り替え、開く時はホイール位置やスロット表示・スクロールを整える。 |
| `updateAbilitiesUIEditorValues()` | 初回はアビリティ数だけスロット要素を生成し、その後は各有効状態に応じてスロット表示を更新する。 |
| `resetScroll(Scrollbar scrollBarToReset)` | 2フレーム待ってから指定スクロールバーの値を1にするコルーチンを開始する。 |
| `resetInventorySlotsRectTransform()` | レイアウト再構築後に2フレーム待ってスクロール位置を先頭へ戻すコルーチンを開始する。 |
