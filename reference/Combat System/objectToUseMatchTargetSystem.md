# objectToUseMatchTargetSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Combat System/objectToUseMatchTargetSystem.cs:5`

**概要**: トリガー内に入ったキャラクタを`matchPlayerToTargetSystem`の周囲リストへ登録/解除する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Match Target System Enabled | `matchTargetSystemEnabled` | `bool` | true | – |
| Check Object Tag | `checkObjectTag` | `bool` | – | – |
| Tags To Locate | `tagsToLocate` | `List<string>` | new List<string> () | – |
| Check Object Layer | `checkObjectLayer` | `bool` | – | – |
| Layer To Check Targets | `layerToCheckTargets` | `LayerMask` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Character Transform | `mainCharacterTransform` | `Transform` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `removeAllMatchTargetList()` | 登録済みの全`matchPlayerToTargetSystem`から自身を周囲リストから外し、内部リストを空にする。 |
