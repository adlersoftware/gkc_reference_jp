# slowObjectsColor

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Powers/slowObjectsColor.cs:5`

**概要**: `slowObject`から開始され、対象の速度を低下させながらレンダラーを`slowColor`へ補間し、時間経過で元の色と速度に戻して自己破棄する。

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Slow Color | `slowColor` | `Color` | – | – |
| Change To Slow | `changeToSlow` | `bool` | true | – |
| Change To Normal | `changeToNormal` | `bool` | – | – |
| Slow Down Duration | `slowDownDuration` | `float` | – | – |
| Timer | `timer` | `float` | 0 | – |
| Set Normal Velocity String | `setNormalVelocityString` | `string` | "setNormalVelocity" | – |
| Set Reduced Velocity String | `setReducedVelocityString` | `string` | "setReducedVelocity" | – |
| Set Can Move AI State String | `setCanMoveAIStateString` | `string` | "setCanMoveAIState" | – |
| Set Override Animation Speed Active State String | `setOverrideAnimationSpeedActiveStateString` | `string` | "setOverrideAnimationSpeedActiveState" | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Renderer Parts | `rendererParts` | `List<Renderer>` | new List<Renderer> () | – |
| Original Color | `originalColor` | `List<Color>` | new List<Color> () | – |
| Transistion Color | `transistionColor` | `List<Color>` | new List<Color> () | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `startSlowObject(bool useSlowObjectColorValue, Color newSlowColor, float newSlowValue, float newSlowDownDuration, slowObject newSlowObjectComponent)` | 各パラメータを保存し、`slowObject`のカスタム速度を反映して低下メッセージを送り、対象レンダラーの元色を記録する。 |
