# shakeCharacterBodyPartSystem

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Others/shakeCharacterBodyPartSystem.cs:5`

**概要**: 人型ボーンの1つを一定時間揺らす演出を行い、対象ボーンを名前かTransformで指定できる。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Shake Animation Enabled | `shakeAnimationEnabled` | `bool` | true | – |
| Shake Rotation Speed | `shakeRotationSpeed` | `Vector3` | – | – |
| Shake Rotation Amount | `shakeRotationAmount` | `Vector3` | – | – |
| Wait Time To Reset Shake | `waitTimeToResetShake` | `float` | – | – |
| Reset Shake Speed | `resetShakeSpeed` | `float` | – | – |
| Regular Shake Duration | `regularShakeDuration` | `float` | – | – |
| Max Time To Stop Shake | `maxTimeToStopShake` | `float` | 10 | – |

### Transform List Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Store Transform List On Start | `storeTransformListOnStart` | `bool` | – | – |
| Character Body Part Info List | `characterBodyPartInfoList` | `List<characterBodyPartInfo>` | new List<characterBodyPartInfo> () | – |

### Debug

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Debug Print | `showDebugPrint` | `bool` | – | – |
| Transform List Stored | `transformListStored` | `bool` | – | – |
| Shake Animation Active | `shakeAnimationActive` | `bool` | – | – |
| Current Body Part Name | `currentBodyPartName` | `string` | – | – |
| Use Custom Duration | `useCustomDuration` | `bool` | – | – |
| Custom Duration | `customDuration` | `float` | – | – |
| Current Rotation Euler | `currentRotationEuler` | `Vector3` | – | – |

### Components

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Animator | `animator` | `Animator` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `setShakePartCustomDuration(float newDuration)` | `customDuration`に`newDuration`を入れ、0以外なら`useCustomDuration`を`true`にする。 |
| `activatShakeAnimationXSecondsFromEditor()` | `currentBodyPartName`を使って名前指定の揺れ開始処理を呼ぶ。 |
| `activatShakeAnimationXSecondsByName(string bodyPartName)` | 名前一致のボーンを探して揺れを開始し、見つからなければデバッグ表示だけ行う。 |
| `activatShakeAnimationXSecondsByTransform(Transform bodyPartTransform)` | Transform一致のボーンを探して揺れを開始し、対象名をコンソールに出力する。 |
| `storeCharacterBones()` | `animator`から頭・胴・手足などのボーンを取得してリストを作り直し、null要素を除去する。 |

## 内部型

- `characterBodyPartInfo`（class）
