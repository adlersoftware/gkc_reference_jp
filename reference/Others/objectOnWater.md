# objectOnWater

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/objectOnWater.cs:5`

**概要**: `FloatingObject`が継承する水面オブジェクト用の基底クラスで、中身が空の`virtual`メソッドのみを定義する。

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `updateExternalForces(Vector3 newValues, bool externalForcesActiveValue)` | 本体が空で何もしない（派生クラスでの上書き前提）。 |
| `isObjectOnWaterActive()` | 常にfalseを返すだけ。 |
| `updateExternalRotationForces(float rotationAmount, Vector3 rotationAxis, Vector3 externalRotationForcePoint)` | 本体が空で何もしない。 |
| `getDensity()` | 常に-1を返すだけ。 |
| `setNewDensity(float newValue)` | 本体が空で何もしない。 |
| `addOrRemoveDensity(float newValue)` | 本体が空で何もしない。 |
| `setOriginalDensity()` | 本体が空で何もしない。 |
