# spiderControllerInterface

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/spiderControllerInterface.cs:5`

**概要**: クモ型コントローラ（spider controller）とカメラ制御のやり取りを定義する、中身が空の`virtual`メソッドのみの基底クラス。

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setGroundcheck(bool b)` | 本体が空で何もしない（派生クラスでの上書き前提）。 |
| `walk(Vector3 direction)` | 本体が空で何もしない。 |
| `run(Vector3 direction)` | 本体が空で何もしない。 |
| `turn(Vector3 goalForward)` | 本体が空で何もしない。 |
| `getGroundNormal()` | 常に`Vector3.zero`を返すだけで、上書き用の`virtual`メソッド。 |
| `getCamTargetPosition()` | 常に`Vector3.zero`を返すだけ。 |
| `getCamTargetRotation()` | 常に`Quaternion.identity`を返すだけ。 |
| `setTargetPosition(Vector3 pos)` | 本体が空で何もしない。 |
| `setTargetRotation(Quaternion rot)` | 本体が空で何もしない。 |
| `getCameraTarget()` | 常に`null`を返すだけ。 |
