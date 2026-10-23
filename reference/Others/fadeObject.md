# fadeObject

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/fadeObject.cs:4`

**概要**: レンダラーのアルファを下げてオブジェクトを消す演出を行い、プール返却にも対応する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Vanish Enabled | `vanishEnabled` | `bool` | true | – |
| Vanish Speed | `vanishSpeed` | `float` | – | – |
| Mesh Renderer | `meshRenderer` | `Renderer` | – | – |
| Vanish At Once | `vanishAtOnce` | `bool` | – | – |
| Delay To Vanish At Once | `delayToVanishAtOnce` | `float` | – | – |
| Send Object To Pool System To Disable | `sendObjectToPoolSystemToDisable` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `activeVanish(float newSpeed)` | `newSpeed`が0より大きければ`vanishSpeed`を更新し、フェードか遅延削除で消す（プール設定時はDespawn）。 |
