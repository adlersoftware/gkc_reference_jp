# pixelCameraEffect

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `cameraEffect`
- **ソース**: `Camera/Camera Effect/pixelCameraEffect.cs:5`

**概要**: 画面をブロック状にピクセル化するポストエフェクト。`BlockCount` とカメラのアスペクト比からブロック数を算出してシェーダに渡し、ブリットする。

## インスペクター設定

### （セクションなし）

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Main Shader | `mainShader` | `Shader` | – | – |
| Use Effect Color | `useEffectColor` | `bool` | – | – |
| Effect Color | `effectColor` | `Color` | Color.white | – |
| Block Count Name | `blockCountName` | `string` | "BlockCount" | – |
| Block Size Name | `blockSizeName` | `string` | "BlockSize" | – |
| Color Name | `colorName` | `string` | "_TintColor" | – |
| Block Count | `BlockCount` | `float` | 128 | Range (64.0f, 1024.0f) |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setMaterial()` | `mainMaterial` が未生成なら `mainShader` から生成し、`HideAndDontSave` にするだけ。 |

<details><summary>Unity コールバック / override（通常は外部から呼ばない）</summary>

`renderEffect(RenderTexture source, RenderTexture destination, Camera mainCamera)`

</details>
