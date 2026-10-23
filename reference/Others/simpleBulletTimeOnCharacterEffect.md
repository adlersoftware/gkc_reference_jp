# simpleBulletTimeOnCharacterEffect

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/simpleBulletTimeOnCharacterEffect.cs:5`

**概要**: キャラクターの移動速度とタイムスケールを下げるスローモーション演出と、メッシュの残像生成を行う。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Effect Enabled | `effectEnabled` | `bool` | true | – |
| Character Animation Speed | `characterAnimationSpeed` | `float` | 1.6f | – |
| Set New Time Scale | `setNewTimeScale` | `bool` | – | – |
| New Time Scale | `newTimeScale` | `float` | – | – |
| Use Model Mesh Trail Effect Enabled | `useModelMeshTrailEffectEnabled` | `bool` | true | – |
| Model Mesh Trail Refresh Rate | `modelMeshTrailRefreshRate` | `float` | 0.3f | – |
| Mesh Trail Material | `meshTrailMaterial` | `Material` | – | – |
| Mesh Trail Max Number | `meshTrailMaxNumber` | `int` | 50 | – |
| Number Of Model Meshes | `numberOfModelMeshes` | `int` | 7 | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Effect Active | `effectActive` | `bool` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Player Controller | `mainPlayerController` | `playerController` | – | – |
| Player Transform | `playerTransform` | `Transform` | – | – |
| Main Time Bullet | `mainTimeBullet` | `timeBullet` | – | – |
| Main Skinned Mesh Renderer | `mainSkinnedMeshRenderer` | `List<SkinnedMeshRenderer>` | new List<SkinnedMeshRenderer> () | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `stopUpdateCoroutine()` | `updateCoroutine`があれば停止するだけ。 |
| `enableOrDisableEffect(bool state)` | 有効時、`state`に応じて移動速度とタイムバレットを切り替え、残像コルーチンの開始/停止と生成済み残像の破棄を行う。 |
