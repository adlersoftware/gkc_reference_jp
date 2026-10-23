# projectilesOnCharacterBodyManager

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Weapons/projectilesOnCharacterBodyManager.cs:5`

**概要**: キャラの体に刺さった投射物を一定時間後に1本ずつ消していく管理コンポーネント。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Remove Projectiles Enabled | `removeProjectilesEnabled` | `bool` | true | – |
| Time To Remove Projectiles | `timeToRemoveProjectiles` | `float` | 5 | – |
| Wait Time Between Projectile Removing | `waitTimeBetweenProjectileRemoving` | `float` | 2 | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `addProjectileToCharacterBody(GameObject newProjectileObject)` | 削除が有効なら未登録の投射物をリストに加え、待ち時間をリセットして削除コルーチンを開始する。 |
| `stopRemoveProjectilesCoroutine()` | `removeCoroutine`があれば停止するだけ。 |
