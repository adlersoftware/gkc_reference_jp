# vehicleBuilder

- **種別**: MonoBehaviour（コンポーネント）
- **継承 / 実装**: `MonoBehaviour`
- **ソース**: `Vehicles/vehicleBuilder.cs:6`

**概要**: エディタ上で車両メッシュの差し替え、設定イベントの実行、シーンへの配置を行うビルダー。パーツのインスタンス化とHUDマネージャへの登録をまとめて行う。

## インスペクター設定

カスタムエディタで表示順・表示名が制御されています。

### Main Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Vehicle Name | `vehicleName` | `string` | – | ビルド時に車両名として各オブジェクトへ設定する文字列。 |
| Layer To Place Vehicle | `layerToPlaceVehicle` | `LayerMask` | – | 配置位置を決めるレイキャストに使うレイヤー。 |
| Place Vehicle Offset | `placeVehicleOffset` | `float` | 2 | 配置位置を接地ポイントから上へ持ち上げる距離。 |
| Vehicle | `vehicle` | `GameObject` | – | ビルド対象となる車両のルートオブジェクト。 |
| Vehicle Camera | `vehicleCamera` | `GameObject` | – | 名前を設定する車両カメラのオブジェクト。 |
| Main Vehicle HUD Manager | `mainVehicleHUDManager` | `vehicleHUDManager` | – | 車両名とパーツ情報を登録するHUD管理コンポーネント。 |
| Vehicle View Transform | `vehicleViewTransform` | `Transform` | – | エディタ視点を合わせる基準となるトランスフォーム。 |

### Explanation

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Build Vehicle Explanation | `buildVehicleExplanation` | `string` | "IMPORTANT: once you create a new veh… | ビルド手順の注意事項を表示する説明用テキスト。 / TextArea (5, 15) |

### Gizmo Settings

| ラベル | フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- | --- |
| Show Gizmo | `showGizmo` | `bool` | – | オンにすると車両パーツ位置に球ギズモを表示する。 |
| Show Gizmo Label | `showGizmoLabel` | `bool` | – | オンにするとパーツ名ラベルをシーンビューに表示する。 |
| Gizmo Label Color | `gizmoLabelColor` | `Color` | Color.black | シーンビューに表示するラベルの文字色。 |
| Gizmo Radius | `gizmoRadius` | `float` | – | パーツ位置に描く球ギズモの半径。 |
| Use Handle | `useHandle` | `bool` | – | オンにするとパーツをシーンビューで移動・回転できる。 |

### その他（コードから設定する項目など）

| フィールド | 型 | 既定値 | 補足 |
| --- | --- | --- | --- |
| `vehiclePartInfoList` | `List<vehiclePartInfo>` | new List<vehiclePartInfo> () | – |
| `vehicleSettingsInfoList` | `List<vehicleSettingsInfo>` | new List<vehicleSettingsInfo> () | – |
| `placeVehicleInScene` | `bool` | – | – |

## 公開メソッド

| シグネチャ | 説明 |
| --- | --- |
| `buildVehicle()` | パーツ調整、ビルド完了処理、テンポラリのリセット、設定イベント適用を順に実行し、シーンを更新する。 |
| `adjustVehicleParts()` | 各有効パーツのメッシュを差し替え／削除し、有効・無効に応じたイベントを発火する。 |
| `adjustVehicleSettings()` | 各設定項目のbool／floatイベントを、設定値で順に呼び出す。 |
| `adjustVehicleSettingsFromEditor()` | エディタから`adjustVehicleSettings`を呼ぶだけ。 |
| `completeVehicleBuild()` | HUDマネージャ・車両・カメラ・親オブジェクトの名前を設定し、パーツを登録して必要ならカメラ前へ配置する。 |
| `setVehicleName(string newValue)` | `vehicleName`を`newValue`にするだけ。 |
| `resetTemporalVehicleParts()` | 各パーツのテンポラリメッシュ参照・生成フラグ・オフセットを初期化する。 |
| `removeTemporalVehicleParts()` | 生成したテンポラリメッシュを破棄し、元のメッシュと追加パーツを再表示して設定を戻す。 |
| `getMeshParentTransformValues()` | 各パーツのメッシュ親の初期ローカル位置・角度を記録する。 |
| `placeVehicleInCameraPosition()` | エディタカメラの前方へ`layerToPlaceVehicle`でレイキャストし、当たった地点の上に車両を移動する。 |
| `alignViewWithVehicleCameraPosition()` | `vehicleViewTransform`を`setEditorCameraPosition`に渡すだけ。 |
| `setEditorCameraPosition(Transform transformToUse)` | `GKC_Utils.alignViewToObject`で指定トランスフォームへエディタビューを向けるだけ。 |

## 内部型

- `vehicleSettingsInfo`（class）
- `vehiclePartInfo`（class）
