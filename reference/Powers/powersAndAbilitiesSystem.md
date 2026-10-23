# powersAndAbilitiesSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Powers/powersAndAbilitiesSystem.cs:6`

**概要**: パワー名と有効/無効イベントを対応付ける汎用システム。名前を指定してイベントを呼び出す。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `powerInfoList` | `List<powerInfo>` | new List<powerInfo> () | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `disableGeneralPower(string powerName)` | 名前が一致するパワーの無効化イベントを発火して終了する。 |
| `enableGeneralPower(string powerName)` | 名前が一致するパワーの有効化イベントを発火して終了する。 |
| `updateComponent()` | `GKC_Utils.updateComponent`でこのコンポーネントを更新するだけ。 |

## 内部型

- `powerInfo`（class）
