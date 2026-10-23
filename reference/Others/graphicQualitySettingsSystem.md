# graphicQualitySettingsSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/graphicQualitySettingsSystem.cs:6`

**概要**: 画質レベル・解像度・ウィンドウ表示・アンチエイリアスを、設定リストの名前指定で切り替える。

**公式ドキュメント抜粋**（[Graphic Quality Settings System](../../docs/player-controller-components/elements-used-by-other-components/graphic-quality-settings-system.md)）

> 

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Graphic Settings Enabled | `graphicSettingsEnabled` | `bool` | true | – |
| Can Change Game Windowed State Enabled | `canChangeGameWindowedStateEnabled` | `bool` | true | – |
| Can Change Anti Aliasing Enabled | `canChangeAntiAliasingEnabled` | `bool` | true | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Current Setting Index | `currentSettingIndex` | `int` | – | – |
| Current Resolution Index | `currentResolutionIndex` | `int` | – | – |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |

### Quality Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Quality Setting Info List | `qualitySettingInfoList` | `List<qualitySettingInfo>` | new List<qualitySettingInfo> () | – |

### Resolution Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Resolution Setting Info List | `resolutionSettingInfoList` | `List<resolutionSettingInfo>` | new List<resolutionSettingInfo> () | – |

### Events Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Use Events On Resolution Change | `useEventsOnResolutionChange` | `bool` | – | – |
| Event On Resolution Change | `eventOnResolutionChange` | `UnityEvent` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setGraphicQualityValue(string newValue)` | 名前一致の画質項目を現在設定にして`QualitySettings.SetQualityLevel`を呼び、項目のイベントを発火する。 |
| `setScreenResolution(string newValue)` | 名前一致の解像度項目を現在設定にして`Screen.SetResolution`を呼び、変更イベントを発火する。 |
| `setGameWindowedState(bool state)` | 現在の解像度設定を維持したまま、`Screen.fullScreen`を`state`に合わせて再設定する。 |
| `setAntiAliasingState(string valueString)` | `valueString`を整数へ変換できた時だけ`setAntiAliasingState(int)`へ渡す。 |
| `setAntiAliasingState(int newValue)` | `canChangeAntiAliasingEnabled`が`true`なら`QualitySettings.antiAliasing`を`newValue`に設定する。 |

## Unity イベント

| フィールド | 型 | 説明 |
| --- | --- | --- |
| `eventOnResolutionChange` | `UnityEvent` | – |

## 内部型

- `qualitySettingInfo`（class）
- `resolutionSettingInfo`（class）
