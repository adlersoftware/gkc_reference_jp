# projectileImpactSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Weapons/projectileImpactSystem.cs:6`

**概要**: 投射物の着弾地点に音とデカールを出し、一定時間後の破棄やプール返却をまとめて行う小さなシステム。

## インスペクター設定

### （セクションなし）

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Audio Source | `mainAudioSource` | `AudioSource` | – | – |
| Main Destroy Game Object | `mainDestroyGameObject` | `destroyGameObject` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `activateImpactElements(Vector3 newPosition, AudioElement impactSoundEffect)` | 位置を`newPosition`へ移し、音の長さで破棄タイマーを設定し、音源ピッチを整えて再生してデカールの親を設定する。 |
| `changeDestroyForSetActiveFunction(bool state)` | `mainDestroyGameObject`の破棄か非アクティブ化かの設定を`state`にするだけ。 |
| `setSendObjectToPoolSystemToDisableState(bool state)` | `mainDestroyGameObject`へプール返却で無効化する設定を渡すだけ。 |
