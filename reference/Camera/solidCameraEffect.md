# solidCameraEffect

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `cameraEffect`
- **ソース**: `Camera/Camera Effect/solidCameraEffect.cs:5`

**概要**: テクスチャを画面全体に敷くソリッド系のポストエフェクト。ブロック数・色・テクスチャをシェーダに渡してブリットする。

## インスペクター設定

### （セクションなし）

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Shader | `mainShader` | `Shader` | – | – |
| Regular Color | `regularColor` | `Color` | Color.white | – |
| Use Effect Color | `useEffectColor` | `bool` | – | – |
| Effect Color | `effectColor` | `Color` | Color.white | – |
| Main Texture | `mainTexture` | `Texture2D` | – | – |
| Block Count Name | `blockCountName` | `string` | "BlockCount" | – |
| Block Size Name | `blockSizeName` | `string` | "BlockSize" | – |
| Tint Color Name | `tintColorName` | `string` | "_TintColor" | – |
| Spr Tex Name | `sprTexName` | `string` | "_SprTex" | – |
| Color Name | `colorName` | `string` | "_Color" | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setMaterial()` | `mainMaterial` が未生成なら `mainShader` から生成し、`HideAndDontSave` にするだけ。 |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`renderEffect(RenderTexture source, RenderTexture destination, Camera mainCamera)`

</details>
