# setHealthCustomWeakSpotID

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Health/setHealthCustomWeakSpotID.cs:6`

**概要**: 名前付きのカスタム状態ごとに、弱点の部位HP ID・被弾時送信関数・体力オンスポット設定を`health`へまとめて適用するコンポーネント。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Health Custom Weak Spot Enabled | `healthCustomWeakSpotEnabled` | `bool` | true | – |
| Custom State Info List | `customStateInfoList` | `List<customStateInfo>` | new List<customStateInfo> () | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Health Custom Weak Spot Ignore Active | `healthCustomWeakSpotIgnoreActive` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Health | `mainHealth` | `health` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setHealthCustomWeakSpotIDByName(string newName)` | `newName`の有効なカスタム状態を探し、各弱点へ部位HPのID・被弾時関数・オンスポット設定を一括適用する。 |
| `enableOrDisableCustomStateInfo(bool state, string newName)` | `newName`に一致するカスタム状態の`customStateEnabled`を`state`にするだけ。 |
| `enableCustomStateInfo(string newName)` | `enableOrDisableCustomStateInfo(true, newName)`を呼ぶだけ。 |
| `disableCustomStateInfo(string newName)` | `enableOrDisableCustomStateInfo(false, newName)`を呼ぶだけ。 |
| `setHealthCustomWeakSpotEnabledState(bool state)` | `healthCustomWeakSpotEnabled`を`state`にするだけ。 |
| `setHealthCustomWeakSpotIgnoreActiveState(bool state)` | `healthCustomWeakSpotIgnoreActive`を`state`にするだけ。 |
| `setHealthCustomWeakSpotEnabledStateFromEditor(bool state)` | 設定後に`updateComponent`でシーンをダーティ更新するだけ。 |
| `enableCustomStateInfoFromEditor(string newName)` | 有効化した後`updateComponent`でシーンをダーティ更新するだけ。 |
| `disableCustomStateInfoFromEditor(string newName)` | 無効化した後`updateComponent`でシーンをダーティ更新するだけ。 |

## 内部型

- `customStateInfo`（class）
- `healthCustomWeakSpotInfo`（class）
