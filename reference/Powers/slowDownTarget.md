# slowDownTarget

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `projectileSystem`
- **ソース**: `Powers/slowDownTarget.cs:5`

## インスペクター設定

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Character State Affected Name | `characterStateAffectedName` | `string` | "Character Freeze Velocity" | – |
| Slow Down Duration | `slowDownDuration` | `float` | 6 | – |
| Slow Value | `slowValue` | `float` | 0.2f | Range (0, 1) |
| Use Slow Object Color | `useSlowObjectColor` | `bool` | true | – |
| Slow Objects Color | `slowObjectsColor` | `Color` | Color.blue | – |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`resetProjectile()`

</details>
