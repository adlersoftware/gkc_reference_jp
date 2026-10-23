# meleeUISystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Combat System/Melee Combat System/meleeUISystem.cs:7`

**概要**: 近接武器の名前とアイコンを表示するUIパネルの表示切替とテキスト更新を担当する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Melee UI Enabled | `meleeUIEnabled` | `bool` | true | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Melee UI Active | `meleeUIActive` | `bool` | – | – |
| Current Melee Weapon Name | `currentMeleeWeaponName` | `string` | – | – |

### UI Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Melee Weapon Text | `meleeWeaponText` | `Text` | – | – |
| Melee Weapon Image | `meleeWeaponImage` | `RawImage` | – | – |
| Melee Panel Game Object | `meleePanelGameObject` | `GameObject` | – | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Events On Melee Panel State Change | `useEventsOnMeleePanelStateChange` | `bool` | – | – |
| Event On Enable Melee Panel | `eventOnEnableMeleePanel` | `UnityEvent` | – | – |
| Event On Disable Melee Panel | `eventOnDisableMeleePanel` | `UnityEvent` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setCurrentMeleeWeaponName(string newName)` | 武器名を保持し、ローカライズマネージャ経由のテキストを`meleeWeaponText`へ表示する。 |
| `setCurrrentMeleeWeaponIcon(Texture newIcon)` | `meleeWeaponImage`のテクスチャを指定アイコンに差し替えるだけ。 |
| `enableOrDisableMeleeUI(bool state)` | UI無効時や状態が同じなら何もせず、パネル表示を切り替えて有効/無効イベントを発火する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnEnableMeleePanel` | `UnityEvent` | – |
| `eventOnDisableMeleePanel` | `UnityEvent` | – |
