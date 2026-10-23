# gravityObjectManager

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Gravity/gravityObjectManager.cs:5`

**概要**: 重力系コンポーネントの共通インターフェースとなる基底クラス。各メソッドは既定値(空・false・`null`)を返すだけで、派生クラスが上書きする。

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `onGroundOrOnAir(bool state)` | 本体が空で何もしない。 |
| `isSearchingSurface()` | 常に`false`を返すダミー実装。 |
| `getCurrentNormal()` | 常に`Vector3.zero`を返すダミー実装。 |
| `getGravityCenter()` | 常に`null`を返すダミー実装。 |
| `isPlayerSearchingGravitySurface()` | 常に`false`を返すダミー実装。 |
| `isUsingRegularGravity()` | 常に`true`を返すダミー実装。 |
